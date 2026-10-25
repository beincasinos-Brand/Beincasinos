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


## Batch 43 — conflicting UKGC identity and product-scope flags (2026-10-25)
- Slot 13 Stakemate now records a material regulator-register discrepancy: the trading name is Inactive under Bet Theory UK Ltd (account 60991) but Active under Bet Theory (Malta) Limited (account 66151). No official URL was guessed; exact GB operator/domain and casino permission remain unresolved.
- Slot 86 PricedUp Casino now records that the UKGC register associates `pricedup.bet` with Off Course Bookmakers Limited (account 1776), but this alone does not establish casino-specific remote product scope. The candidate remains HOLD / NOT SCORED.
- Evidence sources: https://www.gamblingcommission.gov.uk/public-register/business/detail/trading-names/60991 ; https://www.gamblingcommission.gov.uk/public-register/business/detail/trading-names/66151 ; https://www.gamblingcommission.gov.uk/public-register/businesses/results?business-search=Pricedup&uc=true
- These are risk flags, not completed reviews. No tests, merge, workflow or Cloudflare deployment were performed.


## Batch 44 — target-market code validation and publication-state parsing (2026-10-25)
- Added a structural error for market codes outside the 12 target-market codes or the explicit two-letter state/province forms US-XX / CA-XX; this prevents accidental off-target rows such as GH from silently entering the production ledger.
- Hardened publication-state parsing so an approved state followed by an em dash, en dash or hyphen still triggers jurisdiction-specific release gates.
- Added regression tests for an off-target market code and an en-dash publication status. These changes only validate structure; they do not certify legal eligibility.
- Tests have not been executed in this environment. No Actions workflow, PR merge or deployment was triggered.


## Batch 45 — UKGC trading-name status and domain gaps (2026-10-25)
- Slot 59 O'Reels Casino and slot 65 Rose Casino: UKGC record for Jupiter Gaming Limited (account 67098) lists both trading names Inactive. Recorded this as a candidate risk flag; no domains were guessed and both remain HOLD / NOT SCORED.
- Slot 64 BetWright: UKGC record lists the trading name as Active under Onyx Gaming Limited (account 64666), but the source consulted did not establish a canonical casino domain. Active trading-name status alone does not establish the specific domain or remote casino product permission.
- Sources: https://www.gamblingcommission.gov.uk/public-register/business/detail/trading-names/67098 and https://www.gamblingcommission.gov.uk/public-register/business/detail/trading-names/64666
- These are regulator-register reconciliation notes, not consumer reviews. No tests, merge, workflow or Cloudflare deployment were performed.


## Batch 46 — BetWright official domain/register reconciliation (2026-10-25)
- Slot 64 BetWright now has `official_url=https://betwright.com/`, legal entity `Onyx Gaming Limited` (UKGC account 64666), and the direct UKGC domain-register URL. The UKGC domain page lists `betwright.com` as Active; the licence summary lists active Casino Remote permission for account 64666.
- Sources: https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/64666 and https://www.gamblingcommission.gov.uk/public-register/business/detail/64666. The UKGC warns that domain/trading-name data is supplied by businesses and may not be guaranteed accurate: https://www.gamblingcommission.gov.uk/public-register/businesses.
- This resolves one official-domain lead only. Slot 64 remains HOLD / NOT SCORED: terms, withdrawal rules, complaints, responsible-gambling, privacy/cookies, bonus terms, image rights, accessibility, consumer tests, second review and editorial/legal approval remain outstanding. No tests were run; no PR merge, workflow or Cloudflare deployment was triggered.


## Batch 48 — TigerBet official domain and UKGC permission reconciliation (2026-10-25)
- Slot 67 TigerBet now records `official_url=https://www.tigerbet.co.uk/`, legal entity TigerPlay LTD (UKGC account 65319), and direct register evidence. The UKGC domain register lists `www.tigerbet.co.uk` as Active; its licence summary lists Casino Remote as Active from 19 June 2025.
- Sources: https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/65319 and https://www.gamblingcommission.gov.uk/public-register/business/detail/65319. The UKGC notes register domain/trading-name data is supplied by businesses and cannot be guaranteed accurate: https://www.gamblingcommission.gov.uk/public-register/businesses.
- This resolves a domain/operator lead, not the full review. Slot 67 remains HOLD / NOT SCORED pending current terms, withdrawals, complaints, safer-gambling, privacy, bonus terms, image rights, accessibility, consumer tests, independent second review and editorial/legal approval. No tests, merge, workflow or Cloudflare deployment were triggered.


## Batch 49 — Quickbet identity collision check (2026-10-25)
- Slot 57 Quickbet remains unresolved. The current UKGC register contains a legal business named **Quik UK Gaming Limited** (account 57611), but that spelling difference is not enough to map it to the candidate trading name “Quickbet”; no canonical domain or exact trading-name link was established from the evidence consulted. Register search result: https://www.gamblingcommission.gov.uk/public-register/businesses/full/39.
- Do not populate slot 57 with a guessed URL or legal entity based on a similar name. The UKGC register notes that domain/trading-name records are supplied by businesses and may not be guaranteed accurate: https://www.gamblingcommission.gov.uk/public-register/businesses.
- No ledger change made. Slot 57 remains HOLD / NOT SCORED pending exact brand-to-operator/domain evidence and casino-specific remote permission. No tests, merge, workflow or Cloudflare deployment were triggered.


## Batch 50 — Kong Casino white-label domain evidence (2026-10-25)
- Slot 62 now records `official_url=https://www.kongcasino.com/` as a domain identity lead and links the UKGC domain register for Jumpman Gaming Limited (account 39175). The register lists `kongcasino.com` as **White Label**, not Active: https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/39175.
- This status is not evidence that Jumpman is the sole current customer-contracting operator. Verify the live site's legal footer, current terms, and exact white-label arrangement before asserting operator identity or eligibility. Slot 62 remains HOLD / NOT SCORED; all review, evidence, rights, testing and approvals are still outstanding.
- No tests, merge, workflow or Cloudflare deployment were triggered.


## Batch 51 — Fun Casino identity gate (2026-10-25)
- Slot 68 Fun Casino: no authoritative exact-name match that establishes the candidate's canonical domain, contracting operator and GB remote-casino product was corroborated in this pass. The ledger now explicitly records the unresolved identity gate; no domain or operator was guessed.
- Keep the candidate HOLD / NOT SCORED. Do not publish a generic similarly named casino as the same brand. Revisit only with exact trading-name/domain evidence from the UKGC register and the operator's current legal terms.
- No tests, merge, workflow or Cloudflare deployment were triggered.


## Batch 52 — TonyBet Netherlands licence and compliance context (2026-10-25)
- Slot 70 now records `https://tonybet.nl/`, operator TonyBet OÜ, and the Dutch Kansspelautoriteit licensee page. Ksa page lists brand Tonybet, website tonybet.nl and online-gambling licence 1729 valid 15 November 2022 through 14 November 2027: https://kansspelautoriteit.nl/%4013811/tonybet-ou/.
- Compliance context added to the ledger: Ksa warning on prohibited betting markets (12 Aug 2025), marketing incident involving young adults (27 Feb 2026), and role-model advertising violation (17 Jul 2026). Sources: https://kansspelautoriteit.nl/waarschuwing-tonybet-voor-verboden-wedaanbod ; https://kansspelautoriteit.nl/kansspelautoriteit-spreekt-tonybet-kansino-en-betcity-aan-wegens-marketingincidenten ; https://kansspelautoriteit.nl/ksa-spreekt-tonybet-aan-op-overtreding-rolmodellenverbod-tijdens-wk. These are compliance-risk signals, not proof the licence is invalid; current remediation and casino-specific scope must be checked before scoring.
- Slot 70 remains HOLD / NOT SCORED pending consumer evidence, terms, payments/withdrawals, complaints, RG, privacy, current bonuses, image rights, tests and editorial approvals. No tests, merge, workflow or Cloudflare deployment were triggered.


## Batch 53 — Lucky 7 Casino Ksa operator and safer-gambling context (2026-10-25)
- Slot 69 now records Noord Zuid Alliantie B.V. as the operator identified by the Dutch Ksa notice for Lucky 7 Casino, and links that official notice: https://kansspelautoriteit.nl/kansspelautoriteit-spreekt-lucky-7-casino-aan-op-onbereikbaarheid-klantenservice.
- The 27 March 2025 notice says customer-service accessibility and Dutch-language responsible-gambling information issues were addressed after Ksa contact. It also reports signals concerning play after self-exclusion and a prompt encouraging extra deposits; the Ksa said it took those signals seriously. Treat this as dated regulatory context, not a current finding of non-compliance. Current licensee-register entry, canonical domain and remediation status remain to be corroborated; no domain was guessed.
- Slot 69 remains HOLD / NOT SCORED pending exact domain, current register/product scope, terms, payments/withdrawals, complaints, RG, privacy, bonuses, image rights, consumer tests and approvals. No tests, merge, workflow or Cloudflare deployment were triggered.


## Batch 54 — Hommerson Online historical Ksa enforcement / licence gate (2026-10-25)
- Slot 73 records Hommerson Casino B.V. as a historical operator-identity lead only. A Ksa decision dated 14 February 2024 identifies the company in an enforcement matter concerning unlicensed online gambling and says it had applied for an online-gambling licence; this decision does not establish a current licence grant. Source: https://kansspelautoriteit.nl/nieuws/2024/kansspelautoriteit-legt-hommerson-casino-last-onder-dwangsom-aanbieden-illegale-online-kansspelen.
- Current Ksa register and exact brand/domain listing must be checked before any Netherlands-targeted promotion. No canonical domain was guessed. Slot 73 remains HOLD / NOT SCORED; this historical record is not by itself proof of present licensing status.
- No tests, merge, workflow or Cloudflare deployment were triggered.


## Batch 55 — Hard Rock Casino Netherlands exact-register gate (2026-10-25)
- Slot 71 remains unresolved: no exact current Dutch Ksa licensee-register match for the candidate brand/domain was corroborated in this pass. An international brand name is not evidence of permission to offer online casino products in the Netherlands.
- Require the current Ksa register to match the exact legal entity, domain and brand before any Netherlands-targeted recommendation. Official register: https://kansspelautoriteit.nl/register-licensees. No domain or licence was guessed; slot 71 remains HOLD / NOT SCORED.
- No tests, merge, workflow or Cloudflare deployment were triggered.


## Batch 56–57 — Dutch licence and operator-page reconciliation (2026-10-25)
- Slot 69 Lucky 7 Casino: added `https://lucky7casino.nl/` and the Ksa consolidated licensee decision for Noord Zuid Alliantie B.V. Licence stated valid 11 October 2024 through 10 October 2029 for casino games against the operator and sports betting. Operator pages corroborate the legal entity and banking/complaint/privacy content. Ksa's 27 March 2025 notice records customer-service/Dutch-language issues and other signals that the authority says were addressed; represent this as historical context, not a current breach finding. Sources: https://kansspelautoriteit.nl/noord-zuid-alliantie-b-v ; https://kansspelautoriteit.nl/kansspelautoriteit-spreekt-lucky-7-casino-aan-op-onbereikbaarheid-klantenservice ; https://lucky7casino.nl/about-us ; https://lucky7casino.nl/banking ; https://lucky7casino.nl/en/complaint-procedure ; https://lucky7casino.nl/privacy-policy.
- Batch 57 correction: removed two unverified guessed Lucky 7 page paths from the ledger rather than leaving them as evidence. Bonus-terms page is recorded, but current offers remain on HOLD because search results included expired September 2026 promotions; no bonus value should be published without fresh direct verification.
- Slot 73 Hommerson: updated the legal-entity lead to H-Online B.V. based on the Ksa consolidated licence decision. The decision states a licence valid 3 October 2023 through 2 October 2028, but exact current brand/domain mapping still must be confirmed in the Kansspelwijzer. Source: https://kansspelautoriteit.nl/h-online-b-v ; https://kansspelautoriteit.nl/register-licensees.
- Slots 69 and 73 remain HOLD / NOT SCORED. No consumer tests, second reviewer, image-rights clearance or editorial approvals were claimed. No tests, merge, workflow or Cloudflare deployment were triggered.


## Batch 58 — Hard Rock Casino NL candidate / iCasino licence distinction (2026-10-25)
- Corrected slot 71's prior wording: the Ksa does have an official remote-gambling licence decision for iCasino B.V., valid 22 May 2024 through 21 May 2029 for casino games against the operator. This is a potential operator lead only; the decision does not itself name Hard Rock Casino or the domain hardrockcasino.nl. Exact brand/domain mapping still requires the current Kansspelwijzer. Source: https://kansspelautoriteit.nl/icasino-b-v ; https://kansspelautoriteit.nl/register-licensees.
- Slot 71 remains HOLD / NOT SCORED; no license-brand association has been asserted. No tests, merge, workflow or Cloudflare deployment were triggered.


## Batch 59 — Hommerson renamed licence holder and domain gap (2026-10-25)
- Slot 73 now records H-Online B.V. as the current legal name of Hommerson Amusement B.V. Ksa's consolidated decision states the licence is valid 3 October 2023–2 October 2028 for casino games against the operator and sports betting. Ksa's original 2 October 2023 announcement explicitly said the operating domain was not yet known at that time. Exact present brand/domain mapping still requires the current Kansspelwijzer; no URL was guessed. Sources: https://kansspelautoriteit.nl/h-online-b-v ; https://kansspelautoriteit.nl/hommerson-amusement-b-v-nieuwe-koa-vergunninghouder ; https://kansspelautoriteit.nl/register-licensees.

## Batch 60 — Explicit domain identity evidence gate
- Added domain_verification_status, domain_verified_utc, and domain_evidence_url columns to all 100 ledger rows. Every row starts UNVERIFIED because a populated candidate URL is not equivalent to an exact brand/domain/operator match.
- Updated scripts/check_review_ledger.py to require VERIFIED status plus an ISO verification date and HTTPS evidence URL before publication; malformed dates and missing evidence are flagged. Added regression tests for publishable rows with unverified domains and VERIFIED status without date/evidence.
- Updated scripts/test_review_ledger.py fixture rows for the new columns. Tests were not run in this session; no claim of passing CI. No workflow was triggered, no merge and no Cloudflare deployment.


## Batch 61 — Domain verification gate regression coverage (2026-10-25)
- Added two regression cases to scripts/test_review_ledger.py: a malformed verification date must be rejected, and non-HTTPS domain evidence must be rejected. These supplement the existing tests for publishable rows lacking verified domain evidence and VERIFIED status without a date/source.
- Static inspection confirms the new test names and the gate branches are present in the branch files. The test suite has not been executed; no claim of passing tests. No workflow, merge or deployment was triggered.


## Batch 62 — Closed domain-verification state vocabulary (2026-10-25)
- The ledger checker now accepts only UNVERIFIED, VERIFIED, REJECTED, or NEEDS_REVIEW as the canonical domain verification state. Descriptive suffixes after a dash are allowed for explanatory notes, while unknown states fail validation.
- Corrected the delimiter regex after inspecting the saved source. The test addition for unknown states was blocked by the GitHub write interface and was not committed; therefore this behavior is implemented but does not yet have a dedicated regression test. Existing test suite remains unrun.
- No workflow, merge or Cloudflare deployment was triggered.


## Batch 63 — Domain-state and strict-date regression coverage (2026-10-25)
- Added a regression test rejecting unknown domain verification states, and a test rejecting trailing garbage after an otherwise valid ISO date.
- Tightened the checker to parse the entire verification date with date.fromisoformat rather than accepting only a valid-looking first ten characters.
- Existing checks continue to require HTTPS evidence for VERIFIED domain identities and a dated verified domain before publication. No tests were executed in this session, so results remain unverified. No CI workflow, merge or Cloudflare deployment was triggered.


## Batch 64 — Netherlands licence-renewal revalidation queue (2026-10-25)
- Rechecked the current Ksa renewal announcement dated 17 September 2026. It says the first eight continuation permits cover October 2026 through September 2031 and names TOTO Online B.V. (TOTO and Winnitt), Holland Casino N.V. (Holland Casino Online), Play North Limited (Kansino), FPO Nederland B.V. (FairPlay Casino), Bingoal Nederland B.V. (Bingoal), Hillside (New Media Malta) Plc (bet365), NSUS Malta Limited (GG Poker), and Betent B.V. (Betcity).
- Ledger candidates among those named brands include slots 26 TOTO, 27 Holland Casino Online, 28 Kansino, 29 FairPlay Casino, 30 Bingoal, 31 bet365 and 32 Betcity. The announcement supports a company-level renewal lead only; it does not, by itself, verify each row's current domain, exact brand-to-license mapping, offer terms, player experience, or all publication requirements.
- Required next action for each matching row: reconcile the current Ksa licensee/Kansspelwijzer entry to exact legal entity, brand and domain; capture dated register evidence; update domain verification only after exact mapping is confirmed; recheck current terms, complaints, safer-gambling and bonus terms. No row was promoted to VERIFIED, scored or publishable by this batch.
- Official sources: https://kansspelautoriteit.nl/eerste-vervolgvergunningen-voor-online-kansspelen-verleend ; https://kansspelautoriteit.nl/register-licensees ; https://kansspelautoriteit.nl/melden-merk-domein-en-applicatienamen
- No tests were executed; no workflow, merge or Cloudflare deployment was triggered.


## Batch 65 — Regression coverage for four European regulator gates (2026-10-25)
- Added a table-driven regression test covering Belgium, Sweden, Spain and Italy: a row marked PUBLISHED without an exact regulator-register URL must fail the country-specific publication gate.
- This is structural guard coverage only; a URL's presence does not prove the licence or domain is valid. Universal dated HTTPS domain-identity evidence and the complete editorial evidence requirements still apply.
- Tests were not executed in this session. No workflows, merge or Cloudflare deployment were triggered.


## Batch 65 — Dutch continuation-permit evidence leads added to ledger (2026-10-25)
- Updated slots 26–32 with regulator-backed evidence leads for TOTO, Holland Casino Online, Kansino, FairPlay Casino, Bingoal, bet365 and Betcity. Where an individual Ksa company decision page was available, its URL is recorded in the official-register evidence field. For TOTO and FairPlay Casino, only the Ksa's general continuation-permit announcement was found in this pass, so their exact-register URL fields were deliberately left blank rather than mislabelling a general announcement as an individual register entry.
- Ksa's announcement dated 17 September 2026 states these permit renewals run 1 October 2026 through 30 September 2031 and names the relevant permit holders. Individual decision pages for Holland Casino N.V., Play North Limited, Bingoal Nederland B.V., Hillside (New Media Malta) Plc and Betent B.V. confirm the dates and remote-gambling categories.
- These are operator/permit evidence leads, not full brand-domain verification. All seven remain HOLD / NOT SCORED; no domain status was promoted to VERIFIED. Exact domain/app mappings, current terms, bonuses, payments, safer-gambling, complaints, image rights, consumer tests and independent editorial review remain outstanding.
- Sources: https://kansspelautoriteit.nl/eerste-vervolgvergunningen-voor-online-kansspelen-verleend ; https://kansspelautoriteit.nl/holland-casino-n-v ; https://kansspelautoriteit.nl/play-north-ltd ; https://kansspelautoriteit.nl/bingoal-nederland-b-v ; https://kansspelautoriteit.nl/hillside-plc ; https://kansspelautoriteit.nl/betent-b-v
- No tests were executed; no workflow, merge or Cloudflare deployment was triggered.


## Batch 65 — Strict bonus-date validation (2026-10-25)
- The ledger checker now validates the complete `bonus_checked_utc` value rather than accepting any string whose first ten characters look like a date. This prevents malformed trailing content from being accepted as a checked date.
- Added a regression test for a bonus-check date with trailing non-date text. Test suite has not been executed, so the change is recorded but not runtime-verified.
- Source-ledger review confirms the 100 candidate rows still require individual evidence and release review. No brand was promoted to VERIFIED, scored, or published in this batch. No workflow, merge or Cloudflare deployment was triggered.
