#!/usr/bin/env python3
"""Cross-check exact-name Tier-1 prospects against the canonical research registry.

Only enforce mappings when an exact case-insensitive display-name match in the
registry resolves to one non-empty global_brand_id. Alias/white-label matching
is deliberately not inferred here and remains a human-review task.
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACKER = ROOT / "docs" / "tier-1-master-prospect-tracker.csv"
REGISTRY = ROOT / "docs" / "brand-research-template.csv"


def canonical_name(value):
    return (value or "").strip().casefold()


def build_registry_ids(rows):
    ids_by_name = defaultdict(set)
    for row in rows:
        name = canonical_name(row.get("brand_name"))
        brand_id = (row.get("global_brand_id") or "").strip()
        if name and brand_id:
            ids_by_name[name].add(brand_id)
    return ids_by_name


def validate_exact_name_mappings(tracker_rows, registry_ids_by_name):
    errors = []
    warnings = []
    checked = 0
    known_ids = set().union(*registry_ids_by_name.values()) if registry_ids_by_name else set()
    for line, row in enumerate(tracker_rows, start=2):
        name = canonical_name(row.get("brand_name"))
        actual_id = (row.get("global_brand_id") or "").strip()
        if actual_id and actual_id not in known_ids:
            errors.append(
                f"row {line} ({row.get('brand_name', '').strip()}): tracker ID "
                f"{actual_id!r} does not exist in the canonical registry"
            )
        if not name or name not in registry_ids_by_name:
            continue
        registry_ids = registry_ids_by_name[name]
        # Conflicting source IDs must be resolved in the registry itself;
        # do not pick one arbitrarily or infer an alias.
        if len(registry_ids) != 1:
            warnings.append(
                f"row {line} ({row.get('brand_name', '').strip()}): exact-name "
                f"registry match has {len(registry_ids)} global IDs; manual reconciliation required"
            )
            continue
        expected_id = next(iter(registry_ids))
        checked += 1
        if not actual_id:
            errors.append(
                f"row {line} ({row.get('brand_name', '').strip()}): exact-name "
                f"registry match requires global_brand_id={expected_id}"
            )
        elif actual_id != expected_id:
            errors.append(
                f"row {line} ({row.get('brand_name', '').strip()}): tracker ID "
                f"{actual_id!r} conflicts with exact-name registry ID {expected_id!r}"
            )
    return errors, warnings, checked


def read_csv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames or "brand_name" not in reader.fieldnames:
            raise ValueError(f"{path.relative_to(ROOT)}: missing brand_name header")
        if "global_brand_id" not in reader.fieldnames:
            raise ValueError(f"{path.relative_to(ROOT)}: missing global_brand_id header")
        return list(reader)


def main():
    try:
        tracker_rows = read_csv(TRACKER)
        registry_rows = read_csv(REGISTRY)
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        print(f"ERROR: cannot read reconciliation inputs: {exc}", file=sys.stderr)
        return 1

    errors, warnings, checked = validate_exact_name_mappings(
        tracker_rows, build_registry_ids(registry_rows)
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        return 1

    print(
        f"OK: {checked} exact-name prospect/registry mappings checked; "
        f"{len(warnings)} ambiguous exact-name matches left for manual reconciliation."
    )
    print(
        "This is a conservative exact-name guardrail only; it does not infer aliases, "
        "prove operator eligibility, or approve reviews."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
