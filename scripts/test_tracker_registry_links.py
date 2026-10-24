"""Regression tests for conservative prospect-to-registry ID reconciliation."""
import unittest

from scripts.check_tracker_registry_links import (
    build_registry_ids,
    validate_exact_name_mappings,
)


class ExactNameMappingTests(unittest.TestCase):
    def test_exact_name_matching_id_passes(self):
        registry = build_registry_ids([
            {"brand_name": "Fanatics Casino", "global_brand_id": "fanatics-casino"}
        ])
        errors, warnings, checked = validate_exact_name_mappings([
            {"brand_name": "FANATICS CASINO", "global_brand_id": "fanatics-casino"}
        ], registry)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])
        self.assertEqual(checked, 1)

    def test_blank_id_for_unique_exact_match_fails(self):
        registry = build_registry_ids([
            {"brand_name": "Fanatics Casino", "global_brand_id": "fanatics-casino"}
        ])
        errors, warnings, checked = validate_exact_name_mappings([
            {"brand_name": "Fanatics Casino", "global_brand_id": ""}
        ], registry)
        self.assertEqual(checked, 1)
        self.assertEqual(warnings, [])
        self.assertEqual(len(errors), 1)
        self.assertIn("global_brand_id=fanatics-casino", errors[0])

    def test_conflicting_tracker_id_fails(self):
        registry = build_registry_ids([
            {"brand_name": "Fanatics Casino", "global_brand_id": "fanatics-casino"}
        ])
        errors, warnings, checked = validate_exact_name_mappings([
            {"brand_name": "Fanatics Casino", "global_brand_id": "fanatics"}
        ], registry)
        self.assertEqual(checked, 1)
        self.assertEqual(warnings, [])
        self.assertTrue(any("conflicts with exact-name registry ID" in error for error in errors))

    def test_conflicting_registry_ids_are_not_guessed(self):
        registry = build_registry_ids([
            {"brand_name": "Example Casino", "global_brand_id": "example-a"},
            {"brand_name": "Example Casino", "global_brand_id": "example-b"},
        ])
        errors, warnings, checked = validate_exact_name_mappings([
            {"brand_name": "Example Casino", "global_brand_id": ""}
        ], registry)
        self.assertEqual(errors, [])
        self.assertEqual(checked, 0)
        self.assertEqual(len(warnings), 1)
        self.assertIn("manual reconciliation required", warnings[0])


    def test_tracker_id_absent_from_registry_fails(self):
        registry = build_registry_ids([
            {"brand_name": "Example Casino", "global_brand_id": "example-casino"}
        ])
        errors, warnings, checked = validate_exact_name_mappings([
            {"brand_name": "Different Display Name", "global_brand_id": "made-up-id"}
        ], registry)
        self.assertEqual(warnings, [])
        self.assertEqual(checked, 0)
        self.assertEqual(len(errors), 1)
        self.assertIn("does not exist in the canonical registry", errors[0])

    def test_existing_global_id_allows_market_specific_alias_label(self):
        registry = build_registry_ids([
            {"brand_name": "BetMGM Casino (NJ)", "global_brand_id": "betmgm-casino"}
        ])
        errors, warnings, checked = validate_exact_name_mappings([
            {"brand_name": "BetMGM", "global_brand_id": "betmgm-casino"}
        ], registry)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])
        self.assertEqual(checked, 0)

    def test_nonmatching_alias_is_not_inferred(self):
        registry = build_registry_ids([
            {"brand_name": "Fanatics Casino", "global_brand_id": "fanatics-casino"}
        ])
        errors, warnings, checked = validate_exact_name_mappings([
            {"brand_name": "Fanatics", "global_brand_id": ""}
        ], registry)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])
        self.assertEqual(checked, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
