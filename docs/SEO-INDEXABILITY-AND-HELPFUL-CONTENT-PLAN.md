# BeInCasinos — SEO indexability and helpful-content release plan

**Purpose:** make each eligible page genuinely useful and technically eligible for search. This is a QA and editorial standard, not a promise that Google will index every URL. Indexing and rankings are decided by search engines.

## 1. Non-negotiable rule: index quality, not every URL
A URL should be indexable only when it has a distinct search purpose, substantial original value, verified facts, working navigation and a reason to exist independently. A site cannot responsibly promise “100% SEO” or force every page into Google’s index. Thin, duplicate, unverified or legally unsuitable pages should remain noindex, be consolidated, or not be created.

### Index decision
- **INDEX:** unique, complete, useful, source-backed page; approved legal/product status; correct canonical; internal links; accessible layout; no critical factual gaps.
- **HOLD / NOINDEX:** candidate is relevant but evidence, terms, imagery, testing or independent review is missing.
- **CONSOLIDATE:** two URLs substantially answer the same intent, duplicate market/product content, brand aliases, or country variants with no meaningful local difference.
- **EXCLUDE:** product not lawfully available/authorized for the stated market, domain cannot be verified, or the page would mislead users.
- **REMOVE / 404 or 410:** obsolete URL with no useful replacement; use a relevant 301 only when there is a genuinely equivalent destination.

Never remove noindex just to inflate indexed-page counts.

## 2. Helpful content standard for every casino review
The page must help a real reader decide what to check, not merely repeat the operator’s marketing copy. Required evidence and reader value:

1. **Scope:** exact market, domain, operator, product types covered and last-checked date.
2. **Eligibility:** official regulator evidence tied to the exact legal entity/domain/product; state/province restrictions explained.
3. **Offer:** live local promotion, complete terms, expiry, wagering base, max bet, game contribution/exclusions, cap, eligibility and payment restrictions—or a clear statement that no verified offer was found.
4. **Payments:** current methods, currency, fees, minimum/maximum, KYC and stated processing windows, sourced from local terms.
5. **Real testing:** disclose what was actually tested, when, on what device/account state, sample size and limitations. Never imply a deposit/withdrawal test if none occurred.
6. **Games/fairness:** market-specific catalogue and exact-title sources for RTP where used; do not generalize one game’s RTP to the whole site.
7. **Player protection:** limit tools, time-out, self-exclusion, account closure, privacy, security, complaints and escalation route.
8. **Comparison:** compare like-for-like verified fields, not affiliate commission, vague “best” language or invented rankings.
9. **Verdict:** explain who may find the product useful, key limitations, unresolved questions and reasons to avoid it.
10. **Accountability:** author, independent checker, sources, date checked, corrections route and affiliate disclosure.

A page is not high quality simply because it is long. Remove filler, unsupported claims, repeated FAQ paragraphs and boilerplate that does not help with the particular brand/market.

## 3. Scoring: no invented ratings
Use the published 100-point rubric:
- Legal eligibility and operator identity: 25
- Bonus fairness and clarity: 15
- Payments and withdrawals: 15
- Games and fairness: 10
- Support and complaints: 10
- Usability and accessibility: 10
- Privacy and account security: 10
- Evidence freshness/confidence: 5

For each score, attach an evidence ID, source/test date, method, result and limitations. If a critical legal or safety gate is unresolved, do not produce a final score. Unknown is **pending**, not automatically 0, 5, or 10. Show the arithmetic and methodology next to any published score. No AggregateRating schema unless visible ratings are real and eligible for the structured-data policy.

## 4. SEO implementation checklist
### Crawl and index
- Confirm robots.txt permits intended pages and does not block CSS/JS needed for rendering.
- Ensure each indexable page returns HTTP 200, is internally linked, has a stable self-referencing canonical and is not accidentally noindex.
- Sitemap includes only canonical, indexable, approved URLs; exclude redirects, 404s, duplicates, noindex and draft pages.
- Do not create tag/search/filter URLs that generate infinite crawl spaces.
- Verify trailing-slash, www/non-www and HTTP/HTTPS behavior consistently.
- Test mobile rendering and Google-selected canonical in Search Console.
- Monitor sitemap fetch errors, indexing exclusions, manual actions, security issues and Core Web Vitals.

### On-page relevance
- Unique title and meta description that match the actual page.
- One clear H1; headings follow user tasks, not keyword repetition.
- First screen identifies the exact market and the most important verified caveat.
- Add a concise “at a glance” table only with facts that have evidence.
- Use descriptive internal links; avoid repetitive exact-match anchors.
- Include updated date only when the page materially changed; never refresh dates without review.
- Add useful comparison tables only if every row uses consistent, sourced fields.
- Ensure images have rights, useful alt text, responsive sizing and dimensions to reduce layout shift.
- Structured data must match visible content; no fake ratings, offers, authors or review counts.

### Performance and accessibility
- Test real mobile layout, keyboard navigation, contrast, text scaling, accessible form labels, heading order and alt text.
- Compress images and use responsive image sizes; avoid layout shift by reserving dimensions/aspect ratios.
- Minimize blocking scripts and unused client-side code; monitor field data where available.
- Check broken links and 404s before release.

## 5. Avoid thin/duplicate international pages
The 12 target markets are AU, CA, GB, US, CH, DE, NL, SE, ES, IT, FR and BE. A brand’s availability and permitted product vary by jurisdiction. Do not translate or lightly rewrite one review into twelve pages. A localized version must contain real local differences: legal operator/domain, regulator, product availability, local offer, payment methods, terms, support, restrictions and locally relevant player-protection information.

- Country-specific URL only when the product is available and the page has unique value.
- For province/state-based markets, state the covered jurisdiction in the title, H1 and copy.
- For markets where online casino products are not lawfully licensed, do not create a “best online casinos” doorway page that promotes offshore sites.
- French-market pages must distinguish regulated online poker/sports betting from casino games; do not imply online slots/table games are licensed if they are not.
- Australia requires special caution: do not promote offshore interactive casino services as lawful for Australian residents.
- US and Canada pages must be state/province-specific; one jurisdiction’s approval does not imply nationwide availability.
- Merge same-operator aliases and near-duplicate brand domains unless they offer distinct, independently verified products.

## 6. Image asset pipeline
For every visual asset, log: file path, source URL, creator, rights basis/license or permission, capture date, permitted commercial/editorial use, dimensions, crop, alt text and approver. Never treat an image-search result as permission. Do not hotlink competitor screenshots or copy their proprietary review-card assets.

Recommended production sequence:
1. Prefer officially supplied media assets with documented permitted use or commission original brand-neutral art.
2. Save local optimized image variants; never rely on a temporary search thumbnail.
3. Provide useful, non-keyword-stuffed alt text.
4. Reserve image dimensions/aspect ratio to avoid layout shift.
5. Confirm responsive/mobile crop and contrast.
6. Keep ratings, bonus numbers and licence claims out of decorative artwork unless verified and accessible as text.

## 7. Page release gates
Before removing noindex:
- [ ] Exact operator/domain/product eligibility checked in current official source.
- [ ] Current local terms, bonus and cashier evidence saved with timestamps.
- [ ] Factual statements linked to source IDs or documented test records.
- [ ] Score calculated from evidence and independently reviewed, or page remains NOT RATED.
- [ ] Originality and user value review passed; no boilerplate-heavy duplicate.
- [ ] Images rights-cleared and optimized.
- [ ] Mobile, accessibility, broken-link and technical SEO QA passed.
- [ ] Internal links, canonical, robots, sitemap and structured data checked.
- [ ] Author, checker, update date, affiliate disclosure and correction route present.
- [ ] Market-specific advertising and responsible-gambling rules reviewed.

## 8. Measurement loop
Use Search Console to track impressions, clicks, CTR, query intent, indexing and canonical issues. Use analytics only with privacy-compliant configuration. Review pages with impressions but poor CTR for accurate titles/snippets; review pages with clicks but poor engagement for mismatch between search promise and page answer. Re-check high-risk terms and regulatory status on a scheduled cadence and whenever a regulator/operator notice changes.

**Success means trustworthy pages that deserve to be indexed—not forcing every draft into the index.**
