# BeInCasinos — indexability audit and organic growth plan
**Audit date:** 23 October 2026  
**Scope:** live crawl signals, repository sitemap consistency, publication readiness, and organic-search growth  
**Status:** source-side correction committed to research branch; live deployment and Search Console verification still pending

## Executive summary
This is a technical/source consistency audit, not proof that Google has indexed every URL. The live site was checked across all 46 URLs in the corrected repository sitemap. All 46 returned extracted page content, had a final URL matching the requested URL, and exposed a self-referential canonical; the extractor reported no per-URL errors, redirects, missing canonicals, or visible robots directives in the returned page metadata. The robots file allows crawling and advertises the sitemap. This is a useful crawl/metadata check, but the extraction result does not independently prove HTTP status codes, Google-selected canonicals, or actual indexation.

A concrete mismatch was found: the live sitemap announces 46 URLs, while the repository's `sitemap.xml` on this research branch had 44 entries. The live sitemap contained two URLs missing from the repository version: `/markets/` and `/guides/casino-review-evidence-checklist/`. Both live pages were fetched and expose canonical URLs matching their own URLs. The repository sitemap was updated to include both entries, now 46 URLs. This source correction is committed on the research branch only; it is not live until reviewed and deployed through the approved Cloudflare Pages workflow.

The review directory explicitly states that no casino profiles are currently scored or ranked. Therefore the site does not yet have 100 publishable reviews, and no source-side sitemap change can substitute for complete evidence, legal/market eligibility checks, second review, and publication sign-off. Search Console coverage and index status cannot be confirmed from a public crawl.

## Live observations
- `https://beincasinos.online/robots.txt`: fetched successfully; allows `User-agent: *` and names `https://beincasinos.online/sitemap.xml`.
- `https://beincasinos.online/sitemap.xml`: live page title says “Sitemap (46 URLs)”; extraction returns the site's public URL list.
- `/`: canonical is `https://beincasinos.online/`; title and OG description are present.
- `/reviews/`: canonical is self-referential. Content says the directory is in development and no casino profiles are scored or ranked.
- `/how-we-review/`: canonical is self-referential and methodology includes eligibility gates, scoring criteria, evidence rules and limitations.
- `/markets/`: canonical is self-referential and the page identifies itself as a primary-source directory, not legal advice or a casino ranking.
- `/guides/casino-review-evidence-checklist/`: canonical is self-referential and page provides a practical evidence checklist.
- **Full sitemap URL pass:** 46/46 sitemap URLs returned extracted content; 0 extraction errors; 0 final-URL changes; 0 missing canonical tags; 0 canonical mismatches; 0 visible robots directives in returned metadata. This is an extractor-based check, not a replacement for direct HTTP status/header validation or Google Search Console URL Inspection.
- Metadata extraction did not report a robots meta directive on the sampled pages. Verify raw HTML and HTTP headers in Cloudflare/Google Search Console before treating every route as indexable.

## Change made
- Updated `sitemap.xml` on branch `research/nl-batch-35-toto-renewal-enforcement-2026-10-23` from 44 to 46 `<loc>` entries.
- Added `https://beincasinos.online/markets/`.
- Added `https://beincasinos.online/guides/casino-review-evidence-checklist/` with `lastmod` 2026-10-23.
- Commit: `d34396b701aca8b8652ad890a77acf227c22549d`.
- Commit message uses `[CF-Pages-Skip]`; no Cloudflare Pages build or deployment was intentionally triggered.
- Because this is a research branch, the live sitemap may remain unchanged until the source change is reviewed and deployed. No main-branch merge or production deployment was made.

## Required indexation verification (Search Console + live technical checks)
1. Verify the deployed `/sitemap.xml` has 46 valid URLs and returns HTTP 200; confirm the new entries are included.
2. In Google Search Console, open Sitemaps and inspect the sitemap's last read, discovered URL count, and any parsing errors; resubmit only after the approved deployment.
3. In URL Inspection, test representative pages from the homepage, guides, legal/editorial pages, market directory and every future review template. Record: crawl allowed, fetch result, indexing allowed, user-declared canonical, Google-selected canonical, last crawl, and indexing reason.
4. Check page-level HTTP status and redirect chains for every sitemap URL. Sitemap URLs should be canonical, indexable, return a successful response, and not redirect to a different canonical.
5. Inspect raw HTML/headers for accidental `noindex`, conflicting canonical tags, blocked assets, duplicate titles, empty descriptions, malformed structured data, and soft-404/near-duplicate pages.
6. Validate internal links from relevant hubs to every important guide and every approved review. Avoid orphan pages. Do not create mass thin review pages just to enlarge the sitemap.
7. Add only substantive, publication-approved review URLs to the sitemap after each review passes its evidence, legal, editorial and second-review gates. Remove URLs only when retired or genuinely non-indexable, with suitable redirects where relevant.
8. Keep a dated indexation ledger: URL, intended canonical, HTTP result, sitemap presence, Search Console status, last crawl, issue, owner, and resolution date. Recheck after deployment and at least weekly during rollout.

## Organic search growth plan
### Phase 1 — crawl and trust foundation
- Deploy the sitemap correction only through the approved Cloudflare workflow after review.
- Verify canonical, robots, status, mobile rendering and structured data on all 46 URLs.
- Strengthen About, editorial policy, methodology, affiliate disclosure, contact and responsible-gambling pages with accurate authorship, review dates, sources and clear ownership; avoid unsupported expertise claims.
- Ensure guides link contextually to related guides, the methodology and relevant market pages. Keep navigation and breadcrumbs consistent.

### Phase 2 — first 10 evidence-complete reviews
- Choose markets and brands only where online-casino permission is lawful and the exact local operator/domain is verified. Do not fill quotas with offshore brands in prohibited markets.
- Complete current terms, offer-specific rules, deposits/withdrawals, fees/limits, complaints/ADR, safer-gambling controls, privacy/cookies, accessibility and enforcement checks.
- Require independent second review and legal/editorial sign-off. Publish no placeholder, templated thin page, fabricated rating, or untested first-person claim.
- Each review should have an evidence date, market/product scope, sources, meaningful unique analysis, limitations, methodology, affiliate disclosure, and update process.

### Phase 3 — topic clusters and measured iteration
- Build clusters around licence verification, bonus restrictions, withdrawal delays, complaints/ADR, identity verification, safer gambling and market-specific rules.
- Use Search Console query/page reports to identify real impressions, CTR, ranking position, crawl/index coverage and cannibalisation. Prioritise improvements using observed demand, not invented keyword volume.
- Refresh pages when regulator decisions, operator terms or law changes. Merge overlapping guides when they compete for the same intent.
- Acquire legitimate citations and editorial mentions by publishing useful regulator-linked explainers and transparent methodology; do not buy links or automate spam outreach.

## KPI ladder and expectations
- **Technical:** sitemap valid; no accidental noindex; canonical/status consistency; no orphan approved pages.
- **Indexation:** eligible sitemap URLs discovered, crawled, and indexed, tracked separately; submission is not a guarantee of indexing.
- **Early growth:** impressions and query coverage across the approved guide and review set; CTR and clicks by query/page; indexed review count.
- **Scale:** grow from 10 evidence-complete reviews to 25, 50 and 100 only as independent review capacity and lawful market coverage allow.
- **100 million daily search impressions:** aspirational outcome, not a forecast or guarantee. It would require very large, sustained query demand, broad high-quality coverage, strong authority and actual Search Console evidence. It cannot be promised by adding URLs, submitting a sitemap or publishing 100 pages alone. Treat impressions as a measured outcome, not a delivery commitment.

## Outstanding blockers
- No direct Search Console coverage data was available during this audit; all-indexed status is **unverified**.
- Source sitemap correction is not deployed to production.
- The public review directory says no casino profiles are currently scored or ranked; approved reviews remain 0/100.
- Search demand and competitor gaps still need to be measured with reliable keyword/query data, then prioritised against the team's lawful market and evidence constraints.


## Full sitemap crawl pass (23 October 2026)
The corrected 46-URL repository sitemap was used as the test set against the live site. Results: **46/46 extracted**, **0 fetch errors**, **0 redirects/final-URL changes**, **0 missing canonical tags**, **0 canonical mismatches**, and **0 robots directives exposed in returned metadata**. These results show the sampled public routes are fetchable by the extraction service and canonical consistency looks good; they do **not** prove Google indexed all URLs or that every response was HTTP 200. Search Console and raw response/header verification remain required.


## North-star execution plan — 23 October 2026

A separate phased operating plan now defines the 10-million-daily-impressions ambition as a measured north star, not a forecast: `docs/research/10m-daily-impressions-execution-plan-2026-10-23.md`. It records the known 46-URL crawl-extraction limitation, the absent verified Search Console baseline, staged measurement gates, lawful-market rules, technical/indexation prerequisites, first-10-review quality gates, query-led iteration and weekly scorecard. No deployment or Search Console write is implied by this research update.


## Live follow-up QA — 23 October 2026

Read-only recheck of the live sitemap, robots file, review directory, guide index, markets directory and methodology completed.

- Live sitemap still announces **46 URLs** and includes `/markets/` and `/guides/casino-review-evidence-checklist/`. This confirms the live sitemap now exposes those routes; it does not establish that Google has indexed them.
- `robots.txt` still allows crawling and advertises the sitemap.
- The public review directory correctly states that there are no scored/ranked casino profiles yet and that individual profiles will appear only after market-specific checks.
- **New consistency issue:** the live `/markets/` page heading says “Ten markets”, while the owner-confirmed target geography plan names **12** geographies (AU, CA, GB, US, CH, DE, NL, SE, ES, IT, FR, BE). Align the public page heading and table with the approved scope before representing all 12 as covered. Do not silently count US/Canada sub-jurisdictions as nationwide casino permission.
- Existing guide index already covers licence checks, brand vs legal operator, withdrawal processing/verification, complaints/ADR, bonus rules, RTP/probability, safer gambling, regulatory actions and affiliate transparency. Prioritise improving and interlinking these useful pages rather than creating near-duplicates.
- The extractor reported no errors for the six sampled routes. This is content extraction, not an authoritative HTTP-status/header or Google indexation test.
- Search Console baseline is still not verified in this audit; no impressions-per-day number should be claimed from this pass.

### Corrective actions

1. Update the markets directory's “Ten markets” heading and related explanatory copy only after reconciling the table with the 12-geography approved scope.
2. Verify each market row against its primary regulator and the current legal scope; retain separate provincial/state permissions for Canada/US and do not recommend online casinos in restricted markets.
3. Once a release is authorised, run direct HTTP/status/redirect/header checks and Search Console URL Inspection; record the Google-selected canonical and indexation reason.
4. Export actual 28-day and 90-day Search Console page/query data to establish the baseline before making traffic forecasts.
5. Keep all casino review pages out of public rankings until evidence and independent review gates pass.
