# 100-brand target — registry reconciliation audit

**Audit date:** 24 October 2026  
**Branch:** `ops/2026-10-24-target-reconciliation-and-release-gates`  
**Status:** Internal QA / not for publication

## Reproducible counts from `docs/brand-research-template.csv`

| Measure | Count | Meaning |
|---|---:|---|
| Candidate rows | 208 | Market-specific registry records, not approved brands |
| Distinct display names | 208 | Names differ, but cross-market aliases can represent the same global brand |
| Non-empty provisional global brand IDs | 208 | Every row currently has a populated ID; there are 157 distinct IDs, not 208 unique global brands |
| Distinct brand-ID / market pairs excluding explicit unconfirmed/excluded codes | 204 | Market leads; still subject to legal and identity qualification |
| Rows with publication decision HOLD | 206 | Not approved |
| Rows rejected | 2 | Must not count toward the target |
| Rows approved for publication | **0** | The 100-review target remains unmet |

The registry contains 31 global-brand IDs that repeat across more than one row/market. Examples include bet365-casino, 888casino, pokerstars-casino, betsson, betway, leovegas, unibet-casino, bwin, betano, betmgm-casino, draftkings-casino, fanduel-casino, betrivers-casino, hard-rock-bet-casino and fanatics-casino. Cross-market rows do not increase the unique-global-brand count. No duplicate eligible brand-ID/market pair was found by the CSV-level key check, but this does not prove that the candidate is eligible or that the IDs themselves are all canonical.

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


## Detailed market-row reconciliation — 24 October 2026

The current CSV snapshot (208 data rows) breaks down as follows. These are **raw rows**, not eligible or unique global brands.

| Market code | Rows | Scope caveat |
|---|---:|---|
| GB | 24 | Match current Casino Remote permission, exact live domain, contract and enforcement; Midnite remains HOLD because two UKGC account/domain records need resolution |
| IT | 46 | Large lead buffer; verify casino vertical and active ADM concession |
| ES | 19 | Match current DGOJ casino permission and exact product/domain |
| US-NJ | 30 | New Jersey only; multiple brands may share licensed casino affiliates |
| US-MI | 14 | Michigan only |
| US-PA | 2 | Pennsylvania-specific leads; BetRivers and the newer Hollywood Casino Online route remain HOLD |
| CA-ON | 13 | Ontario only; not all Canada |
| CA-BC | 1 | British Columbia only |
| CA-QC | 2 | Québec-specific product and operator checks |
| CH | 10 | ESBK platform association does not replace game-specific permission or contract check |
| BE | 10 | A+ domain leads; nine dossier rows in the current surfaced table because Circus/PokerStars share one record and Betsson is now surfaced on the current domain |
| NL | 8 | Check shared operators and exact Ksa product/domain |
| SE | 7 | Current domain-specific licence and terms required |
| DE | 13 | Mixed nationwide and category/state-specific leads |
| DE-SH | 2 | Schleswig-Holstein-specific; reconcile overlap with DE |
| FR | 2 | Online casino is not generally authorised; do not count these as eligible casino brands without a lawful product-specific basis |
| UNCONFIRMED | 3 | Not countable until market and local route are evidenced |
| EXCLUDED | 1 | Archive only |

Repeated global identities include bet365 (5 rows), 888casino (4), PokerStars (4), Betsson (4), Betway (3), LeoVegas (3), Unibet (3), bwin (3), Betano (3), BetMGM (3), DraftKings (3), FanDuel (3), BetRivers (3), Hard Rock Bet (3) and Fanatics (3). Count each canonical brand once globally even if multiple market-specific reviews are later approved.

## Scope-triage identities and exclusions

Seven canonical IDs have at least one scope-triage record: ComeOn Casino, Betano, Betsson, NordicBet Casino, Betclic, Winamax and Espacejeux. Three records remain in UNCONFIRMED (Betsson, NordicBet Casino and Rizk) and must not count until a named target market and local route are evidenced. Two rejected rows are 32Red (inactive current GB casino permission/domain) and Betfred (Spain casino permission extinguished in 2023); the latter rejection applies to the Spanish row, not automatically to unrelated markets. Current totals: 208 market-specific rows, 157 distinct global IDs, 206 HOLD and 2 rejected.

## Belgium source correction

The current surfaced Belgian A+ table associates dossier 595153 with betssoncasino.be, Casino Middelkerke x Betsson, SA/NV EXPLOITATIE CASINO MIDDELKERKE, listed expiry 22 February 2039. An earlier captured row associated that dossier with betfirstcasino.be. This is a material domain/brand transition and remains HOLD until the current live legal footer and customer contract are matched. The separate B+ leads are not counted as A+ casino licences.


## Updated artifact inventory — 24 October 2026

A fresh GitHub directory listing on the current branch returned:
- `docs/reviews/internal/`: **170 files** total.
- Candidate-specific filenames matching the evidence-review/product-scope-review pattern: **63**.
- `review-drafts/`: **21 files**.

These are file counts, not completed consumer reviews. They may overlap by brand and market, include scope checks rather than finished reviews, and do not have second-review/editorial approval merely because a file exists. The approved review count remains **0/100**.

## Sweden — current Betsson URL / licence-holder conflict (24 October 2026)

A new official-register recheck shows both Betsson Nordic Ltd and Spin Nordic Ltd on the URL lookup for `betsson.com` and `betsson.com/sv`. The lookup includes a commercial-online licence period from 24 August 2026 to 23 August 2031, while the separate Betsson Nordic holder page still records its 2025 AML warning as appealed. The URL page alone does not clearly map each licence line to each holder. Do not assume the older holder still contracts with Swedish customers, and do not attribute Betsson Nordic Ltd's SEK 6.5m AML sanction to Spin Nordic Ltd without evidence. The current Swedish customer contract and exact licence-holder mapping remain unresolved; Betsson SE stays HOLD and adds zero approved reviews.

Sources: https://www.spelinspektionen.se/licens-o-tillstand/licensregister/licensurl/?url=betsson.com ; https://www.spelinspektionen.se/licens-o-tillstand/licensregister/licensurl/?url=betsson.com/sv ; https://www.spelinspektionen.se/licens-o-tillstand/licensregister/licenshallare/?id=55963B9F241E74FEF05A9A6199A7FEA3C303C08563FEFA6BAA7412866C21B9A8
