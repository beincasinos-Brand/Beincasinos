# Big Batch 75 — Brillbet domain evidence and candidate triage
Date: 2026-10-25

## Ledger update: Brillbet (slot 34, GB)
- The existing evidence note records that the UK Gambling Commission's domain-name record lists `brillbet.co.uk` and `brillbet.com` as Active under UK Digital Bookmakers Ltd, account 101570, and the trading-name record lists `brillbet` as Active.
- Official domain register: https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/101570
- The ledger now records `domain_verification_status=VERIFIED`, date `2026-10-25`, and the exact official register URL.
- This is a narrow domain/licensee identity check. Brillbet remains HOLD / NOT SCORED; current consumer terms, cashier/withdrawals, complaints/ADR, safer gambling, privacy/cookies, accessibility, offer terms, image rights, consumer testing, affiliate disclosure, second review and editorial/legal approval remain outstanding.

## Triage cases left unchanged
- **BetTOM (slot 11):** the ledger itself says to verify `bettom.com` against the UKGC domain record and live footer. No exact-match evidence is recorded, so no VERIFIED status was assigned.
- **AK Bets (slot 15):** existing research note says the inspected UKGC account summary does not list a Remote Casino licence and the domain register has no recorded domain names. Betting permissions are not a substitute for casino permission. Keep excluded from casino recommendation pending regulator evidence.
- **Silkbet (slot 25):** no current exact domain/operator match in the evidence note; do not promote.
- **Midnite (slot 43):** two potentially relevant licensee records need reconciliation; do not collapse them into a guessed operator identity.
- **QuinnBet (slot 60):** official enforcement notice is recorded in the ledger, but exact current domain identity still needs a register match. Enforcement context must be disclosed accurately in a future review.
- **Kong Casino (slot 62):** domain record says White Label, not Active; contracting operator remains to be reconciled.
- **Bet442 (slot 97):** register search returns more than one licensee lead; exact operator/product scope remains unresolved.

## Current verified-domain count
The eight rows confirmed in Batch 74 plus Brillbet make **9** ledger rows with the exact `VERIFIED` state, subject to the narrow meaning above. No numeric scores are assigned and no review is publication-ready from this evidence alone.

## Execution status
No automated tests run, no merge, no workflow run, and no deployment performed.
