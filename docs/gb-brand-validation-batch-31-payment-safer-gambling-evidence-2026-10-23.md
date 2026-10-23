# Great Britain casino review evidence — batch 31: payments, complaints and safer-gambling policy pages
**Research date:** 2026-10-23  
**Scope:** Public legal/help pages only. No account, sign-in, deposits, gambling or submitted support requests.  
**Status:** Evidence collection only; no review approved.

## 666 Casino — public terms and help-page findings
Source: https://www.666casino.com/info/terms/
- The terms page fetched successfully and says it was last published **17 August 2026**.
- It identifies Jupiter Gaming Limited and UKGC licence **67098**.
- The terms require identity/age checks and describe possible requests for proof of identity, residence, payment-method ownership and source of funds; transactions may be suspended pending checks.
- The terms' complaints section says customers should contact support, that the query is investigated and the operator aims to respond within **3 working days** unless extended investigation is needed; unresolved complaints can be escalated. Full alternative-dispute-resolution details and the current complaint pathway still need to be checked before review approval.
- The page links to deposit methods, contact us, responsible gambling, privacy policy and fair play. Exact withdrawal fees/timing and current supported methods were not verified in this batch.
- A direct request to `/info/payments/` and `/info/withdrawals/` returned page-not-found errors. This does not prove the information is unavailable elsewhere; the links exposed by the terms page should be followed and recorded in a subsequent pass.

## Lad Casino — payment and safer-gambling pages
Sources: https://www.ladcasino.com/info/payment-methods/ and https://www.ladcasino.com/info/safer-gambling/
- The payment-methods page states a **£10 minimum deposit**, maximum **£2,000 per deposit transaction**, and a **£10 minimum withdrawal** (it says to contact support about smaller withdrawals).
- It lists Visa/Mastercard debit cards as accepted for deposits and withdrawals. The fetched text was short and does not establish processing time, fees, limits by method, or whether other methods are available; do not infer those details.
- The safer-gambling page describes deposit limits based on net deposits, time-out options, self-exclusion periods from **6 months to 5 years**, and explains that operator self-exclusion is different from GAMSTOP. These are the operator's published claims; functionality was not tested inside an account.
- The `/info/contact/` and `/info/payments/` routes returned “Page Unavailable” content in this fetch, while `/info/payment-methods/` and `/info/safer-gambling/` were readable. This is a public-page usability/documentation gap worth recording, not proof that customer support itself is unavailable.
- Current complaint escalation/ADR route, payout processing times, withdrawal restrictions and fees remain unverified.

## What remains open before a publication-ready review
For both brands, no account was created and no transaction or gameplay test was performed. Therefore we have no firsthand evidence for onboarding friction, cashier operation, real withdrawal processing, support response quality, bonus wagering in practice, game fairness testing, or actual account-limit controls. Do not claim any such tests occurred.

Required dossier checks:
1. Resolve the exact official licence/domain/operator relationship and date the evidence.
2. Read the complete payment and withdrawal policy; capture method-specific fees, limits, processing times, verification holds and bonus-related restrictions.
3. Capture the complaint process, named ADR provider and escalation deadlines from current terms.
4. Record responsible-gambling tools as documented policy only unless they are safely testable without creating an account.
5. Inspect current promotion-specific terms before stating bonus values or wagering rules.
6. Add editorial methodology and commercial-affiliate disclosures before any publication approval.

## Batch outcome
- Public policy evidence expanded: 2 brands (666 Casino, Lad Casino).
- Specific published payment limits captured for Lad Casino: £10 min deposit, £2,000 max per deposit transaction, £10 min withdrawal; Visa/Mastercard debit listed.
- Specific published safer-gambling policy details captured for Lad Casino: deposit limits, time-out, 6-month to 5-year self-exclusion, GAMSTOP distinction.
- New publication-approved brands: 0.
- New publication-approved reviews: 0.
- Production deploys, main-branch changes, DNS changes: 0.
