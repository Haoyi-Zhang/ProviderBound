"""Independent certificate replay. Does NOT call inference or fixed-point search.

Trust: this Python program, its interpreter/standard library, and the explicit
closed inventory plus owner labels. This is not a proof of inventory completeness.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

MAX_FILE_BYTES = 64 * 1024 * 1024

class Rejected(ValueError):
    pass

def demand(condition, message):
    if not condition:
        raise Rejected(message)

def no_duplicates(pairs):
    result = {}
    for key, value in pairs:
        demand(key not in result, 'repeated JSON field')
        result[key] = value
    return result

def load(path):
    with Path(path).open('rb') as stream:
        data = stream.read(MAX_FILE_BYTES + 1)
    demand(len(data) <= MAX_FILE_BYTES, 'file size limit')
    return json.loads(data.decode('utf-8'), object_pairs_hook=no_duplicates)

def read_model(raw):
    """Separately written inventory interpretation and graph validation."""
    demand(isinstance(raw, dict), 'input object')
    if raw.get('kind') == 'inventory':
        items = raw['providers']
        demand(isinstance(items, list) and 0 < len(items) <= 300, 'inventory size')
        owners = []; by_name = {}; names_seen = set()
        for i, item in enumerate(items):
            identifier = item['id']
            demand(isinstance(identifier, str) and identifier and identifier not in names_seen, 'provider id')
            names_seen.add(identifier); owners.append(item['owner'])
            rules = item['relocations']; starts = set()
            demand(isinstance(rules, list) and len(rules) <= 32, 'rule count')
            for rule in rules:
                demand(isinstance(rule, list) and len(rule) == 2, 'rule arity')
                a, b = rule
                demand(isinstance(a, str) and isinstance(b, str) and a and a.endswith('/') and b.endswith('/') and a not in starts, 'prefix rules')
                starts.add(a)
            original_names = set(); converted_names = set()
            for entry in item['entries']:
                original = entry['name']
                demand(isinstance(original, str) and original and original not in original_names, 'source entry name')
                original_names.add(original)
                demand(not (rules and original.endswith(('.class', '.dex'))), 'unsupported bytecode relocation')
                destination = original; best_length = -1
                for a, b in rules:
                    if original[:len(a)] == a and len(a) > best_length:
                        destination = b + original[len(a):]; best_length = len(a)
                demand(destination not in converted_names, 'non-injective within-provider transform')
                converted_names.add(destination)
                value = bytes.fromhex(entry['payload'])
                by_name.setdefault(destination, {})[i] = value
        observed = {}
        for entry in raw['observed']:
            key = entry['name']; demand(isinstance(key, str) and key and key not in observed, 'output name')
            observed[key] = bytes.fromhex(entry['payload'])
        demand(set(observed) == set(by_name), 'closed inventory union does not match output keys')
        rows = []
        for key in sorted(by_name):
            choices = by_name[key]
            rows.append({'key': key, 'present': sorted(choices),
                         'good': [p for p in sorted(choices) if choices[p] == observed[key]]})
        model = {'owners': owners, 'before': raw['before'], 'rows': rows}
    else:
        demand(raw.get('kind') == 'graph', 'input language')
        model = {key: raw[key] for key in ('owners', 'before', 'rows')}
    owner = model['owners']
    demand(isinstance(owner, list) and 1 <= len(owner) <= 300, 'provider limit')
    demand(all(isinstance(s, str) and bool(s) for s in owner), 'owner strings')
    n = len(owner)
    def index(x):
        return type(x) is int and 0 <= x < n
    rows = model['rows']; before = model['before']
    demand(isinstance(rows, list) and len(rows) <= 20_000, 'region limit')
    demand(isinstance(before, list), 'precedence list')
    for pair in before:
        demand(isinstance(pair, list) and len(pair) == 2 and all(index(p) for p in pair), 'precedence endpoints')
    demand(len(before) == len(set(map(tuple, before))), 'duplicate precedence')
    keys = set(); entries = len(before)
    for row in rows:
        demand(isinstance(row, dict) and set(row) == {'key', 'present', 'good'}, 'row fields')
        key = row['key']
        demand(isinstance(key, str) and key and key not in keys, 'row name')
        keys.add(key)
        for field in ('present', 'good'):
            a = row[field]
            demand(isinstance(a, list) and all(index(p) for p in a) and len(a) == len(set(a)), 'row index set')
        demand(set(row['good']) <= set(row['present']), 'good subset')
        entries += len(row['present'])
    demand(entries <= 250_000, 'incidence limit')
    return model

def verify(raw, cert):
    """Raise Rejected for a false or malformed certificate; return semantic labels."""
    model = read_model(raw)
    n = len(model['owners']); rows = model['rows']; K = set(map(tuple, model['before']))
    present = [set(row['present']) for row in rows]
    good = [set(row['good']) for row in rows]
    def idx(x, upper):
        return type(x) is int and 0 <= x < upper
    def obstruction(obj, force=None):
        demand(isinstance(obj, dict), 'obstruction object')
        if obj.get('kind') == 'missing':
            demand(set(obj) == {'kind', 'row'}, 'missing fields')
            r = obj['row']
            demand(idx(r, len(rows)) and not present[r], 'missing row claim')
            return
        demand(set(obj) == {'kind', 'nodes', 'reasons'} and obj['kind'] == 'trap', 'trap fields')
        nodes = obj['nodes']; reasons = obj['reasons']
        demand(isinstance(nodes, list) and nodes and all(idx(v, n) for v in nodes) and len(nodes) == len(set(nodes)), 'nonempty trap set')
        U = set(nodes)
        demand(isinstance(reasons, list) and len(reasons) == len(U), 'trap reason coverage')
        covered = set()
        for reason in reasons:
            demand(isinstance(reason, dict), 'reason object')
            v = reason.get('node'); kind = reason.get('kind')
            demand(idx(v, n) and v in U and v not in covered, 'one reason per trap node')
            covered.add(v)
            if kind in ('before', 'forced'):
                demand(set(reason) == {'node', 'kind', 'pred'}, 'precedence reason fields')
                p = reason['pred']; demand(idx(p, n) and p in U, 'blocked predecessor in trap')
                if kind == 'before':
                    demand((p, v) in K, 'base precedence edge')
                else:
                    demand(force is not None and p == force[1] and v != p and v in present[force[0]], 'counterfactual precedence edge')
            else:
                demand(kind == 'row' and set(reason) == {'node', 'kind', 'row'}, 'row reason fields')
                r = reason['row']
                demand(idx(r, len(rows)), 'reason row index')
                demand(v in present[r] and v not in good[r] and good[r] <= U, 'self-blocking observation')
        demand(covered == U, 'trap node coverage')
    demand(isinstance(cert, dict), 'certificate object')
    if cert.get('status') == 'inconsistent':
        demand(set(cert) == {'status', 'obstruction'}, 'inconsistent fields')
        obstruction(cert['obstruction'])
        return {'status': 'inconsistent'}
    demand(cert.get('status') == 'classified' and set(cert) == {'status', 'orders', 'obstructions', 'regions'}, 'classification fields')
    orders = cert['orders']; classes = cert['regions']; bank = cert['obstructions']
    demand(isinstance(bank, list) and len(bank) <= sum(len(x) for x in good), 'obstruction bank limit')
    used_bank = set(); validated_forces = set()
    demand(isinstance(orders, list) and orders, 'at least one existence witness')
    demand(len(orders) <= 1 + sum(len(x) for x in good), 'witness count limit')
    demand(isinstance(classes, list) and len(classes) == len(rows), 'complete region coverage')
    winners = []
    for order in orders:
        demand(isinstance(order, list) and len(order) == n and all(idx(p, n) for p in order) and len(set(order)) == n, 'witness permutation')
        rank = [0] * n
        for k, p in enumerate(order):
            rank[p] = k
        demand(all(rank[a] < rank[b] for a, b in K), 'witness violates precedence')
        row_winners = []
        for r in range(len(rows)):
            demand(bool(present[r]), 'output has no candidate provider')
            winner = min(present[r], key=lambda p: rank[p])
            demand(winner in good[r], 'witness violates output bytes')
            row_winners.append(winner)
        winners.append(row_winners)
    answer = []
    for r, item in enumerate(classes):
        demand(isinstance(item, dict) and set(item) == {'owners', 'class', 'support', 'excluded'}, 'region certificate fields')
        labels = item['owners']
        demand(isinstance(labels, list) and labels and all(isinstance(o, str) and o for o in labels) and labels == sorted(set(labels)), 'nonempty canonical owner set')
        label_set = set(labels); support = item['support']
        demand(isinstance(support, list) and len(support) == len(labels), 'positive witness coverage')
        supported = set()
        for pair in support:
            demand(isinstance(pair, list) and len(pair) == 2, 'support shape')
            o, w = pair
            demand(isinstance(o, str) and o in label_set and o not in supported and idx(w, len(orders)), 'support index')
            demand(model['owners'][winners[w][r]] == o, 'witness has a different owner')
            supported.add(o)
        demand(supported == label_set, 'all owners witnessed')
        exclusions = item['excluded']; expected = {p for p in good[r] if model['owners'][p] not in label_set}
        demand(isinstance(exclusions, list) and len(exclusions) == len(expected), 'negative witness coverage')
        excluded = set()
        present_key = None
        for block in exclusions:
            demand(isinstance(block, dict) and set(block) == {'provider', 'obstruction'}, 'excluded provider fields')
            p = block['provider']
            demand(idx(p, n) and p in expected and p not in excluded, 'excluded provider index')
            oi = block['obstruction']
            demand(idx(oi, len(bank)), 'obstruction index')
            # Reuse only an identical obstruction and the identical forced edge set.
            if present_key is None:
                present_key = tuple(sorted(present[r]))
            obligation = (oi, p, present_key)
            if obligation not in validated_forces:
                obstruction(bank[oi], (r, p)); validated_forces.add(obligation)
            used_bank.add(oi); excluded.add(p)
        demand(excluded == expected, 'all excluded candidates refuted')
        expected_class = 'ambiguous' if len(labels) > 1 else ('developer' if labels == ['developer'] else 'library')
        demand(item['class'] == expected_class, 'classification category')
        answer.append({'key': rows[r]['key'], 'owners': labels, 'class': expected_class})
    demand(used_bank == set(range(len(bank))), 'unused obstruction bank entry')
    return {'status': 'classified', 'regions': answer}

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('input'); p.add_argument('certificate')
    args = p.parse_args()
    try:
        answer = verify(load(args.input), load(args.certificate))
        print(json.dumps(answer, indent=2))
    except (Rejected, ValueError, TypeError, KeyError, OSError, RecursionError) as exc:
        p.exit(2, 'REJECT: ' + str(exc) + '\n')
if __name__ == '__main__':
    main()
