# Batch 16 — Post-release smoke-test results and remaining readiness gaps
Date: 2026-10-25
Status: robots correction confirmed live by fresh public fetch.

## Confirmed production result
A fresh public fetch returned the following from both `https://beincasinos.online/robots.txt` and `https://beincasinos.pages.dev/robots.txt`:
```text
User-agent: *
Allow: /
Sitemap: https://beincasinos.online/sitemap.xml
```
This confirms the previous site-wide `Disallow: /` is no longer present in the live responses. Source change was committed to main as `50ebe6115b293053cacffa53cca2d0f87d032b94`. This verifies the robots response only; it does not certify every URL or indexing.

## Smoke-test observations
- Homepage fetch succeeded and reports canonical `https://beincasinos.online/`.
- Reviews directory fetch succeeded and reports canonical `https://beincasinos.online/reviews/`.
- Sitemap fetch succeeded and currently reports 146 URLs.
- Representative review `/reviews/bet365-casino-gb/` fetched successfully and reports canonical `https://beincasinos.online/reviews/bet365-casino-gb/`.
- The representative bet365 page is explicitly “Not rated — no hands-on testing”; it provides source-led facts, but time-sensitive offer terms require rechecking.
- The directory says there are 100 market research profiles but also says no casino profiles are currently scored or ranked. This is a material distinction: 100 URLs/profiles do not mean 100 completed reviews.

## Important coverage gaps still visible
- The current directory filters cover Belgium, Canada — British Columbia, Germany, Great Britain, Italy, Netherlands, Spain, Sweden, Switzerland and United States — Michigan.
- Australia and France do not appear in the current directory's market filter. Do not present the 12-market plan as complete until those markets have eligible, source-backed profiles or are explicitly held due to legal/product restrictions.
- Several profiles remain “Not rated” and “Current bonus not verified.” Keep those labels until the evidence record is complete.
- The current sitemap includes multiple Spain-specific profiles and some sports/poker-related brand profiles. Confirm exact product category, domain, canonical and relevant authorisation before describing them as casino reviews.
- Search Console indexing remains unverified in this smoke test. A 200 response and sitemap inclusion are not indexing confirmation.

## Next release priorities
1. Audit all 146 sitemap entries for HTTP status, canonical, robots/noindex, duplicate intent, title/H1 uniqueness and product/market mismatch.
2. Reconcile the public directory and sitemap: keep only defensible, distinct, useful URLs; remove/redirect true duplicates and hold unsupported profiles.
3. Build a per-brand evidence ledger and finish exact operator/domain/product/market checks.
4. Capture current terms, bonus, payment and safer-gambling sources for each page; keep offer amounts hidden where terms conflict or cannot be fetched.
5. Add the missing target-market coverage only from official regulator/operator evidence; never fill a quota with unverified brands.
6. Run a production build/smoke test through the existing Cloudflare Pages pipeline, avoiding unnecessary GitHub Actions.
7. In Search Console, inspect representative URLs and monitor indexed, crawled-not-indexed, discovered-not-indexed and impressions separately.

## Scope boundary
This record confirms a crawler-directive fix and representative fetches. It does not assert 100 completed reviews, 100 legally eligible brands, 146 valid indexable pages, or any number of Google-indexed URLs.
