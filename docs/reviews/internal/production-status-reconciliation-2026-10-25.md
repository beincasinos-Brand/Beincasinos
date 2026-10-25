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


## Batch 29 — New Jersey ten additional platforms (2026-10-25)
- Added `docs/reviews/internal/big-batch-29-new-jersey-ten-additional-platform-evidence-matrix-2026-10-25.md` and `docs/reviews/internal/big-batch-29-new-jersey-ten-additional-review-work-orders-2026-10-25.md`.
- Candidates sourced from the official New Jersey DGE authorised Internet Gaming Sites list. Poker and sportsbook products are explicitly separated from casino evidence.
- All ten HOLD / NOT SCORED pending exact current product/domain terms, consumer checks, image-rights clearance and independent review. No merge/deploy performed.


## Batch 30 — Ontario ten-platform evidence matrix (2026-10-25)
- Added `docs/reviews/internal/big-batch-30-ontario-ten-platform-evidence-matrix-2026-10-25.md` and `docs/reviews/internal/big-batch-30-ontario-ten-review-work-orders-2026-10-25.md`.
- Ontario-specific candidates are leads only until the current iGaming Ontario operator register confirms the exact domain, legal entity and casino product scope. No claim of nationwide Canadian authorisation.
- All ten HOLD / NOT SCORED pending terms, payment/withdrawal evidence, player-protection checks, image rights, consumer testing and independent review. No merge/deploy performed.


## Batch 31 — France online-casino market eligibility (2026-10-25)
- Added `docs/compliance/market-gates/france-online-casino-market-gate-2026-10-25.md` and `docs/reviews/internal/big-batch-31-france-follow-up-work-orders-2026-10-25.md`.
- ANJ and French government guidance say online casino games are not authorised in France; permitted online categories are narrower and separately regulated. The batch therefore blocks France-targeted casino acquisition pages rather than manufacturing a list of purportedly legal casino brands.
- Follow-up work orders cover the France market exclusion, internal release gate, and separate legal review if an authorised product category is considered.
- This does not count as ten completed reviews or add any scored brands. No public pages changed; no merge/deploy performed.


## Batch 32 — 100-row ledger remediation audit (2026-10-25)
- Added `docs/reviews/internal/big-batch-32-ledger-remediation-audit-2026-10-25.md`, generated from the current 100-row CSV snapshot.
- Audit records row/column counts, score/HOLD/consumer-test/image-rights totals, market distribution, missing evidence-field counts and a strict remediation order.
- This is an internal data-quality audit, not a brand verification or finished-review milestone. All publication holds remain in force until evidence, eligibility, rights, testing, independent review and editorial/legal sign-off pass.
- No public pages changed; no merge/deploy performed.


## Batch 33 — 100-brand publication-blocker triage (2026-10-25)
- Added `docs/reviews/internal/big-batch-33-publication-blocker-triage-2026-10-25.md` with live ledger blank-cell counts and a prioritised remediation queue (identity/market eligibility, evidence bundles, rights, real tests, scoring, second review and release gates).
- This is an operational triage document, not a claim that review production is complete. All rows remain HOLD until the per-row acceptance gate is satisfied.
- No public content changed; no merge/deploy performed.


## Batch 34 — premium review template and acceptance QA (2026-10-25)
- Added `docs/reviews/internal/premium-review-production-template-2026-10-25.md` as the canonical content structure, evidence requirements, 100-point scoring rubric, visual/asset policy and release checklist.
- Added `docs/reviews/internal/big-batch-34-review-template-acceptance-qa-2026-10-25.md` with implementation and acceptance tasks for the review UI, market-specific evidence, truthful fallback states, accessibility and release blocking.
- These are internal editorial/QA specifications, not claims that website components are implemented or that any review is cleared. No merge/deploy performed.


## Batch 35 — image-rights remediation policy (2026-10-25)
- Added `docs/reviews/internal/big-batch-35-image-rights-remediation-policy-2026-10-25.md` defining the rights evidence needed for public images, neutral original fallbacks, and proposed future ledger fields.
- No assets were changed or cleared; all unresolved rights remain publication blockers. No merge/deploy performed.


## Batch 36 — Switzerland ESBK ten-platform reconciliation (2026-10-25)
- Added `docs/reviews/internal/big-batch-36-switzerland-esbk-ten-platform-reconciliation-2026-10-25.md` and `docs/reviews/internal/big-batch-36-switzerland-ten-review-work-orders-2026-10-25.md`.
- Reconciled the ten online casino platforms named on the official ESBK page, including the two already present in the ledger (Admiral and Casineo); duplicate rows are explicitly prohibited.
- Official-list evidence is not treated as proof of current bonus terms, payment performance, image rights or completed review scores. All ten work orders remain HOLD / NOT SCORED.
- No public pages changed; no merge/deploy performed.


## Batch 37 — blank-domain identity resolution queue (2026-10-25)
- Added `docs/reviews/internal/big-batch-37-blank-domain-identity-resolution-queue-2026-10-25.md`, enumerating all ledger rows with a blank official domain and a regulator-first resolution procedure.
- No URLs were guessed or written into the ledger. Rows without exact domain/operator/product matches remain HOLD / NOT SCORED.
- No public pages changed; no merge/deploy performed.


## Batch 38 — target-market coverage reconciliation (2026-10-25)
- Added `docs/reviews/internal/big-batch-38-target-market-coverage-reconciliation-2026-10-25.md`, comparing the current 100-row ledger against all 12 requested target markets and identifying missing market codes and jurisdiction pitfalls.
- Explicitly preserves state-level US scope, province-level Ontario scope, France/Australia online-casino exclusions, and national regulator checks for SE/ES/IT/BE.
- This audit does not clear or score brands and does not rebalance the ledger without an approved allocation. No public pages changed; no merge/deploy performed.


## Batch 39 — jurisdiction-specific publication gates (2026-10-25)
- Updated `scripts/check_review_ledger.py` with release blocks for aggregate US and Canada market codes, and for Australia/France online-casino acquisition pending qualified legal review.
- Added structural register-link gates for publishable BE/SE/ES/IT rows and regression tests in `scripts/test_review_ledger.py`.
- These checks do not prove live regulator status; exact domain/operator/product matching still needs human verification. Portfolio remains HOLD / NOT SCORED.
- Added `docs/reviews/internal/big-batch-39-jurisdiction-publication-gates-2026-10-25.md`. Tests were not run in-session; no Actions workflow, merge, or deployment was triggered.


## Batch 40 — regulator-backed US domain resolution (2026-10-25)
- Updated four blank ledger `official_url` fields for slots 75 Monopoly Casino (US-NJ), 76 Horseshoe Casino (US-NJ), 77 Fanatics Casino (US-NJ), and 80 Mohegan PA Casino (US-PA), using domains listed on official state regulator pages.
- Sources: New Jersey DGE Internet Gaming Sites (https://www.njoag.gov/about/divisions-and-offices/division-of-gaming-enforcement-home/internet-gaming-sites/) and Pennsylvania Gaming Control Board Interactive Gaming Operators (https://gamingcontrolboard.pa.gov/interactive-gaming-operators) plus its current authorised-site PDF (updated 2026-02-13).
- Domain matches alone do not complete identity/legal-entity matching or review requirements. All four rows remain HOLD / NOT SCORED; no public pages changed, no Actions workflow, merge, or deployment performed.


## Batch 41 — target-market coverage diagnostics (2026-10-25)
- Updated `scripts/check_review_ledger.py` to compare the 100-row ledger against the current 12 target markets: AU, CA, GB, US, CH, DE, NL, SE, ES, IT, FR and BE.
- US state-specific rows (for example US-NJ/US-PA/US-MI) and Canadian province-specific rows (for example CA-ON) count toward portfolio coverage only; this roll-up does not grant nationwide eligibility or bypass the exact-jurisdiction publication gates.
- Missing market coverage is reported as a warning, not a hard failure, because this is a planning diagnostic and not evidence of legal eligibility. AU and FR remain subject to their separate online-casino market gates.
- Added a regression test confirming the coverage gap appears as a warning rather than a publication approval or gate error.
- Validation has not been run in a repository runner; do not infer test success. No GitHub Actions workflow, PR merge or Cloudflare deploy was triggered.


## Batch 42 — UKGC domain-lead reconciliation (2026-10-25)
- Ledger slot 60, QuinnBet Casino: populated `official_url=https://www.quinnbet.com` from the UK Gambling Commission business-register search result for QuinnBet (Gibraltar) Limited, which lists `m.quinnbet.com` and `www.quinnbet.com`.
- Ledger slot 97, Bet442: populated `official_url=https://bet442.co.uk/` from the UK Gambling Commission business-register search result listing that domain under AG Communications Limited and Betable Limited.
- These are domain-identity leads only, not complete casino product or current-licence clearance. The notes explicitly retain HOLD / NOT SCORED pending product-scope, terms, withdrawals, image rights, consumer testing and editorial approvals.
- Official source: https://www.gamblingcommission.gov.uk/public-register/businesses — register states domain/trading-name data is supplied by businesses and may not be guaranteed accurate; row-level corroboration remains required.
- No tests were run, and no PR merge, workflow or Cloudflare deployment was triggered.
