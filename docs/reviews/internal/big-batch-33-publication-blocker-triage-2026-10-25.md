# Batch 33 — 100-brand ledger: publication-blocker triage and next-action queue

Date: 2026-10-25. Internal operations artifact generated from the current 100-row ledger. This batch prioritises the next work so the project stops treating a candidate list as finished reviews.

## Snapshot from current ledger

- Rows: 100; columns: 43
- Missing field counts are literal blank-cell counts, not claims that nonblank evidence is sufficient.
- `official_url`: 40 blank
- `legal_entity`: 0 blank
- `regulator`: 0 blank
- `official_register_url`: 0 blank
- `terms_url`: 76 blank
- `withdrawals_url`: 83 blank
- `complaints_url`: 86 blank
- `responsible_gambling_url`: 78 blank
- `bonus_offer_url`: 77 blank
- `bonus_checked_utc`: 72 blank
- `image_source_url`: 50 blank
- `image_rights_status`: 0 blank
- `deposit_methods_url`: 85 blank
- `fees_limits_url`: 85 blank
- `privacy_cookies_url`: 85 blank
- `accessibility_evidence_url`: 100 blank
- `regulatory_actions_url`: 99 blank
- `adr_url`: 99 blank
- `reviewer_primary`: 100 blank
- `reviewer_secondary`: 100 blank
- `independent_review_date`: 100 blank
- `editorial_approval_date`: 100 blank
- `affiliate_disclosure_status`: 0 blank
- `evidence_bundle_path`: 93 blank
- `overall_score`: 100 blank
- `consumer_test_status`: 0 blank

## Priority queue

### P0 — Stop invalid or unverified candidates from looking publication-ready
1. Keep all rows `HOLD` and `NOT SCORED` until exact brand/domain/operator/product scope is reconciled with the regulator for the named market.
2. Rows without an official domain or legal-operator match are identity leads only. Resolve exact canonical domain first; otherwise mark `IDENTITY UNRESOLVED` and do not create public review copy.
3. For US rows, bind each candidate to the exact state regulator and licensed operator; a parent brand, another state, or sportsbook approval does not establish casino eligibility.
4. For European rows, verify the current national register and exact online casino product. Do not treat a company name or a domain alone as proof of current authorisation.
5. Keep France-targeted online-casino acquisition excluded and Australia online-casino promotion excluded pending an applicable legal basis.

### P1 — Evidence capture (one record per domain/product/market)
Required evidence bundle:
- Official regulator entry and date checked.
- Operator's legal entity and customer-contracting terms.
- Casino product page and country/state eligibility.
- Current bonus terms and expiry, or explicit `NO OFFER VERIFIED`.
- Cashier/deposit page, withdrawals page, fees/limits and identity-verification rules.
- Complaints path, ADR/escalation and regulator complaint route.
- Safer-gambling tools, self-exclusion and age/geolocation restrictions.
- Privacy/cookies and accessibility evidence.
- Regulatory actions and sanctions search, including date and scope.
- Image source plus documented permission/licence; otherwise use an original neutral editorial graphic, not a copied logo.

### P2 — Real testing and review score
- Mark consumer testing only after a named tester records date, device/browser, region eligibility, task steps and observed result. Never claim a real-money withdrawal test unless one was lawfully and actually performed.
- Score each of the nine rubric dimensions against cited evidence; do not give points merely because a page exists.
- Independent reviewer checks identity, terms, calculations, score and claims; editorial/legal approval remains separate from affiliate/business relationships.
- Record affiliate disclosure status and placement before any outbound commercial link.

### P3 — Content completeness and visual quality
- Use a consistent premium review template: operator/licence, availability by market, game categories, bonus terms, deposits/withdrawals, verification, support/complaints, responsible-gambling controls, privacy, pros/cons, methodology, evidence date and affiliate disclosure.
- No fake user ratings, fabricated personal experience, invented scores, generic bonus amounts or unlicensed brand assets.
- If a section cannot be verified, show a clear “not verified” status internally and omit the unsupported consumer claim rather than filling the gap.

## Per-row acceptance gate

A row may advance from HOLD only if all apply:
- Exact canonical domain, legal entity, regulator and casino product match.
- Named market eligibility passes.
- Dated primary-source evidence is stored and sufficient for every published claim.
- Bonus and payments are current and accurately qualified, or omitted.
- Image rights are cleared or an original fallback is used.
- Consumer-test status is truthful and evidence-backed.
- Score is calculated from the approved rubric and independently reviewed.
- Affiliate disclosure, editorial approval and legal review are recorded.

## Next execution sequence

1. Resolve rows with blank official domains and identity mismatches first; do not silently guess their URLs.
2. Finish exact regulator/operator mapping for the highest-priority target markets.
3. Replace rights-pending images with cleared neutral assets where feasible.
4. Complete dated terms/cashier/safer-gambling evidence bundles.
5. Conduct actual tests and independent review; only then prepare publication copy.
6. Re-run the ledger audit and compare field-level counts before requesting any release.

**No publication clearance is granted by this report.** The current ledger remains a research backlog, not 100 completed reviews. No public content, merge or deployment was changed.
