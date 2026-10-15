"""Owned regression fixtures for the staged P010 claim auditor.

Only the named benign current science files are copied into owned temporary directories
under this tests directory. No upstream program or campaign is executed.
"""
from __future__ import annotations

import csv
import contextlib
import io
import importlib.util
import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parent
SCRIPT = HERE.parent / "scripts" / "audit_claims.py"
CURRENT = Path(os.environ.get(
    "P010_ARTIFACT",
    str(HERE.parent),
)).resolve()
spec = importlib.util.spec_from_file_location("staged_audit_claims", SCRIPT)
audit_module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(audit_module)


class AuditClaimsTests(unittest.TestCase):
    def fixture(self):
        holder = tempfile.TemporaryDirectory(prefix="p010-claim-", dir=HERE)
        self.addCleanup(holder.cleanup)
        root = Path(holder.name)
        for relative in dict.fromkeys(audit_module.JSON_FILES + audit_module.CSV_FILES
                                      + audit_module.DIAGNOSTIC_BINDINGS):
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((CURRENT / relative).read_bytes())
        return root

    def assert_rejected(self, root: Path, needle: str):
        report = audit_module.audit(root)
        self.assertEqual(report["status"], "FAIL")
        self.assertEqual(report["claims"], {})
        self.assertTrue(report["errors"])
        self.assertIn(needle, "\n".join(report["errors"]))

    def test_correct_actual_current_sources_pass(self):
        report = audit_module.audit(CURRENT)
        self.assertEqual(report["status"], "PASS")
        self.assertEqual(report["errors"], [])
        self.assertEqual(report["claims"]["finite_labelled_models"], 90582)
        self.assertEqual(report["claims"]["debian_package_additional_owner_resolutions"], 0)
        self.assertNotIn("107", str(report["claims"]))
        for totals in report["claims"]["retained_same_information_diagnostic"].values():
            self.assertEqual(totals["same_information_direct_owner_matches"], 8156)
            self.assertEqual(totals["direct_developer_inclusions"], 0)

    def diagnostic(self, root):
        path = root / audit_module.JSON_FILES[6]
        return path, json.loads(path.read_text(encoding="utf-8"))

    def test_diagnostic_and_receipt_are_required_named_sources(self):
        for relative in audit_module.JSON_FILES[6:9]:
            with self.subTest(relative=relative):
                root = self.fixture()
                (root / relative).unlink()
                self.assert_rejected(root, "missing scientific source: " + relative)

    def test_diagnostic_decision_fields_are_required_strict_counts(self):
        fields = ("local_developer_inclusions", "certified_developer_inclusions",
                  "direct_developer_inclusions", "developer_scope_differences",
                  "same_information_direct_owner_matches",
                  "same_information_direct_scope_matches")
        for field in fields:
            for mutation in ("missing", "boolean", "wrong"):
                with self.subTest(field=field, mutation=mutation):
                    root = self.fixture()
                    path, value = self.diagnostic(root)
                    counts = value["observations"][0]["counts"]
                    if mutation == "missing":
                        del counts[field]
                    else:
                        counts[field] = True if mutation == "boolean" else counts[field] + 1
                    path.write_text(json.dumps(value), encoding="utf-8")
                    self.assert_rejected(root, field)

    def test_diagnostic_observation_membership_and_pair_binding(self):
        for mutation in ("duplicate", "pair", "scheme", "missing"):
            with self.subTest(mutation=mutation):
                root = self.fixture()
                path, value = self.diagnostic(root)
                if mutation == "duplicate":
                    value["observations"][1] = value["observations"][0]
                elif mutation == "pair":
                    value["observations"][0]["pair_id"] = "different-owned-pair"
                elif mutation == "scheme":
                    value["observations"][0]["scheme"] = "different-owned-schema"
                else:
                    value["observations"].pop()
                path.write_text(json.dumps(value), encoding="utf-8")
                report = audit_module.audit(root)
                self.assertEqual(report["status"], "FAIL")
                self.assertEqual(report["claims"], {})

    def test_diagnostic_aggregate_must_equal_its_rows(self):
        root = self.fixture()
        path, value = self.diagnostic(root)
        value["metrics"]["archive"]["same_information_direct_owner_matches"] += 1
        path.write_text(json.dumps(value), encoding="utf-8")
        self.assert_rejected(root, "same_information_direct_owner_matches")

    def test_coordinated_diagnostic_edits_still_bind_to_build_census(self):
        root = self.fixture()
        path, value = self.diagnostic(root)
        for key in ("collision_observations", "same_information_direct_owner_matches",
                    "same_information_direct_scope_matches"):
            value["observations"][0]["counts"][key] += 1
            value["metrics"]["archive"][key] += 1
        path.write_text(json.dumps(value), encoding="utf-8")
        self.assert_rejected(root, "collision_observations")

    def test_diagnostic_execution_receipt_cannot_claim_native_runs(self):
        for key in ("actual_ant_builds", "provider_code_executions",
                    "archive_extractions", "public_zip_output_replays"):
            with self.subTest(key=key):
                root = self.fixture()
                path = root / audit_module.JSON_FILES[7]
                value = json.loads(path.read_text(encoding="utf-8"))
                value[key] = 1
                path.write_text(json.dumps(value), encoding="utf-8")
                self.assert_rejected(root, key)

    def test_changed_diagnostic_producer_requires_new_evidence(self):
        root = self.fixture()
        path = root / "scripts/analyze_owner_granularity.py"
        with path.open("a", encoding="utf-8") as stream:
            stream.write("\n# owned benign source-change fixture\n")
        self.assert_rejected(root, "scripts/analyze_owner_granularity.py")

    def test_changed_owner_labels_cannot_inherit_zero_scope_counts(self):
        root = self.fixture()
        path = root / "inputs/public/providers.csv"
        text = path.read_text(encoding="utf-8")
        text = text.replace("lib:batik-all-1.18", "developer", 1)
        path.write_text(text, encoding="utf-8")
        binding_path = root / audit_module.JSON_FILES[8]
        bindings = json.loads(binding_path.read_text(encoding="utf-8"))
        bindings["inputs/public/providers.csv"] = hashlib.sha256(path.read_bytes()).hexdigest()
        binding_path.write_text(json.dumps(bindings), encoding="utf-8")
        self.assert_rejected(root, "all-library owner labels")

    def test_self_report_with_arbitrary_numbers_cannot_replace_missing_source(self):
        root = self.fixture()
        (root / "inputs/public/selection.json").unlink()
        docs = root / "docs"
        docs.mkdir()
        (docs / "claim-evidence-index.json").write_text(
            json.dumps({"all_numbers": [107, 5671, 4, 42, 14, 43, 40, 80, 90582, 165630, 3471]}),
            encoding="utf-8",
        )
        self.assert_rejected(root, "missing scientific source: inputs/public/selection.json")

    def test_mutated_semantic_summary_field_fails(self):
        root = self.fixture()
        path = root / "results/current/public/summary.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["region_observations"] += 1
        path.write_text(json.dumps(value), encoding="utf-8")
        self.assert_rejected(root, "region_observations")

    def test_missing_semantic_field_fails(self):
        root = self.fixture()
        path = root / "results/current/public/summary.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        del value["region_observations"]
        path.write_text(json.dumps(value), encoding="utf-8")
        self.assert_rejected(root, "missing field")

    def test_mutated_csv_census_fails(self):
        root = self.fixture()
        path = root / "results/current/public/cases.csv"
        with path.open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream)
            fields = reader.fieldnames
            rows = list(reader)
        rows[0]["entry_regions"] = str(int(rows[0]["entry_regions"]) + 1)
        with path.open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
        self.assert_rejected(root, "region_observations")

    def test_duplicate_json_key_fails(self):
        root = self.fixture()
        path = root / "results/current/public/summary.json"
        contents = path.read_text(encoding="utf-8")
        contents = contents.replace('"region_observations": 165630,', '"region_observations": 165630, "region_observations": 165630,', 1)
        path.write_text(contents, encoding="utf-8")
        self.assert_rejected(root, "duplicate JSON key")

    def test_duplicate_csv_column_fails(self):
        root = self.fixture()
        path = root / "inputs/public/collision_pairs.csv"
        contents = path.read_text(encoding="utf-8")
        first, rest = contents.split("\n", 1)
        path.write_text(first + ",pair_id\n" + rest, encoding="utf-8")
        self.assert_rejected(root, "missing/duplicate CSV columns")

    def test_boolean_in_integer_field_fails(self):
        root = self.fixture()
        path = root / "inputs/public/selection.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["provider_count"] = True
        path.write_text(json.dumps(value), encoding="utf-8")
        self.assert_rejected(root, "expected strict integer")

    def test_boolean_in_nested_category_count_fails(self):
        root = self.fixture()
        path = root / "inputs/public/selection.json"
        value = json.loads(path.read_text(encoding="utf-8"))
        value["category_counts"]["mixed"] = True
        path.write_text(json.dumps(value), encoding="utf-8")
        self.assert_rejected(root, "category_counts/mixed")

    def test_nonfinite_json_fails(self):
        root = self.fixture()
        path = root / "results/current/oracle_summary.json"
        contents = path.read_text(encoding="utf-8")
        contents = contents.replace('"mismatches": 0,', '"mismatches": NaN,', 1)
        path.write_text(contents, encoding="utf-8")
        self.assert_rejected(root, "non-finite JSON constant")

    def test_float_overflow_json_fails(self):
        root = self.fixture()
        path = root / "results/current/oracle_summary.json"
        contents = path.read_text(encoding="utf-8")
        contents = contents.replace('"cpu_seconds": 4.272078339999999,', '"cpu_seconds": 1e999,', 1)
        path.write_text(contents, encoding="utf-8")
        self.assert_rejected(root, "non-finite JSON number")

    def test_default_cli_stdout_does_not_write_docs(self):
        root = self.fixture()
        capture = io.StringIO()
        with contextlib.redirect_stdout(capture):
            status = audit_module.main(["--artifact", str(root)])
        self.assertEqual(status, 0)
        self.assertEqual(json.loads(capture.getvalue())["status"], "PASS")
        self.assertFalse((root / "docs").exists())

    def test_cli_rejects_output_inside_artifact(self):
        root = self.fixture()
        destination = root / "docs" / "claim-evidence-index.json"
        with contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit) as context:
                audit_module.main(["--artifact", str(root), "--output-json", str(destination)])
        self.assertEqual(context.exception.code, 2)
        self.assertFalse(destination.exists())


if __name__ == "__main__":
    unittest.main()
