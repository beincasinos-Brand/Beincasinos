# BeInCasinos technical SEO release checklist

**Date:** 23 October 2026
**Status:** Pre-release checklist; no production audit or deployment is claimed by this document.
**Constraint:** Avoid unnecessary GitHub Actions runs while the account's Actions-minute allowance is low.

## 1. Crawl and index eligibility
- [ ] Confirm production hostname and one canonical URL convention (HTTPS, preferred host, trailing-slash rule).
- [ ] Test HTTP and HTTPS variants plus www/non-www variants; every alternate must redirect in one hop to the preferred URL.
- [ ] Confirm redirects are server-side permanent redirects where appropriate; no redirect loops or chains.
- [ ] Confirm every intended public page returns HTTP 200 and has useful, unique content.
- [ ] Confirm drafts, internal research, staging pages, filters, search results and thin archives are not indexable.
- [ ] Check robots.txt does not accidentally block important CSS/JS or intended public pages.
- [ ] Check meta robots and X-Robots-Tag for accidental noindex on intended pages.
- [ ] Check canonical tags are absolute, self-referential on canonical pages and consistent with internal links and sitemap.
- [ ] Ensure canonical URLs do not point to redirects, errors, irrelevant pages or different market variants.
- [ ] Verify XML sitemap returns 200, valid XML and contains only canonical, indexable, useful URLs.
- [ ] Exclude redirect URLs, 404/410 pages, noindex pages, internal drafts and duplicate parameter URLs from sitemap.
- [ ] Ensure sitemap lastmod changes only when material page content changes; never fabricate freshness.
- [ ] Validate breadcrumbs and internal links; remove orphaned high-value pages.
- [ ] Check pagination/facets do not create uncontrolled URL duplication.
- [ ] Verify public pages render meaningful main content without relying on blocked or failed client scripts.

## 2. Page-level quality
For each proposed public review page:
- [ ] Correct country and product are stated near the top.
- [ ] Exact legal operator, licence and domain are sourced to the regulator and current first-party terms.
- [ ] Current offer terms are fully checked or the offer is omitted.
- [ ] Payment policy and observed payment performance are clearly distinguished.
- [ ] Historic regulatory action is attributed to the named licensee and date, with the regulator's scope/context.
- [ ] Safer-gambling, complaints and ADR details are current and market-specific.
- [ ] No unsupported score, fake hands-on testing, fake user reviews or guarantees.
- [ ] Named author/reviewer, fact-checker, last checked date, correction route and affiliate disclosure are visible.
- [ ] Title, H1, meta description and Open Graph fields are unique and accurately describe the page.
- [ ] Internal links are useful and descriptive; no forced exact-match anchor repetition.
- [ ] Structured data matches visible content and uses only eligible schema types.
- [ ] Images have appropriate alt text, sensible dimensions and no unlicensed competitor assets.
- [ ] Mobile layout, keyboard access, contrast and core content are usable.
- [ ] Page has a clear purpose and unique value beyond swapped brand names.

## 3. Market and compliance gates
- [ ] Regulator confirms active permission for the exact product and market.
- [ ] Domain/trading name maps to the legal entity in current official records.
- [ ] Current first-party terms identify the contracting party and jurisdiction.
- [ ] Unresolved entity or market status means HOLD; do not add to best lists or affiliate promotions.
- [ ] Affiliate relationships are disclosed near commercial links and in the global policy.
- [ ] Commercial agreements cannot alter factual findings or score.
- [ ] Safer-gambling messaging is not removed or weakened for conversion.
- [ ] Internal research documents stay out of public routes, navigation and sitemap.

## 4. Performance and accessibility
- [ ] Measure mobile Core Web Vitals using field data when available; lab scores alone are not field performance.
- [ ] Inspect largest contentful paint, interaction to next paint and cumulative layout shift.
- [ ] Compress and size images appropriately; lazy-load below-the-fold images but not the primary LCP image.
- [ ] Avoid unnecessary third-party scripts and affiliate widgets that block rendering.
- [ ] Check semantic headings, accessible names, keyboard focus and link purpose.
- [ ] Verify no horizontal overflow on small screens.
- [ ] Test common Android mobile viewport sizes as well as desktop.

## 5. Search Console and measurement
- [ ] Confirm the correct Domain property or URL-prefix property is verified.
- [ ] Inspect representative canonical pages with URL Inspection; compare user-declared and Google-selected canonicals.
- [ ] Submit the sitemap once after it is valid; repeated submission does not guarantee faster indexing.
- [ ] Record indexing status by page group: eligible reviews, guides, category pages and excluded drafts.
- [ ] Monitor Page indexing, Sitemaps, Manual actions, Security issues and Core Web Vitals reports.
- [ ] Maintain a weekly export of query/page/date/device/country impressions, clicks, CTR and average position.
- [ ] Separate branded from non-branded queries and segment by country and page template.
- [ ] Investigate pages with impressions but low CTR, pages with no impressions, and query cannibalization.
- [ ] Treat indexing and ranking as outcomes to observe, not guaranteed results of a submission.

## 6. Release procedure without unnecessary Actions runs
1. Review the changed file list and ensure no internal review drafts are in public content directories.
2. Run local/static checks where available before invoking hosted CI.
3. Check the current Actions-minute balance and workflow trigger configuration.
4. Avoid repeatedly re-running successful or unrelated workflows.
5. If a build/deploy is needed, use the repository's documented deployment path and preserve logs.
6. After deployment, verify production status codes, redirects, canonicals, robots, sitemap and a sample of public pages.
7. Roll back if critical redirects, index directives, public content or data integrity are broken.
8. Record the deployed commit and verification evidence in the tracker.

## 7. Go/no-go criteria
**NO-GO** if any of these are true:
- Preferred domain/redirect chain is unresolved.
- Sitemap includes drafts, redirecting URLs, errors or noindex pages.
- Public review claims an unverified operator, licence, bonus, payout or hands-on test.
- Pages contain thin near-duplicates or unsupported structured data.
- Current market eligibility is uncertain.
- Internal notes, private material or unfinished review drafts are exposed publicly.

**GO** only when the intended URL set, legal-market checks, page-level evidence, canonical/indexability controls and production smoke checks pass. This checklist itself does not certify that any of those checks have already passed.
