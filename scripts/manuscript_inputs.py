"""Validate retained diagnostic source identities before exporting paper tables."""
from pathlib import Path
import hashlib, json
def validate_diagnostic_inputs(artifact):
    artifact=Path(artifact)
    record=artifact/'results/diagnostics/current/input-source-sha256.json'
    for relative, expected in json.loads(record.read_text(encoding='utf-8')).items():
        path=(artifact/relative).resolve()
        if not path.is_relative_to(artifact.resolve()):
            raise ValueError('diagnostic path leaves artifact')
        if hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
            raise RuntimeError('current diagnostic input/source changed: '+relative)
