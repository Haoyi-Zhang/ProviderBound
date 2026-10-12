"""Same-information owner-label diagnostic on the retained 43-provider corpus.

Reconstruct both first-winner content maps from bundled provider bytes; do not
run Ant or provider classes. Retained Ant case counts cross-check reconstruction,
but this is a model replay, not a new external-builder experiment. Both methods
receive the same complete inventory, observed bytes and label map, with no
precedence or historical order passed to inference. Only the label map changes
between archive identity and the recorded Debian binary package.
"""
from __future__ import annotations
import argparse
from collections import Counter
import csv
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from archive_producer import read_archive
from archive_checker import unpack_archive
from producer import infer
from checker import verify


def records(path):
    with path.open(newline='', encoding='utf-8') as stream:
        return list(csv.DictReader(stream))


def merge(stores, order):
    output = {}
    for p in order:
        for key, payload in stores[p].items():
            output.setdefault(key, payload)
    return output


def analyze_pair(stores, labels):
    """Compare local bytes, replayed certificates and a literal two-order oracle."""
    outputs = [merge(stores, (0, 1)), merge(stores, (1, 0))]
    universe = sorted(set(stores[0]) | set(stores[1]))
    results = []
    for observed in outputs:
        rows = []
        for key in universe:
            present = [p for p in (0, 1) if key in stores[p]]
            good = [p for p in present if stores[p][key] == observed[key]]
            rows.append({'key': key, 'present': present, 'good': good})
        raw = {'kind': 'graph', 'owners': list(labels), 'before': [], 'rows': rows}
        certificate = json.loads(json.dumps(infer(raw)))
        answer = verify(raw, certificate)
        feasible = [order for order, candidate in zip(((0, 1), (1, 0)), outputs)
                    if candidate == observed]
        counts = Counter(entry_regions=len(rows), admissible_orders=len(feasible))
        narrowed = []
        for row, accepted in zip(rows, answer['regions']):
            possible = {next(p for p in order if p in row['present']) for order in feasible}
            oracle = {labels[p] for p in possible}
            exact = set(accepted['owners'])
            local = {labels[p] for p in row['good']}
            if exact != oracle or not exact <= local:
                raise ValueError('certificate/oracle/local containment disagreement')
            if len(row['present']) < 2:
                continue
            counts['collision_observations'] += 1
            counts['local_exact_count'] += local == oracle
            counts['certified_exact_count'] += exact == oracle
            counts['local_set_size_sum'] += len(local)
            counts['certified_set_size_sum'] += len(exact)
            counts['local_ambiguous'] += len(local) > 1
            counts['certified_ambiguous'] += len(exact) > 1
            # Developer inclusion is the manuscript's conservative scope policy.
            counts['developer_scope_differences'] += ('developer' in local) != ('developer' in exact)
            if exact < local:
                counts['strict_narrowings'] += 1
                counts['removed_owner_associations'] += len(local - exact)
                narrowed.append(row['key'])
            # Provider precision is independent of the chosen label quotient.
            counts['provider_narrowings'] += possible < set(row['good'])
        results.append({'counts': dict(counts), 'narrowed_paths': narrowed})
    return results


def aggregate(rows):
    counts = Counter()
    for row in rows:
        counts.update(row['counts'])
    # Zero-valued findings must be explicit in the result, not missing fields.
    for key in ('strict_narrowings', 'removed_owner_associations', 'local_ambiguous',
                'certified_ambiguous', 'developer_scope_differences', 'provider_narrowings'):
        counts.setdefault(key, 0)
    n = counts['collision_observations']
    return {**dict(counts),
            'local_exact_rate': counts['local_exact_count'] / n,
            'certified_exact_rate': counts['certified_exact_count'] / n,
            'local_mean_set_size': counts['local_set_size_sum'] / n,
            'certified_mean_set_size': counts['certified_set_size_sum'] / n}


def run():
    public = ROOT / 'inputs/public'
    metadata = {row['archive']: row for row in records(public / 'providers.csv')}
    selection = json.loads((public / 'selection.json').read_text(encoding='utf-8'))
    providers = sorted(set(metadata) - set(selection['builder_archives']))
    if len(providers) != 43:
        raise ValueError('expected the current 43-provider study, not an archived frame')
    stores = {}
    for name in providers:
        path = public / 'jars' / name
        left, right = read_archive(path), unpack_archive(path)
        if left != right:
            raise ValueError('archive adapters disagree')
        stores[name] = left
    retained = {row['build_id']: row for row in records(ROOT / 'results/current/public/cases.csv')}
    schemes = {'archive': [], 'debian_package': []}
    pair_rows = []
    for pair in records(public / 'collision_pairs.csv'):
        names = (pair['left'], pair['right'])
        maps = [stores[name] for name in names]
        labels = {'archive': [metadata[name]['owner'] for name in names],
                  'debian_package': ['deb:' + metadata[name]['package'] for name in names]}
        for scheme, owner_map in labels.items():
            analyzed = analyze_pair(maps, owner_map)
            for suffix, row in zip(('ab', 'ba'), analyzed):
                build_id = pair['pair_id'] + '-' + suffix
                counts = row['counts']
                if scheme == 'archive':
                    historical = retained[build_id]
                    for current, previous in (
                            ('entry_regions', 'entry_regions'),
                            ('collision_observations', 'collision_regions'),
                            ('admissible_orders', 'admissible_actual_orders'),
                            ('local_ambiguous', 'local_ambiguous_regions'),
                            ('certified_ambiguous', 'certified_ambiguous_regions'),
                            ('strict_narrowings', 'global_narrowings')):
                        if counts.get(current, 0) != int(historical[previous]):
                            raise ValueError('model replay differs from retained case counts: ' + build_id)
                    row['build_id'] = build_id
                    row['pair_id'] = pair['pair_id']
                schemes[scheme].append(row)
            pair_rows.append({'pair_id': pair['pair_id'], 'scheme': scheme,
                              'archives': list(names), 'labels': owner_map,
                              'identical_content_maps': merge(maps, (0, 1)) == merge(maps, (1, 0)),
                              'identical_output_pair_paths_with_owner_flip':
                                  len(set(maps[0]) & set(maps[1]))
                                  if merge(maps, (0, 1)) == merge(maps, (1, 0)) and owner_map[0] != owner_map[1] else 0,
                              'strict_narrowings': sum(r['counts'].get('strict_narrowings', 0) for r in analyzed),
                              'narrowed_paths': sorted(set(k for r in analyzed for k in r['narrowed_paths']))})
    metrics = {name: aggregate(rows) for name, rows in schemes.items()}
    for scheme in metrics:
        metrics[scheme]['identical_output_pair_paths_with_owner_flip'] = sum(
            row['identical_output_pair_paths_with_owner_flip'] for row in pair_rows if row['scheme'] == scheme)
    narrowing_pairs = sorted({row['pair_id'] for row in pair_rows if row['strict_narrowings']})
    return {
        'scope': 'New model replay on retained provider bytes; no new Ant builds or downstream analyzer execution.',
        'information_control': 'Same inventory, exact output bytes, empty precedence and identical label map for both methods; no historical order given to inference.',
        'label_schemas': {'archive': 'Recorded per-JAR owner field',
                          'debian_package': 'deb: plus recorded Debian binary-package field; version is not part of this label'},
        'provider_archives': len(providers), 'pair_cases': len(pair_rows) // 2,
        'modeled_outputs_per_schema': len(schemes['archive']),
        'retained_case_count_checks': len(schemes['archive']),
        'archive_adapter_disagreements': 0, 'certificate_oracle_disagreements': 0,
        'metrics': metrics, 'narrowing_pairs': narrowing_pairs, 'pairs': pair_rows,
        'downstream_interpretation': 'No developer/library scope changes in this all-library corpus. Package-level attribution gains must be evaluated after applying the package map to both methods. Provider-history resolution does not disappear when labels are merged; no vulnerability, finding-suppression or call-graph outcome is measured.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'results/owner-granularity.json')
    args = parser.parse_args()
    output = args.output.resolve()
    if not output.is_relative_to(ROOT):
        parser.error('diagnostic output must stay inside this artifact')
    result = run()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'pairs'}, indent=2))


if __name__ == '__main__':
    main()
