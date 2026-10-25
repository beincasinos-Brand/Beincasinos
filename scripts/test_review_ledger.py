"""Regression tests for the evidence-first review-ledger gate."""
import csv
import tempfile
import unittest
from pathlib import Path

from scripts import check_review_ledger as gate


def sample_rows():
    rows = []
    for i in range(100):
        rows.append({
            "slot": str(i + 1),
            "brand_name": f"Test Casino {i + 1}",
            "global_brand_id": f"test-casino-{i + 1}",
            "market_code": "GB",
            "official_url": f"https://example{i + 1}.invalid/",
            "legal_entity": "",
            "regulator": "",
            "official_register_url": "",
            "terms_url": "",
            "withdrawals_url": "",
            "complaints_url": "",
            "responsible_gambling_url": "",
            "bonus_offer_url": "",
            "bonus_checked_utc": "",
            "bonus_status": "NOT CAPTURED",
            "image_source_url": "",
            "image_rights_status": "PENDING — official source and reuse permission required",
            **{name: "" for name in gate.SCORE_LIMITS},
            "overall_score_100": "NOT SCORED",
            "review_status": "NOT SCORED",
            "publication_status": "HOLD — not approved for publication",
            "blockers": "Evidence incomplete",
            "deposit_methods_url": "",
            "fees_limits_url": "",
            "privacy_cookies_url": "",
            "accessibility_evidence_url": "",
            "regulatory_actions_url": "",
            "adr_url": "",
            "reviewer_primary": "",
            "reviewer_secondary": "",
            "independent_review_date": "",
            "editorial_approval_date": "",
            "consumer_test_status": "NOT PERFORMED",
            "affiliate_disclosure_status": "NOT REVIEWED",
            "evidence_bundle_path": "",
            "domain_verification_status": "UNVERIFIED — exact brand/domain match not fully reviewed",
            "domain_verified_utc": "",
            "domain_evidence_url": "",
        })
    return rows


class ReviewLedgerGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name) / "ledger.csv"
        self.rows = sample_rows()
        self.columns = list(self.rows[0])
        self.write()
        gate.errors.clear()
        gate.warnings.clear()

    def tearDown(self):
        self.temp.cleanup()
        gate.errors.clear()
        gate.warnings.clear()

    def write(self):
        with self.path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=self.columns)
            writer.writeheader()
            writer.writerows(self.rows)

    def test_held_candidates_can_remain_unscored(self):
        self.assertEqual(gate.check(self.path), 100)
        self.assertEqual(gate.errors, [])

    def test_partial_rubric_score_is_rejected(self):
        self.rows[0]["score_licence_20"] = "18"
        self.write()
        gate.check(self.path)
        self.assertTrue(any("partial rubric score" in message for message in gate.errors))

    def test_overall_score_must_match_component_sum(self):
        for field, maximum in gate.SCORE_LIMITS.items():
            self.rows[0][field] = str(maximum)
        self.rows[0]["overall_score_100"] = "99"
        self.write()
        gate.check(self.path)
        self.assertTrue(any("overall score must equal component sum 100" in message for message in gate.errors))

    def test_non_https_source_url_is_rejected(self):
        self.rows[0]["official_url"] = "http://example.invalid/"
        self.write()
        gate.check(self.path)
        self.assertTrue(any("official_url must be an HTTPS URL" in message for message in gate.errors))

    def test_malformed_bonus_check_date_is_rejected(self):
        self.rows[0]["bonus_offer_url"] = "https://example.invalid/bonus"
        self.rows[0]["bonus_checked_utc"] = "24-10-2026"
        self.write()
        gate.check(self.path)
        self.assertTrue(any("bonus_checked_utc must start with an ISO date" in message for message in gate.errors))

    def test_duplicate_brand_market_identity_is_rejected(self):
        self.rows[1]["brand_name"] = self.rows[0]["brand_name"]
        self.write()
        gate.check(self.path)
        self.assertTrue(any("duplicate brand/market identity" in message for message in gate.errors))

    def test_published_state_without_evidence_and_rights_is_rejected(self):
        self.rows[0]["publication_status"] = "PUBLISHED"
        self.write()
        gate.check(self.path)
        self.assertTrue(any("lacks required fields" in message for message in gate.errors))
        self.assertTrue(any("image rights are explicitly cleared" in message for message in gate.errors))


    def test_aggregate_us_publication_is_blocked_even_with_other_fields_missing(self):
        self.rows[0]["market_code"] = "US"
        self.rows[0]["publication_status"] = "PUBLISHED"
        self.write()
        gate.check(self.path)
        self.assertTrue(any("aggregate US market" in message for message in gate.errors))

    def test_australia_publication_is_blocked_pending_legal_review(self):
        self.rows[0]["market_code"] = "AU"
        self.rows[0]["publication_status"] = "APPROVED_TO_PUBLISH"
        self.write()
        gate.check(self.path)
        self.assertTrue(any("publication blocked for AU" in message for message in gate.errors))

    def test_european_market_publication_requires_exact_regulator_register(self):
        cases = (
            ("BE", "Belgium publication requires the exact Belgian Gaming Commission register entry"),
            ("SE", "Sweden publication requires the exact regulator register entry"),
            ("ES", "Spain publication requires the exact DGOJ register entry"),
            ("IT", "Italy publication requires the exact ADM register entry"),
        )
        for market, expected_error in cases:
            with self.subTest(market=market):
                self.rows[0]["market_code"] = market
                self.rows[0]["publication_status"] = "PUBLISHED"
                self.rows[0]["official_register_url"] = ""
                self.write()
                gate.check(self.path)
                self.assertTrue(any(expected_error in message for message in gate.errors))

    def test_unknown_market_code_is_rejected(self):
        self.rows[0]["market_code"] = "GH"
        self.write()
        gate.check(self.path)
        self.assertTrue(any("outside the approved target-market code format" in message for message in gate.errors))

    def test_state_with_en_dash_still_triggers_publication_gates(self):
        self.rows[0]["market_code"] = "AU"
        self.rows[0]["publication_status"] = "APPROVED_TO_PUBLISH – reviewed"
        self.write()
        gate.check(self.path)
        self.assertTrue(any("publication blocked for AU" in message for message in gate.errors))

    def test_target_market_coverage_gaps_are_reported_as_warnings(self):
        self.write()
        gate.check(self.path)
        self.assertTrue(any("target-market coverage gaps" in message for message in gate.warnings))
        self.assertFalse(any("target-market coverage gaps" in message for message in gate.errors))

    def test_publishable_row_requires_dated_exact_domain_evidence(self):
        self.rows[0]["publication_status"] = "PUBLISHED"
        self.rows[0]["domain_verification_status"] = "UNVERIFIED"
        self.write()
        gate.check(self.path)
        self.assertTrue(any("publication requires VERIFIED exact brand/domain identity" in message for message in gate.errors))

    def test_verified_domain_requires_date_and_https_evidence(self):
        self.rows[0]["domain_verification_status"] = "VERIFIED"
        self.rows[0]["domain_verified_utc"] = ""
        self.rows[0]["domain_evidence_url"] = ""
        self.write()
        gate.check(self.path)
        self.assertTrue(any("VERIFIED domain identity requires" in message for message in gate.errors))

    def test_verified_domain_rejects_malformed_verification_date(self):
        self.rows[0]["domain_verification_status"] = "VERIFIED"
        self.rows[0]["domain_verified_utc"] = "25/10/2026"
        self.rows[0]["domain_evidence_url"] = "https://regulator.example/register"
        self.write()
        gate.check(self.path)
        self.assertTrue(any("domain_verified_utc must start with an ISO date" in message for message in gate.errors))

    def test_bonus_checked_date_rejects_trailing_garbage(self):
        self.rows[0]["bonus_checked_utc"] = "2026-10-25-not-a-date"
        self.rows[0]["bonus_offer_url"] = "https://example.invalid/bonus"
        self.write()
        gate.check(self.path)
        self.assertTrue(any("bonus_checked_utc must start with an ISO date" in message for message in gate.errors))

    def test_signoff_dates_reject_trailing_garbage(self):
        self.rows[0]["independent_review_date"] = "2026-10-25-not-a-date"
        self.write()
        gate.check(self.path)
        self.assertTrue(any("independent_review_date must start with an ISO date" in message for message in gate.errors))

    def test_verified_domain_rejects_trailing_date_garbage(self):
        self.rows[0]["domain_verification_status"] = "VERIFIED"
        self.rows[0]["domain_verified_utc"] = "2026-10-25-not-a-date"
        self.rows[0]["domain_evidence_url"] = "https://regulator.example/register"
        self.write()
        gate.check(self.path)
        self.assertTrue(any("domain_verified_utc must start with an ISO date" in message for message in gate.errors))

    def test_verified_domain_rejects_non_https_evidence(self):
        self.rows[0]["domain_verification_status"] = "VERIFIED"
        self.rows[0]["domain_verified_utc"] = "2026-10-25"
        self.rows[0]["domain_evidence_url"] = "http://regulator.example/register"
        self.write()
        gate.check(self.path)
        self.assertTrue(any("domain_evidence_url must be an HTTPS URL" in message for message in gate.errors))

    def test_unknown_domain_verification_state_is_rejected(self):
        self.rows[0]["domain_verification_status"] = "MAYBE"
        self.write()
        gate.check(self.path)
        self.assertTrue(any("domain_verification_status must be one of" in message for message in gate.errors))

    def test_ontario_scope_is_not_treated_as_nationwide_canada(self):
        self.rows[0]["market_code"] = "CA"
        self.rows[0]["publication_status"] = "LIVE"
        self.write()
        gate.check(self.path)
        self.assertTrue(any("exact province and regulator authorisation" in message for message in gate.errors))


if __name__ == "__main__":
    unittest.main()
