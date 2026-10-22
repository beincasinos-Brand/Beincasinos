# 100-brand content, review and SEO execution plan

**Status:** internal operating plan; not a public recommendation or launch approval.  
**Updated:** 2026-10-22  
**North-star ambition:** 100 million daily impressions is an aspiration only, not a forecast or guarantee.

## Current inventory truth

- `docs/brand-research-template.csv` contains 100 candidate rows plus its header (100 candidates, not 100 verified brands).
- Candidates are research leads. Do not describe them as licensed, approved, safe, recommended, tested, or commercially qualified until the evidence for the exact brand, legal entity, domain, product and target jurisdiction is independently checked.
- Current verified-to-publish count remains **0** in the 100-brand sprint until each profile passes all gates.
- Public `/reviews/` correctly states that no live casino profiles are scored or ranked yet. Keep that truthful status until profiles are genuinely approved.
- The production route for the ADR guide has an unresolved 404/cache issue. Its repair workflow failed with Cloudflare API HTTP 401 / error 10000 (authentication error); no cache purge was accepted. See Issue #14 and workflow run 39749376879.

## Release sequence

### Gate 0 — production reliability and publisher readiness

1. Fix the Cloudflare token used by the targeted cache-repair workflow. Use a new/replaced GitHub Actions secret with only Zone:Read and Zone:Cache Purge on the `beincasinos.online` zone. Never paste secrets into chat.
2. Rerun the targeted workflow and require all checks to pass: clean canonical URL HTTP 200, correct self-canonical, sitemap inclusion, and www-to-apex redirect. Do not change DNS to work around a path-level failure.
3. Complete the owner-only release checklist in Issue #2: publisher identity/contact, trademark, target-market legal/advertising review, Morocco privacy/CNDP review, commercial/affiliate policy, hosting cost/terms, and manual accessibility/mobile/outbound-link QA.
4. Do not re-submit the sitemap or request mass indexing until the release checklist is explicitly cleared by the owner. The existing prior Search Console snapshot is stale relative to the current 44-URL sitemap.

### Gate 1 — research the 100 candidate brands in batches

Process 10 brands at a time. A candidate may move through `prospect → researching → verified_for_review → approved_to_publish → published`, or be held/rejected. Keep the exact status in the CSV; do not count a row as verified until the evidence log is complete.

For every brand, record:
- exact official domain and consumer-facing brand;
- exact legal entity and any white-label relationship;
- regulator register record and active permission for the exact product;
- permitted and excluded jurisdictions, checked against the current regulator source;
- current official terms, bonus restrictions, withdrawals, fees/limits and verification conditions;
- complaints escalation, customer support and safer-gambling controls;
- dated primary-source links for every material claim;
- historic regulatory actions and unresolved discrepancies;
- commercial relationship and visible paid/affiliate disclosure;
- reviewer, UTC check date, next-review date, and second editorial sign-off.

A missing or conflicting material fact means **HOLD**. A licence in one market does not establish global availability. Do not assign a score until eligibility checks pass and each scoring criterion has evidence.

### Batch order

1. **CH — official register-led batch:** finish the Swiss Federal Gaming Board-listed platforms and verify exact current domain/operator/product scope. Do not infer permission from brand similarity.
2. **GB — UKGC batch:** confirm exact domain and trading name against the current UKGC register, active remote-casino permission, terms, complaints and historical actions. Distinguish the licensed operator from the brand.
3. **NL — KSA batch:** use the current Kansspelwijzer/register and current permit decisions; re-check renewals and domain/product scope.
4. **DE — official state/whitelist batch:** include only brands with exact current permission and product scope confirmed from official sources.
5. Other markets only after a documented market-specific legal and advertising/affiliate eligibility review. Do not make a global casino list by mixing incomparable legal regimes.

## Public review page specification

Every approved profile must be genuinely useful and materially distinct, not a spun template. Include:
- a clear answer-first summary stating the market and date checked;
- brand/domain/legal-operator relationship and what the regulator record does and does not prove;
- current product and jurisdiction scope;
- a practical terms table: bonus eligibility, wagering base, expiry, max bet, max cashout, excluded games, fees, withdrawal limits and verification rules where applicable;
- official complaints route, support options, safer-gambling tools and local help resources;
- historic regulatory actions and unresolved facts in fair context;
- transparent source log, correction/contact route, update date and next review date;
- visible affiliate/paid-placement disclosure; editorial conclusions remain independent of payment.

Never claim hands-on testing, withdrawal speed, complaint resolution, customer experience or monitoring unless that activity was actually performed and documented. Do not use unsupported superlatives or fabricated user reviews.

## SEO architecture

- Build one useful hub at `/reviews/`, then link to each approved profile only after the profile passes publication checks.
- Create market hubs only when there are enough verified, distinct profiles to help users compare that market; avoid empty taxonomy pages.
- Connect brand profiles to relevant guides: licence checks, legal operator vs brand, bonus terms, withdrawals, complaints, safer gambling and review methodology.
- Use descriptive titles and unique meta descriptions; one clear H1; correct canonical; meaningful internal links; breadcrumbs where useful; valid sitemap entries only for canonical 200 URLs.
- Add structured data only when it accurately represents visible page content. Never add fake ratings, fake review counts, or aggregate ratings without real eligible data.
- Avoid doorway pages, duplicated boilerplate, keyword stuffing, fake freshness dates and mass indexing requests.
- After release, measure actual Google Search Console queries, clicks, impressions, CTR, average position and country/page coverage; use GA/analytics only after privacy and consent review.

## Weekly operating scorecard

Report counts, not assumptions:
- candidates in registry / verified / held / rejected / published;
- percentage of material claims backed by current primary sources;
- live canonical pages returning HTTP 200;
- sitemap URL count vs successful canonical URLs;
- Search Console clicks, impressions, CTR and average position by page/query/country;
- pages indexed as reported by Search Console, with date and method;
- pages needing review because of changed terms, licence records or regulatory actions.

## Acceptance criteria for the 100-brand milestone

“100 brands” means 100 distinct brands with completed source-backed evidence, exact market/product scope, current terms and complaints/safety information, dated review, no unresolved critical conflicts, and independent editorial approval. Candidate names or bulk-generated pages do not count. The milestone is not complete merely because 100 URLs exist.
