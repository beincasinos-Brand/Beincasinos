# Production SEO verification plan

Date: 2026-10-23
Status: partial live spot-check completed on 2026-10-23; full URL-by-URL and Search Console verification remains open.

## First checks
1. Request the live homepage, robots.txt, sitemap.xml, and apex/www HTTP/HTTPS variants.
2. Record UTC time, HTTP status, redirect chain, final URL, content type, and response body.
3. Confirm one preferred HTTPS hostname and consistent permanent redirects from other variants.
4. Parse the live sitemap and compare its URLs with the repository version.
5. For each sitemap URL, check final status, canonical URL, robots directives, and visible main content.
6. Ensure the sitemap contains only final, intended, indexable URLs.
7. Check internal links, titles, descriptions, headings, and structured data against visible page content.
8. Confirm the live sitemap and homepage in Search Console after technical checks pass.

## Observed production evidence (2026-10-23)
- Live `robots.txt` was readable and contained `User-agent: *`, `Allow: /`, and the apex `sitemap.xml` URL.
- Live `sitemap.xml` was readable and reported 45 URLs.
- Fetching `https://www.beincasinos.online/` ended at `https://beincasinos.online/`; raw status codes and permanence were not exposed, so the redirect is observed but not fully verified.
- The live homepage, `/reviews/`, `/markets/`, and two guide pages exposed self-referencing canonical metadata.
- The live review directory explicitly says no casino profiles are currently scored or ranked.
- The branch sitemap had 44 URLs and omitted `/markets/`; the branch sitemap has now been corrected to 45 URLs. This does not itself deploy anything.
- Full evidence and limitations: [live production SEO spot-check](live-production-seo-spot-check-2026-10-23.md).

## Current blockers
- Previous Cloudflare API repair returned 401 / error 10000; do not claim it is fixed until raw HTTP status and redirect chain are checked.
- Not every sitemap URL has been tested for status, canonical, robots and content.
- No Search Console action or indexation report was obtained.

## Completion evidence
For each check, record the exact URL, UTC timestamp, observed status/result, and evidence reference. Mark a check complete only after observing the result.

## Official references
- https://developers.google.com/search/help/crawling-index-faq
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting
