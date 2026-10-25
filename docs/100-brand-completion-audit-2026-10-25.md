# BeInCasinos 100-brand completion audit — 25 October 2026

## Release truth (do not inflate counts)

This is a work-tracking audit, not a claim that the target is complete.

- Target: 100 distinct, verified casino consumer brands with 100 complete, market-specific review pages.
- Latest prior source-tree inventory: 95 non-template `docs/brand-profile-*.md` dossiers, with later additions recorded in the inventory. These files include duplicates, unresolved identities, and supplier/operator context; file count is not unique verified brands.
- Approved reviews: the latest verification sprint says **0/100 approved**. Editorial branch drafts may exist, but they are not counted as approved unless the evidence gate and independent sign-off are met.
- Live publication, deploy success, sitemap inclusion, and Google indexing are separate states. Never claim one based on another.
- Do not merge or deploy this batch automatically. Keep work on a feature branch to avoid unplanned Cloudflare deploys and Actions consumption.

## Market scope (owner's latest list)

AU, CA, GB, US, CH, DE, NL, SE, ES, IT, FR, BE.

Do not add Ghana or other out-of-scope markets. The US must be state-specific: a general US brand claim is insufficient where online casino legality and licence permissions vary by state. Switzerland, Germany, Belgium, France, Italy, the Netherlands, Sweden, Spain, Canada and Australia require market-specific legality and operator/brand permission checks; do not treat an international domain as proof of local availability.

## Brand-level acceptance gates

A brand-market pair may move from HOLD to review-ready only when all applicable items are evidenced with direct, dated sources:

1. Canonical consumer-facing brand name and official domain.
2. Contracting/operator legal entity matched to the exact domain and product.
3. Current regulator register entry and permitted product scope for the target market; state regulator for US entries.
4. Market availability and exclusions; no extrapolation from another country's licence.
5. Current terms, bonus terms (or explicitly state no offer could be verified), wagering requirements, max bet, expiry and excluded games where relevant.
6. Deposits, withdrawals, payment-method availability, fees/limits and stated processing times. Do not claim real-world payout speed without a reliable basis.
7. Complaint/ADR route, safer-gambling tools, age requirement and self-exclusion details.
8. Game catalogue and game types verified from current official pages; distinguish casino, live dealer, slots, table games, poker, bingo and sportsbook rather than assuming every product exists.
9. Bonus/affiliate disclosure, commercial relationship status and paid-placement labelling policy.
10. Logo/screenshots/images have a source and reuse permission or a clear licence; do not copy competitor artwork or imply endorsement.
11. Evidence freshness date, source URLs, unresolved questions, editor, and independent second-editor approval.
12. Scoring rubric applied consistently; show component scores and explain evidence gaps. Never fabricate a numeric score, user rating, test result, bonus amount or availability claim.

## Review page minimum content

- Original summary and clear market label.
- Operator/licence explanation with official register source.
- Games and platform experience, separating verified facts from editorial judgement.
- Bonus terms in a structured, dated table; “not verified” is preferable to invented specifics.
- Payments and withdrawals with official terms and limitations.
- Mobile/accessibility, support, complaint route, player protection and responsible-gambling tools.
- Transparent strengths, drawbacks, best-fit audience and who should avoid it.
- Reproducible score breakdown; no unsubstantiated star ratings.
- Official links, review/update date, affiliate disclosure, author/editor and corrections route.
- Relevant original visual assets with rights status. If unavailable, use a designed text-led card rather than an unlicensed logo or stock image.
- Internal links to market guide, comparison page, methodology and responsible-gambling policy.

## Status vocabulary

- `CANDIDATE`: name only; not verified.
- `RESEARCHING`: sources being collected.
- `HOLD`: unresolved identity, legal, product, terms, payment or consumer-protection question.
- `REVIEW-READY`: source gate complete, waiting for editorial review.
- `APPROVED`: all gates passed and second editor signed off.
- `PUBLISHED`: approved page is in the site build and checked after deployment.
- `INDEX-OBSERVED`: independently observed in Search Console or an equivalent first-party index report.

Only `APPROVED` counts toward the 100 approved-review target. Only `PUBLISHED` counts toward live pages.

## Batch workflow

1. Reconcile the 100 candidate CSV with all dossier files and review-page directories; deduplicate brand aliases, market variants and operator/supplier entities.
2. Build one canonical row per brand-market pair. Keep each target market separate when terms or licence status differ.
3. Process the strongest evidence first: regulator register, official terms, bonus terms, payment pages, complaints/ADR and safer-gambling pages.
4. Mark blocked items HOLD with the exact missing proof; do not fill blanks with guesses.
5. Draft reviews only from collected evidence; do not reuse one generic review with only the country name changed.
6. Run content, link, structured-data, accessibility, sitemap and build checks without triggering deployment.
7. Have an independent editor review scores, claims, affiliate disclosures and image rights.
8. Release only after the owner-approved batch has passed all gates; verify canonical URL, redirects, robots, sitemap and live rendering after deployment.

## Immediate next work

- Reconcile every current dossier and existing review draft against the status vocabulary.
- Prioritise completion of existing evidence-rich market dossiers before adding more candidate names.
- Explicitly separate evidence-ready drafts from public approved reviews in the tracker.
- Keep Cloudflare deployment as a final step, as requested by the owner.
