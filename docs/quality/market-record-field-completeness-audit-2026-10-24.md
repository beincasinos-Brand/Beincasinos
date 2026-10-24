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
| Current terms URL | 181 | 23 | 11.3% |
| Withdrawals URL | 196 | 8 | 3.9% |
| Complaints URL | 197 | 7 | 3.4% |
| Responsible-gambling URL | 192 | 12 | 5.9% |
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


## Source-link remediation pass — 24 October 2026

Updated four Great Britain market rows in `docs/brand-research-template.csv` with official operator help/terms sources:
- **bet365 Casino:** added the official GB terms page to terms, withdrawals, complaints and safer-gambling source fields; the page contains relevant sections 11, 25 and 29, so this is one shared source, not four independent policies.
- **William Hill Casino:** added official UK/Jersey/Gibraltar terms, UK complaints procedure and UK safer-gambling tools.
- **Grosvenor Casinos:** added the official terms page for terms, withdrawal-policy research and safer-gambling source; dedicated complaints/ADR source remains unresolved.
- **Paddy Power Games:** added the official general terms page for terms/withdrawal/safer-gambling research and its official complaints procedure.

The CSV now has **23/204 terms URLs, 8/204 withdrawal URLs, 7/204 complaints URLs and 10/204 safer-gambling URLs**. These fields are source leads only: shared URLs may cover several sections, and page presence does not mean the policies were fully reviewed or that the live product/contracting entity was matched. All four rows remain **HOLD**. No partnership contacts were guessed. No consumer review was approved, no Actions workflow was triggered and no Cloudflare deployment was performed.


### Additional safer-gambling source pass

Added official Great Britain safer-gambling sources for **Betway Casino** and **Betfred Casino** on 24 October 2026. Betway's official GB casino slots page describes account controls; Betfred's official safer-gambling FAQ identifies Petfre (Gibraltar) Limited and UKGC account 39544. These are operator sources, not independent usability tests. Current coverage is **12/204** rows with a safer-gambling URL; **192/204** remain blank. Both records remain HOLD.
