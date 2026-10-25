# Live Technical Launch Audit — Batch 09
Date: 2026-10-25
Scope: public production URLs + GitHub source comparison
Status: findings verified; proposed robots correction is on research branch only and is not live until reviewed/merged/deployed.

## Critical finding: production robots blocks all crawling
Live URL checked: https://beincasinos.online/robots.txt
Observed body:
```
User-agent: *
Disallow: /
Sitemap: https://beincasinos.online/sitemap.xml
```
The main-branch file `robots.txt` matches this rule exactly (blob SHA observed: cdf074dae628e4b29e1cadfe930548f73b3f69ae). This is a site-wide crawl block. It does not guarantee URLs are absent from the index, but it prevents compliant crawlers from fetching pages while active. This is a launch blocker if the intention is to make the public site discoverable in search.

## Sitemap check
Live URL: https://beincasinos.online/sitemap.xml
- Fetch succeeded; the sitemap declares 146 URLs.
- Includes homepage, reviews directory, review pages, guides, tools and policy pages.
- Sitemap presence is not proof of crawling or indexing. With `Disallow: /` active, the sitemap and robots directives conflict operationally: URLs are submitted but crawling is blocked.
- Recheck XML parsing, canonical hosts, HTTP status, redirects, noindex, internal linking and Search Console coverage after the robots fix is deployed.

## Public review-directory spot check
Live URL: https://beincasinos.online/reviews/
- Directory exposes numerous profiles, but its own editorial status text says no casino profiles are currently scored or ranked and numeric ratings are withheld until eligibility/evidence/editorial checks pass.
- Multiple visible cards correctly say “NOT RATED”, “Editorial score Pending verification”, and “Current bonus Not verified”. Do not replace these with invented ratings, stars or bonus amounts.
- A large share of the listed URLs are Spain profiles, while the intended target set is AU, CA, GB, US, CH, DE, NL, SE, ES, IT, FR, BE. The sitemap sample includes some legacy/market-specific URLs; perform a complete distribution/deduplication review before declaring the 100-brand target finished.
- Profiles in the sitemap include names associated with different product categories (for example poker or betting brands); confirm casino-specific authorisation and do not infer casino permission from a sports/poker record.

## Proposed correction prepared for review
Candidate robots policy for the public launch:
```
User-agent: *
Allow: /

Sitemap: https://beincasinos.online/sitemap.xml
```
This only removes the site-wide crawl block. It does not grant indexing, rankings, or legal permission. Keep internal evidence docs out of the public build; verify that generated public output does not contain internal `docs/` files. Ensure pages intended to stay private are protected independently, not by robots.txt.

## Required post-merge/deploy checks
1. Fetch live `/robots.txt` and confirm `Disallow: /` is gone.
2. Fetch sitemap and confirm valid XML, canonical HTTPS host, no staging URLs and correct count.
3. Test a representative sample from each of the 12 target markets for HTTP 200, self-canonical, indexability, visible unique content, accurate market/product label and internal links.
4. Verify Google Search Console sitemap processing and URL Inspection after the live change; do not claim indexed until GSC reports it.
5. Confirm `www` host behaviour and canonical/redirect consistency.
6. Run the production build and test the built output before merging. Avoid repeated deploys; do one launch candidate only after all blockers are addressed.

## Scope/limitations
This is a bounded live check, not a full crawl of all 146 URLs or a Search Console inspection. It does not establish how many URLs Google has indexed. No production changes or deployment were performed by this audit.
