"""Finite, file-free regressions for canonical force-key preparation.

The literal-order reference below uses only the mathematical graph semantics;
it does not call normalization, inference, search, or certificate replay.
"""
from copy import deepcopy
from itertools import combinations, permutations, product
from pathlib import Path
import builtins
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
import producer
import checker


def graph(owners, rows, edges=()):
    return {'kind': 'graph', 'owners': list(owners),
            'before': [list(edge) for edge in edges],
            'rows': [{'key': f'r{i}', 'present': list(p), 'good': list(g)}
                     for i, (p, g) in enumerate(rows)]}


def subsets(values):
    values = tuple(values)
    for size in range(len(values) + 1):
        yield from combinations(values, size)


def graph_models():
    """Exactly the nonempty-present, <=3-provider, <=2-row finite family."""
    for n in range(1, 4):
        row_choices = [(p, g) for p in subsets(range(n)) if p
                       for g in subsets(p)]
        edge_choices = tuple((a, b) for a in range(n) for b in range(n) if a != b)
        owner_maps = (['developer'] + [f'lib:{p}' for p in range(1, n)],
                      ['lib:shared'] * n)
        for edges in subsets(edge_choices):
            for count in range(3):
                for rows in product(row_choices, repeat=count):
                    for owners in owner_maps:
                        yield graph(owners, rows, edges)


def literal_answer(raw):
    possibilities = [set() for _ in raw['rows']]
    feasible = False
    for order in permutations(range(len(raw['owners']))):
        positions = {p: i for i, p in enumerate(order)}
        if any(positions[a] >= positions[b] for a, b in raw['before']):
            continue
        winners = []
        for row in raw['rows']:
            first = next((p for p in order if p in row['present']), None)
            if first is None or first not in row['good']:
                break
            winners.append(first)
        else:
            feasible = True
            for labels, p in zip(possibilities, winners):
                labels.add(raw['owners'][p])
    if not feasible:
        return {'status': 'inconsistent'}
    regions = []
    for row, labels in zip(raw['rows'], possibilities):
        owners = sorted(labels)
        category = ('ambiguous' if len(owners) > 1 else
                    'developer' if owners == ['developer'] else 'library')
        regions.append({'key': row['key'], 'owners': owners, 'class': category})
    return {'status': 'classified', 'regions': regions}


def forced_rows():
    return graph(['developer', 'lib:1', 'lib:2', 'lib:3'],
                 [([3, 1, 0, 2], [2, 0, 3, 1]),
                  ([2, 3, 1, 0], [1, 0, 2, 3]),
                  ([2, 0, 1], [2, 1, 0])],
                 [(0, 1), (0, 2), (0, 3)])


class PresentProviderTupleTests(unittest.TestCase):
    def test_one_tuple_per_queried_row_and_exact_query_count(self):
        raw = forced_rows()
        counts = [0] * len(raw['rows'])

        def sort(values, *args, **kwargs):
            for i, row in enumerate(raw['rows']):
                if values is row['present']:
                    counts[i] += 1
            return builtins.sorted(values, *args, **kwargs)

        with patch.object(producer, 'sorted', sort, create=True), \
                patch.object(producer, 'search', wraps=producer.search) as search:
            cert = producer.infer(raw)
        self.assertEqual(counts, [1, 1, 1])
        self.assertEqual(search.call_count, 6)  # base + 3 full-set + 2 smaller-set
        self.assertEqual(checker.verify(raw, cert), literal_answer(raw))

    def test_checker_tuple_once_per_exclusion_row(self):
        raw = forced_rows()
        cert = producer.infer(raw)
        counts = {frozenset(row['present']): 0 for row in raw['rows']}

        def sort(values, *args, **kwargs):
            if isinstance(values, set) and frozenset(values) in counts:
                counts[frozenset(values)] += 1
            return builtins.sorted(values, *args, **kwargs)

        with patch.object(checker, 'sorted', sort, create=True):
            self.assertEqual(checker.verify(raw, cert), literal_answer(raw))
        self.assertEqual(counts, {frozenset(range(4)): 2, frozenset(range(3)): 1})

    def test_zero_queries_do_not_prepare_tuple(self):
        raw = graph(['lib:shared'] * 3, [([2, 0, 1], [0, 1, 2])])
        sorts = [0, 0]

        def producer_sort(values, *args, **kwargs):
            if values is raw['rows'][0]['present']:
                sorts[0] += 1
            return builtins.sorted(values, *args, **kwargs)

        def checker_sort(values, *args, **kwargs):
            if isinstance(values, set) and values == {0, 1, 2}:
                sorts[1] += 1
            return builtins.sorted(values, *args, **kwargs)

        with patch.object(producer, 'sorted', producer_sort, create=True), \
                patch.object(producer, 'search', wraps=producer.search) as search:
            cert = producer.infer(raw)
        with patch.object(checker, 'sorted', checker_sort, create=True):
            self.assertEqual(checker.verify(raw, cert), literal_answer(raw))
        self.assertEqual(search.call_count, 1)
        self.assertEqual(sorts, [0, 0])

    def test_no_rows_empty_candidates_and_self_cycle(self):
        cases = (graph(['developer'], []),
                 graph(['developer'], [([], [])]),
                 graph(['developer'], [([0], [0])], [(0, 0)]))
        for raw in cases:
            with self.subTest(raw=raw):
                self.assertEqual(checker.verify(raw, producer.infer(raw)), literal_answer(raw))

    def test_witness_reuse_with_different_present_sets(self):
        raw = graph(['developer', 'lib:1', 'lib:2'],
                    [([1, 0], [0, 1]), ([2, 0], [0, 2]), ([2, 1, 0], [1, 2, 0])])
        with patch.object(producer, 'search', wraps=producer.search) as search:
            cert = producer.infer(raw)
        self.assertEqual(search.call_count, 3)
        self.assertEqual(len(cert['orders']), 3)
        self.assertEqual(checker.verify(raw, cert), literal_answer(raw))

    def test_exclusion_reasons_and_scope_remain_mandatory(self):
        raw = forced_rows()
        original = producer.infer(raw)
        mutations = []
        for field, value in (('provider', False), ('provider', 99), ('obstruction', False),
                             ('obstruction', 99)):
            bad = deepcopy(original)
            bad['regions'][0]['excluded'][0][field] = value
            mutations.append(bad)
        bad = deepcopy(original)
        bad['regions'][0]['excluded'].pop()
        mutations.append(bad)
        bad = deepcopy(original)
        bad['regions'][0]['excluded'][1] = deepcopy(bad['regions'][0]['excluded'][0])
        mutations.append(bad)
        bad = deepcopy(original)
        bad['regions'][0]['excluded'][1]['obstruction'] = bad['regions'][0]['excluded'][0]['obstruction']
        mutations.append(bad)
        bad = deepcopy(original)
        bad['obstructions'][0]['reasons'] = []
        mutations.append(bad)
        bad = deepcopy(original)
        bad['obstructions'].append(deepcopy(bad['obstructions'][0]))
        mutations.append(bad)
        for i, bad in enumerate(mutations):
            with self.subTest(mutation=i), self.assertRaises(checker.Rejected):
                checker.verify(raw, bad)

    def test_admission_stays_strict(self):
        original = forced_rows()
        for field, value in (('present', [False, 1, 2, 3]), ('present', [0, 1, 1, 3]),
                             ('good', [99]), ('good', [False])):
            raw = deepcopy(original)
            raw['rows'][0][field] = value
            with self.subTest(field=field, value=value):
                with self.assertRaises(producer.InputError):
                    producer.infer(raw)
                with self.assertRaises(checker.Rejected):
                    checker.read_model(raw)

    def test_frozen_finite_family_against_literal_orders(self):
        count = 0
        for raw in graph_models():
            cert = producer.infer(raw)
            self.assertEqual(checker.verify(raw, cert), literal_answer(raw), raw)
            count += 1
        self.assertEqual(count, 90582)


if __name__ == '__main__':
    unittest.main()
