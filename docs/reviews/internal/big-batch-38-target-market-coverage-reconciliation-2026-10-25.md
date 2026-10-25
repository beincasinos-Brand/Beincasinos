# Batch 38 — target-market coverage reconciliation

Date: 2026-10-25. Internal portfolio audit against the latest target-market list.

## Target markets
- AU: 0 rows in the current 100-row ledger — online casino acquisition excluded pending legal review
- CA: 0 rows in the current 100-row ledger — Ontario-only evidence must not be presented as nationwide Canada
- GB: 65 rows in the current 100-row ledger
- US: 0 rows in the current 100-row ledger — state-level licence required; do not treat US as a single licence market
- CH: 2 rows in the current 100-row ledger
- DE: 2 rows in the current 100-row ledger
- NL: 18 rows in the current 100-row ledger
- SE: 0 rows in the current 100-row ledger
- ES: 0 rows in the current 100-row ledger
- IT: 0 rows in the current 100-row ledger
- FR: 0 rows in the current 100-row ledger — online-casino acquisition excluded pending legal review
- BE: 0 rows in the current 100-row ledger — Belgian Gaming Commission licence/category check required

## Existing ledger distribution
- CH: 2
- DE: 2
- GB: 65
- NL: 18
- US-MI: 2
- US-NJ: 7
- US-PA: 4

## Gap findings
- The current 100-row ledger contains only CH, DE, GB, NL, US-MI, US-NJ, US-PA as market codes. This is not balanced coverage of the 12 requested target markets.
- Canada appears through US-style/other jurisdiction records in separate work batches but does not have a `CA` row in this 100-row ledger; Ontario evidence is provincial and must not be generalized to the entire country.
- The current ledger uses state-specific US codes (US-PA, US-NJ, US-MI). Keep them separate; an aggregate `US` row must not replace state-level authorisation evidence.
- Australia and France are not gaps to fill with online-casino acquisition pages: the existing compliance gates block that content pending a lawful, reviewed scope.
- Belgium needs exact Belgian Gaming Commission authorisation/category evidence before any local casino acquisition content.
- Sweden, Spain and Italy require current national regulator/operator/domain/product mapping before any candidate can be described as verified.

## Required portfolio actions
1. Do not simply overwrite the fixed 100-row ledger to make the market counts look balanced. First approve a target allocation and deduplication rule.
2. Add a separate market eligibility status per brand/market combination, including exact jurisdiction and product scope.
3. For CA, start with Ontario-regulated operators only when exact iGaming Ontario/AGCO evidence matches the domain and casino product; label the province explicitly.
4. For GB, match each exact consumer domain and operating entity to the Gambling Commission's current register.
5. For CH, use the ESBK list as the initial eligibility source and check individual game approvals as relevant.
6. For DE, match the exact domain/product to the current GGL whitelist and permitted category.
7. For NL, match current Ksa licence holder, domain and product scope; avoid assuming an old candidate is still active.
8. For SE/ES/IT/BE, capture the respective current regulator entry, exact legal operator and local product scope before creating public review copy.
9. Keep AU and FR online-casino acquisition excluded unless qualified legal review establishes a permitted alternative scope.
10. After market eligibility, continue with bonus, payments, consumer tests, image rights and editorial approval; market eligibility alone is not a review score.

## Release status
This is a coverage audit only. No new candidate is cleared, no score is approved, and no row is removed from HOLD by this report. No public pages changed; no merge/deploy performed.
