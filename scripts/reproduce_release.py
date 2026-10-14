"""Compatibility entry point for the current standalone scientific campaign.

This entry verifies exact artifact membership before running the bundled
43-provider scientific campaign.
"""
import hashlib
import re
from pathlib import Path, PurePosixPath
from reproduce import run
from release_manifest import files

ROOT = Path(__file__).resolve().parents[1]


def verify_manifest(root=None):
    root = (ROOT if root is None else Path(root)).resolve()
    manifest = root/'RELEASE-MANIFEST.sha256'
    if not manifest.is_file():
        raise ValueError('release integrity manifest is missing')
    listed = set()
    for line in manifest.read_text(encoding='utf-8').splitlines():
        if not line.strip():
            continue
        if '  ' not in line:
            raise ValueError('malformed manifest row')
        expected, relative = line.split('  ', 1)
        name = PurePosixPath(relative)
        if (not re.fullmatch(r'[0-9a-f]{64}', expected) or not relative or
                '\\' in relative or name.is_absolute() or '..' in name.parts or
                ':' in relative or str(name) != relative):
            raise ValueError('malformed manifest digest or relative path')
        if relative in listed:
            raise ValueError(f'duplicate manifest member: {relative}')
        path = root/relative
        if path.is_symlink() or not path.is_file():
            raise ValueError(f'manifest file missing: {relative}')
        try:
            path.resolve().relative_to(root)
        except ValueError as exc:
            raise ValueError('manifest member resolves outside artifact') from exc
        with path.open('rb') as stream:
            digest = hashlib.file_digest(stream, 'sha256').hexdigest() if hasattr(hashlib, 'file_digest') else hashlib.sha256(stream.read()).hexdigest()
        if digest != expected:
            raise ValueError(f'manifest content differs: {relative}')
        listed.add(relative)
    if listed != {name for name, _ in files(root)}:
        raise ValueError('manifest membership differs from current artifact')
    print(f'manifest: PASS ({len(listed)} files)', flush=True)
    return len(listed)

if __name__ == '__main__':
    verify_manifest()
    run()
