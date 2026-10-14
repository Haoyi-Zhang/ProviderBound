"""Owned interface/receipt controls; no malformed archives or external builder."""
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
from itertools import permutations
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import analyze_owner_granularity as granularity
import public_corpus


def direct_counts(stores, labels):
    """Independent tiny reference: literal full-map merges, no producer calls."""
    worlds = []
    keys = sorted({key for store in stores for key in store})
    for order in permutations(range(len(stores))):
        merged, winners = {}, {}
        for key in keys:
            for p in order:
                if key in stores[p]:
                    merged[key], winners[key] = stores[p][key], p
                    break
        worlds.append((merged, winners))
    result = {'collision_observations': 0, 'direct_developer_inclusions': 0,
              'strict_narrowings': 0, 'provider_narrowings': 0,
              'developer_scope_differences': 0}
    for observed, _ in worlds:
        compatible = [winner for content, winner in worlds if content == observed]
        for key in keys:
            present = [p for p in range(len(stores)) if key in stores[p]]
            if len(present) < 2:
                continue
            good = {p for p in present if stores[p][key] == observed[key]}
            possible = {winner[key] for winner in compatible}
            local, exact = {labels[p] for p in good}, {labels[p] for p in possible}
            result['collision_observations'] += 1
            result['direct_developer_inclusions'] += 'developer' in exact
            result['strict_narrowings'] += exact < local
            result['provider_narrowings'] += possible < good
            result['developer_scope_differences'] += ('developer' in exact) != ('developer' in local)
    return result


class ReviewContractTests(unittest.TestCase):
    def test_decision_counts_match_independent_literal_reference(self):
        controls = [
            ([{'target': b'equal', 'probe': b'a'}, {'target': b'equal', 'probe': b'b'}],
             ['developer', 'lib:b']),
            ([{'target': b'equal', 'probe': b'a'}, {'target': b'equal', 'probe': b'b'}],
             ['deb:shared', 'deb:shared']),
            ([{'target': b'equal'}, {'target': b'equal'}], ['developer', 'lib:b']),
            ([{'owned-a': b'a'}, {'owned-b': b'b'}], ['developer', 'lib:b'])]
        for stores, labels in controls:
            with self.subTest(labels=labels, stores=stores):
                actual = granularity.aggregate(granularity.analyze_pair(stores, labels))
                for field, value in direct_counts(stores, labels).items():
                    self.assertEqual(actual[field], value)
                n = actual['collision_observations']
                self.assertEqual(actual['same_information_direct_owner_matches'], n)
                self.assertEqual(actual['same_information_direct_scope_matches'], n)
                self.assertEqual(actual['certified_developer_inclusions'], actual['direct_developer_inclusions'])

    def test_two_provider_diagnostic_refuses_silent_inventory_omission(self):
        stores = [{"target": b"owned-equal"}, {"target": b"owned-equal"},
                  {"third-only": b"owned-third"}]
        with self.assertRaisesRegex(ValueError, "exactly two"):
            granularity.analyze_pair(stores, ["developer", "lib:b", "lib:c"])

    def test_no_collision_has_no_rate_not_a_division_failure(self):
        rows = granularity.analyze_pair([{"owned-a": b"a"}, {"owned-b": b"b"}],
                                        ["developer", "lib:b"])
        result = granularity.aggregate(rows)
        self.assertEqual(result["collision_observations"], 0)
        self.assertEqual(result["entry_regions"], 4)
        for field in ("local_exact_rate", "certified_exact_rate",
                      "local_mean_set_size", "certified_mean_set_size"):
            self.assertIsNone(result[field])

    def test_prebuilt_replay_does_not_claim_new_ant_execution(self):
        # One summary object drives the forty required orchestration slots.
        # This is a metadata test, not forty validated public cases. No archive
        # bytes are made or parsed and the mock never invokes _process_pair.
        counts = {key: 0 for key in ("regions", "collisions", "local_amb", "cert_amb",
                                     "narrow", "coupled", "oracle_mismatch", "ant_mismatch", "adapter_mismatch")}
        for method in ("catalogue_tiebreak", "inventory_size_proxy", "dependency",
                       "local_bytes", "certified", "trusted_trace"):
            for metric in ("observations", "set_size", "oracle_exact",
                           "oracle_conservative", "hidden_winner_covered"):
                counts[f"baseline.{method}.{metric}"] = 1
        result = {"rows": [{"build_id": "owned-ab"}, {"build_id": "owned-ba"}], "counts": counts,
                  "equal_outputs": True, "flips": 0, "cert_sizes": [1]}
        class Future:
            def result(self):
                return result
        class Pool:
            def __enter__(self):
                return self
            def __exit__(self, *args):
                pass
            def submit(self, *args):
                return Future()
        with TemporaryDirectory() as directory:
            folder = Path(directory)
            pair = {"pair_id": "owned", "left": "owned-a.jar", "right": "owned-b.jar", "kind": "equal-only"}
            with patch.object(public_corpus, "_read_csv", return_value=[pair] * 40), \
                    patch.object(public_corpus, "ProcessPoolExecutor", return_value=Pool()), \
                    patch.object(public_corpus, "as_completed", side_effect=lambda items: items), \
                    patch.object(public_corpus.Path, "is_file", return_value=True), \
                    patch.object(public_corpus.subprocess, "run") as builder:
                summary = public_corpus.run(folder / "out", workers=1, prebuilt=folder / "prebuilt")
                builder.assert_not_called()
                self.assertEqual(summary["actual_ant_builds"], 0)
                self.assertEqual(summary["output_archives_checked"], 80)
                self.assertEqual(summary["execution_mode"], "prebuilt-output-replay")
                self.assertIsNone(summary["builder"])
                self.assertIsNone(summary["ant_first_winner_mismatches"])


if __name__ == "__main__":
    unittest.main()
