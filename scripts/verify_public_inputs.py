#!/usr/bin/env python3
"""Verify the frozen public JAR corpus and its collision-pair census.

The verifier uses only bundled files.  It checks provider metadata, licensing
records, archive safety through the producer-side parser, and independently
recomputes every unordered non-META-INF collision pair among the 43 study
providers.  It emits no checksum/version manifest.
"""
from __future__ import annotations
import csv
import json
import sys
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from archive_producer import read_archive

PUBLIC = ROOT / "inputs" / "public"
BUILDERS = {"ant-1.10.15.jar", "ant-launcher-1.10.15.jar"}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def nonmeta(table: dict[str, bytes]) -> dict[str, bytes]:
    return {name: payload for name, payload in table.items()
            if not name.upper().startswith("META-INF/")}


def run() -> dict[str, object]:
    providers = read_csv(PUBLIC / "providers.csv")
    listed = {row["archive"]: row for row in providers}
    jar_files = {path.name for path in (PUBLIC / "jars").glob("*.jar")}
    if set(listed) != jar_files:
        raise RuntimeError("providers.csv and bundled JAR names differ")
    for name, row in listed.items():
        path = PUBLIC / "jars" / name
        if path.is_symlink() or not path.is_file():
            raise RuntimeError(f"provider is not a regular bundled file: {name}")
        if path.stat().st_size != int(row["bytes"]):
            raise RuntimeError(f"provider size metadata differs: {name}")
        package = row["package"]
        license_path = PUBLIC / "licenses" / f"{package}.copyright"
        if not license_path.is_file() or not license_path.read_text(errors="replace").strip():
            raise RuntimeError(f"missing Debian copyright record: {package}")

    experiment = sorted(name for name in listed if name not in BUILDERS)
    if len(experiment) != 43:
        raise RuntimeError(f"expected 43 experiment providers, found {len(experiment)}")
    stores = {name: nonmeta(read_archive(PUBLIC / "jars" / name)) for name in experiment}
    recomputed: list[dict[str, object]] = []
    for left, right in combinations(experiment, 2):
        shared = sorted(set(stores[left]) & set(stores[right]))
        if not shared:
            continue
        equal = sum(stores[left][key] == stores[right][key] for key in shared)
        different = len(shared) - equal
        kind = "mixed" if equal and different else ("equal-only" if equal else "different-only")
        recomputed.append({"left": left, "right": right, "kind": kind,
                           "shared_nonmeta": len(shared), "equal_nonmeta": equal,
                           "different_nonmeta": different})

    declared = read_csv(PUBLIC / "collision_pairs.csv")
    declared_core = [{key: (int(row[key]) if key.endswith("_nonmeta") else row[key])
                      for key in ("left", "right", "kind", "shared_nonmeta",
                                  "equal_nonmeta", "different_nonmeta")}
                     for row in declared]
    if recomputed != declared_core:
        raise RuntimeError("collision-pair census differs from bundled declaration")
    categories: dict[str, int] = {}
    for row in recomputed:
        categories[row["kind"]] = categories.get(row["kind"], 0) + 1
    summary = {
        "bundled_jars": len(jar_files),
        "experiment_provider_archives": len(experiment),
        "builder_archives": len(BUILDERS),
        "recomputed_collision_pairs": len(recomputed),
        "pair_categories": dict(sorted(categories.items())),
        "selection_scope": "all unordered pairs among the 43 bundled study providers; META-INF entries excluded",
        "licensing_records_checked": len({row["package"] for row in providers}),
    }
    if summary["recomputed_collision_pairs"] != 40:
        raise RuntimeError("frozen corpus no longer contains exactly 40 collision pairs")
    return summary


def main() -> None:
    try:
        print(json.dumps(run(), indent=2))
    except (OSError, ValueError, RuntimeError) as exc:
        raise SystemExit(f"public input verification failed: {exc}") from exc


if __name__ == "__main__":
    main()
