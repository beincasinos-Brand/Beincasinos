# Batch 13 — Sitemap URL audit plan and per-URL classification schema
Date: 2026-10-25
Scope: prepare a repeatable audit of the live sitemap without asserting a crawl result that has not been run.

## Audit input
Live sitemap URL previously observed: https://beincasinos.online/sitemap.xml
Previous technical audit counted 146 URL entries at that time. Re-fetch before using that count as current. A sitemap entry is only a discovery hint, not proof of indexing or quality.

## Per-URL output schema
Record one row per URL with:
- URL as listed in sitemap
- Fetch timestamp and HTTP status
- Redirect chain and final URL
- Canonical URL from HTML
- Robots meta / X-Robots-Tag
- robots.txt crawl permission
- Sitemap membership
- Page template and page intent
- Target market and product category, if applicable
- Title, meta description and H1
- Main-content word count and unique-content notes
- Internal inlinks and orphan status
- Structured data types and validation result
- Duplicate/near-duplicate cluster
- Decision: KEEP / FIX / NOINDEX / REMOVE / REDIRECT
- Reason, evidence URL, and next action

## Decision rules
- **KEEP:** 200 response, intended canonical, crawlable/indexable, distinct user intent, useful main content, correct market/product claims.
- **FIX:** page is useful but has repairable metadata, canonical, internal-link, structured-data, or content issues.
- **NOINDEX:** page may be useful to users but is low-value for search or a controlled utility/duplicate; do not use as a substitute for correcting canonical errors.
- **REMOVE:** obsolete, unsupported, misleading, thin, or redundant page with no appropriate replacement.
- **REDIRECT:** only when a close equivalent exists; do not redirect unrelated pages to the homepage.

## Priority ordering
P0: robots.txt, server availability, sitemap parse, TLS, accidental noindex.
P1: canonical consistency, redirects, 4xx/5xx, duplicate URL forms, sitemap-to-page mismatches.
P2: market and product claims, legal gate, missing/duplicate title and H1, empty templates.
P3: thin/near-duplicate copy, orphan URLs, broken internal links, structured-data correctness.
P4: refresh stale terms/bonus facts, improve source citations and image provenance, monitor indexing.

## Market checks
Use only target markets AU, CA, GB, US, CH, DE, NL, SE, ES, IT, FR, BE. For Canada and US, retain province/state boundaries. For France, Australia, and any other jurisdiction with product-specific restrictions, do not label a brand “legal” or “licensed” without exact product and domain evidence. The market field is not inferred from a brand's language, currency, or generic footer.

## Sample QA after a controlled release
Check at minimum:
- Homepage
- /reviews/ directory
- One individual review
- One guide
- Responsible-gambling page
- robots.txt
- sitemap.xml
- One unsupported/removed URL to confirm intended 404/410 or redirect behavior

For each, save timestamp, response status, final URL, canonical, robots directives and a screenshot or source excerpt. Then compare Search Console URL Inspection separately; do not infer indexing from HTTP 200 or sitemap membership.

## Automation caution
Do not add a new GitHub Actions workflow just for this checklist; repository usage previously approached the included Actions-minute allowance. Run a local/manual or existing Cloudflare diagnostic where practical. Any automated fetcher must respect robots directives, avoid stressing operator sites, and never use credentials or private endpoints.

## Current status
This file is a schema and workflow. It is not a completed fetch of all sitemap URLs, does not certify indexation, and does not change production.
