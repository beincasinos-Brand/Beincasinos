# Global brand deduplication and target reconciliation — 24 October 2026

**Status:** Internal control document; not for publication.  
**Source of truth checked:** `docs/brand-research-template.csv` on branch `ops/2026-10-24-target-reconciliation-and-release-gates`, current file SHA `85f2fd4c08bf462185dcb0da0d1de2583eb25d74`.  
**Purpose:** reconcile raw market records against canonical global brand identities and prevent research leads from being counted as verified or approved reviews.

## Exact snapshot

| Measure | Verified snapshot |
|---|---:|
| Market-specific candidate/research records | 204 |
| Nonblank canonical `global_brand_id` values | 154 |
| IDs appearing in more than one market/row | 30 |
| Records marked `evidence captured` | 163 |
| Records marked `research` | 28 |
| Records marked `research lead — unverified` | 4 |
| Records marked `scope triage` | 7 |
| Records explicitly rejected | 2 |
| Records whose publication decision is `HOLD` | 202 |
| Publication-approved reviews | **0/100** |

The 154 IDs are provisional identity buckets, not 154 verified eligible casinos. Some IDs still need product-scope/legal checks, some have market/domain/contracting-entity uncertainty, and multiple rows may refer to one brand in different jurisdictions. The 163 “evidence captured” rows do not mean the consumer review evidence is complete; the publication-decision field remains HOLD for those rows.

## Current target-market raw-row counts

| Market code | Rows | Notes |
|---|---:|---|
| GB | 23 | Exact live domain, active Casino Remote permission, terms and enforcement still required |
| IT | 46 | Largest buffer; some entries are broad remote-gambling leads rather than proven casino products |
| ES | 19 | Exact DGOJ casino permission and current product evidence still required |
| US-NJ | 30 | State-specific; rows are not distinct operators |
| US-MI | 14 | State-specific; rows are not distinct operators |
| US-PA | 1 | State-specific lead |
| CA-ON | 13 | Ontario only |
| CA-BC | 1 | British Columbia only |
| CA-QC | 2 | Québec only; confirm local product scope and legal entity |
| CH | 10 | ESBK-listed platform leads; game-specific approvals and contracts remain |
| BE | 10 | Belgium A+ domain rows; nine dossier rows in the current surfaced A+ table because Circus and PokerStars share one record, with Betsson now surfaced on the current domain |
| NL | 8 | Deduplicate shared operator and brand/domain variants |
| SE | 7 | Exact domain/product and current register checks remain |
| DE | 13 | Mixed general and Schleswig-Holstein-specific scope; do not infer nationwide casino permission |
| DE-SH | 1 | State-specific; avoid double counting with DE rows |
| FR | 2 | Online casino is not generally authorised; do not count these as eligible casino brands without a lawful product-specific basis |
| UNCONFIRMED | 3 | Do not count until a named target market and local route are evidenced |
| EXCLUDED | 1 | Archive only; not part of the eligible target |

The raw counts above sum to 204. State/province variants and same-brand cross-market rows are deliberate research coverage, not additional global brands.

## Global duplicate groups requiring explicit one-brand counting

These canonical IDs already have multiple rows and must be counted once globally, even if separate market-specific reviews are eventually approved:

| Canonical ID | Row count | Market records represented |
|---|---:|---|
| `bet365-casino` | 5 | GB, NL, US-MI, DE, US-NJ |
| `888casino` | 4 | GB, ES, SE, IT |
| `pokerstars-casino` | 4 | GB, BE, ES, US-NJ |
| `betsson` | 4 | Unconfirmed, BE, IT, SE |
| `betway` | 3 | GB, ES, DE |
| `leovegas` | 3 | GB, IT, DE |
| `unibet-casino` | 3 | GB, BE, SE |
| `bwin` | 3 | GB, BE, ES |
| `betano` | 3 | GB, BE, DE |
| `betmgm-casino` | 3 | GB, US-MI, US-NJ |
| `draftkings-casino` | 3 | CA-ON, US-MI, US-NJ |
| `fanduel-casino` | 3 | CA-ON, US-MI, US-NJ |
| `betrivers-casino` | 3 | CA-ON, US-MI, US-NJ |
| `hard-rock-bet-casino` | 3 | CA-ON, US-MI, US-NJ |
| `fanatics-casino` | 3 | CA-ON, US-MI, US-NJ |
| `william-hill-casino` | 2 | GB, ES |
| `ladbrokes-casino` | 2 | GB, BE |
| `betfair-casino` | 2 | GB, ES |
| `casumo` | 2 | GB, DE |
| `codere` | 2 | ES, IT |
| `caesars-palace-online-casino` | 2 | CA-ON, US-NJ |
| `bally-bet-casino` | 2 | CA-ON, US-NJ |
| `winamax` | 2 | FR, ES |
| `betparx-casino` | 2 | US-PA, US-NJ |
| `casino777` | 2 | CH, BE |

Five further duplicate groups also exist in the CSV (30 repeated groups total). Re-run this reconciliation after every registry change; do not hard-code the 154 count into a public page.

## Known scope and exclusion blockers

- `32red` — excluded because the current GB casino permission/domain was not active in the checked evidence.
- `betfred` — Spanish casino record rejected because DGOJ casino licences were extinguished in 2023; this does not automatically exclude unrelated markets, but the Spanish row must not count.
- `betsson`, `nordicbet-casino` — unconfirmed market route needs to be resolved before counting the affected row.
- `betano`, `comeon-casino`, `betclic`, `winamax`, `espacejeux` — one or more rows remain in scope triage. A brand's existence or permission in one country does not resolve another market's legal scope.
- Australia and France must not be padded with offshore online-casino offers where online casino is generally prohibited.
- Canada and the US must remain province/state/tribal-specific; do not represent one local permission as nationwide authorisation.

## Belgium batch correction

The current surfaced official A+ table includes dossier 595153 with `betssoncasino.be`, Casino Middelkerke x Betsson, SA/NV EXPLOITATIE CASINO MIDDELKERKE, listed expiry 22 February 2039. Earlier captured data associated that dossier with `betfirstcasino.be`. The brand/domain transition remains a live-contract blocker. Belgium A+ evidence memo and internal drafts are updated, and separate B+ online gaming-arcade leads are explicitly kept outside the A+ count.

## Next execution gates

1. Resolve the seven scope-triage IDs and three unconfirmed-market rows.
2. Recheck the 30 duplicate groups against the global identity ledger and remove spelling/alias variants.
3. For each surviving candidate, capture current regulator permission for the exact casino product and consumer domain.
4. Capture current contract, casino bonus rules, payment/withdrawal policy, complaints/ADR, safer-gambling tools, privacy/cookies, accessibility and dated enforcement history.
5. Record consumer UX/support checks only if actually performed and lawful; do not invent deposit/withdrawal tests.
6. Obtain a second reviewer and editorial/legal approval for each original review.
7. Mark a global brand “counted toward 100” only when its canonical identity is unique and at least one eligible market review has passed all gates; separately count completed market-specific reviews.

**Current truth:** 204 market rows; 154 provisional global identity buckets; 0 publication-approved reviews. This audit improves counting discipline, not the approved-review total.
