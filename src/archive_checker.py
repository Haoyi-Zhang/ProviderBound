"""Checker-side concrete archive interpretation, independent of producer code."""
from __future__ import annotations
from pathlib import Path
from zipfile import BadZipFile, ZipFile

_LIMIT_FILE = 32 * 1024 * 1024
_LIMIT_MEMBER = 16 * 1024 * 1024
_LIMIT_TOTAL = 128 * 1024 * 1024
_LIMIT_COUNT = 20_000

class ArchiveRejected(ValueError):
    pass

def _name_ok(value):
    if type(value) is not str or not value or value[0] == '/' or '\\' in value or '\x00' in value:
        return False
    fields = value.split('/')
    return all(field not in ('', '.', '..') for field in fields)

def unpack_archive(filename):
    filename = Path(filename)
    if not filename.exists() or not filename.is_file():
        raise ArchiveRejected('archive does not exist')
    if filename.stat().st_size > _LIMIT_FILE:
        raise ArchiveRejected('compressed archive too large')
    table = {}; amount = 0
    try:
        archive = ZipFile(filename)
    except BadZipFile as exc:
        raise ArchiveRejected('not a ZIP archive') from exc
    with archive:
        members = archive.infolist()
        for member in members:
            if member.is_dir():
                continue
            key = member.filename
            if key.upper() == 'META-INF/MANIFEST.MF':
                continue
            if not _name_ok(key) or key in table:
                raise ArchiveRejected('invalid or repeated entry')
            if not 0 <= member.file_size <= _LIMIT_MEMBER:
                raise ArchiveRejected('member too large')
            amount += member.file_size
            if len(table) + 1 > _LIMIT_COUNT or amount > _LIMIT_TOTAL:
                raise ArchiveRejected('expanded archive limit')
            payload = archive.read(key)
            if len(payload) != member.file_size:
                raise ArchiveRejected('declared member size mismatch')
            table[key] = payload
    return table

def interpret_archives(specifications, output_archive, precedence=()):
    """Build graph form from a list of dictionaries with id/owner/path fields."""
    if type(specifications) not in (list, tuple) or len(specifications) == 0:
        raise ArchiveRejected('provider sequence')
    labels=[]; stores=[]; identifiers=set()
    for specification in specifications:
        if type(specification) is not dict or set(specification) != {'id','owner','path'}:
            raise ArchiveRejected('provider specification fields')
        identity=specification['id']; label=specification['owner']
        if type(identity) is not str or not identity or identity in identifiers:
            raise ArchiveRejected('provider identity')
        if type(label) is not str or not label:
            raise ArchiveRejected('provider owner')
        identifiers.add(identity); labels.append(label); stores.append(unpack_archive(specification['path']))
    product=unpack_archive(output_archive)
    universe=set()
    for store in stores:
        universe.update(store.keys())
    if universe != set(product.keys()):
        raise ArchiveRejected('output names differ from provider union')
    constraints=[]
    for key in sorted(universe):
        candidates=[]; matching=[]
        for number, store in enumerate(stores):
            if key in store:
                candidates.append(number)
                if store[key] == product[key]:
                    matching.append(number)
        constraints.append({'key':key,'present':candidates,'good':matching})
    edges=[]
    for pair in precedence:
        if type(pair) not in (list,tuple) or len(pair)!=2:
            raise ArchiveRejected('precedence pair')
        edges.append([pair[0],pair[1]])
    return {'kind':'graph','owners':labels,'before':edges,'rows':constraints}
