# BeInCasinos premium review UX — implementation notes

Date: 25 October 2026  
Branch: `ops/2026-10-24-target-reconciliation-and-release-gates`  
Status: implemented in source; not deployed.

## Competitive research findings

The product patterns most worth learning from established review publishers are not their logos or exact layouts, but their decision-support mechanics:

- Casino.org foregrounds reviews, weighted criteria and a documented review process.
- Casinos.org foregrounds evidence, dated checks, payout behaviour, terms and a visible score explanation.
- Casino Guru separates an expert safety assessment from player feedback and exposes the factors behind the score.
- Casino.band's comparison concept shows the value of comparing independent rating sources side by side instead of treating one score as universal truth.

Sources checked 25 October 2026:
- https://www.casino.org/reviews/
- https://www.casino.org/how-we-rate/
- https://casinos.org/reviews/
- https://casinos.org/review-process/
- https://casino.guru/casino-reviews
- https://casino.band/casino-reviews-compared

## Changes implemented in source

1. Replaced the homepage's abstract checklist illustration with a cinematic, responsive casino-photo hero and a floating evidence snapshot.
2. Changed the primary action to the brand directory and made the scoring methodology discoverable from the first screen.
3. Made the sample review interface explicitly illustrative, not a fabricated live casino score.
4. Replaced the six-category homepage preview with the same nine-category, 100-point rubric used by the production ledger.
5. Updated the public methodology page to define all nine weights and state that eligibility is a separate pass/fail gate.
6. Updated page title and social metadata for reviews, scores and comparisons.
7. Added a visible photo credit to the Pexels source page.

Hero image source: Pavel Danilyuk, Pexels, https://www.pexels.com/photo/a-roulette-table-inside-a-casino-7594128/ . The source page identifies the photo as free to use. The site currently hotlinks the image; production hardening should download/optimize and self-host a properly licensed copy when permitted, record the asset source/license, and test fallback behaviour.

## Single scoring source of truth

The nine weights total exactly 100:

| Criterion | Weight |
|---|---:|
| Licence and operator transparency | 20 |
| Payments and withdrawals | 18 |
| Safer-gambling controls | 15 |
| Product and games | 12 |
| Bonus terms | 10 |
| Complaints and support | 10 |
| Usability and accessibility | 8 |
| Privacy transparency | 4 |
| Evidence quality | 3 |
| **Total** | **100** |

Mandatory market eligibility is a separate gate. A failed or unresolved gate means no total score and no recommendation. Desk research cannot be described as real-money testing. Scores must remain withheld until the evidence, second review and editorial/legal approval are complete.

## Remaining launch gates

- Build a genuinely reusable profile template that renders real brand-specific evidence, not placeholder bonuses, ratings or unlicensed logos.
- Replace hotlinked hero imagery with an optimized, licensed local asset if licensing permits.
- Complete visual regression checks at mobile, tablet and desktop widths, keyboard navigation, contrast, reduced motion, and broken-image fallback.
- Reconcile public review and directory language with actual approval counts before indexing or deployment.
- Keep all 100 candidate profiles on hold until brand/domain, operator, market permission, terms, image rights, consumer testing status, affiliate disclosure, independent review and editorial approval are resolved.
- Do not merge or deploy until the user-approved launch gate is satisfied.
