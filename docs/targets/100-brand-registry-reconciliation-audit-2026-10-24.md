# 100-brand target — registry reconciliation audit

**Audit date:** 24 October 2026  
**Branch:** `ops/2026-10-24-target-reconciliation-and-release-gates`  
**Status:** Internal QA / not for publication

## Reproducible counts from `docs/brand-research-template.csv`

| Measure | Count | Meaning |
|---|---:|---|
| Candidate rows | 204 | Market-specific registry records, not approved brands |
| Distinct display names | 204 | Names differ, but cross-market aliases can represent the same global brand |
| Non-empty provisional global brand IDs | 154 | Useful deduplication keys; not 154 regulator-verified eligible operators |
| Distinct brand-ID / market pairs excluding explicit unconfirmed/excluded codes | 200 | Market leads; still subject to legal and identity qualification |
| Rows with publication decision HOLD | 202 | Not approved |
| Rows rejected | 2 | Must not count toward the target |
| Rows approved for publication | **0** | The 100-review target remains unmet |

The registry contains 30 global-brand IDs that repeat across more than one row/market. Examples include bet365-casino, 888casino, betway, leovegas, unibet-casino, pokerstars-casino, bwin, betano, betmgm-casino, betsson and casino777. Cross-market rows do not increase the unique-global-brand count. No duplicate eligible brand-ID/market pair was found by the CSV-level key check, but this does not prove that the candidate is eligible or that the IDs themselves are all canonical.

## File inventory — do not confuse records with reviews

The `docs/reviews/internal/` directory currently contains 165 files, including research batches, market-scope memos, product-scope checks and candidate-specific evidence-review drafts. A filename inventory finds 50 files matching the candidate evidence-review naming pattern. These are research artifacts, not 50 publication-approved reviews. The separate `review-drafts/` folder contains 21 additional drafts; some overlap the same brands and are not additive without reconciliation.

## Required next steps

1. Reconcile global IDs and aliases to one canonical brand ledger, while preserving distinct brand and market records where justified.
2. For every candidate, verify current local online-casino permission, exact consumer domain and contracting entity against the relevant official regulator and live contract.
3. Exclude candidates with inactive, expired, mismatched or unsupported permission; do not pad a jurisdictional quota.
4. Complete current terms, bonus, payments/withdrawals, complaints/ADR, safer-gambling, privacy/cookies, accessibility and enforcement evidence with dated sources.
5. Produce original, market-specific consumer analysis without claiming unperformed deposits, withdrawals, account creation, support contacts or gameplay.
6. Obtain independent second-review and editorial/legal approval before changing any row to `approved` or publishing a scored profile.

## Current conclusion

There are enough *raw candidate rows* to research a 100-review target, but the current registry does **not** yet establish 100 distinct eligible brands and has **0/100 approved reviews**. Do not index or publish internal research as if it were completed consumer reviews. The nine Belgium A+ records are local domain/operator leads, not nine new global brands; Circus and PokerStars.be share one A+ dossier/operator.

This audit is a registry consistency snapshot only. It is not a legal opinion, consumer test, independent review or deployment sign-off.


## Belgium A+ reconciliation correction — 24 October 2026

The current official Belgian Gaming Commission A+ table surfaces **10 domain/brand records under 9 A+ licence dossiers**: Casino777, Napoleon, StarCasino, Betano, Circus, PokerStars.be, Ladbrokes, Unibet, bwin and Betsson Casino. Circus and PokerStars.be share dossier 20635 / SA/NV GAMBLING MANAGEMENT. Dossier 595153 is currently surfaced with `betssoncasino.be` and SA/NV EXPLOITATIE CASINO MIDDELKERKE (listed expiry 22 February 2039); earlier project evidence referred to `betfirstcasino.be`. This discrepancy is a domain/brand transition to investigate, not a reason to infer continuity of the customer contract. All ten domain records remain HOLD, and the Belgian batch adds **0 approved reviews**.

Official source: https://data.gamingcommission.be/licenses/APLUS/latest/table.html?lang=en
