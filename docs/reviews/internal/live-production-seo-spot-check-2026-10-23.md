# Live production SEO spot-check — 2026-10-23

**Scope:** Public HTTP fetches of BeInCasinos homepage, robots.txt, sitemap.xml, www homepage, review directory and market directory.  
**Important limitation:** The fetch tool exposed final URLs and page content/metadata but did not expose raw HTTP status codes or complete response headers. No Search Console access was used.

## Observed results

| Check | Observation | Result |
| --- | --- | --- |
| `https://beincasinos.online/` | Page returned readable HTML content; canonical and Open Graph URL both point to the HTTPS apex homepage. | PASS for fetch and canonical metadata |
| `https://www.beincasinos.online/` | Final URL resolved to `https://beincasinos.online/`; same homepage content and canonical. | Redirect observed; permanence/status code not independently verified |
| `https://beincasinos.online/robots.txt` | Allows all crawlers with `User-agent: *`, `Allow: /`; declares `https://beincasinos.online/sitemap.xml`. | PASS for visible directives |
| `https://beincasinos.online/sitemap.xml` | Live page identifies 45 URLs; URLs are HTTPS apex-host URLs and include `/markets/`. | Live sitemap fetch succeeded |
| `https://beincasinos.online/reviews/` | Canonical points to the page itself. Page explicitly says the directory is in development and no casino profiles are currently scored or ranked. | Accurate public disclosure; target of 100 approved reviews is not yet achieved |
| `https://beincasinos.online/markets/` | Canonical points to the page itself; page describes itself as a market-rule and regulator directory, not a casino ranking. | PASS for observed canonical and scope disclosure |
| Representative guide pages | `/guides/brand-name-vs-legal-operator/` and `/guides/how-to-check-a-casino-licence/` return readable content with self-referencing canonical and Open Graph URLs. | PASS for spot-check only |

## Repository sitemap drift found and corrected on the working branch

The repository `sitemap.xml` snapshot contained **44 unique URLs**, while the live sitemap reports **45 URLs**. The known difference is `https://beincasinos.online/markets/`, present in production but missing from the working-branch sitemap snapshot.

The working-branch sitemap has now been updated to include `/markets/`, bringing its declared URL count to 45. This is a repository correction only; it does not deploy the change or prove the live sitemap is now generated from this branch.

Other repository snapshot facts: 44 URLs were unique; 17 had `lastmod` values and 27 did not. Missing `lastmod` is not automatically an indexing error; do not invent dates. Keep dates only where supported by a substantive update.


## Additional page sample — 10 priority routes

A second live fetch checked these routes: `/guides/`, `/market-research/`, `/about/`, `/how-we-review/`, `/editorial-policy/`, `/affiliate-disclosure/`, `/privacy/`, `/terms/`, `/responsible-gambling/`, and `/tools/terms-checklist/`.

**Observed result:** all 10 returned readable page content, each fetch ended at the requested apex HTTPS URL, and each exposed a self-referencing canonical URL matching the requested page. No per-URL fetch errors were returned. This is a positive spot-check, not a full crawl and not a substitute for HTTP status/header capture, link validation or legal review.

## Remaining verification gaps

- Obtain raw HTTP status codes, redirect chain and content type for HTTP/HTTPS and apex/www variants using a trusted direct HTTP check.
- Verify the permanent redirect behaviour rather than inferring it from the final URL alone.
- Compare all 45 live sitemap URLs with their final status, canonical, robots directives and page content; this spot-check did not validate every URL.
- Inspect Search Console for sitemap processing, indexed URLs, exclusions, queries, impressions and clicks. No Search Console result is claimed.
- Continue the 100-brand evidence pipeline; the public review directory confirms no scored/ranked casino profiles currently exist.

## Decision

**Partial pass for crawl discovery and sampled canonical metadata. Full production SEO verification remains open.** No deployment or Actions workflow was triggered as part of this audit.

## Source URLs

- https://beincasinos.online/
- https://www.beincasinos.online/
- https://beincasinos.online/robots.txt
- https://beincasinos.online/sitemap.xml
- https://beincasinos.online/reviews/
- https://beincasinos.online/markets/
- https://beincasinos.online/guides/brand-name-vs-legal-operator/
- https://beincasinos.online/guides/how-to-check-a-casino-licence/
- Google crawling and indexing FAQ: https://developers.google.com/search/help/crawling-index-faq
