# 100-brand verification sprint

**Goal:** build a source-backed, market-specific registry of 100 casino brands before publishing or commercially promoting brand profiles. The owner's 100-million-daily-impressions ambition is a long-term north star, not a forecast or guarantee.

**Current state (2026-10-21):**
- 10 Swiss online-casino platform/domain leads copied from the Swiss Federal Gaming Board's official online-gambling page into `docs/verified-brand-registry.csv`.
- 10/100 have an official regulator source confirming that the named casino platform is listed as operating online in Switzerland.
- 0/100 are marked approved for publication in this sprint: exact legal-entity/domain matching, current licence scope and game permissions, current terms, complaints/support, safer-gambling controls, and editorial review remain to be completed for each row.
- This is deliberately not a claim that 10 profiles are fully verified, safe, or ready to recommend.

## What counts as a verified brand

A brand only counts toward the 100 verified target when all required fields are recorded in `docs/brand-research-template.csv` / `docs/brand-profile-template.md` and independently checked:

1. Exact official domain and consumer brand are identified from an official brand or regulator source.
2. Legal operator is matched to the domain and current regulator record.
3. Current status, product permission, and named jurisdiction are confirmed from the regulator's own register/decision.
4. The permitted market/product scope is explicit; a licence in one country is not treated as global permission.
5. Current official terms, bonus/withdrawal restrictions where relevant, complaints route, support contact, and safer-gambling tools are reviewed.
6. Every material claim has a primary-source URL and a UTC check date.
7. Conflicts, unknowns, enforcement history, and market limitations are documented; unresolved material issues mean `hold`, not `verified`.
8. A second editorial check is completed before a public page is published. Commercial interest never changes a factual verdict or score.

## Batch order

1. **CH:** finish the 10 FGB-listed online platforms; this is a small, clearly bounded official list.
2. **GB:** use the Gambling Commission's current business, domain, trading-name and licence datasets. Require the exact domain/trading-name mapping plus active remote casino permission; an operator's active licence alone is insufficient.
3. **NL:** use the Kansspelautoriteit's current Kansspelwijzer and current permit decisions; re-check any permit renewals and exact brand/domain mapping.
4. **DE:** use the relevant official state authority/official whitelist and confirm the exact permit and product scope before any profile.
5. Add another market only after a documented legal/advertising/affiliate eligibility review.

## Publishing and SEO gates

- Keep the internal registry private to the source repository until individual profiles pass the review gate.
- Do not generate 100 near-identical pages, invent scores, or use affiliate rankings as evidence.
- Each public page must add original analysis: exact entity/domain evidence, a concise market-scope explanation, meaningful terms and payment limitations, a dated source log, complaints/support links, corrections route, and commercial disclosure.
- No page should imply that BeInCasinos tested an operator, monitored withdrawals, or independently resolved complaints unless those activities actually occurred.
- Do not remove any launch/crawl safeguard or request mass indexing until legal, privacy, domain, and editorial launch checks are explicitly cleared.
- Measure Google Search Console impressions, clicks, CTR, positions, indexed pages and country/query coverage. 100 million daily impressions cannot be guaranteed by content volume or any technical setting.

## Source starting points

- Swiss Federal Gaming Board: https://www.esbk.admin.ch/en/online-gambling
- Great Britain Gambling Commission register and downloadable datasets: https://www.gamblingcommission.gov.uk/public-register/businesses and https://www.gamblingcommission.gov.uk/public-register/businesses/download
- Netherlands Kansspelautoriteit register: https://kansspelautoriteit.nl/register-licensees

## Next action

Complete the CH evidence fields first, then create a regulator-backed GB batch from the official datasets. Keep every row at `hold` until the required domain/operator/permission and editorial checks are complete.
