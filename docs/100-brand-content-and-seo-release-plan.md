# 100-brand content, review and SEO execution plan

**Status:** internal operating plan; not a public recommendation or launch approval.  
**Updated:** 2026-10-22  
**North-star ambition:** 100 million daily impressions is an aspiration only, not a forecast or guarantee.

## Current inventory truth

- `docs/brand-research-template.csv` contains 100 candidate rows plus its header (100 candidates, not 100 verified brands).
- Candidates are research leads. Do not describe them as licensed, approved, safe, recommended, tested, or commercially qualified until the evidence for the exact brand, legal entity, domain, product and target jurisdiction is independently checked.
- Current verified-to-publish count remains **0** in the 100-brand sprint until each profile passes all gates.
- Public `/reviews/` correctly states that no live casino profiles are scored or ranked yet. Keep that truthful status until profiles are genuinely approved.
- **Production route status (verified 2026-10-22):** the ADR guide returns HTTP 200 with the expected self-canonical; the sitemap returns HTTP 200 and includes the guide; the www guide URL returns HTTP 200 and resolves to the apex canonical. The latest repair workflow preflights the public route and skips the privileged cache purge when the page is already healthy. This confirms route availability, not Google indexing or search traffic. See [successful production verification](https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39753522659) and [static site checks](https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39753522742).
- **Latest repository checks (verified 2026-10-22):** commit `0c849925513c5a71cf258bd59f667dd150e314c2` passed the full static-site workflow, including Chromium browser smoke tests, and passed read-only Cloudflare launch diagnostics. See [static checks](https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39754095237) and [Cloudflare diagnostics](https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39754095326). The latest read-only Cloudflare diagnostics on commit `7d246c4670c8720b4744f43ee7cfbcf820ec23d5` also passed ([run](https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39754552186)); the static checks for that commit were still in progress when this note was updated ([run](https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39754552261)). This validates repository/build checks, not Google indexing or search performance.

## Release sequence

### Gate 0 — production reliability and publisher readiness

1. The ADR guide route currently passes production checks, so do not rotate credentials or run a cache purge merely for this resolved incident. If a future verified route/cache issue requires a purge, repair the GitHub Actions credential through GitHub's secret settings with only the minimum required zone permissions; never paste secrets into chat.
2. For any route repair, require production checks for HTTP 200, the expected self-canonical, sitemap inclusion, and www-to-apex behavior. Do not change DNS to work around a path-level failure. The latest successful checks prove availability of this guide, not Google indexing.
3. Complete the owner-only release checklist in Issue #2: publisher identity/contact, trademark, target-market legal/advertising review, Morocco privacy/CNDP review, commercial/affiliate policy, hosting cost/terms, and manual accessibility/mobile/outbound-link QA.
4. Do not re-submit the sitemap or request mass indexing until the release checklist is explicitly cleared by the owner. The existing prior Search Console snapshot is stale relative to the current 44-URL sitemap.
5. Treat indexing as a separate measurement from HTTP availability and CI. Google's guidance says crawl/indexing is not guaranteed and can take time; inspect representative priority URLs and use the Page indexing report to diagnose exclusions rather than repeatedly requesting the same URLs. See [Google Search Console Page indexing report](https://support.google.com/webmasters/answer/7440203?hl=en-TT).
6. Do not respond to slow indexing by publishing dozens of near-duplicate pages. Google's spam policy identifies scaled, unoriginal content made primarily to manipulate rankings as abuse; prioritize genuinely useful, evidence-backed pages and internal discoverability. See [Google Search spam policies](https://developers.google.com/search/docs/essentials/spam-policies?rd=1&visit_id=639264566515765879-584995437).

### Gate 1 — research the 100 candidate brands in batches

Process 10 brands at a time. A candidate may move through `prospect → researching → verified_for_review → approved_to_publish → published`, or be held/rejected. Keep the exact status in the CSV; do not count a row as verified until the evidence log is complete.

For every brand, record:
- exact official domain and consumer-facing brand;
- exact legal entity and any white-label relationship;
- regulator register record and active permission for the exact product;
- permitted and excluded jurisdictions, checked against the current regulator source;
- current official terms, bonus restrictions, withdrawals, fees/limits and verification conditions;
- complaints escalation, customer support and safer-gambling controls;
- dated primary-source links for every material claim;
- historic regulatory actions and unresolved discrepancies;
- commercial relationship and visible paid/affiliate disclosure;
- reviewer, UTC check date, next-review date, and second editorial sign-off.

A missing or conflicting material fact means **HOLD**. A licence in one market does not establish global availability. Do not assign a score until eligibility checks pass and each scoring criterion has evidence.

### Batch order

1. **CH — official register-led batch:** finish the Swiss Federal Gaming Board-listed platforms and verify exact current domain/operator/product scope. Do not infer permission from brand similarity.
2. **GB — UKGC batches 1–4:** continue checking exact domains and trading names against the current UKGC register, active remote-casino permission, terms, complaints and historical actions. The current research notes are [batch 1](gb-brand-research-batch-1.md), [batch 2](gb-brand-research-batch-2.md), [batch 3](gb-brand-research-batch-3.md), [batch 4](gb-brand-research-batch-4.md), and [batch 5](gb-operator-research-batch-5.md). Batch 5 adds eight official-register operator leads; all eight remain HOLD because consumer brand/domain and other publication checks are incomplete. Distinguish the licensed operator from the consumer brand; related entity records are not automatically distinct brands.
3. **NL — KSA batch:** follow the new [Netherlands verification protocol](nl-market-verification-protocol.md); use individual live Kansspelwijzer entries and current permit decisions, re-check renewals and domain/product scope. The automated extraction did not expose a complete stable operator list, so 0 Dutch brands are approved from this pass.
4. **DE — official state/whitelist batch:** include only brands with exact current permission and product scope confirmed from official sources.
5. Other markets only after a documented market-specific legal and advertising/affiliate eligibility review. Do not make a global casino list by mixing incomparable legal regimes.

## Public review page specification

Every approved profile must be genuinely useful and materially distinct, not a spun template. Include:
- a clear answer-first summary stating the market and date checked;
- brand/domain/legal-operator relationship and what the regulator record does and does not prove;
- current product and jurisdiction scope;
- a practical terms table: bonus eligibility, wagering base, expiry, max bet, max cashout, excluded games, fees, withdrawal limits and verification rules where applicable;
- official complaints route, support options, safer-gambling tools and local help resources;
- historic regulatory actions and unresolved facts in fair context;
- transparent source log, correction/contact route, update date and next review date;
- visible affiliate/paid-placement disclosure; editorial conclusions remain independent of payment.

Never claim hands-on testing, withdrawal speed, complaint resolution, customer experience or monitoring unless that activity was actually performed and documented. Do not use unsupported superlatives or fabricated user reviews.

## SEO architecture

- Build one useful hub at `/reviews/`, then link to each approved profile only after the profile passes publication checks.
- Create market hubs only when there are enough verified, distinct profiles to help users compare that market; avoid empty taxonomy pages.
- Connect brand profiles to relevant guides: licence checks, legal operator vs brand, bonus terms, withdrawals, complaints, safer gambling and review methodology.
- Use descriptive titles and unique meta descriptions; one clear H1; correct canonical; meaningful internal links; breadcrumbs where useful; valid sitemap entries only for canonical 200 URLs.
- Add structured data only when it accurately represents visible page content. Never add fake ratings, fake review counts, or aggregate ratings without real eligible data.
- Avoid doorway pages, duplicated boilerplate, keyword stuffing, fake freshness dates and mass indexing requests.
- After release, measure actual Google Search Console queries, clicks, impressions, CTR, average position and country/page coverage; use GA/analytics only after privacy and consent review.

## Weekly operating scorecard

Report counts, not assumptions:
- candidates in registry / verified / held / rejected / published;
- percentage of material claims backed by current primary sources;
- live canonical pages returning HTTP 200;
- sitemap URL count vs successful canonical URLs;
- Search Console clicks, impressions, CTR and average position by page/query/country;
- pages indexed as reported by Search Console, with date and method;
- pages needing review because of changed terms, licence records or regulatory actions.

## Acceptance criteria for the 100-brand milestone

“100 brands” means 100 distinct brands with completed source-backed evidence, exact market/product scope, current terms and complaints/safety information, dated review, no unresolved critical conflicts, and independent editorial approval. Candidate names or bulk-generated pages do not count. The milestone is not complete merely because 100 URLs exist.


## Production technical audit — 22 October 2026

A live read-only audit checked the homepage, `/reviews/`, `/guides/`, `/sitemap.xml`, and `/robots.txt`.

- The homepage, review hub, and guide hub returned page content with unique titles, descriptions, and self-referencing canonical URLs on `https://beincasinos.online/`.
- The homepage links to core policy pages and the main learning guides; the guide hub links to the newer withdrawal, payment verification, operator-identity, complaint, bonus-term and probability explainers.
- `robots.txt` permits crawling and declares `https://beincasinos.online/sitemap.xml`.
- The sitemap contains 44 canonical apex URLs in the repository snapshot and includes the latest guide additions. Reconcile every URL against the live HTTP status, canonical and robots directive during future release checks.
- The review hub accurately says that no casino profiles are currently scored or ranked; the candidate research notes remain internal until the evidence gates are passed.

**Important limitation:** this is a crawlability and on-page metadata check, not proof that Google indexed any specific URL or that the site is receiving impressions. Use dated Search Console performance and indexing reports for those claims. Do not repeatedly submit the same URL as a substitute for improving evidence, internal discovery and page quality.


### Follow-up audit — live pages and register research (22 October 2026)

A second live fetch checked the homepage, `/robots.txt`, `/sitemap.xml`, `/reviews/`, `/market-research/`, and `/privacy/`.

- Homepage title, description, Open Graph URL and canonical consistently point to the apex homepage. The live sitemap advertises **44 URLs**.
- The review hub remains transparent: no casino profiles are scored or ranked, and the planned scoring framework is not represented as completed testing.
- The market-research page documents market-specific restrictions and identifies the Swiss Federal Gaming Board's ten listed online platforms as a research snapshot, not an endorsement or ranking. Any later profile still needs fresh operator, licence-extension, product-permit, terms, complaint and safer-gambling checks.
- The privacy notice currently describes a static informational site and says there is no analytics integration, advertising pixel, contact form, visitor account system or active affiliate tracking in the current source. This is a claim about current implementation; re-audit and update the notice before enabling any of those features. Confirm the contact mailbox is monitored before relying on it for privacy or editorial requests.
- New private UKGC register follow-up in `docs/gb-operator-research-batch-5.md` records active-domain leads for Gamesys Operations Limited and SBKI/Fitzbet, plus a material 2023 regulatory-action record for Gamesys. These are **research leads only**; none is approved for a public profile.

**Release gate remains unchanged:** the last code commit in this follow-up changes internal research documentation only. Cloudflare's read-only diagnostic completed successfully, and static site checks completed successfully. This does not itself publish new public content, establish Google indexing, or demonstrate Search Console performance.


### Sitemap-wide live audit — 22 October 2026

A live fetch inspected all **44 URLs** currently listed by `https://beincasinos.online/sitemap.xml` (homepage, hubs, tools, policy pages and guides).

- All 44 sitemap entries were retrievable by the page-fetch audit; no per-page fetch errors were returned.
- The homepage and all 43 remaining entries returned a title and description, and each inspected page's canonical matched its sitemap URL.
- The complaint guide change for Great Britain was verified live at `/guides/how-to-complain-about-a-casino/`; the page links to the Gambling Commission's official eight-week complaint guidance and its ADR guide (updated 15 May 2026).
- This is an external fetch and metadata audit, not a Googlebot crawl, Search Console indexation report, performance measurement, or guarantee of indexation. Fetch success alone does not prove HTTP status as seen by every crawler, ranking, or impressions.
- Follow-up: compare the exact 44 URLs against Search Console's Page indexing and Performance reports when authorized data is available; resolve any discovered excluded/canonical-selected URLs with evidence rather than resubmitting everything repeatedly.


### Complete sitemap URL spot-check — 22 October 2026

A live production crawl checked the homepage separately and all 43 non-homepage URLs returned by the sitemap extractor (the XML advertises 44 URLs total). Across the checked pages, the fetch results showed page titles, meta descriptions and self-referencing apex canonicals; no noindex directive was returned in the extracted page metadata. The new payment-method ownership guide is live and includes anti-phishing advice, safe handling of identity documents, a carefully scoped Great Britain verification note, and links to related withdrawal/complaint guides.

This is a crawler-based metadata/content availability check, not a definitive HTTP-status matrix from every network path and not a Google indexing report. The XML advertises 44 URLs; the extractor returned 43 non-homepage entries, with the homepage independently checked above. Keep using Search Console's URL Inspection and indexing reports for Google's own state.
