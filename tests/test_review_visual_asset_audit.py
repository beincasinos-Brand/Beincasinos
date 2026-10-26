import tempfile
import unittest
from pathlib import Path

from scripts.review_visual_asset_audit import inspect_page


class ReviewVisualAssetAuditTests(unittest.TestCase):
    def test_ignores_site_logo_and_detects_generic_review_art(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            page = root / "reviews" / "sample" / "index.html"
            page.parent.mkdir(parents=True)
            page.write_text(
                '<img src="/assets/beincasinos-mark.svg" alt="BIC">'
                '<img src="/assets/review-card-art.svg" alt="">',
                encoding="utf-8",
            )
            result = inspect_page(page, root)
            self.assertFalse(result["has_brand_specific_logo_asset"])
            self.assertEqual(result["generic_images"], ["/assets/review-card-art.svg"])
            self.assertEqual(result["missing_alt"], ["/assets/review-card-art.svg"])

    def test_detects_brand_named_logo_asset(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            page = root / "reviews" / "sample" / "index.html"
            page.parent.mkdir(parents=True)
            page.write_text(
                '<img src="/assets/brands/sample-logo.svg" alt="Sample Casino logo">',
                encoding="utf-8",
            )
            result = inspect_page(page, root)
            self.assertTrue(result["has_brand_specific_logo_asset"])
            self.assertEqual(result["missing_alt"], [])


if __name__ == "__main__":
    unittest.main()
