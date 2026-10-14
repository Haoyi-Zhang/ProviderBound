"""Read-only checks for the bundled scientific objects and optional manuscript.

This compatibility entry does not compile a paper, run an experiment, execute
providers, or manufacture a claim by finding its number in unrelated reports.
"""
from __future__ import annotations
import argparse
import ast
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import re
import subprocess

ART = Path(__file__).resolve().parents[1]
PAPER = ART.parent / 'paper'


def run(cmd, cwd=None, timeout=30):
    result = subprocess.run(cmd, cwd=cwd, timeout=timeout, text=True,
                            capture_output=True, encoding='utf-8', errors='replace')
    if result.returncode:
        raise RuntimeError(f'command failed ({result.returncode}): {result.stderr[-2000:]}')
    return result.stdout


def find_pdf():
    pdf = PAPER / 'main.pdf'
    if not pdf.is_file():
        raise RuntimeError('primary manuscript main.pdf is missing')
    out = run(['pdfinfo', str(pdf)], timeout=30)
    match = re.search(r'^Pages:\s+(\d+)\s*$', out, re.M)
    if match is None or int(match.group(1)) <= 0:
        raise RuntimeError('primary manuscript has no positive page count')
    return pdf


def check_artifact(root):
    import audit_claims
    import verify_public_inputs
    from reproduce_release import verify_manifest
    root = Path(root).resolve()
    result = {'checks': [], 'errors': []}
    try:
        with redirect_stdout(io.StringIO()):
            count = verify_manifest(root)
        result['checks'].append({'name': 'manifest', 'files': count, 'passed': True})
    except (OSError, ValueError) as exc:
        result['errors'].append(f'manifest: {exc}')
    scientific = audit_claims.audit(root)
    result['scientific_objects'] = scientific
    if scientific['status'] != 'PASS':
        result['errors'].append('one or more named scientific-object checks failed')
    try:
        corpus = verify_public_inputs.run(root)
        result['public_input_census'] = corpus
    except (OSError, ValueError, RuntimeError) as exc:
        result['errors'].append(f'public input census: {exc}')
    syntax = []
    for directory in ('src', 'scripts', 'tests'):
        for path in sorted((root / directory).rglob('*.py')):
            try:
                ast.parse(path.read_text(encoding='utf-8-sig'), filename=str(path))
            except (OSError, SyntaxError, UnicodeError) as exc:
                syntax.append({'path': str(path.relative_to(root)), 'error': str(exc)})
    result['checks'].append({'name': 'python-syntax', 'passed': not syntax, 'errors': syntax})
    result['errors'].extend(f"syntax: {entry['path']}" for entry in syntax)
    result['status'] = 'PASS' if not result['errors'] else 'FAIL'
    result['scope'] = ('Bundled input/result contracts, exact manifest membership and Python syntax. '
                       'No new native execution, proof certification, literature certification or submission approval.')
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--artifact', type=Path, default=ART)
    parser.add_argument('--paper', type=Path, help='inspect primary PDF metadata with pdfinfo')
    parser.add_argument('--output-json', type=Path, help='optional report path outside the artifact')
    parser.add_argument('--strict', action='store_true', help='compatibility flag; failures always exit nonzero')
    parser.add_argument('--skip-build', action='store_true', help='compatibility flag; this entry never builds')
    args = parser.parse_args(argv)
    output = args.output_json.resolve() if args.output_json else None
    root = args.artifact.resolve()
    if output is not None and output.is_relative_to(root):
        parser.error('report output must be outside the artifact')
    result = check_artifact(root)
    if args.paper:
        global PAPER
        PAPER = args.paper.resolve()
        try:
            pdf = find_pdf()
            result['paper_metadata'] = {'primary': str(pdf), 'positive_page_count': True}
        except (OSError, RuntimeError, subprocess.SubprocessError) as exc:
            result['errors'].append(f'paper metadata: {exc}')
            result['status'] = 'FAIL'
    serialized = json.dumps(result, indent=2, sort_keys=True) + '\n'
    if output is not None:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(serialized, encoding='utf-8')
    print(serialized)
    return 0 if result['status'] == 'PASS' else 2


if __name__ == '__main__':
    raise SystemExit(main())
