# Production SEO verification plan

Date: 2026-10-23
Status: internal checklist only; no production or Search Console result is claimed.

## First checks
1. Request the live homepage, robots.txt, sitemap.xml, and apex/www HTTP/HTTPS variants.
2. Record UTC time, HTTP status, redirect chain, final URL, content type, and response body.
3. Confirm one preferred HTTPS hostname and consistent permanent redirects from other variants.
4. Parse the live sitemap and compare its URLs with the repository version.
5. For each sitemap URL, check final status, canonical URL, robots directives, and visible main content.
6. Ensure the sitemap contains only final, intended, indexable URLs.
7. Check internal links, titles, descriptions, headings, and structured data against visible page content.
8. Confirm the live sitemap and homepage in Search Console after technical checks pass.

## Current blockers
- Previous Cloudflare route repair returned API 401 / error 10000; do not call it fixed until raw production responses verify the redirect.
- The repository sitemap snapshot is not proof of live production or indexation.
- No Search Console action or production validation is recorded in this plan.

## Completion evidence
For each check, record the exact URL, UTC timestamp, observed status/result, and evidence reference. Mark a check complete only after observing the result.

## Official references
- https://developers.google.com/search/help/crawling-index-faq
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- https://developers.google.com/search/docs/crawling-indexing/canonicalization-troubleshooting
