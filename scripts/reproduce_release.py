"""Compatibility entry point for the current standalone scientific campaign.

The current artifact contains the 43-provider corpus, not the older 107-JAR
exploratory frame. Reproduction never runs analyses requiring that absent frame.
"""
import hashlib
from pathlib import Path
from reproduce import run
from release_manifest import files

ROOT = Path(__file__).resolve().parents[1]


def verify_manifest():
    manifest = ROOT/'RELEASE-MANIFEST.sha256'
    if not manifest.is_file():
        raise ValueError('release integrity manifest is missing')
    listed = set()
    for line in manifest.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        expected, relative = line.split('  ', 1)
        path = ROOT/relative
        if not path.is_file():
            raise ValueError(f'manifest file missing: {relative}')
        with path.open('rb') as stream:
            digest = hashlib.file_digest(stream, 'sha256').hexdigest() if hasattr(hashlib, 'file_digest') else hashlib.sha256(stream.read()).hexdigest()
        if digest != expected:
            raise ValueError(f'manifest content differs: {relative}')
        listed.add(relative)
    if listed != {name for name, _ in files(ROOT)}:
        raise ValueError('manifest membership differs from current artifact')
    print(f'manifest: PASS ({len(listed)} files)', flush=True)

if __name__ == '__main__':
    verify_manifest()
    run()
