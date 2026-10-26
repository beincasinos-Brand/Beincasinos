# BeInCasinos — 100-brand verification tracker

**As of:** 2026-10-25  
**Purpose:** prevent candidate counts from being mistaken for completed reviews. This is an internal tracker. It must be updated only when evidence is actually captured.

## Required status definitions
- **CANDIDATE:** brand name proposed; not yet verified.
- **RESEARCHING:** primary-source checks underway.
- **HOLD:** one or more critical facts missing or unresolved.
- **EXCLUDE:** local legal eligibility failed or specialist legal review says do not promote.
- **READY FOR EDITOR:** evidence, original draft, scorecard, image rights and SEO checks assembled.
- **APPROVED:** independent editor signed off; all claims sourced; publication QA complete.
- **PUBLISHED:** approved page exists in production and was checked on mobile.

Do not count a brand as “verified” because it is famous, has an affiliate programme, appears on a competitor site, or has a licence in another country. Do not count a market-specific dossier as a unique global brand. Count a review as complete only when its status is APPROVED or PUBLISHED.

## Current batch accounting
- Market-specific review-draft Markdown files currently visible in PR #169: 162 (this is a file count, includes workbench scaffolds and does not equal unique brands or completed reviews).
- Shared editorial, source-check and card specifications: separate files, not brands
- Approved public reviews delivered by this batch: 0
- Candidate names may repeat across markets; deduplicate by canonical brand and legal operator before calculating unique-brand progress.
- Do not claim “100 brands complete” until the tracker contains 100 distinct canonical brands and each has the evidence and approval fields below.

## Candidate queue (initial records)
All rows start as **CANDIDATE / NOT VERIFIED / NOT RATED** until primary evidence is captured.

| # | Candidate | Market | Status | Unique-brand check | Regulator evidence | Terms captured | Score | Image rights | Editor approval |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | Kokobet | AU | HOLD | Pending | Pending | Pending | NOT RATED | Pending | Pending |
| 2 | Binobet | CA-Ontario | HOLD | Pending | Pending | Pending | NOT RATED | Pending | Pending |
| 3 | MrPunter | GB | HOLD | Pending | Pending | Pending | NOT RATED | Pending | Pending |
| 4 | Casinia | DE | HOLD | Pending | Pending | Pending | NOT RATED | Pending | Pending |
| 5 | Legiano | NL | HOLD | Pending | Pending | Pending | NOT RATED | Pending | Pending |
| 6 | SGCasino | SE | HOLD | Pending | Pending | Pending | NOT RATED | Pending | Pending |
| 7 | BullCasino | ES | HOLD | Pending | Pending | Pending | NOT RATED | Pending | Pending |
| 8 | Millioner | IT | HOLD | Pending | Pending | Pending | NOT RATED | Pending | Pending |
| 9 | Betscore | FR | EXCLUDE / LEGAL REVIEW | Pending | Pending | Pending | NOT RATED | Pending | Pending |
| 10 | Casinia | BE | HOLD | Possible duplicate of #4 | Pending | Pending | NOT RATED | Pending | Pending |
| 11 | Binobet | CH | HOLD | Possible duplicate of #2 | Pending | Pending | NOT RATED | Pending | Pending |
| 12 | MrPunter | US-New Jersey | HOLD | Possible duplicate of #3 | Pending | Pending | NOT RATED | Pending | Pending |
| 13 | bet365 | AU | HOLD | Pending | Pending | Pending | NOT RATED | Pending | Pending |
| 14 | Betway | CA-Ontario | HOLD | Pending | Pending | Pending | NOT RATED | Pending | Pending |
| 15 | William Hill | GB | RESEARCHING | Same brand may have distinct operators by market | Partial source note only | Pending | NOT RATED | Pending | Pending |
| 16 | Tipico | DE | HOLD | Pending | Pending | Pending | NOT RATED | Pending | Pending |
| 17 | Unibet | NL | HOLD | Pending | Pending | Pending | NOT RATED | Pending | Pending |
| 18 | Svenska Spel | SE | RESEARCHING | Confirm product and legal entity scope | Partial official register note | Pending | NOT RATED | Pending | Pending |
| 19 | Codere | ES | HOLD | Pending | Pending | Pending | NOT RATED | Pending | Pending |
| 20 | Lottomatica | IT | HOLD | Pending | Pending | Pending | NOT RATED | Pending | Pending |
| 21 | Napoleon | BE | HOLD | Pending | Pending | Pending | NOT RATED | Pending | Pending |
| 22 | BetMGM | US-Michigan | HOLD | Market-specific product and operator check needed | Pending | Pending | NOT RATED | Pending | Pending |

## Additional candidates from batches 09–10

These ten are added as distinct candidate names for tracking only. Regulator-record discovery is not equivalent to full verification or review approval. Related aliases and future market variants must be deduplicated.

| # | Candidate | Market | Status | Unique-brand / regulator check | Terms captured | Score evidence | Score | Image rights | Editor approval |
|---:|---|---|---|---|---|---|---|---|---|

| 23 | VideoSlots | ES | HOLD | DGOJ operator/domain record located; recheck exact product scope at publication | Current terms pending | Pending | NOT RATED | Pending | Pending |
| 24 | Monopoly Casino | ES | HOLD | DGOJ operator/domain record located; current local terms pending | Current terms pending | Pending | NOT RATED | Pending | Pending |
| 25 | Platin Casino | ES | HOLD | DGOJ record lists domain under 8PE España PLC; recheck current product scope | Current terms pending | Pending | NOT RATED | Pending | Pending |
| 26 | Fuego Casino | ES | HOLD | DGOJ record lists domain under 8PE España PLC; recheck domain/product status | Current terms pending | Pending | NOT RATED | Pending | Pending |
| 27 | AdmiralBet | ES | HOLD | DGOJ operator search lists domain under Beatya Online SA; exact product scope pending | Current terms pending | Pending | NOT RATED | Pending | Pending |
| 28 | Luckia | ES | HOLD | DGOJ operator/domain record located; current customer terms pending | Current terms pending | Pending | NOT RATED | Pending | Pending |
| 29 | Casino Barcelona | ES | HOLD | DGOJ operator/domain record located; current customer terms pending | Current terms pending | Pending | NOT RATED | Pending | Pending |
| 30 | Jokerbet | ES | HOLD | DGOJ operator/domain record located; current customer terms pending | Current terms pending | Pending | NOT RATED | Pending | Pending |
| 31 | Versus | ES | HOLD | DGOJ operator/domain record located; current customer terms pending | Current terms pending | Pending | NOT RATED | Pending | Pending |
| 32 | 1xBet | ES | HOLD | DGOJ operator/domain record located; current product and customer terms pending | Current terms pending | Pending | NOT RATED | Pending | Pending |

## Fields required for each additional brand
- Canonical brand and exact market scope
- Deduplicated legal operator and official domain
- Official regulator register URL, exact entry, licence scope/status and date checked
- Operator legal terms and privacy policy
- Current bonus URL and archived binding terms, or explicitly “no offer verified”
- Official payments/withdrawal terms; test log only if actually tested
- Game catalogue evidence and date checked
- Support and complaints route; player-protection tools
- Original copy, pros/cons and FAQs with source notes
- 100-point rubric item scores, rationale, confidence and limitations
- Image source, rights permission, attribution and alt text
- Title, meta description, H1, canonical, structured-data QA and internal links
- Affiliate disclosure, safer-gambling notice and correction route
- Reviewer, second editor, approval date and production URL

## Reporting rule
Every progress update must distinguish (a) files created, (b) unique candidate brands, (c) evidence-verified brands, (d) approved reviews, and (e) published pages. These are different numbers. Never inflate one using another.

## Additional candidates from batch 11 (candidate-only; no verification implied)

| # | Candidate | Market | Status | Unique-brand / regulator check | Terms captured | Score evidence | Score | Image rights | Editor approval |
|---:|---|---|---|---|---|---|---|---|---|
| 33 | BacanaPlay | ES | HOLD | DGOJ finder is a starting point; exact current legal entity, domain and casino scope must be confirmed | Pending | Pending | NOT RATED | Pending | Pending |
| 34 | SlotStars | ES | HOLD | Exact current DGOJ entry and product scope pending | Pending | Pending | NOT RATED | Pending | Pending |
| 35 | PrimeCasino | ES | HOLD | Exact current DGOJ entry and product scope pending | Pending | Pending | NOT RATED | Pending | Pending |
| 36 | LuckyVegas | ES | HOLD | Exact current DGOJ entry and product scope pending | Pending | Pending | NOT RATED | Pending | Pending |
| 37 | PlayKasino | ES | HOLD | Exact current DGOJ entry and product scope pending | Pending | Pending | NOT RATED | Pending | Pending |
| 38 | Metal Casino | ES | HOLD | Exact current DGOJ entry and product scope pending | Pending | Pending | NOT RATED | Pending | Pending |
| 39 | Luna Casino | ES | HOLD | Exact current DGOJ entry and product scope pending | Pending | Pending | NOT RATED | Pending | Pending |
| 40 | SpinGenie | ES | HOLD | Exact current DGOJ entry and product scope pending | Pending | Pending | NOT RATED | Pending | Pending |
| 41 | PlayUZU | ES | HOLD | Exact current DGOJ entry and product scope pending | Pending | Pending | NOT RATED | Pending | Pending |
| 42 | Slingo | ES | HOLD | Confirm brand/domain and exact Spanish casino product scope; possible brand/product alias check required | Pending | Pending | NOT RATED | Pending | Pending |

## Additional Germany candidates from batch 13 (candidate-only)

The GGL whitelist is the official starting source, but the exact entry, product category, legal entity and territory must be rechecked at publication. In particular, a virtual-slots entry must not be presented as permission for all casino games nationwide.

| # | Candidate | Market | Status | Unique-brand / regulator check | Terms captured | Score evidence | Score | Image rights | Editor approval |
|---:|---|---|---|---|---|---|---|---|---|
| 43 | BacanaPlay | DE | HOLD | GGL whitelist candidate domain; capture exact current entry/category | Pending | Pending | NOT RATED | Pending | Pending |
| 44 | LuckyVegas | DE | HOLD | GGL whitelist candidate domain; capture exact current entry/category | Pending | Pending | NOT RATED | Pending | Pending |
| 45 | SpinGenie | DE | HOLD | GGL whitelist candidate domain; capture exact current entry/category | Pending | Pending | NOT RATED | Pending | Pending |
| 46 | PlayOJO | DE | HOLD | GGL whitelist candidate domain; capture exact current entry/category | Pending | Pending | NOT RATED | Pending | Pending |
| 47 | DrückGlück | DE | HOLD | GGL lists separate product categories; exact domain, operator and scope need capture | Pending | Pending | NOT RATED | Pending | Pending |
| 48 | 888casino | DE | HOLD | Verify exact domain/product category; don't infer table-game permission | Pending | Pending | NOT RATED | Pending | Pending |
| 49 | 888slots | DE | HOLD | GGL whitelist candidate domain; capture exact current entry/category | Pending | Pending | NOT RATED | Pending | Pending |
| 50 | Mr Green | DE | HOLD | GGL whitelist candidate domain; capture exact current entry/category | Pending | Pending | NOT RATED | Pending | Pending |
| 51 | Slotmagie | DE | HOLD | GGL whitelist candidate domain; capture exact current entry/category | Pending | Pending | NOT RATED | Pending | Pending |
| 52 | Wunderino | DE | HOLD | Confirm the entry separately by product category; don't infer casino permission from sports-betting listing | Pending | Pending | NOT RATED | Pending | Pending |

## Additional candidates from batches 14–15 (candidate-only; duplicates expected)

| # | Candidate | Market | Status | Unique-brand / regulator check | Terms captured | Score evidence | Score | Image rights | Editor approval |
|---:|---|---|---|---|---|---|---|---|---|
| 53 | Paf | SE | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 54 | Betsson | SE | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 55 | Unibet | SE | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 56 | Svenska Spel | SE | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 57 | LeoVegas | SE | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 58 | ComeOn | SE | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 59 | Maria Casino | SE | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 60 | Mr Green | SE | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 61 | NordicBet | SE | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 62 | Betway | SE | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 63 | Jackpotjoy | SE | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 64 | Bingo.com | SE | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 65 | Holland Casino | NL | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 66 | TOTO Casino | NL | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 67 | Unibet | NL | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 68 | bet365 | NL | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 69 | Jack's Casino | NL | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 70 | BetCity | NL | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 71 | OneCasino | NL | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 72 | Kansino | NL | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 73 | Circus | NL | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 74 | BetNation | NL | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 75 | 711 | NL | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |
| 76 | VBet | NL | HOLD | Exact current local register entry and domain match pending; deduplicate canonical brand/operator | Pending | Pending | NOT RATED | Pending | Pending |

## Additional candidates from batches 16–17 (candidate-only; duplicates and legal exclusions possible)

| # | Candidate | Market | Status | Unique-brand / regulator check | Terms captured | Score evidence | Score | Image rights | Editor approval |
|---:|---|---|---|---|---|---|---|---|---|
| 77 | Napoleon | BE | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 78 | Betway | BE | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 79 | Casino777 | BE | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 80 | StarCasino | BE | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 81 | bwin | BE | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 82 | Unibet | BE | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 83 | Ladbrokes | BE | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 84 | Golden Palace | BE | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 85 | Circus | BE | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 86 | 777.be | BE | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 87 | BetFirst | BE | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 88 | VBet | BE | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 89 | Betclic | FR | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 90 | Winamax | FR | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 91 | Unibet | FR | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 92 | PokerStars | FR | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 93 | ParionsSport | FR | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 94 | PMU | FR | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 95 | NetBet | FR | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 96 | bwin | FR | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 97 | ZEbet | FR | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 98 | VBet | FR | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 99 | FDJ | FR | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |
| 100 | Betsson | FR | HOLD | Exact current official record and permitted product scope pending; France online-casino category must be excluded if unauthorised | Pending | Pending | NOT RATED | Pending | Pending |


## Latest accounting checkpoint — 2026-10-25, batch 23

PR #169 was re-counted after batches 18–23:
- Total changed files in PR: **396**.
- Markdown files under `review-drafts/`: **300**.
- These are file counts, not unique verified brands.
- **Approved/publish-ready reviews: 0 confirmed.**
- **Production pages added by these workbench batches: 0.**
- **Deployments performed by these workbench batches: 0.**

The recent batches contain structured research scaffolds and legal/product eligibility gates. They do not contain captured, complete evidence for every current offer, cashier, game catalogue, support route and image right. Many market-specific entries repeat the same global brand. Australia and Switzerland require especially strict product/domain eligibility checks; France online-casino claims must not be inferred from sports-betting authorisations; Ontario entries need exact current iGaming Ontario row/domain confirmation.

### Honest path to the 100-review milestone
1. Deduplicate candidate names into canonical global brand identities and distinct market/operator records.
2. Exclude candidates that fail the exact target-market product/legal gate.
3. Capture regulator entry, first-party terms, bonus, cashier, games, player protection, support/privacy and complaints with dated source links.
4. Clear image rights; no competitor-image scraping or unsupported brand claims.
5. Score only when minimum evidence is present; keep unresolved records NOT RATED.
6. Have an independent editor approve each complete review and run mobile/SEO QA.
7. Publish only approved consumer pages; keep internal research workbenches out of production and the public sitemap.
8. Run production build and preview checks before the first deploy; verify canonical URLs, robots, sitemap, redirects and noindex behavior.

**Release decision at this checkpoint: NOT READY for production deploy.** Do not treat file count or candidate count as completion.


## Canonical-name deduplication checkpoint — 2026-10-25

A normalized-name pass over the 100 numbered candidate rows produced **79 exact-name groups**, meaning 21 rows are repeats by case/punctuation-insensitive name normalization. This is an automated first pass, not final alias resolution; it can still miss related aliases and product variants. The detailed table is in `CANONICAL-BRAND-DEDUPLICATION-REGISTRY.md`.

- Candidate rows: 100
- Exact-name groups after normalization: 79
- Unique verified brands: 0 confirmed
- Approved reviews: 0 confirmed
- Published reviews: 0 confirmed

This corrects any possible impression that 100 candidate rows equal 100 distinct, verified brands. Do not fill the remaining count with unverified aliases just to reach a headline number.
