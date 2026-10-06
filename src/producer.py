"""Inference for an explicitly bounded first-winner build language.

No third-party program is executed. `checker.py` contains neither imports from
this module nor a copy of its fixed-point search algorithm.
"""
from __future__ import annotations
from collections import deque
from pathlib import Path
import argparse
import json

MAX_PROVIDERS, MAX_REGIONS, MAX_INCIDENCES = 300, 20_000, 250_000
MAX_INPUT_BYTES = 32 * 1024 * 1024

class InputError(ValueError):
    pass

def _object(pairs):
    out = {}
    for k, v in pairs:
        if k in out:
            raise InputError('duplicate JSON key')
        out[k] = v
    return out

def load(path):
    with Path(path).open('rb') as stream:
        data = stream.read(MAX_INPUT_BYTES + 1)
    if len(data) > MAX_INPUT_BYTES:
        raise InputError('input exceeds byte limit')
    return json.loads(data.decode('utf-8'), object_pairs_hook=_object)

def normalize(data):
    """Convert a raw finite inventory to membership/equal-payload constraints.

    Path-only relocation is one simultaneous, longest-prefix substitution. It
    deliberately does not implement Java/DEX rewriting or resource merging.
    """
    if not isinstance(data, dict):
        raise InputError('input must be an object')
    if data.get('kind') == 'graph':
        model = {k: data[k] for k in ('owners', 'before', 'rows')}
        validate(model)
        return model
    if data.get('kind') != 'inventory':
        raise InputError('unknown input kind')
    providers = data.get('providers')
    if not isinstance(providers, list) or not 1 <= len(providers) <= MAX_PROVIDERS:
        raise InputError('provider count')
    inventories = []
    ids, owners = [], []
    for provider in providers:
        ids.append(provider['id']); owners.append(provider['owner'])
        rules = provider['relocations']
        if not isinstance(rules, list):
            raise InputError('relocations must be a list')
        if len(rules) > 32 or any(not isinstance(r, list) or len(r) != 2 for r in rules):
            raise InputError('relocation rule shape')
        if any(not all(isinstance(v, str) for v in rule) for rule in rules):
            raise InputError('relocation prefixes must be strings')
        prefixes = [r[0] for r in rules]
        if len(prefixes) != len(set(prefixes)) or any(not a or not a.endswith('/') or not b.endswith('/') for a, b in rules):
            raise InputError('relocation prefixes must be distinct nonempty directory prefixes')
        entries, originals = {}, set()
        for entry in provider['entries']:
            name, payload = entry['name'], entry['payload']
            if not isinstance(name, str) or not name or name in originals:
                raise InputError('duplicate/invalid entry name')
            originals.add(name)
            if rules and name.endswith(('.class', '.dex')):
                raise InputError('bytecode relocation is not implemented')
            try:
                value = bytes.fromhex(payload)
            except (ValueError, TypeError) as exc:
                raise InputError('payload must be hexadecimal bytes') from exc
            matches = [(len(a), a, b) for a, b in rules if name.startswith(a)]
            if matches:
                _, a, b = max(matches)
                name = b + name[len(a):]
            if name in entries:
                raise InputError('within-provider relocation collision is unsupported')
            entries[name] = value
        inventories.append(entries)
    if len(ids) != len(set(ids)) or any(not isinstance(x, str) or not x for x in ids):
        raise InputError('provider identifiers')
    observed = {}
    for row in data['observed']:
        key = row['name']
        if not isinstance(key, str) or not key:
            raise InputError('observed name')
        if key in observed:
            raise InputError('duplicate observed name')
        observed[key] = bytes.fromhex(row['payload'])
    expected = set().union(*(set(x) for x in inventories))
    if set(observed) != expected:
        raise InputError('observed key set is not the closed inventory union')
    rows = []
    for key in sorted(expected):
        present = [p for p, inv in enumerate(inventories) if key in inv]
        good = [p for p in present if inventories[p][key] == observed[key]]
        rows.append({'key': key, 'present': present, 'good': good})
    model = {'owners': owners, 'before': data['before'], 'rows': rows}
    validate(model)
    return model

def validate(model):
    owners, edges, rows = model['owners'], model['before'], model['rows']
    if not isinstance(owners, list) or not 1 <= len(owners) <= MAX_PROVIDERS:
        raise InputError('provider count')
    if any(not isinstance(x, str) or not x for x in owners):
        raise InputError('owner label')
    n = len(owners)
    def indices(xs):
        return isinstance(xs, list) and all(type(x) is int and 0 <= x < n for x in xs) and len(xs) == len(set(xs))
    if not isinstance(edges, list) or any(not isinstance(e, list) or len(e) != 2 or any(type(x) is not int or not 0 <= x < n for x in e) for e in edges):
        raise InputError('precedence shape')
    if len(set(map(tuple, edges))) != len(edges):
        raise InputError('duplicate precedence')
    if not isinstance(rows, list) or len(rows) > MAX_REGIONS:
        raise InputError('region count')
    keys = set(); size = len(edges)
    for row in rows:
        if not isinstance(row, dict) or set(row) != {'key', 'present', 'good'}:
            raise InputError('row shape')
        if not isinstance(row['key'], str) or not row['key'] or row['key'] in keys:
            raise InputError('region key')
        keys.add(row['key'])
        if not indices(row['present']) or not indices(row['good']) or not set(row['good']) <= set(row['present']):
            raise InputError('candidate sets')
        size += len(row['present'])
    if size > MAX_INCIDENCES:
        raise InputError('incidence limit')

def search(model, force=None):
    """Linear queue closure for one feasibility query, including empty good sets."""
    n = len(model['owners']); rows = model['rows']
    for r, row in enumerate(rows):
        if not row['present']:
            return None, {'kind': 'missing', 'row': r}
    edges = set(map(tuple, model['before']))
    if force is not None:
        r, p = force
        edges.update((p, q) for q in rows[r]['present'] if q != p)
    succ = [[] for _ in range(n)]; pred = [[] for _ in range(n)]
    indegree = [0] * n; blocks = [0] * n; good_rows = [[] for _ in range(n)]
    bad_sets = []; bad_rows = [[] for _ in range(n)]
    for a, b in sorted(edges):
        succ[a].append(b); pred[b].append(a); indegree[b] += 1
    for r, row in enumerate(rows):
        bad = set(row['present']) - set(row['good']); bad_sets.append(bad)
        for p in bad:
            blocks[p] += 1; bad_rows[p].append(r)
        for p in row['good']:
            good_rows[p].append(r)
    queue = deque(p for p in range(n) if not indegree[p] and not blocks[p])
    queued = set(queue); chosen = set(); active = set(); order = []
    def release(p):
        if p not in queued and indegree[p] == 0 and blocks[p] == 0:
            queued.add(p); queue.append(p)
    while queue:
        p = queue.popleft(); chosen.add(p); order.append(p)
        for q in succ[p]:
            indegree[q] -= 1; release(q)
        for r in good_rows[p]:
            if r in active:
                continue
            active.add(r)
            for q in sorted(bad_sets[r]):
                blocks[q] -= 1; release(q)
    if len(order) == n:
        return order, None
    residual = set(range(n)) - chosen
    reasons = []
    base = set(map(tuple, model['before']))
    for p in sorted(residual):
        preceding = [q for q in pred[p] if q in residual]
        if preceding:
            q = min(preceding)
            reasons.append({'node': p, 'kind': 'before' if (q, p) in base else 'forced', 'pred': q})
        else:
            r = next(r for r in bad_rows[p] if r not in active)
            reasons.append({'node': p, 'kind': 'row', 'row': r})
    return None, {'kind': 'trap', 'nodes': sorted(residual), 'reasons': reasons}

def infer(data):
    model = normalize(data)
    base, trap = search(model)
    if base is None:
        return {'status': 'inconsistent', 'obstruction': trap}
    orders = []; order_indices = {}; order_ranks = []; counterfactual = {}
    def intern(order):
        key = tuple(order)
        if key not in order_indices:
            order_indices[key] = len(orders); orders.append(order)
            order_ranks.append({p: i for i, p in enumerate(order)})
        return order_indices[key]
    intern(base)
    classifications = []; obstructions = []; obstruction_indices = {}; object_indices = {}
    def intern_obstruction(obj):
        if id(obj) in object_indices:
            return object_indices[id(obj)]
        key = json.dumps(obj, sort_keys=True, separators=(',', ':'))
        if key not in obstruction_indices:
            obstruction_indices[key] = len(obstructions); obstructions.append(obj)
        object_indices[id(obj)] = obstruction_indices[key]
        return obstruction_indices[key]
    for r, row in enumerate(model['rows']):
        good = sorted(row['good']); supports = {}; impossible = {}
        # All retained orders satisfy the entire input, so reuse their winners
        # here even when this row has a different counterfactual candidate set.
        # Ranks are constructed once per interned order, not once per row.
        for w, rank in enumerate(order_ranks):
            winner = min(row['present'], key=rank.get)
            supports.setdefault(model['owners'][winner], w)
        for p in good:
            owner = model['owners'][p]
            if owner in supports:
                continue
            # The added edges depend only on p and the provider set, not on
            # the row name. Reuse only literally identical force obligations.
            obligation = (p, tuple(sorted(row['present'])))
            if obligation not in counterfactual:
                counterfactual[obligation] = search(model, (r, p))
            order, obstruction = counterfactual[obligation]
            if order is not None:
                supports[owner] = intern(order)
            else:
                impossible[p] = obstruction
        owners = sorted(supports)
        label = 'ambiguous' if len(owners) > 1 else ('developer' if owners == ['developer'] else 'library')
        exclusions = [{'provider': p, 'obstruction': intern_obstruction(impossible[p])} for p in good if model['owners'][p] not in supports]
        classifications.append({'owners': owners, 'class': label,
                                'support': [[o, supports[o]] for o in owners], 'excluded': exclusions})
    return {'status': 'classified', 'orders': orders, 'obstructions': obstructions, 'regions': classifications}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input'); parser.add_argument('output')
    args = parser.parse_args()
    try:
        cert = infer(load(args.input))
        encoded = json.dumps(cert, separators=(',', ':')) + '\n'
        if len(encoded.encode('utf-8')) > 64 * 1024 * 1024:
            raise InputError('certificate exceeds replay file budget')
        Path(args.output).write_text(encoded, encoding='utf-8')
    except (InputError, ValueError, TypeError, KeyError, OSError, RecursionError) as exc:
        parser.exit(2, 'input rejected: ' + str(exc) + '\n')
if __name__ == '__main__':
    main()
