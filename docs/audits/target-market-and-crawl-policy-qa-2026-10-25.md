# Target-market and crawl-policy QA — 25 October 2026

Branch: `ops/2026-10-24-target-reconciliation-and-release-gates`
Purpose: release-gate audit only; no publication approval.

## Findings verified from branch source
- `brand-directory/index.html` contains 100 cards and 100 `data-market` attributes.
- Distinct labels in those cards: `CH`, `DE`, `NL`, `GB`, `US-PA`, `US-NJ`, `US-MI`.
- The owner's current target markets are AU, CA, GB, US, CH, DE, NL, SE, ES, IT, FR and BE. AU, CA, SE, ES, IT, FR and BE are not explicit directory labels. US state-specific labels do not establish nationwide US eligibility.
- Directory metadata says `index,follow` and canonicalizes to `https://beincasinos.online/brand-directory/`; source `sitemap.xml` includes that URL.
- Source `robots.txt` says `Disallow: /` and comments that this is a pre-launch block. That intentionally blocks crawling despite the page metadata and sitemap. Do not remove the block until the owner-authorized release gate.
- A dated production audit separately recorded `/brand-directory/` as HTTP 404 and production robots behavior different from branch source. This historical observation must be re-tested after the one authorized deployment; it is not a live check from this report.

## Required remediation before launch
1. Reconcile every directory card against the 12 target-market scope; exclude unsupported markets and distinguish US state licences from national availability.
2. Do not infer eligibility from a brand name, a licence in another jurisdiction, or a generic regulator URL. Confirm the exact domain, contracting entity and relevant casino permission in the local regulator's current record and current customer terms.
3. Keep the pre-launch crawl block until owner-approved release. At release, align robots.txt, page robots metadata, canonical URLs, sitemap URLs and generated Cloudflare Pages output in one reviewed change.
4. Confirm `/brand-directory/` returns the intended page, and re-fetch robots.txt and sitemap.xml from production after deployment. Do not deploy merely to test.
5. Keep all unreviewed brands HOLD / NOT SCORED. Research cards, regulator evidence and bonus leads are not completed consumer reviews. Do not add scores, claim firsthand testing, or reuse images without rights evidence.

## Status
This is a QA finding, not a fix. No ledger row was changed, no review was approved, no merge was made and no Cloudflare Pages deployment was performed.
