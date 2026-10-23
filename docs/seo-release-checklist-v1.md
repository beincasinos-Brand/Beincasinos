# BeInCasinos — SEO release checklist v1

**Purpose:** verify technical and editorial readiness before releasing new pages. This is a checklist, not proof that the site is indexed or receiving impressions.

## A. URL and crawlability
- [ ] Each intended public page returns HTTP 200 without a redirect chain.
- [ ] Canonical URL is absolute, self-referential, and matches the preferred HTTPS hostname.
- [ ] No accidental `noindex`, blocked robots rule, or authentication wall on public pages.
- [ ] Internal links use the canonical URL and do not lead to 404/5xx responses.
- [ ] XML sitemap contains only canonical, indexable, successful URLs.
- [ ] Sitemap is reachable and submitted in Google Search Console.
- [ ] Robots.txt is reachable and does not block required CSS/JS or public page paths.
- [ ] Redirects from renamed URLs are one-hop and point to the closest relevant destination.
- [ ] Locale/country variants have correct canonical and hreflang annotations where applicable.

## B. On-page content
- [ ] One descriptive H1 per page; heading hierarchy is meaningful.
- [ ] Title and meta description are unique and match the actual page intent.
- [ ] Main content is visible in rendered HTML and useful without requiring client-only interaction.
- [ ] Pages provide first-hand research, clear sourcing, update dates and limitations.
- [ ] Claims about prices, terms, availability, rankings or regulatory status are dated and source-linked.
- [ ] Similar pages have distinct value; avoid thin location/keyword permutations.
- [ ] Editorial byline, methodology, corrections contact and ownership disclosures are accessible.
- [ ] Internal links connect related pages naturally; avoid orphan pages.

## C. Structured data
- [ ] Structured data matches visible page content exactly.
- [ ] Use only schema types supported by the page; do not fabricate ratings, reviews, prices or author credentials.
- [ ] Validate JSON-LD syntax and test representative URLs in Google's Rich Results Test where relevant.
- [ ] Review warnings and errors; document which are actionable rather than adding markup just for appearance.

## D. Performance and accessibility
- [ ] Test representative mobile and desktop URLs.
- [ ] Check Core Web Vitals in field data when available; lab results alone are not field evidence.
- [ ] Images have descriptive alt text when informative and are appropriately sized.
- [ ] Interactive elements are keyboard accessible and have meaningful labels.
- [ ] Check layout shifts, oversized images, console errors and failed network requests.
- [ ] No blocking overlays or intrusive interstitials obscure primary content.

## E. Search Console and measurement
- [ ] Verify the correct domain/property in Google Search Console.
- [ ] Inspect a sample of canonical URLs with URL Inspection; record status and date.
- [ ] Review sitemap processing errors and Page Indexing report.
- [ ] Separate discovered, crawled, indexed and served URLs; these are not interchangeable.
- [ ] Record impressions, clicks, CTR and average position from Search Console with date range and country/device filters.
- [ ] Do not promise indexing, ranking, traffic or impression targets; search engines control these outcomes.
- [ ] Annotate deployments and content updates to make later comparisons meaningful.

## F. Release gate

A page is ready for release only when crawlability, canonical, content, and source checks pass. A site-wide release should not trigger expensive CI/deploy jobs just to re-submit unchanged URLs. Prefer targeted checks and one deliberate deployment after a coherent batch of changes.

## Minimal audit record

| Field | Value |
|---|---|
| URL | |
| Checked at (UTC) | |
| HTTP status | |
| Canonical | |
| Robots/indexability | |
| Sitemap included | |
| Rendered content checked | |
| Structured data checked | |
| Mobile/performance check | |
| Search Console evidence | |
| Blocking issue | |
| Next action / owner | |
