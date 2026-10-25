# Batch 100 — Master 100-review completion register
**Purpose:** provide a single acceptance ledger for the BeInCasinos first 100-brand milestone.

## Record structure
One row per distinct consumer brand:
1. Canonical brand ID and display name
2. Official domain and legal operator
3. Product category
4. Intended market(s) from AU, CA, GB, US, CH, DE, NL, SE, ES, IT, FR, BE
5. Market-specific regulator evidence URL and check date
6. Current terms URL and bonus status
7. Payments/withdrawal evidence
8. Responsible-gambling evidence
9. Image source and rights status
10. Draft path and proposed canonical slug
11. Rubric score/status
12. Affiliate relationship and disclosure status
13. Editorial reviewer and approval date
14. Final state: candidate, blocked, pending, evidence-complete, editorial-approved, publish-ready

## Counting rules
- Count unique consumer brands, not batches or markdown files.
- Do not count a parent company and a product as separate brands without a meaningful distinction.
- Do not count locale variants as new brands.
- Do not count a sportsbook, lottery, land-based venue, or supplier as an online casino unless the actual reviewed product qualifies.
- Exclude blocked and unresolved candidates from the publish-ready total.

## Portfolio acceptance
The first 100 milestone is met only when 100 distinct candidates have complete evidence, original finished review copy, rights-cleared visuals or valid fallbacks, current offer status, appropriate market eligibility, consistent scoring, and editorial approval. This document does not assert that milestone is already met.

## Release discipline
Keep this inventory in the review PR until reconciled against existing files and the live site. Merge/deploy only after human review. Do not submit a sitemap of draft or unpublished content.
