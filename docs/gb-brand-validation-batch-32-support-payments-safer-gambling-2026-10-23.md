# GB brand validation batch 32 — support, deposits and safer-gambling policy check

**Research date:** 2026-10-23  
**Status:** Evidence-only; no brand or review approved by this batch.  
**Branch:** `research/gb-batch-32-2026-10-23`  
**Scope:** Public policy/help pages for 666 Casino and Lad Casino. No account was created, no money deposited, no game played, no withdrawal attempted, and no support contact submitted.

## Findings

### 666 Casino

- Public Contact Us page: https://www.666casino.com/contact-us/ says customers with issues should use live chat or email. The extracted page exposed a protected email link (not a safely readable address); live-chat availability and response quality were not tested.
- Safer Gambling page: https://www.666casino.com/info/safer-gambling describes deposit limits (daily/weekly/monthly), limits calculated from net deposits, immediate effect for lower limits and a cooling-off period for increases. It also describes reality checks, time-outs (typically 24 hours to around six weeks), and self-exclusion. These are operator-published descriptions, not independent functionality tests.
- A live fetch of the safer-gambling page succeeded via the non-trailing-slash URL. The trailing-slash URL timed out. The fair-play page produced a browser SSL protocol error in this fetch. The deposit-methods URL returned 404 in this fetch, despite having been reachable in an earlier research batch. Treat these as access/route instability, not proof that the underlying service or payment options do not exist.
- The site links to the UK Gambling Commission domain-name record for account 67098 and external support resources including GAMSTOP, IBAS and GamCare. These links alone do not establish that a specific complaint is eligible for a given ADR scheme; exact complaint/ADR wording and current escalation process remain to be checked.
- The Contact Us page was readable; a separate fetch of the terms page timed out in this batch. Earlier batch evidence recorded terms identifying Jupiter Gaming Limited and UKGC account 67098, last published 17 Aug 2026. Recheck before publication.

### Lad Casino

- Terms: https://www.ladcasino.com/info/terms/ says terms were last published 17 Aug 2026 and identifies Jupiter Gaming Limited as the service provider. The complete licence number/complaints clauses must be taken from the terms/register and verified again at publication.
- Contact Us: https://www.ladcasino.com/contact-us/ says users can consult the FAQ or contact support through live chat/email. Support operation and response time were not tested.
- FAQ: https://www.ladcasino.com/info/faq/ currently contains only “Questions Forthcoming”, so it is not useful as a substantive self-service FAQ at the time of this fetch.
- Deposit: https://www.ladcasino.com/info/deposit/ loads a page titled “Deposit” but the extracted body contains no usable instructions.
- Withdraw: https://www.ladcasino.com/info/withdraw/ displays “This info page is currently unavailable.” This is a specific public-documentation gap, not proof withdrawals themselves are unavailable.
- Earlier batch 31 captured https://www.ladcasino.com/info/payment-methods/ with a £10 minimum deposit, £2,000 maximum per deposit transaction, £10 minimum withdrawal (smaller withdrawals: contact support), and Visa/Mastercard debit cards for deposits/withdrawals. Processing time, fees and other methods were not established. Earlier batch 31 also captured the safer-gambling page describing net-deposit-based limits, time-outs and self-exclusion periods from six months to five years. These claims are operator-published and were not functionally tested.
- The Lad Casino site links to the UKGC domain-name record for account 67098, plus GAMSTOP and IBAS. Current ADR terms and escalation procedure remain a separate evidence task.

## Editorial decision

**666 Casino: HOLD. Lad Casino: HOLD.** Neither is approved as a publication-ready brand/review by this batch. The public pages provide some useful policy evidence, but payment and complaint/ADR coverage remains incomplete, some routes fail or contain empty content, and no hands-on account, transaction, game, withdrawal, or support tests were performed.

## Next evidence required

1. Recheck official UKGC domain-name record and operator/legal entity on the day of publication.
2. Capture complete current terms sections for complaints, ADR, withdrawal processing/fees, KYC/source-of-funds, dormant accounts, bonus terms and jurisdiction restrictions.
3. Confirm the exact payment-method list and all minimum/maximum limits from an accessible official page; distinguish deposits from withdrawals.
4. Capture the full safer-gambling wording, including self-exclusion, GAMSTOP, cooling-off and support referrals.
5. Conduct lawful, documented hands-on tests only where an authorized test account is available; record timestamps, steps and outcomes. Do not invent first-hand experience.
6. Apply the shared review evidence dossier template and editorial/legal sign-off before publication.

## Batch outcome

- New verified-and-approved brands: **0**
- New publication-approved reviews: **0**
- Production deploys / main-branch changes / DNS changes: **0**
