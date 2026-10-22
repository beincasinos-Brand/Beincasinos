#!/usr/bin/env python3
"""Validate the internal paid-listing pipeline without treating prospects as approved."""
import csv
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
TRACKER = ROOT / "docs" / "paid-listing-sales-pipeline.csv"
STAGES = {
    "not_contacted", "qualified", "draft_ready", "contacted", "follow_up_due",
    "replied_interested", "qualified_buyer", "in_discussion", "proposal_sent",
    "won", "lost", "do_not_contact",
}
QUALIFICATION = {"not reviewed", "hold", "pass", "reject"}
YES_NO = {"yes", "no", "not reviewed", "not applicable"}
REQUIRED = {
    "brand_name", "legal_entity", "target_market", "official_contact_source",
    "contact_email_or_form", "qualification_status", "pipeline_stage",
    "first_contact_date_utc", "last_contact_date_utc", "next_action_date_utc",
    "agreement_status", "invoice_status", "paid_label_confirmed",
    "market_review_confirmed", "privacy_tracking_review", "source_evidence_url",
    "do_not_contact_reason",
}
errors = []
if not TRACKER.is_file():
    raise SystemExit(f"FAIL: missing tracker: {TRACKER.relative_to(ROOT)}")
with TRACKER.open(encoding="utf-8-sig", newline="") as handle:
    reader = csv.DictReader(handle)
    headers = set(reader.fieldnames or [])
    missing = REQUIRED - headers
    if missing:
        errors.append("missing required columns: " + ", ".join(sorted(missing)))
    rows = list(reader)

seen = set()
for line, row in enumerate(rows, start=2):
    label = f"row {line}"
    brand = (row.get("brand_name") or "").strip()
    if not brand:
        if any((v or "").strip() for v in row.values()):
            errors.append(f"{label}: data exists but brand_name is blank")
        continue
    key = brand.casefold()
    if key in seen:
        errors.append(f"{label}: duplicate brand_name {brand!r}")
    seen.add(key)

    # Every prospect row must have a minimally identifiable entity, market and
    # traceable source even while it remains in the untouched research queue.
    for field in ("legal_entity", "target_market", "source_evidence_url"):
        if not (row.get(field) or "").strip():
            errors.append(f"{label} {brand}: populated prospect requires {field}")
    source_url = (row.get("source_evidence_url") or "").strip()
    if source_url:
        parsed_source = urlparse(source_url)
        if parsed_source.scheme != "https" or not parsed_source.netloc:
            errors.append(f"{label} {brand}: source_evidence_url must be a valid HTTPS URL")

    stage = (row.get("pipeline_stage") or "").strip()
    qual = (row.get("qualification_status") or "").strip().casefold()
    if stage not in STAGES:
        errors.append(f"{label} {brand}: unknown pipeline_stage {stage!r}")
    if qual not in QUALIFICATION:
        errors.append(f"{label} {brand}: qualification_status must be one of {sorted(QUALIFICATION)}")
    for field in ("paid_label_confirmed", "market_review_confirmed", "privacy_tracking_review"):
        value = (row.get(field) or "").strip().casefold()
        if value not in YES_NO:
            errors.append(f"{label} {brand}: invalid {field} value {value!r}")
    if stage in {"contacted", "follow_up_due", "replied_interested", "qualified_buyer", "in_discussion", "proposal_sent", "won"}:
        if not (row.get("first_contact_date_utc") or "").strip():
            errors.append(f"{label} {brand}: stage {stage} requires first_contact_date_utc")
    if stage == "do_not_contact" and not (row.get("do_not_contact_reason") or "").strip():
        errors.append(f"{label} {brand}: do_not_contact requires a reason")
    if stage == "won":
        for field in ("legal_entity", "target_market", "source_evidence_url", "agreement_status", "invoice_status", "placement_type", "currency", "term_start", "term_end"):
            if not (row.get(field) or "").strip():
                errors.append(f"{label} {brand}: won requires {field}")
        if (row.get("agreement_status") or "").strip().casefold() not in {"signed", "executed"}:
            errors.append(f"{label} {brand}: won requires signed/executed agreement_status")
        if (row.get("invoice_status") or "").strip().casefold() not in {"paid", "complete"}:
            errors.append(f"{label} {brand}: won requires paid/complete invoice_status (not applicable is not accepted for a paid listing)")
        for field in ("paid_label_confirmed", "market_review_confirmed", "privacy_tracking_review"):
            if (row.get(field) or "").strip().casefold() != "yes":
                errors.append(f"{label} {brand}: won requires {field}=yes")
    if stage in {"qualified", "draft_ready", "proposal_sent", "won"} and qual != "pass":
        errors.append(f"{label} {brand}: stage {stage} requires qualification_status=pass")

    # Once research or outreach begins, require traceable primary-source URLs.
    if stage not in {"not_contacted", "do_not_contact"}:
        for field in ("official_contact_source", "source_evidence_url"):
            value = (row.get(field) or "").strip()
            parsed = urlparse(value)
            if not value or parsed.scheme != "https" or not parsed.netloc:
                errors.append(f"{label} {brand}: {stage} requires a valid HTTPS {field}")

    # Dates are recorded as ISO calendar dates in UTC (YYYY-MM-DD).
    for field in ("first_contact_date_utc", "last_contact_date_utc", "next_action_date_utc", "term_start", "term_end"):
        value = (row.get(field) or "").strip()
        if value:
            try:
                parsed_date = date.fromisoformat(value)
                if parsed_date.isoformat() != value:
                    raise ValueError("not canonical ISO format")
            except ValueError:
                errors.append(f"{label} {brand}: {field} must use YYYY-MM-DD format")
    first = (row.get("first_contact_date_utc") or "").strip()
    last = (row.get("last_contact_date_utc") or "").strip()
    if first and last:
        try:
            if date.fromisoformat(last) < date.fromisoformat(first):
                errors.append(f"{label} {brand}: last_contact_date_utc cannot precede first contact")
        except ValueError:
            pass
    start = (row.get("term_start") or "").strip()
    end = (row.get("term_end") or "").strip()
    if start and end:
        try:
            if date.fromisoformat(end) < date.fromisoformat(start):
                errors.append(f"{label} {brand}: term_end cannot precede term_start")
        except ValueError:
            pass

if errors:
    print(f"FAIL: {len(errors)} paid-listing pipeline issue(s)")
    for error in errors:
        print(f"  ERROR: {error}")
    sys.exit(1)
print(f"PASS: paid-listing pipeline schema and hard gates validated ({len(seen)} populated prospect row(s)).")
print("Reminder: this validates tracker consistency, not licensing, legal compliance, owner approval, or commercial truth.")
