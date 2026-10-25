# Live Recheck and Release Reconciliation — Batch 15
Date: 2026-10-25
Scope: live production crawl directive, homepage, review directory, and sitemap compared with repository state.
Status: fresh live fetch completed; this is an audit record, not a deploy.

## Fresh live findings

### 1. Live robots.txt currently allows crawling
Live URL: https://beincasinos.online/robots.txt
Observed body:
```
User-agent: *
Allow: /
Sitemap: https://beincasinos.online/sitemap.xml
```
This differs from the repository `main` branch file fetched during this audit, which still contains `Disallow: /`. The research branch contains the crawl-permissive version. This indicates production and the current main-branch source are out of sync, or production has been updated through another deployment/source. Do not assume which deployment is authoritative: reconcile Cloudflare Pages deployment commit, GitHub main, and live output before further release changes.

### 2. Homepage is reachable and describes the product conservatively
Live homepage: https://beincasinos.online/
- Title: “BeInCasinos — Casino Reviews & Research”
- Canonical reported by the page: `https://beincasinos.online/`
- Description emphasizes evidence-led review standards, operator checks, terms, withdrawals, and market-specific research.
- Homepage says profiles are desk research, not product tests, and that scores/promotional amounts are published only when supported by evidence.
- Navigation exposes reviews, market guides, editorial policy, responsible-gambling resources, disclosure, and contact/privacy/terms pages.
- A browser-content fetch succeeded. This is not a full browser rendering, accessibility, performance, or link-status audit.

### 3. Review directory is live but not a finished 100-review launch
Live URL: https://beincasinos.online/reviews/
- The page states “100” market research profiles and explicitly says no live casino profiles are scored or ranked.
- Sample profile cards use “NOT RATED”, “Pending verification”, and “Current bonus Not verified”.
- The directory's stated methodology is clear: exact domain/operator and market/product eligibility before scoring; six weighted criteria; unassessed criterion means no total score; affiliate commission/listing fees must not influence ratings.
- The 100 visible research profiles are not evidence that there are 100 distinct, verified, fully tested, publication-ready casino reviews.
- The visible market filter list includes Belgium, Canada—British Columbia, Germany, Great Britain, Italy, Netherlands, Spain, Sweden, Switzerland, and United States—Michigan. It does not visibly show Australia or France, even though both are in the current target-market plan. Audit directory filter and actual brand allocation against all 12 targets: AU, CA, GB, US, CH, DE, NL, SE, ES, IT, FR, BE.
- Many entries are Spain-focused. Deduplicate brands repeated across countries and separate casino products from sportsbook/poker products before reporting the unique-brand count.

### 4. Sitemap is reachable, but its URLs need reconciliation
Live URL: https://beincasinos.online/sitemap.xml
- Fetch succeeded and returned a long list of review, guide, policy, and tool URLs.
- A prior live audit recorded 146 sitemap URLs; recount from the latest raw XML before using that as a current exact count.
- For every URL, check HTTP status/final URL, canonical, robots/noindex, title/H1 uniqueness, content completeness, market/product eligibility, duplicate clusters, internal links, and inclusion rationale.
- A sitemap entry is only a discovery hint, not proof of Google indexing or quality.

## Release reconciliation actions (ordered)

1. In Cloudflare Pages, record the production deployment's source commit SHA and build status.
2. Compare that SHA to GitHub `main`; resolve why the live robots output currently differs from `main/robots.txt`.
3. Make the crawl-permissive robots policy part of the authoritative source of truth. Keep the sitemap URL canonical and HTTPS.
4. Run a static build using `python3 scripts/build_site.py` in a local/preview environment; do not trigger GitHub Actions just to check this.
5. Parse the live sitemap and create a URL-by-URL status table. Do not bulk-index stale, duplicate, thin, ineligible, or noindex draft routes.
6. Audit all 12 market filters and ensure each market has eligible candidates before publishing country-specific claims. Australia and France require especially careful product-category wording.
7. Keep all unsupported ratings and bonus amounts withheld. A profile can be published as clearly labelled, source-linked research only if its claims are supported and it adds distinct reader value.
8. After an authorized production deploy, re-fetch `robots.txt`, homepage, review directory, sitemap, and representative URLs; then inspect Google Search Console coverage and sitemap status. Request indexing only for priority pages that pass the gates.

## What this audit does not claim

- It does not certify 100 unique brands or 100 complete reviews.
- It does not prove Google indexed any particular URL.
- It does not claim account/deposit/withdrawal/game/support testing.
- It does not confirm a successful deployment or identify the production commit.
- It does not certify legal availability in all 12 target markets.

## Acceptance checklist

- [ ] Live production commit SHA recorded and matches approved GitHub source.
- [ ] Main-branch `robots.txt` and live `robots.txt` agree and permit intended crawling.
- [ ] Sitemap parses; every URL has an explicit KEEP / FIX / NOINDEX / REMOVE / REDIRECT decision.
- [ ] Canonicals, redirects, index directives and sitemap inclusion agree.
- [ ] Directory filters and profile inventory cover the 12 target markets without false claims.
- [ ] Brand-level duplicates and non-casino product scopes are resolved.
- [ ] Each published profile has dated primary-source evidence and a clear limitations section.
- [ ] Numeric scores are withheld unless every criterion and eligibility gate passes.
- [ ] Current bonus claims link to exact official terms and market eligibility.
- [ ] Mobile rendering, links, accessibility basics, metadata and structured data pass preview QA.
- [ ] Production recheck and GSC review completed after authorized release.

