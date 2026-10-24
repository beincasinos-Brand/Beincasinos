# Market-record field completeness audit — 24 October 2026

## Scope and method

Parsed the current 33-column `docs/brand-research-template.csv` on branch `feature/directory-global-brand-count-disclosure-2026-10-23`. Counted non-empty cells across all populated market-specific records. This is a structural completeness audit, not proof that a URL works or that its contents support the stated claim.

- Header columns: **33**
- Populated market-specific rows: **204**
- Publication decisions: **202 HOLD**, **2 rejected**
- Records with a non-empty official URL, legal entity, regulator, official register URL, licence scope, allowed-market note, source notes, last-checked date, status and unresolved-issues field: **204/204** each. Non-empty values can still be stale or insufficient.

## Missing fields

| Field | Missing rows | Filled rows | Coverage |
|---|---:|---:|---:|
| Current terms URL | 184 | 20 | 9.8% |
| Withdrawals URL | 200 | 4 | 2.0% |
| Complaints URL | 200 | 4 | 2.0% |
| Responsible-gambling URL | 198 | 6 | 2.9% |
| Partnership contact URL | 204 | 0 | 0.0% |
| Privacy/tracking review status | 62 | 142 | 69.6% |
| Named reviewer | 20 | 184 | 90.2% |

**Interpretation:** a populated operator/register link is not a complete consumer review. The most severe common gap is that none of the 204 records has a partnership-contact URL, while payment/withdrawal and complaints source links are present on only four records each. Current terms links are present on only 20 records. Do not promote these candidates to approved status based on regulator-register evidence alone.

## Market-specific row counts

| Market code | Rows |
|---|---:|
| IT | 46 |
| US-NJ | 30 |
| GB | 23 |
| ES | 19 |
| US-MI | 14 |
| CA-ON | 13 |
| DE | 13 |
| CH | 10 |
| BE | 10 |
| NL | 8 |
| SE | 7 |
| CA-QC | 2 |
| FR | 2 |
| US-PA | 1 |
| CA-BC | 1 |
| DE-SH | 1 |
| EXCLUDED | 1 |
| UNCONFIRMED | 3 |
| **Total** | **204** |

These are market-specific rows, not unique global brands. The source has 154 provisional global IDs in the separately maintained deduplication audit; neither count establishes current eligibility.

## Required next actions

1. Prioritise the current-terms URL for each candidate and capture the actual terms/version date.
2. Add official withdrawal/payment, complaints/ADR and safer-gambling source URLs for each market-specific product.
3. Record privacy/tracking review outcome, not just a URL.
4. Research partnership contacts separately; do not invent addresses or infer a contact from an unrelated support page.
5. Keep all candidates on HOLD until identity, local product permission, terms, consumer protections, image rights and editorial sign-off are complete.
6. Re-run this audit after updates so progress is measurable.

## Limitations

This is a point-in-time parse of the feature-branch CSV. It did not fetch any URL, test product availability, validate a licence beyond the supplied notes, test payments, or check the deployed Cloudflare site. No review has been approved and no deployment or indexing is claimed.
