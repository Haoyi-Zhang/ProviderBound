"""File-free finite controls and retained three-provider record mutations."""
from pathlib import Path
import copy
import sys
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
from triple_study import census, direct_owners
from triple_report import load_records, validate, tables


class TripleStudyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.summary, cls.records = load_records()

    def test_complete_census(self):
        triples, _ = census()
        self.assertEqual(len(triples),4)
        self.assertEqual(sorted(len({row['package'] for row in triple}) for triple in triples),[1,1,3,3])

    def test_global_coupling_not_local_tie_break(self):
        graph = {'kind':'graph','owners':['developer','lib:B','lib:C'],'before':[],
                 'rows':[{'key':'shared','present':[0,1,2],'good':[0,1]},
                         {'key':'anchor','present':[0,1,2],'good':[1]}]}
        self.assertEqual(direct_owners(graph),{'shared':['lib:B'],'anchor':['lib:B']})
        graph['rows'] = graph['rows'][:1]
        self.assertEqual(direct_owners(graph)['shared'],['developer','lib:B'])

    def test_owner_quotient_and_inconsistency(self):
        graph = {'kind':'graph','owners':['pkg:same']*3,'before':[],
                 'rows':[{'key':'x','present':[0,1,2],'good':[0,1,2]}]}
        self.assertEqual(direct_owners(graph),{'x':['pkg:same']})
        graph['before'] = [[0,1],[1,0]]
        self.assertIsNone(direct_owners(graph))

    def test_all_retained_records_and_tables(self):
        self.assertEqual(len(validate(self.summary,self.records)),4)
        self.assertEqual(set(tables(self.summary,self.records)),{'triple-native.tex','triple-cost.tex'})

    def test_native_member_mutation_rejected(self):
        records = copy.deepcopy(self.records)
        name = next(iter(records[0]['native_entries']))
        records[0]['native_entries'][name] = '0'*64
        with self.assertRaises(ValueError):
            validate(self.summary,records)

    def test_missing_output_and_boolean_count_rejected(self):
        with self.assertRaises(ValueError):
            validate(self.summary,self.records[:-1])
        summary = copy.deepcopy(self.summary)
        summary['semantic']['native_ant_builds'] = True
        with self.assertRaises(ValueError):
            validate(summary,self.records)
        records = copy.deepcopy(self.records)
        records[0]['triple'] = True
        with self.assertRaises(ValueError):
            validate(self.summary,records)

    def test_changed_source_and_false_measurement_rejected(self):
        for kind in ('source','sample','size'):
            summary = copy.deepcopy(self.summary)
            if kind=='source':
                summary['source_bindings']['src/checker.py'] = '0'*64
            elif kind=='sample':
                summary['timings'][0]['producer']['seconds'][0] = float('nan')
            else:
                summary['timings'][0]['certificate_bytes'] += 1
            with self.subTest(kind=kind), self.assertRaises(ValueError):
                validate(summary,self.records)


if __name__ == '__main__':
    unittest.main()
