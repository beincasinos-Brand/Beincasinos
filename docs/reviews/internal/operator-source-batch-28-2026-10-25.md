# Batch 28 — Peachy Games and PlaySunny operator transition — 25 October 2026

Official consumer-facing sources:
- Peachy Games support/terms page: https://www.peachygames.com/information/support/
- Peachy Games support page: https://www.peachygames.com/support/
- PlaySunny support/terms page: https://release.playsunny.co.uk/page/information/support/
- UKGC Solaya domain record (account 100050): https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/100050
- UKGC Solaya licence summary: https://www.gamblingcommission.gov.uk/public-register/business/detail/100050

Findings:
- Peachy Games terms version 010426 say last updated 1 April 2026 and explicitly state that Solaya Group Limited became the operator on 1 April 2026; Dazzletag Entertainment Limited operated the site before that date. Terms identify Solaya Group Limited, Gibraltar company number 125734, and state UK-only access.
- PlaySunny terms version 290926 say last updated 29 September 2026 and likewise identify Solaya Group Limited as operator from 1 April 2026, with Dazzletag as the previous operator. The terms state UKGC account 100050 and licence reference 100050-R-341529-001.
- These direct terms explain why older UKGC search results can still show historical Dazzletag trading-name records alongside Solaya’s active domain records. They provide stronger consumer-facing evidence for the current operator than the register alone.
- PlaySunny terms state customer funds are held separately but are not protected in insolvency. This is a material consumer-risk disclosure and must be represented accurately if the brand is ever reviewed; do not imply funds are protected.
- Peachy Games support page describes GAMSTOP and cross-brand self-exclusion support. This is operator-published information and has not been independently function-tested.
- The official register warns that domain and trading-name data are supplied by licensees and may not be guaranteed accurate: https://www.gamblingcommission.gov.uk/public-register/businesses

Proposed corrections to slots 47 (Peachy Games) and 48 (Play Sunny), not yet applied to canonical CSV:
- legal_entity: Solaya Group Limited (Gibraltar company 125734; current operator expressly identified in brand terms from 1 April 2026; UKGC account 100050).
- official_register_url: https://www.gamblingcommission.gov.uk/public-register/business/detail/100050
- terms_url: Peachy Games https://www.peachygames.com/information/support/ ; PlaySunny https://release.playsunny.co.uk/page/information/support/
- complaints/ADR, payments/withdrawals, privacy/cookies and responsible-gambling fields should only be populated with exact stable policy URLs after direct link verification; do not infer paths from labels.
- Keep both HOLD / NOT SCORED pending cashier and withdrawal review, complaint/ADR mapping, current offer-specific terms, image rights, consumer testing, independent review and editorial/legal approval. No score or bonus clearance is assigned.

No CSV write was made in this batch. No merge or Cloudflare Pages deployment.
