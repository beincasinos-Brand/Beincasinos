# Batch 33 — Canonical 100 candidate reconciliation
**Internal tracker instructions — do not treat this as 100 completed reviews.**

## Objective
Reconcile all batch files into one unique brand inventory, then validate each candidate against the 12 intended markets: AU, CA, GB, US, CH, DE, NL, SE, ES, IT, FR and BE. The inventory should separate “draft written”, “identity verified”, “licence verified”, “offer verified”, “assets cleared”, “scored” and “publish-ready”.

## Canonical inventory fields
One record per unique casino operator/product family:
- Stable internal ID.
- Canonical brand display name.
- Official consumer domain(s) and market mapping.
- Legal operator entity per market.
- Regulator and licence record per market.
- Product type (casino, sportsbook, bingo, game supplier, hybrid).
- Primary source URLs and date checked.
- Bonus status: verified / none found / account-specific / conflict / unknown.
- Cashier and withdrawal evidence status.
- Game lobby and game-category evidence status.
- Responsible-gambling and support evidence status.
- Image rights record.
- Review copy file path(s), canonical path and duplicate/supplement links.
- Score rubric complete? Yes/No.
- Market legal/eligibility gate passed? Yes/No.
- Technical and editorial QA passed? Yes/No.
- Publish-ready? Yes/No, with blocker reason.

## Reconciliation rules
1. Merge all supplements into the canonical brand record; do not count a supplemental file as a new review.
2. Alias names, product formats, game titles and game providers are not casino operators unless there is a distinct consumer-facing operator and legal entity.
3. A brand may have multiple market-specific entities, but count it once toward a 100-brand target unless the agreed inventory definition explicitly counts separate licensed entities.
4. Do not force the list to 100 by adding brands with uncertain identity, duplicate names or no verified online casino product.
5. Maintain a replacement queue for candidates that fail identity or legal checks.
6. A verified affiliate-program listing does not establish consumer-facing licensing or country eligibility.
7. Do not infer licensing from a parent company, retail casino, sportsbook licence, third-party comparison page or search-result snippet.

## Status definitions
- **Draft written:** original editorial copy exists; facts may remain unverified.
- **Identity verified:** official domain and exact consumer product identified.
- **Legal verified:** relevant official register confirms the operator/domain/product scope for the target market.
- **Facts verified:** current official evidence supports terms, cashier, lobby, support and player controls.
- **Assets cleared:** rights basis is recorded for every production image.
- **Scored:** rubric completed with written rationale and evidence per category.
- **Publish-ready:** all identity, legal, facts, asset, editorial and technical gates passed for that market.
- **Blocked:** unresolved conflict, stale evidence or missing critical information; no public CTA or rating.

## Review integrity
No fabricated “verified” badges, star ratings, game counts, bonus values, payout speed, player reviews or “best casino” claims. A page can be useful and search-friendly without a made-up score: use clear review methodology, original analysis, market-specific scope, cited official sources, pros/cons and responsible-gambling resources.

## Next reconciliation pass
- Read every BATCH markdown file in the dated review folder.
- Extract brand headings and normalise spelling/case.
- Join supplements to existing canonical brands.
- Identify all duplicates, ambiguous entity types and candidates without current primary evidence.
- Keep an explicit count of unique brands and a separate count of publish-ready market pages.
- Do not claim completion until the inventory is actually reconciled and evidence has been checked.
