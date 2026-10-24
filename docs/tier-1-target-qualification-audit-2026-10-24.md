# Tier-1 master tracker qualification audit — 24 October 2026

**Status:** Internal data-quality audit; not publication approval.

## Snapshot

Parsed from `docs/tier-1-master-prospect-tracker.csv` on 24 October 2026 after the Pennsylvania target correction.

- Data rows: **106** (excluding header), not 100.
- Rows within the currently permitted research scope (GB, NL, CH, DE, US-NJ, US-PA, US-MI): **104**; 2 category-level exclusions are for FR and AU.
- The `global_brand_id` field is blank on **105 rows**; the Hollywood Casino Online (US-PA) row now has the provisional ID `hollywood-casino`. The remaining cross-market identities still require human reconciliation.
- Columns: 18.
- The Hollywood Casino Online (US-PA) row remains **Hold**, with the PGCB-listed URL `http://www.hollywoodcasino.com`. The PGCB's 2024–2025 Annual Report reports a December 2024 site launch under the Hollywood Casino at Penn National Race Course certificate. The separate legacy `pa.hollywoodcasino.com` URL ended 14 December 2023 and must not be reused. Verify the current HTTPS canonical/redirect and exact customer-contracting entity before publication.
- Publication status: **103 Hold**, 1 Exclude, 1 Exclude from French online-casino listings, 1 Exclude from Australian online-casino listings.
- Willingness to pay: **104 Unconfirmed**, 2 Not applicable. No row is evidence of confirmed paid-listing demand.
- The `official_domain` field is the literal placeholder `VERIFY` in **58 rows**. Two rows use `NOT APPLICABLE`; no row currently uses `UNKNOWN`. The PGCB-listed Hollywood Casino URL is HTTP; its current HTTPS canonical/redirect is still unverified.
- All 106 rows remain unapproved for publication; licence/domain evidence does not substitute for review of the current consumer product.

## Market distribution

| Market code | Rows | Interpretation |
|---|---:|---|
| GB | 69 | Requires exact domain/operator/product checks and current consumer-term review |
| NL | 18 | Requires exact Ksa brand/domain and permit-scope confirmation |
| US-NJ | 7 | New Jersey only; do not generalize to the United States |
| US-PA | 4 | Pennsylvania only; BetRivers is the current regulator-backed replacement lead |
| US-MI | 2 | Michigan only |
| CH | 2 | Swiss register and exact operator/product checks required |
| DE | 2 | Check exact federal/state product scope; Schleswig-Holstein permission is not blanket Germany permission |
| FR | 1 | Keep excluded from French online-casino listings pending applicable legal clearance |
| AU | 1 | Keep excluded from Australian online-casino listings pending applicable legal clearance |

## Data-quality risks

1. The tracker has 106 data rows while project language often refers to a 100-brand target. Do not silently truncate or count duplicates; choose a documented 100-row active scope after eligibility checks.
2. A market code does not prove a brand is currently available or lawful in that market. In the US, each state is a separate scope.
3. The VERIFY placeholder appears in 58 official-domain cells. These rows need primary-source domain identification before they can count as verified candidates. Hollywood Casino Online (PA) has a regulator-listed HTTP URL, but its HTTPS canonical/redirect and customer contract are not yet verified.
4. Most rows remain Hold; commercial willingness-to-pay is unconfirmed for every ordinary prospect.
5. The legacy `docs/brand-prospect-list.md` spans broader regions than the current Tier-1 strategy. Requalify the queue instead of copying its names into public reviews.
6. A regulator entry can confirm an entity, domain or permitted activity, but does not establish that a full consumer-facing review has been tested or independently approved.
7. The PGCB's logo directory and certificate-holder list can differ in granularity: a logo alone is not enough to prove that a specific customer-facing skin/domain is currently authorized.

## Required next steps

1. Keep all rows on Hold until their official domain and exact legal operator are resolved; retain explicit Exclude decisions where the current product scope is not established.
2. Replace each VERIFY only with a domain corroborated by the brand's current official site and the regulator record where one exists; otherwise record UNKNOWN and keep the Hold or Exclude. For Hollywood Casino Online (PA), confirm the secure route and contract entity without treating the retired `pa.hollywoodcasino.com` URL as current.
3. Review each product against current terms, offers, payment/withdrawal disclosures, complaints/ADR, safer-gambling controls, privacy, accessibility and regulatory history.
4. Document an explicit scope decision for the 100-brand target, deduplicate same-brand/market entries, and distinguish prospects from review-ready profiles.
5. Populate a stable global brand identity only after human reconciliation of brand aliases and market variants; do not blindly slug names where two records may be the same brand or operator.
6. Keep paid-listing demand marked Unconfirmed until directly evidenced; do not infer it from a launch, licence or affiliate programme.
7. Update this audit only after the tracker changes and rerun a row-count/domain-placeholder check.

**Decision:** The tracker is a research queue, not a list of 100 completed or approved reviews. Current approved-review count remains **0/100** until the separate publication gate is satisfied.
