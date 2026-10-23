# SEO and indexing evidence gates — 2026-10-23

**Purpose:** actionable internal gate list for BeInCasinos. This document is not evidence that the production site currently passes any check.

## Search visibility goals are not guarantees

Google's official documentation says sitemap submission helps discovery but does not guarantee crawling, indexing or rankings. Indexing depends on crawl accessibility, successful responses, indexable content, duplication/canonicalization, and content usefulness. Source: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap and https://developers.google.com/search/docs/essentials/technical

No one can responsibly promise 100 million daily impressions or top-10 rankings. Treat them as long-term aspirations and measure actual Search Console impressions, clicks, query coverage, indexed canonical URLs and qualified outcomes.

## Release checks (run against production and record actual results)

### 1. Domain and response behavior
- [ ] Confirm the preferred host and HTTPS behavior for apex and www; test redirect chains, final URLs and status codes.
- [ ] Ensure every intended landing page returns a real 200 response and not a soft 404.
- [ ] Check that no public route accidentally points to a preview/deployment host.
- [ ] Confirm no redirect loops or mixed canonical targets.

### 2. Crawl and index directives
- [ ] Fetch production robots.txt and verify important pages/assets are crawlable.
- [ ] Check page-level robots meta and X-Robots-Tag; ensure intended pages do not accidentally carry noindex.
- [ ] Confirm sitemap contains only canonical, indexable, public URLs that return success.
- [ ] Exclude internal evidence, draft, QA, admin and thin duplicate routes from public navigation and sitemap; use appropriate access controls or noindex policy rather than assuming robots.txt hides a URL from indexing.
- [ ] Confirm sitemap URLs use one host, HTTPS and canonical path conventions.

### 3. Canonicals, metadata and localization
- [ ] Every indexable page has an intentional self-referencing canonical or documented alternate strategy.
- [ ] Titles and meta descriptions are unique, descriptive and market-specific.
- [ ] Region/language pages have meaningful localized body content; use hreflang only where genuine alternates exist and cross-reference them correctly.
- [ ] Avoid near-identical city/country pages created only by swapping place names.

### 4. Content usefulness and trust
- [ ] Casino review pages include named legal operator, regulator/licence evidence, terms access date, dated bonus rules if covered, payments/withdrawals with evidence, limitations on testing, safer-gambling information and transparent scoring.
- [ ] Separate verified facts, operator claims, reviewer observations and unresolved items.
- [ ] Add original comparative insight and decision-useful tables only when supported by evidence.
- [ ] Remove fabricated first-hand language, generic filler, unsupported “best/safest/fastest” claims and unverified promotional terms.
- [ ] Provide clear author/reviewer credentials, editorial policy, affiliate disclosure, correction policy, contact details and responsible-gambling resources.

### 5. Technical and measurement
- [ ] Validate structured data against the visible page and applicable Google feature rules; never add ratings or offers that are not shown and supported.
- [ ] Test mobile layout, keyboard access, performance and internal crawlable links.
- [ ] Record production test date, URLs sampled, status/canonical/index directives and tool outputs in a release artifact.
- [ ] Check Search Console URL Inspection and Page Indexing for canonical selection and indexing reasons; check Performance by query/page/country/device after enough data accrues.
- [ ] Use an agreed reporting window and baseline; do not infer success from a sitemap submission or a single site: search.

## Stop conditions
Do not publish a brand review while its current market-specific contracting operator, licence/domain match, terms and claim sources remain unresolved. Do not run a production deploy or expensive CI merely to publish internal research. Do not count an internal draft as a live URL or an approved review.

## Current project status
This is a control document. No production crawl, Search Console mutation, deploy or indexation verification is claimed by this commit.
