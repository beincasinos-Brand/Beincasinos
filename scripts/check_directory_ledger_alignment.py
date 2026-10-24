#!/usr/bin/env python3
"""Fail CI if the canonical 100-brand ledger drifts from the public directory."""
from __future__ import annotations

import csv
import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIRECTORY = ROOT / "brand-directory" / "index.html"
LEDGER = ROOT / "docs" / "targets" / "100-brand-review-production-ledger-2026-10-24.csv"


def parse_directory_identities(source: str) -> set[tuple[str, str]]:
    identities: set[tuple[str, str]] = set()
    pattern = re.compile(
        r'<article class="brand-card"(?P<attrs>[^>]*)>(?P<body>.*?)</article>',
        re.IGNORECASE | re.DOTALL,
    )
    for match in pattern.finditer(source):
        attrs, body = match.group("attrs"), match.group("body")
        market_match = re.search(r'data-market="([^"]+)"', attrs, re.IGNORECASE)
        name_match = re.search(r"<h2>(.*?)</h2>", body, re.IGNORECASE | re.DOTALL)
        if not market_match or not name_match:
            continue
        name = html.unescape(re.sub(r"<[^>]+>", "", name_match.group(1))).strip()
        market = html.unescape(market_match.group(1)).strip().upper()
        if name and market:
            identities.add((name, market))
    return identities


def parse_ledger_identities(path: Path) -> set[tuple[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as handle:
        rows = csv.DictReader(handle)
        if not rows.fieldnames or not {"brand_name", "market_code"}.issubset(rows.fieldnames):
            raise ValueError("canonical ledger must contain brand_name and market_code columns")
        identities = set()
        for row in rows:
            name = html.unescape((row.get("brand_name") or "").strip())
            market = (row.get("market_code") or "").strip().upper()
            if name and market:
                identities.add((name, market))
        return identities


def compare_identities(
    directory_ids: set[tuple[str, str]],
    ledger_ids: set[tuple[str, str]],
    *,
    require_100: bool = False,
) -> list[str]:
    errors: list[str] = []
    if require_100 and len(directory_ids) != 100:
        errors.append(f"public directory must contain 100 unique brand/market identities; found {len(directory_ids)}")
    if require_100 and len(ledger_ids) != 100:
        errors.append(f"canonical ledger must contain 100 unique brand/market identities; found {len(ledger_ids)}")
    missing = sorted(directory_ids - ledger_ids)
    extra = sorted(ledger_ids - directory_ids)
    if missing:
        errors.append("public directory identities missing from canonical ledger: " + "; ".join(f"{n} [{m}]" for n, m in missing[:20]))
    if extra:
        errors.append("canonical ledger identities absent from public directory: " + "; ".join(f"{n} [{m}]" for n, m in extra[:20]))
    return errors


def main() -> int:
    try:
        directory_ids = parse_directory_identities(DIRECTORY.read_text(encoding="utf-8"))
        ledger_ids = parse_ledger_identities(LEDGER)
    except (OSError, UnicodeError, ValueError, csv.Error) as exc:
        print(f"ERROR: could not parse directory/ledger: {exc}", file=sys.stderr)
        return 1
    errors = compare_identities(directory_ids, ledger_ids, require_100=True)
    if errors:
        for error in errors:
            print("ERROR: " + error, file=sys.stderr)
        return 1
    print(f"PASS: canonical ledger matches all {len(directory_ids)} public brand/market identities.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
