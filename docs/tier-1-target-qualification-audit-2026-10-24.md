# Tier-1 prospect-tracker qualification audit — 24 October 2026

**Status:** Internal data-quality audit; not publication approval.

## Current snapshot

Parsed from `docs/tier-1-master-prospect-tracker.csv` on 24 October 2026.

- Data rows: **114** (excluding header); this is a mixed market-specific research queue, not 100 approved reviews.
- Rows within the current roadmap/supplemental research scope: **112** across GB, BE, SE, DK, ES, IT, NL, DE/DE-SH, CH, CA-ON, US-NJ, US-PA and US-MI. Two category-level exclusions remain for FR and AU.
- Columns: **18**. No malformed-width rows and no duplicate brand/market keys were found in the latest quote-aware parse.
- `global_brand_id` is populated for **15 rows**, representing **14 distinct IDs** because `bet365-casino` is shared across two market rows. The remaining **99 rows** have blank IDs, so global deduplication is incomplete.
- Publication status: **111 Hold**, 1 Exclude, 1 Exclude from French online-casino listings, and 1 Exclude from Australian online-casino listings.
- Willingness to pay remains unconfirmed for all ordinary prospects. No row is evidence of confirmed paid-listing demand.
- The `official_domain` field is `VERIFY` in **58 rows** and `NOT APPLICABLE` in **2 rows**. No row currently uses `UNKNOWN`; the PGCB-listed Hollywood Casino URL is HTTP, and its HTTPS canonical/redirect plus customer-contracting entity remain unverified.
- All 114 rows remain unapproved for publication; regulator/domain evidence is not a substitute for current terms, cashier/withdrawal checks, complaints/RG/privacy/accessibility review, documented testing, image rights and independent sign-off.

## Market distribution

| Market code | Rows | Interpretation |
|---|---:|---|
| GB | 70 | Exact domain/operator/product checks and current consumer-term review required |
| NL | 18 | Confirm current Ksa brand/domain notification and permit scope |
| US-NJ | 7 | New Jersey only; do not generalize to the United States |
| US-PA | 4 | Pennsylvania only; verify exact domain and customer-contracting entity |
| US-MI | 2 | Michigan only; verify exact operator/platform roles and customer terms |
| CH | 3 | Swiss register, operator and game-permission checks required |
| DE-SH | 1 | Territory-limited Tipico scope; not nationwide Germany |
| DE | 1 | State/product scope must be explicit; Schleswig-Holstein permission is not nationwide German permission |
| BE | 1 | Belgian Gaming Commission domain/operator and A+ licence scope must match the product |
| SE | 1 | Swedish licence, domain and current customer terms must match |
| DK | 1 | Danish licence and exact casino product/domain must match |
| ES | 1 | DGOJ current authorisation and domain match required |
| IT | 1 | ADM concession/domain and current terms required |
| CA-ON | 1 | Ontario-specific registration and customer-contract checks; no province-wide generalization |
| FR | 1 | Excluded from French online-casino listings pending applicable legal clearance |
| AU | 1 | Excluded from Australian online-casino listings pending applicable legal clearance |

## Data-quality risks

1. The tracker has 114 rows while the programme goal is 100 globally unique brands. Choose a documented 100-brand cohort after identity and eligibility review; do not silently truncate the queue.
2. Fifteen rows currently have a populated global ID, representing 14 distinct IDs; 99 rows still lack one. Brand aliases, white-label relationships and market variants require human reconciliation before the cohort can be described as 100 unique brands.
3. The `VERIFY` placeholder appears in 58 official-domain cells. These entries need primary-source domain identification before they can count as verified candidates.
4. Market permission is not transferable: US states are separate scopes, Tipico is Schleswig-Holstein-specific, and Ontario/European permissions do not imply broader national or international availability.
5. The legacy `docs/brand-prospect-list.md` covers regions outside the current programme. Requalify the queue rather than copying its names into public reviews.
6. A regulator entry can confirm a domain, entity or permitted activity but does not establish consumer quality, firsthand testing, review approval or willingness to buy a paid listing.
7. Hollywood Casino Online (PA) is a HOLD lead: the PGCB's 13 February 2026 certificate-holder list names `http://www.hollywoodcasino.com` for slots/table games with a 19 December 2024 commencement date. The older `pa.hollywoodcasino.com` URL ended 14 December 2023. Verify HTTPS canonical/redirect and the customer-contracting entity.

## Required next steps

1. Keep all rows on Hold until the current official domain, legal operator and product scope are resolved; retain explicit Exclude decisions where scope is not established.
2. Replace each `VERIFY` only with a domain corroborated by the brand's current official site and regulator record where one exists; otherwise record `UNKNOWN` and keep Hold/Exclude status.
3. Review current terms, offers, payment/withdrawal disclosures, complaints/ADR, safer-gambling controls, privacy, accessibility and regulatory history for each product.
4. Map the candidate register to global IDs manually; the separate candidate-to-global-ID map currently has 39 provisional mappings and 61 unresolved candidates.
5. Document an explicit 100-brand cohort and market scope. Deduplicate same-brand/market records before claiming progress against the goal.
6. Keep paid-listing demand Unconfirmed until directly evidenced; do not infer it from a licence, launch, domain or affiliate programme.
7. Update this audit only after tracker changes and rerun the row-count, schema, duplicate-key and domain-placeholder checks.

**Decision:** the tracker is a research queue, not a list of 100 completed or approved reviews. Current approved-review count remains **0/100** until each separate publication gate is satisfied.
