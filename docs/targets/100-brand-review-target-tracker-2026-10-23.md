# BeInCasinos — 100-brand / 100-review target tracker

**Last reconciled:** 24 October 2026  
**Working branch:** `ops/2026-10-24-target-reconciliation-and-release-gates`  
**Target:** 100 distinct, jurisdiction-appropriate brands with 100 independently checked, high-quality reviews.  
**Publication approvals:** **0/100**. Do not treat research records or internal drafts as completed reviews.

## Current position

The active research CSV contains **204 market-specific records** across the confirmed target geographies. This is a lead buffer, not 204 verified distinct operators: the registry includes same-brand variants, cross-market entries, state/province-specific records, leads whose casino vertical is not yet proven, and rows that must be excluded or deduplicated. All 204 records remain HOLD or otherwise not approved for publication.

Eighteen internal evidence drafts are tracked: BetMGM Casino (New Jersey), 888casino (GB), Betfred (GB), William Hill Casino (GB), Betway Casino (GB), NorthStar Bets (Ontario), Betano Casino (Ontario), TOTO Casino (Netherlands), Holland Casino Online (Netherlands), Lottomatica (Italy), Luckia (Spain), 888casino (Spain), Betway (Spain), SolCasino (Spain), William Hill Casino (Spain), and Betsson (Sweden), Betway virtual slots (Germany), and LeoVegas virtual slots (Germany). They are not approved consumer reviews. The 100-review target is not met until each review has complete current primary-source evidence, documented consumer-product checks where lawful, a second reviewer, and editorial/legal sign-off.

## Market-by-market lead inventory

Counts below are raw rows whose current registry market-scope text maps to the geography. They are **not** counts of eligible brands. Deduplicate brand + local product + contracting entity, and verify current online-casino permission before promoting a row into the final 100.

Three of the 204 registry records are deliberately not allocated to an active target market in the current scope field: Betsson Casino and NordicBet Casino remain in scope triage until a named local route is evidenced; Rizk has no confirmed market route. In addition, two casino leads are explicitly rejected/excluded: 32Red (GB) because its current UKGC casino permission/domain was not active, and Betfred (ES) because DGOJ records its singular casino-game licences as extinguished on 5 September 2023. None may count toward the 100.

| Target geography | Raw scoped rows | Qualification gate / next work |
|---|---:|---|
| Australia (AU) | 0 | Legal-scope gate: online casino services are generally prohibited. Do not create offshore-casino recommendations to fill a quota. Research lawful explanatory content only if approved. |
| Canada (CA) | 16 | Province/territory-specific. Ontario has 13 directory-mapped records; BC and Québec have separate records. Confirm current local regulator/operator/product and never generalise Ontario permission to Canada. |
| Great Britain (GB) | 23 | Reconcile active UKGC Casino Remote permission to exact domain, customer contract and local product. Remove surrendered/inactive accounts; complete consumer-evidence gates. |
| United States (US) | 45 | State/tribal-specific: 30 New Jersey rows (29 newly added from DGE's approved-site list), 14 Michigan-specific rows and one Pennsylvania lead. This is a candidate buffer, not 45 distinct operators. Verify exact state/tribal site, contracting entity and casino-game authorisation. Details: `docs/research/new-jersey-dge-authorized-casino-candidates-2026-10-23.md`. |
| Switzerland (CH) | 10 | ESBK-listed online-casino platforms; match exact contracting entity, current concession extension and relevant per-game permits. |
| Germany (DE) | 1 | Schleswig-Holstein-specific lead only. Verify current state-specific authorisation and product; do not imply nationwide eligibility. |
| Netherlands (NL) | 8 | Reconcile Ksa licence holder to exact live domain/product. TOTO and Winnitt share TOTO Online B.V.; do not double-count them as distinct operators without materially distinct product evidence. |
| Sweden (SE) | 7 | Svenska Spel has a domain-level licence lookup; Betsson Nordic Ltd has a regulator-confirmed betsson.com/sv licence lead plus a material SEK 6.5m AML sanction (appeal pending). The remaining domain/operator rows need exact current licence-register matching; all remain HOLD. |
| Spain (ES) | 19 | 16 individual DGOJ profiles checked across 18 brand/domain rows. PartyCasino/Bwin share ELECTRAWORKS CEUTA, S.A.; PlatinCasino/Fuegocasino share 8PE ESPAÑA, PLC. Winamax's 2026 roulette/slots/blackjack licences are provisional and need effectiveness confirmation. Betfred.es is excluded because its casino licences were extinguished in 2023. All remaining candidates are HOLD pending consumer evidence and second review. Details: `docs/research/spain-dgoj-candidate-expansion-2026-10-23.md`. |
| Italy (IT) | 46 | ADM candidate buffer. Several entries are broad remote-gambling leads, not proven casino products; confirm active concession, domain and casino vertical. Deduplicate cross-listed brands. |
| France (FR) | 2 | These are sports/poker-related leads, not online-casino authorisations. Online casino is not generally authorised; do not count either toward the casino-review target. |
| Belgium (BE) | 10 | Match each live domain to the current A+ licence table, operator and expiry; verify the casino product and current terms before counting. |

## Mandatory qualification pipeline

1. **Scope:** confirm one of the 12 target geographies; archive everything else.
2. **Legal permission:** current primary regulator source confirms the exact online-casino product in that local jurisdiction.
3. **Identity:** live domain, trading name and contracting entity match the permission.
4. **Current product evidence:** dated terms, bonus conditions, payments/withdrawals, fees/limits, complaints/ADR, safer-gambling tools, privacy/cookies and accessibility.
5. **Risk and enforcement:** current sanctions, suspensions, ownership/domain changes and relevant complaints/consumer risks are recorded with balanced context.
6. **Consumer checks:** reproducible checks are documented where lawful and possible. Never claim an account, payment, withdrawal or support test that did not occur.
7. **Editorial quality:** original, useful, market-specific writing; clear methodology and affiliate disclosure; no copied filler, unsupported “best” claims, fake scores or invented first-hand experience.
8. **Second review:** another reviewer checks the primary sources, calculations, claims, legal framing and all material caveats.
9. **Release approval:** editorial/legal sign-off recorded. Only then may the row be marked `reviewed` / `approved`.

## Review completion ledger

| Measure | Current verified value |
|---|---:|
| Raw market-specific research records | 204 |
| Internal evidence drafts tracked | 18 |
| Publication-approved reviews | 0 |
| Remaining approved reviews to target | 100 |

**Do not manufacture progress:** research records are not approved brands; draft documents are not completed reviews; a regulator directory entry alone is not a consumer review. Where local law does not permit online casino services, leave that geography as a legal-scope gate rather than filling a quota.

## Related records

- Confirmed geography scope: `docs/target-geographies-12-confirmed-2026-10-23.md`
- Active candidate registry: `docs/brand-research-template.csv`
- Out-of-scope archive: `docs/research-excluded-out-of-scope-2026-10-23.csv`
- Swiss / Belgian source memo: `docs/research/switzerland-belgium-regulator-candidates-2026-10-23.md`
- Ontario regulator mapping: `docs/research/ontario-regulated-casino-candidates-2026-10-23.md`
- Current roadmap: `docs/100-verified-brands-10-markets-roadmap-2026-10-22.md`


## Latest work batch — 23 October 2026

- US-NJ: expanded the registry from one to 30 New Jersey-scoped rows using the official DGE Internet Gaming Sites list, which explicitly states that sites absent from the list are not approved. The 29 new records are candidate leads grouped under licensed Atlantic City casino affiliates, not 29 distinct operators; several domains still require exact contracting-entity and casino-vertical checks. All remain HOLD. Memo: `docs/research/new-jersey-dge-authorized-casino-candidates-2026-10-23.md`.

A BetMGM Casino (NJ) evidence draft is now recorded at `docs/reviews/internal/betmgm-casino-nj-evidence-review-2026-10-23.md`. The DGE authorized-site listing was captured, but the operator's public terms/promotions/responsible-gambling routes redirected to a geolocation selector; current NJ-specific consumer terms remain unverified. This draft is HOLD and is not counted as an approved review.


## Ontario evidence update — 23 October 2026
- Added `docs/reviews/internal/betano-casino-ontario-evidence-2026-10-23.md`. iGaming Ontario's operator directory lists Betano under Kaizen Gaming Canada Inc. with casino and sports-betting categories (directory dated 1 September 2026). First-party terms summary, deposit-method guidance, withdrawal-processing estimates and responsible-gaming pages were captured with dates. The evidence distinguishes operator statements from tested outcomes and blocks publication pending complete binding terms, exact current entity/domain match, privacy/cookie review, enforcement search, lawful UX/accessibility checks, authorised image rights, second review and legal/editorial sign-off.
- Betano Ontario remains **HOLD** and is not an approved review. The addition increases internal evidence drafts from 17 to 18; approved reviews remain **0/100**. No Actions workflow or production deployment was triggered.


## Homepage design update — 23 October 2026
- Added a responsive 12-market research showcase to the homepage, with clear market-specific verification notes and separate legal-scope cautions for Australia and France.
- Added responsive three-column / two-column / single-column card layouts, compact regulator-check labels, hover states that respect reduced-motion preferences, and an explicit note that market cards are research scopes—not approved casino recommendations.
- Updated `index.html` and `styles.css` on the existing draft PR branch. Static source verification confirms all 12 market cards and responsive CSS are present. Production deployment, live visual QA, accessibility audit and real-device screenshot checks remain outstanding.
- This is a design/content-navigation improvement, not a review-count increase. Approved reviews remain **0/100**; do not infer that the site is deployed from branch commits.

## Website directory — 100-brand research queue (23 October 2026)

Created `brand-directory/index.html` on this branch with 100 entries sourced from `docs/tier-1-master-prospect-tracker.csv`. The page includes search, market and status filters; each card shows the market scope, known domain/operator (or an explicit not-verified label), and a pending/excluded state. It includes a clear warning that entries are research leads, not recommendations, and a `noindex,follow` directive while legal and editorial gates remain open. Added navigation links from the home page, reviews page and market-research page.

**Important scope note:** the first 100 tracker rows are GB-heavy (64 GB entries) and include four excluded leads plus markets that need additional legal-scope work. This is a working queue display, not the final 100 approved brands. The directory is intentionally not added to the sitemap; do not remove noindex or promote entries until regulator/domain/product verification and editorial approval are complete. No logo/brand imagery is represented as official; the cards use original CSS artwork and monograms. No deployment or GitHub Actions run was triggered.

### Directory content enrichment — 23 October 2026

Updated `brand-directory/index.html` to expand all 100 queue cards with product scope, market, known legal operator (or an explicit unverified label), regulator/authority, official register link, evidence grade, a per-brand next-action checklist, and a primary-source link when a valid URL is recorded in the tracker. Domain links are only rendered as clickable links where the CSV contains a syntactically valid HTTPS URL; otherwise the card says the domain is not verified. Added expandable verification details and matching styles. Source-level verification confirmed 100 cards, 100 expandable checklists, working search/market/status filter hooks, and the noindex directive.

**Imagery:** the directory uses original CSS-generated decorative art and initials, not third-party logos or stock images; official logos are not claimed. To replace those placeholders responsibly, each brand asset must be sourced from and checked against the official brand site, with permissions/usage terms considered. The page remains noindex and all entries remain research leads; this is not 100 approved reviews. No Cloudflare deploy or GitHub Actions run was triggered.


## Follow-on work added — 23 October 2026

- Added `docs/reviews/100-brand-review-production-standard.md`: required review structure, minimum primary-source evidence, jurisdiction controls, affiliate disclosure, image provenance and independent sign-off gates.
- Added `docs/targets/brand-image-asset-register-2026-10-23.csv`: 100 directory entries with image source, permission/licence, alt-text and check-date fields. Image URLs and rights are deliberately blank until verified; do not substitute invented logo URLs or unlicensed images. The current directory artwork is decorative CSS, not official brand imagery.
- These are production controls, not 100 completed reviews. Publication approvals remain 0/100 until each brand independently clears the evidence and sign-off gates.


### Directory follow-up — evidence filter and sourced image candidates

- Added an evidence-grade filter (A/B/C/unassigned) to the 100-card directory; every card now carries a machine-readable grade so users can narrow the research queue without implying approval.
- Located 11 brand-image assets on official brand websites and rendered them on their matching cards: admiral.ch, casineo.ch, jollie.de, Betsuna, Vegas Club Casino, Betinia Casino, Casushi, FruitKings, Betcrown, BetLegend and BetNero.
- All 11 image records remain **rights pending** in `docs/targets/brand-image-asset-register-2026-10-23.csv`. Official-site hosting is not proof of permission to republish; confirm rights/terms and visual rendering before production.
- The directory still has `noindex,follow`, is excluded from the sitemap, and remains a research queue. No production deployment or GitHub Actions run was initiated.


### Further directory enrichment — 23 October 2026

- Expanded official-site image candidates from 11 to **20**; all remain rights-pending and are tracked individually. No claim of image reuse permission is made.
- Added a collapsible, brand-specific research context/evidence-limits note to **all 100 cards**, sourced from the existing prospect tracker, including the tracker’s last-checked date with an explicit caveat that it does not mean every term/licence was rechecked on that date.
- Added the evidence-grade filter and machine-readable grade to all 100 cards. The page remains noindex and excluded from the sitemap until legal/operator/product checks and editorial approvals are complete.


### Image resilience and rights-label QA — 23 October 2026

- Added image-load fallback monograms for all 20 externally hosted image candidates, so a broken/blocked logo URL degrades gracefully rather than leaving an empty image area.
- Changed the visible image ribbon to **SOURCE FOUND · RIGHTS PENDING** on all 20 candidates. This explicitly avoids implying permission to republish.
- Final source-level checks: 100 brand cards; 100 brand-specific research-context panels; 100 evidence-grade attributes and an active evidence filter; 20 sourced image tags with 20 fallbacks and rights-pending labels; 100 image manifest rows. The page remains noindex and has not been deployed to Cloudflare.


### Directory usability and image-source QA — 23 October 2026

- Added a visible **Clear filters** control for search, market, status and evidence grade. It resets all controls together and returns keyboard focus to the search field.
- Added keyboard-visible focus styling and a screen-reader status role to the empty-results message. The result count remains an `aria-live` announcement.
- Corrected the desktop filter toolbar to allocate a dedicated column to the reset control; tablet and mobile breakpoints continue to collapse the toolbar.
- Source-level regression check after the change: **100 cards**, **100 research-context panels**, **100 evidence-grade attributes**, **43 image candidates**, **20 fallback monograms**, and **20 visible rights-pending labels**. Search, market, status, evidence and reset handlers are present.
- Checked the 20 image candidate source pages through a page extractor: **18 candidates appeared in official-page image links or Open Graph metadata**; two page fetches timed out (admiral.ch and Betinia Casino). See `docs/targets/brand-image-source-page-qa-2026-10-23.md`.
- This does not clear image rights. All 20 remain rights-pending; the directory stays `noindex,follow` and excluded from the sitemap. No Cloudflare deployment or GitHub Actions run was triggered.

- Follow-up search improvement: the directory search now matches full card text, including regulator/authority labels, evidence descriptions and brand-specific research-context notes, as well as the original brand/domain/operator index.


### Image candidate correction — 23 October 2026

- Replaced the Jollie social-preview image with the official-site logo asset `https://jollie.de/Assets/Images/jollie-logo-white-1.svg` in both the directory and asset register after checking the Jollie page's image list.
- Added `docs/targets/official-image-candidate-qa-2026-10-23.md` documenting the spot-check results, the two timeouts, and the limits of this check.
- Image reuse permissions are still pending for all 20 candidates. Source presence is not a licence check. The directory remains `noindex,follow`; no Cloudflare deployment or GitHub Actions run was triggered.


### Latest directory polish — 23 October 2026

- Improved layout stability for the 20 official-site image candidates by reserving a consistent 160×64 contained image slot, adding explicit intrinsic dimension hints, and retaining asynchronous decoding/lazy loading.
- Static QA: 100 brand cards and 100 context panels remain present; all 43 image candidates have alt text, fallback monograms, and visible rights-pending labels. No duplicate HTML IDs were found. This does not change the publication status: the directory remains `noindex,follow`, the PR is unmerged, and no Cloudflare production deployment is confirmed.

- Final HTML source check after the image-layout patch: 100 unique brand labels; 100/100 cards contain legal-operator field, regulator/authority, evidence grade, checklist and research-context panel; 20/20 candidate image tags have dimension hints and alt text; no malformed image attributes or unsafe `target=_blank` links detected. This remains source-level QA, not a live-browser test or Cloudflare deployment.


### Brand-list integrity correction — 23 October 2026

- Replaced the France and Australia category placeholders (not actual brands) with Silkbet and BigBangBet, using the official UKGC register/domain evidence already recorded in the master prospect tracker. Both remain HOLD: live consumer-product status, current terms, withdrawals, complaints, safer-gambling controls and enforcement history still require review.
- Added a visible market-scope guardrail stating France and Australia are excluded from this online-casino directory. Current source-level check confirms 100 cards and 100 unique card labels. Page remains noindex and no production deployment is confirmed.

- Image follow-up: Silkbet official homepage exposed an SVG candidate now added to the directory and asset register, marked rights pending. BigBangBet's official homepage fetch returned `invalid_url`, so no speculative image URL was added. Current total is 43 sourced image candidates; image rights remain unconfirmed.


## Directory image inventory reconciliation — 23 October 2026

After adding Silkbet's SVG and Ember Casino's official-site image candidates, the branch contains **43/100 cards with sourced image candidates** in `brand-directory/index.html` and the 100-row asset register. All 43 are marked rights pending and retain fallback monograms. The remaining 57 cards use CSS-generated decorative artwork, not official brand logos/photos. The image QA note distinguishes the original 20-candidate spot-check from the current 43-candidate inventory. This does not change publication approvals: **0/100 approved reviews**, and the directory remains `noindex,follow` pending evidence, legal-scope, image-rights and editorial gates.


## Brand-list qualification correction — 23 October 2026

The excluded planned Maine entry `Caesars online casino brands` was replaced by `Horseshoe Online Casino (Michigan)`. The Michigan Gaming Control Board's authorized-platform list identifies Caesars/Horseshoe and the casino-games URL `https://horseshoeonlinecasino.com/us/mi/casino`. This entry is Michigan-specific and remains HOLD pending exact customer-contracting entity, current terms, withdrawals, complaints, safer-gambling controls and enforcement review. No consumer testing or positive review is claimed. The asset register has been updated; no official Horseshoe image was sourced, so the card retains original CSS artwork.


### Official-site image follow-up — 23 October 2026

Added three image candidates to the directory and asset register: ThreeSix Vegas (source `36vegascasinos.uk`; verify its relationship to the listed `36vegas.co.uk` domain), Midnite (official `logo-emblem-2025.svg`), and Winz.nl (official homepage favicon, small-icon candidate only). All three are marked rights pending. Historical snapshot at that stage: 25/100 candidate assets and 75 cards using editorial CSS artwork/monograms; superseded by the latest 43/100 count. This is not rights clearance or production-deployment confirmation.


### Latest image follow-up — 23 October 2026

Brillbet's official page exposed `https://brillbet-co-uk.s3.eu-west-1.amazonaws.com/media/logo.png`; the candidate is added to the directory and register as rights pending. The fetched Brillbet URL redirected to a customer-service notice, so current consumer-product availability is unresolved and the brand remains on HOLD. Historical snapshot at that stage: 41/100 sourced image candidates and 59 CSS-art cards; superseded by the latest 43/100 count. All 100 brand cards retain evidence context and a verification checklist; publication approvals remain 0/100.


### Starcasino image follow-up — 23 October 2026

Added a logo candidate exposed by Starcasino's official casino page and recorded it in the asset register as rights pending. The directory now has 43 sourced image candidates and 57 cards using editorial CSS artwork/monograms. This does not establish logo reuse permission or change the publication status: 0/100 reviews approved.


### Additional official-site image candidates — 23 October 2026

Added TOTO's official logo SVG, plus Kansino and Stakewise UK favicon candidates. The latter are small-icon candidates, not full-size logos. All are marked **SOURCE FOUND — RIGHTS PENDING**. Current image inventory is 33/100, with 67 cards still using editorial CSS artwork/monograms. This source check does not establish reuse rights, full image quality, or production deployment.


### Betty Casino image candidate — 23 October 2026

Added the official Betty Casino homepage favicon `https://playbetty.co.uk/favicon/android-icon-192x192.png`. This is a square icon candidate rather than a full-size wordmark and remains rights pending. Historical snapshot at that stage: 34/100 sourced candidates, with 66 cards retaining CSS-generated editorial artwork; superseded by the latest 43/100 count. Source presence is not permission to reuse.


### Final image inventory reconciliation — 23 October 2026

Current checked source state: 100 unique brand cards, 100 visible research snapshots, 100 verification checklists, 43 sourced image candidates and 43 matching rights-pending labels. The remaining 57 cards use CSS-generated editorial artwork/monograms. The asset register retains 100 brand rows. This is static source QA only; image candidates are not reuse-cleared, the page remains `noindex,follow`, and no production deployment is confirmed.


### Latest image sourcing batch — 23 October 2026

Added official-page candidates for VBET Netherlands, Fair Play Casino Netherlands, BetMGM Netherlands, Hard Rock Bet, and Lottoland UK. VBET/BetMGM/Hard Rock Bet provide logo SVG candidates; Fair Play and Lottoland provide favicon candidates only. All candidates remain rights pending. Historical snapshot at that stage: 39/100 image candidates and 61 CSS-art cards; superseded by the latest 43/100 count. This is not a claim that the assets are licensed for republication or that local casino products have been approved.


### Further image candidates — 23 October 2026

Added official-page favicon candidates for Horseshoe Online Casino (Michigan) and BestOdds. These are small icons only, not full-size logo assets; both remain rights pending. Historical snapshot at that stage: 41/100 sourced image candidates and 59 CSS-art cards; superseded by the latest 43/100 count. This does not change the 0/100 approved-review status or the noindex publication gate.









## Authoritative current directory state — 23 October 2026

Latest branch-source audit: **100 unique brand cards, 100 visible research snapshots, 50 sourced image candidates, 50 rights-pending labels and 50 CSS artwork/monogram fallbacks**. The image register has 100 rows, 50 with sourced candidates. All image tags have alt text, dimensions, lazy loading and fallback handling. The official-domain field is populated on 53/100 cards; the legal-operator field is populated on 50/100 cards. These are field-coverage counts, not licensing approvals. Evidence grades: A 44, B 7, C 49; statuses: 99 HOLD, 1 EXCLUDE. Review approval remains 0/100. The page is noindex, PR #36 is open/draft/unmerged and not mergeable, and no Cloudflare production deployment is confirmed. Historical counts above describe earlier batch checkpoints only.


## Reconciliation addendum — 24 October 2026

The preceding counts are the **23 October baseline**, not a live total of distinct, approved reviews. On 24 October, draft PR [#141](https://github.com/beincasinos-Brand/Beincasinos/pull/141) contains 19 additional internal evidence-review draft files across selected Great Britain and Switzerland candidates, plus a primary-source spot-check memo and this release-gate audit. Those drafts may overlap brands already represented in earlier research PRs, and some deliberately remain HOLD because domain-to-entity mapping, consumer evidence, or follow-up on regulatory history is unresolved. Therefore, do not add the 19 to the older 18 as a verified unique count.

**Authoritative publication count remains 0/100.** Neither candidate rows nor internal drafts count toward the goal. PR #141 is a draft and is not merged; no public review pages were changed and no Cloudflare deployment was performed.

The live-site release-gate audit is recorded at `docs/audits/live-site-release-gate-2026-10-24.md`. Its live fetch confirmed that `robots.txt` allows crawling and points to the sitemap, the sitemap currently advertises 46 URLs, and `/reviews/` explicitly states that no casino profiles are currently scored or ranked. These checks do not establish Google indexing, full technical QA, or publication readiness.

Before promoting any candidate, record the exact market, product, live domain, contracting legal entity, current regulator evidence, dated consumer-product checks, enforcement follow-up, image rights, independent second review, and editorial/legal sign-off. If any mandatory field is unresolved, keep the candidate on HOLD and do not score it.


### Additional primary-source delta — 24 October 2026

- **QuinnBet (GB):** UKGC records account 61011, QuinnBet (Gibraltar) Limited, with Casino Remote Active and active domain/trading-name entries. The regulator also records a settlement dated **20 August 2026**, including a public statement and payment in lieu of a financial penalty of **£609,104**, for AML/CTF, remote customer interaction and financial-vulnerability-control failings. Keep on enhanced-risk HOLD; licence status does not negate the enforcement findings. See `docs/research/primary-source-follow-up-ukgc-nj-2026-10-24.md`.
- **Betway (GB):** UKGC account 39372 shows Casino Remote Active, active `betway.com` / `casino.betway.com` domain entries, and no regulatory actions recorded for that business in the checked record. Still HOLD pending exact live contracting-entity match and full consumer evidence; this is not a quality verdict.
- **New Jersey inventory:** the live DGE approved-site page now includes `jackiecasino.playstar.com` and `rwbetnj.com/en/casino` under Ocean Resort Casino. Added as unqualified leads only; neither counts as a distinct eligible brand until exact product/entity mapping, deduplication and consumer review gates pass. See `docs/research/new-jersey-dge-candidate-delta-2026-10-24.md`.

These deltas are research corrections, not newly approved reviews. Keep the authoritative publication count at **0/100** until each candidate has passed all mandatory gates.


### Further UKGC identity reconciliation — 24 October 2026

- **Sky Vegas:** current UKGC records show Bonne Terre Gaming Limited (65519) with Casino Remote Active and active Sky Vegas domains/trading name; Bonne Terre Limited (38718) has its casino licence surrendered effective 31 October 2025 and the related Sky Vegas records inactive. This materially narrows the ambiguity, but the live site's customer contract must still confirm the current contracting entity.
- **Ladbrokes Casino:** account 1611 has Casino Remote Active and active Ladbrokes/Coral trading names but no matching domain in the current search result; account 54743 (LC International Limited) is associated with ladbrokes.com and the Ladbrokes trading name. Do not infer the contracting entity for every product/domain from this overlap.
- **Coral Casino:** the current UKGC search for coral.co.uk maps that domain to LC International Limited (54743), while account 1611 also lists Coral as a trading name. Confirm the live customer contract and product terms before publication.

Detailed official-source URLs and caveats are recorded in `docs/research/primary-source-follow-up-sky-ladbrokes-coral-2026-10-24.md`. All three remain HOLD pending live-contract verification, complete consumer evidence and independent sign-off; these are not newly approved reviews.


### UKGC candidate follow-up — 24 October 2026

- **Midnite (GB):** UKGC search results show Dribble Media Limited (account 42647) and Midnite Limited (account 101839) with overlapping brand/domain signals. Account 101839 shows Casino Remote active and a www.midnite.com domain record, but the live contracting entity and relationship between records remain unresolved. HOLD.
- **Betty Casino (GB):** Betty Gaming (Malta) Limited (account 100695) has an active Casino Remote signal and domain records for betty.com / playbetty.co.uk. A checked actions record showed no actions recorded at that time; this is not a consumer-quality verdict. HOLD pending complete product evidence and independent review.
- **Brillbet (GB):** UK Digital Bookmakers Ltd (account 101570) has an active Casino Remote/trading-name signal, but the live consumer URL previously redirected to a customer-service notice. Current availability and binding terms are unresolved. HOLD.

Evidence memo: `docs/research/ukgc-candidate-follow-up-midnite-betty-brillbet-2026-10-24.md`. UKGC domain/trading-name data is licensee-supplied and must be cross-checked against the live contract. This batch adds **0 approved reviews**; the authoritative publication count remains **0/100**.


### Betway historical-enforcement correction — 24 October 2026

The current UKGC actions page for Betway Limited (account 39372) states no actions are recorded on that page today, but the Commission's own announcement dated 21 September 2022 records a £408,915 penalty for gambling advertising appearing on children's pages of West Ham United FC's website. Because UKGC sanctions remain on the public register for three years from publication, an empty current actions page must not be represented as no historical action. Record the dated historical action alongside the current active licence/domain signal and the current-page result. Full note: `docs/research/ukgc-historical-enforcement-betway-2026-10-24.md`. Betway remains HOLD; this adds **0 approved reviews**.


### Belgium A+ register batch — 24 October 2026

Checked the Belgian Gaming Commission's official A+ register (table page displayed last-updated 8 October 2026): https://data.gamingcommission.be/licenses/APLUS/latest/table.html?lang=en. Added one batch memo and five internal market-specific draft files for Casino777.be, Napoleon Casino, StarCasino.be, Betano Casino and Circus Casino. The source records domain/operator/dossier/expiry associations; it does not prove current terms, consumer quality, payment performance, or publication readiness.

- `docs/research/belgium-aplus-casino-primary-source-batch-2026-10-24.md`
- `docs/reviews/internal/casino777-be-evidence-review-2026-10-24.md`
- `docs/reviews/internal/napoleon-casino-be-evidence-review-2026-10-24.md`
- `docs/reviews/internal/starcasino-be-evidence-review-2026-10-24.md`
- `docs/reviews/internal/betano-casino-be-evidence-review-2026-10-24.md`
- `docs/reviews/internal/circus-casino-be-evidence-review-2026-10-24.md`

Key controls: Betano's listed A+ expiry is 31 December 2026, so current status/renewal must be rechecked before publication. The official register lists Circus Casino and PokerStars.be together under Casino de Namur / SA/NV GAMBLING MANAGEMENT; preserve separate brand/domain records while avoiding a false claim of separate licence holders. Belgian licensees for Unibet, bwin and Ladbrokes must not be conflated with their operators in other markets. All five drafts remain HOLD pending live contract, terms, payments policy, complaints, safer-gambling, privacy, accessibility, enforcement, image rights, independent second review and editorial/legal sign-off.

This batch adds **5 internal drafts, 0 publication-approved reviews**. It does not change the authoritative count of **0/100 approved reviews**, publish any review, or authorize production deployment.


### Belgium A+ register batch — completion addendum, 24 October 2026

Expanded the Belgium A+ register work to cover all nine domain rows in the official table: Casino777, Napoleon Casino, StarCasino, Betano, Circus, PokerStars.be, Ladbrokes Casino, Unibet Casino and bwin Casino. Four additional internal drafts were added for PokerStars.be, Ladbrokes Casino, Unibet Casino and bwin Casino, and the research memo was extended. Source: https://data.gamingcommission.be/licenses/APLUS/latest/table.html?lang=en

- **9 Belgium-specific internal drafts/records are represented; 0 approved reviews.**
- Circus and PokerStars.be share one listed A+ dossier/operator; they are distinct brand/domain entries, not separate licence holders.
- Betano's listed expiry remains 31 December 2026 and must be rechecked after that date.
- Local Belgian licensees must not be confused with the same brands' GB or other-market operators.
- No public pages were changed and no production deployment was performed by this research batch.


### Correction: current Belgium A+ row for Betsson Casino — 24 October 2026

A fresh lookup of the current official A+ register returned dossier 595153 with domain `betssoncasino.be`, establishment Casino Middelkerke x Betsson, operator SA/NV EXPLOITATIE CASINO MIDDELKERKE, listed expiry 22 February 2039. Earlier captured data associated the dossier with `betfirstcasino.be`. This domain/brand transition must be checked against the live site and current customer contract; do not assume the transition or terms are verified. Added `docs/reviews/internal/betsson-casino-be-evidence-review-2026-10-24.md` and corrected the Belgium batch memo.

This corrects the previous batch's claim that all current A+ rows were represented: the earlier nine drafts omitted the Betsson row. There are now **10 Belgium-specific internal draft files** covering the surfaced current A+ row set (nine dossier rows, ten domain strings), with Circus and PokerStars sharing one row. All remain HOLD; approved reviews remain **0/100**.


### Belgium B+ product-scope batch — 24 October 2026

Added eight internal B+ product-scope drafts for Madison Casino, PepperMill, CasinoExperience, Loco Casino, CasinoBelgium, Wellington Casino, Versailles Casino and 711 Casino. Official source: https://data.gamingcommission.be/licenses/BPLUS/latest/table.html?lang=en (table updated 16 October 2026). These are **B+ online gaming-arcade records, not A+ online-casino licences**. Do not add them to the casino-only approved target unless editorial/legal scope explicitly permits B+ arcade products. Wellington and Versailles share the listed operator SA/NV SONIC; PepperMill has multiple B+ establishment/operator records. All eight are HOLD pending live contracts, exact product taxonomy, terms and consumer evidence.

This adds eight internal scope/evidence drafts, **zero approved reviews**. The A+ Belgium register batch and the B+ product-scope queue remain separate to avoid inflating the casino count.


### Ontario official-directory batch — 24 October 2026

Added five Ontario-specific internal evidence drafts from iGaming Ontario's official operator/site directory (which states it was accurate as of 1 September 2026):
- `docs/reviews/internal/bet99-casino-ontario-evidence-review-2026-10-24.md` — 1000007698 Ontario Ltd
- `docs/reviews/internal/casino-days-ontario-evidence-review-2026-10-24.md` — Golden Nebula Limited
- `docs/reviews/internal/spin-casino-ontario-evidence-review-2026-10-24.md` — Cadtree Limited
- `docs/reviews/internal/playojo-ontario-evidence-review-2026-10-24.md` — Skill On Net Ltd
- `docs/reviews/internal/royal-panda-ontario-evidence-review-2026-10-24.md` — TigerGen Limited

Primary sources: https://igamingontario.ca/en/operator/operators and https://www.igamingontario.ca/en/player/regulated-igaming-market. Ontario-only permission; the regulator directory states 19+ and physical presence in Ontario are required to play. These records establish directory association and product category, not tested consumer experience. Cadtree also lists Jackpot City, Royal Vegas and Ruby Fortune; TigerGen also lists LeoVegas, so deduplicate operators and global brands separately. All five remain HOLD pending exact live domain/contract, current terms, payment/withdrawal policy, complaints, safer-gambling, privacy/accessibility, enforcement and independent sign-off. This batch adds **5 internal drafts, 0 approved reviews**.


### Registry reconciliation QA — 24 October 2026

A CSV-level audit of `docs/brand-research-template.csv` now records exact counts in `docs/targets/100-brand-registry-reconciliation-audit-2026-10-24.md`:

- 204 market-specific candidate rows; 204 display names; 154 provisional global brand IDs.
- 200 distinct brand-ID / market pairs after excluding explicit unconfirmed/excluded codes; no duplicate eligible pair found at the key level.
- 202 rows remain HOLD, 2 are rejected, and **0 are approved**.
- `docs/reviews/internal/` contains 165 files of mixed types; 50 match the candidate evidence-review filename pattern. The separate `review-drafts/` folder contains 21 more draft files with overlap possible. These counts are file inventories, not counts of completed reviews.

The previous summary of “18 internal evidence drafts” is a historical snapshot and must not be used as the current file count. Conversely, the larger file inventory must not be described as completed reviews: it includes batch research, scope audits and duplicate drafts. The next blocker is evidence qualification and approval, not raw lead quantity.


### Belgium A+ count correction — 24 October 2026

Re-opened the official A+ register on 24 October and reconciled the current surfaced rows with the existing Betsson draft. The correct current snapshot is **10 consumer-domain/brand records under 9 A+ licence dossiers**, not nine domain records: Casino777, Napoleon, StarCasino, Betano, Circus, PokerStars.be, Ladbrokes, Unibet, bwin and Betsson Casino. Circus and PokerStars.be share dossier 20635 and the same listed operator. Betsson Casino's current surfaced domain is `betssoncasino.be` under dossier 595153, expiry 22 February 2039; older evidence linked this dossier to `betfirstcasino.be`, so the domain/brand transition remains a material HOLD pending live contract confirmation. See `docs/research/belgium-aplus-casino-primary-source-batch-2026-10-24.md` and `docs/reviews/internal/betsson-casino-be-evidence-review-2026-10-24.md`.

Source: Belgian Gaming Commission official A+ table: https://data.gamingcommission.be/licenses/APLUS/latest/table.html?lang=en. All ten records remain internal/HOLD; this correction adds **0 approved reviews**.


### Registry reconciliation update — 24 October 2026

Expanded the existing audit at `docs/targets/100-brand-registry-reconciliation-audit-2026-10-24.md` with the exact market-row breakdown, major repeated global-brand IDs, scope-triage identities, exclusions and the Belgium Betsson domain-transition correction. This consolidates the analysis in the existing target audit rather than maintaining a second copy.

The CSV snapshot remains 204 market rows / 154 provisional global-brand IDs / 202 HOLD / 2 rejected / 0 approved. Counts are a QA snapshot and must be regenerated after further registry changes.
