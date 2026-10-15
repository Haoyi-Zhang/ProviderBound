#!/usr/bin/env python3
"""Audit current P010 quantitative claims against named scientific inputs only.

This is a read-only verifier. It never scans the artifact tree, treats a number's
mere occurrence as evidence, or reads reports/claim indexes/process tables.
Without --output-json the compact result goes to stdout. An explicit output must
be outside the artifact root. It does not run an experiment or a build.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


class AuditError(ValueError):
    pass


JSON_FILES = (
    "results/current/oracle_summary.json",
    "results/current/campaign_summary.json",
    "inputs/public/selection.json",
    "results/current/public/summary.json",
    "results/current/scale_summary.json",
    "results/owner-granularity.json",
    "results/diagnostics/current/owner-granularity.json",
    "results/diagnostics/current/receipt.json",
    "results/diagnostics/current/input-source-sha256.json",
)
CSV_FILES = (
    "results/current/oracle_details.csv",
    "results/current/cases.csv",
    "inputs/public/providers.csv",
    "inputs/public/collision_pairs.csv",
    "results/current/public/cases.csv",
)
# These files produced the retained diagnostic. Auditor/test changes do not
# rewrite that execution's receipt or make its earlier test run current.
DIAGNOSTIC_BINDINGS = (
    "scripts/analyze_owner_granularity.py",
    "scripts/reproduce_diagnostics.py",
    "src/archive_producer.py",
    "src/archive_checker.py",
    "src/producer.py",
    "src/checker.py",
    "inputs/public/providers.csv",
    "inputs/public/collision_pairs.csv",
    "inputs/public/selection.json",
    "results/current/public/cases.csv",
)


def unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out = {}
    for key, value in pairs:
        if key in out:
            raise AuditError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def bad_constant(value: str) -> None:
    raise AuditError(f"non-finite JSON constant: {value}")


def finite_tree(value: Any, location: str) -> None:
    if isinstance(value, float) and not math.isfinite(value):
        raise AuditError(f"non-finite JSON number at {location}")
    if isinstance(value, dict):
        for key, member in value.items():
            finite_tree(member, f"{location}/{key}")
    elif isinstance(value, list):
        for index, member in enumerate(value):
            finite_tree(member, f"{location}/{index}")


def source(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise AuditError(f"source escapes artifact root: {relative}")
    if not path.is_file():
        raise AuditError(f"missing scientific source: {relative}")
    return path


def read_json(root: Path, relative: str) -> Any:
    try:
        value = json.loads(
            source(root, relative).read_text(encoding="utf-8"),
            object_pairs_hook=unique_object,
            parse_constant=bad_constant,
        )
        finite_tree(value, relative)
        return value
    except (UnicodeError, OSError, json.JSONDecodeError) as exc:
        raise AuditError(f"invalid JSON {relative}: {exc}") from exc


def read_csv(root: Path, relative: str, columns: tuple[str, ...]) -> list[dict[str, str]]:
    try:
        with source(root, relative).open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream, strict=True)
            header = reader.fieldnames
            if header is None or len(header) != len(set(header)) or any(c not in header for c in columns):
                raise AuditError(f"missing/duplicate CSV columns: {relative}")
            rows = list(reader)
        if any(None in row or any(value is None for value in row.values()) for row in rows):
            raise AuditError(f"malformed CSV row: {relative}")
        return rows
    except (UnicodeError, OSError, csv.Error) as exc:
        raise AuditError(f"invalid CSV {relative}: {exc}") from exc


def member(obj: Any, key: str, location: str) -> Any:
    if not isinstance(obj, dict) or key not in obj:
        raise AuditError(f"missing field {location}/{key}")
    return obj[key]


def integer(value: Any, location: str) -> int:
    if type(value) is not int:
        raise AuditError(f"expected strict integer at {location}; got {type(value).__name__}")
    return value


def csv_integer(row: dict[str, str], column: str, location: str) -> int:
    value = row[column]
    if not re.fullmatch(r"(?:0|[1-9][0-9]*)", value):
        raise AuditError(f"expected unsigned decimal CSV integer at {location}/{column}")
    return int(value)


def exact(observed: Any, expected: Any, location: str) -> None:
    if type(observed) is not type(expected):
        raise AuditError(f"semantic mismatch at {location}: observed {observed!r}, expected {expected!r}")
    if isinstance(expected, dict):
        if observed.keys() != expected.keys():
            raise AuditError(f"semantic mismatch at {location}: keys differ")
        for key in expected:
            exact(observed[key], expected[key], f"{location}/{key}")
        return
    if isinstance(expected, list):
        if len(observed) != len(expected):
            raise AuditError(f"semantic mismatch at {location}: list length differs")
        for index, (actual, wanted) in enumerate(zip(observed, expected)):
            exact(actual, wanted, f"{location}/{index}")
        return
    if observed != expected:
        raise AuditError(f"semantic mismatch at {location}: observed {observed!r}, expected {expected!r}")


def field(obj: Any, key: str, expected: int, location: str) -> int:
    observed = integer(member(obj, key, location), f"{location}/{key}")
    exact(observed, expected, f"{location}/{key}")
    return observed


def csv_sum(rows: list[dict[str, str]], column: str, relative: str) -> int:
    return sum(csv_integer(row, column, f"{relative}:row{index}") for index, row in enumerate(rows, 2))


def audit_diagnostic(root, data, builds, providers, owner):
    """Bind the retained direct comparison, without running provider programs."""
    relative, receipt_path, bindings_path = JSON_FILES[6:9]
    value, receipt, bindings = (data[name] for name in JSON_FILES[6:9])
    for name in DIAGNOSTIC_BINDINGS:
        recorded = member(bindings, name, bindings_path)
        if type(recorded) is not str or not re.fullmatch(r"[0-9a-f]{64}", recorded):
            raise AuditError(f"invalid diagnostic source binding: {name}")
        actual = hashlib.sha256(source(root, name).read_bytes()).hexdigest()
        exact(actual, recorded, bindings_path + ":" + name)

    # The zero developer counts below depend on this supplied label census,
    # not on a claim that the labels constitute independent ownership truth.
    metadata = {row["archive"]: row for row in providers}
    if any(not row["owner"].startswith("lib:") for row in providers):
        raise AuditError("retained diagnostic requires its all-library owner labels")
    for key, count in (("provider_archives", 43), ("pair_cases", 40),
                       ("modeled_outputs_per_schema", 80),
                       ("retained_case_count_checks", 80),
                       ("archive_adapter_disagreements", 0),
                       ("certificate_oracle_disagreements", 0)):
        field(value, key, count, relative)
    for key in ("actual_ant_builds", "provider_code_executions",
                "archive_extractions", "public_zip_output_replays"):
        field(receipt, key, 0, receipt_path)
    for key, count in (("label_schemas", 2),
                       ("modeled_outputs_per_label_schema", 80),
                       ("collision_observations_per_schema", 8156)):
        field(receipt, key, count, receipt_path)
    schemas = ("archive", "debian_package")
    exact(set(member(value, "label_schemas", relative)), set(schemas), relative + ":label schemas")
    pair_rows = member(value, "pairs", relative)
    exact(pair_rows, member(owner, "pairs", JSON_FILES[5]), relative + ":retained pair rows")
    for pair in pair_rows:
        names = member(pair, "archives", relative)
        scheme = member(pair, "scheme", relative)
        if type(names) is not list or len(names) != 2 or any(name not in metadata for name in names):
            raise AuditError("invalid diagnostic provider pair")
        if scheme not in schemas:
            raise AuditError("unknown diagnostic label scheme")
        labels = [metadata[name]["owner"] if scheme == "archive"
                  else "deb:" + metadata[name]["package"] for name in names]
        exact(member(pair, "labels", relative), labels, relative + ":pair labels")

    observations = member(value, "observations", relative)
    if type(observations) is not list or len(observations) != 160:
        raise AuditError("retained diagnostic requires 160 observations")
    expected_builds = {row["build_id"]: row for row in builds}
    decision_fields = ("local_developer_inclusions", "certified_developer_inclusions",
                       "direct_developer_inclusions", "developer_scope_differences",
                       "same_information_direct_owner_matches",
                       "same_information_direct_scope_matches")
    totals = {}
    for scheme in schemas:
        rows = [row for row in observations if member(row, "scheme", relative) == scheme]
        exact(len(rows), 80, relative + ":" + scheme + ":row count")
        ids = [member(row, "build_id", relative) for row in rows]
        if any(type(name) is not str for name in ids) or len(set(ids)) != 80:
            raise AuditError("duplicate/invalid diagnostic build ID")
        exact(set(ids), set(expected_builds), relative + ":" + scheme + ":build IDs")
        sums = Counter()
        for row in rows:
            build = expected_builds[row["build_id"]]
            location = relative + ":" + scheme + ":" + row["build_id"]
            exact(member(row, "pair_id", location), build["pair_id"], location + ":pair ID")
            counts = member(row, "counts", location)
            n = csv_integer(build, "collision_regions", CSV_FILES[4])
            field(counts, "collision_observations", n, location)
            field(counts, "entry_regions", csv_integer(build, "entry_regions", CSV_FILES[4]), location)
            for key in decision_fields:
                field(counts, key, n if key.startswith("same_information_") else 0, location)
                sums[key] += counts[key]
            for key, column in (("local_ambiguous", "local_ambiguous_regions"),
                                ("certified_ambiguous", "certified_ambiguous_regions"),
                                ("strict_narrowings", "global_narrowings")):
                expected = csv_integer(build, column, CSV_FILES[4]) if scheme == "archive" else 0
                exact(integer(counts.get(key, 0), location + ":" + key), expected, location + ":" + key)
            field(counts, "provider_narrowings", csv_integer(build, "global_narrowings", CSV_FILES[4]), location)
            sums["collision_observations"] += n
        metrics = member(member(value, "metrics", relative), scheme, relative)
        for key, count in sums.items():
            field(metrics, key, count, relative + ":metrics/" + scheme)
        # Keep the previously checked label-quotient results connected too.
        previous = member(member(owner, "metrics", JSON_FILES[5]), scheme, JSON_FILES[5])
        for key, expected in previous.items():
            exact(member(metrics, key, relative), expected, relative + ":metrics/" + scheme + "/" + key)
        exact(sums["collision_observations"], 8156, relative + ":collision sum")
        totals[scheme] = dict(sums)
    return totals


def _audit_checked(root: Path) -> dict[str, Any]:
    root = root.resolve()
    if not root.is_dir():
        raise AuditError(f"artifact directory missing: {root}")
    data = {name: read_json(root, name) for name in JSON_FILES}
    oracle = data[JSON_FILES[0]]
    campaign = data[JSON_FILES[1]]
    selection = data[JSON_FILES[2]]
    public = data[JSON_FILES[3]]
    scale = data[JSON_FILES[4]]
    owner = data[JSON_FILES[5]]
    details = read_csv(root, CSV_FILES[0], ("providers", "structures", "labelled_cases", "feasible_labelled_cases"))
    cases = read_csv(root, CSV_FILES[1], ("case", "group", "status", "rows", "incidences", "developer", "library", "ambiguous", "dependency_strictly_narrowed", "bytes_strictly_narrowed", "certificate_bytes"))
    providers = read_csv(root, CSV_FILES[2], ("archive", "owner", "package", "bytes"))
    pairs = read_csv(root, CSV_FILES[3], ("pair_id", "left", "right", "kind", "shared_nonmeta", "equal_nonmeta", "different_nonmeta"))
    builds = read_csv(root, CSV_FILES[4], ("build_id", "pair_id", "pair_kind", "first_archive", "second_archive", "entry_regions", "collision_regions", "local_ambiguous_regions", "certified_ambiguous_regions", "global_narrowings", "equal_regions_resolved_by_coupling", "ant_matches_first_winner", "archive_adapters_equal", "oracle_mismatches", "local_bytes_oracle_exact", "certified_oracle_exact"))

    # Current finite oracle: derive every count from its row-level census.
    exact(len(details), 69, CSV_FILES[0] + ":row count")
    exact({csv_integer(r, "providers", CSV_FILES[0]) for r in details}, {1, 2, 3}, CSV_FILES[0] + ":provider domain")
    for key, expected in (("structural_cases", 45291), ("labelled_cases", 90582), ("feasible_labelled_cases", 11398)):
        exact(csv_sum(details, "structures" if key == "structural_cases" else key, CSV_FILES[0]), expected, CSV_FILES[0] + ":" + key)
        field(oracle, key, expected, JSON_FILES[0])
    field(oracle, "region_classifications_checked", 21918, JSON_FILES[0])
    field(oracle, "mismatches", 0, JSON_FILES[0])
    exact(member(oracle, "provider_counts", JSON_FILES[0]), [1, 2, 3], JSON_FILES[0] + ":provider_counts")
    exact(member(oracle, "region_counts", JSON_FILES[0]), [0, 1, 2], JSON_FILES[0] + ":region_counts")
    owner_schemes = member(oracle, "owner_schemes", JSON_FILES[0])
    if not isinstance(owner_schemes, list) or len(owner_schemes) != 2 or any(type(s) is not str or not s for s in owner_schemes):
        raise AuditError("invalid oracle owner_schemes")

    # Current small scientific campaign: row sums and status census, not a flow table.
    exact(len(cases), 60, CSV_FILES[1] + ":row count")
    exact(len({r["case"] for r in cases}), 60, CSV_FILES[1] + ":unique cases")
    group_counts = Counter(r["group"] for r in cases)
    status_counts = Counter(r["status"] for r in cases)
    exact(dict(group_counts), {"generated": 40, "fixture": 20}, CSV_FILES[1] + ":groups")
    exact(dict(status_counts), {"classified": 43, "inconsistent": 15, "admission-rejected": 2}, CSV_FILES[1] + ":statuses")
    for key, expected in (("cases", 60), ("generated_cases", 40), ("boundary_fixtures", 20), ("public_builds", 0), ("classified_inputs", 43), ("inconsistent_inputs", 15), ("admission_rejected_inputs", 2), ("rows", 130), ("incidences", 505), ("developer", 22), ("library", 34), ("ambiguous", 24), ("dependency_strictly_narrowed", 54), ("bytes_strictly_narrowed", 18), ("certificate_bytes", 59646)):
        field(campaign, key, expected, JSON_FILES[1])
        if key in {"rows", "incidences", "developer", "library", "ambiguous", "dependency_strictly_narrowed", "bytes_strictly_narrowed", "certificate_bytes"}:
            exact(csv_sum(cases, key, CSV_FILES[1]), expected, CSV_FILES[1] + ":" + key)

    # Frozen public frame: two builders plus 43 study providers, 40 unique pairs.
    field(selection, "provider_count", 43, JSON_FILES[2])
    field(selection, "builder_count", 2, JSON_FILES[2])
    field(selection, "pair_count", 40, JSON_FILES[2])
    field(selection, "build_count", 80, JSON_FILES[2])
    builder_names = member(selection, "builder_archives", JSON_FILES[2])
    if not isinstance(builder_names, list) or len(builder_names) != 2 or len(set(builder_names)) != 2 or any(type(x) is not str for x in builder_names):
        raise AuditError("invalid builder_archives")
    archive_names = [r["archive"] for r in providers]
    exact(len(archive_names), 45, CSV_FILES[2] + ":row count")
    exact(len(set(archive_names)), 45, CSV_FILES[2] + ":unique archive count")
    exact(sum(name not in builder_names for name in archive_names), 43, CSV_FILES[2] + ":study provider count")
    if any(name not in archive_names for name in builder_names):
        raise AuditError("builder archive missing from provider census")
    for index, row in enumerate(providers, 2):
        csv_integer(row, "bytes", f"{CSV_FILES[2]}:row{index}")
        if not row["owner"] or not row["package"]:
            raise AuditError(f"missing owner/package in {CSV_FILES[2]}:row{index}")
    exact(len(pairs), 40, CSV_FILES[3] + ":row count")
    exact(len({r["pair_id"] for r in pairs}), 40, CSV_FILES[3] + ":unique IDs")
    selected = set(archive_names) - set(builder_names)
    pair_by_id = {}
    unordered = set()
    for index, row in enumerate(pairs, 2):
        if row["left"] not in selected or row["right"] not in selected or row["left"] == row["right"]:
            raise AuditError(f"invalid provider pair in {CSV_FILES[3]}:row{index}")
        pair = frozenset((row["left"], row["right"]))
        if pair in unordered:
            raise AuditError("duplicate unordered collision pair")
        unordered.add(pair)
        pair_by_id[row["pair_id"]] = row
        shared = csv_integer(row, "shared_nonmeta", CSV_FILES[3])
        equal = csv_integer(row, "equal_nonmeta", CSV_FILES[3])
        different = csv_integer(row, "different_nonmeta", CSV_FILES[3])
        exact(equal + different, shared, CSV_FILES[3] + ":collision partition")
        if shared == 0 or row["kind"] != ("mixed" if equal and different else "equal-only" if equal else "different-only"):
            raise AuditError("invalid collision pair category")
    categories = {"equal-only": 30, "different-only": 9, "mixed": 1}
    exact(dict(Counter(r["kind"] for r in pairs)), categories, CSV_FILES[3] + ":categories")
    exact(member(selection, "category_counts", JSON_FILES[2]), categories, JSON_FILES[2] + ":category_counts")

    # Current 80 concrete two-order builds and row-derived regional counts.
    exact(len(builds), 80, CSV_FILES[4] + ":row count")
    exact(len({r["build_id"] for r in builds}), 80, CSV_FILES[4] + ":unique build IDs")
    by_pair = defaultdict(list)
    for index, row in enumerate(builds, 2):
        pair_id = row["pair_id"]
        if pair_id not in pair_by_id:
            raise AuditError(f"unknown public build pair: {pair_id}")
        pair = pair_by_id[pair_id]
        if row["pair_kind"] != pair["kind"] or {row["first_archive"], row["second_archive"]} != {pair["left"], pair["right"]}:
            raise AuditError(f"public build/pair mismatch: {pair_id}")
        for key in ("ant_matches_first_winner", "archive_adapters_equal", "oracle_mismatches"):
            value = csv_integer(row, key, f"{CSV_FILES[4]}:row{index}")
            exact(value, 0 if key == "oracle_mismatches" else 1, f"{CSV_FILES[4]}:row{index}/{key}")
        for key in ("entry_regions", "collision_regions", "local_ambiguous_regions", "certified_ambiguous_regions", "global_narrowings", "equal_regions_resolved_by_coupling", "local_bytes_oracle_exact", "certified_oracle_exact"):
            csv_integer(row, key, f"{CSV_FILES[4]}:row{index}")
        by_pair[pair_id].append(row)
    exact(set(by_pair), set(pair_by_id), CSV_FILES[4] + ":pair coverage")
    for pair_id, rows in by_pair.items():
        if len(rows) != 2 or rows[0]["first_archive"] != rows[1]["second_archive"] or rows[0]["second_archive"] != rows[1]["first_archive"]:
            raise AuditError(f"missing two opposite orders: {pair_id}")
    for key, expected in (("public_provider_archives", 43), ("collision_pairs", 40), ("actual_ant_builds", 80), ("region_observations", 165630), ("collision_region_observations", 8156), ("local_byte_ambiguous_regions", 7042), ("certified_ambiguous_regions", 6942), ("global_narrowings_over_local_bytes", 100), ("equal_byte_regions_resolved_by_global_coupling", 100), ("indistinguishable_shared_regions_with_owner_flip", 3471), ("reversed_pairs_with_identical_output_maps", 30), ("ant_first_winner_mismatches", 0), ("independent_archive_adapter_mismatches", 0), ("certificate_vs_actual_two_order_oracle_mismatches", 0)):
        field(public, key, expected, JSON_FILES[3])
    exact(member(public, "pair_categories", JSON_FILES[3]), categories, JSON_FILES[3] + ":pair_categories")
    for summary_key, csv_key, expected in (("region_observations", "entry_regions", 165630), ("collision_region_observations", "collision_regions", 8156), ("local_byte_ambiguous_regions", "local_ambiguous_regions", 7042), ("certified_ambiguous_regions", "certified_ambiguous_regions", 6942), ("global_narrowings_over_local_bytes", "global_narrowings", 100), ("equal_byte_regions_resolved_by_global_coupling", "equal_regions_resolved_by_coupling", 100)):
        exact(csv_sum(builds, csv_key, CSV_FILES[4]), expected, CSV_FILES[4] + ":" + summary_key)
    baselines = member(public, "baseline_comparison_on_collision_regions", JSON_FILES[3])
    for name, column, expected in (("local_bytes", "local_bytes_oracle_exact", 8056), ("certified", "certified_oracle_exact", 8156)):
        baseline = member(baselines, name, JSON_FILES[3] + ":baselines")
        field(baseline, "oracle_exact_count", expected, JSON_FILES[3] + ":" + name)
        exact(csv_sum(builds, column, CSV_FILES[4]), expected, CSV_FILES[4] + ":" + column)

    # Owner labels: archive-level gain is real; package-level gain is zero.
    field(owner, "provider_archives", 43, JSON_FILES[5])
    field(owner, "pair_cases", 40, JSON_FILES[5])
    field(owner, "modeled_outputs_per_schema", 80, JSON_FILES[5])
    field(owner, "retained_case_count_checks", 80, JSON_FILES[5])
    field(owner, "archive_adapter_disagreements", 0, JSON_FILES[5])
    field(owner, "certificate_oracle_disagreements", 0, JSON_FILES[5])
    metrics = member(owner, "metrics", JSON_FILES[5])
    owner_pairs = member(owner, "pairs", JSON_FILES[5])
    if not isinstance(owner_pairs, list) or len(owner_pairs) != 80:
        raise AuditError("owner-granularity pair census must have 80 rows")
    for scheme, flips, narrowings in (("archive", 3471, 100), ("debian_package", 0, 0)):
        subset = [p for p in owner_pairs if member(p, "scheme", JSON_FILES[5] + ":pairs") == scheme]
        exact(len(subset), 40, JSON_FILES[5] + ":" + scheme + ":pair count")
        exact({p["pair_id"] for p in subset}, set(pair_by_id), JSON_FILES[5] + ":" + scheme + ":pair IDs")
        calculated_flips = sum(integer(member(p, "identical_output_pair_paths_with_owner_flip", JSON_FILES[5] + ":pairs"), "owner flip") for p in subset)
        calculated_narrow = sum(integer(member(p, "strict_narrowings", JSON_FILES[5] + ":pairs"), "strict narrowing") for p in subset)
        exact(calculated_flips, flips, JSON_FILES[5] + ":" + scheme + ":flip sum")
        exact(calculated_narrow, narrowings, JSON_FILES[5] + ":" + scheme + ":narrowing sum")
        metric = member(metrics, scheme, JSON_FILES[5] + ":metrics")
        field(metric, "identical_output_pair_paths_with_owner_flip", flips, JSON_FILES[5] + ":metrics/" + scheme)
        field(metric, "strict_narrowings", narrowings, JSON_FILES[5] + ":metrics/" + scheme)
        field(metric, "collision_observations", 8156, JSON_FILES[5] + ":metrics/" + scheme)
        field(metric, "entry_regions", 165630, JSON_FILES[5] + ":metrics/" + scheme)
        field(metric, "certified_exact_count", 8156, JSON_FILES[5] + ":metrics/" + scheme)
    archive_pairs = [p for p in owner_pairs if p["scheme"] == "archive"]
    exact(sum(p["identical_content_maps"] is True for p in archive_pairs), 30, JSON_FILES[5] + ":equal-map pair count")
    exact({p["pair_id"] for p in archive_pairs if p["strict_narrowings"] > 0}, set(member(owner, "narrowing_pairs", JSON_FILES[5])), JSON_FILES[5] + ":narrowing pair IDs")
    field(member(metrics, "debian_package", JSON_FILES[5] + ":metrics"), "removed_owner_associations", 0, JSON_FILES[5] + ":debian_package")

    diagnostic = audit_diagnostic(root, data, builds, providers, owner)

    if not isinstance(scale, list) or len(scale) != 3:
        raise AuditError("scale source must contain the three retained probes")
    forced = [row for row in scale if member(row, "case", JSON_FILES[4]) == "forced-repeated-collision"]
    exact(len(forced), 1, JSON_FILES[4] + ":forced probe count")
    for key, expected in (("providers", 300), ("regions", 20000), ("certificate_bytes", 8602784)):
        field(forced[0], key, expected, JSON_FILES[4] + ":forced-repeated-collision")
    exact(max(integer(member(row, "certificate_bytes", JSON_FILES[4]), "scale certificate_bytes") for row in scale), 8602784, JSON_FILES[4] + ":largest certificate")

    return {
        "schema_version": 2,
        "status": "PASS",
        "errors": [],
        "scope": "Named current scientific JSON/CSV bindings only; no campaign execution or full scientific acceptance",
        "scientific_sources": list(dict.fromkeys(JSON_FILES + CSV_FILES + DIAGNOSTIC_BINDINGS)),
        "claims": {
            "finite_labelled_models": 90582,
            "finite_mismatches": 0,
            "current_campaign_cases": 60,
            "public_provider_archives": 43,
            "public_collision_pairs": 40,
            "actual_two_order_builds": 80,
            "region_observations": 165630,
            "collision_region_observations": 8156,
            "identical_output_pair_paths_with_owner_flip": 3471,
            "archive_label_strict_narrowings": 100,
            "debian_package_additional_owner_resolutions": 0,
            "retained_same_information_diagnostic": diagnostic,
            "largest_retained_scale_probe": {"providers": 300, "regions": 20000, "certificate_bytes": 8602784},
        },
    }


def audit(root: Path) -> dict[str, Any]:
    """Importable, never-writing API for final_release_gate.

    Expected input-contract failures return FAIL, rather than escaping to the gate.
    A PASS covers only the named local scientific sources and their field relations.
    """
    try:
        return _audit_checked(root)
    except (AuditError, TypeError, KeyError, ValueError, OSError) as exc:
        return {
            "schema_version": 2,
            "status": "FAIL",
            "claims": {},
            "errors": [str(exc)],
            "scope": "named local scientific source contract",
        }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact", type=Path, required=True)
    parser.add_argument("--output-json", type=Path, help="existing-parent path outside artifact; otherwise stdout")
    args = parser.parse_args(argv)
    root = args.artifact.resolve()
    output = args.output_json.resolve() if args.output_json else None
    if output is not None and output.is_relative_to(root):
        parser.error("--output-json must be outside the artifact")
    result = audit(root)
    rendered = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if output is None:
        sys.stdout.write(rendered)
    else:
        if not output.parent.is_dir():
            parser.error("--output-json parent directory must already exist")
        output.write_text(rendered, encoding="utf-8")
    return 0 if result["status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
