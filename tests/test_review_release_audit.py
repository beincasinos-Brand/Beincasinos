import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "review_release_audit.py"
SPEC = importlib.util.spec_from_file_location("review_release_audit", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

class ReviewReleaseAuditTests(unittest.TestCase):
    def test_parser_extracts_title_h1_canonical_and_image(self):
        parser = MODULE.PageParser()
        parser.feed('<html><head><title>Sample review</title><link rel="canonical" href="https://example.test/reviews/sample/"></head><body><h1>Sample review</h1><img src="/sample.webp" alt="Sample casino lobby"></body></html>')
        self.assertEqual(" ".join(parser.title_parts), "Sample review")
        self.assertEqual(" ".join(parser.h1_parts), "Sample review")
        self.assertEqual(parser.canonical, "https://example.test/reviews/sample/")
        self.assertEqual(parser.images[0]["alt"], "Sample casino lobby")

    def test_audit_flags_missing_canonical_and_disclosures(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "sample" / "index.html"
            page.parent.mkdir()
            page.write_text("<html><head><title>Short</title></head><body><h1>Short</h1><p>Small page.</p></body></html>", encoding="utf-8")
            result = MODULE.audit(page, root)
            codes = {flag["code"] for flag in result["flags"]}
            self.assertIn("missing_canonical", codes)
            self.assertIn("thin_text", codes)
            self.assertIn("affiliate_disclosure_not_detected", codes)
            self.assertIn("safer_gambling_not_detected", codes)

    def test_first_hand_testing_and_absolute_claims_are_flagged(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "claims.html"
            page.write_text("<title>Example</title><h1>Example</h1><p>We tested it. This is 100% safe.</p>", encoding="utf-8")
            codes = {flag["code"] for flag in MODULE.audit(page, root)["flags"]}
            self.assertIn("first_hand_testing_claim", codes)
            self.assertIn("absolute_gambling_claim", codes)

    def test_numeric_score_is_flagged_for_human_verification(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            page = root / "score.html"
            page.write_text("<title>Example</title><h1>Example</h1><p>Affiliate commission. Gamble responsibly. Score: 8.2/10</p>", encoding="utf-8")
            codes = {flag["code"] for flag in MODULE.audit(page, root)["flags"]}
            self.assertIn("numeric_score_present", codes)

if __name__ == "__main__":
    unittest.main()
