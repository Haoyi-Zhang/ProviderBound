"""Read-only native-record, exact-answer and measurement consumer."""
from pathlib import Path
import argparse
import lzma
import hashlib
import itertools
import json
import math
import statistics
import sys
from triple_study import ROOT, census, direct_owners, merged, encoded, require
from checker import verify


def load_records():
    directory = ROOT/'results/triple-study'
    summary = json.loads((directory/'summary.json').read_text(encoding='utf-8'))
    records = json.loads(lzma.decompress((directory/'records.json.xz').read_bytes()))
    return summary, records


def validate(summary, records):
    expected_bindings = ('scripts/triple_study.py','src/producer.py','src/checker.py',
                         'src/archive_producer.py','src/archive_checker.py','inputs/public/providers.csv')
    require(set(summary['source_bindings']) == set(expected_bindings), 'Source binding inventory')
    for name in expected_bindings:
        require(summary['source_bindings'][name] == hashlib.sha256((ROOT/name).read_bytes()).hexdigest(),
                'Study source changed: '+name)
    triples, maps = census()
    orders = list(itertools.permutations(range(3)))
    expected = {(t+1,order,schema) for t in range(4) for order in orders for schema in ('jar','package')}
    require(len(records)==48 and len(summary['timings'])==48, 'Study record inventory')
    seen = set()
    derived = []
    cert_sizes = {}
    def record_key(record):
        order = record['order']
        require(type(record['triple']) is int and 1<=record['triple']<=4 and
                type(order) is list and len(order)==3 and
                all(type(x) is int for x in order) and sorted(order)==[0,1,2] and
                type(record['label_schema']) is str, 'Native row identity types')
        return record['triple'],tuple(order),record['label_schema']
    for t, triple in enumerate(triples):
        derived.append({'triple':t+1,'archives':[row['archive'] for row in triple],
            'package_labels':sorted({row['package'] for row in triple}), 'ant_builds':6,
            'region_observations':0,'per_jar_narrowings':0,'per_package_narrowings':0,'oracle_mismatches':0})
    for record in records:
        key = record_key(record)
        require(key in expected and key not in seen, 'Duplicate/unknown labelled native output')
        seen.add(key)
        t, order, schema = key
        triple = triples[t-1]
        names = [row['archive'] for row in triple]
        actual = merged(maps,names,order)
        expected_entries = {name:hashlib.sha256(data).hexdigest() for name,data in sorted(actual.items())}
        require(record['native_entries']==expected_entries, 'Native member identities differ')
        labels = ['lib:'+row['archive'] if schema=='jar' else 'pkg:'+row['package'] for row in triple]
        rows = []
        for name in sorted(actual):
            present = [i for i in range(3) if name in maps[names[i]]]
            good = [i for i in present if maps[names[i]][name]==actual[name]]
            rows.append({'key':name,'present':present,'good':good})
        graph = {'kind':'graph','owners':labels,'before':[],'rows':rows}
        require(graph==record['graph'], 'Native graph differs from retained inputs')
        answer = verify(graph,record['certificate'])
        reference = direct_owners(graph)
        require(answer==record['answer'] and reference==record['direct_owners'], 'Stored answer differs')
        owners = {row['key']:row['owners'] for row in answer['regions']}
        require(owners==reference, 'Literal six-order reference differs')
        narrowed = sum(set(owners[row['key']]) < {labels[i] for i in row['good']} for row in rows)
        require(type(record['global_narrowings']) is int and narrowed==record['global_narrowings'],
                'Native narrowing count')
        derived[t-1]['per_jar_narrowings' if schema=='jar' else 'per_package_narrowings'] += narrowed
        if schema=='jar':
            derived[t-1]['region_observations'] += len(rows)
        cert_sizes[key] = len(encoded(record['certificate']))
    require(seen==expected, 'Missing labelled native output')
    semantic = {'provider_archives':43,'three_way_collision_triples':4,'native_ant_builds':24,
        'labelled_output_models':48,'rows':derived,'certificate_oracle_mismatches':0,
        'archive_adapter_mismatches':0,'first_winner_content_mismatches':0}
    # Canonical serialized comparison distinguishes Boolean/real count substitutions.
    require(encoded(semantic)==encoded(summary['semantic']), 'Three-provider summary differs')
    seen = set()
    for record in summary['timings']:
        key = record_key(record)
        require(key in expected and key not in seen, 'Timing row inventory')
        seen.add(key)
        require(type(record['certificate_bytes']) is int and record['certificate_bytes']==cert_sizes[key],
                'Certificate size differs')
        for phase in ('producer','checker','direct_six_order'):
            item = record[phase]
            samples = item['seconds']
            require(type(samples) is list and len(samples)==5 and
                    all(type(x) is float and math.isfinite(x) and x>0 for x in samples),
                    'Five actual finite positive timed samples required')
            require(all(type(item[field]) is float and math.isfinite(item[field])
                        for field in ('median_seconds','minimum_seconds','maximum_seconds')) and
                    item['median_seconds']==statistics.median(samples) and
                    item['minimum_seconds']==min(samples) and item['maximum_seconds']==max(samples),
                    'Timing aggregate differs')
            peak = item['python_peak_allocated_bytes']
            require(type(peak) is int and peak>=0, 'Python allocation peak')
    require(seen==expected, 'Missing timing rows')
    return derived


def tables(summary, records):
    rows = validate(summary,records)
    first = [r'\begin{tabular}{lrrrrr}',r'\toprule',
             r'Triple & Pkgs & Regions & JAR refin. & Pkg refin. & Cert. KiB \\',r'\midrule']
    for row,name in zip(rows,('Batik','Flow/Layout/XML','Mail','SAC/XML APIs')):
        sizes = [item['certificate_bytes']/1024 for item in summary['timings'] if item['triple']==row['triple']]
        first.append(f"{name} & {len(row['package_labels'])} & {row['region_observations']:,} & "
                     f"{row['per_jar_narrowings']} & {row['per_package_narrowings']} & "
                     f"{statistics.median(sizes):.1f}"+r' \\')
    first.extend([r'\bottomrule',r'\end{tabular}',''])
    second = [r'\begin{tabular}{lrr}',r'\toprule',
              r'Loaded-graph phase & Median ms & Python alloc. KiB \\',r'\midrule']
    for key,name in (('producer','Producer'),('checker','Independent replay'),('direct_six_order','Six-order direct solver')):
        ms = statistics.median(item[key]['median_seconds']*1000 for item in summary['timings'])
        peak = statistics.median(item[key]['python_peak_allocated_bytes']/1024 for item in summary['timings'])
        second.append(f'{name} & {ms:.3f} & {peak:.1f}'+r' \\')
    second.extend([r'\bottomrule',r'\end{tabular}',''])
    return {'triple-native.tex':'\n'.join(first).encode('utf-8'),
            'triple-cost.tex':'\n'.join(second).encode('utf-8')}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out',type=Path)
    args = parser.parse_args()
    products = tables(*load_records())
    if args.out:
        args.out.mkdir(parents=True,exist_ok=True)
        for name,data in products.items():
            (args.out/name).write_bytes(data)
    print('24 native builds, 48 exact labelled outputs and phase measurements consistent')
