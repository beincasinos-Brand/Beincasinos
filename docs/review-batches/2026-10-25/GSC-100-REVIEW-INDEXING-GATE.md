# BeInCasinos — 100-review Google Search Console indexing gate

**Checkpoint:** 2026-10-25  
**Branch:** `big-batch/review-scorecards-2026-10-25`  
**PR:** https://github.com/beincasinos-Brand/Beincasinos/pull/169

## Current verified state

- Current PR file count from GitHub: 423 changed files.
- Markdown files in the research-dossier tree: 325.
- Approved consumer reviews confirmed in tracker: 0.
- New public production review routes created by the review batches: 0 confirmed.
- Deploy performed by the review batches: 0.
- Google indexing for any new review from these batches: not established.

**Important:** GSC property verification and sitemap submission do not mean a URL is indexed. A Markdown dossier in a research folder is not a public review page and must not be added to the public sitemap.

## What counts toward 100

A review may be marked READY FOR EDITOR only when all critical requirements are present. It counts as APPROVED only after a second editor has reviewed the evidence and the page passes publication QA. It counts as PUBLISHED only after the real production URL is fetched and checked. The 100-review milestone requires 100 distinct canonical brand identities, deduplicated across market variants.

For each brand-market page:
1. Exact consumer-facing domain and legal operator are matched to a current regulator record.
2. The record permits the actual online casino product in the stated market; if not, exclude that market.
3. Current binding bonus terms are captured, or the page explicitly says no offer is verified.
4. Payment methods, limits, fees, KYC and withdrawal language are sourced; actual test claims have dated test logs.
5. Game catalogue/provider claims are dated and sourced.
6. Player protection, privacy, support and complaints are checked.
7. Original copy, meaningful pros/cons, user-serving FAQs, known limitations and evidence dates are included.
8. Every image has documented reuse rights, attribution requirements and factual alt text.
9. Numeric score and confidence are withheld until the evidence gate passes; score arithmetic is shown.
10. Affiliate disclosure and safer-gambling information are visible.
11. Author/reviewer, correction route and update policy are present.
12. Mobile layout, links, canonical, robots, structured data, sitemap inclusion and internal links are QA'd.

## Indexing checklist after production routes exist

- [ ] Confirm each approved page returns HTTP 200 on the canonical host.
- [ ] Confirm no accidental `noindex`, auth wall, robots block or redirect loop.
- [ ] Confirm self-referencing canonical URL matches the final production URL.
- [ ] Confirm page is linked from an appropriate market hub and not orphaned.
- [ ] Confirm visible content matches structured data; omit unsupported Review/AggregateRating/Offer claims.
- [ ] Confirm XML sitemap contains only canonical, indexable, approved production URLs.
- [ ] Fetch the live sitemap and sample URLs from outside the build environment.
- [ ] Submit/refresh sitemap in GSC and inspect representative URLs.
- [ ] Track GSC status; do not claim indexed until GSC confirms it.
- [ ] Monitor crawl/indexing errors and update stale regulatory/offer evidence.

## Deployment rule

**NO-GO for declaring the 100-review milestone complete.** The current PR is research-workbench heavy and is not a set of 100 approved production pages. Do not merge or deploy the workbench as consumer reviews. Continue by completing distinct evidence records, converting approved records into actual site routes using the existing production architecture, then run the project's own CI and preview checks before deployment.

## Evidence accountability

Maintain separate counts for: candidate rows, unique canonical brands, evidence-verified market records, READY FOR EDITOR, APPROVED, PUBLISHED, and URLs confirmed indexed by GSC. Never substitute one count for another.
