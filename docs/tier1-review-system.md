# Tier 1 review system

Focus: AU, US, FR, DE, CH, GB, NL. Reviews for any other market stay in the repo but are `noindex`, out of `sitemap.xml` and hidden in `/reviews/` (decided by `market` in `data/affiliate-links.json`; change it to bring one back, then run `apply`).

## Files
- `data/tier1-reviews.json`: one record per Tier 1 review: entity, licence line, offer, six criteria (rating 0-5 or `null`, paraphrased note, source URL), regulatory history.
- `scripts/build_tier1.py apply|check`: renders the same snapshot card (logo frame, evidence meter, offer, last checked, score) and an evidence table on every Tier 1 review. CI runs `check`.

## Score rule (from docs/editorial-review-scoring-rubric.md)
A number appears only when all six criteria are rated AND `evidence_complete` AND `second_review` are true. Missing evidence is `null` ("Not assessed"), never a low score. Weights: terms 25, payments 20, safer gambling 20, complaints 15, licence 10, usability 10.

## Logos
Put the operator's official logo (from its affiliate media kit) at `assets/brands/<review-slug>.svg` (or .png/.webp). The card uses it automatically in a fixed 160x64 frame; until then it shows a monogram. Do not hotlink.

## Status 27 Oct 2026
Researched: bet365 (5/6), Betfair (6/6, domain gap to resolve), William Hill (4/6, offer unverified), 888casino (0/6; operator pages unreachable from the research sandbox). The other 25 Tier 1 reviews show 0/6 until researched.
