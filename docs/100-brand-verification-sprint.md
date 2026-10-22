# 100-brand verification sprint

**Goal:** build a source-backed, market-specific registry of 100 casino brands before publishing or commercially promoting brand profiles. The owner's 100-million-daily-impressions ambition is a long-term north star, not a forecast or guarantee.

**Current state (2026-10-22):**
- `docs/brand-research-template.csv` currently contains 100 candidate rows. These are a mixed-market prospect/research list, not 100 verified brands; names in the CSV do not by themselves prove current existence, licence status, product permission, market eligibility, or willingness to pay.
- The earlier first research batch comprised 10 Swiss regulator-listed platform/domain leads and 6 UK leads for further domain/operator/licence matching. That earlier batch count is not the total candidate inventory.
- **0/100 are approved for publication** in this sprint. Exact legal-entity/domain matching, current licence scope and product permissions, current terms, complaints/support, safer-gambling controls, dated primary sources, and second editorial review remain required for each candidate.
- The targeted ADR route repair workflow ran but failed before purge with Cloudflare API HTTP 401 / error 10000 (authentication error); no cache purge was accepted. See issue #14 and workflow run https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39749376879.
- One lead must not count toward the verified-brand target merely because a regulator lists a related operator or domain. In particular, a surrendered licence is not evidence of current authorisation.
- This is deliberately not a claim that 16 profiles are fully verified, safe, or ready to recommend.

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
