# Registry audit — 23 October 2026

Input: `docs/brand-research-template.csv` on the research branch.

## Count reconciliation

- 204 non-empty market-specific rows.
- 154 distinct `global_brand_id` values; 30 IDs recur in more than one market.
- 163 rows marked `evidence captured`, 28 `research`, 7 `scope triage`, 4 `research lead — unverified`, 2 excluded.
- 202 rows are `HOLD`; 2 are rejected.
- Publication-approved reviews: **0/100**.

These are candidate/evidence tracking counts, not 154 verified operators or 100 publishable reviews.

## Market row counts

| Market | Rows | Current publication state |
|---|---:|---|
| IT | 46 | All HOLD |
| US-NJ | 30 | All HOLD |
| GB | 23 | All HOLD |
| ES | 19 | 18 HOLD, 1 rejected |
| US-MI | 14 | All HOLD |
| CA-ON | 13 | All HOLD |
| DE | 13 | All HOLD |
| CH | 10 | All HOLD |
| BE | 10 | All HOLD |
| NL | 8 | All HOLD |
| SE | 7 | All HOLD |
| CA-QC | 2 | All HOLD |
| FR | 2 | Legal-scope review needed; both HOLD |
| US-PA | 1 | HOLD |
| CA-BC | 1 | HOLD |
| DE-SH | 1 | HOLD |
| UNCONFIRMED | 3 | Not confirmed; HOLD |
| EXCLUDED | 1 | Rejected |

## Required evidence fields — blank counts out of 204, after the latest source-link updates

| Field | Blank rows |
|---|---:|
| Current terms URL | 182 |
| Withdrawal-policy URL | 199 |
| Complaints/ADR URL | 198 |
| Responsible-gambling URL | 195 |
| Privacy/tracking review | 62 |
| Partnership contact URL | 204 |
| Partnership evidence URL | 204 |
| Launch year and source URL | 204 each |
| Listing-fee fit score | 204 |
| Fit rationale | 92 |
| Sales priority | 99 |
| Decision-maker contact source | 142 |

A populated field is not automatically verified; every source must match the exact market, operator and product.

## Repeat global IDs to deduplicate

- `bet365-casino`: 5 market rows.
- `888casino`, `pokerstars-casino`, `betsson`: 4 rows each.
- `betway`, `leovegas`, `unibet-casino`, `bwin`, `betano`, `betmgm-casino`, `draftkings-casino`, `fanduel-casino`, `betrivers-casino`, `hard-rock-bet-casino`: 3 rows each.

One global brand can have different local operators and permissions, but country/state/province variants must not be counted as distinct global brands unless the target explicitly means market-specific products. The PokerStars GB route currently returned FanDuel-branded US-facing content in extraction, so its current GB brand/domain identity remains unresolved; see the internal PokerStars dossier.

## Work order to reach the first target

1. Deduplicate to a shortlist of 100 distinct global brands and exclude unconfirmed/ineligible records.
2. Verify regulator permission, exact domain, legal contracting entity and local market scope from primary sources.
3. Complete current terms, offer-specific bonus conditions (or say unverified), payment/withdrawal methods and limits, fees, complaints/ADR, safer-gambling, privacy/cookies and enforcement evidence.
4. Keep every draft HOLD until an independent second editor and editorial/legal/affiliate-disclosure sign-off are recorded.
5. Publish only approved reviews after authorised Cloudflare Pages release; then verify canonical/indexability and inspect URLs in Search Console.

## 10 million daily impressions: measurement gates

10 million/day is approximately 300 million impressions per 30 days. This registry has no verified Search Console baseline, so it cannot support a deadline or traffic forecast. Establish a 28-day baseline first, then track sustained 10k/day, 100k/day, 1m/day and 10m/day stages using impressions, clicks, CTR, position, country/device, query and canonical URL data. More candidate rows or published pages do not guarantee impressions.

Research-only. No deployment, `main` merge, DNS change or Search Console write. Keep using `[CF-Pages-Skip]` for research commits to avoid unnecessary Cloudflare builds.

## Source-link maintenance — 23 October 2026

The candidate CSV was updated with official Great Britain policy links for 888casino, bet365 Casino, Betway Casino and William Hill Casino. The generic 888 user-agreement URL was replaced by the GB-specific agreement; William Hill and bet365 terms/complaint routes were added; current responsible-gambling links were added where directly sourced. Betway's dynamic policy routes remain extraction-limited and are explicitly marked as unverified policy text, not absent. CSV commit: `a3cc48798fce39aa98d01a1fe055a6e2b9fa991e`.
