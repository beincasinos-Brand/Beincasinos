# BeInCasinos SEO execution backlog — crawlable pages before scale

**Updated:** 22 October 2026  
**Status:** internal implementation backlog; not a claim of ranking or indexing.  
**Release rule:** this plan does not authorise production deployment. Public pages should only be added after their factual, legal, editorial and technical checks pass.

## Objective

Grow useful, discoverable coverage without manufacturing thin pages, misleading casino rankings, or implying legal availability where a product is not permitted. The 100-brand target is a research target, not permission to publish 100 incomplete profiles.

## Workstream A — technical baseline

Complete on a single release candidate before production:
- [ ] Run the configured static-site build from a clean checkout and save the full log.
- [ ] Check all internal links in built HTML; fail on broken local links, empty anchors, placeholder hrefs and accidental links to internal research docs.
- [ ] Parse generated sitemap as XML; require HTTP URLs on the canonical apex host, unique URLs, no redirecting URLs, no 404/5xx URLs, and no noindex pages.
- [ ] Confirm each indexable HTML page has one descriptive title, one meta description, a canonical URL, a single primary H1, language declaration, viewport, and useful visible text.
- [ ] Verify robots.txt is valid plain text and declares the actual sitemap URL.
- [ ] Check www-to-apex, HTTP-to-HTTPS, trailing-slash policy, unknown-path 404, and query-string canonical behaviour.
- [ ] Check JSON-LD parses and matches visible content; never add ratings/reviews/aggregateRating unless there are genuine published reviews and substantiation.
- [ ] Inspect mobile viewport, keyboard focus, heading order, contrast, accessible names, cookie controls, privacy/affiliate notices, and safer-gambling footer.
- [ ] Confirm build output contains no internal evidence packs, unpublished drafts, tokens, environment values, or credentials.
- [ ] Capture before/after URL inventory and deployment commit so the release is auditable.

## Workstream B — build topic clusters in useful order

Publish a hub only when it has a distinct audience purpose and enough substantive, verified content to be useful.

1. **Trust and methodology:** how reviews are researched; evidence standards; correction policy; affiliate disclosure; responsible gambling; complaints and contact.
2. **Market legality hubs:** one per target market with regulator links, licence/product distinctions, last-checked date, and explicit restrictions. Avoid claiming the whole country has a single uniform licence where regulation is regional.
3. **Product explainers:** slots/RTP/volatility, roulette variants, blackjack rules, baccarat, craps, live dealer, poker, bingo and lottery. Explain rules and odds accurately; do not imply a game guarantees profit.
4. **Payment and account guides:** deposits, withdrawals, KYC, fees, payment-method availability and dispute escalation. Distinguish operator claims from independently observed testing.
5. **Vertical hubs:** sports betting, horse racing, bingo, lottery, poker, land-based venues, social/sweepstakes products and B2B game studios each get separate legal scope and separate review standards. Do not mix them into an “online casino” ranking.
6. **Brand reviews:** only after exact local permission, legal entity/domain match, current terms, payments, bonuses, RG, privacy, support, enforcement and independent second review are evidenced.

## Workstream C — market gates

| Market | Publication rule |
|---|---|
| Australia | No “legal online casinos in Australia” list. Prioritise legal restrictions and consumer protection; treat other permitted gambling verticals separately. |
| Canada | Name the province/territory on every relevant hub and profile. Ontario approval is not nationwide authorisation. |
| Great Britain | Match exact domain and casino permission in the current UKGC register; betting permission alone is not casino permission. |
| Switzerland | Match platform to ESBK/FGB online-casino list and confirm specific game permissions. |
| France | No legal online-casino recommendations. If covering legal online poker/betting, label those verticals accurately and separately. |
| Italy | Match exact domain, concessionaire and casino-game scope to current ADM records. |
| Germany | Distinguish GGL-authorised virtual slots/poker from state-authorised table games and state scope. |
| Austria | Do not infer Austrian authorisation from an EU or foreign licence; require current local legal sign-off. |
| Netherlands | Match exact domain, entity, active Ksa permit and product scope. |
| Sweden | Match exact domain/entity and licence validity in the current Spelinspektionen register. |

## Workstream D — editorial acceptance criteria

A page is not ready because it contains a brand name or long word count. Before it is indexable:
- Its main intent is clear and not a near-duplicate of another market page.
- It answers the reader's decision question with specific, current, sourced facts.
- Material claims have dated primary sources and uncertainty is stated.
- No unperformed deposit, withdrawal, account, support or gameplay test is described as completed.
- Promotional terms include key limitations and are not presented as guaranteed value.
- Commercial links are disclosed and do not determine editorial score.
- Responsible-gambling support and local complaint routes are visible.
- An editor who did not compile the evidence reviews the finished page.
- A last-reviewed date reflects an actual review, not a template date.
- Pages with unresolved legal or material factual gaps remain HOLD and are excluded from public navigation and sitemap.

## Workstream E — search measurement

Use Search Console and server/build evidence as separate signals:
- Crawlability: HTTP status, canonical, robots, sitemap membership and internal links.
- Indexing: Search Console URL Inspection / Pages report; a sitemap submission is not proof of indexation.
- Performance: impressions, clicks, CTR and average position by query/page/country, assessed over meaningful time windows.
- Quality: helpfulness, source freshness, original observations, corrections and reader task completion.
- Business: affiliate clicks and conversion only where legally allowed, consented, disclosed and measured responsibly.

Do not promise a traffic target or infer indexation from a successful fetch. Avoid repeated URL submissions as a ranking tactic; fix the underlying content and technical issue instead.

## Next concrete batch

1. Establish a reproducible local/CI build and crawl check.
2. Fix any build or sitemap/link errors revealed by that check.
3. Create genuinely useful market/legal hubs with current official citations.
4. Complete one brand evidence pack end-to-end, including independent review, before scaling the template.
5. Update the verification ledger only with evidence and actual sign-off.
6. Run release QA, obtain explicit owner approval, then deploy one tested release.

**Current gate:** approved brand reviews remain 0/100 until the ledger and evidence records say otherwise. This document itself does not change that count.


## Live release-gate snapshot — 22 October 2026

This section records a direct production/preview check and must be refreshed before any release. It is not an indexation claim.

| Check | Observed result | Release implication |
|---|---|---|
| Production `/robots.txt` | Fetch succeeds; `User-agent: *`, `Allow: /`, and canonical sitemap URL present | Crawler directives do not globally block crawling in the fetched file; still inspect response headers and page-level robots directives |
| Production `/sitemap.xml` | Valid-looking XML response labelled 44 URLs; does not include `/markets/` | Sitemap is stale relative to the market-hub candidate |
| Production `/markets/` | HTTP 404 at check time | Candidate page is not live; do not submit it for indexing or claim it is published |
| PR #37 preview `/markets/` | Page renders; title, description, Open Graph and canonical observed; canonical targets the production apex URL | Preview content/metadata check passed, but canonical is expected to point to production and is not evidence of production availability |
| PR #37 preview sitemap | 45 URLs; includes `https://beincasinos.online/markets/` | Sitemap candidate differs from production by one URL; verify XML, uniqueness, status, canonical and robots for all entries before release |
| PR #37 CI | GitHub Actions “Static site checks” run #1178 succeeded on head `403a61c` | CI success does not replace crawl/link/accessibility/public-artifact checks |
| PR #35 CI and preview | Static site checks run #1179 succeeded on head `2058035`; Cloudflare preview succeeded | Sisal evidence remains internal and on HOLD; build success is not brand approval |

### Required next actions before the single production deploy

1. Re-run a clean build and a full internal-link crawl against the exact release commit; include the full list of failures and fixes.
2. Parse both production and candidate sitemaps as XML; compare the URL inventory, verify uniqueness and canonical host, and check every URL's HTTP status, redirects, page-level robots and canonical target.
3. Inspect all generated files for unpublished brand drafts, internal evidence packs, private data, environment values and credentials. Internal Sisal evidence must not be reachable from the public output.
4. Verify the root and `www` host behaviour, HTTP-to-HTTPS redirects, trailing-slash policy, query-string canonicals, unknown-path 404, metadata, structured data, keyboard navigation and mobile layout.
5. Keep PR #37 draft until the release candidate passes these checks. Merge/deploy only through the owner-approved one-deploy release plan.
6. After deployment, immediately verify `/markets/`, production sitemap and robots, key pages, canonical/redirect behaviour, and Search Console sitemap/URL inspection. A successful fetch or submitted URL is not proof of indexing.
7. Keep the brand ledger unchanged unless a specific profile passes all evidence gates and an independent second reviewer plus legal/editorial sign-off is recorded.

**Status at this snapshot:** the market hub is available on preview but not on production; the production route returns 404. Approved brand reviews remain 0/100. No production deploy was performed by this QA pass.

## Sitemap URL fetch sweep — 22 October 2026

A live fetch sweep was run across all 44 URLs listed in the production sitemap at the time of checking.

- **44/44 URLs fetched without a per-URL fetch error** in the QA tool.
- Each returned the same final URL that was requested; no redirect was observed in this sweep.
- All 44 extracted pages returned visible text, a title, and a canonical URL matching the requested sitemap URL.
- The separate `/markets/` check still returned 404 and is not in the production sitemap.
- This is a page-fetch/metadata sweep, not a complete HTTP status-code audit, internal-link crawl, accessibility test, legal review, or Google indexing confirmation.

### Release decision

The existing sitemap pages passed this limited fetch/canonical sample. The overall release remains **HOLD** because PR #37 is not in production and `/markets/` is 404; PR #35 Sisal evidence remains internal/HOLD; full internal-link/public-artifact/accessibility and final release checks are still required. Do not deploy until the approved single-release plan is ready.

## Host canonicalisation and 404 checks — 22 October 2026

Live fetches confirmed these requested variants all resolve to `https://beincasinos.online/` and expose the apex canonical URL:

- `http://beincasinos.online/`
- `https://www.beincasinos.online/`
- `http://www.beincasinos.online/`

A deliberately nonexistent path, `/this-route-should-not-exist-qa-20261022/`, returned 404 as expected. The market hub `/markets/` separately still returns 404 because it is not yet released.

This check supports host canonicalisation and unknown-path handling at the homepage level. It does not establish the exact redirect status code or validate every path/query-string combination.

## Public artifact provenance guard — 22 October 2026

GitHub Actions run #1183 completed successfully on roadmap head `e2b4e79` and stored artifact `beincasinos-public-site-dist` (artifact ID `12436799005`, SHA-256 `a44ce9a114e0b1d5c5dcaec02b7d286c6380ac8945dfe77de7d0274ad8225a7f`, expiry 29 October 2026). It passed the HTML/local-link, schema/regression, JavaScript, host-config, public-only build, internal-file exclusion and Chromium smoke-test steps.

**Important:** this artifact was built from PR #36's roadmap branch and does **not** contain PR #37's new `/markets/` hub. It is not the release artifact for the intended combined site. Do not deploy or promote it as the final candidate. The release artifact must be rebuilt from the exact approved commit that includes all approved changes, and its SHA/contents must be verified before the one production deployment.

## Release-gate recheck — 22 October 2026 (latest pass)

A fresh production fetch checked the homepage, `/robots.txt`, `/sitemap.xml`, `/reviews/`, and `/markets/`.

- The homepage and review directory returned visible content and self-consistent apex canonical metadata.
- The fetched `robots.txt` content says `User-agent: *`, `Allow: /`, and identifies `https://beincasinos.online/sitemap.xml`. This fetch confirms the published text currently allows crawling; it does not test every CDN response header or every URL's robots directives.
- Production `/sitemap.xml` still identifies 44 URLs and does not include `/markets/`.
- Production `/markets/` still returns 404; the preview route must not be represented as live production content.
- PR #37 CI run #1184 completed successfully on head `2b2c1ae`, including Chromium browser smoke tests for 35 routes, responsive widths and axe checks.
- PR #36 CI run #1185 completed successfully on head `1fc47cb`, including Chromium browser smoke tests and public-only artifact exclusion checks.
- Both PRs remain open and draft. No production deployment was performed.

### Updated decision

Crawlability text at the root appears open, but the overall release remains **HOLD**. Do not submit `/markets/` for indexing while it returns 404. Before the single deployment, rebuild from the exact reviewed combined commit, validate that artifact contains the hub and excludes all internal drafts/evidence, parse and compare the sitemap, and complete the final production release checklist. Approved brand reviews remain **0/100**; CI success does not convert any candidate into an approved review.


## Live production recheck — 23 October 2026 (supersedes the earlier stale-404 snapshot)

A fresh uncached fetch of the production routes now shows the market hub is live and the earlier `/markets/` 404 snapshot is stale:

- `https://beincasinos.online/markets/` returned the expected market-rules page with title, description, visible body content and canonical `https://beincasinos.online/markets/`.
- `https://www.beincasinos.online/markets/` resolves to the apex HTTPS route and the page declares the same apex canonical.
- `https://beincasinos.online/markets/index.html` resolves to the canonical trailing-slash route.
- `https://beincasinos.online/sitemap.xml` currently contains **45 URLs** and includes `https://beincasinos.online/markets/`.
- `https://beincasinos.online/robots.txt` is reachable and contains `User-agent: *`, `Allow: /` and the canonical sitemap URL.

This verifies the current route, metadata/canonical and sitemap membership at fetch time. It does **not** prove Google has indexed the page, validate every sitemap URL, test all HTTP response headers, or replace Search Console URL Inspection. The old 22 October observations remain as historical snapshots and should not be read as current state. The full release gate remains HOLD until the exact final artifact, whole-site checks and brand/editorial approvals are complete.


## Full live sitemap fetch sweep — 23 October 2026

The current production sitemap was fetched and its **45 URLs** were checked in live batches. Results: **45/45 returned extracted page content without a fetch error; 45/45 had a title; 45/45 exposed a canonical matching the requested URL; zero redirects were observed; zero canonical mismatches; zero pages fell below 500 extracted characters**. The separate guide-hub link sweep also checked 30 linked guide URLs with no fetch errors or canonical mismatches.

This is a live content/metadata fetch audit, not a substitute for HTTP-status tooling, XML parser validation, response-header checks, structured-data validation, browser accessibility testing, Search Console URL Inspection, or proof of indexing. A fetch returning content does not prove a URL is indexed. Preserve the publication and legal/editorial gates; approved casino reviews remain 0/100.
