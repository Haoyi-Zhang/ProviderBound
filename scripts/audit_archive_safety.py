#!/usr/bin/env python3
"""Audit the retained archive frame for ambiguous or unsafe ZIP/JAR semantics.

The audit is deliberately independent of the producer and checker.  It rejects
conditions for which a map-from-path abstraction would be ambiguous: duplicate
file names, aliases after the documented path normalization, traversal or
absolute paths, NUL/backslash names, encrypted members, and Unix symbolic-link
members.  Directory duplicates are ignored because directories are not model
keys.  Compression ratios are reported, not used as a scientific claim.
"""
from __future__ import annotations
import argparse, hashlib, json, os, re, stat, sys, zipfile
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for block in iter(lambda: f.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def find_frame() -> list[Path]:
    # Prefer an explicit 107-path list retained by the independent baseline.
    baseline = ROOT / 'results' / 'information-baselines.json'
    if baseline.exists():
        obj = json.loads(baseline.read_text(encoding='utf-8'))
        lists: list[list[str]] = []
        def walk(x):
            if isinstance(x, list) and len(x) == 107 and all(isinstance(v, str) for v in x):
                if sum(v.lower().endswith(('.jar', '.zip')) for v in x) >= 100:
                    lists.append(x)
            if isinstance(x, dict):
                for v in x.values(): walk(v)
            elif isinstance(x, list):
                for v in x: walk(v)
        walk(obj)
        for values in lists:
            paths=[]
            for value in values:
                p=Path(value)
                candidates=[p, ROOT/p, ROOT/'inputs'/p, ROOT/'data'/p]
                found=next((q.resolve() for q in candidates if q.exists()), None)
                if found is None:
                    break
                paths.append(found)
            if len(paths)==107:
                return sorted(set(paths))

    # Otherwise find the narrowest directory whose recursive JAR set is 107.
    candidates=[]
    for d in [ROOT/'inputs', ROOT/'data', ROOT/'corpus', ROOT]:
        if not d.exists():
            continue
        for sub in [d, *[p for p in d.rglob('*') if p.is_dir()]]:
            jars=sorted(p.resolve() for p in sub.rglob('*.jar') if p.is_file() and not p.is_symlink())
            if len(jars)==107:
                candidates.append((len(sub.parts), len(str(sub)), sub, jars))
    if candidates:
        # Deepest/narrowest candidate, then shortest lexical representation.
        candidates.sort(key=lambda t: (-t[0], t[1], str(t[2])))
        return candidates[0][3]
    raise SystemExit('Could not identify the retained 107-archive frame')


def canonical_name(name: str) -> str:
    # Mirrors the paper's deliberately small lexical normalization language.
    if '\x00' in name or '\\' in name:
        raise ValueError('NUL/backslash')
    if name.startswith('/') or re.match(r'^[A-Za-z]:', name):
        raise ValueError('absolute')
    parts=[]
    for part in name.split('/'):
        if part in ('', '.'):
            continue
        if part == '..':
            raise ValueError('traversal')
        parts.append(part)
    if not parts:
        raise ValueError('empty')
    return '/'.join(parts)


def is_symlink(info: zipfile.ZipInfo) -> bool:
    mode=(info.external_attr >> 16) & 0xFFFF
    return stat.S_ISLNK(mode)


def audit_archive(path: Path) -> dict:
    raw_names=[]
    canonical=[]
    errors=[]
    encrypted=0
    symlinks=0
    files=0
    dirs=0
    uncompressed=0
    compressed=0
    max_member_uncompressed=0
    max_ratio=0.0
    with zipfile.ZipFile(path) as zf:
        bad=zf.testzip()
        if bad is not None:
            errors.append({'kind':'crc', 'entry':bad})
        for info in zf.infolist():
            if info.is_dir() or info.filename.endswith('/'):
                dirs += 1
                continue
            files += 1
            raw_names.append(info.filename)
            if info.flag_bits & 0x1:
                encrypted += 1
                errors.append({'kind':'encrypted', 'entry':info.filename})
            if is_symlink(info):
                symlinks += 1
                errors.append({'kind':'symlink', 'entry':info.filename})
            try:
                cname=canonical_name(info.filename)
                canonical.append(cname)
                if cname != info.filename:
                    errors.append({'kind':'noncanonical-name', 'entry':info.filename, 'canonical':cname})
            except ValueError as exc:
                errors.append({'kind':'unsafe-name', 'entry':info.filename, 'reason':str(exc)})
            uncompressed += info.file_size
            compressed += info.compress_size
            max_member_uncompressed=max(max_member_uncompressed, info.file_size)
            if info.compress_size:
                max_ratio=max(max_ratio, info.file_size/info.compress_size)
    raw_dups=sorted(k for k,v in Counter(raw_names).items() if v>1)
    canon_dups=sorted(k for k,v in Counter(canonical).items() if v>1)
    for name in raw_dups:
        errors.append({'kind':'duplicate-raw-name','entry':name})
    for name in canon_dups:
        errors.append({'kind':'duplicate-canonical-name','entry':name})
    return {
        'path': str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path),
        'sha256': sha256(path),
        'bytes': path.stat().st_size,
        'file_entries': files,
        'directory_entries': dirs,
        'uncompressed_bytes': uncompressed,
        'compressed_member_bytes': compressed,
        'max_member_uncompressed_bytes': max_member_uncompressed,
        'max_member_compression_ratio': round(max_ratio, 6),
        'encrypted_entries': encrypted,
        'symlink_entries': symlinks,
        'raw_duplicate_names': raw_dups,
        'canonical_duplicate_names': canon_dups,
        'errors': errors,
    }


def main() -> int:
    ap=argparse.ArgumentParser()
    ap.add_argument('--strict', action='store_true')
    args=ap.parse_args()
    frame=find_frame()
    records=[audit_archive(p) for p in frame]
    errors=[{'archive':r['path'], **e} for r in records for e in r['errors']]
    summary={
        'schema_version': 1,
        'frame_archives': len(frame),
        'archives_with_errors': sum(bool(r['errors']) for r in records),
        'total_file_entries': sum(r['file_entries'] for r in records),
        'total_uncompressed_bytes': sum(r['uncompressed_bytes'] for r in records),
        'max_archive_uncompressed_bytes': max((r['uncompressed_bytes'] for r in records), default=0),
        'max_member_uncompressed_bytes': max((r['max_member_uncompressed_bytes'] for r in records), default=0),
        'max_member_compression_ratio': max((r['max_member_compression_ratio'] for r in records), default=0),
        'duplicate_raw_names': sum(len(r['raw_duplicate_names']) for r in records),
        'duplicate_canonical_names': sum(len(r['canonical_duplicate_names']) for r in records),
        'encrypted_entries': sum(r['encrypted_entries'] for r in records),
        'symlink_entries': sum(r['symlink_entries'] for r in records),
        'errors': errors,
        'archives': records,
    }
    out=ROOT/'docs'/'archive-safety-audit.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2, sort_keys=True)+'\n', encoding='utf-8')
    md=[
        '# Archive-Semantics and Safety Audit','',
        'This audit is independent of the certificate producer and checker. It checks the retained 107-archive frame for conditions that would make the finite path-to-byte-map abstraction ambiguous or unsafe.','',
        f"- Archives: **{summary['frame_archives']}**",
        f"- File entries: **{summary['total_file_entries']}**",
        f"- Archives with a rejected condition: **{summary['archives_with_errors']}**",
        f"- Duplicate raw file names: **{summary['duplicate_raw_names']}**",
        f"- Duplicate names after lexical normalization: **{summary['duplicate_canonical_names']}**",
        f"- Encrypted entries: **{summary['encrypted_entries']}**",
        f"- Unix symbolic-link entries: **{summary['symlink_entries']}**",'',
        'The compression-size figures are diagnostic only. The scientific claims concern pinned, hash-verified inputs; the artifact does not claim a general-purpose hostile-archive extraction sandbox.',''
    ]
    if errors:
        md += ['## Rejected conditions',''] + [f"- `{e['archive']}` — {e['kind']}: `{e.get('entry','')}`" for e in errors]
    else:
        md += ['No ambiguous or unsafe member condition was found in the retained frame. Any future archive presenting one of these conditions must be rejected rather than silently assigned an implementation-dependent meaning.']
    (ROOT/'docs'/'archive-safety-audit.md').write_text('\n'.join(md)+'\n', encoding='utf-8')
    if args.strict and (len(frame)!=107 or errors):
        return 2
    return 0

if __name__=='__main__':
    raise SystemExit(main())
