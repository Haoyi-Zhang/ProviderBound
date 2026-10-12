"""Benign same-information controls for the owner-label diagnostic."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from analyze_owner_granularity import analyze_pair, aggregate


class OwnerGranularityTests(unittest.TestCase):
    def test_same_package_removes_owner_gain_not_provider_gain(self):
        stores = [{'target': b'equal', 'probe': b'a'}, {'target': b'equal', 'probe': b'b'}]
        before = deepcopy(stores)
        archive = aggregate(analyze_pair(stores, ['lib:a', 'lib:b']))
        package = aggregate(analyze_pair(stores, ['deb:shared', 'deb:shared']))
        self.assertEqual(archive['strict_narrowings'], 2)
        self.assertEqual(package['strict_narrowings'], 0)
        self.assertEqual(archive['provider_narrowings'], package['provider_narrowings'])
        self.assertEqual(package['provider_narrowings'], 2)
        self.assertEqual(package['local_exact_rate'], 1.0)
        self.assertEqual(package['local_mean_set_size'], 1.0)
        self.assertEqual(stores, before)

    def test_distinct_package_labels_preserve_owner_gain(self):
        stores = [{'target': b'equal', 'probe': b'a'}, {'target': b'equal', 'probe': b'b'}]
        result = aggregate(analyze_pair(stores, ['deb:a', 'deb:b']))
        self.assertEqual(result['strict_narrowings'], 2)

    def test_equal_outputs_remain_ambiguous_without_order_evidence(self):
        result = aggregate(analyze_pair([{'target': b'equal'}] * 2, ['lib:a', 'lib:b']))
        self.assertEqual(result['certified_ambiguous'], 2)
        self.assertEqual(result['strict_narrowings'], 0)

    def test_developer_inclusion_policy_is_measured_separately(self):
        stores = [{'target': b'equal', 'probe': b'a'}, {'target': b'equal', 'probe': b'b'}]
        result = aggregate(analyze_pair(stores, ['developer', 'lib:b']))
        self.assertEqual(result['developer_scope_differences'], 1)
        self.assertEqual(result['strict_narrowings'], 2)

    def test_noncollision_regions_do_not_change_metric_denominator(self):
        result = aggregate(analyze_pair([{'target': b'equal', 'unique': b'u'},
                                         {'target': b'equal'}], ['lib:a', 'lib:b']))
        self.assertEqual(result['entry_regions'], 4)
        self.assertEqual(result['collision_observations'], 2)


if __name__ == '__main__':
    unittest.main()
