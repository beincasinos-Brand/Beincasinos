# Search discovery and indexing verification checklist — 22 October 2026

## Confirmed repository and CI facts

- Canonical host intended by source files: `https://beincasinos.online/`.
- `robots.txt` allows all user agents and advertises `https://beincasinos.online/sitemap.xml`.
- The source-controlled sitemap currently lists 42 URL entries. This is a submitted/discovery inventory, not evidence that Google indexed any URL.
- Latest integrated source/build/browser workflow passed on commit `08e984464e0d8081ca4ae8c6f26e1b31cba7716f`: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39697317267
- Latest read-only Cloudflare diagnostic reported a valid API token, readable zone, Pages project `beincasinos`, production branch `main`, and active production deployments: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39697317005
- DNS A lookups returned Cloudflare addresses for both apex and `www`. The `www` CNAME query returned no answer; this alone does not prove a DNS fault because proxied records may be represented differently. An HTTP redirect test is still required.
- No current Search Console URL Inspection result or successful current sitemap submission is established by these CI results.

## Owner/browser steps — Search Console

1. Open the correct Google Search Console property for `https://beincasinos.online/` (or its verified Domain property).
2. Open **Sitemaps** and submit `https://beincasinos.online/sitemap.xml` if the current sitemap has not been submitted since the 42-URL inventory was published.
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
- `https://www.beincasinos.online/` — expected permanent redirect to `https://beincasinos.online/`.
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