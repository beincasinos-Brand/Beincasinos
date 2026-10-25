# 100-slot ledger audit — 25 October 2026

**Source inspected:** `docs/targets/100-brand-review-production-ledger-2026-10-24.csv` on `main` at commit `bdc1a4421d59c4c49b37ebb466bc04cd86d0270f`.  
**Purpose:** turn the current ledger into an actionable completion queue. This is a read-only audit; the source ledger was not changed.

## Snapshot

- Ledger rows: **100**
- Non-empty rows: **100**
- Distinct values in the current `global_brand_id` field: **100**
- Review status: **100 HOLD — candidate/evidence work incomplete**
- Publication status: **100 HOLD — not approved for publication**
- Rows with bonus information recorded as not captured: **89**
- Rows with a captured bonus/promotion note: **11**, but the notes themselves say several offers have conflicts or incomplete full terms; none is automatically publication-cleared.
- Scores: no overall score is approved in the inspected first rows; score fields must not be populated from guesswork.

**Interpretation:** the 100-slot ledger exists and contains useful leads, but this is not 100 verified brands or 100 completed reviews. The operational target now is to move rows through identity verification, full evidence capture, scoring, second review and release—not to add a hundred more names.

## Market distribution in the ledger

| Market code | Rows |
|---|---:|
| GB | 10 |
| BE | 7 |
| SE | 6 |
| NL | 7 |
| DE-SH | 2 |
| CH | 9 |
| IT | 9 |
| ES | 9 |
| CA-ON | 9 |
| CA-BC | 1 |
| CA-QC | 2 |
| US-NJ | 9 |
| US-MI | 9 |
| US-PA | 2 |
| DE | 9 |

The ledger uses market-specific codes; for reporting against the twelve-market plan, combine US state codes under US and Canadian province codes under CA, but retain the subnational code in each actual evidence record. The table shows 100 slots across 15 codes, not 15 countries.

## Immediate data-quality risks

1. **Bonus copy is not the same as verified current terms.** Some rows contain headline values or an offer-page summary but lack complete conditions, expiry, max cashout, excluded games/payment methods, or a current eligibility check.
2. **Licence scope must remain narrow.** A German state-scoped casino permission (for example, Schleswig-Holstein) is not nationwide German authorisation. A state/province licence must remain labelled with its state/province.
3. **Domain/operator matching is not interchangeable.** A regulator entry for one entity or domain must not be reused for a sibling brand or redirect without evidence.
4. **A blank image URL and pending rights mean no approved logo/image.** Do not scrape competitor artwork or use a brand mark without a defensible usage basis.
5. **Testing claims are currently constrained.** A row marked NOT PERFORMED cannot be described as hands-on tested. A review may still summarise documented terms, but it must clearly distinguish desk research from actual consumer testing.
6. **Second review is mandatory.** One researcher’s notes are not independent editorial approval.

## Suggested completion order

### Batch A — resolve identity and market gate first
Prioritise rows with a current regulator URL and an apparent exact-domain record. Re-open the regulator record, confirm current status and product scope, verify the contracting entity from terms, and store a dated evidence note. If a material conflict appears, HOLD or EXCLUDE.

### Batch B — close consumer terms
For every row that passes Batch A, capture current official terms, payment/withdrawal rules, complaints/ADR, safer-gambling controls, privacy/cookies and regulatory-action history. Record the exact page URLs and UTC check date.

### Batch C — bonuses and images
Only after market eligibility is clear, capture the exact current bonus rules and distinguish a welcome offer from a game-specific promotion. Resolve image permission separately; a brand logo is not automatically free to reuse.

### Batch D — score and independent review
Apply the repository's weighted scoring method only when evidence is sufficient. Document unknowns, score rationale, and material limitations. Require a second editor to check citations, market eligibility, claims and disclosures.

### Batch E — release controls
Only approved reviews may be rendered publicly. Check the page route, canonical, metadata, internal links, mobile layout, accessible image text, affiliate disclosure and sitemap inclusion. No batch should trigger a deployment until the release gates pass.

## Required count dashboard

Track these as separate measures every session:

| Metric | Current evidence-based state |
|---|---:|
| Ledger slots filled | 100 |
| Rows on HOLD | 100 |
| Fully verified unique brands | Not established by this audit |
| Market-eligible brands | Not established by this audit |
| Evidence-complete reviews | Not established by this audit |
| Second-editor-approved reviews | 0 established by this ledger snapshot |
| Public review pages released from this ledger | 0 established by this ledger snapshot |
| Pages indexed by Google from this ledger | Not established by this audit |

Do not infer verified/public/indexed counts from file count, slot count, sitemap size or a successful sitemap submission.

## Next action

Work the existing 100 rows one by one, starting with exact domain + legal operator + regulator permission. Update the ledger only when the relevant evidence is present, and keep each row on HOLD until every required gate passes. The 12-market eligibility protocols in this branch provide the market-specific checklist.
