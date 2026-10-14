"""Owned regression fixtures for the staged P010 claim auditor.

Only the named benign current science files are copied into owned temporary directories
under this tests directory. No upstream program or campaign is executed.
"""
from __future__ import annotations

import csv
import contextlib
import io
import importlib.util
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
        for relative in audit_module.JSON_FILES + audit_module.CSV_FILES:
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
