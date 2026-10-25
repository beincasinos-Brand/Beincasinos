# Big Batch 72 — UKGC domain and enforcement evidence pass
Date: 2026-10-25
Scope: official register cross-checks for selected GB ledger entries; record only source-supported evidence.

## Findings and ledger changes
### BetWright — slot 64
- UKGC domain register identifies `betwright.com` as **Active** under Onyx Gaming Limited, account 64666: https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/64666
- UKGC licence summary lists Casino Remote permission as Active: https://www.gamblingcommission.gov.uk/public-register/business/detail/64666
- Ledger now records `domain_verification_status=VERIFIED`, date 2026-10-25, and the official domain-register URL.
- This flag is limited to domain/operator evidence; BetWright remains HOLD / NOT SCORED pending current product terms, withdrawals, complaints, safer-gambling, privacy, bonus terms, image rights, consumer testing, independent review and editorial/legal approval.

### Kong Casino — slot 62
- UKGC domain register for Jumpman Gaming Limited, account 39175, classifies `kongcasino.com` as **White Label**, not Active: https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/39175
- Do not convert this into an Active-domain verification or claim Jumpman is necessarily the direct contracting operator without checking the live site's legal terms and the white-label arrangement.
- Ledger intentionally remains UNVERIFIED / HOLD / NOT SCORED.

### QuinnBet Casino — slot 60
- Added the UKGC enforcement notice to the ledger's `regulatory_actions_url`: https://www.gamblingcommission.gov.uk/news/article/quinnbet-gibraltar-limited-to-pay-gbp609-104-for-regulatory-failures
- The notice, published 20 August 2026, says QuinnBet (Gibraltar) Limited agreed to pay £609,104 following findings concerning anti-money-laundering and social-responsibility controls. This is a material due-diligence signal that should be transparently discussed in a future review, with context and the operator's response verified before publication.
- No score assigned; slot remains HOLD / NOT SCORED. This notice alone does not establish current product performance or current customer outcomes.

## Guardrails
- The UKGC public register explains that domain/trading names are supplied by the gambling business and may not be independently guaranteed: https://www.gamblingcommission.gov.uk/public-register/businesses
- Never turn an official domain entry into a fabricated bonus, payment test, UX rating, or hands-on review.
- No tests run, no merge, no workflow run, and no deployment performed.
