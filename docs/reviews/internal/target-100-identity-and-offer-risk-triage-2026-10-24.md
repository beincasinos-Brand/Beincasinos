# Target-100 identity and offer-risk triage — 24 October 2026

## Purpose
This is a release-risk worklist based on the current internal 100-row ledger and official-source checks. It intentionally does not promote unverified candidates into “verified” brands. No user account was created, no real-money transaction was made, and no consumer test was performed.

## Priority 0 — resolve before calling a row a verified casino
| Slot | Candidate | Market | Current issue | Required evidence / disposition |
|---:|---|---|---|---|
| 15 | Betano Casino | Germany | Current regulator note establishes virtual-slot scope but not a separate table/live-casino permission. | Match the exact licensed vertical and consumer domain. If only virtual slots are authorised, label accurately or remove from a full-casino cohort. |
| 24 | DraftKings Casino | Ontario | Regulator source lists Crown DK CAN Ltd, but ledger has not conclusively matched the exact Ontario consumer domain and contracting entity. | Capture current iGaming Ontario operator record plus the live Ontario terms/entity. |
| 25 | Espacejeux | Québec | Candidate may overlap with Loto-Québec / lotoquebec.com rather than a distinct current product. | Confirm a distinct live product/brand or deduplicate it; do not count one operator/domain twice. |
| 5 | MERKUR Spiel | Schleswig-Holstein | Permission is state-specific, not evidence of nationwide German availability. | Keep the DE-SH scope in title, content, regulator record and eligibility notes. |
| 20 | Tipico Casino | Schleswig-Holstein | Permission is state-specific and exact licensed casino vertical must be preserved. | Confirm current whitelist record and terms; never generalise to all Germany. |

## Priority 1 — offer claims need tighter proof
| Slot | Candidate | Source lead already in ledger | Outstanding control |
|---:|---|---|---|
| 28 | Hollywood Casino (PA) | Official help-centre new-user article | Reconcile conflicting official offer wording; capture complete PA-specific terms and exact eligible product before stating a number. |
| 38 | Fanatics Casino (NJ) | Official casino homepage | Public claim is up to $1,000 in casino credit for eligible first-day losses; credit is not cash. Detailed eligibility and loss calculation remain unverified in-app. |
| 39 | BetRivers Casino (MI) | Official iRush Rewards page | Treat as a loyalty-program source, not a verified welcome offer or cash-equivalent value. |
| 93 | Casineo.ch (CH) | Official promotions and bonus-conditions pages | Confirm the year/expiry, eligibility, wagering and current welcome-offer terms. |
| 95 | Casino Gran Madrid Online (ES) | Official welcome landing page | Recorded campaign ends 2026-10-31; recheck on/after expiry and do not reuse as a current offer without a fresh source. |
| 3 | ComeOn Casino (SE) | Official Swedish promotion page | Recorded page has anomalous start-date text; offer availability is unresolved. Do not present it as current until date/terms are confirmed. |
| 32 | Betsson Casino (SE) | Official bonus page | Source appeared stale in prior review; refresh page and full current terms or leave offer unclaimed. |

## Priority 2 — 46 blank promotion URLs
The current quote-aware ledger parse reports 100 rows, 43 columns, no malformed row widths, no duplicate slot IDs, **54 populated bonus/promotion URLs and 46 blank**. Blank rows are not evidence that no offer exists; they mean an official market-specific promotion source has not yet been captured. Highest-priority blank candidates from the current ledger include:
- Slot 15 Betano Casino (DE): first resolve licensed vertical before searching for a casino offer.
- Slot 19 Winnitt (NL): confirm exact brand/domain/customer contract, then find current official offer terms.
- Slot 23 Luckia (ES): official-site access may be market-restricted; do not substitute unrelated search snippets or generic corporate material.
- Slot 24 DraftKings Casino (CA-ON): resolve exact Ontario route/entity before promotion research.
- Slot 25 Espacejeux (CA-QC): resolve potential duplication before spending further research time.
- Slot 26 Bally Bet Casino (NJ): confirm live product route and contracting entity before offer capture.
- Slot 31 Starcasino.be (BE): capture current official offer only after confirming current licence/domain association.
- Slot 43 Fun Casino (SE): confirm exact active licence/domain and current consumer-facing offer.

## Search discipline and evidence policy
Official-source web searches during this pass did not yield sufficiently complete, current market-specific terms for the named blank candidates above. No speculative URL was inserted, and no bonus amount was inferred from an unrelated page. Next search pass should focus on one market and operator at a time, prioritising exact licence/domain matching and terms pages over affiliate comparison pages.

## Global release blockers (unchanged)
- Overall score: NOT SCORED for all 100.
- Review and publication status: HOLD for all 100.
- Consumer testing: NOT PERFORMED for all 100.
- Image source URL: blank for all 100; image-rights status pending for all 100.
- Deposit-method, fees/limits, accessibility, regulatory-actions and ADR source fields: blank for all 100.
- Privacy/cookies URL: populated for 9/100 only.
- Affiliate disclosure: NOT REVIEWED for all 100; evidence bundle paths: 0.
- CI is unconfirmed in the available PR-triggered workflow lookup. No merge or Cloudflare Pages deployment is claimed.
