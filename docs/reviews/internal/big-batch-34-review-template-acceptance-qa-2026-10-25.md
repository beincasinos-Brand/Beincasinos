# Batch 34 — review-template integration and content acceptance QA

Date: 2026-10-25. Internal editorial/implementation specification.

## Objective
Create one reusable production standard so all future BeInCasinos reviews have the same high-quality structure without inventing missing information.

## Master template
Use `docs/reviews/internal/premium-review-production-template-2026-10-25.md` as the canonical section order, score rubric, visual/asset policy and release checklist.

## Implementation tasks
1. Map each template field to the existing 43-column production ledger or document a controlled schema change before editing the CSV.
2. Keep all unverified records private/internal; no draft content should render as a published score, bonus, rating or licence claim.
3. Add market-specific availability to every review. State-specific US evidence, Ontario evidence and European national authorisations are not interchangeable.
4. Implement explicit fallback states: “No current offer verified”, “Payment terms not independently tested”, and “Image rights not cleared” are internal workflow states; unsupported claims must be omitted from public pages.
5. Use a reusable card design with score only when approved, date checked, market badge text, operator/licence link, key caveat, and transparent affiliate disclosure.
6. Make mobile layout the primary acceptance target: no clipped cards, no hidden terms, keyboard-visible focus, meaningful alt text, readable contrast and no essential text baked into imagery.
7. Ensure page title, meta description, canonical, breadcrumbs and structured data reflect only verified facts and the correct market; never generate fake aggregate ratings or review counts.
8. Add a pre-publish review that blocks HOLD records, missing image rights, blank approval fields, unresolved identity, and missing affiliate disclosure.
9. Validate one completed page end-to-end before producing a batch of public pages; do not deploy repeatedly while evidence remains incomplete.

## Acceptance criteria
- Every published review follows the master template.
- Scores and bonuses are absent unless approved and evidenced.
- Images are licensed/owned/cleared or original editorial assets.
- The market gate is evaluated independently from the score.
- Reviewer, second reviewer and approval dates are recorded truthfully.
- The current 100-row ledger remains HOLD until the row-level gates pass.

## Current limitation
This batch adds the editorial master and QA implementation plan only. It does not claim that the website code has been changed to use the template, that consumer testing has happened, or that any review is cleared. No merge/deploy performed.
