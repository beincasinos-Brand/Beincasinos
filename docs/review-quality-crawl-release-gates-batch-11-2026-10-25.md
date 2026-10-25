# Batch 11 — Review-page quality, crawl and release gates
Date: 2026-10-25
Scope: editorial and technical release checklist for BeInCasinos. This is a working control document, not evidence that a brand is licensed or that a page has been indexed.

## Release blockers confirmed in the preceding audit
1. The live robots.txt returned `Disallow: /`, which prevents compliant crawlers from crawling the site. A proposed allow-all correction is on this research branch only and must not be described as live until merged and deployed.
2. Live review pages still expose unscored/pending verification states. Do not change these to stars, ratings, or rankings without a completed evidence record.
3. The sitemap had 146 URLs at the audit time. Inclusion in a sitemap is not proof of indexing, canonical selection, eligibility, or quality.
4. Existing profiles are unevenly distributed across the 12 target markets. Do not manufacture a quota of 100 by assigning brands to countries without official, domain-specific evidence.
5. A logo, affiliate relationship, operator claim, or generic terms page is not proof of a current market licence.

## Page-level publication gate (all must pass)
- [ ] Exact brand and exact operating domain recorded; redirects and locale variants checked.
- [ ] Legal operator name recorded from an authoritative source; uncertainty explicitly labelled.
- [ ] Target market and exact product category recorded (casino, sportsbook, poker, bingo, lottery, etc.).
- [ ] Official regulator register checked for that jurisdiction, domain, operator and product where applicable; date and source URL recorded.
- [ ] Terms and bonus terms fetched from the exact domain; effective/update date recorded; contradictory terms resolved.
- [ ] Bonus headline, currency, minimum deposit, wagering requirement, eligible games, expiry, max cashout and withdrawal restrictions are sourced or marked “not verified.”
- [ ] Payment methods and limits are sourced; estimated processing time is not represented as a tested result.
- [ ] KYC, withdrawal conditions, account closure and dormant-account terms summarized fairly.
- [ ] Safer-gambling tools, self-exclusion, deposit/time limits and help routes checked on the exact site.
- [ ] Complaints route and independent dispute route checked where applicable; no invented complaint history or support-response tests.
- [ ] Review contains original, brand-specific analysis rather than swapped-name template copy.
- [ ] Score calculation cites the evidence for every scored dimension; any missing dimension means no overall numeric score.
- [ ] Editorial date and next-review trigger set; broken source links and stale bonus claims rechecked before release.
- [ ] Affiliate disclosure visible near commercial links; commercial relationship never changes editorial score.
- [ ] Image rights/provenance recorded; do not hotlink or imply an official logo endorsement without permission.
- [ ] Canonical URL, title, description, one clear H1, internal links, breadcrumbs and relevant structured data validated.
- [ ] Page is useful and indexable; no accidental noindex, robots block, soft-404, or duplicate locale variant.

## Editorial score policy
Use the existing weights only after the market/domain/product authorisation gate passes:
- Terms clarity and fairness: 25
- Payment/withdrawal transparency: 20
- Safer-gambling controls: 20
- Complaints/support transparency: 15
- Operator/licence transparency: 10
- Usability/accessibility: 10

Each dimension needs an evidence note and a dated source. “Not checked” is not zero, and must not be converted into a guessed score. If any dimension is unassessed, show “Not rated — evidence review incomplete.” A high score is not a claim of safety, legality in every country, or guaranteed payout.

## Search and indexability release checks
1. Confirm production `robots.txt` allows intended public pages and still names the canonical sitemap.
2. Fetch the sitemap and parse every URL; require HTTP 200, self-consistent canonical, indexable response, correct locale/market intent, unique title/H1 and non-empty main content.
3. Flag redirects, 4xx/5xx, canonical-to-other-page, noindex, robots-blocked URLs, parameter variants, near-duplicates and orphan pages.
4. Verify that sitemap lastmod values reflect real substantive updates, not build time alone.
5. Check internal links from relevant directories and guides; no indexable page should depend solely on the sitemap.
6. After a controlled deployment, inspect a small representative sample in Search Console URL Inspection; submit/refresh sitemap if needed; monitor indexed vs discovered/crawled-not-indexed separately.
7. Do not use bulk indexing promises, fake traffic, automated query spam or paid links. No daily impression target can be guaranteed.

## First controlled deployment sequence
- [ ] Review and merge the proposed robots correction only after checking the entire diff and build behavior.
- [ ] Avoid triggering unnecessary GitHub Actions; use the existing Cloudflare Pages integration and check its deployment status.
- [ ] Verify homepage, /reviews/, one review URL, one guide, responsible-gambling page, robots.txt and sitemap after deployment.
- [ ] If review pages remain thin or unverified, keep them honestly unrated and consider noindexing/removing low-value duplicates rather than mass-publishing doorway pages.
- [ ] Record deployment ID/time and live response evidence before saying the release is complete.

## Batch status
This batch defines a release process and records known blockers. It does not certify all 100 brands, complete all 100 reviews, merge the robots change, deploy production, or establish Google indexing.
