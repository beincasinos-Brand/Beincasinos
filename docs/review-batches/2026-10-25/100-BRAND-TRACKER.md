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
