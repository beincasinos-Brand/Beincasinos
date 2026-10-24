import unittest

from scripts.check_directory_ledger_alignment import compare_identities, parse_directory_identities


class DirectoryLedgerAlignmentTests(unittest.TestCase):
    def test_parses_public_brand_name_and_market(self):
        source = (
            '<article class="brand-card" data-market="NL" data-status="HOLD">'
            '<h2>Holland Casino Online</h2></article>'
            '<article class="brand-card" data-market="US-NJ">'
            '<h2>Ember Casino</h2></article>'
        )
        self.assertEqual(
            parse_directory_identities(source),
            {("Holland Casino Online", "NL"), ("Ember Casino", "US-NJ")},
        )

    def test_exact_identity_sets_pass(self):
        identities = {("Holland Casino Online", "NL"), ("Ember Casino", "US-NJ")}
        self.assertEqual(compare_identities(identities, identities), [])

    def test_market_mismatch_is_not_treated_as_a_match(self):
        directory = {("Tipico Casino", "DE")}
        ledger = {("Tipico Casino", "DE-SH")}
        errors = compare_identities(directory, ledger)
        self.assertTrue(any("missing from canonical ledger" in e for e in errors))
        self.assertTrue(any("absent from public directory" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
