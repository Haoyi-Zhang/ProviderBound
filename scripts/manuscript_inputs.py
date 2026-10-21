"""Shared binding contract for the retained diagnostic, gate and paper export.

The catalogue and receipt describe their recorded execution. Two subsequently
maintained auditor programs retain historical identities; they are not counted
as current-code test execution. Every other recorded file must still match.
"""
from pathlib import Path, PurePosixPath
import hashlib
import json
import re

CATALOGUE = 'results/diagnostics/current/input-source-sha256.json'
# Canonical JSON identity preserves all 165 original names AND digest values,
# including the historical auditor identities. It is not a newly issued receipt.
RETAINED_CATALOGUE_SHA256 = 'c5d53f8ec8009a34c4de7b536754a86d0e1fbdd7b4e3d9e7b9fc4cc6c0430e41'
HISTORICAL_PROGRAMS = frozenset(('scripts/audit_claims.py', 'tests/test_audit_claims.py'))
SCIENTIFIC_BINDINGS = (
    'scripts/analyze_owner_granularity.py', 'scripts/reproduce_diagnostics.py',
    'src/archive_producer.py', 'src/archive_checker.py', 'src/producer.py', 'src/checker.py',
    'inputs/public/providers.csv', 'inputs/public/collision_pairs.csv',
    'inputs/public/selection.json', 'results/current/public/cases.csv',
)


def _unique(pairs):
    result = {}
    for name, value in pairs:
        if name in result:
            raise ValueError('duplicate diagnostic binding: ' + name)
        result[name] = value
    return result


def validate_diagnostic_inputs(artifact):
    artifact = Path(artifact).resolve()
    bindings = json.loads((artifact / CATALOGUE).read_text(encoding='utf-8'),
                          object_pairs_hook=_unique)
    if not isinstance(bindings, dict) or len(bindings) != 165:
        raise ValueError('retained diagnostic catalogue must contain all 165 bindings')
    for relative, digest in bindings.items():
        name = PurePosixPath(relative)
        if (name.is_absolute() or '..' in name.parts or ':' in relative
                or '\\' in relative or str(name) != relative):
            raise ValueError('invalid diagnostic binding path: ' + relative)
        if type(digest) is not str or not re.fullmatch(r'[0-9a-f]{64}', digest):
            raise ValueError('invalid diagnostic source binding: ' + relative)
    canonical = json.dumps(bindings, sort_keys=True, separators=(',', ':')).encode('utf-8')
    if hashlib.sha256(canonical).hexdigest() != RETAINED_CATALOGUE_SHA256:
        raise ValueError('retained diagnostic catalogue identity changed; new execution evidence required')
    if not (set(SCIENTIFIC_BINDINGS) | HISTORICAL_PROGRAMS) <= bindings.keys():
        raise ValueError('mandatory diagnostic source binding missing')
    historical = {}
    checked = 0
    for relative, expected in bindings.items():
        path = artifact / relative
        if path.is_symlink() or not path.resolve().is_relative_to(artifact) or not path.is_file():
            raise ValueError('diagnostic file missing or outside artifact: ' + relative)
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if relative in HISTORICAL_PROGRAMS:
            historical[relative] = {'recorded_sha256': expected, 'current_sha256': actual}
        elif actual != expected:
            raise ValueError('current diagnostic input/source changed: ' + relative)
        else:
            checked += 1
    return {'execution_scope': 'retained diagnostic; not current auditor test execution',
            'catalogue_entries': len(bindings), 'current_file_bindings_checked': checked,
            'historical_program_bindings': historical}
