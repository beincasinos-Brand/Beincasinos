# Registry-count reconciliation gate — 23 October 2026

## Why this gate exists

The directory must not imply that 100 market-specific cards equal 100 distinct global brands or 100 eligible casino products. The public-facing research directory now labels its 100 cards as research entries and explains the difference between directory cards, registry rows, provisional global-brand IDs and publication-approved reviews.

## Conflicting snapshots that must be reconciled

- `docs/research/global-brand-deduplication-audit-2026-10-23.md` reports an active CSV snapshot of **175 market-specific rows** and **140 provisional global-brand IDs**.
- `docs/targets/100-brand-review-target-tracker-2026-10-23.md` reports **204 market-specific research records**.
- The directory displays **100 research cards**; it is a curated working view, not proof of 100 unique eligible global brands.
- The tracker records **0/100 publication-approved reviews**.

These numbers describe different snapshots/scopes and must not be silently substituted for one another. Do not claim the 140 provisional IDs or 175 rows are eligible brands. The source CSV, row inclusion rules, and tracker snapshot date must be reconciled before a definitive count is published.

## Reconciliation checklist

1. Freeze a dated copy of `docs/brand-research-template.csv` and record its commit SHA and row count.
2. Validate every row has a stable `global_brand_id`, `market_code`, customer-facing brand, exact domain candidate, legal entity candidate, source URL and current verification date (or an explicit unknown).
3. Review every provisional alias group manually. Preserve separate market rows where local licences, contracting entities or terms differ; deduplicate only the global-brand count.
4. For each brand-market pair, verify the current primary regulator record authorises the relevant online-casino product and matches the live domain and contracting entity.
5. Mark excluded, historical, out-of-scope, duplicate and non-casino leads explicitly; none counts toward the eligible target.
6. Publish two independently computed figures: (a) distinct global brands after alias review, and (b) eligible brand-market pairs after regulator verification.
7. Count a review only after current consumer evidence, reproducible lawful checks, second review, and editorial/legal sign-off are recorded.

## Acceptance criteria

- One dated registry snapshot and one reproducible counting rule.
- Every merged alias has a documented reason and reviewer.
- No excluded or unverified row contributes to the eligible count.
- Dashboard and tracker totals are generated from the same snapshot.
- Publication-approved reviews remain a separate count; drafts and research leads do not count.

**Status: OPEN / HOLD.** This document records a quality gate, not completion of reconciliation. No publication approval or Cloudflare deployment is implied.
