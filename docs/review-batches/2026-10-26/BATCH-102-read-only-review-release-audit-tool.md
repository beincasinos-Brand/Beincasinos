# Batch 102 — Read-only review release audit

## What this adds
- A standard-library-only Python script at `scripts/review_release_audit.py`.
- Scans review HTML pages for technical/editorial warning signs: missing title/H1/canonical, canonical URLs ending in `index.html`, weak meta descriptions, absent image tags or alt text, thin visible text, missing detectable affiliate/safer-gambling language, first-hand testing claims, and potentially misleading absolute gambling claims.
- Produces a console summary, with optional JSON and CSV reports for triage.
- Makes no source changes and does not deploy, modify the sitemap, or request indexing.

## Run from the repository root
```sh
python3 scripts/review_release_audit.py
python3 scripts/review_release_audit.py --json /tmp/review-audit.json --csv /tmp/review-audit.csv
```

## How to interpret it
This is a **triage tool, not an approval engine**. Static checks can create false positives and false negatives. A phrase match cannot validate an affiliate disclosure; a missing phrase does not prove the disclosure is absent. Human review must still verify the exact operator, consumer domain, product category, target-market rules, current bonus terms, payment/withdrawal details, safer-gambling information, image rights, score calculation, and all cited evidence. Do not convert the presence of a numeric score into evidence that the score is justified.

## Release gate
Keep all candidate pages on HOLD until the review completion register is reconciled with actual routes and the live site. Publish only editorial-approved, market-eligible pages with verified evidence and cleared visuals. Do not deploy merely because the script exits successfully.
