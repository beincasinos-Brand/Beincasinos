# 100-review release audit — 25 October 2026

## Snapshot
- Review route files in PR #171: 102 HTML routes were found under `reviews/**/index.html`.
- Production ledger: 100 candidate rows.
- Ledger publication state: 100/100 marked `HOLD — not approved for publication`.
- Ledger numeric overall scores: 0/100.
- Ledger editorial approval dates: 0/100.
- Ledger linked draft routes: 18/100.
- The 100-row inventory therefore does **not** represent 100 completed, publish-ready reviews.
- A sampled set of review pages contains no inline `<img>` tags; image sources and reuse permissions remain a publication gate.
- 45 canonical URLs were normalized in this work batch where the existing canonical incorrectly ended in `/index.html`. Existing clean canonicals were left unchanged.

## Publication acceptance required for each review
1. Unique brand and exact market/product scope; remove duplicate brand/locale candidates.
2. Primary regulator evidence matched to the exact consumer domain and contracting entity.
3. Current terms, deposit/withdrawal methods, limits/fees, complaints and dispute escalation, privacy/cookies, accessibility, and safer-gambling evidence.
4. Current promotion captured from the official source with date, full conditions and eligibility. If not verifiable, explicitly state no verified offer rather than invent one.
5. Original review copy that distinguishes source-based facts from hands-on testing. Never claim testing that did not happen.
6. Rights-cleared brand/product image or a designed fallback that does not imply permission to reuse third-party artwork.
7. Consistent rubric calculation from completed evidence; withhold numeric score where categories are unassessed.
8. Affiliate disclosure, reviewer identity, independent editorial approval, technical/link/canonical QA, and market eligibility.
9. Only after all gates pass: add the approved route to the review hub and sitemap.

## Safety / release rule
Do not merge or deploy this candidate batch as “100 final reviews” until the acceptance requirements are met. No sitemap or indexation request should include drafts on HOLD.

## Work log
- Added/maintained the transparent 100-point scoring and publication QA standard.
- Normalized 45 review-page canonicals that explicitly pointed at `index.html`; verified representative corrected pages through GitHub.
- No production deployment or indexation request was triggered by these changes.
