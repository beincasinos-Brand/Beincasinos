# Draft review noindex safety batch — 2026-10-25

## Changes made
Added `<meta name="robots" content="noindex, nofollow">` to 24 market-specific review HTML routes on the draft branch. These routes explicitly describe themselves as evidence profiles or have unresolved verification, scoring, image-rights, testing, or editorial approval gates. The directive is a temporary release-safety measure so draft pages are not presented as approved search landing pages if the branch is deployed for QA.

## Routes updated
- `reviews/7melons-ch/index.html`
- `reviews/888casino-gb/index.html`
- `reviews/admiral-bet-it/index.html`
- `reviews/admiral-ch/index.html`
- `reviews/admiralbet-es/index.html`
- `reviews/bet365-casino-gb/index.html`
- `reviews/bet99-ca-on/index.html`
- `reviews/betano-de/index.html`
- `reviews/betcity-nl/index.html`
- `reviews/betfair-casino-es/index.html`
- `reviews/betfair-it/index.html`
- `reviews/betflag-it/index.html`
- `reviews/betfred-casino-gb/index.html`
- `reviews/betinia-us-nj/index.html`
- `reviews/betmgm-casino-us-mi/index.html`
- `reviews/bally-bet-casino-us-nj/index.html`
- `reviews/betparx-casino-us-pa/index.html`
- `reviews/betrivers-casino-us-mi/index.html`
- `reviews/betsson-se/index.html`
- `reviews/bingoal-nl/index.html`
- `reviews/borgata-online-casino-us-nj/index.html`
- `reviews/bwin-be/index.html`
- `reviews/caesars-palace-online-casino-ca-on/index.html`
- `reviews/casineo-ch/index.html`

## Release rules
- Do not treat noindex as a substitute for evidence, local eligibility, image-rights clearance, review scoring, current bonus terms, hands-on testing disclosure, or independent editorial approval.
- Keep these routes out of the public review hub and sitemap while on HOLD.
- Remove the noindex directive only after the individual page has passed the publication gates and is approved for indexing.
- This batch does not add numeric scores, unverified bonus claims, product claims, or images.

## Status
Code change only on PR #171's draft branch. This report does not claim production deployment or a completed 100-review launch.
