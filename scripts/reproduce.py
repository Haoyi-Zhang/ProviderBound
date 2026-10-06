"""Fresh, bounded reproduction; --skip-public runs the portable finite campaign."""
from pathlib import Path
import argparse, datetime, json, os, platform, re, subprocess, sys, time
from telemetry import usage

ROOT = Path(__file__).resolve().parents[1]


def prepare_output(path):
    path = Path(path).resolve()
    if path.exists() and (not path.is_dir() or any(path.iterdir())):
        raise ValueError('output must be absent or empty; previous results are never reused')
    path.mkdir(parents=True, exist_ok=True)
    return path


def compare_generated(inputs):
    index = json.loads((inputs/'index.json').read_text(encoding='utf-8'))
    paths = [Path('index.json')] + [Path(x['path']).relative_to('inputs') for x in index]
    for path in paths:
        fresh = json.loads((inputs/path).read_text(encoding='utf-8'))
        retained = json.loads((ROOT/'inputs'/path).read_text(encoding='utf-8'))
        if fresh != retained:
            raise ValueError(f'generated input differs from retained fixture: {path}')
    return len(paths)


def run():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', default='reproduced')
    parser.add_argument('--java', action='store_true', help='compile/run the two owned Java builds')
    parser.add_argument('--skip-public', action='store_true', help='omit Ant; no external-builder result is claimed')
    args = parser.parse_args()
    if sys.flags.optimize:
        parser.error('assertions must remain enabled; do not use -O')
    out = Path(args.output)
    if not out.is_absolute():
        out = ROOT/out
    try:
        out = prepare_output(out)
    except ValueError as exc:
        parser.error(str(exc))
    scratch = out/'scratch'; scratch.mkdir()
    env = dict(os.environ, PYTHONUTF8='1', PYTHONDONTWRITEBYTECODE='1',
               PYTHONHASHSEED='0', OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1',
               MKL_NUM_THREADS='1', TMP=str(scratch), TEMP=str(scratch), TMPDIR=str(scratch))
    py = [sys.executable, '-B']
    commands = [
        ('generate', py+['scripts/make_inputs.py', '--output', str(out/'inputs')], 180),
        ('public-inputs', py+['scripts/verify_public_inputs.py'], 180),
        ('unit', py+['-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_*.py', '-v'], 180),
        ('oracle', py+['tests/oracle.py', str(out)], 180),
        ('campaign', py+['scripts/campaign.py', str(out), '--inputs', str(out/'inputs')], 180),
    ]
    if not args.skip_public:
        commands.append(('public', py+['scripts/public_corpus.py', '--output', str(out/'public'), '--workers', '4'], 900))
    commands.append(('scale', py+['scripts/scale.py', str(out)], 180))
    if args.java:
        commands.append(('java', py+['scripts/java_pilot.py', str(out)], 180))
    environment = {'python': sys.version, 'executable': sys.executable,
                   'platform': platform.platform(), 'machine': platform.machine(),
                   'logical_cpu_count': os.cpu_count(), 'assertions_enabled': __debug__,
                   'started_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                   'public_requested': not args.skip_public, 'java_requested': args.java,
                   'env': {k: env[k] for k in ('PYTHONUTF8', 'PYTHONDONTWRITEBYTECODE', 'PYTHONHASHSEED')}}
    (out/'environment.json').write_text(json.dumps(environment, indent=2)+'\n', encoding='utf-8')
    start = time.monotonic(); before = usage(children=True)
    summary = {'status': 'running', 'commands': [], 'unit_tests_run': None,
               'regenerated_input_files_compared': 0, 'public_requested': not args.skip_public,
               'java_requested': args.java, 'deadline_seconds': 1650,
               'maximum_workers': 4 if not args.skip_public else 1,
               'scope': 'Finite semantic comparisons and requested integrations, not a mechanized implementation proof.'}

    def save():
        after = usage(children=True)
        summary.update(wall_seconds=time.monotonic()-start,
                       cpu_seconds_children=None if after['cpu_seconds'] is None else after['cpu_seconds']-before['cpu_seconds'],
                       child_peak_rss_kib=after['peak_rss_kib'], rss_scope=after['scope'])
        (out/'reproduction_summary.json').write_text(json.dumps(summary, indent=2)+'\n', encoding='utf-8')

    save()
    for name, cmd, stage_limit in commands:
        remaining = 1650-(time.monotonic()-start)
        if remaining <= 0:
            summary.update(status='failed', error='campaign deadline exhausted'); save()
            raise SystemExit(2)
        timeout = min(stage_limit, remaining); began = time.monotonic()
        try:
            result = subprocess.run(cmd, cwd=ROOT, env=env, text=True, encoding='utf-8',
                                    errors='replace', capture_output=True, timeout=timeout)
            log = result.stdout+result.stderr; code = result.returncode
        except subprocess.TimeoutExpired as exc:
            def decoded(value):
                return value.decode('utf-8', errors='replace') if isinstance(value, bytes) else (value or '')
            log = decoded(exc.stdout)+decoded(exc.stderr)+'\nSTAGE TIMEOUT\n'; code = 124
        (out/f'{name}.txt').write_text(log, encoding='utf-8')
        summary['commands'].append({'command': name, 'argv': cmd, 'exit_code': code,
                                    'wall_seconds': time.monotonic()-began, 'timeout_seconds': timeout})
        if code:
            summary.update(status='failed', error=f'{name} exited {code}'); save()
            print(log, file=sys.stderr); raise SystemExit(code)
        try:
            if name == 'generate':
                summary['regenerated_input_files_compared'] = compare_generated(out/'inputs')
            if name == 'unit':
                match = re.search(r'Ran (\d+) tests? in ', log)
                if not match:
                    raise ValueError('unit execution count absent from actual test log')
                summary['unit_tests_run'] = int(match.group(1))
        except ValueError as exc:
            summary.update(status='failed', error=str(exc)); save(); raise SystemExit(2) from exc
        save(); print(f'{name}: PASS', flush=True)
    summary['status'] = 'complete'; save()
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    run()
