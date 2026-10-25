# Batch 85 — 100-review launch acceptance test
**Purpose:** define what “complete” means before merging review content into production.

## Per-review acceptance checklist
- [ ] Unique canonical brand ID and no unresolved duplicate.
- [ ] Exact official domain, legal operator, product category, and market eligibility evidenced.
- [ ] Current official terms linked; offers are dated and qualified or clearly marked unverified.
- [ ] Payments, withdrawal claims, game counts, suppliers, and support claims have evidence.
- [ ] Score follows published rubric and excludes commercial weighting.
- [ ] Image rights are cleared or a neutral fallback is used.
- [ ] Responsible-gambling controls and relevant local support links are checked.
- [ ] Affiliate disclosure is visible where commercial links appear.
- [ ] Original, useful copy; no copied competitor text or templated keyword stuffing.
- [ ] Title, description, heading hierarchy, canonical, internal links, and mobile rendering pass QA.
- [ ] Structured data matches visible evidence; no fabricated aggregate ratings.
- [ ] Second-person review of legal and bonus claims completed.

## Portfolio-level acceptance
- 100 distinct brands, not 100 documents or locale variants.
- Coverage for the 12 requested target markets is accurately represented; no unsupported “available in all markets” labels.
- Categories are separated; candidates that are not online casinos are not miscounted.
- Blocked and pending candidates are explicitly recorded.
- Every review has evidence status and last-check field.
- No empty pages, placeholder bonuses, fake ratings, broken images, or unlabelled sponsored placements.

## Release sequence
1. Finish candidate inventory and deduplication.
2. Verify primary evidence brand-by-brand.
3. Complete review copy and asset rights.
4. Run technical and editorial QA.
5. Review PR diff and obtain human approval.
6. Only then merge/deploy and refresh sitemap/indexing checks.

## Current programme status
This checklist is a release gate, not a statement that 100 reviews are complete. Keep the PR draft and do not deploy while critical evidence or assets remain unresolved.
