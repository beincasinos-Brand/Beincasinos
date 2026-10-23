# BeInCasinos — 10 million daily Search impressions: execution plan

**Prepared:** 23 October 2026  
**Status:** research/operating plan only; not a traffic forecast and not a guarantee.  
**Production constraints:** Cloudflare Pages is the hosting platform. Use the existing approved release workflow; do not merge/deploy, change DNS, purchase plans, or write to Search Console without owner authorization. Use `[CF-Pages-Skip]` for research-only commits to conserve GitHub Actions minutes.

## 1. What the target means

10,000,000 impressions per day equals roughly **300 million impressions per 30-day period**. There is no verified current Search Console performance baseline in the evidence available for this plan. Therefore the target date, required ranking share, and likelihood of success cannot honestly be estimated yet.

Do not optimise for URL count. Search impressions accrue when useful pages are eligible to appear for relevant queries; thin pages, duplicate market variants, unsupported claims, and pages without genuine demand can dilute quality rather than create durable growth.

## 2. Current known baseline and limitations

- Live-site audit: 46 URLs in the live sitemap were extracted; the repository sitemap was corrected to 46 URLs on the research branch. This extraction check is not a direct HTTP-status audit and does not prove Google indexation.
- `robots.txt` was observed allowing crawling and pointing to the sitemap.
- The live `/reviews/` page states that no casino profiles are scored or ranked yet.
- Search Console notes last recorded 32 submitted URLs before the source-side sitemap correction. Search Analytics returned no rows in that connector snapshot; this must not be interpreted as a verified zero-impression baseline.
- Registry audit: 204 market-specific candidate rows, 154 provisional global brand IDs, 202 HOLD and 2 rejected. These are not 154 verified operators.
- Publication-approved reviews: **0/100**. No candidate draft should be counted as a completed review.
- Known research branch only: the corrected 46-entry sitemap has not been represented as deployed.

## 3. Stage gates and measurement

Use Search Console's actual 28-day and 90-day page/query exports as the baseline before setting growth deadlines. Capture date range, property, country, device, search type, clicks, impressions, CTR, average position, top queries, top landing pages and indexation status. Save dated snapshots for comparison.

| Stage | Daily impressions | Approx. 30-day impressions | Gate to move on |
|---|---:|---:|---|
| Baseline | Unknown until verified | Unknown | Retrieve and archive real Search Console exports |
| Stage 1 | 10,000 | 300,000 | Stable visibility across relevant pages, no critical technical blockers |
| Stage 2 | 100,000 | 3,000,000 | Growing non-brand query coverage and pages earning impressions |
| Stage 3 | 1,000,000 | 30,000,000 | Multiple topic clusters show sustained qualified demand and editorial capacity |
| North star | 10,000,000 | 300,000,000 | Sustained, independently measured Search Console impressions—not a projection |

These are measurement gates, not promised timelines. Re-evaluate monthly using actual results and content quality.

## 4. Priority order

### P0 — release and measurement prerequisites

1. Obtain owner/editorial/legal approval for any production release; maintain the single-deploy rule.
2. After an approved release, verify the live sitemap contains the intended canonical URLs and returns a successful HTTP status.
3. In Search Console, inspect the sitemap processing result and URL Inspection for representative pages: homepage, guides, methodology, market directory and each newly approved review.
4. Record crawl allowed, fetch status, indexing allowed, declared canonical, Google-selected canonical, last crawl and exclusion reason. Do not infer indexation from sitemap membership or a successful build.
5. Validate status/redirect/canonical/noindex/robots metadata from raw responses. Fix server errors, redirect chains, conflicting canonicals, soft 404s, broken internal links and accidental noindex before publishing more pages.
6. Finish publisher identity, contact, affiliate disclosure, privacy, responsible-gambling and market-specific legal gates. Do not publish casino promotion where local law does not permit it.

### P1 — build authority with useful information pages

Prioritise the questions that help users understand evidence and risk, not generic “best casino” copy. Each page must answer a distinct intent and cite current primary sources.

| Cluster | Example page intent | Required evidence / unique value |
|---|---|---|
| Licence verification | How to check whether an online casino is authorised in [market] | Regulator register steps, entity/domain matching, date checked, common false positives |
| Withdrawals | What to check before relying on casino withdrawal claims | Official terms, method/limit/fee caveats, verification and escalation route |
| Bonus terms | How wagering requirements, expiry and game contributions work | Plain-language examples; current offer-specific terms or explicitly say not verified |
| Complaints and ADR | How to escalate a gambling dispute in [market] | Regulator's official process, operator complaints route and recognised ADR source |
| Safer gambling | Deposit limits, time-outs and self-exclusion in [market] | Official regulator/service sources and accurate access instructions |
| Privacy and payments | Identity checks, data handling and payment-method caveats | Operator policy and relevant regulator/privacy authority sources |
| Editorial methodology | How BeInCasinos evaluates evidence and handles conflicts | Transparent rubric, source dates, limitations, correction process and affiliate disclosure |

Do not create a near-duplicate page for every market. Only localise where rules, regulator processes, licensed entities, payment methods or consumer remedies materially differ. AU and FR remain legal-scope gates for online casino recommendations; US and Canada need state/province-specific authorisation.

### P2 — publish a small, complete first batch before scaling

1. Deduplicate candidate records by global brand, local product, legal operator, licence and domain.
2. Select the first 10 candidates only from lawful target markets with current primary regulator evidence and a verified live local domain.
3. For every review capture current terms, exact bonus rules or an explicit “not verified”, deposits/withdrawals and limits/fees, complaints/ADR, safer-gambling tools, privacy/cookies, accessibility, enforcement and ownership/domain changes.
4. Require reproducible consumer checks where lawful and possible; never imply an account, cashier, withdrawal or support test happened if it did not.
5. Add a second-editor sign-off, editorial/legal review, methodology and clear affiliate disclosure.
6. Publish only after approval. Add each approved canonical URL to sitemap and contextual internal links. Keep drafts/HOLD pages private and excluded from the public artifact.
7. Use the first 10 reviews to validate the template and workload; do not scale to 100 by copying a boilerplate structure with only brand names changed.

### P3 — improve internal discovery and information architecture

- Maintain a small number of clear hubs: guides, markets, methodology and approved reviews.
- Link every guide from a relevant hub and link between related guides where the next step is genuinely useful.
- Each approved review should link to its market regulator/methodology and closely relevant consumer guides; avoid sitewide exact-match anchor spam.
- Use breadcrumbs only where they reflect real navigation. Add valid structured data only when the visible page supports it; never add fake ratings or review markup for untested/unpublished products.
- Use descriptive titles and meta descriptions that match each page's real content; avoid repeating a single template across every market.
- Audit orphan pages, broken links, image alt text, mobile readability, keyboard access, page performance and consent behaviour.
- Keep sitemap limited to canonical, indexable, useful pages that return success. Do not add HOLD dossiers, thin placeholders, or excluded candidates.

### P4 — query-led iteration

On a weekly cadence, export Search Console data and group by:
- high impressions / low CTR: review title and description accuracy; do not promise rankings or use misleading offers;
- positions around 5–20: improve answer completeness, evidence freshness, internal links and intent match;
- impressions but low conversion to useful next steps: improve clarity/navigation rather than adding promotional pressure;
- discovered/crawled but not indexed: inspect originality, duplication, usefulness, canonical choice and crawl signals before requesting indexing;
- pages with declining performance: check source freshness, changed rules/domains, seasonality and technical regressions.

Do not set CTR targets without a real baseline segmented by query, position, country and device. Search Console average position and impressions are aggregated metrics; interpret them with context.

## 5. Review page acceptance checklist

A review is publishable only when all required items pass:

- [ ] Target market and casino product are lawful and explicit.
- [ ] Current primary regulator record matches legal operator, exact domain and product.
- [ ] Current terms and offer-specific bonus rules captured or limitations clearly disclosed.
- [ ] Deposit and withdrawal methods, limits, fees, timings and exceptions are source-backed; no unsupported generalisation.
- [ ] Complaints and ADR escalation are current and sourced.
- [ ] Safer-gambling tools, self-exclusion and privacy/cookies reviewed.
- [ ] Relevant regulatory actions and ownership/domain changes checked.
- [ ] Original, market-specific analysis; no copied filler, fabricated score, testimonial or first-person test.
- [ ] Methodology, checked date, conflicts/affiliate disclosure, limitations and correction route visible.
- [ ] Independent second editor and legal/editorial sign-off recorded.
- [ ] Canonical, status, sitemap, internal links, mobile/accessibility and structured data validated.
- [ ] Search Console inspection recorded after authorised publication.

## 6. Weekly operating scorecard

Record, with evidence links and UTC timestamp:

1. Published and approved reviews (never count drafts).
2. Canonical useful pages in sitemap, and live sitemap count.
3. Search Console impressions/clicks/CTR/position over 28 and 90 days.
4. Pages with impressions, pages indexed according to Google, and exclusions by reason.
5. Non-brand queries and country/device distribution.
6. New/updated pages with real evidence improvements.
7. Broken links, status errors, canonical/noindex issues, page experience and accessibility issues.
8. Source freshness: regulator checks and terms/offer last-reviewed dates.
9. Editorial second-review completion and corrections/complaints.
10. Work remaining, blockers and owner approval needed.

## 7. Explicit non-goals

- No promise that 10 million daily impressions can be achieved by a fixed date.
- No mass-generated thin pages or fabricated consumer testing, reviews, scores, authors, ratings, or testimonials.
- No country-wide permission inferred from another market's licence.
- No affiliate placement disguised as editorial ranking.
- No deployment, DNS/Cloudflare settings, paid plan, or Search Console write without explicit approval.
- No counting of internal research dossiers as public reviews.

## References

- Internal live audit: `docs/live-production-seo-and-publication-readiness-audit-2026-10-22.md`
- Indexability audit: `docs/research/indexability-audit-and-organic-growth-plan-2026-10-23.md`
- Registry audit: `docs/research/registry-audit-2026-10-23.md`
- Target tracker: `docs/targets/100-brand-review-target-tracker-2026-10-23.md`
- Confirmed target geographies: `docs/target-geographies-12-confirmed-2026-10-23.md`
