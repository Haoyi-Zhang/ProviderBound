"""Native three-provider archive study on the complete retained collision census.

Only Apache Ant's archive task is executed. Provider classes are never loaded.
All four triples sharing a non-META-INF member are included, with all six
provider orders. No corpus or result from the earlier pair study is rewritten.
"""
from pathlib import Path
import argparse
import csv
import gc
import lzma
import hashlib
from html import escape
import itertools
import json
import os
import shutil
import statistics
import subprocess
import sys
import tempfile
import time
import tracemalloc

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'src'))
from archive_producer import read_archive, lower_archives
from archive_checker import interpret_archives
from producer import infer
from checker import verify


def require(condition, message):
    if not condition:
        raise ValueError(message)


def encoded(value):
    return (json.dumps(value, sort_keys=True, separators=(',', ':'))+'\n').encode('utf-8')


def census():
    with (ROOT/'inputs/public/providers.csv').open(encoding='utf-8', newline='') as stream:
        rows = sorted((row for row in csv.DictReader(stream)
                       if not row['archive'].startswith('ant-')), key=lambda row:row['archive'])
    maps = {row['archive']:read_archive(ROOT/'inputs/public/jars'/row['archive']) for row in rows}
    triples = []
    for triple in itertools.combinations(rows, 3):
        common = set.intersection(*(set(maps[row['archive']]) for row in triple))
        common = {key for key in common if not key.startswith('META-INF/')}
        if common:
            triples.append(tuple(triple))
    require(len(rows) == 43 and len(triples) == 4, 'Frozen three-way collision census changed')
    return triples, maps


def direct_owners(model):
    """Literal whole-order reference; neither inference nor certificates used."""
    owners, rows = model['owners'], model['rows']
    worlds = []
    for order in itertools.permutations(range(len(owners))):
        rank = {p:i for i,p in enumerate(order)}
        if any(rank[a] >= rank[b] for a,b in model['before']):
            continue
        if all(row['present'] and min(row['present'], key=rank.get) in row['good'] for row in rows):
            worlds.append(order)
    if not worlds:
        return None
    return {row['key']:sorted({owners[next(p for p in order if p in row['present'])]
                              for order in worlds}) for row in rows}


def measure(function):
    """Warm callable time; separate one-call Python allocation peak, not JVM/RSS."""
    function()
    durations = []
    for _ in range(5):
        start = time.perf_counter()
        function()
        durations.append(time.perf_counter()-start)
    gc.collect()
    tracemalloc.start()
    function()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return {'seconds':durations, 'median_seconds':statistics.median(durations),
            'minimum_seconds':min(durations), 'maximum_seconds':max(durations),
            'python_peak_allocated_bytes':peak}


def merged(maps, names, order):
    result = {}
    for index in order:
        for key, value in maps[names[index]].items():
            result.setdefault(key, value)
    return result


def run(destination):
    destination = Path(destination)
    require(not destination.exists(), 'Fresh output directory required')
    java = shutil.which('java')
    if os.environ.get('JAVA_HOME'):
        java = str(Path(os.environ['JAVA_HOME'])/'bin'/('java.exe' if os.name == 'nt' else 'java'))
    require(java is not None and Path(java).is_file(), 'Installed Java runtime required')
    triples, maps = census()
    records, timings, aggregate = [], [], []
    permutations = list(itertools.permutations(range(3)))
    with tempfile.TemporaryDirectory(prefix='provider-triples-') as temporary:
        temporary = Path(temporary)
        xml = ['<project default="all"><target name="all">']
        for number, triple in enumerate(triples):
            for oi, order in enumerate(permutations):
                output = temporary/f't{number}-o{oi}.zip'
                xml.append('<zip destfile="'+escape(str(output), quote=True)+
                           '" duplicate="preserve" filesonly="true">')
                for index in order:
                    source = ROOT/'inputs/public/jars'/triple[index]['archive']
                    xml.append('<zipfileset src="'+escape(str(source), quote=True)+
                               '" excludes="META-INF/MANIFEST.MF" defaultexcludes="no"/>')
                xml.append('</zip>')
        xml.append('</target></project>')
        build = temporary/'build.xml'
        build.write_text('\n'.join(xml)+'\n', encoding='utf-8')
        jars = ROOT/'inputs/public/jars'
        cp = os.pathsep.join(str(jars/name) for name in ('ant-1.10.15.jar','ant-launcher-1.10.15.jar'))
        command = [java, '-Xmx768m', '-cp', cp, 'org.apache.tools.ant.Main', '-q', '-f', str(build)]
        native = subprocess.run(command, capture_output=True, timeout=180)
        require(native.returncode == 0, 'Native Ant build failed: '+native.stderr.decode('utf-8',errors='replace'))
        for number, triple in enumerate(triples):
            names = [row['archive'] for row in triple]
            count = {'triple':number+1, 'archives':names,
                     'package_labels':sorted({row['package'] for row in triple}),
                     'ant_builds':6, 'region_observations':0,
                     'per_jar_narrowings':0, 'per_package_narrowings':0,
                     'oracle_mismatches':0}
            for oi, order in enumerate(permutations):
                output = temporary/f't{number}-o{oi}.zip'
                actual = read_archive(output)
                require(actual == merged(maps, names, order), 'Ant differs from exact first-winner content')
                native_entries = {key:hashlib.sha256(value).hexdigest() for key,value in sorted(actual.items())}
                for schema in ('jar','package'):
                    labels = ['lib:'+row['archive'] if schema == 'jar' else 'pkg:'+row['package'] for row in triple]
                    specs = [(str(i),labels[i],jars/names[i]) for i in range(3)]
                    graph = lower_archives(specs, output)
                    independently_lowered = interpret_archives(
                        [{'id':str(i),'owner':labels[i],'path':jars/names[i]} for i in range(3)], output)
                    require(graph == independently_lowered, 'Independent archive adapters differ')
                    certificate = infer(graph)
                    answer = verify(independently_lowered, certificate)
                    reference = direct_owners(independently_lowered)
                    reported = {row['key']:row['owners'] for row in answer['regions']}
                    require(reported == reference, 'Exact six-order oracle differs')
                    narrowings = sum(set(reported[row['key']]) < {labels[i] for i in row['good']}
                                     for row in graph['rows'])
                    count['per_'+schema+'_narrowings' if schema=='jar' else 'per_package_narrowings'] += narrowings
                    if schema == 'jar':
                        count['region_observations'] += len(graph['rows'])
                    raw = {'triple':number+1, 'order':list(order), 'label_schema':schema,
                           'native_entries':native_entries, 'graph':graph,
                           'certificate':certificate, 'answer':answer,
                           'direct_owners':reference, 'global_narrowings':narrowings}
                    records.append(raw)
                    timing = {'triple':number+1,'order':list(order),'label_schema':schema,
                              'certificate_bytes':len(encoded(certificate)),
                              'producer':measure(lambda:infer(graph)),
                              'checker':measure(lambda:verify(independently_lowered,certificate)),
                              'direct_six_order':measure(lambda:direct_owners(independently_lowered))}
                    timings.append(timing)
            aggregate.append(count)
    semantic = {'provider_archives':43, 'three_way_collision_triples':4,
                'native_ant_builds':24,'labelled_output_models':48,'rows':aggregate,
                'certificate_oracle_mismatches':0,'archive_adapter_mismatches':0,
                'first_winner_content_mismatches':0}
    summary = {'semantic':semantic,
               'timing_boundary':'Same loaded three-provider graph; one warmup then five timed calls. Separate one-call tracemalloc peak. Excludes archive reading, Ant, JSON serialization and certificate I/O. No cross-host or general-provider-count claim.',
               'timings':timings,
               'source_bindings':{name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
                   for name in ('scripts/triple_study.py', 'src/producer.py', 'src/checker.py',
                                'src/archive_producer.py', 'src/archive_checker.py',
                                'inputs/public/providers.csv')},
               'environment':{'python':sys.version, 'platform':sys.platform,
                              'java_version':subprocess.run([java,'-version'],capture_output=True).stderr.decode('utf-8',errors='replace')},
               'scope':'All retained three-way non-META-INF collision triples; public provider classes never executed. Package labels are metadata, not developer ownership.'}
    destination.mkdir(parents=True)
    (destination/'summary.json').write_bytes(encoded(summary))
    (destination/'records.json.xz').write_bytes(lzma.compress(encoded(records),format=lzma.FORMAT_XZ,preset=6))
    (destination/'builder.stdout.bin').write_bytes(native.stdout)
    (destination/'builder.stderr.bin').write_bytes(native.stderr)
    (destination/'builder-command.json').write_bytes(encoded({
        'argv':['<JAVA>','-Xmx768m','-cp','<ARTIFACT_ROOT>/inputs/public/jars/ant-1.10.15.jar'+os.pathsep+
                '<ARTIFACT_ROOT>/inputs/public/jars/ant-launcher-1.10.15.jar',
                'org.apache.tools.ant.Main','-q','-f','<WORK_ROOT>/build.xml'],
        'returncode':native.returncode,'actual_zip_tasks':24,
        'manifest_handling':'META-INF/MANIFEST.MF excluded; other entries opaque first-winner bytes'}))
    return summary


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--compare',type=Path)
    args = parser.parse_args()
    summary = run(args.out)
    if args.compare:
        previous = json.loads((args.compare/'summary.json').read_text(encoding='utf-8'))
        require(summary['semantic'] == previous['semantic'], 'Three-provider semantic summary changed')
        require(lzma.decompress((args.out/'records.json.xz').read_bytes()) ==
                lzma.decompress((args.compare/'records.json.xz').read_bytes()), 'Three-provider records changed')
    print(json.dumps(summary['semantic'],indent=2))
