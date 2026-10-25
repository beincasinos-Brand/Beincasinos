# Big Batch 71 — verified-domain register and publication-boundary audit
Date: 2026-10-25
Scope: validate ledger status fields and document the boundary between domain identity and publication readiness.

## Snapshot verified from the current branch ledger
- Ledger rows: 100
- Header fields: 46
- Rows with `domain_verification_status=VERIFIED`: 3
- The three records are:
  - Slot 1 — admiral.ch (CH), evidence: https://www.esbk.admin.ch/en/online-gambling/
  - Slot 2 — casineo.ch (CH), evidence: https://www.esbk.admin.ch/en/online-gambling/
  - Slot 67 — TigerBet (GB), evidence: https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/65319
- Remaining 97 rows do not currently carry the exact VERIFIED state in that field.

## What the verified flag means
The flag is deliberately narrow: a dated official register source has been recorded as evidence for the exact brand/domain identity lead. It does not certify:
- the completeness of the current product or country availability;
- the operator's full legal relationship to every white-label or group brand;
- current bonus availability or any wagering/withdrawal term;
- payment reliability or any consumer deposit/withdrawal test;
- complaint outcomes, customer support quality, or safer-gambling tools;
- privacy, cookies, accessibility or mobile UX;
- image reuse rights;
- the final rubric score, second review, affiliate disclosure or editorial/legal approval.

## Release gate status
All three records remain `HOLD / NOT SCORED`. Do not display a numerical score or imply hands-on consumer testing until evidence fields and approvals required by the checker are complete. A verified domain is a necessary input, not a substitute for the rest of the evidence bundle.

## Coverage remains incomplete
Current 100-row distribution: GB 65, NL 18, US-PA 4, US-NJ 7, US-MI 2, CH 2, DE 2. There are no rows coded for AU, CA, SE, ES, IT, FR or BE. AU and FR online-casino acquisition remains excluded pending qualified legal review; CA and US must remain jurisdiction-specific.

## Actions in this batch
- Read back the current CSV from the target branch and parsed the quoted CSV structure, including multiline quoted fields.
- Confirmed 100 data rows and 46 columns.
- Confirmed exactly three rows with the canonical VERIFIED value and checked their evidence URL/date fields.
- No changes to scores, bonuses, legal status or publication status.
- No tests executed, no merge, no workflow run, and no deployment performed.
