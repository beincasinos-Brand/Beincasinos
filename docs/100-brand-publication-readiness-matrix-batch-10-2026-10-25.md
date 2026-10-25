# 100-Brand Publication Readiness Matrix — Batch 10
Date: 2026-10-25
Status: INTERNAL PLANNING DOCUMENT — NOT PUBLIC COPY

## Goal
Build a credible 100-brand review set across the 12 intended markets (AU, CA, GB, US, CH, DE, NL, SE, ES, IT, FR, BE), without manufacturing reviews, ratings, bonuses, legal permissions or hands-on tests. Existing profile count alone is not completion: each row needs an exact domain, correct product type, evidence trail, unique editorial analysis, current market gate and a release decision.

## Hard publication states
- READY: exact domain and operator match verified in current official register; target product category permitted; current terms and bonus sources captured; unique evidence-led review complete; all scoring criteria assessed; editor sign-off complete.
- PUBLISH UNRATED: legal gate passed and identity verified, but one or more quality criteria lack sufficient evidence. Clearly disclose what was and was not checked; omit total score and rating.
- HOLD: exact domain/operator, current permission, or product category unresolved; market excluded by terms; material conflict in offer/terms; or core source unavailable.
- REMOVE/REDIRECT: duplicate brand/slug, wrong product category, inactive/obsolete domain, misleading market label, or no defensible user value.

## Suggested distribution planning for 100 unique brand-market profiles
This is a planning allocation, not a claim that eligible brands have already been verified. Keep all rows empty until an actual candidate passes the relevant gate.
| Market | Planning slots | Required market evidence |
|---|---:|---|
| AU | 8 | ACMA category check; no inference from sports wagering to online casino permission |
| CA | 8 | Province-specific gate; separate Ontario and BC; no national blanket claim |
| GB | 10 | UKGC exact domain/operator, active status and relevant product scope |
| US | 8 | State-specific authorisation; exact state + domain + casino product |
| CH | 8 | ESBK/FGB online-casino list and per-game permit conditions |
| DE | 8 | GGL exact domain and category (e.g. virtual slots vs sports betting) |
| NL | 8 | KSA exact domain and current licence/product scope |
| SE | 8 | Spelinspektionen current licence and product category |
| ES | 10 | DGOJ exact operator/domain and game-specific authorisations |
| IT | 8 | ADM concessionaire + exact domain and remote-gambling category |
| FR | 6 | ANJ authorised product category; do not imply general online slots/table authorisation |
| BE | 10 | Belgian Gaming Commission exact domain and online licence class |
| TOTAL | 100 | Slots can be rebalanced only after eligible supply is researched |

## One-row evidence record (required per candidate)
- Brand display name:
- Canonical gambling domain and redirect destination:
- Target market and product type:
- Legal operator entity:
- Official regulator register URL + exact matching record:
- Licence/authorisation status + date checked:
- Terms URL + last updated date:
- Current offer URL + timestamp, eligibility, wagering basis, expiry, max bet, max cashout:
- Cashier/payment URL + methods, limits, fees, KYC and withdrawal timing:
- Safer-gambling URL + available limits, time-outs, self-exclusion and closure:
- Complaints/ADR route + evidence of actual outcomes:
- Hands-on tests performed (or explicitly not performed):
- Criterion-by-criterion evidence and confidence:
- Score calculation and missing criteria:
- Affiliate/commercial relationship disclosure:
- Editorial reviewer and approval date:
- Final state: READY / PUBLISH UNRATED / HOLD / REMOVE-REDIRECT.

## Minimum unique content requirements for each review
1. Market and product-specific opening summary, not a generic brand paragraph reused across pages.
2. Exact legal operator/domain and licence facts with source and date; distinguish regulator register facts from operator claims.
3. Product availability and exclusions for that market.
4. Current bonus explained in plain language only if exact offer terms were captured; state wagering basis, expiry, maximum bet and restrictions.
5. Payment/withdrawal facts sourced to current terms; never describe stated processing time as a tested payout.
6. Responsible-gambling tools, how to find them, and what was actually tested.
7. Complaint/ADR path, regulator decisions and resolved outcomes only where reliable evidence exists.
8. Pros/cons grounded in the collected evidence; unresolved issues should be called out rather than hidden.
9. Score only after all score dimensions are assessed and the legal gate passes; otherwise use “Not rated — evidence incomplete”.
10. Useful comparison links to genuinely relevant guides and market pages; avoid forced exact-match anchors.
11. Correct title/meta description, canonical URL, crawlable status, schema consistent with visible content and no fabricated review/rating schema.
12. Visible last-checked date that matches the evidence ledger; review volatile offers before every publication.

## Existing live-site audit implications
- Public sitemap currently returns 146 URLs, but sitemap count is not a count of verified reviews or indexed pages.
- Production robots.txt currently blocks crawling with `Disallow: /`; proposed `Allow: /` is on the research branch only and has not been deployed.
- The public directory says no profiles are currently scored/ranked; many cards remain “Not rated / Pending verification / Bonus not verified”. Preserve that honesty.
- A sitemap sample shows a high concentration of Spain profiles. Before claiming “100 brands across target markets”, calculate unique canonical domains and market distribution, deduplicate alternate slugs/domains, and identify missing AU/FR coverage.
- Some entries are betting or poker-oriented. Do not present them as online-casino reviews unless the specific casino product and local permission are established.

## Prioritised execution order
P0 — Resolve launch crawl block through reviewed PR, run build/output checks, then make one controlled deployment and verify live robots/sitemap/canonical behaviour.
P1 — Audit sitemap rows for unique canonical domain, correct target market, product type, status and duplicate slugs.
P2 — Rebuild the candidate pool from official regulator records, starting with the least-covered markets; exact-domain match is mandatory.
P3 — Capture operator terms, offer, payment, safer-gambling and complaint sources with evidence timestamps.
P4 — Publish only reviews that meet READY or PUBLISH UNRATED rules; hold unresolved profiles from market-specific recommendations.
P5 — Validate Search Console sitemap processing and inspect representative URLs after deployment; track actual indexed status separately from submitted/discovered counts.
P6 — Improve internal linking and unique informational value; use Search Console query/page data to prioritize improvements after the pages are crawlable.

## Success criteria
- Crawlable robots policy is live and verified.
- All sitemap URLs are canonical, intended, valid, and not blocked/noindexed unintentionally.
- 100 distinct brand-domain-market records exist with evidence ledgers; the count does not rely on duplicate brand aliases.
- Every published review has an honest status, sources, current date and market-specific scope.
- No fabricated star ratings, scores, bonus amounts, licence claims, official logos, or payout tests.
- GSC indexing is measured from Search Console, never inferred from sitemap inclusion.
- Organic impressions and clicks are measured; no daily-impression target is represented as guaranteed.

## Limitation
This matrix is a workflow and proposed distribution only. It is not proof that 100 legally eligible brands currently exist across these slots. Real market availability and product permission can make the final distribution uneven. No production deployment or GSC data change is performed by this document.
