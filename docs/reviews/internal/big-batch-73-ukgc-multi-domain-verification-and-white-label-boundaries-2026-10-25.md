# Big Batch 73 — UKGC multi-domain verification and white-label boundaries
Date: 2026-10-25
Scope: verify exact candidate domains against the UK Gambling Commission public domain register; distinguish Active from White Label entries.

## Ledger changes — exact domains listed Active
The following four rows now have dated official evidence in `domain_verification_status` and `domain_evidence_url`:
1. Slot 35 — Betty Casino: `playbetty.co.uk`, Active under Betty Gaming (Malta) Limited, account 100695. Source: https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/100695
2. Slot 37 — FruitKings: `fruitkings.com`, Active under Solaya Group Limited, account 100050. Source: https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/100050
3. Slot 47 — Peachy Games: `peachygames.com`, Active under Solaya Group Limited, account 100050. Source: https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/100050
4. Slot 48 — Play Sunny: `playsunny.co.uk`, Active under Solaya Group Limited, account 100050. Source: https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/100050

These entries establish only the narrow domain-to-licensee register match. They do not establish a complete consumer review, bonus availability, product-specific terms, payment reliability, image rights, or publication readiness. All four remain HOLD / NOT SCORED.

## White-label and ambiguous cases deliberately not promoted
- Kong Casino (`kongcasino.com`) appears as White Label under Jumpman Gaming Limited, account 39175, rather than Active: https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/39175. Keep UNVERIFIED pending current operator/terms reconciliation.
- 247Bet (`www.247bet.com`) and Casiku (`www.casiku.com`) appear as White Label under White Hat Gaming Limited, account 52894: https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/52894. Do not describe White Hat as the consumer-facing contract operator without the site's terms.
- BetCrown, BetLegend, BetNero, 7Bet, BetFusion, Neptune Play, and PlayWins appear as White Label under Anakatech Interactive Limited, account 48789: https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/48789. They remain UNVERIFIED until the consumer-facing operator and current terms are established.
- Midnite remains unresolved because the register search returns two licensees (Dribble Media Limited and Midnite Limited) with matching trading-name/domain leads: https://www.gamblingcommission.gov.uk/public-register/businesses/results?business-search=Midnite. Do not collapse the records into a guessed single operator.
- The UKGC states that domain/trading names are provided by gambling businesses and may not be guaranteed by the Commission: https://www.gamblingcommission.gov.uk/public-register/businesses.

## Current ledger scope
The 100-candidate ledger remains a research queue, not 100 publishable reviews. A verified domain flag does not clear scores, bonus details, image rights, consumer tests, disclosures, second review or editorial/legal approval.

## Work completed
- Cross-checked current official register search results for exact domain and licensee labels.
- Updated four rows only where the exact domain was listed Active.
- Left White Label and ambiguous operator mappings unchanged.
- No tests run, no merge, no workflow run, and no deployment performed.
