#!/usr/bin/env python3
"""Evidence and publication gate for the 100-brand editorial ledger.

This is a conservative structural gate, not a regulator lookup or a review.
Run from the repository root: python3 scripts/check_review_ledger.py
"""
import csv
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LEDGER = ROOT / "docs/targets/100-brand-review-production-ledger-2026-10-24.csv"
SCORE_LIMITS = {
    "score_licence_20": 20,
    "score_payments_18": 18,
    "score_safety_15": 15,
    "score_product_12": 12,
    "score_bonus_10": 10,
    "score_complaints_10": 10,
    "score_ux_8": 8,
    "score_privacy_4": 4,
    "score_evidence_3": 3,
}
REQUIRED_COLUMNS = {
    "slot", "brand_name", "global_brand_id", "market_code", "official_url",
    "legal_entity", "regulator", "official_register_url", "terms_url",
    "withdrawals_url", "complaints_url", "responsible_gambling_url",
    "bonus_offer_url", "bonus_checked_utc", "bonus_status",
    "image_source_url", "image_rights_status", *SCORE_LIMITS,
    "overall_score_100", "review_status", "publication_status", "blockers",
    "deposit_methods_url", "fees_limits_url", "privacy_cookies_url",
    "accessibility_evidence_url", "regulatory_actions_url", "adr_url",
    "reviewer_primary", "reviewer_secondary", "independent_review_date",
    "editorial_approval_date", "consumer_test_status", "affiliate_disclosure_status",
    "evidence_bundle_path", "domain_verification_status", "domain_verified_utc", "domain_evidence_url",
}
PUBLISHABLE_STATES = {"APPROVED", "APPROVED_TO_PUBLISH", "PUBLISHED", "LIVE"}
TARGET_MARKETS = {"AU", "CA", "GB", "US", "CH", "DE", "NL", "SE", "ES", "IT", "FR", "BE"}
errors = []
warnings = []


def has_https_url(value):
    try:
        parsed = urlparse((value or "").strip())
        return parsed.scheme == "https" and bool(parsed.netloc)
    except ValueError:
        return False


def check(ledger_path):
    with ledger_path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        columns = reader.fieldnames or []
    missing = sorted(REQUIRED_COLUMNS - set(columns))
    if missing:
        errors.append(f"{ledger_path}: missing required columns: {', '.join(missing)}")
    if len(columns) != len(set(columns)):
        errors.append(f"{ledger_path}: duplicate column names")
    if len(rows) != 100:
        errors.append(f"{ledger_path}: expected 100 candidate rows, found {len(rows)}")

    seen_slots, seen_keys = set(), set()
    for line, row in enumerate(rows, start=2):
        label = f"{ledger_path}:{line}"
        brand = row.get("brand_name", "").strip()
        market = row.get("market_code", "").strip().upper()
        if market and market not in TARGET_MARKETS and not re.fullmatch(r"(?:US|CA)-[A-Z]{2}", market):
            errors.append(f"{label}: market_code {market!r} is outside the approved target-market code format")
        slot = row.get("slot", "").strip()
        key = (brand.casefold(), market)
        if not brand:
            errors.append(f"{label}: missing brand_name")
        if not market:
            errors.append(f"{label}: missing market_code")
        if slot in seen_slots:
            errors.append(f"{label}: duplicate slot {slot!r}")
        seen_slots.add(slot)
        if key in seen_keys:
            errors.append(f"{label}: duplicate brand/market identity {brand!r}/{market}")
        seen_keys.add(key)

        for field in ("official_url", "official_register_url", "domain_evidence_url"):
            value = row.get(field, "").strip()
            if value and not has_https_url(value):
                errors.append(f"{label}: {field} must be an HTTPS URL when populated")
        for field in ("terms_url", "withdrawals_url", "complaints_url",
                      "responsible_gambling_url", "bonus_offer_url", "image_source_url",
                      "deposit_methods_url", "fees_limits_url", "privacy_cookies_url",
                      "accessibility_evidence_url", "regulatory_actions_url", "adr_url"):
            value = row.get(field, "").strip()
            if value and not has_https_url(value):
                errors.append(f"{label}: {field} must be an HTTPS URL when populated")

        # Score is all-or-nothing: no partial numeric score can masquerade as a final rating.
        numeric_scores = {}
        for field, maximum in SCORE_LIMITS.items():
            raw = row.get(field, "").strip()
            if not raw:
                continue
            try:
                score = float(raw)
            except ValueError:
                errors.append(f"{label}: {field} must be blank or numeric, got {raw!r}")
                continue
            if not 0 <= score <= maximum:
                errors.append(f"{label}: {field}={score:g} is outside 0–{maximum}")
            numeric_scores[field] = score
        overall_raw = row.get("overall_score_100", "").strip()
        if numeric_scores and len(numeric_scores) != len(SCORE_LIMITS):
            errors.append(f"{label}: partial rubric score; either score all 9 components or leave all blank")
        if overall_raw and overall_raw.casefold() not in {"not scored", "not assigned", "pending", "n/a"} and len(numeric_scores) != len(SCORE_LIMITS):
            errors.append(f"{label}: overall_score_100 requires all 9 rubric components")
        if len(numeric_scores) == len(SCORE_LIMITS):
            expected = sum(numeric_scores.values())
            if not overall_raw:
                errors.append(f"{label}: complete rubric needs overall_score_100")
            else:
                try:
                    overall = float(overall_raw)
                    if not 0 <= overall <= 100 or abs(overall - expected) > 0.001:
                        errors.append(f"{label}: overall score must equal component sum {expected:g}, got {overall:g}")
                except ValueError:
                    errors.append(f"{label}: overall_score_100 must be numeric when populated")

        rights = row.get("image_rights_status", "").strip().casefold()
        if rights and any(token in rights for token in ("pending", "not cleared", "unknown", "permission not evidenced")):
            # Source URL can be retained as a research candidate, but it must not be represented as cleared.
            if "cleared" in rights and "not cleared" not in rights:
                errors.append(f"{label}: contradictory image-rights state {rights!r}")

        bonus_url = row.get("bonus_offer_url", "").strip()
        bonus_date = row.get("bonus_checked_utc", "").strip()
        bonus_status = row.get("bonus_status", "").strip().casefold()
        if bonus_date:
            try:
                date.fromisoformat(bonus_date[:10])
            except ValueError:
                errors.append(f"{label}: bonus_checked_utc must start with an ISO date (YYYY-MM-DD)")
        if bonus_status and any(token in bonus_status for token in ("not captured", "not checked", "pending", "unknown")):
            if bonus_date and not bonus_url:
                warnings.append(f"{label}: dated bonus status has no official offer URL")
        if bonus_url and not bonus_date:
            warnings.append(f"{label}: bonus source has no checked date; do not publish as current")

        # New sign-off fields must never be left ambiguous: blank is not evidence of a test or approval.
        for field in ("consumer_test_status", "affiliate_disclosure_status"):
            if not row.get(field, "").strip():
                errors.append(f"{label}: {field} must explicitly state its status")
        for field in ("independent_review_date", "editorial_approval_date"):
            raw_date = row.get(field, "").strip()
            if raw_date:
                try:
                    date.fromisoformat(raw_date[:10])
                except ValueError:
                    errors.append(f"{label}: {field} must start with an ISO date (YYYY-MM-DD)")

        domain_status_raw = row.get("domain_verification_status", "").strip().upper()
        domain_status = re.split(r"\s*[—–-]\s*", domain_status_raw, maxsplit=1)[0].strip()
        domain_date = row.get("domain_verified_utc", "").strip()
        domain_evidence = row.get("domain_evidence_url", "").strip()
        allowed_domain_states = {"UNVERIFIED", "VERIFIED", "REJECTED", "NEEDS_REVIEW"}
        if domain_status and domain_status not in allowed_domain_states:
            errors.append(f"{label}: domain_verification_status must be one of {', '.join(sorted(allowed_domain_states))}")
        if domain_date:
            try:
                date.fromisoformat(domain_date[:10])
            except ValueError:
                errors.append(f"{label}: domain_verified_utc must start with an ISO date (YYYY-MM-DD)")
        if domain_status == "VERIFIED" and (not domain_date or not has_https_url(domain_evidence)):
            errors.append(f"{label}: VERIFIED domain identity requires domain_verified_utc and HTTPS domain_evidence_url")

        state = row.get("publication_status", "").strip().upper()
        # Accept common dash punctuation after a canonical state while keeping the
        # actual decision vocabulary closed to the explicit allow-list.
        canonical_state = re.split(r"\s*[—–-]\s*", state, maxsplit=1)[0].strip()
        is_publishable = canonical_state in PUBLISHABLE_STATES

        # Market scope is an independent release gate: a populated brand record is not
        # proof that online casino acquisition is lawful in every country or sub-jurisdiction.
        if is_publishable:
            if market in {"AU", "FR"}:
                errors.append(f"{label}: publication blocked for {market}; online-casino acquisition scope is excluded pending qualified legal review")
            if market == "US":
                errors.append(f"{label}: publication blocked for aggregate US market; exact state-level authorisation is required")
            if market == "CA":
                errors.append(f"{label}: publication blocked for aggregate CA market; exact province and regulator authorisation are required")
            if market == "BE" and not row.get("official_register_url", "").strip():
                errors.append(f"{label}: Belgium publication requires the exact Belgian Gaming Commission register entry")
            if market == "SE" and not row.get("official_register_url", "").strip():
                errors.append(f"{label}: Sweden publication requires the exact regulator register entry")
            if market == "ES" and not row.get("official_register_url", "").strip():
                errors.append(f"{label}: Spain publication requires the exact DGOJ register entry")
            if market == "IT" and not row.get("official_register_url", "").strip():
                errors.append(f"{label}: Italy publication requires the exact ADM register entry")

        if is_publishable:
            if domain_status != "VERIFIED" or not domain_date or not has_https_url(domain_evidence):
                errors.append(f"{label}: publication requires VERIFIED exact brand/domain identity with dated HTTPS evidence")
            required = (
                "official_url", "legal_entity", "regulator", "official_register_url",
                "terms_url", "withdrawals_url", "complaints_url",
                "responsible_gambling_url", "bonus_offer_url", "bonus_checked_utc",
                "image_source_url", "image_rights_status", "overall_score_100",
                "deposit_methods_url", "fees_limits_url", "privacy_cookies_url",
                "accessibility_evidence_url", "regulatory_actions_url", "adr_url",
                "reviewer_primary", "reviewer_secondary", "independent_review_date",
                "editorial_approval_date", "consumer_test_status",
                "affiliate_disclosure_status", "evidence_bundle_path",
            )
            absent = [field for field in required if not row.get(field, "").strip()]
            if absent:
                errors.append(f"{label}: publication state {state!r} lacks required fields: {', '.join(absent)}")
            if row.get("reviewer_primary", "").strip().casefold() == row.get("reviewer_secondary", "").strip().casefold():
                errors.append(f"{label}: primary and secondary reviewers must be named and different")
            if row.get("consumer_test_status", "").strip().upper() != "COMPLETED":
                errors.append(f"{label}: publication blocked until consumer/usability testing is documented as COMPLETED")
            if row.get("affiliate_disclosure_status", "").strip().upper() != "REVIEWED":
                errors.append(f"{label}: publication blocked until affiliate disclosure is reviewed")
            rights_state = row.get("image_rights_status", "").casefold()
            if "cleared" not in rights_state or any(token in rights_state for token in ("not cleared", "pending", "unknown", "permission not evidenced")):
                errors.append(f"{label}: publication blocked until image rights are explicitly cleared")
            if not re.search(r"second reviewer|independent review|editorial approval", row.get("blockers", ""), re.I):
                warnings.append(f"{label}: publication state should cite independent-review/editorial approval evidence in blockers or the linked review record")
    # Coverage diagnostics are warnings, not publication approval. US states and Canadian
    # provinces roll up only for coverage counting; each row still needs its exact local gate.
    represented_markets = set()
    for row in rows:
        code = row.get("market_code", "").strip().upper()
        if code.startswith("US-"):
            represented_markets.add("US")
        elif code.startswith("CA-"):
            represented_markets.add("CA")
        elif code:
            represented_markets.add(code)
    missing_markets = sorted(TARGET_MARKETS - represented_markets)
    if missing_markets:
        warnings.append(
            "target-market coverage gaps: " + ", ".join(missing_markets)
            + "; absence is not evidence of market eligibility, and AU/FR online-casino acquisition remains gated"
        )
    return len(rows)


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_LEDGER
    try:
        count = check(path)
    except (OSError, UnicodeError, csv.Error) as exc:
        print(f"ERROR: cannot read ledger: {exc}", file=sys.stderr)
        return 2
    for message in errors:
        print("ERROR:", message)
    for message in warnings:
        print("WARN:", message)
    if errors:
        print(f"Review ledger gate: FAIL ({len(errors)} errors, {len(warnings)} warnings; {count} rows)")
        return 1
    print(f"Review ledger gate: PASS structurally ({count} rows, {len(warnings)} warnings). This does not approve any brand or verify live evidence.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
