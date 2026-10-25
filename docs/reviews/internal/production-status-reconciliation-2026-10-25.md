# Production status reconciliation — 2026-10-25

Purpose: record actual internal research artifacts and prevent draft research from being misreported as finished reviews.

## Files created on this branch in the current work session
- Batch 10 verification report and review drafts.
- Batch 11 verification report and editorial checklist.
- Batch 12 Pennsylvania verification report and internal review drafts.
- Batch 13 New Jersey verification report and internal review drafts.
- Batch 14 Ontario verification report and internal review drafts.
- Batch 15 Ontario verification report and internal review drafts.
- Batch 16 Swiss regulator-register candidate list and verification gates (`docs/reviews/internal/batch-16-swiss-register-candidates.md`).
- Batch 17 Australia online-casino market eligibility gate (`docs/compliance/market-gates/australia-online-casino-market-gate-2026-10-25.md`).
- Batch 18 audit of the existing 100-row production ledger (`docs/reviews/internal/big-batch-18-ledger-reconciliation-audit-2026-10-25.md`): 0 scores, 100 publication holds, 100 consumer tests not performed, 76 rows missing at least one core identity/evidence field, and unresolved image rights on all 100 rows.
- Batch 19 GB identity-reconciliation leads for Quickbet, QuinnBet, O'Reels, Stakemate and Fun Casino (`docs/reviews/internal/big-batch-19-gb-identity-reconciliation-leads-2026-10-25.md`). These are explicitly source-quality-labeled leads; no row is cleared or scored.
- Batch 20 Swiss official-platform evidence matrix (`docs/reviews/internal/big-batch-20-switzerland-ten-platform-evidence-matrix-2026-10-25.md`), matching the ten platforms listed by ESBK while keeping all ten review drafts HOLD / NOT SCORED.
- Batch 21 Germany whitelist/product-scope matrix (`docs/reviews/internal/big-batch-21-germany-whitelist-product-scope-matrix-2026-10-25.md`), explicitly distinguishing online slots, poker, sportsbook and state-limited casino permissions.

## Not complete
- Batches 10–15 contain internal verification notes and draft material for 60 brand candidates; these are not 60 finished consumer-facing reviews.
- Batch 16 lists 10 Swiss regulator-register candidates; it is not ten complete reviews.
- Batch 17 is a market-compliance gate, not a brand batch.
- No review scores have been approved; keep scores blank until evidence checks pass.
- Images are not cleared for reuse unless rights are documented.
- Batch 18 measured the ledger snapshot at 100 rows / 43 columns, with no overall scores and every row on publication HOLD. Its audit identifies missing target markets, state-specific US eligibility, image-rights blockers, and identity/evidence gaps. Full row-by-row reconciliation is still outstanding.
- The site has not been merged or deployed as part of this work.

## Release gates
1. Reconcile brand identity, canonical domain, operator and regulator scope.
2. Capture current dated offer terms and cashier/withdrawal rules.
3. Verify safer-gambling tools, complaints/ADR, privacy and cookies.
4. Clear image rights and affiliate disclosures.
5. Complete mobile/accessibility checks and independent editorial review.
6. Update the ledger and only then consider public content.

No deployment requested or performed.

## Batch 22 — Spain DGOJ (2026-10-25)
- Added `docs/reviews/internal/big-batch-22-spain-dgoj-ten-domain-evidence-matrix-2026-10-25.md` with ten .es-domain candidates and regulator/entity/product-scope blockers.
- Added `docs/reviews/internal/big-batch-22-spain-ten-review-drafts-2026-10-25.md` with ten internal review work orders.
- Primary source: DGOJ official licensed-operator finder: https://www.ordenacionjuego.es/en/operadores-juego/operadores-licencia/operadores
- Candidates: 888casino.es, platincasino.es, fuegocasino.es, admiralbet.es, betway.es, casumo.es, codere.es, casino777.es, bet365.es, luckia.es.
- All ten remain HOLD / NOT SCORED. No bonus, withdrawal test, user experience test, image right, or final licence/product-scope determination is claimed. No merge/deploy performed.


## Batch 23 — Sweden (2026-10-25)
- Added `docs/reviews/internal/big-batch-23-sweden-ten-platform-evidence-matrix-2026-10-25.md` and `docs/reviews/internal/big-batch-23-sweden-ten-review-work-orders-2026-10-25.md`.
- Ten candidate domains are listed for exact-domain matching against the current Spelinspektionen register; they are not represented as fully verified licences.
- All ten HOLD / NOT SCORED. No scores, bonus claims, tested withdrawals, image-rights clearance or consumer tests are asserted. No merge/deploy performed.


## Batch 24 — Belgium market gate (2026-10-25)
- Added `docs/compliance/market-gates/belgium-online-casino-market-gate-2026-10-25.md`.
- Belgium-facing casino affiliate pages remain HOLD until the exact domain, operator and casino licence category are verified against the current Belgian Gaming Commission register. Foreign licences alone are not sufficient evidence of Belgian authorisation.
- This is a compliance gate, not a brand-count batch; no unverified names or bonus claims added. No merge/deploy performed.


## Batch 25 — Italy ADM (2026-10-25)
- Added `docs/reviews/internal/big-batch-25-italy-adm-ten-domain-evidence-matrix-2026-10-25.md` and `docs/reviews/internal/big-batch-25-italy-ten-review-work-orders-2026-10-25.md`.
- Ten candidate domains and concessionaire leads were taken from the official ADM remote-gambling concessionaire register; exact current product scope and legal terms still require row-level verification.
- All ten HOLD / NOT SCORED. No bonus claims, withdrawal tests, image rights or consumer tests are asserted. No merge/deploy performed.


## Batch 26 — Netherlands 2026 licence renewal cycle (2026-10-25)
- Added `docs/reviews/internal/big-batch-26-netherlands-2026-licence-renewal-matrix-2026-10-25.md` and `docs/reviews/internal/big-batch-26-netherlands-ten-review-work-orders-2026-10-25.md`.
- Based on the Ksa announcement dated 17 September 2026 naming eight follow-up licence holders for October 2026–September 2031; includes a separate HOLD check for Oranje Palace because omission from that announcement alone does not establish its current status.
- All ten work orders HOLD / NOT SCORED pending exact current domain/product register match and full consumer-review evidence. No merge/deploy performed.


## Batch 27 — Michigan ten-platform matrix (2026-10-25)
- Added `docs/reviews/internal/big-batch-27-michigan-ten-platform-evidence-matrix-2026-10-25.md` and `docs/reviews/internal/big-batch-27-michigan-ten-review-work-orders-2026-10-25.md`.
- Based on the MGCB current legal internet-gaming list and authorised platform provider directory; state-specific URLs and tribal/commercial operator relationships are recorded as leads for review.
- All ten HOLD / NOT SCORED pending current first-party terms, consumer testing, image-rights clearance, safer-gambling/payment evidence and independent review. No merge/deploy performed.


## Batch 28 — Pennsylvania additional ten platform matrix (2026-10-25)
- Added `docs/reviews/internal/big-batch-28-pennsylvania-ten-additional-platform-evidence-matrix-2026-10-25.md` and `docs/reviews/internal/big-batch-28-pennsylvania-ten-additional-review-work-orders-2026-10-25.md`.
- Candidates are drawn from the PGCB official Interactive Gaming Operators page; each exact PA domain/operator/product relationship still requires current row-level and first-party verification.
- All ten HOLD / NOT SCORED pending terms, payment/withdrawal evidence, safer-gambling and complaint checks, image rights, consumer testing and independent review. No merge/deploy performed.
