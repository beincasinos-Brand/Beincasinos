# Target-market and crawl-policy QA — 25 October 2026

Branch: `ops/2026-10-24-target-reconciliation-and-release-gates`
Purpose: release-gate audit only; no publication approval.

## Findings verified from branch source
- `brand-directory/index.html` contains 100 cards and 100 `data-market` attributes (source SHA at inspection: `3c576c6b9a9d607e9459426cd5291532cf571ba0`).
- Market distribution: GB 65; NL 18; US-NJ 7; US-PA 4; CH 2; DE 2; US-MI 2. This is heavily GB-weighted, not a balanced 100-brand set across the owner's requested markets.
- The owner's current target markets are AU, CA, GB, US, CH, DE, NL, SE, ES, IT, FR and BE. AU, CA, SE, ES, IT, FR and BE have no explicit directory labels. US state-specific labels do not establish nationwide US eligibility.
- Directory metadata says `index,follow` and canonicalizes to `https://beincasinos.online/brand-directory/`; source `sitemap.xml` includes that URL.
- Source `robots.txt` says `Disallow: /` and comments that this is a pre-launch block. That intentionally blocks crawling despite the page metadata and sitemap. Do not remove the block until the owner-authorized release gate.
- A dated production audit separately recorded `/brand-directory/` as HTTP 404 and production robots behavior different from branch source. This historical observation must be re-tested after the one authorized deployment; it is not a live check from this report.

## Required remediation before launch
1. Reconcile every directory card against the 12 target-market scope; exclude unsupported markets and distinguish US state licences from nationwide US eligibility.
2. Rebalance the 100-card research set against the approved market plan; do not fill gaps with brands lacking local eligibility evidence.
3. Do not infer eligibility from a brand name, a licence in another jurisdiction, or a generic regulator URL. Confirm the exact domain, contracting entity and relevant casino permission in the local regulator's current record and current customer terms.
4. Keep the pre-launch crawl block until owner-approved release. At release, align robots.txt, page robots metadata, canonical URLs, sitemap URLs and generated Cloudflare Pages output in one reviewed change.
5. Confirm `/brand-directory/` returns the intended page, and re-fetch robots.txt and sitemap.xml from production after deployment. Do not deploy merely to test.
6. Keep all unreviewed brands HOLD / NOT SCORED. Research cards, regulator evidence and bonus leads are not completed consumer reviews. Do not add scores, claim firsthand testing, or reuse images without rights evidence.

## Status
This is a QA finding, not a fix. No ledger row was changed, no review was approved, no merge was made and no Cloudflare Pages deployment was performed.
