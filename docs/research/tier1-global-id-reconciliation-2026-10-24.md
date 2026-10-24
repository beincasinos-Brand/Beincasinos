# Tier-1 prospect global-ID reconciliation — 24 October 2026

**Purpose:** fill only high-confidence global brand IDs where the Tier-1 prospect row clearly refers to a customer-facing brand already present in the canonical research registry. This is a data-quality reconciliation, not a licensing, market-eligibility or review approval.

## IDs filled in this pass

| Tier-1 tracker label | Market | Assigned canonical ID | Existing registry evidence | Scope/caution |
|---|---|---|---|---|
| admiral.ch | CH | `admiral` | `Admiral.ch (CH)` | Swiss market record only; legal contracting entity remains to verify. |
| Ember Casino | US-NJ | `ember-casino` | `Ember Casino (NJ)` | New Jersey only; operator/skin relationship still requires review. |
| Horseshoe Online Casino (Michigan) | US-MI | `horseshoe-online-casino` | `Horseshoe Online Casino (MI)` and `(NJ)` | Same global product identity, separate market records; do not merge jurisdictional evidence. |
| Betinia Casino | US-NJ | `betinia` | `Betinia (NJ)` | New Jersey only; skin and contracting-party details remain a review item. |
| TOTO | NL | `toto-casino` | `TOTO Casino (NL)` | Product/permit scope and exact current domain remain unverified. |
| Kansino | NL | `kansino` | `Kansino (NL)` | Product/permit scope and exact current domain remain unverified. |
| Bingoal | NL | `bingoal` | `Bingoal (NL)` | Product/permit scope and exact current domain remain unverified. |
| Betcity | NL | `betcity` | `BetCity (NL)` | Product/permit scope and exact current domain remain unverified. |
| BetMGM | NL | `betmgm-casino` | `BetMGM Casino`, `(MI)`, `(NJ)` | Global identity only; this does **not** establish BetMGM's current Dutch licence, domain or market availability. |
| Monopoly Casino | US-NJ | `monopoly-casino` | `Monopoly Casino (NJ)` | New Jersey only; live domain and operator relationship remain unverified. |
| Hard Rock Bet | US-MI | `hard-rock-bet-casino` | `Hard Rock Bet Casino`, `(MI)`, `(NJ)` | Global identity only; Michigan permissions/domain must be verified before any publication. |
| theScore Bet | US-NJ | `thescore-bet-casino` | `theScore Bet Casino (NJ)` | New Jersey only; exact active domain/operator record still requires verification. |

## Explicitly not mapped

- `Starcasino.nl`: the registry has similarly named BE and IT rows, but the Netherlands identity is not established by a matching market-specific record. Leave blank pending source verification.
- `Fun Casino` (GB): the only registry name match in this snapshot is a Swedish market row. The generic name plus cross-market mismatch is not enough to infer a global identity.

## Counting effect

Before this pass the tracker had 114 market-specific rows, 97 blank IDs and 17 populated ID cells / 16 distinct IDs. This pass filled 12 previously blank cells using IDs already present in the registry; it creates no new canonical IDs. The resulting tracker should have **85 blank ID cells, 29 populated ID cells and 28 distinct IDs** (unless the snapshot changes concurrently).

These are bookkeeping IDs, not 28 eligible operators or completed reviews. The tracker still contains provisional leads, unknown domains and market/vertical checks. The approved consumer-review count remains **0/100**. Do not collapse market-specific records in the evidence itself; preserve each market's operator, domain, permissions, terms, consumer protections and enforcement history.

## Validation to run

- `python3 scripts/check_prospect_tracker.py`
- `python3 scripts/check_tracker_registry_links.py`
- `python3 -m unittest scripts.test_tracker_registry_links -v`

The GitHub Actions runner currently fails before executing steps, so this reconciliation has not yet been validated by a successful CI run.
