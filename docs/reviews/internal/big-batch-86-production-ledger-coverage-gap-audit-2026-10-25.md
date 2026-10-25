# Big Batch 86 — Production ledger coverage-gap audit

Date: 2026-10-25  
Branch: `ops/2026-10-24-target-reconciliation-and-release-gates`

## Audit result

The production ledger was fetched from the working branch and parsed directly. It contains 100 rows across 46 fields. All 100 rows remain `HOLD`. The ledger has no populated numeric overall scores, and no review is cleared for publication.

| Market code currently in production ledger | Rows | Declared target-market implication |
|---|---:|---|
| GB | 65 | Over-concentrated relative to a balanced international directory |
| NL | 18 | Present, but current exact-domain evidence and review work still required |
| US-PA | 4 | State-specific only |
| US-NJ | 7 | State-specific only |
| US-MI | 2 | State-specific only |
| CH | 2 | Low coverage |
| DE | 2 | Low coverage |
| **Total** | **100** | |

The declared target set is AU, CA, GB, US, CH, DE, NL, SE, ES, IT, FR and BE. The production ledger currently has no rows for AU, CA, SE, ES, IT, FR or BE. US is represented only by PA, NJ and MI; that is not nationwide US coverage. Australia and France need legal gates rather than automatic candidate filling for online casino products.

The separate intake queue currently contains 47 rows: CA-ON 20, SE 10, BE 10, ES 4 and IT 3. All 47 are `HOLD` and `NOT SCORED`. They are not production-ledger rows and must not be counted as completed reviews.

## Ledger schema / readiness blockers

The ledger has dedicated evidence fields for licence, payments, safety, product, bonus, complaints, UX, privacy and evidence quality, as well as terms, withdrawals, complaints, responsible-gambling, image rights, reviewer identities, independent review, editorial approval, consumer tests and affiliate disclosures. These are the intended gates—not optional decoration.

Before any row can be released:
1. Confirm exact live domain and current legal entity against the competent regulator.
2. Capture current product-specific licence scope, terms, bonus terms and date checked.
3. Capture deposit/withdrawal methods, limits, fees and published processing conditions without claiming an unperformed live test.
4. Record safer-gambling, complaint/ADR, privacy/cookie and accessibility evidence.
5. Establish image rights; use original art if brand asset rights are not established.
6. Apply the documented scoring rubric to evidence; retain individual category scores and the evidence bundle.
7. Obtain independent second review and editorial/legal sign-off, then re-evaluate publication status.

## Next highest-value work order

1. Rebalance the candidate pipeline toward under-covered target markets with official exact-domain evidence, starting with current-registry work for BE, SE, ES and IT already represented in the intake queue.
2. Review the 20 Ontario candidates against the current iGaming Ontario directory and current live operator pages; the published directory page used in this batch's earlier research states its listing is accurate as of 2026-09-01.
3. Build current exact-domain queues for NL and DE and expand state-specific US coverage only where the relevant regulator explicitly permits online casino products.
4. Treat AU and FR as legal/editorial exclusion gates for online casino reviews, not as a reason to populate unlawful or unsupported pages.
5. Only then migrate candidates into the production ledger when the minimum evidence bundle is complete; never copy queue-only register leads into production as if fully reviewed.

## Integrity note

This is a coverage and readiness audit, not a review-writing batch. It does not claim that the 100 brands are verified, tested, scored or publication-ready. No production-ledger row was changed. No test suite or GitHub Actions workflow was run; no merge or deployment occurred.
