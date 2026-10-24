# Target-100 release-gate audit — canonical public-directory ledger — 24 October 2026

## Scope and method
Read-only structural audit of `docs/targets/100-brand-review-production-ledger-2026-10-24.csv` on branch `ops/2026-10-24-target-reconciliation-and-release-gates`. The CSV was parsed with quote-aware handling and checked for row widths, slot uniqueness, brand/market uniqueness, and release-gate fields. The ledger is an internal research tracker, not a consumer-ready review catalogue.

## Current structural result
- Data rows: **100**; columns: **43**; every row has 43 fields; duplicate slot IDs: **0**; duplicate brand/market pairs: **0**.
- Official consumer-facing domain URL: **60/100** populated; 40 blank. Slot 33 (BetAhoy) now matches the active domain record for Bet Ahoy Ltd / account 100094. Slot 28 (Kansino) now has its official consumer domain, but its licence reference differs across current official pages and remains on HOLD pending Ksa reconciliation. Slot 23 (Imperial Treasures) now has the PGCB-linked consumer domain. Slots 7 (888.nl) and 13 (Stakemate) remain unresolved; the exact domain/operator/product match still needs regulator verification for several other rows. Do not infer a valid operator domain for blank rows.
- Official register URL: **100/100** populated; this counts URL presence only and does not establish that every URL matches the exact brand, product, contracting entity or territory.
- Terms URL: **20/100**.
- Bonus/promotion URL: **15/100**. All populated promotion links remain source leads unless individually cleared against current market-specific terms; no offer is approved for publication.
- Complaints URL: **11/100**; responsible-gambling URL: **21/100**.
- Deposit-method URL: **14/100**; fees/limits URL: **14/100**; withdrawal URL: **13/100**.
- Privacy/cookies URL: **15/100**; accessibility evidence URL: **0/100**.
- Regulatory-action URL: **1/100**; ADR/dispute URL: **1/100**. A regulator complaint process is not private ADR unless the source explicitly establishes that.
- Image-source URL: **50/100**. For those 50, image rights status remains **PENDING — SOURCE FOUND · RIGHTS PENDING**; the other **50/100** are marked **NOT FOUND — editorial fallback required**. No image is cleared merely because a source URL exists.
- Overall score: **NOT SCORED for 100/100**.
- Review status: **HOLD for 100/100**; publication status: **HOLD for 100/100**.
- Consumer testing: **NOT PERFORMED for 100/100**.
- Affiliate disclosure status: **NOT REVIEWED for 100/100**.
- Primary/secondary reviewer fields and approval dates: **0/100 populated**; evidence bundle path: **0/100**.

## Release decision
**Do not publish or rank these 100 entries as completed reviews.** No entry has a substantiated overall score, independent second-review sign-off, documented consumer testing, cleared image rights, or a complete evidence bundle. Keep the public approved-review count at zero until individual entries pass all applicable gates. Do not manufacture scores, ratings, screenshots, testimonials, payment-test claims, or bonus availability.

## Highest-priority blockers
1. **Domain and legal identity:** 42 entries have no official consumer-facing URL captured. Validate exact domain, contracting entity, product and market against the primary regulator before any score.
2. **Thin terms/payment evidence:** only 19 terms URLs, 13 deposit-method URLs, 13 fees/limits URLs and 12 withdrawal URLs are captured. A regulator URL or operator homepage is not a substitute for detailed payment and contract evidence.
3. **Offer scope:** 15 promotion URLs are present, but no offer has been cleared for publication. Check the full current market-specific terms, product scope, eligibility, opt-in, wagering, max bet, eligible games, expiry and caps. Treat points/credit/rewards separately from cash.
4. **Player protection and privacy:** complaint URLs exist for 10 entries, responsible-gambling URLs for 20 and privacy/cookies URLs for 14. Fill these from official sources; distinguish regulator escalation from private ADR.
5. **Image rights:** 50 source leads have pending rights; 50 entries have no source. Use only assets with documented licence/permission or a deliberate original editorial fallback.
6. **Independent review and consumer testing:** no reviewer assignments or approval dates are recorded; no hands-on consumer tests were performed. Do not imply that deposits, games, withdrawals, support or account controls were tested.
7. **Regulatory and territory scope:** verify each current exact domain/product and permitted territory. Do not generalise state/province-specific permission to a whole country; do not recommend unlicensed or offshore products as substitutes.
8. **Publisher/compliance:** verify publisher identity and monitored contact route; review privacy/cookie implementation, affiliate disclosures and commercial relationships, target-market requirements and trademark clearance before commercial launch.
9. **Technical QA:** test key pages and tools in desktop/mobile browsers, keyboard and screen-reader paths, broken/internal/external links, image alt text and rights, structured data, metadata uniqueness, HTTP status/redirects, sitemap consistency, security headers and performance.
10. **Release control:** no merge-to-production or Cloudflare deployment is authorised by this audit. Respect the project constraint to wait until the 100-review target and required checks are complete, then perform the planned single deployment only with required approval.

## Source batch 11 — official Swiss and German operator sources (historical batch note; current totals are in the structural result above)
Added official terms, payments, privacy, player-protection and/or support sources for slots 1–6 where available:
- ADMIRAL.ch (CH): operator terms, payments and responsible-gambling resources; official Swiss Federal Gaming Board page lists admiral.ch among online casino platforms.
- Casineo.ch (CH): official terms, help/payment/limits and privacy policy; Federal Gaming Board page lists casineo.ch among online casino platforms. Some localized help content contains domain/product wording that needs reconciliation before publication.
- Tipico Casino (DE): operator terms, privacy and safer-gambling sources plus GGL whitelist. The whitelist distinguishes virtual-slot permissions from the Schleswig-Holstein-scoped online-casino offer; do not imply nationwide permission for casino.tipico.de.
- Jollie (DE): terms, privacy, player-protection and support sources plus GGL whitelist. The whitelist lists Aurora Alea A/S / jollie.de for virtual slots; payment methods and a formal complaint/ADR route remain to be sourced.
- Winz (NL): terms, safer-gambling, privacy, payment and operator complaint-procedure sources captured. The complaint route is not independent ADR; the separate cookie policy still needs capture.
- Starcasino (NL): terms, safer-gambling and complaint-disclosure source leads captured. Exact current register entry, separate privacy/cookie and payment pages still need capture.
These are public documentation leads only. No account creation, deposits, gameplay or withdrawals were tested. No score, image-rights clearance or publication approval was added. Batch 12 is documented in `docs/reviews/internal/operator-source-batch-12-2026-10-24.md`.


## Source batch 13 — official operator sources for slots 7–10 (historical snapshot)
- Added `docs/reviews/internal/operator-source-batch-13-2026-10-24.md` and reconciled source fields for GetLucky (NL), Oranje Palace (NL) and Betsuna (GB).
- Slot 7 (888.nl) remains unresolved: this pass did not establish the current operator, exact Ksa/domain match or current terms. A shared GetLucky promo page containing a stray “888” reference was explicitly rejected as identity evidence.
- GetLucky's official homepage states Tulipa Ent Limited and Ksa licence 2165/01.272.549; the operator-published welcome page advertises up to 200 spins across three €20 qualifying deposits for players 24+, subject to opt-in and 1x deposit wagering before withdrawing spin winnings. Captured as a dated source lead only, not cleared for publication.
- Oranje Palace's official terms identify Holland Gaming Technology Ltd and state Ksa licence 1631/01.272.522; payment, limits, complaint and privacy sections were recorded, with a caveat that this single page is not a tested transaction or independent ADR evidence.
- Betsuna's GB homepage and FAQ identify ProgressPlay Limited / UKGC account 39335 and publish payment options, withdrawal processing estimates and minimums. These are operator statements, not observed transactions; current GB terms and formal complaints/ADR sources remain open.
- Re-parsed ledger after update: 100 rows × 43 columns, zero malformed rows; official domains 52/100; terms 15/100; bonus/promotion 10/100; complaints 8/100; responsible-gambling 17/100; deposits 10/100; fees/limits 10/100; withdrawals 9/100; privacy/cookies 9/100; accessibility 0/100; regulatory-action 1/100; ADR 1/100; image sources 50/100.
- All 100 remain NOT SCORED/HOLD. No independent reviewer/date, approval date, evidence bundle or image-rights clearance has been added; consumer testing remains NOT PERFORMED and affiliate disclosure remains NOT REVIEWED. CI remains unconfirmed; no merge or Cloudflare Pages deployment.


## Source batch 14 — official UK and Pennsylvania sources for slots 11–14 (historical snapshot)
- Added `docs/reviews/internal/operator-source-batch-14-2026-10-24.md` and reconciled the canonical ledger for Hollywood Casino Online (PA) and Smooth Spins (GB).
- Hollywood Casino's consumer-facing `hollywoodcasino.com` domain is now captured. Exact contracting entity still needs confirmation against the current Pennsylvania regulator record; existing regulator, cashier-help, complaint-form, privacy and bonus URLs remain leads, not cleared evidence.
- Smooth Spins' official terms, updated 22 October 2026, identify BV Gaming Limited / UKGC account 39576 and document account verification, deposits, withdrawals, safer-gambling tools and a three-step operator complaint process. Operator-published terms are not transaction testing; privacy/cookies and independent ADR still need capture.
- BetTOM (slot 11) and Stakemate (slot 13) remain source-gap holds; no current exact customer domain/terms match was inferred.
- Fresh quote-aware parse: 100 rows × 43 columns, every row width valid, zero duplicate slot IDs and zero duplicate brand/market keys; official domains 49/100; terms 12/100; bonus/promotion 9/100; complaints 7/100; responsible-gambling 14/100; deposits 8/100; fees/limits 8/100; withdrawals 7/100; privacy/cookies 7/100; accessibility 0/100; regulatory-action 1/100; ADR 1/100; image sources 50/100.
- All 100 remain NOT SCORED/HOLD; image-rights pending for 50 source leads and 50 not found; no reviewers/approval dates/evidence bundles; consumer tests NOT PERFORMED and affiliate disclosures NOT REVIEWED. CI remains unconfirmed; no merge or Cloudflare Pages deployment.


## Source batch 15 — UK operator and licence-scope checks for slots 15–18 (historical snapshot)
- Added `docs/reviews/internal/operator-source-batch-15-2026-10-24.md` and reconciled official source leads for AK Bets, Planet Sport Bet, Betmaster UK and 36 Vegas.
- AK Bets is a material product-scope hold: UKGC account 65961 shows active betting ancillary-remote and non-remote licences, but the inspected record does not list a Remote Casino licence and the domain register says no domains are recorded. Casino marketing is not proof of online-casino permission.
- Planet Sport Bet's active trading name is confirmed on the UKGC record for Planet Bet Limited (65109). A search result for a lookalike `planetsportbet-uk.com` showed terms effective after the audit date and was explicitly excluded from current evidence.
- Betmaster UK official terms PDF and privacy page are captured; the exact UKGC record (account 65699) now replaces a generic register URL. 36 Vegas operator page identifies 36Gaming Limited (66806); the public card says “ThreeSix Vegas”, so alias reconciliation remains required. Its offer page is a source lead only and says invited selected accounts only.
- Fresh ledger counts: 100 rows × 43 columns, zero malformed widths and zero duplicate brand/market pairs; official domains 52/100; terms 14/100; bonus/promotion 10/100; complaints 8/100; responsible-gambling 16/100; deposits 9/100; fees/limits 9/100; withdrawals 8/100; privacy/cookies 8/100; accessibility 0/100; regulatory-action 1/100; ADR 1/100; image sources 50/100.
- All 100 remain NOT SCORED/HOLD. Image rights are pending for 50 source leads and 50 are not found; consumer testing NOT PERFORMED 100/100; affiliate disclosures NOT REVIEWED 100/100; reviewer/approval dates and evidence bundles 0/100. CI remains unconfirmed; no merge or Cloudflare Pages deployment.


## Source batch 16 — Michigan operator-policy evidence (historical snapshot)
- Added `docs/reviews/internal/operator-source-batch-16-2026-10-24.md` for Horseshoe Online Casino (MI), with official Michigan terms, payments/withdrawals, responsible-gaming and privacy sources.
- The payment page states a $5 minimum digital deposit and $1 minimum digital withdrawal; methods and availability vary by state/bank, and the terms describe up to 72 hours internal withdrawal processing. These are operator-published statements, not a live transaction test. Exact customer-contracting entity and MGCB operator/platform mapping remain to verify; no bonus or score was cleared.
- Fresh ledger counts: 100 rows × 43 columns, zero malformed widths and zero duplicate brand/market pairs; official domains 52/100; terms 15/100; bonus/promotion 10/100; complaints 8/100; responsible-gambling 17/100; deposits 10/100; fees/limits 10/100; withdrawals 9/100; privacy/cookies 9/100; accessibility 0/100; regulatory-action 1/100; ADR 1/100; image sources 50/100.
- All 100 remain NOT SCORED/HOLD. Image rights pending for 50 source leads and 50 not found; consumer testing NOT PERFORMED 100/100; affiliate disclosure NOT REVIEWED 100/100; reviewer/approval dates and evidence bundles 0/100. CI remains unconfirmed; no merge or Cloudflare Pages deployment.


## Source batch 17 — New Jersey and Pennsylvania (historical snapshot)
- Added `docs/reviews/internal/operator-source-batch-17-2026-10-24.md` and reconciled slots 22–23.
- Betinia NJ terms v1.4 (last updated 2 October 2026) identify Jersix LLC; the official safer-gambling page describes limits, cool-off and state self-exclusion, and the complaints page directs patrons to operator escalation / NJDGE and promotes AskGamblers. Its accessible payments page displayed “No payments found”; no payment methods, fees or limits are inferred.
- Imperial Treasures is linked by the PGCB interactive-gaming operators page. The PGCB certificateholders PDF (13 February 2026) separately notes Wind Creek Bethlehem has no interactive gaming operator while listing FlowPlay and the Imperial Treasures site for slots/table games. Exact current certificateholder/operator/product scope must be confirmed before recommendation.
- BigBangBet UK remains on domain/product verification hold; search results for `bigbangbet.net` are treated as a separate domain and not used to substantiate `bigbangbet.co.uk`.
- Latest canonical ledger parse: 100 rows × 43 columns, all widths valid; zero duplicate slot IDs and zero duplicate brand/market pairs. Official domains 53/100; official-register URL field presence 100/100; terms 17/100; promotion links 14/100; complaints 9/100; responsible-gambling 19/100; deposits 10/100; fees/limits 10/100; withdrawals 9/100; privacy/cookies 10/100; accessibility 0/100; regulatory-action 1/100; ADR 1/100; image sources 50/100.
- All 100 remain NOT SCORED/HOLD. Image rights pending for 50 source leads and 50 not found; consumer testing NOT PERFORMED 100/100; affiliate disclosure NOT REVIEWED 100/100; reviewer fields, approval dates and evidence bundles 0/100. CI remains unconfirmed; no merge or Cloudflare Pages deployment.


## Source batch 18 — Netherlands (historical snapshot)
- Added `docs/reviews/internal/operator-source-batch-18-2026-10-24.md` and reconciled official sources for TOTO (slot 26), Holland Casino Online (slot 27) and Fair Play Casino (slot 29).
- TOTO sources now include its consumer site, participant rules, privacy, complaint procedure, limits and payment/withdrawal help. The help page says deposits use iDEAL/Wero and withdrawals are generally processed within 24 hours, often arriving within an hour; these are operator statements, not transaction tests.
- Holland Casino Online official help sources describe a €10 minimum deposit, current published monthly net-deposit limits and a withdrawal reflection/processing sequence; exact domain/operator match, privacy/cookies and complaint/ADR evidence remain open.
- Fair Play Casino's operator payment page identifies FPO Nederland B.V. and licence 1605/01.247.159 and lists iDEAL/Wero, €0 stated operator fees and instant processing for deposits/withdrawals. These are not tested transactions.
- Latest canonical ledger parse: 100 rows × 43 columns, all widths valid, zero duplicate slots and zero duplicate brand/market pairs. Official domains 55/100; official-register URL presence 100/100; terms 17/100; promotion links 14/100; complaints 9/100; responsible-gambling 19/100; deposits 13/100; fees/limits 13/100; withdrawals 12/100; privacy/cookies 11/100; accessibility 0/100; regulatory-action 1/100; ADR 1/100; image sources 50/100.
- All 100 remain NOT SCORED/HOLD. Image rights pending for 50 source leads and 50 not found; consumer tests NOT PERFORMED 100/100; affiliate disclosure NOT REVIEWED 100/100; reviewer fields, approval dates and evidence bundles 0/100. CI unconfirmed; no merge or Cloudflare Pages deployment.


## Source batch 19 — Netherlands — latest snapshot
- Added `docs/reviews/internal/operator-source-batch-19-2026-10-24.md` and reconciled first-party sources for Bingoal (slot 30), bet365 NL (slot 31) and BetCity (slot 32).
- Bingoal's official terms identify Bingoal Nederland B.V. and Ksa licence 1701/01.247.170, but the captured PDF dates to 31 July 2023, so current-version confirmation is still required.
- bet365's official Dutch terms state licence 3598, while a separate official casino homepage/footer search result states 1690. This licence-number inconsistency is an explicit hold pending current Ksa/domain/product reconciliation.
- BetCity's official site identifies Betent B.V. and Ksa licence 1712/01.247.822 and links to terms, bonus terms, complaints, safer-gambling, privacy and cookies pages. JavaScript prevents complete text extraction in this pass; URLs are leads, not full-text review.
- Latest canonical ledger parse: 100 rows × 43 columns, all widths valid, zero duplicate slot IDs and zero duplicate brand/market pairs. Official domains 58/100; official-register URL field presence 100/100; terms 19/100; promotion links 15/100; complaints 10/100; responsible-gambling 20/100; deposits 13/100; fees/limits 13/100; withdrawals 12/100; privacy/cookies 14/100; accessibility 0/100; regulatory-action 1/100; ADR 1/100; image sources 50/100.
- All 100 remain NOT SCORED/HOLD. Image rights pending for 50 source leads and 50 not found; consumer tests NOT PERFORMED 100/100; affiliate disclosure NOT REVIEWED 100/100; reviewer fields, approval dates and evidence bundles 0/100. CI remains unconfirmed; no merge or Cloudflare Pages deployment.

## Required evidence sequence
1. Reconcile each candidate's exact consumer-facing domain, product type, market and contracting legal entity against the current primary regulator record.
2. Capture current official terms and market-specific promotion terms, including eligibility, opt-in, minimum deposit, wagering, max bet, eligible games, expiry, caps and cash-vs-credit distinctions.
3. Capture official deposit/withdrawal methods, fees/limits/verification, complaints and ADR, safer-gambling/self-exclusion, privacy/cookies, accessibility and regulator-enforcement sources.
4. Record images only where created or sourced with documented permission/licence; do not assume official logos or promotional artwork are reusable.
5. Perform hands-on testing only where lawful and actually completed; record date, method, market, device and limitations.
6. Apply the published scoring rubric only after evidence exists; require an independent second reviewer, editorial approval and affiliate-disclosure review.
7. Add a complete evidence-bundle path and run repository checks before requesting release review.

## CI and deployment status
The available workflow-run lookup returned no PR-triggered runs for the inspected commit. **CI is unconfirmed, not passed.** This work does not merge PR #141, change DNS/indexing, or deploy Cloudflare Pages. The hosting target remains **Cloudflare Pages**, not Vercel.


## Source batch 20 — latest snapshot
- Added `docs/reviews/internal/operator-source-batch-20-2026-10-24.md` with primary-source evidence for Kansino (slot 28), Silkbet (slot 25) and Betty (slot 35).
- Kansino now has its official consumer domain, current terms (version 1.16 effective 19 October 2026), payment/withdrawal, safer-gambling, privacy/cookies and regulator-escalation links recorded. The terms describe iDEAL/Wero via Trustly deposits, Trustly withdrawals, required account limits, a seven-day limit-increase cool-off and CRUKS connection. **Hard hold:** current official Kansino pages state differing licence references/dates; verify against the Ksa register before scoring or publication. Offer remains uncleared; no transaction tested.
- Silkbet's UKGC register entry identifies Silkbet Limited (account 101183) and active remote casino/betting activities from 7 May 2026, but full consumer terms and payment/protection evidence remain uncaptured.
- Betty's official homepage advertises 50 free spins with a £20 minimum first deposit and 48-hour validity, and makes withdrawal-speed claims. These are operator claims, not independently tested; offer-specific terms remain unreviewed.
- Latest canonical ledger parse after this batch: 100 rows × 43 columns; zero duplicate slot IDs and zero duplicate brand/market pairs. Official domains 59/100; official-register URL field presence 100/100; terms 20/100; promotion links 15/100; complaints 11/100; responsible-gambling 21/100; deposits 14/100; fees/limits 14/100; withdrawals 13/100; privacy/cookies 15/100; accessibility 0/100; regulatory-action 1/100; ADR 1/100; image sources 50/100.
- All 100 remain NOT SCORED/HOLD; image rights, independent review, consumer testing, affiliate disclosure and evidence-bundle gates remain open. CI unconfirmed; no merge or Cloudflare Pages deployment.


## Source batch 21 — Great Britain — latest snapshot
- Added `docs/reviews/internal/operator-source-batch-21-2026-10-24.md`. UKGC business, domain and trading-name records match Bet Ahoy Ltd (account 100094), active remote casino licence and active `www.betahoy.co.uk` domain; the canonical ledger now records that exact domain. Consumer terms, cashier, complaint/ADR, RG, privacy, accessibility and offer-specific review remain incomplete.
- UKGC trading-name evidence confirms “brillbet” under UK Digital Bookmakers Ltd (account 101570), but the domain register record was not retrieved; `brillbet.co.uk` remains a lead rather than a confirmed current domain.
- Latest ledger: 100 rows × 43 columns; zero malformed widths or duplicate slot IDs/brand-market pairs. Official domains 60/100; register URL fields 100/100 (presence only); terms 20/100; promotions 15/100; complaints 11/100; responsible-gambling 21/100; deposits 14/100; fees/limits 14/100; withdrawals 13/100; privacy/cookies 15/100; accessibility 0/100; regulatory actions 1/100; ADR 1/100; image sources 50/100.
- All 100 remain NOT SCORED/HOLD. CI unconfirmed; no merge or Cloudflare Pages deployment.
