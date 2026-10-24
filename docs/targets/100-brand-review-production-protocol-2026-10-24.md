# BeInCasinos — 100-brand review production protocol
Updated: 24 October 2026
Branch: ops/2026-10-24-target-reconciliation-and-release-gates

## Status truth
The new production ledger selects 100 unique candidate identities from the current scoped registry using a round-robin market spread. They are candidates for research, not 100 verified brands or completed reviews. Existing source notes support only the claims they explicitly document. The publication-approved review count remains 0/100.

## Required profile content
Each eventual internal review should include: market and date checked; brand/domain/contracting-entity match; exact regulator record and casino-product permission; current welcome offer and complete bonus terms; wagering base/multiplier, expiry, max bet, max cashout, eligible games, payment exclusions and forfeiture rules; deposit/withdrawal methods, limits, fees and published processing estimates; complaints/ADR; safer-gambling tools; privacy/cookies; accessibility and responsive UX; historic regulatory action; image source and rights; original verdict, source log, affiliate disclosure, reviewer and second-reviewer sign-off.

Do not claim a deposit, game session, support interaction or withdrawal test unless it was actually performed and documented. Do not treat operator marketing as independent evidence. A regulator entry is a licensing fact, not a quality review.

## Evidence-first score (100 points)
- Licence, identity and market scope: 20
- Payments and withdrawals: 18
- Safer gambling and player protection: 15
- Product and games: 12
- Bonus transparency and value: 10
- Complaints and support: 10
- Usability and accessibility: 8
- Privacy and security: 4
- Evidence quality and editorial clarity: 3

Score each component only when the underlying evidence is sufficient. Missing material evidence is NOT SCORED, not zero and not an invented midpoint. An inactive licence, uncertain casino-product permission, conflicting domain/contracting entity, market illegality or unresolved safety-critical issue blocks the total score and publication. The score is an editorial assessment, not a guarantee of safety or winnings.

## Images and bonus terms
Use an official brand image only when its source and reuse basis are recorded. Until rights are established, use a generic monogram or text treatment; do not copy competitor artwork or hotlink logos. Every bonus must be captured from the official market-specific operator page on a dated visit and reconciled against the full bonus terms. If the current offer cannot be verified, say so and leave the bonus fields blank.

## Publication gates
1. Market is in scope and online-casino service is lawful there.
2. Current official regulator record confirms the exact licensee and casino product.
3. Domain, consumer-facing brand and contracting entity match.
4. Current general terms, bonus, payments/withdrawals, complaints/ADR, safer-gambling, privacy/cookies and contact details are captured.
5. Enforcement history is checked against primary decisions and dates.
6. Image rights and provenance are recorded.
7. Lawful consumer/usability checks are documented, with no unsupported first-hand claims.
8. Original, market-specific review is written; commercial and affiliate disclosures are visible.
9. Independent second reviewer checks sources, scoring and material caveats.
10. Editorial/legal approval is recorded before any public page or indexability change.

## Files
- 100-row internal worklist: docs/targets/100-brand-review-production-ledger-2026-10-24.csv
- Source registry: docs/brand-research-template.csv
- Existing research notes: docs/reviews/internal/
- Content/SEO release plan: docs/100-brand-content-and-seo-release-plan.md

No score, current bonus, image, consumer-experience claim or publication approval is invented in the new ledger. Bonus and image evidence remains pending until captured.


## Automated ledger guardrail (24 October 2026)

`python3 scripts/check_review_ledger.py` verifies the 100-row ledger schema, unique brand/market identities, HTTPS evidence links, ISO-formatted bonus-check dates, component score bounds and score-sum consistency. It rejects partial rubric scoring and prevents a row from being marked approved/published without the required source fields and explicitly cleared image rights. Regression tests live in `scripts/test_review_ledger.py` and are wired into the static-site workflow.

A structural PASS is not evidence that a regulator page is current, that an offer is available, that a brand is safe, or that a review is approved. Run this gate alongside manual primary-source review and the full publication checklist; do not bypass HOLD statuses to satisfy a numeric target.


## Expanded evidence and sign-off ledger fields (24 October 2026)

The ledger now has 43 columns. In addition to the original identity, licensing, bonus and scoring fields, it tracks deposit methods, fees/limits, privacy/cookies, accessibility evidence, regulatory actions, ADR, named primary and secondary reviewers, independent-review and editorial-approval dates, consumer-test status, affiliate-disclosure review and an evidence-bundle path. Every candidate currently explicitly records consumer/usability testing as `NOT PERFORMED` and affiliate disclosure as `NOT REVIEWED`.

The automated gate requires all schema fields and blocks publication until the review record has the necessary evidence URLs, distinct named reviewers, dated approvals, completed consumer/usability testing, reviewed affiliate disclosure, a complete consistent rubric score, and explicitly cleared image rights. A populated field is only a tracking assertion; source freshness, accuracy and the underlying review still require manual verification.


## Pre-launch crawl gate and latest bonus evidence (24 October 2026)

Before explicit launch approval, the deployment artifact must ship with `robots.txt` using `Disallow: /`. The artifact validator enforces that state and rejects a site-wide allow rule. The canonical sitemap remains prepared for future launch readiness but is not permission to publish or index.

The 24 October source pass recorded official offer pages for Jackpots.ch (CH) and Unibet (SE), bringing the candidate ledger to 13 bonus/promotion URLs. These offers remain on HOLD pending exact offer-specific terms, complete consumer-review evidence, image rights, testing and independent sign-off.


## Review-ledger regression coverage

The test suite now has seven regression cases covering the explicit unscored state, partial rubric rejection, score-total consistency, duplicate brand/market identity, non-HTTPS source rejection, malformed bonus-check date rejection, and publication blocked by missing evidence or image-rights clearance. GitHub Actions execution remains unconfirmed due to runner allocation; do not claim these tests passed until the job actually runs.


## Market scope and legal holds

A source URL must match the exact country/state/province in the candidate row. LeoVegas now points to the German offer page, not the UK promotions page. Ladbrokes Belgium now points to its local Belgian casino/promotion pages, not UK account terms. Belgium-specific candidates Casino777.be and Ladbrokes Belgium remain on HOLD because Belgian restrictions on gambling bonuses/promotional inducements require a legal/compliance determination for the exact mechanic before publication. Do not copy offers across markets.


## Belgian promotional-inducement hold

Belgian market candidates Casino777.be, Napoleon Casino Belgium, Circus Casino Belgium and Ladbrokes Casino Belgium remain on HOLD pending local legal/compliance confirmation that each exact promotional mechanic is permitted and the live terms are complete. Do not assume a promotional page establishes legal availability. See `docs/reviews/internal/belgium-promotion-compliance-hold-2026-10-24.md`.

Latest ledger audit reports 54 dated official bonus/promotion URLs across 100 rows, with no numeric scores assigned. Actions validation remains unconfirmed because runner allocation fails before steps begin.


## Canonical ledger identity rule

The canonical 100-brand production ledger must match the public directory's 100 card identities and market codes exactly. A prior 100-candidate cross-market research set is preserved separately at `docs/targets/100-brand-review-cross-market-research-ledger-2026-10-24.csv`; its sources cannot be reused for a different brand or market without a verified identity match.

After reconciliation, the canonical ledger has 100 unique public brand/market rows, eight matched bonus/promotion source leads, zero assigned numerical scores, and explicit NOT SCORED / HOLD states. These eight sources are not approved offers. The other rows remain held until current market-specific terms are verified.


## Automated public-directory identity guard

The workflow runs `scripts/check_directory_ledger_alignment.py` after the ledger validator. It requires exactly 100 unique public brand/market pairs and exact set equality with the canonical ledger. Four unit tests cover parsing, exact-match acceptance, market mismatch rejection and the 100-identity CI requirement. GitHub Actions execution remains unconfirmed due runner allocation.


## Canonical source count correction

The public-directory-aligned ledger now contains nine source leads (not eight), including GetLucky (NL). GetLucky remains held because its public directory card lacks a verified official domain and the precise regulator/domain mapping is not complete. No numerical score or public bonus claim is approved.


## Additional canonical directory bonus sources

The canonical directory ledger now has 13 official source leads after checks for admiral.ch, Starcasino.nl, Winz.nl and 888.nl. All remain held pending exact offer-specific terms. Do not reuse offers across markets; for 888.nl, the Dutch promotion route was not readable, so no current amount is claimed.
