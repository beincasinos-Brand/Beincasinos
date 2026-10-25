# Big Batch 39 — jurisdiction-specific publication gate

Date: 2026-10-25  
Scope: repository-level release safety; no public casino copy, scores, or offers were approved.

## Change delivered

Updated `scripts/check_review_ledger.py` to treat market eligibility as a separate publication gate, not as an implication of a populated brand row. Added regression tests in `scripts/test_review_ledger.py`.

The gate now blocks a row marked approved/published/live when its market code is:
- `AU` or `FR`: online-casino acquisition remains excluded pending qualified legal review.
- `US`: an aggregate country code, because state-level authorisation is required.
- `CA`: an aggregate country code, because exact province and regulator authorisation are required.

For publishable `BE`, `SE`, `ES`, and `IT` rows, the gate also requires a populated official-register URL. This is a structural check only: it does not independently prove that the URL is current, official, or matches the precise domain/operator/product. Manual verification remains mandatory.

## Regression tests added

- Aggregate US publication is rejected.
- Australia publication is rejected pending legal review.
- Aggregate Canada publication is rejected so Ontario evidence cannot be generalized nationwide.

Existing structural checks remain in place, including full-or-empty rubric scoring, score-sum validation, evidence completeness, image-rights clearance, separate reviewers, consumer-test status, and affiliate-disclosure review.

## Safety and scope

- The current 100-row portfolio remains `HOLD / NOT SCORED`; this change does not make any brand verified or publishable.
- No licence, bonus, image right, consumer test, or review score was invented.
- No public website content was changed.
- No workflow was run, to avoid consuming Actions minutes.
- No PR merge or deployment was performed.

## Validation limitation

The code and test files were updated through GitHub's file API. A local test run was not available in this session; run `python3 -m unittest scripts.test_review_ledger` and `python3 scripts/check_review_ledger.py` before merge. Any findings should be fixed before the PR is approved.
