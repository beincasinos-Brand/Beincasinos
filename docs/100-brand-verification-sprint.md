# 100-brand verification sprint

**Goal:** build a source-backed, market-specific registry of 100 casino brands before publishing or commercially promoting brand profiles. The owner's 100-million-daily-impressions ambition is a long-term aspiration, not a forecast or guarantee.

## Current state (2026-10-22)

- `docs/brand-research-template.csv` contains 100 candidate rows. These are research leads, not 100 verified brands; candidate names do not prove existence, licence status, product permission, market eligibility, or willingness to pay.
- The Swiss/FGB and Great Britain/UKGC research batches remain internal evidence logs. Current GB documents: [batch 1](gb-brand-research-batch-1.md), [batch 2](gb-brand-research-batch-2.md), [batch 3](gb-brand-research-batch-3.md), [batch 4](gb-brand-research-batch-4-2026-10-22.md), [batch 5](gb-brand-research-batch-5-2026-10-22.md), [batch 6](gb-brand-research-batch-6-2026-10-22.md), and [batch 7](gb-brand-research-batch-7-2026-10-22.md), and [batch 8](gb-brand-research-batch-8-2026-10-22.md), and [batch 9](gb-brand-research-batch-9-2026-10-22.md), and [batch 10](gb-brand-research-batch-10-2026-10-22.md). Batch 5 records surrendered licences for BresBet/Bet St George and the limited scope of the Rank Group land-based settlement; batch 6 records the dated QuinnBet settlement and a separate supplier-risk case; batch 7 adds Petfre enforcement-index tracking and Betfred entity-mapping cautions; batch 8 adds a current UKGC enforcement triage queue and competitor-page quality controls; batch 9 records the UKGC's 21 October 2026 L & L Europe decision and three named domain leads; batch 10 records the primary UKGC Stakelogic BV supplier decision and strict attribution limits. These remain research leads pending current register, decision and domain/product checks.
- Denmark regulator evidence has expanded through internal batches [4](reviews/internal/denmark-official-operator-evidence-batch-4-2026-10-22.md), [5](reviews/internal/denmark-official-operator-evidence-batch-5-2026-10-22.md), [6](reviews/internal/denmark-official-operator-evidence-batch-6-2026-10-22.md), [7](reviews/internal/denmark-official-operator-evidence-batch-7-2026-10-22.md), and [8](reviews/internal/denmark-official-operator-evidence-batch-8-2026-10-22.md), plus the [regulatory-history watchlist](reviews/internal/denmark-regulatory-history-insolvency-watchlist-2026-10-22.md). These are candidate evidence notes, not completed reviews.
- The three GB batches cover regulator identity leads, domain/operator ambiguities, and historic surrendered permissions. Some rows are related entities rather than distinct consumer brands, so they must be deduplicated before counting the 100-brand target.
- **0/100 candidates are approved for publication** in this sprint. The new Denmark batches are regulator/operator evidence only; they do not count as fully verified brands or publication-ready reviews. The Danish Gambling Authority reported Jackpotbet A/S was declared bankrupt on 18 June 2026 and its licences revoked; exclude it from active candidates unless a new official record establishes lawful current permission. Source: https://spillemyndigheden.dk/en-us/news-articles/gambling-operator-declared-bankrupt. Research documents are not completed consumer reviews, legal opinions, or evidence of hands-on testing.
- The targeted ADR route repair workflow previously failed before purge with Cloudflare API HTTP 401 / error 10000 (authentication error); no cache purge was accepted. See [issue #14](https://github.com/beincasinos-Brand/BeIncasinos/issues/14) and [workflow run](https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39749376879). A current content fetch can read the canonical guide, but this alone does not prove the edge returned raw HTTP 200.
- The latest static site check run for the previous research commit passed, including Chromium browser smoke tests. The latest run after batch 3 was still in progress at the last check; do not call it passed until it finishes.


- [Batch 11](gb-brand-research-batch-11-2026-10-22.md), [batch 12](gb-brand-research-batch-12-2026-10-22.md), [batch 13](gb-brand-research-batch-13-2026-10-22.md), [batch 14](gb-brand-research-batch-14-2026-10-22.md), and [batch 15](gb-brand-research-batch-15-2026-10-22.md) extend the GB evidence queue. Batch 11–12 are supplier/enforcement leads; batch 13 records 888casino.com / 888 UK Limited register mapping; batch 14 flags 32Red Limited's surrendered Casino Remote permission; batch 15 records Betway Limited's active Casino Remote permission and listed domains. These are internal evidence notes, not five publication-ready reviews. Keep the sprint total at **0/100 approved** until each brand independently passes all verification and editorial gates.


- [Batch 16](gb-brand-research-batch-16-2026-10-22.md) records Betfair Casino Limited (UKGC account 39435), its active Casino Remote entry and www.betfair.com domain, plus the Commission's 17 December 2025 combined enforcement settlement affecting four Paddy Power Betfair licensees. The £2m total must not be attributed solely to Betfair Casino Limited. This remains an internal evidence lead, not a completed review; approved brands remain **0/100**.


- [Batch 17](gb-brand-research-batch-17-2026-10-22.md) records the official William Hill domain/operator mapping: www.williamhill.com is associated in the UKGC search with WHG (International) Limited (account 39225), while William Hill's own terms describe a separate William Hill Global PLC operator for many non-GB markets. Do not infer Moroccan eligibility from the GB record. This is an identity lead only; the sprint remains **0/100 approved brands** and **0 publication-ready reviews**.


- [Batch 18](gb-brand-research-batch-18-2026-10-22.md) records the UKGC's active Casino Remote entry for Hillside (UK Gaming) ENC (bet365) and distinguishes it from the separate betting licensee Hillside (UK Sports) ENC. It also records the licensee-specific 2024 AML/customer-interaction settlement with correct attribution. This is internal evidence, not a completed review; approved brands remain **0/100**.

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

## Latest register evidence

- [GB batch 13: 888 UK Limited / 888casino.com](gb-brand-research-batch-13-2026-10-22.md) records the current UKGC register's active Casino Remote permission and active domain association for 888casino.com. This advances one identity check only; terms, payments, complaints, safer-gambling and second-editor review remain open.

- [GB batch 14: 32Red licence-status alert](gb-brand-research-batch-14-2026-10-22.md) records the UKGC register's surrendered Casino Remote permission for 32Red Limited effective 12 March 2025; the brand must not be treated as currently licensed in Great Britain without fresh exact-domain/operator evidence.

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
