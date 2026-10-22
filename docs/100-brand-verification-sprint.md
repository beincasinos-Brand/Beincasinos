# 100-brand verification sprint

**Goal:** build a source-backed, market-specific registry of 100 casino brands before publishing or commercially promoting brand profiles. The owner's 100-million-daily-impressions ambition is a long-term aspiration, not a forecast or guarantee.

## Current state (2026-10-22)

- `docs/brand-research-template.csv` contains 100 candidate rows. These are research leads, not 100 verified brands; candidate names do not prove existence, licence status, product permission, market eligibility, or willingness to pay.
- The Swiss/FGB and Great Britain/UKGC research batches remain internal evidence logs. Current GB documents: [batch 1](gb-brand-research-batch-1.md), [batch 2](gb-brand-research-batch-2.md), [batch 3](gb-brand-research-batch-3.md), [batch 4](gb-brand-research-batch-4-2026-10-22.md), [batch 5](gb-brand-research-batch-5-2026-10-22.md), [batch 6](gb-brand-research-batch-6-2026-10-22.md), and [batch 7](gb-brand-research-batch-7-2026-10-22.md), and [batch 8](gb-brand-research-batch-8-2026-10-22.md). Batch 5 records surrendered licences for BresBet/Bet St George and the limited scope of the Rank Group land-based settlement; batch 6 records the dated QuinnBet settlement and a separate supplier-risk case; batch 7 adds Petfre enforcement-index tracking and Betfred entity-mapping cautions; batch 8 adds a current UKGC enforcement triage queue and competitor-page quality controls. All remain research leads pending direct decision and domain/product checks.
- Denmark regulator evidence has expanded through internal batches [4](reviews/internal/denmark-official-operator-evidence-batch-4-2026-10-22.md), [5](reviews/internal/denmark-official-operator-evidence-batch-5-2026-10-22.md), [6](reviews/internal/denmark-official-operator-evidence-batch-6-2026-10-22.md), [7](reviews/internal/denmark-official-operator-evidence-batch-7-2026-10-22.md), and [8](reviews/internal/denmark-official-operator-evidence-batch-8-2026-10-22.md), plus the [regulatory-history watchlist](reviews/internal/denmark-regulatory-history-insolvency-watchlist-2026-10-22.md). These are candidate evidence notes, not completed reviews.
- The three GB batches cover regulator identity leads, domain/operator ambiguities, and historic surrendered permissions. Some rows are related entities rather than distinct consumer brands, so they must be deduplicated before counting the 100-brand target.
- **0/100 candidates are approved for publication** in this sprint. The new Denmark batches are regulator/operator evidence only; they do not count as fully verified brands or publication-ready reviews. The Danish Gambling Authority reported Jackpotbet A/S was declared bankrupt on 18 June 2026 and its licences revoked; exclude it from active candidates unless a new official record establishes lawful current permission. Source: https://spillemyndigheden.dk/en-us/news-articles/gambling-operator-declared-bankrupt. Research documents are not completed consumer reviews, legal opinions, or evidence of hands-on testing.
- The targeted ADR route repair workflow previously failed before purge with Cloudflare API HTTP 401 / error 10000 (authentication error); no cache purge was accepted. See [issue #14](https://github.com/beincasinos-Brand/BeIncasinos/issues/14) and [workflow run](https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39749376879). A current content fetch can read the canonical guide, but this alone does not prove the edge returned raw HTTP 200.
- The latest static site check run for the previous research commit passed, including Chromium browser smoke tests. The latest run after batch 3 was still in progress at the last check; do not call it passed until it finishes.

## What counts as a verified brand

A brand only counts toward the 100 verified target when all required fields are recorded in `docs/brand-research-template.csv` / `docs/brand-profile-template.md` and independently checked:

1. Exact official domain and consumer brand are identified from an official brand or regulator source.
2. Legal operator is matched to the domain and current regulator record.
3. Current status, product permission, and named jurisdiction are confirmed from the regulator's own register/decision.
4. Permitted market/product scope is explicit; a licence in one country is not treated as global permission.
5. Current official terms, bonus/withdrawal restrictions where relevant, complaints route, support contact, and safer-gambling tools are reviewed.
6. Every material claim has a primary-source URL and a UTC check date.
7. Conflicts, unknowns, enforcement history, and market limitations are documented; unresolved material issues mean `hold`, not `verified`.
8. A second editorial check is completed before a public page is published. Commercial interest never changes a factual verdict or score.

## Batch order

1. **CH:** finish the 10 FGB-listed online platforms and verify exact domain/operator/product scope from current official sources.
2. **GB:** continue with the UK Gambling Commission's current business, domain, trading-name and licence records. Require exact domain/trading-name mapping plus active remote casino permission; an operator's active licence alone is insufficient. Recheck the domain and permissions immediately before publication.
3. **DK:** continue beyond operator/domain discovery into brand-specific current terms, payment/withdrawal restrictions, support, complaints and safer-gambling evidence; resolve shared-operator and domain-transition conflicts. Exclude revoked/bankrupt operators from active candidates.
4. **NL:** use the Kansspelautoriteit's current Kansspelwijzer and permit decisions; re-check renewals and exact brand/domain mapping.
5. **DE:** use the relevant official state authority/official whitelist and confirm exact permit and product scope before any profile.
6. Add another market only after a documented legal/advertising/affiliate eligibility review.

## Publishing and SEO gates

- Keep the internal registry private to the source repository until individual profiles pass the review gate.
- Do not generate 100 near-identical pages, invent scores, or use affiliate rankings as evidence.
- Each public page must add original analysis: exact entity/domain evidence, a concise market-scope explanation, meaningful terms and payment limitations, a dated source log, complaints/support links, corrections route, and commercial disclosure.
- No page should imply BeInCasinos tested an operator, monitored withdrawals, or independently resolved complaints unless those activities actually occurred.
- Do not request mass indexing or treat a sitemap submission as launch approval until route reliability, legal/privacy, publisher/contact, domain, and editorial checks are explicitly cleared.
- Measure Google Search Console impressions, clicks, CTR, positions, indexed pages and country/query coverage. 100 million daily impressions cannot be guaranteed by content volume or any technical setting.

## Source starting points

- Swiss Federal Gaming Board: https://www.esbk.admin.ch/en/online-gambling
- Great Britain Gambling Commission register and datasets: https://www.gamblingcommission.gov.uk/public-register/businesses and https://www.gamblingcommission.gov.uk/public-register/businesses/download
- Netherlands Kansspelautoriteit register: https://kansspelautoriteit.nl/register-licensees

## Next actions

1. Continue exact domain/operator/product checks on the Swiss and GB research leads.
2. Complete terms, withdrawals, complaints, safer-gambling and regulatory-action evidence for each candidate that passes the identity gate.
3. Recheck the public route and resolve the Cloudflare secret issue through the owner-managed GitHub Actions secret; never paste a token into chat.
4. Keep every row on hold until all evidence, market eligibility, and second editorial review checks pass.
