#!/usr/bin/env python3
"""Validate the internal Tier-1 prospect tracker without treating leads as approved reviews."""
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TRACKER = ROOT / "docs" / "tier-1-master-prospect-tracker.csv"
ROADMAP_MARKETS = {"GB", "BE", "SE", "DK", "ES", "IT", "NL", "DE", "CH", "CA-ON"}
REQUIRED = {
    "brand_name", "market", "product_scope", "official_domain", "legal_operator",
    "regulator_or_authority", "publication_status", "next_action", "last_checked_utc",
    "notes", "global_brand_id",
}


def main():
    errors = []
    try:
        with TRACKER.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            headers = reader.fieldnames or []
            missing = sorted(REQUIRED - set(headers))
            if missing:
                errors.append("missing required columns: " + ", ".join(missing))
            rows = list(reader)
    except (OSError, UnicodeError, csv.Error) as exc:
        print(f"ERROR: cannot read prospect tracker: {exc}", file=sys.stderr)
        return 1

    if len(headers) != len(set(headers)):
        errors.append("duplicate column names found")

    represented_markets = {
        (row.get("market") or "").strip().upper()
        for row in rows
        if (row.get("market") or "").strip()
    }
    missing_markets = sorted(ROADMAP_MARKETS - represented_markets)
    if missing_markets:
        errors.append("roadmap markets missing from tracker: " + ", ".join(missing_markets))

    seen = {}
    for line, row in enumerate(rows, start=2):
        if None in row:
            errors.append(f"row {line}: more values than header columns")
            continue
        if any(value is None for value in row.values()):
            errors.append(f"row {line}: fewer values than header columns")
            continue
        brand = (row.get("brand_name") or "").strip()
        market = (row.get("market") or "").strip().upper()
        if not brand:
            errors.append(f"row {line}: brand_name is blank")
        if not market:
            errors.append(f"row {line}: market is blank")
        if not (row.get("publication_status") or "").strip():
            errors.append(f"row {line}: publication_status is blank")
        key = (brand.casefold(), market)
        if brand and market and key in seen:
            errors.append(f"row {line}: duplicate brand/market key; first seen on row {seen[key]}")
        elif brand and market:
            seen[key] = line

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    blank_ids = sum(not (row.get("global_brand_id") or "").strip() for row in rows)
    placeholders = sum((row.get("official_domain") or "").strip().upper() in {"", "VERIFY"} for row in rows)
    print(f"OK: {len(rows)} prospect rows; schema, brand/market uniqueness, and all {len(ROADMAP_MARKETS)} roadmap markets checked.")
    if blank_ids:
        print(f"WARNING: {blank_ids} rows lack global_brand_id; cross-market deduplication is incomplete.")
    if placeholders:
        print(f"WARNING: {placeholders} rows have blank/VERIFY official domains; these remain unqualified research leads.")
    print("This check validates tracker structure only; it does not approve brands or reviews.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
