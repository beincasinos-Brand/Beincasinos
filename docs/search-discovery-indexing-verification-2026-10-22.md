# Search discovery and indexing verification checklist — 22 October 2026

## Confirmed repository and CI facts

- Canonical host intended by source files: `https://beincasinos.online/`.
- `robots.txt` allows all user agents and advertises `https://beincasinos.online/sitemap.xml`.
- The source-controlled and live production sitemap now list 44 canonical URL entries, including `/guides/alternative-dispute-resolution-gambling/` and `/guides/what-a-gambling-licence-means/`. This is a submitted/discovery inventory, not evidence that Google indexed any URL.
- The licence-guide integrated source/build/browser workflow passed on commit `e2a9e628908a4454dc73543113a32d5060175140`: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39745520599.
- Latest read-only Cloudflare diagnostic reported a valid API token, readable zone, Pages project `beincasinos`, production branch `main`, and active production deployments: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39697317005
- Live fetch verification found `https://www.beincasinos.online/` resolves to `https://beincasinos.online/`. This confirms the observed redirect path, not Google indexing.
- Read-only Search Console connector check on 22 October 2026: `https://beincasinos.online/` property is connected. The submitted sitemap record reports 32 submitted URLs, 0 errors, 0 warnings, last submitted `2026-10-21T21:39:13Z`, and last downloaded `2026-10-21T21:39:14Z`. Production sitemap now contains 44 URLs, so the sitemap should be resubmitted in Search Console and its status rechecked. The connector's `indexed` field is marked deprecated and returned 0; do not treat that field as a reliable current index count. Search Analytics queries returned no rows for the last 12 months, which does not by itself establish a true zero-impressions verdict; inspect the property directly in Search Console.

## Owner/browser steps — Search Console

1. Open the correct Google Search Console property for `https://beincasinos.online/` (or its verified Domain property).
2. Open **Sitemaps** and submit `https://beincasinos.online/sitemap.xml` if the current 43-URL sitemap has not been submitted.
3. Record the submission timestamp and the exact status/error shown. A successful fetch means Google can read the sitemap; it does not mean all listed URLs are indexed.
4. Inspect these representative URLs one at a time:
   - `https://beincasinos.online/`
   - `https://beincasinos.online/guides/`
   - `https://beincasinos.online/guides/documenting-withdrawal-delay/`
   - `https://beincasinos.online/tools/wagering-calculator/`
5. For each URL, record Google's exact verdict: URL on Google / not on Google; crawl allowed; fetch result; indexing allowed; declared canonical; Google-selected canonical; last crawl; and any page-specific reason.
6. Open **Indexing → Pages** and capture counts plus the top exclusion/error reasons. Prioritise fixes for accidental `noindex`, blocked resources, server errors, redirects, duplicate/canonical conflicts, and soft 404s. Do not attempt to force-index every URL if Google identifies a duplicate or low-value page.
7. Request indexing only after a meaningful fix or publication. Repeated requests do not increase priority or guarantee indexing.

## Live host and canonical checks

Test the following URLs from a normal browser or a trustworthy HTTP checker, recording status code, final URL, and response headers:

- `https://beincasinos.online/` — expected 200 and self-canonical.
- `https://www.beincasinos.online/` — live fetch resolved to `https://beincasinos.online/` at the last check; periodically recheck the redirect.
- `http://beincasinos.online/` and `http://www.beincasinos.online/` — expected HTTPS redirect to the canonical host.
- `https://beincasinos.online/robots.txt` — expected 200 and crawl policy matching the source file.
- `https://beincasinos.online/sitemap.xml` — expected 200, valid XML, canonical HTTPS host, no redirected/non-canonical URLs, and only existing indexable pages.

Do not change nameservers or DNS records based only on an A/CNAME lookup. Confirm current records and actual HTTP behavior first; keep the existing configuration if the tests pass.

## Reporting standard

Keep these concepts separate in every report:

- **Published:** a page exists in source or on the live host.
- **Discovered:** Google has found the URL.
- **Crawled:** Google fetched the URL.
- **Indexed:** Google selected the URL for its index.
- **Visible:** Search Console reports impressions/clicks for queries and pages.

Never infer indexing, ranking, impressions, or traffic from a passing build, a live HTTP 200, or sitemap membership. Do not claim a traffic target is achieved until Search Console data supports it.

## Latest production verification — 22 October 2026

- Verified `https://beincasinos.online/guides/what-a-gambling-licence-means/` is live and returns the expected page metadata with a self-canonical URL.
- Verified `https://beincasinos.online/sitemap.xml` is live and reports 43 URLs, including the new guide.
- Verified `https://www.beincasinos.online/` resolves to the apex host in a live fetch. This does not prove Google has indexed the site or any specific URL.

## Search Console connector readout — 22 October 2026

- The read-only connector can access the `https://beincasinos.online/` Search Console property.
- Sitemap record: `https://beincasinos.online/sitemap.xml`; 32 submitted URLs; 0 errors; 0 warnings; last submitted 21 October 2026 at 21:39:13 UTC; last downloaded 21:39:14 UTC.
- The live sitemap was verified to contain 44 URLs after the ADR guide release. The 32-URL submission record is stale relative to the current sitemap. Submit `sitemap.xml` again in Search Console and verify the updated submitted count/status. The connected connector is read-only and exposes no sitemap-submission action, so this step has not been performed automatically.
- The connector exposes an `indexed` sitemap field marked deprecated and returned 0; do not report this as a reliable current indexed-page count.
- Search Analytics requests for daily clicks, impressions, CTR and position returned no rows for the last 12 months. This is an empty connector result, not proof of exactly zero impressions; validate directly in Search Console, including the property, date range, and search type.
- URL Inspection verdicts, Google's selected canonicals, and Pages indexing/exclusion reasons remain unverified.


## ADR guide production verification — 22 October 2026

- PR #12 was merged as commit `64e4b83a592884da5457082c2d9f25c5319362af`; integrated Static site checks passed, including Chromium browser smoke tests: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39747923664.
- Production guide library links to `/guides/alternative-dispute-resolution-gambling/` and live `sitemap.xml` lists 44 canonical URLs including this guide.
- The clean canonical route intermittently returned a cached 404 to the external fetch checker, while a cache-busted request and `index.html` route loaded the guide with the expected title, metadata and self-canonical. Treat this as a cache/edge consistency issue to clear and recheck, not as proof of stable clean-route availability. Do not claim route QA fully passed until the clean URL consistently returns the guide.
- Search Console connector still reports the older sitemap submission as 32 URLs (last submitted 21 October 2026 21:39 UTC), with 0 errors/warnings. Resubmit the current 44-URL sitemap in the Search Console UI; connector is read-only and no submission was made.
- Search Analytics returned no rows for the last 12 months; this does not prove exactly zero impressions. URL Inspection, selected canonical, and Pages exclusion reasons remain unverified.
