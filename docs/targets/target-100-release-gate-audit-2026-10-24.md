# Target-100 release-gate audit — reconciled 2026-10-24

## Scope and method
Read-only structural audit of `docs/targets/100-brand-review-production-ledger-2026-10-24.csv` on branch `ops/2026-10-24-target-reconciliation-and-release-gates`. The complete CSV was parsed with quote-aware CSV handling and checked for row width, slot uniqueness and gate-field population. This is an internal research ledger, not a production review catalogue.

## Current structural result
- Data rows: **100**; columns: **43**; every data row has exactly 43 fields; duplicate slot IDs: **0**.
- Official bonus/promotion URL field: **55 populated / 45 blank**. A URL is a research lead, not proof an offer is live, available in the stated market, lawful, or fully understood.
- Image source URL: **0 populated**; image reuse/rights status: **PENDING for 100/100**.
- Overall score: **NOT SCORED for 100/100**.
- Review status: **HOLD for 100/100**; publication status: **HOLD for 100/100**.
- Deposit-method URL: **2/100**; fees/limits URL: **2/100**; withdrawal URL: **2/100**; accessibility evidence URL: **0/100**; regulatory-actions URL: **0/100**; ADR/dispute-resolution URL: **0/100**.
- Privacy/cookies URL: **10/100 populated; 90 blank**.
- Consumer testing: **NOT PERFORMED for 100/100**.
- Affiliate disclosure status: **NOT REVIEWED for 100/100**.
- Evidence bundle path: **0/100**.

## Release decision
**Do not publish or rank these 100 entries as completed reviews.** No entry has a substantiated overall score, independent second-review sign-off, documented consumer testing, cleared image rights, or a complete evidence bundle. Keep the public approved-review count at zero until individual entries pass all applicable gates. Do not manufacture scores, ratings, screenshots, testimonials, payment-test claims, or bonus availability.

## Highest-priority identity and scope risks
1. **Slot 15 — Betano Casino (DE):** current ledger evidence mentions virtual slots, but does not establish a separate online table/live-casino permission. Do not label it a full casino until product and licence scope are proven.
2. **Slot 24 — DraftKings Casino (CA-ON):** exact Ontario customer domain/contracting entity mapping is not yet established from the recorded regulator source.
3. **Slot 25 — Espacejeux (CA-QC):** may overlap the Loto-Québec/lotoquebec.com product rather than represent a distinct current brand; resolve or deduplicate before counting it as a separate verified target.
4. **Slots 5 and 20 — MERKUR Spiel / Tipico Casino (DE-SH):** permission recorded is Schleswig-Holstein-specific; do not imply nationwide German online-casino availability.
5. **Slot 28 — Hollywood Casino (US-PA):** offer-source notes contain conflicting first-time-deposit wording; use the newer official help-centre article only as a lead until the complete Pennsylvania terms are confirmed.
6. **Slot 38 — Fanatics Casino (US-NJ):** public homepage claim is casino credit, not cash; complete in-app eligibility and loss-calculation terms were not captured.
7. **Slot 39 — BetRivers Casino (US-MI):** recorded page describes loyalty/rewards, not a verified welcome bonus or guaranteed cash value.
8. **Slot 95 — Casino Gran Madrid Online (ES):** recorded promotion period ends **2026-10-31**; recheck on/after expiry and do not carry the offer forward automatically.
9. **Slot 93 — Casineo.ch (CH):** a recorded promo code's page did not clearly state the year for its 14 November expiry; confirm the year and eligibility before making a current claim.
10. **Slots 23 — Luckia (ES), and 46 other rows with blank offer URL:** do not infer a welcome bonus from a generic homepage. Research official market-specific promotion and full terms; if unavailable, record NOT FOUND / NEEDS ACCOUNT and retain HOLD.

## Required evidence sequence
1. Reconcile each brand's exact consumer-facing domain, product type, market and contracting legal entity against the current regulator record.
2. Capture current official terms and market-specific promotion terms, including eligibility, opt-in, minimum deposit, wagering, max bet, eligible games, expiry, caps and cash-vs-credit distinctions.
3. Capture official deposit/withdrawal methods, fees/limits/verification, complaints and ADR, safer-gambling/self-exclusion, privacy/cookies, accessibility, and regulator enforcement sources.
4. Record images only where created or sourced with documented permission/licence; do not assume official logos or promotional artwork are reusable.
5. Perform hands-on testing only where lawful and actually completed; record date, method, market, device and limitations. Never imply a deposit/withdrawal test was run if it was not.
6. Apply the published scoring rubric only after evidence exists; require an independent second reviewer, editorial approval, and affiliate-disclosure review.
7. Add a complete evidence-bundle path and run repository checks before requesting release review.

## Source batches recorded
- Payment-source batch 07 added official public payment/withdrawal documentation for Gun Lake Casino / Play Gun Lake (MI) and Hollywood Casino Online (PA), plus a Play Gun Lake responsible-gambling source and Hollywood Casino privacy-policy source. These are documentation leads only; no account or transaction tests were performed. Current field counts: deposit-method 2/100, fees/limits 2/100, withdrawal 15/100, privacy/cookies 10/100.
Internal source notes currently cover batches 01–06, including Great Britain offer leads; Ontario, New Jersey, Michigan and Pennsylvania sources; Italy, Spain, Sweden, Belgium, Netherlands and Switzerland offer leads. Individual batches preserve caveats about stale pages, conflicting terms, rotating promotions, restricted market scope and rewards that are not cash. See `docs/reviews/internal/official-bonus-source-batch-*-2026-10-24.md` for dated detail.

## CI and deployment status
The available workflow-run lookup returned no PR-triggered runs for the inspected documentation commit. **CI is unconfirmed, not passed.** This work does not merge PR #141, change DNS/indexing, or deploy Cloudflare Pages. The project hosting target remains **Cloudflare**, not Vercel.
