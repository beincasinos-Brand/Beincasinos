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
            "overall_score_100": "",
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


if __name__ == "__main__":
    unittest.main()
