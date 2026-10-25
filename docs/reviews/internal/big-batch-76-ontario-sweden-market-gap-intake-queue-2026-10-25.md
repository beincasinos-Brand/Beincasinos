# Big Batch 76 — Ontario and Sweden market-gap intake queue
Date: 2026-10-25
Status: research queue only. Not a licence confirmation, consumer review, endorsement or publication approval.

## Work completed
Created machine-readable intake queue:
`docs/targets/ca-on-se-candidate-intake-queue-2026-10-25.csv`

It contains 20 candidates split across two missing target-market codes:
- 10 Ontario-only (CA-ON) site/operator leads from the existing iGaming Ontario directory matrix.
- 10 Sweden candidate leads that require a fresh exact-domain and licence-register check.

Every row starts with review and publication status HOLD; score status NOT SCORED; bonus status NOT CLEARED; image rights NOT CLEARED. Ontario entries are explicitly marked RECHECK CURRENT DIRECTORY because the prior matrix cites a directory snapshot accurate as of 1 September 2026. Sweden candidates are NOT VERIFIED because the current regulator register has not been matched against each exact domain.

## Ontario queue
Bet99, Caesars, Horseshoe Online Casino, BetMGM Casino, Betty, Jackpot City, Royal Vegas, Ruby Fortune, Spin Casino, and Betway.
Primary source: https://igamingontario.ca/en/operator/operators
Scope is Ontario only. This is not nationwide Canada authorisation.

## Sweden queue
888 Casino Sweden, 44Aces Sweden, Betinia Sweden, BetMGM Sweden, Betsafe Sweden, Boost Casino, Golden Bull, Hajper, Happy Casino, and OneCasino.
Primary source for exact current re-check: https://www.spelinspektionen.se/licens-o-tillstand/licensregister/
The names and URLs are candidate leads only; no current licence or domain match is asserted.

## Intake requirements
Before moving any queue row into the 100-brand production ledger:
1. Re-open the regulator's current register and capture access date, exact site/domain, legal entity, licence status and permitted casino product.
2. Capture official terms, bonus conditions, deposits/withdrawals, fees/limits, complaints/ADR, safer-gambling and privacy evidence.
3. Verify image rights or use documented original artwork.
4. Record real consumer-test status, score rubric evidence, primary/secondary reviewer, affiliate disclosure and editorial/legal approval.
5. Preserve the jurisdiction code (CA-ON, not generic CA); never treat a Swedish-language page as proof of Swedish authorisation.

## Current milestone impact
This expands structured intake work for two markets previously absent from the 100-row ledger. It does not add unverified candidates to the production ledger, change scores, or make any review publishable. Current production ledger stays 100 rows; no automated tests run, no merge, no workflow run, and no deployment performed.
