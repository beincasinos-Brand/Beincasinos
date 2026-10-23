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
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "docs" / "brand-research-template.csv"
TARGET_REVIEWS = 100
REQUIRED_COLUMNS = {
    "brand_name",
    "official_url",
    "markets_allowed",
    "legal_entity",
    "regulator",
    "official_register_url",
    "license_scope",
    "source_notes",
    "last_checked_utc",
    "status",
    "publication_decision",
    "unresolved_issues",
}
VALID_STATUSES = {"prospect", "research", "scope triage", "legal hold", "legal scope hold", "evidence captured", "draft", "reviewed", "research lead — unverified", "excluded - current permission/domain not active"}
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

for line, row in enumerate(rows, start=2):
    if None in row:
        errors.append(f"Line {line}: extra CSV fields beyond the header")
    missing_values = [key for key, value in row.items() if key is not None and value is None]
    if missing_values:
        errors.append(f"Line {line}: missing CSV values for: " + ", ".join(missing_values))

if len(rows) < TARGET_REVIEWS:
    errors.append(f"Need at least {TARGET_REVIEWS} candidate rows to support the review target, found {len(rows)}")
elif len(rows) > TARGET_REVIEWS:
    warnings.append(f"Registry has {len(rows)} candidate rows for a target of {TARGET_REVIEWS} approved reviews; surplus leads are allowed and must not be counted as completed reviews")

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

    official_url = (row.get("official_url") or "").strip()
    market_scope = (row.get("markets_allowed") or "").strip()
    if not market_scope:
        errors.append(f"{brand}: markets_allowed must state a specific jurisdiction or explicitly say none confirmed")
    if not official_url:
        errors.append(f"{brand}: official_url is required for a candidate record")
    else:
        parsed = urlparse(official_url)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            errors.append(f"{brand}: official_url must be an absolute HTTP(S) URL")

    if decision == "HOLD" and not issues:
        errors.append(f"{brand}: HOLD decision must explain unresolved issues")
    for field in ("official_register_url", "terms_url", "withdrawals_url", "complaints_url", "responsible_gambling_url", "partnership_contact_url", "launch_year_source_url", "partnership_evidence_url"):
        value = (row.get(field) or "").strip()
        if value:
            parsed = urlparse(value)
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                errors.append(f"{brand}: {field} must be an absolute HTTP(S) URL when populated")
    # Enforce confirmed target scope and jurisdiction-specific legal gates.
    scope_text = market_scope.casefold()
    forbidden_markets = ("ghana", "colombia", "brazil", "argentina", "mexico", "south africa", "nigeria", "denmark")
    for forbidden in forbidden_markets:
        if forbidden in scope_text and decision != "rejected":
            errors.append(f"{brand}: out-of-scope geography {forbidden!r} cannot remain an active target candidate")
    if decision == "approved":
        if "australia" in scope_text or ("france" in scope_text and "no online casino authorisation" in scope_text):
            errors.append(f"{brand}: cannot approve an online-casino review for a market where this record explicitly notes no general online-casino authorisation")
        if "canada" in scope_text and not any(province in scope_text for province in ("ontario", "quebec", "québec", "british columbia", "alberta", "manitoba", "saskatchewan", "nova scotia", "new brunswick", "newfoundland", "prince edward island", "yukon", "northwest territories", "nunavut")):
            errors.append(f"{brand}: Canadian approval requires a named province/territory")
        if ("united states" in scope_text or "usa" in scope_text or "u.s." in scope_text) and not any(state in scope_text for state in ("michigan", "new jersey", "pennsylvania", "west virginia", "delaware", "connecticut", "rhode island", "nevada", "massachusetts", "illinois", "tribal")):
            errors.append(f"{brand}: US approval requires an explicit state/tribal jurisdiction")
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
print(f"Candidate rows: {len(rows)} (target: {TARGET_REVIEWS} approved reviews)")
print(f"Columns: {len(columns)}")
print(f"Unique non-empty brand names: {len({n for n in names if n})}")
approved_count = sum(1 for row in rows if (row.get("publication_decision") or "").strip() == "approved")
print(f"Publication-approved rows: {approved_count} / {TARGET_REVIEWS}")
print(f"Errors: {len(errors)}")
print(f"Warnings: {len(warnings)}")
for message in errors:
    print("ERROR:", message)
for message in warnings:
    print("WARNING:", message)
sys.exit(1 if errors else 0)
