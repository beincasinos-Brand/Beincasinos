# Big Batch 74 — ledger integrity read-back after UKGC evidence
Date: 2026-10-25

## Read-back results
The CSV was fetched again from the working branch after the Batch 72–73 edits and parsed with CSV quote handling (including embedded commas/newlines).

- Data rows: 100
- Header columns: 46
- Rows whose `domain_verification_status` is exactly `VERIFIED`: 8
- Rows with a populated numeric overall score: 0
- Market distribution remains: GB 65, NL 18, US-PA 4, US-NJ 7, US-MI 2, CH 2, DE 2.

## Eight exact-domain evidence rows
| Slot | Brand | Market | Official evidence |
|---:|---|---|---|
| 1 | admiral.ch | CH | https://www.esbk.admin.ch/en/online-gambling/ |
| 2 | casineo.ch | CH | https://www.esbk.admin.ch/en/online-gambling/ |
| 35 | Betty Casino | GB | https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/100695 |
| 37 | FruitKings | GB | https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/100050 |
| 47 | Peachy Games | GB | https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/100050 |
| 48 | Play Sunny | GB | https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/100050 |
| 64 | BetWright | GB | https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/64666 |
| 67 | TigerBet | GB | https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/65319 |

## Interpretation and release boundary
- The eight records are narrow official-domain identity evidence only.
- The 100-row ledger remains a candidate ledger; it is not 100 completed or publishable reviews.
- No numeric scores are populated. Do not generate or publish a score without the required category evidence and review process.
- All records remain HOLD / NOT SCORED until current terms, withdrawal/payment evidence, complaints, safer-gambling, privacy, bonus terms, image rights, consumer testing, affiliate disclosure, second review, and editorial/legal approval are completed as applicable.
- Coverage remains unbalanced and incomplete for the requested 12 markets. AU, CA, SE, ES, IT, FR and BE are absent from the current 100-row ledger; market eligibility and local legal constraints must be resolved before adding or promoting brands.

## Execution status
This was a read-back audit, not a test-suite run. No automated tests were run; no merge, workflow run, or deployment was performed.
