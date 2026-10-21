#!/usr/bin/env python3
"""Regression tests for the paid-listing tracker validator using isolated fixtures."""
import csv
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "check_sales_pipeline.py"
TRACKER = ROOT / "docs" / "paid-listing-sales-pipeline.csv"
with TRACKER.open(encoding="utf-8-sig", newline="") as handle:
    FIELDS = next(csv.reader(handle))


class SalesPipelineValidatorTests(unittest.TestCase):
    def run_fixture(self, row=None):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "scripts").mkdir()
            (root / "docs").mkdir()
            shutil.copy2(VALIDATOR, root / "scripts" / "check_sales_pipeline.py")
            with (root / "docs" / "paid-listing-sales-pipeline.csv").open("w", newline="", encoding="utf-8") as handle:
                writer = csv.DictWriter(handle, fieldnames=FIELDS)
                writer.writeheader()
                if row is not None:
                    writer.writerow({field: row.get(field, "") for field in FIELDS})
            return subprocess.run(
                [sys.executable, str(root / "scripts" / "check_sales_pipeline.py")],
                capture_output=True, text=True, check=False,
            )

    def test_empty_template_passes(self):
        result = self.run_fixture()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("0 populated prospect row(s)", result.stdout)

    def test_invalid_pipeline_stage_fails(self):
        result = self.run_fixture({"brand_name": "Example", "qualification_status": "hold", "pipeline_stage": "maybe"})
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unknown pipeline_stage", result.stdout)

    def test_contacted_row_requires_first_contact_date(self):
        result = self.run_fixture({
            "brand_name": "Example", "qualification_status": "hold", "pipeline_stage": "contacted",
            "official_contact_source": "https://example.com/contact", "source_evidence_url": "https://example.com/terms",
        })
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("requires first_contact_date_utc", result.stdout)

    def test_contacted_row_rejects_non_https_evidence(self):
        result = self.run_fixture({
            "brand_name": "Example", "qualification_status": "hold", "pipeline_stage": "contacted",
            "first_contact_date_utc": "2026-10-20",
            "official_contact_source": "http://example.com/contact", "source_evidence_url": "https://example.com/terms",
        })
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("valid HTTPS official_contact_source", result.stdout)

    def test_won_paid_listing_rejects_not_applicable_invoice(self):
        row = {
            "brand_name": "Example", "legal_entity": "Example Ltd", "target_market": "GB",
            "qualification_status": "pass", "pipeline_stage": "won",
            "first_contact_date_utc": "2026-10-20",
            "official_contact_source": "https://example.com/contact",
            "source_evidence_url": "https://example.com/terms",
            "agreement_status": "signed", "invoice_status": "not applicable",
            "placement_type": "paid listing", "currency": "GBP",
            "term_start": "2026-10-21", "term_end": "2027-10-20",
            "paid_label_confirmed": "yes", "market_review_confirmed": "yes",
            "privacy_tracking_review": "yes",
        }
        result = self.run_fixture(row)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("not applicable is not accepted for a paid listing", result.stdout)

    def test_won_row_requires_contract_and_review_gates(self):
        result = self.run_fixture({
            "brand_name": "Example", "qualification_status": "pass", "pipeline_stage": "won",
            "first_contact_date_utc": "2026-10-20",
            "official_contact_source": "https://example.com/contact", "source_evidence_url": "https://example.com/terms",
        })
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("won requires signed/executed agreement_status", result.stdout)
        self.assertIn("won requires paid_label_confirmed=yes", result.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
