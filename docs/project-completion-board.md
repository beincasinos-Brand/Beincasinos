# Current project checkpoint — 24 October 2026

**Working branch:** `feature/directory-global-brand-count-disclosure-2026-10-23`  
**Release:** draft PR #52; not merged. **Cloudflare production deployment is not confirmed.** No GitHub Actions run was triggered during this work.

## First target: 100 distinct eligible brands and 100 publication-ready reviews

| Measure | Current state | What it means |
|---|---:|---|
| Market-specific research records | 204 | Research leads, not verified eligible brands |
| Provisional global-brand IDs | 154 | Still require deduplication and consumer-facing identity checks |
| Distinct-ID review workqueue | 100 | Planning queue only; all entries remain HOLD |
| Directory cards | 100 | 100 distinct displayed titles, not 100 verified eligible global brands |
| Directory status | 98 HOLD / 2 EXCLUDE | No card is approved as a recommendation |
| Internal evidence-draft packages | 62 | Draft evidence packages, not completed consumer reviews |
| Publication-approved reviews | **0/100** | Target remains unmet |
| Image candidates in directory | 63/100 | All candidates remain rights-pending; direct rendering/permission is not cleared |
| CSS-art / monogram fallbacks | 37/100 | Retain until an appropriate asset and reuse basis are verified |

## Latest completed work
- Fixed a CSS cascade defect: the author-level flex rule could override the HTML `hidden` attribute on logo fallbacks, making fallback monograms appear even when an image loaded. Added `.brand-logo-fallback[hidden]{display:none!important}`.
- Added `scripts/check_brand_directory.py`, a dependency-free static source gate for 100 cards, unique titles, 100 asset-register rows, HTML/register image URL matching, alt text, lazy loading, fallback handlers, `noindex,follow`, and sitemap exclusion. The script is committed but has **not been executed in CI or locally**; GitHub Actions remains intentionally unused.

- Corrected the directory release QA snapshot so it accurately records `noindex,follow` and sitemap exclusion; an earlier snapshot had incorrectly said `index,follow` and that the directory was in the sitemap.
- Added official-page image candidates for **LottoGo Casino, Alfobet and Rollerbet** to the directory and asset register. The Los Vegas favicon candidate was removed after a direct 404 response.
- Reconciled the directory HTML and 100-row image register: **100 cards, 100 unique displayed titles, 63 image tags and 63 matching register URLs**, with no HTML/register source mismatches found in the static check. All image tags include alt text, lazy loading and error fallbacks.
- Tested a small batch of official pages and candidate image URLs. Some pages were blocked or geolocated; LottoGo and Alfobet direct asset checks returned no extractable text, and Rollerbet's favicon request returned 403. These are unresolved rendering checks, not rights clearance.
- Updated the image-readiness audit and this target tracker to reflect the current counts.

## Release and quality gates still open

1. Deduplicate the displayed cards against the first-100 distinct-ID queue and confirm the exact consumer-facing brand, legal entity, domain, market and casino product.
2. Verify local authorisation from current primary regulator sources before counting any brand toward the 100 eligible-brand target.
3. Complete terms, payments/withdrawals, complaints/ADR, safer-gambling, privacy, enforcement, accessibility and lawful consumer-check evidence for each review.
4. Obtain a documented reuse basis for every logo/image or use original artwork. Do not treat official-site hosting as image permission.
5. Complete second-review and editorial/legal sign-off. Internal drafts do not count as publication-ready reviews.
6. Run browser/device checks and validate the Cloudflare preview/live response only after release approval. Keep the directory `noindex,follow` and excluded from the sitemap until an explicit release decision.

## Current working records

- [100-brand target tracker](targets/100-brand-review-target-tracker-2026-10-23.md)
- [Brand directory source QA](quality/brand-directory-release-qa-2026-10-24.md)
- [Directory image-readiness audit](targets/directory-image-readiness-audit-2026-10-24.md)
- [100-card research directory](../brand-directory/index.html)
- [First-100 distinct-ID research workqueue](research/first-100-distinct-id-review-workqueue-2026-10-23.md)
- [100-row image asset register](targets/brand-image-asset-register-2026-10-23.csv)

**Bottom line:** visible progress has been made on the directory and image-source coverage, but the first target is not complete. Do not claim 100 verified brands, 100 approved reviews, live deployment, or search indexing.

---

# Latest research and CI checkpoint — 22 October 2026

- PR #26 merged after the complete integrated CI job passed, including Chromium browser smoke tests, the public-only deployment artifact build, and the check that internal research files are excluded from that artifact: https://github.com/beincasinos-Brand/BeInCasinos/pull/26
- Germany register is now tracked internally as 13 site/domain entries, but these are not 13 unique brands and the source evidence is scoped to virtual-slot permissions unless a state-level online-casino concession is separately confirmed. Official GGL whitelist: https://www.gluecksspiel-behoerde.de/de/fuer-spielende/uebersicht-erlaubter-anbieter-whitelist/
- PR #20 merged after the same integrated CI job passed. Its Search Console record documents 32 submitted URLs versus 44 current sitemap URLs, and explicitly treats indexing/performance as unverified: https://github.com/beincasinos-Brand/BeInCasinos/pull/20
- Spain is the next research market: the official DGOJ finder currently displays licensed-operator records and consumer domains. Each candidate still needs matching legal entity, exact domain, general licence and specific game permission checked before it can count as a verified review: https://www.ordenacionjuego.es/en/operadores-juego/operadores-licencia/operadores
- Count discipline remains unchanged: 20 first-stage candidate brands across Switzerland and Great Britain, plus a Germany register with deduplication and product-scope limits; **0/100 fully publication-approved brand reviews**. Candidate registers and HOLD drafts are not publication-ready reviews.
- No production deployment, DNS/nameserver change, billing change, or Search Console write action was made. Keep the single-deploy rule: do not deploy until the 100-brand evidence target and owner/legal/hosting release gates are cleared.

# Live site audit — 22 October 2026

- Added `docs/live-production-seo-and-publication-readiness-audit-2026-10-22.md` from read-only public checks of the homepage, `www` canonicalization, robots, sitemap, reviews directory, guides directory, and a missing route.
- Confirmed the live sitemap currently lists 44 URLs; `www` resolves to the apex host; `/reviews/` explicitly states that no profiles are scored or ranked yet. These observations do not establish Google indexation.
- Follow-up remains owner-gated: verify current sitemap submission in Search Console after release approval, complete legal/privacy/identity/hosting gates, and keep the 100-brand publication count at 0 until each profile is independently verified and second-reviewed.

## ADR guide release — 22 October 2026

- Merged PR #12 (commit `64e4b83a592884da5457082c2d9f25c5319362af`) and the integrated Static site checks passed, including Chromium smoke tests: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39747923664.
- Production guide index links to the new ADR page and live sitemap lists 44 canonical URLs. The clean route intermittently returned 404 in external fetch checks, but a cache-busted URL and `index.html` route returned the page. Clear/recheck the edge cache before calling route delivery fully stable.
- Search Console's last submitted sitemap record remains 32 URLs; resubmit the current 44-URL sitemap in the UI. The available connector is read-only.

## Search Console status — 22 October 2026

- Read-only connector confirms the `https://beincasinos.online/` Search Console property is connected.
- Sitemap last submitted 21 October 2026 at 21:39 UTC; connector reports 32 submitted URLs and 0 errors/warnings. The live sitemap now contains 44 URLs, so resubmission is still needed.
- Search Analytics returned no rows for the last 12 months; do not equate this with a verified zero-impression result. The connector's sitemap `indexed` field is deprecated and must not be used as an index count.
- No URL Inspection or Pages exclusion verdicts have been verified. The connector is read-only; no sitemap submission was made.

## Latest production verification — 22 October 2026

- Merged PR #10 adding the evidence-led gambling-licence guide; integrated static-site CI passed and Cloudflare Pages deployed the merged release.
- Live production fetch confirms `/guides/what-a-gambling-licence-means/` loads with a self-canonical URL and `sitemap.xml` lists 43 URLs including the guide. The `www` host resolves to the apex host.
- Google Search Console URL Inspection, sitemap submission status, indexed URL counts, impressions and clicks remain unverified. A live page and sitemap entry are not evidence of indexing.
- Search Console follow-up steps are recorded in `docs/search-discovery-indexing-verification-2026-10-22.md`.

## Licensing-literacy content release candidate — 22 October 2026

- Added a general educational guide at `/guides/what-a-gambling-licence-means/` explaining licence scope, jurisdiction limits, enforcement records, and what a licence does not guarantee.
- Linked the guide from `/guides/`, added its canonical URL to `sitemap.xml`, and updated `docs/seo-topic-map.csv`.
- Content cites official UK Gambling Commission registers and consumer guidance for the UK-specific examples; it does not claim that any individual operator is licensed or that one licence authorises a product worldwide.
- Source change is on branch `seo/guide-licence-limits-2026-10-22` and is awaiting CI/review through a pull request. Sitemap count in this branch is 43 URLs; repository checks and a sitemap entry do not establish Google indexing.
- No production deployment, DNS change, Search Console action, or live operator endorsement was made.

## Verified withdrawal-content release checkpoint — 22 October 2026

- Added `/guides/documenting-withdrawal-delay/` with a practical evidence timeline, safe handling of personal data, factual support-message template, official complaint escalation steps, and recovery-scam warnings.
- Confirmed the public page resolves with the expected title and description: https://beincasinos.online/guides/documenting-withdrawal-delay/
- Confirmed the public guide index links to the new page and the public sitemap lists 42 URLs, including this guide and the recent withdrawal/bonus/payment-ownership guides: https://beincasinos.online/guides/ and https://beincasinos.online/sitemap.xml
- Latest static checks passed on commit `08e984464e0d8081ca4ae8c6f26e1b31cba7716f`, including Chromium browser smoke tests and the sanitized public artifact step: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39697317267
- Latest read-only Cloudflare diagnostics passed on the same commit: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39697317005
- Public HTTP availability, sitemap presence, and CI success do not establish Google indexing, search ranking, impressions, or Search Console access. Continue to hold operator reviews unless entity/domain/product/jurisdiction and current primary evidence are verified.
- No DNS or nameserver changes were made.

## Latest content and live-route verification — 21 October 2026, 23:58 UTC

- Added `/guides/withdrawal-processing-times/`, an educational guide separating operator review, identity checks, payment dispatch, and bank/wallet settlement. It includes a document checklist, safer handling of sensitive information, and escalation guidance without unsupported operator-specific timing claims.
- Added the guide to `/guides/`, `sitemap.xml`, and `docs/seo-topic-map.csv`. The live sitemap currently reports 39 URLs.
- External live retrieval verified the new guide's HTTP content, canonical URL, title, meta description, Open Graph fields, and sitemap availability: https://beincasinos.online/guides/withdrawal-processing-times/
- Fixed metadata mismatches surfaced by CI. Latest commit `e4fe4dedb1a568388ec646a9ee4016fa864aec74` passed Static site checks, including HTML/local links, paid-listing pipeline schema and regression tests, shared JavaScript syntax, deployment configuration, public artifact leak checks, and Chromium smoke tests: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39696706174. Read-only Cloudflare diagnostics also passed: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39696706181.
- These checks verify repository/build behavior and that the route is publicly retrievable. They do not prove Google indexing, search impressions, rankings, or Search Console submission. Keep brand reviews on hold until current entity/domain/licence/product/jurisdiction evidence is complete.
- No DNS or nameserver changes were made.

## SEO expansion — 21 October 2026

- Added four original educational guides: RTP explained, RTP vs volatility, withdrawal verification, and how to evaluate complaint data. Each includes primary-source reading, caveats, canonical metadata, and related internal links.
- Added the four routes to the sitemap and Guides library; updated the artifact validator to compare sitemap entries with the current indexable HTML route set instead of a hard-coded count.
- Integrated CI passed on commit `9ca6bdb3f8842a444db2ed807eb5181edb855350`, including HTML/link checks, public artifact/sitemap validation and Chromium smoke tests across 28 indexable routes: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39608954109.
- Added `docs/seo-growth-plan-1m-daily-impressions.md` and `docs/seo-topic-map.csv`. The 1,000,000 daily impressions target remains an ambition, not measured performance or a guarantee. Topic ideas are not search-volume claims.
- Search remains intentionally blocked in `robots.txt` until owner, legal, privacy, domain and live-host launch gates are cleared. No Cloudflare project, DNS change, deployment, or Search Console submission has occurred.

## Cloudflare Pages Free preparation — 21 October 2026

- Updated the static allowlist build to copy the source-controlled `cloudflare/_headers` file into `dist/_headers`, preserving the prepared CSP, HSTS, and other security headers for Cloudflare Pages.
- Extended host-configuration and public-artifact checks to validate Cloudflare header rules and ensure `dist/_headers` is included. The existing Vercel config remains as a fallback; no provider account was connected or changed.
- Updated README and hosting runbook to make Cloudflare Pages Free the preferred initial host. A host-aware `www` to apex Redirect Rule and live header/route checks remain deployment-stage tasks.
- Expanded the paid-listing pipeline to 100 research candidates; all remain `hold` / `not_contacted`. These are unqualified research leads, not confirmed operators or willing buyers. No outreach was sent.
- The integrated GitHub Actions workflow passed on commit `9966fd502a40c7bf9daafdf2b29cce6f07daaf3a`, including site checks, pipeline hard gates/regressions, JavaScript syntax, Cloudflare header validation, artifact leak checks, and Chromium browser smoke tests: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39608408703. Later deployment-runbook/README evidence updates are documentation-only and have their own CI runs pending. No Cloudflare project, deployment, DNS change, Search Console submission, or public launch has occurred.

## Latest verified integrated site QA — 21 October 2026, 13:02 UTC

- The latest source commit `d2132ae6cbeb7a8864edea07e3c18e9b1f65c516` passed the complete GitHub Actions Static site checks workflow: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39604429326.
- The verified change expands the public guide `/guides/how-casino-review-sites-make-money/` with a side-by-side explanation of fixed listing fees, CPA, revenue share and hybrid agreements, plus clearly labelled hypothetical arithmetic examples. The copy explicitly avoids presenting examples as market rates, earnings forecasts, or endorsements.
- This is source/build/artifact/browser-smoke verification only. No operator willingness-to-pay, real audience metrics, live-domain state, legal compliance, or production behaviour is established by CI.
- The 47-row commercial pipeline remains `hold` / `not_contacted`; no outreach has been sent. The Vercel team remains on Hobby with no linked project. No deployment, DNS change, indexing, paid-plan purchase, or public-launch approval has occurred.
- Release remains **BLOCKED** pending qualified name/trademark review, legal publisher identity and privacy/market review, owner verification of domain/mailbox access, approval of suitable commercial hosting and billing, and live-host/manual acceptance after an authorised preview.

# BeInCasinos — project completion board

## Latest verified pipeline QA — 21 October 2026, 12:43 UTC

- Tightened the paid-listing prospect validator so every populated row must include a legal-entity field, target market, and traceable HTTPS evidence URL even while it remains at `hold` / `not_contacted`. Added regression coverage for missing identity/evidence and non-HTTPS source URLs.
- The complete GitHub Actions workflow passed on commit `f82eae68ab99fbfd4dbf2f81bc55a02e0517820b`, including pipeline schema/hard-gate validation, regression tests, static-site checks, public-only artifact leak checks, and Chromium browser smoke tests: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39601637466.
- The 47-row sales pipeline still contains 47 unique candidate names, all `hold` / `not_contacted`. These are research leads, not 47 verified operators or confirmed paid-listing buyers. No outreach was sent.
- This automated pass does not clear trademark, legal/privacy, domain/mailbox, commercial hosting, live-host acceptance, or owner launch approval. Public deployment and indexing remain blocked.


## Commercial workflow and automated guardrails — 21 October 2026

- Strengthened `scripts/check_sales_pipeline.py` to require traceable HTTPS source URLs once a prospect reaches an active pipeline stage, validate ISO date fields, and reject reversed contact/placement date ranges. New CI is pending; the prior validator and CI integration both passed: https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39595922848.

- Added `scripts/check_sales_pipeline.py` and wired it into CI. It checks tracker columns, duplicate names, controlled stage/qualification values, required dates/reasons, and blocks `won` unless signed agreement, invoice status, market review, privacy/tracking review and paid-label confirmation are recorded. This is data-integrity automation, not legal or commercial verification.
- Validator CI run: pending at time of this commit; track at https://github.com/beincasinos-Brand/BeInCasinos/actions.

- Added a launch-gated commercial outreach operating standard to `docs/commercial-outreach-pipeline.md`: exact entity/domain/product/market checks, dated evidence requirements, separate proof of willingness to pay, owner approval before contact, model-specific safeguards for fixed fee/CPA/revshare/hybrid, and activation/renewal/removal controls. No outreach was sent or authorised.
- Added source-level checks to keep the public partner page's pre-launch status and commercial-integrity statements visible. The complete static-site workflow passed, including Chromium browser smoke tests, on commit `f2d30d2349e96aa197680f319077fb28555ebed7`: https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39595461346.
- The outreach playbook and README links have since been updated; their CI run is pending. Do not describe those latest documentation changes as verified until their own run passes.
- Release remains blocked: this does not verify the domain/mailbox, clear the brand, approve target markets, purchase hosting, pass live-host QA, or grant owner launch approval.

**Latest integrated verification — 21 October 2026, 11:45 UTC**

- The operator qualification scorecard and linked project documentation passed the complete Static site checks workflow on commit `4f9186924a04d3d33628aead46dfa724a554759b`: https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39594205787. This is repository/source and automated browser validation only; it does not clear any owner, legal, hosting, live-domain, or launch gate.
- The launch evidence register remains explicit: CI/artifact PASS; domain/mailbox UNVERIFIED; name, legal/privacy, hosting, market and commercial gates OPEN/BLOCK; live-host QA and Search Console NOT STARTED; explicit public-launch approval NOT_GRANTED.

**Snapshot:** 21 October 2026 (updated after complaint-guide build changes)  
**Release decision:** BLOCKED — do not deploy publicly or enable indexing.  


## Tier 1 prospect tracker — 21 October 2026

- Added three UKGC-backed GB research leads to the internal master tracker: Silkbet, BigBangBet, and RoyalOl / Speadboom. The rows preserve uncertainty about live consumer-product status and keep commercial signal Unknown, willingness to pay Unconfirmed, and publication status Hold. The full source/build/artifact/Chromium workflow passed for the tracker update: https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39589118702.
- The master tracker now has 103 brand-name research rows plus two market-category restriction rows. This is a research backlog, not 103 qualified buyers; the legacy 100-name list remains a separate document. No outreach was sent.

## Latest public-review methodology update — 21 October 2026

- Published the planned six-category, 100-point scoring weights directly on `/reviews/`, linked the full methodology, and clarified that no casino profiles are currently scored or ranked. Mandatory market/operator/product eligibility remains pass/fail before scoring; missing evidence cannot be converted into invented points.
- Added a source-level CI guard requiring all six weights, the methodology link, and the explicit pre-launch status to remain visible. The page, guard, public artifact checks, and Chromium browser smoke workflow passed: https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39588733763, https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39588775707, and https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39588787474.
- These checks validate source and preview-artifact behaviour only; manual live-host, legal, privacy, and owner launch gates remain open.

**Purpose:** One owner-facing list of work completed, outstanding evidence, and actions that require owner or third-party participation.


## Latest operator research batch — 21 October 2026

- Added a fourth UKGC-backed research batch to [the internal UKGC register audit](ukgc-register-audit-2026-10.md), checking current licence/domain/trading-name records for Silkbet, BigBangBet, and the RoyalOl/Speadboom relationship. Findings deliberately distinguish an active operator permission from a fully reviewed consumer-facing product: Silkbet is still presented as launching; BigBangBet's recorded UK domain is specifically `bigbangbet.co.uk`; and RoyalOl's relationship to a B2B corporate site needs clarification. All three remain Hold, no public profiles are approved, and paid-listing willingness remains unconfirmed. No outreach was sent. Latest research commit: https://github.com/beincasinos-Brand/BeInCasinos/commit/df92068f0c4e944085fb1c65595a276e4e16f8b9.

## Latest verified update — 21 October 2026

- Expanded the public complaint guide with official starting points for Great Britain, Australia, France, Germany, the Netherlands, Switzerland, and state-specific US routes. The page now explains that regulatory reporting is not the same as individual dispute resolution or compensation, and carries a dated source-review notice. The HTML/link/build/artifact/browser workflow passed for the source links and dated notice: https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39585552501, https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39585584042, and https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39585620272. A matching internal source-review log was added. The follow-up launch-acceptance check now requires reviewers to confirm that these market-specific complaint links are current and do not promise refunds; that check also passed CI, including Chromium browser smoke tests: https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39585704495.

- The review-freshness policy, internal scoring rubric alignment, and launch acceptance check have now all passed CI, including Chromium browser smoke tests: https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39585037138, https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39585048308, and https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39585088481. The stated 90-day refresh is a planned operating standard, not evidence of active monitoring; no casino profile should be scored or ranked until the market-specific eligibility gates pass.

- The operator evidence checklist on `/partners/` and the matching internal outreach-playbook guardrails are now verified by successful full CI runs, including Chromium browser smoke tests: https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39583892480 and https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39583930526. The public page explains that commercial intake is not open, lists evidence operators would need to supply in a future process, and explicitly says submissions do not guarantee publication, a positive assessment, or an agreement. The outreach playbook remains research-first; no outreach was sent.

- Added `/guides/how-to-complain-about-a-casino/`, an evidence-first guide covering complaint records, formal operator procedures, official escalation routes, payment disputes, and recovery-scam warning signs. It is linked from the guides hub and added to the sitemap and browser smoke suite. Route inventory is now **23 indexable routes / 24 HTML files including 404**. The first CI runs exposed a social-description mismatch and a sequencing issue while the sitemap update was pending. The description was corrected; the full CI run including Chromium smoke tests then passed on the integrated source commit: https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39583259274. This validates repository checks only, not production hosting or launch approval.

- Updated `docs/release-readiness-audit.md` to reflect the current release gate and link the latest successful pre-launch checklist and completion-board CI runs. The audit refresh passed the full CI workflow, including the Chromium browser-smoke step: https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39582302227. Release remains blocked because legal, domain, hosting, privacy, and live-host checks cannot be resolved by source CI alone.

- Added `docs/operator-prospect-qualification-scorecard.md` and linked it from README. It separates mandatory legal/evidence gates from an internal 0–10 research-priority score and direct-evidence commercial qualification stages. It explicitly states that the 100-name queue is a backlog, not 100 verified prospects or buyers, and that fixed-fee, CPA, revenue-share, hybrid and sponsorship formats remain hypotheses. The full CI workflows passed, including HTML/local-link checks, JS syntax, Vercel config, public-only artifact/leak checks, and Chromium browser smoke tests: https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39581082370 and https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39581090861.
- Refreshed `docs/prelaunch-launch-checklist.md` so its canonical/social metadata and automated-browser-test inventory reflects the current **23 indexable routes** rather than the stale 20-route count. Local CI success is not production-host QA or launch approval. The checklist update passed CI: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39581888259. The completion-board refresh also passed CI: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39581896197.

- Added the public guide `/guides/how-to-compare-casino-review-sites/`, linked it from the homepage, guides hub, and review hub, and added it to the sitemap and browser smoke-test route list. The current expected inventory is **23 indexable routes / 24 HTML files including 404**. The guide explains how readers can compare review publishers without implying BeInCasinos has independently tested or audited its competitors.
- Added the guide's source-backed internal competitor benchmark and updated it with public publisher disclosures/methodology statements. These are publishers' own published claims, not independent audits: Casino.org describes its own review methodology and says it does not accept third-party advertising on its main site; AskGamblers says it charges a listing fee while separating payment from acceptance, review outcome, rating, and placement; Casino.com, Casino Guru, and Gambling.com have their own published methodology/editorial disclosures.
- Updated the internal paid-listing and outreach frameworks to cover fixed-fee, CPA, revenue-share, hybrid, and sponsored-content models as hypotheses. No rates are validated, no partner has agreed to pay, no outreach has been sent, and the public partnerships page does not accept paid placements.
- CI for the latest guide, sitemap, review-hub connection, competitor-disclosure research, and outreach-framework changes passed: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39578043732 (latest outreach commit), https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39578006556 (competitor-disclosure research), and https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39577972909 (guide links). Earlier attempts failed before fixes to the social-description metadata and expected sitemap URL count; those failures were superseded by successful runs.
- These CI results confirm repository/source/build/browser-smoke checks only. They do **not** clear trademark, market-law, privacy, hosting-plan, domain-control, manual accessibility, live-host or launch-approval gates. Public launch and indexing remain blocked.

## Current verified repository state

- Static English-language site source exists, including homepage, guides, market research, safer-gambling information, editorial and commercial disclosure pages, privacy/contact drafts, 404, two learning tools, robots, sitemap, CSS and JavaScript.
- A public-only build script copies an allowlist into `dist/`; internal docs and trackers are intended to remain out of the public artifact.
- A source-level checker and GitHub Actions workflow exist. The latest verified Vercel configuration, public-only build/artifact and Chromium smoke run passed on 21 October 2026: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39576912855. The build was then hardened so public route folders copy only approved browser-facing asset types and reject symlinks/unexpected file types; that stricter build and the independent artifact file-type guard both passed the full CI/browser smoke workflow: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39576912855 and https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39576924300. The follow-up README documentation run also passed: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39576950527. It checked 24 HTML files (including the 404 page), syntax-checked shared JavaScript, built the public-only artifact, verified internal-file exclusion, and ran browser smoke tests over all 23 indexable routes, mobile/desktop overflow, mobile navigation, calculator edge cases, and both tools. The source-level checker reported 0 structural errors and 2 intentional launch warnings because the privacy and Terms of Use pages remain pre-launch drafts. At the time of that older snapshot, the source check reported 9 warnings. On 20 October 2026, seven general guides/safer-gambling pages received a dated editorial source check and their on-page notices now state the review date and limits. The privacy page remains an explicit pre-launch draft; legal/privacy and live QA gates remain open. The internal pricing-hypothesis, UKGC audit, and media-kit evidence documents are planning aids, not launch approval or proof of audience/demand. This is not production hosting, browser rendering, legal compliance or accessibility sign-off.
- `robots.txt` currently blocks all crawlers as a temporary pre-launch measure.
- The sitemap/artifact checker was strengthened on 21 October 2026 to detect duplicate sitemap entries and compare every indexable HTML route in the built public artifact against the canonical sitemap in both directions. The updated GitHub Actions run passed: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39576550572. This guards against future pages silently being omitted from the sitemap or stale sitemap URLs surviving a content change.
- On 21 October 2026, a Terms of Use page was added to the public source, sitemap, and public-only build allowlist; the route is included in browser smoke tests and the deployment artifact URL-count check was raised from 20 to 21. The terms are explicitly a pre-launch draft and require qualified legal review before release. The public privacy page was also rewritten to describe the current repository's data-minimising design accurately: no site account system, contact form, analytics integration, advertising pixel or active affiliate tracking; the two tools are client-side. It also identifies hosting logs, mailbox handling, cookie testing, legal publisher identity and applicable privacy review as unresolved deployment-specific checks. This is a clearer pre-launch notice, **not** a final privacy policy or legal clearance. The privacy page and contact page intentionally remain release warnings until the owner verifies legal identity/contact handling and a qualified review confirms applicable obligations.
- The legacy 100-name queue is a research backlog, not 100 verified brands. The Tier 1 tracker currently has 102 rows including 100 brand-name entries and two category-level market restrictions; one UK lead (Ivy Casino) is excluded after the UKGC register spot-check showed it inactive. On 21 October 2026, 12 additional UK launch leads (Quickbet, Los Vegas, O'Reels Casino, QuinnBet Casino, LottoGo Casino, Kong Casino, BetMaze, BetWright, Rose Casino, MogoBet, TigerBet, and Fun Casino) were added as grade-C secondary-source leads with `Hold` status and `VERIFY` for domain/operator. They expand the research queue only; none is primary-source-qualified, and none has confirmed willingness to pay. A further nine secondary-source market-entry leads were added on 21 October: Lucky 7 Casino, Tonybet, Hard Rock Casino, BetMGM, Hommerson Online, VBET (Netherlands), plus Monopoly Casino, Horseshoe Casino, and Fanatics Casino (New Jersey only). These are `Hold`/grade-C leads with exact domains/operators requiring verification; Dutch/US market entry is not proof of a new global brand or paid-listing demand. Four additional US state-specific launch leads were added: Hollywood Casino (Pennsylvania), Hard Rock Bet (Michigan), Mohegan PA Casino (Pennsylvania), and theScore Bet (New Jersey). State-level permission must never be generalized to nationwide US availability. Six more UK secondary-source leads were added: Proper Bet, Betta Bet, Rollerbet, Conquer Casino, PricedUp Casino, and Rialto. Each remains `Hold` until exact operator/domain and current UKGC status are confirmed. Seven additional UK discovery leads were added to complete a 100-name queue: Spin King, Bet442, Funky Jackpot, London.bet Casino, BetGoodwin Casino, Casino Kings, and Mr Run. The 100-name discovery target is now met at the queue level only; the names are not 100 verified operators or confirmed fee-paying buyers. The 100-row generic research template is a candidate queue, not 100 fully verified operators or 100 willing paid-listing buyers. The tracker is not the final 100-brand qualification list. Seven Dutch regulated-operator prospects were added from the Ksa's 17 September 2026 continuation-licence announcement; those renewals are not evidence of new launches or willingness to buy.
- No brand has confirmed willingness to pay a BeInCasinos listing fee. No outreach was sent in this work.
- An internal [paid-listing offer framework](paid-listing-offer-framework.md) now defines tentative test-price hypotheses, disclosure rules, reporting boundaries, and the readiness gates for any future sales test. Prices are unvalidated hypotheses; no rate card was published and no outreach was sent.
- A dated [UKGC register spot-check audit](ukgc-register-audit-2026-10.md) documents operator permission vs. brand launch/domain proof, including Bet Ahoy, BetLegend, BetTOM, and the inactive Ivy Casino trading-name entry. These remain research leads/holds, not qualified paid buyers.
- An internal [media-kit evidence template](media-kit-evidence-template.md) now requires dated, source-backed audience metrics and explicitly prohibits invented traffic figures; it is a template, not a completed media kit.
- The internal [Morocco privacy/data-protection checklist](privacy-law-09-08-prelaunch-checklist.md) now links to CNDP primary materials, including the 2025 cookie-processing procedure, and lists controller identity, processing notifications/authorisations, transfers, retention, and deployed-cookie checks as legal-review questions. It is not a legal opinion and does not close the privacy gate.

## Gate board

| Gate | Status | Evidence needed to close |
|---|---|---|
| Brand/name risk | BLOCKED | Complete the [name-clearance workpaper](name-clearance-research.md) and obtain a qualified trademark review of “BeInCasinos” / “BEIN” in relevant markets; decision recorded before public branding. |
| Domain control | OWNER ACTION | Owner verifies active registration, renewal, auto-renew and DNS access in Spaceship. No credentials or account screenshots should be shared here. |
| Publisher identity | OWNER ACTION | Legal publisher/business identity and a monitored contact route. |
| Hosting | PROVIDER SELECTED; PLAN BLOCKED | Owner selected Vercel. Connected BeinCasinos team is Hobby with no linked projects. Do not deploy the commercial paid-listing/affiliate business on Hobby; review current Pro price/usage and commercial terms before plan approval. No project, deployment or DNS connection has been created. |
| Market/legal scope | IN PROGRESS | Select initial launch markets and obtain appropriate review of gambling listings, paid placement, affiliate/advertising rules, privacy and consumer protection. AU and FR online-casino promotions must not be treated as ordinary eligible markets. US casino products need state-specific verification. ACMA reports Australian gambling reforms passed on 19 August 2026, with a range of measures expected to commence 1 January 2027; re-check detailed commencement and guidance before any AU activity. |
| Prospect qualification | IN PROGRESS | Expand the master tracker; verify exact domain, legal operator, regulator record, product scope, enforcement history, source dates and commercial contact for every candidate. |
| Paid-listing demand | NOT VALIDATED | Direct operator response, rate-card/media-kit evidence, signed agreement or payment. Launches, affiliate programmes and supplier deals alone are not evidence of willingness to pay. |
| Privacy/contact/disclosures | BLOCKED | Finalise notices to match actual hosting, logs, contact method, analytics, cookies and any tracking; publish real publisher contact and a correction/privacy request process. |
| Source checks | CI PASS, SCOPE LIMITED | Keep CI green after each change. It does not replace manual browser/device, screen-reader, legal, or live-host checks. |
| Live acceptance testing | NOT RUN | Complete the manual test plan against the selected live host and retain evidence for each test. |
| Search indexing | BLOCKED | Only after the owner’s separate launch approval: remove the pre-launch crawl block, verify canonical host/HTTPS, inspect URLs and submit sitemap. |

## Next work sequence

1. Expand and qualify the Tier 1 master tracker; keep unknown evidence blank or explicitly marked `VERIFY`.
2. Reconcile the legacy 100-name queue with the selected markets, excluding unsuitable categories and removing duplicates.
3. Prepare a source-backed, per-brand evidence packet before drafting any public operator profile.
4. Finalise the commercial offer and media kit only after real audience data exists; do not invent traffic, conversion, pricing acceptance or testimonials.
5. Resolve name, identity, domain and hosting gates with the owner.
6. Run source checks, build the public-only artifact, inspect it for internal-file leakage and placeholders, then complete manual production acceptance testing.
7. Launch and enable indexing only after documented approval.

## Do not do without owner approval

- Buy a subscription, start a paid trial, or incur any cost.
- Change nameservers/DNS or email records.
- Deploy the site, expose the internal research files, remove the crawl block, or submit Search Console.
- Send commercial outreach, sign agreements, or represent any brand as a paying partner.
- Publish a legal/licensing claim that has not been verified against the current official register.

## Project references

- [README](../README.md)
- [Tier 1 master prospect tracker](tier-1-master-prospect-tracker.csv)
- [Target-market regulatory matrix](target-market-regulatory-matrix.md)
- [Commercial prospect qualification rubric](commercial-prospect-qualification.md)
- [Commercial outreach pipeline](commercial-outreach-pipeline.md)
- [Hosting decision note](hosting-decision.md)
- [Domain and hosting runbook](domain-and-hosting-setup.md)
- [Pre-launch checklist](prelaunch-launch-checklist.md)
- [Release-readiness audit](release-readiness-audit.md)
- [Manual launch acceptance test plan](launch-acceptance-test-plan.md)

## Latest brand and product work — 20 October 2026

- Owner's positioning is now documented in `docs/brand-identity-and-growth-north-star.md`: premium international casino reviews, BIC monogram, evidence-led editorial voice, and top-10 / 100-million-daily-impressions ambitions treated strictly as aspirations rather than current claims.
- The BIC monogram has been added to the site's primary navigation across public HTML pages and the favicon has been replaced with a matching evergreen/mint mark. Site source changes are committed and the combined source/build/artifact CI passed on run https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39497549965.
- Added `/reviews/` as a review-standard hub, connected it in the primary navigation and sitemap, included it in the public-only build allowlist, and updated the artifact checker to expect 19 sitemap URLs. The hub intentionally does not list unverified casinos as recommendations.
- Homepage positioning now leads with evidence-led casino reviews while keeping educational guides available. No individual casino profile is yet approved for publication; the 100-brand list remains an internal prospect/research queue, not a live verified review database.
- The 100-million daily search-impressions ambition is not a forecast or guarantee. Report only real, dated Search Console metrics after launch.

- Latest combined source/artifact verification passed on GitHub Actions: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39497037760. The check covered 20 HTML pages, built the public-only artifact, and verified the internal-file exclusion and sitemap. This remains source/packaging CI—not real-browser, legal, live-host, accessibility, or launch approval.

- Dated official-source review log added at `docs/editorial-source-review-log-2026-10-20.md`; seven general guides/safer-gambling pages now show a source-check date and retain caveats about current local rules. This is not legal sign-off.
- Added `docs/international-seo-content-architecture.md` with market gates, evidence standards, and SEO guardrails; it explicitly treats top-10 and 100-million daily impressions as ambitions, not forecasts.
- Homepage metadata and positioning now reflect the casino-review and research direction. The public `/reviews/` hub is in navigation and sitemap; individual operator reviews remain unpublished until each passes evidence gates.

- Latest source-check result after the seven editorial notice updates: **20 HTML pages checked, 0 structural errors, 1 warning** (the privacy page is intentionally marked pre-launch draft). See passing run https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39497391660. Artifact build and internal-file exclusion also passed. This is not legal review or live-browser QA.

- Added `docs/editorial-review-scoring-rubric.md` with pass/fail eligibility gates, a weighted 100-point evidence-based rubric, and rules that prohibit paid placement from influencing scores. The public How We Review page now explains the same methodology. This defines a process; it does not mean any casino has been scored or that a top-10 ranking exists yet.

- Public review-scoring methodology passed the source/build/artifact workflow on run https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39497604480. The latest internal profile-template documentation update is still being checked by CI; no deployment or indexing action was performed.
- Added public `/partners/` information page and linked it in the primary navigation across the public HTML pages. It states that paid partnerships are not open yet, discloses that audience data is not established, and prohibits paid influence on editorial scores. The page is included in the public-only build and sitemap; no operator outreach or paid listing sale has occurred.

- The public operator information page `/partners/` is now part of the navigation, public-only build, and sitemap (20 indexable URLs). It explicitly states that paid placements are not yet open and makes no audience-performance claims. Current CI run: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39498716612 (success).

- UK prospect research: ThreeSix Vegas now has an upgraded internal evidence record linking the UKGC active remote-casino licence, active trading-name record, active domain record, and operator site. It remains **Hold** pending full terms/withdrawal/complaints/regulatory-action review; paid-listing willingness remains unconfirmed. See `docs/ukgc-register-audit-2026-10.md` and the tracker. Source/build/artifact CI passed on https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39499260241.

- Added Bet Ahoy Ltd as a held UK prospect because the UKGC register shows active remote Casino permission from 17 December 2025. Exact consumer brand/domain and launch remain unverified, so the licence activity date is not counted as a brand launch and the prospect is not publishable yet.

- Tier 1 prospect research improved with official regulator evidence: BetTOM's active domain and remote-casino permission are matched; Betsuna's 22 May 2026 launch and white-label status are recorded alongside the UKGC's £1m ProgressPlay enforcement action; Swiss prospects admiral.ch and casineo.ch now have official ESBK online-start evidence. All remain on hold pending full editorial/legal review; no prospect has confirmed willingness to pay. See `docs/ukgc-register-audit-2026-10.md` and `docs/swiss-prospect-research-batch-2026.md`.

- Created `docs/brand-profile-casineo-ch-draft.md` from the Swiss regulator's official March 2026 approval/listing. The profile remains unscored and on hold because exact legal entity, terms, withdrawals, complaints, RG controls and enforcement review are incomplete; no commercial willingness is inferred.
- Created `docs/brand-profile-admiral-ch-draft.md` from the ESBK's official July 2025 online-start listing for Casino Mendrisio/admiral.ch. It remains unscored until the exact operating entity, terms, withdrawals, complaints, safer-gambling controls and regulatory history are checked.
- Added `docs/brand-profile-tipico-casino-de-sh-draft.md` and upgraded the internal Tipico prospect with the official 1 April 2026 launch announcement and GGL whitelist evidence. Its online-casino scope is limited to Schleswig-Holstein; full terms/withdrawal/RG/enforcement review remains outstanding and the profile is unscored.
- Added `docs/brand-profile-ember-casino-us-nj-draft.md` after matching the Ember Casino domain against the NJ DGE authorized-sites list and Delaware North's 4 June 2026 launch announcement. The profile remains unscored; it records the difference between the brand owner/group and the DGE-listed casino affiliate, and limits the scope to New Jersey.
- Added `docs/brand-profile-bettom-gb-draft.md` with the current UKGC licence/domain/trading-name match and dated launch announcement. It remains on hold for terms, withdrawal, complaints, safer-gambling and enforcement review; no score or paid-listing interest is claimed.
- Added held profile dossiers for ThreeSix Vegas and Betsuna. ThreeSix Vegas records a matched UKGC domain/licence but no verified consumer launch date; Betsuna records the 2026 launch claim, white-label domain status and material ProgressPlay enforcement history. Both remain unscored, and paid-listing willingness is unconfirmed.

- Latest source/build/artifact CI after the new profile dossiers passed: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39500484315. The run confirms source-level structure/link checks, shared JavaScript syntax, the public-only build, and exclusion of internal research files. The site still has one intentional privacy-draft warning; no live-host/browser/accessibility/legal test is implied.
- Internal held profile dossiers now exist for twenty-seven candidates: Casineo.ch, Admiral.ch, Tipico Casino (Schleswig-Holstein only), Ember Casino (New Jersey only), BetTOM, ThreeSix Vegas, Betsuna, Betinia (New Jersey only), Vegas Club Casino (New Jersey only), Winz.nl, Megaways Casino, BestOdds, Stakewise, 44Aces, Betcrown, BetLegend, BetNero, Casushi, FruitKings, 7Bet Casino, Justin Casino, LuckyMate Casino, Casiku, 247Bet, Midnite, Brillbet and Betty Casino. None is scored or approved for public publication; current terms, withdrawals, complaints, safer-gambling controls, exact legal/domain matches and regulatory histories remain to be completed as applicable.
- Added `docs/brand-profile-betinia-us-nj-draft.md` with the official NJ DGE authorized-site listing, the NJ Casino Control Commission's Q1 2026 skin-agreement report, and the operator's current rules page. The launch date remains unconfirmed by a primary source; profile is unscored and NJ-only.
- Added `docs/brand-profile-vegas-club-us-nj-draft.md` with the current NJ DGE authorized-site listing and state quarterly report. G2 Digital NJ and the Caesars/Boardwalk Regency license affiliate are kept distinct; public launch date remains secondary-source reported, and the profile is unscored/NJ-only.
- Added `docs/brand-profile-winz-nl-draft.md` after locating the official Ksa permit for Orange Gaming B.V. The dossier explicitly keeps Winz.nl on hold until the exact brand/domain notification is verified; a company permit alone is not treated as domain approval.

- Added a Chromium browser smoke suite to CI. It passed on https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39571590296, covering all 20 indexable routes, mobile overflow checks at 390px, desktop homepage overflow at 1440px, mobile menu/Escape behaviour, calculator valid/zero/negative/empty/over-limit inputs, checklist progress/reset, metadata parity, and uncaught page errors. Manual device/accessibility/production-host QA remains open.


- Automated QA was strengthened on 20 October 2026 with Chromium checks for declared page language, exactly one main landmark, skip-to-content links, accessible names for visible form controls and buttons. The enhanced suite passed on run https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39502557582. This is a lightweight smoke test only; WCAG conformance, keyboard/screen-reader review, contrast and real-device/manual testing remain open. See [launch acceptance test plan](launch-acceptance-test-plan.md).


- The expanded six-width responsive smoke suite passed on 20 October 2026: all 20 indexable routes were checked at 320, 375, 390, 768, 1024 and 1440px, alongside the accessibility smoke checks and interactive-tool checks. Run: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39502713824. Manual/device and live-host QA remain outstanding.


- The Chromium suite now fails on uncaught page errors and browser-console errors as well as structural, responsive, accessibility-smoke and interactive-tool checks. The full run passed on https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39502853616. This does not replace manual cross-browser/device, screen-reader, WCAG, legal/privacy or production-host QA.

- Added a baseline Content Security Policy to both prepared host configs and a CI validator (`scripts/check_host_config.py`) to prevent security-header drift. The validator, public-only build and expanded Chromium smoke tests passed on https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39503326238. Live deployed headers still require verification; current CSP permits inline scripts/styles and is not a strict nonce/hash-based policy.

- Added axe-core automated accessibility scans to the Chromium suite. The 20-route WCAG 2.1 A/AA-tag scan initially exposed low-contrast supporting text; the affected homepage/guide/footer colours were corrected. Passing run: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39504107580. Manual accessibility review remains required.

- Expanded the wagering-calculator browser tests to cover decimal values, empty/negative/over-limit multipliers, amount input limits, currency changes, and invalid-input state. The full source/build/security-config/artifact/Chromium/axe suite passed: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39504606241. Manual production-host and real-device checks remain open.

- Hardened the prepared CSP further: both scripts and styles are now same-origin only (`script-src 'self'; style-src 'self'`); the two learning-tool scripts and styles are external files included by the public-only build, inline style attributes were replaced by classes, and source CI rejects inline scripts/styles. Full CI passed on https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39506143452. Live deployed response headers still need verification.

- UK prospect research batch added eight held leads (Brillbet, Betty Casino, Casushi, FruitKings, Betcrown, BetLegend, BetNero and 247Bet) to the Tier 1 tracker using UKGC licence/domain records where available. Several are white-label domains or have unresolved brand/operator matches; launch dates are secondary-source claims or remain unverified. All are Hold, and willingness to pay remains Unconfirmed. See `docs/tier-1-new-brand-research-seeds.md` and the tracker.

- Follow-up UKGC research added Casiku (White Hat Gaming white-label domain; launch timing is secondary-source only) and Midnite (UKGC search returns both Dribble Media Limited and Midnite Limited for the brand/domain, requiring operator-transition resolution). Both remain Hold; no willingness to pay is inferred.

- A second UKGC-backed research batch added eight more held leads (Stakewise, 44Aces, Casino and Friends, Peachy Games, Play Sunny, Neptune Play, PlayWins and BetFusion). Some are white-label domains or have unresolved current-operator/product scope; launch dates remain secondary-source claims or unverified. All are Hold and none has confirmed willingness to pay.

- A third UK research batch added five leads with active UKGC domain/licence evidence: Megaways Casino (official 24 March 2026 relaunch), BestOdds, LuckyMate Casino, 7Bet Casino and Justin Casino. Launch timing for four of these is secondary-source reported or needs confirmation; all remain Hold and willingness to pay is Unconfirmed.

- Added three internal GB dossiers (BestOdds, Stakewise and 44Aces) with current UKGC licence/domain evidence. Together with the Megaways Casino dossier, this brings the internal dossier set to 14; terms, withdrawals, complaints, safer-gambling controls, enforcement and commercial qualification remain incomplete, so none is approved for public publication.

- Hosting decision updated: Vercel is the selected platform. The connected BeinCasinos team is on Hobby with no linked projects; do not use Hobby for the commercial paid-listing/affiliate business. Review current Pro price/usage and commercial terms before any paid upgrade. No project, subscription, DNS change or deployment has been made.

- Canonical host default is now set to `https://beincasinos.online` (apex), matching existing canonical, Open Graph and sitemap URLs; final host setup should redirect `www` permanently to apex and verify both hostnames. This is a source-level decision only—DNS remains unchanged.


## Follow-up — 21 October 2026

- Public review methodology is now versioned as v1.0 with a visible 21 October 2026 update date on both `/reviews/` and `/how-we-review/`. The source checker enforces the public version/date disclosure. All three related CI runs passed: [Reviews page](https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39590735156), [detailed methodology](https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39590739170), and [disclosure guard](https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39590743225). This does not imply any live casino profiles are scored, nor does it clear external launch gates.


- Latest CI run: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39573291872 passed all 10 substantive steps, including source/link checks, shared-JavaScript syntax, Vercel configuration, public-only build, internal-file exclusion, Chromium browser smoke tests, and sanitized artifact storage. This is repository/CI evidence only; it is not live-host validation, legal clearance, or release approval.
- The tracker validation now enforces a minimum of 100 brand-name research leads while excluding two category-level restriction rows. The 100-name count remains a research-queue milestone only; the added grade-C leads remain held until primary-source operator/domain and market permission checks are completed.
- Release remains BLOCKED. Do not deploy, enable indexing, or represent the prospect queue as 100 qualified or fee-paying buyers.


## Latest operations update — 21 October 2026

- Added the owner-facing launch-gate/evidence checklist and commercial partnership operating playbook in PR #1. The pull request was marked ready and merged to `main` after the full repository workflow passed: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39592440087.
- Latest verified workflow result: all substantive steps passed, including HTML/local-link checks, shared JavaScript syntax, Vercel configuration validation, public-only build, internal-file exclusion, Chromium browser smoke tests, and sanitized artifact storage. This is CI evidence for the repository, not production-host or legal approval.
- The commercial playbook documents fixed-fee listings, CPA, revenue share, hybrid and sponsored-content models as options to validate—not confirmed deals or proven pricing. No operator outreach was sent and no willingness to pay is claimed.
- Deployment remains BLOCKED pending evidence for trademark/name clearance, legal review across the intended markets, real mailbox/contact monitoring, final privacy and commercial disclosures, live-domain/DNS verification, manual device/accessibility QA, and explicit owner authorization for paid hosting and production deployment.
- No Vercel project or paid subscription was created, no DNS was changed, no production deployment was made, and indexing remains blocked.


- Added `docs/tier-1-market-compliance-gate-2026-10-21.md`, an internal primary-source screening matrix for AU, US, FR, DE, CH, GB and NL. It flags France's online-casino prohibition, Switzerland's Swiss-authorisation requirement, state-by-state US review, UK/Netherlands affiliate responsibilities and Australia's August 2026 reforms affecting activity-based affiliate commissions. It is a risk-screening aid, not legal clearance; all markets remain gated pending legal review and dated evidence.


## Tier-1 compliance gate hardening — 21 October 2026

- Added and linked `docs/tier-1-market-compliance-gate-2026-10-21.md` to README, the owner release gates, and the final deploy runbook.
- Tightened the market dispositions: block online-casino promotion into France and Australia; keep the US held by state/product; require exact official authorisation for Switzerland and Germany; require current regulator/domain and affiliate-advertising review for Great Britain and the Netherlands.
- Aligned the Australia note with the existing target-market matrix: ACMA reports a range of advertising/affiliate reforms due to commence 1 January 2027. The enacted text, commencement/transition instruments, exact scope and qualified advice still need re-checking before any 2027 campaign or commission agreement.
- This work is an internal screening control only. It does not constitute legal clearance or approve any operator. No partner outreach, paid placement, affiliate activation, production deploy, DNS change, Vercel upgrade, or indexing change was made.
- The structured launch-evidence-register commit (`585e92dfb3e424308156584c08c2925e728f00b8`) passed the full `Static site checks` workflow on 21 October 2026: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39593500182. All 10 substantive steps passed, including HTML/local-link checks, JavaScript syntax, Vercel configuration, public-only artifact build and leak checks, Chromium browser smoke tests, and sanitized artifact storage. This verifies the latest repository commit only; legal, owner, and live-host gates remain open.


- Added `docs/paid-placement-order-form-internal-draft.md`, a non-binding internal order-form and contract checklist covering exact deliverables, market eligibility, fee/commission calculations, disclosure, privacy/tracking, editorial independence, pause/removal rights, invoicing and recordkeeping. It is not a live offer or a substitute for counsel-drafted terms. It cannot be used until publisher identity, legal review, audience evidence, market approval, privacy controls and launch approval are complete.

- Opened [Release blocker checklist issue #2](https://github.com/beincasinos-Brand/Beincasinos/issues/2) to track external/owner-only evidence gates separately from code tasks. The issue explicitly keeps production deployment and indexing blocked until the legal, domain, privacy, hosting, and live-QA evidence is recorded.


- Added `docs/measurement-and-media-kit-plan.md` and linked it from README. It defines a privacy-first measurement sequence, source/date/metric definitions, a truthful media-kit evidence table, and a hard stop against selling inventory before legal, privacy, audience and owner gates are met. This is planning only: it does not enable analytics or assert any traffic figures.


- Added `docs/launch-evidence-register-template.csv`, a structured gate-by-gate register for identity, hosting, market/privacy, editorial/commercial, build/QA, deployment and indexing. It distinguishes owner actions and unverified checks from passes; keep credentials and private account evidence out of the repository.

## Current launch evidence status register — 21 October 2026

- Added `docs/launch-evidence-register-current-status-2026-10-21.csv`, a current-state register with 25 gate rows separating verified source/CI/artifact passes from unverified owner evidence, legal review, hosting approval, manual live-host QA, and indexing steps.
- The latest recorded CI run for main commit `b294cbc210b16600366dd5e513ee774074daebd3` passed: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39593632251. This is source/build/browser-smoke evidence, not production-host or legal clearance.
- Statuses deliberately remain open or blocked where no verifiable evidence exists. In particular, domain/mailbox access, publisher and trademark review, market-specific legal review, commercial hosting approval, manual acceptance tests, production DNS/deployment, and Search Console indexing are not marked complete.
- Linked the register from README. Keep private account evidence, tokens, inbox contents, and credentials out of the repository.


## Operator qualification controls — 21 October 2026

- Added [`docs/operator-qualification-scorecard.md`](operator-qualification-scorecard.md), an internal qualification standard with hard market/legal gates, evidence-weighted review criteria, an evidence record, explicit hold/reject/pass outcomes, and recheck triggers.
- The scorecard explicitly prevents numerical scores from overriding licence/legal gates, treats missing evidence as not evidenced, separates commercial fit from editorial judgement, and confirms that prospect leads are neither approved listings nor confirmed buyers.
- This is a documentation/process improvement. It does not clear any candidate, contact operators, establish commercial demand, or remove launch blockers.


## Latest verified commercial-pipeline regression coverage — 21 October 2026, 12:05 UTC

- The latest integrated **Static site checks** workflow passed on commit `8474df58c7527115321b5f83f0d25ee928e237ac`: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39596686109.
- Added regression coverage for case-insensitive duplicate brand names and a valid fully-qualified paid-listing path, alongside the prior negative cases for invalid stage, missing first-contact date, non-HTTPS evidence URL, incomplete contract/payment/review gates, malformed or reversed dates, and a paid listing incorrectly marked with an inapplicable invoice.
- This is a passing automated source/build/browser-smoke and pipeline-validator run. It does not prove a real partner is licensed, willing to pay, or legally promotable, and does not replace a current final-artifact inspection or manual live-host/device tests.
- Release remains **BLOCKED**. No Vercel project/paid plan, DNS change, public deployment, Search Console submission, indexing unblock, or partner outreach was performed. Domain/mailbox evidence, name clearance, qualified market/privacy review, commercial hosting approval and explicit owner release approvals remain outstanding.


## Public content expansion — review-site business model transparency — 21 October 2026

- Added the public guide `/guides/how-casino-review-sites-make-money/` to explain affiliate CPA, revenue share and hybrid arrangements, fixed-fee listings, sponsorship disclosures, evidence standards, and the distinction between commercial revenue and editorial eligibility. The guide explicitly says BeInCasinos has no scored/ranked casino profiles or active paid placements at this stage and makes no audience-performance claims.
- Added the guide to the Guides hub and sitemap, and included it in the Chromium/axe browser smoke route inventory so CI tests its HTTP response, metadata, responsive widths, accessible structure and WCAG 2.1 A/AA scan.
- The page is educational media literacy, not an endorsement or instruction to gamble. It does not add casino offers, operator links, affiliate tracking, forms, or claims of live partnerships.
- CI for the latest content commit must pass before describing the new route as verified. Live-host testing, legal/privacy review, domain/mailbox verification, commercial hosting approval and owner launch authorization remain separate gates.


## Verification checkpoint — 21 October 2026, 12:17 UTC

- Integrated workflow run **39598335966** passed on commit `9042b53b2f9b94f8eabe7c6556e384ac713ab602`. It checked HTML/local links, the paid-listing pipeline validator and regression tests, shared JavaScript syntax, Vercel/security configuration, public-only artifact construction and exclusion of internal files, and Chromium/axe smoke tests across 24 indexable routes and six viewport widths. See https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39598335966.
- The public-only artifact was uploaded as `beincasinos-public-site-dist` (artifact ID `12345955066`, approximately 72,972 bytes). It is a temporary CI artifact, not a deployed site; inspect/rebuild the exact release artifact before any deployment.
- Added the new casino-review-business-model guide to the manual launch acceptance checklist so human browser checks include it too.
- Updated the launch evidence register to reference the latest passing workflow and artifact.
- Release remains **BLOCKED** pending real-world owner evidence and approval: domain/DNS control, monitored mailbox, name/trademark decision, accurate publisher/legal identity, qualified privacy/market review, approved commercial hosting, manual device/live-host QA, and explicit launch authorization. No DNS changes, public deployment, Search Console submission, indexing unblock, or commercial outreach were performed.


## Prospect research and pipeline hygiene — 21 October 2026

- Added 12 additional UK launch-discovery candidates to the internal research note and paid-listing pipeline: Brillbet, BetLegend, BetAhoy, Proper Bet, Stakewise, Betty, Megaways Casino, BestOdds, 247Bet, TigerBet, Betnero and ThreeSix Vegas.
- All 12 are recorded as `hold` / `not_contacted`. This is not a list of approved operators or willing buyers. Most evidence is secondary-source discovery only; Brillbet has an initial UKGC trading-name match, while Betty has an operator record but its exact brand/domain mapping remains unverified. Each requires exact-domain, remote-casino licence/product-scope and regulatory-history checks.
- No outreach was sent. The prospect count is still far below the desired 100, and no evidence supports a claim that any of these brands will pay a listing fee.
- Updated the manual launch acceptance checklist to include the new public guide and refreshed the launch evidence register after the 24-route integrated CI pass.


## Prospect discovery batch 2 — 21 October 2026

- Added 13 more 2024–2025 discovery leads to the internal research note and sales tracker: Neptune Play, PricedUp Casino, DragonBet Casino, Bally Casino UK, Rose Casino, O'Reels Casino, BetMaze Casino, Puntit Casino, LuckyMate Casino, Lottoland Casino, Casino Kings, Casiku and Mega Riches Casino.
- The combined research queue is now approximately **38 candidate entries**, not 100. New entries are `hold` / `not_contacted`, and their legal entity, exact domain, product permission and launch evidence remain unverified unless explicitly stated. Some discovery sources are low-confidence and must be replaced with primary evidence before qualification.
- No sales outreach or paid partnership was initiated. No willingness-to-pay is known. Continue to keep France and Australia online-casino promotion blocked and evaluate all other markets separately.


## Netherlands discovery follow-up — 21 October 2026

- Added VBet, Lucky7 Casino, Betnation and Circus as four additional Netherlands market-entry discovery leads, each recorded `hold` / `not_contacted`.
- The internal research queue now contains approximately **42 candidate entries**, still short of the target 100. All newly added Dutch candidates require a current Ksa/Kansspelwijzer check for exact permit holder, domain, product scope and status before qualification; historic launch dates do not establish current authorisation.
- No outreach or public promotion has been initiated. NL remains a separate market-specific review gate.


## Pipeline reconciliation — 21 October 2026

- Reconciled the initial 13 research leads into `docs/paid-listing-sales-pipeline.csv`; the tracker now contains **42 unique candidate rows**, all `hold` / `not_contacted`. This is a discovery queue, not 42 approved operators or prospective paying customers.
- Each record has a source URL and an explicit verification task. Unknown legal entities and secondary-source-only launch claims remain marked unverified; Betsuna also carries a caution to review the operator's material regulatory history before editorial consideration.
- Updated the launch evidence register to the latest previously passing CI checkpoint. The newest source changes still need their own completed CI run before being treated as verified.

## Latest research and content checkpoint — 21 October 2026

- The paid-listing pipeline contains **47 candidate rows** after the latest research commits. All remain `hold` / `not_contacted`; this is a discovery backlog, not 47 approved operators, qualified buyers, or brands willing to pay. No outreach has been sent.
- The latest two research commits passed the full integrated workflow, including the pipeline validator, public-only artifact exclusion, and Chromium/axe smoke tests: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39599636140 and https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39599621913.
- Added market-specific official starting points to the public licence-check guide. Its own CI run is pending; do not call that particular content change verified until the new run completes.
- Release remains **BLOCKED**: no production deployment, DNS change, Search Console submission, or crawl unblock has been performed. Name clearance, legal/privacy review, mailbox/domain evidence, commercial hosting approval, and live-host/manual acceptance remain open.


## Cloudflare runbook alignment — 21 October 2026, 14:13 UTC

- Merged PR #3 (`Docs: align deployment runbook with Cloudflare Pages`) into `main` at `dbc2a759844301075b4fe42595bfa8a2431b0a05`. The runbook now consistently documents Cloudflare Pages Free as the preferred host, the public-only build (`python3 scripts/build_site.py`, output `dist`), and the required legal, privacy, DNS-preservation, preview, public-launch and indexing gates.
- The post-merge GitHub Actions run passed: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39614845935. The `check` job completed successfully, including local HTML/link checks, paid-listing pipeline validation and regression tests, JavaScript syntax, host configuration validation, public artifact leak checks, and Chromium smoke tests.
- This CI result confirms repository/source and generated-artifact checks only. It does not prove the domain is live, Cloudflare is connected, DNS is correct, legal review is complete, or the site is production-ready.
- Secrets posted in chat must be revoked and replaced; no token was used by automation. No Cloudflare project, DNS change, public deployment, crawl unblock, Search Console verification, or external operator outreach was performed.
- Release remains blocked until the owner-only/legal gates in `docs/final-deploy-runbook.md` and GitHub issue #2 are evidenced and a controlled preview passes manual checks.


## Follow-up documentation CI — 21 October 2026, 14:15 UTC

- The completion-board evidence update passed the full GitHub Actions `Static site checks` workflow on commit `7f32f57ce34bd08f008d4b04cb4ca2cecd4b4c8a`: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39615185334.
- The check job completed successfully: HTML/local links, paid-listing pipeline hard gates and regression tests, JS syntax, host configuration, public-only artifact exclusions, Chromium smoke tests, and sanitized artifact creation.
- The public route sitemap currently contains the site’s educational, methodology, policy, contact and tool pages. It is prepared but must not be submitted to Search Console until launch gates are cleared and the owner authorizes indexing.
- No live-host/manual acceptance result is implied by CI. Cloudflare project setup, domain/DNS verification, legal/privacy clearance, Search Console verification, production deployment and public indexing remain unconfirmed or blocked.

## Current operational checkpoint — 21 October 2026, 23:46 UTC

- Cloudflare Pages project `beincasinos` is connected to GitHub with `main` as production branch. Read-only diagnostics report production deployment commit `4832a591b0d8df0b20a64b9b7dfa1415e3b3005e` as active: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39695415851.
- Static site checks passed on commit `4832a591b0d8df0b20a64b9b7dfa1415e3b3005e`, including HTML/local links, pipeline schema/regression tests, JavaScript syntax, build/security configuration, public-only artifact checks, and Chromium smoke tests: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39695415837.
- Live public fetch completed at 23:46 UTC: the homepage and `robots.txt` loaded, the sitemap returned 37 canonical apex URLs, and `https://www.beincasinos.online/` resolved to `https://beincasinos.online/`. Homepage canonical and Open Graph URL both point to the apex domain. `robots.txt` allows crawling and names the root sitemap. This verifies retrieval/redirect behavior from the external fetcher, not Google indexing.
- Registry now has 16 research leads (10 Swiss regulator-listing leads and 6 UK leads); these are not 16 approved reviews. All entries remain publication-hold until exact legal operator/domain mapping, current product-specific licence scope, terms, safer-gambling controls and regulatory history are reviewed. The 32Red Limited Casino Remote licence is recorded as surrendered and is not treated as an eligible active UK licence.
- Search Console submission/indexing and Google impressions/clicks are not confirmed by CI or the Cloudflare API. Do not claim indexed URLs or traffic without Search Console evidence. Google states sitemap submission and recrawl requests do not guarantee indexing.
- Open owner/legal gates remain: name clearance, jurisdiction-specific legal/privacy review, contact/mailbox verification, manual live-host acceptance, and Search Console account-side inspection/submission. No DNS or nameserver change was made by this checkpoint.


## Brand research progress — 22 October 2026

- Built a Swiss regulator-backed inventory of 10 online casino platforms listed by the Swiss Federal Gaming Board. Internal research drafts now exist for the full set: jackpots.ch, mycasino.ch, online.swisscasinos.ch, casino777.ch, starvegas.ch, 7melons.ch, pasino.ch, swiss4win.ch, admiral.ch, and casineo.ch. The master register is `docs/brand-verification-register-switzerland-batch-1.md`.
- Built a Great Britain first-stage inventory of 10 brands with UK Gambling Commission records showing active remote casino licences: 888casino, Sky Vegas, Ladbrokes, Coral, LeoVegas, Grosvenor online casino, Betway, Unibet, Betfred, and Paddy Power. Internal research drafts are in the review PR and will remain on HOLD until CI and further checks pass. Master register: `docs/brand-verification-register-great-britain-batch-1.md`.
- Licence-status due diligence caught an exclusion: Mr Green Limited's UKGC record shows its Casino Remote licence surrendered on 28 October 2024, so it is not counted as an active Great Britain candidate without fresh regulator evidence.
- Counting discipline: 20 first-stage jurisdiction/licence candidates identified across two distinct markets; **0 fully publication-approved brand reviews** so far. These counts are deliberately separate. A licence listing is not a complete operator review, a game-permit check, a payout test, or permission to target another country.
- Relevant internal work: PR #19 merged (MyCasino.ch draft); PR #21 merged (eight additional Swiss drafts); PR #22 merged (Swiss candidate register); PR #23 merged (Great Britain candidate register). PR #20 Search Console audit and PR #24 Great Britain drafts are still in CI/review as of this update.
- No production deployment, DNS/nameserver change, billing change, or Search Console write action was made. Do not deploy until the owner-requested 100-brand verification target and all launch gates are met; the final deployment should be a single controlled release after acceptance checks.

### Next brand-verification gates
1. Finish current CI/review and merge only after successful checks.
2. For each brand, verify the exact consumer domain and legal entity against current site terms and regulator records, including product/jurisdiction scope.
3. Review payments, withdrawal rules, current bonus terms (if mentioned), complaints/escalation, privacy/contact, safer-gambling resources, game-permit scope, and regulator enforcement history.
4. Capture dated primary-source evidence, resolve discrepancies, and require second-editor sign-off before counting a brand as fully verified.
5. Repeat with additional regulated jurisdictions until 100 profiles pass the complete verification gate. Keep candidates that lack evidence on HOLD rather than inflating the total.
