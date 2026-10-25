# Batch 18 — 100-brand ledger reconciliation audit

Audit date: 2026-10-25
Source ledger: `docs/targets/100-brand-review-production-ledger-2026-10-24.csv`
Source blob SHA audited: `1006fee40ffdf29cf54ffcedca60714406110dea`

## Actual ledger snapshot

- 100 brand rows; 43 columns.
- 0 rows have an overall score.
- 100/100 rows have publication status HOLD.
- 100/100 rows have consumer testing marked NOT PERFORMED.
- 76/100 rows are missing at least one core identity/evidence field among official URL, legal entity, regulator, official register URL, terms URL, review status, or publication status.
- Image-rights status: 47 rows have a source but rights remain pending; 48 have no image source and need an editorial fallback; 5 explicitly say rights are not cleared. No row should use an unlicensed operator logo as if permission were granted.

### Market distribution in the ledger

| Market code | Rows |
|---|---:|
| GB | 65 |
| NL | 18 |
| US-PA | 4 |
| US-NJ | 7 |
| US-MI | 2 |
| CH | 2 |
| DE | 2 |
| **Total** | **100** |

## Critical reconciliation findings

1. The latest approved target geography set is AU, CA, GB, US, CH, DE, NL, SE, ES, IT, FR and BE. The ledger currently has no AU, CA, SE, ES, IT, FR or BE rows.
2. The ledger uses state-specific US codes (US-PA, US-NJ, US-MI), which must remain state/product-specific for eligibility. Do not flatten these into a generic claim that a casino is available across the United States.
3. A 100-row ledger is not the same as 100 publish-ready reviews. Scores are blank, publication is on hold, consumer tests have not been performed, and image rights are unresolved across all rows.
4. Adding more draft batches without reconciling their exact domain, contracting operator, licence scope and row identity increases duplication risk. Do not copy candidate batches into the production ledger solely to make the row count look complete.
5. Australia requires a separate compliance gate: ACMA states online casinos are prohibited services under the Interactive Gambling Act and prohibited services must not be advertised in Australia. See https://www.acma.gov.au/interactivegambling and https://www.acma.gov.au/investigations-online-gambling-providers. Do not build Australian-facing online-casino bonus rankings or affiliate acquisition pages without a legal review of the permitted informational scope.

## Required next actions — ordered

1. Reconcile each of the existing 100 rows to one canonical brand/domain/operator identity; flag aliases and duplicates rather than guessing.
2. Verify the exact regulator register entry and product/territory scope for every market-specific row using the current official register.
3. Capture dated, offer-specific bonus terms only when accessible and current; otherwise mark NOT VERIFIED and omit offer claims from public cards.
4. Keep all scores blank until evidence exists for every rubric component and independent review is complete.
5. Replace unlicensed brand imagery with neutral, properly licensed assets or original artwork; track permission evidence for every logo/screenshot.
6. Add missing target markets only after a legal-market eligibility gate and verified operator/domain shortlist; do not create empty placeholders or inflate the 100 count.
7. Perform and record consumer-flow/accessibility tests, affiliate disclosure review, second-person review, and editorial/legal approval before changing any publication status from HOLD.

## Release decision

**NO-GO for public publication of these 100 rows as finished reviews.** This is a data-quality and compliance audit only. No score was assigned, no unsupported offer was added, and no deployment or merge was performed.
