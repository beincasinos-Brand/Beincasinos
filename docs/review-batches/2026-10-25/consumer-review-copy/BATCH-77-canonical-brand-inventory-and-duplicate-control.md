# Batch 77 — Canonical brand inventory and duplicate control
**Purpose:** stop duplicate brands, domains, and near-identical review pages from inflating the 100-brand target.

## Canonical record
Each candidate needs a stable brand ID, consumer-facing name, verified legal operator and parent group where available, official domain and locale domains, product category, market eligibility, evidence and last-check date, content status, existing slug/canonical plan, and aliases or white-label relationships.

## Merge rules
- One brand with multiple language pages is one brand, not multiple unique brands.
- Parent companies and casino brands count separately only when they are distinct consumer products with independent evidence and a meaningful review scope.
- A sportsbook is not automatically a casino brand.
- A land-based casino, lottery platform, bingo brand, poker room, and online casino must retain correct categories.
- Similar names are not sufficient to merge or distinguish records; verify operator and domain.

## Reconciliation checklist
1. Normalise case, punctuation, Unicode, and legal suffixes.
2. Compare domains, operator names, product categories, and aliases.
3. Mark likely duplicates for human review.
4. Resolve collisions before counting toward 100.
5. Keep rejected or blocked candidates in the ledger with a reason; don't silently erase the history.

## Completion definition
The target is 100 distinct, category-appropriate, evidence-backed brand reviews—not 100 markdown files. Batch count is a workflow metric, not a published brand count.
