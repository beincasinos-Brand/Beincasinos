# Batch 32 — 100-row ledger remediation audit

Checked: 2026-10-25 against the current branch ledger. This is an internal QA audit, not a consumer review or licence certification.

## Snapshot

- Ledger rows parsed (excluding header): 100
- Columns: 43
- Rows with overall score blank: 100
- Rows marked publication HOLD: 100
- Rows with consumer test not marked completed: 100
- Rows with image rights not cleared: 100

## Market distribution (ledger snapshot)

- CH: 2
- DE: 2
- GB: 65
- NL: 18
- US-MI: 2
- US-NJ: 7
- US-PA: 4

## Missing field counts

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

## Required remediation order

1. **Identity and jurisdiction:** reconcile exact official domain, contracting legal entity, regulator entry and product scope. A brand or parent-group name alone is insufficient.
2. **Market eligibility:** enforce a separate pass/fail gate per country/province/state. France online casino acquisition content and Australia online-casino content remain excluded pending a valid legal basis; Ontario evidence cannot be generalized to all Canada; US state approvals are not interchangeable.
3. **Evidence bundle:** add dated official sources for terms, cashier, withdrawal limits/fees, complaints/ADR, privacy/cookies, safer gambling and regulatory actions. Record what was actually checked.
4. **Bonus accuracy:** no promotional amount is publication-cleared until full eligibility, wagering, expiry, game exclusions, maximum bet, cashout and payment restrictions are captured from current terms.
5. **Images:** source discovery is not permission. Record a licence/permission or replace with original, commissioned, or otherwise cleared assets; do not publish uncertain logos or casino imagery.
6. **Consumer testing and scoring:** conduct documented mobile/accessibility and cashier/withdrawal tests where lawful and possible; independently review evidence; only then calculate the rubric and seek editorial/legal approval.
7. **Release discipline:** retain HOLD until all mandatory fields and gates pass. Never fill gaps with guessed ratings, generic bonuses, assumed licence claims or fabricated test results.

## Acceptance criteria for each of the 100 rows

A row can move out of HOLD only when the exact domain and product are eligible in its named market, evidence is dated and attached, image rights and affiliate disclosure are cleared, all score components are supported, a second reviewer and editorial/legal approver sign off, and the consumer-test status accurately records what was performed.

## Important interpretation

This audit measures ledger completeness only. A populated URL is not proof that the linked page is current or sufficient; a candidate brand is not a verified authorised product; and a bonus description is not an approved offer. The counts above are the result of parsing the current CSV snapshot and should be re-run after edits.
