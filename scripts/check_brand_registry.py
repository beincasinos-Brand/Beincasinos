#!/usr/bin/env python3
"""Validate the 100-brand research registry without approving reviews for publication.

Run from any directory:
    python3 scripts/check_brand_registry.py
"""
from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs" / "brand-research-template.csv"
EXPECTED_BRANDS = 100
REQUIRED_COLUMNS = {
    "brand_name",
    "official_url",
    "legal_entity",
    "regulator",
    "official_register_url",
    "license_scope",
    "markets_allowed",
    "source_notes",
    "last_checked_utc",
    "status",
    "publication_decision",
    "unresolved_issues",
}
VALID_STATUSES = {"prospect", "evidence captured", "draft", "reviewed"}
VALID_DECISIONS = {"not reviewed", "HOLD", "approved", "rejected"}
errors: list[str] = []
warnings: list[str] = []

if not REGISTRY.is_file():
    print(f"ERROR: registry file missing: {REGISTRY}", file=sys.stderr)
    sys.exit(1)

with REGISTRY.open("r", encoding="utf-8-sig", newline="") as handle:
    reader = csv.DictReader(handle)
    columns = set(reader.fieldnames or [])
    missing = sorted(REQUIRED_COLUMNS - columns)
    if missing:
        errors.append("Missing required columns: " + ", ".join(missing))
    rows = list(reader)

if len(rows) != EXPECTED_BRANDS:
    errors.append(f"Expected {EXPECTED_BRANDS} brand rows, found {len(rows)}")

names = [((row.get("brand_name") or "").strip().casefold()) for row in rows]
for name, count in Counter(names).items():
    if not name:
        errors.append("Blank brand_name found")
    elif count > 1:
        errors.append(f"Duplicate brand_name ({count} rows): {name}")

for line, row in enumerate(rows, start=2):
    brand = (row.get("brand_name") or "").strip() or f"line {line}"
    status = (row.get("status") or "").strip()
    decision = (row.get("publication_decision") or "").strip()
    issues = (row.get("unresolved_issues") or "").strip()
    register_url = (row.get("official_register_url") or "").strip()
    source_notes = (row.get("source_notes") or "").strip()

    if status not in VALID_STATUSES:
        errors.append(f"{brand}: invalid status {status!r}")
    if decision not in VALID_DECISIONS:
        errors.append(f"{brand}: invalid publication_decision {decision!r}")
    if decision == "approved":
        if status != "reviewed":
            errors.append(f"{brand}: approved decision requires status=reviewed")
        if issues:
            errors.append(f"{brand}: approved decision still has unresolved_issues")
        if not register_url or not source_notes:
            errors.append(f"{brand}: approved decision requires regulator source and source notes")
    if status == "evidence captured" and decision != "HOLD":
        warnings.append(f"{brand}: evidence captured should normally remain HOLD until review is complete")
    if status == "prospect" and decision == "approved":
        errors.append(f"{brand}: prospect cannot be approved")
    if status == "evidence captured" and (not register_url or not source_notes):
        warnings.append(f"{brand}: evidence-captured row is missing a register URL or source notes")

print(f"Registry: {REGISTRY.relative_to(ROOT)}")
print(f"Rows: {len(rows)} / {EXPECTED_BRANDS}")
print(f"Columns: {len(columns)}")
print(f"Unique non-empty brand names: {len({n for n in names if n})}")
print(f"Errors: {len(errors)}")
print(f"Warnings: {len(warnings)}")
for message in errors:
    print("ERROR:", message)
for message in warnings:
    print("WARNING:", message)
sys.exit(1 if errors else 0)
