"""Producer-side lowering from concrete ZIP/JAR archives to the finite graph.

The parser deliberately supports only opaque archive entries.  It excludes the
builder-generated JAR manifest, rejects duplicate/path-unsafe names, and never
executes classes or resource transformers.  The checker has a separately
written implementation in archive_checker.py.
"""
from __future__ import annotations
from pathlib import Path
from zipfile import BadZipFile, ZipFile

MAX_ARCHIVE_BYTES = 32 * 1024 * 1024
MAX_ENTRY_BYTES = 16 * 1024 * 1024
MAX_UNCOMPRESSED_BYTES = 128 * 1024 * 1024
MAX_ENTRIES = 20_000
MANIFEST = "META-INF/MANIFEST.MF"

class ArchiveInputError(ValueError):
    pass

def _safe_name(name: str) -> bool:
    if not isinstance(name, str) or not name or "\\" in name or "\x00" in name or name.startswith("/"):
        return False
    parts = name.split('/')
    return bool(parts) and all(part not in ("", ".", "..") for part in parts)

def read_archive(path: str | Path) -> dict[str, bytes]:
    source = Path(path)
    if not source.is_file() or source.stat().st_size > MAX_ARCHIVE_BYTES:
        raise ArchiveInputError("archive missing or exceeds compressed-byte limit")
    result: dict[str, bytes] = {}
    total = 0
    try:
        with ZipFile(source) as archive:
            for info in archive.infolist():
                if info.is_dir():
                    continue
                name = info.filename
                if name.upper() == MANIFEST.upper():
                    continue
                if not _safe_name(name):
                    raise ArchiveInputError("unsafe archive entry name")
                if name in result:
                    raise ArchiveInputError("duplicate archive entry name")
                if info.file_size < 0 or info.file_size > MAX_ENTRY_BYTES:
                    raise ArchiveInputError("entry exceeds uncompressed-byte limit")
                total += info.file_size
                if len(result) >= MAX_ENTRIES or total > MAX_UNCOMPRESSED_BYTES:
                    raise ArchiveInputError("archive structural limit")
                data = archive.read(info)
                if len(data) != info.file_size:
                    raise ArchiveInputError("entry length mismatch")
                result[name] = data
    except BadZipFile as exc:
        raise ArchiveInputError("malformed ZIP/JAR archive") from exc
    return result

def lower_archives(providers, observed_path: str | Path, before=()):
    """Return graph form from ``(id, owner, path)`` provider tuples."""
    if not isinstance(providers, (list, tuple)) or not providers:
        raise ArchiveInputError("nonempty provider list required")
    ids: set[str] = set(); owners: list[str] = []; inventories: list[dict[str, bytes]] = []
    for item in providers:
        if not isinstance(item, (list, tuple)) or len(item) != 3:
            raise ArchiveInputError("provider tuple shape")
        identifier, owner, path = item
        if not isinstance(identifier, str) or not identifier or identifier in ids:
            raise ArchiveInputError("provider identifier")
        if not isinstance(owner, str) or not owner:
            raise ArchiveInputError("owner label")
        ids.add(identifier); owners.append(owner); inventories.append(read_archive(path))
    observed = read_archive(observed_path)
    expected = set().union(*(set(inv) for inv in inventories))
    if set(observed) != expected:
        raise ArchiveInputError("observed archive is not the closed provider union")
    rows = []
    for name in sorted(expected):
        present = [i for i, inv in enumerate(inventories) if name in inv]
        good = [i for i in present if inventories[i][name] == observed[name]]
        rows.append({"key": name, "present": present, "good": good})
    return {"kind": "graph", "owners": owners, "before": [list(x) for x in before], "rows": rows}
