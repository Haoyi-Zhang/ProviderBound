"""Fresh, offline owner/receipt diagnostics. No Ant, provider execution or extraction.

This path reproduces the current bounded corrections, not the native build study.
One retained test writes a traversal-name ZIP; it is deliberately not executed by
this benign-fixture path. Its absence is reported, never counted as a pass.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import platform
import sys
from tempfile import TemporaryDirectory
import time
import unittest

ROOT = Path(__file__).resolve().parents[1]
for part in ('src', 'scripts', 'tests'):
    sys.path.insert(0, str(ROOT / part))
import analyze_owner_granularity as granularity
import verify_public_inputs

EXCLUDED = {'test_boundary.BoundaryTests.test_concrete_archive_adapters_and_safety':
            'Retained test writes a traversal-name ZIP; omitted from this benign-fixture run.'}


def leaves(suite):
    for item in suite:
        if isinstance(item, unittest.TestSuite):
            yield from leaves(item)
        else:
            yield item


def dump(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n', encoding='utf-8')


def main():
    if not __debug__:
        raise RuntimeError('Run without Python -O/-OO.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    output.relative_to((ROOT / 'results').resolve())
    if output.exists():
        raise ValueError('a fresh output path is required; retained evidence is never overwritten')
    output.mkdir(parents=True)
    started = datetime.now(timezone.utc).isoformat()
    clock = time.perf_counter()
    with TemporaryDirectory(prefix='owned-', dir=output) as scratch:
        for name in ('TEMP', 'TMP', 'TMPDIR'):
            os.environ[name] = scratch
        all_tests = list(leaves(unittest.defaultTestLoader.discover(str(ROOT / 'tests'), pattern='test_*.py')))
        found = {test.id() for test in all_tests}
        if not set(EXCLUDED) <= found:
            raise ValueError('named exclusion no longer identifies an actual retained test')
        selected = [test for test in all_tests if test.id() not in EXCLUDED]
        stream = io.StringIO()
        result = unittest.TextTestRunner(stream=stream, verbosity=2).run(unittest.TestSuite(selected))
        (output / 'tests.log').write_text(stream.getvalue(), encoding='utf-8')
        tests = {'discovered': len(all_tests), 'selected': len(selected), 'run': result.testsRun,
                 'failures': len(result.failures), 'errors': len(result.errors),
                 'skipped': len(result.skipped), 'excluded_not_executed': EXCLUDED,
                 'selected_test_ids': [test.id() for test in selected]}
        dump(output / 'tests.json', tests)
        if not result.wasSuccessful():
            raise RuntimeError('selected diagnostics failed; inspect raw tests.log')
        public = verify_public_inputs.run()
        dump(output / 'public-inputs.json', public)
        owner = granularity.run()
        dump(output / 'owner-granularity.json', owner)
        historical = json.loads((ROOT / 'results/owner-granularity.json').read_text(encoding='utf-8'))
        comparisons = []
        for scheme, metrics in historical['metrics'].items():
            for field, value in metrics.items():
                actual = owner['metrics'][scheme][field]
                if actual != value:
                    raise ValueError(f'retained metric changed: {scheme}.{field}')
                comparisons.append({'scheme': scheme, 'field': field, 'retained': value, 'current': actual})
        dump(output / 'retained-metric-comparison.json', comparisons)
    consumed = []
    for part in ('src', 'scripts', 'tests', 'inputs'):
        consumed.extend(p for p in (ROOT / part).rglob('*') if p.is_file() and '__pycache__' not in p.parts)
    consumed.extend(ROOT / p for p in ('results/owner-granularity.json', 'results/current/public/cases.csv'))
    dump(output / 'input-source-sha256.json', {str(p.relative_to(ROOT)).replace('\\', '/'):
         hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(set(consumed))})
    import zipfile
    summary = {'started_utc': started, 'finished_utc': datetime.now(timezone.utc).isoformat(),
               'wall_seconds': time.perf_counter() - clock, 'command': [sys.executable, *sys.argv],
               'cwd': str(Path.cwd()), 'python': sys.version, 'platform': platform.platform(),
               'hash_seed': os.environ.get('PYTHONHASHSEED'),
               'zipfile_sha256': hashlib.sha256(Path(zipfile.__file__).read_bytes()).hexdigest(),
               'actual_ant_builds': 0, 'provider_code_executions': 0,
               'archive_extractions': 0, 'public_zip_output_replays': 0,
               'modeled_outputs_per_label_schema': owner['modeled_outputs_per_schema'],
               'label_schemas': 2, 'collision_observations_per_schema': owner['metrics']['archive']['collision_observations'],
               'tests': tests, 'retained_metric_checks': len(comparisons),
               'scope': 'Bundled provider bytes and caller-declared labels; new model replay and owned controls, not new native builds or ownership authentication.',
               'unmeasured': ['real downstream analyzer/finding benefit', 'ownership-label truth',
                              'fresh Ant/JVM experiment', 'general ZIP header-parser correctness']}
    dump(output / 'receipt.json', summary)
    print(json.dumps({key: summary[key] for key in ('actual_ant_builds', 'modeled_outputs_per_label_schema', 'tests', 'retained_metric_checks')}, indent=2))


if __name__ == '__main__':
    main()
