# Directory release-gate hardening — 24 October 2026

**Branch:** `feature/directory-global-brand-count-disclosure-2026-10-23`  
**Change:** `scripts/check_brand_directory.py` strengthened in commit `703df230091f17c82227c3c7aa8878750e8e4b0e`.  
**State:** source-level verification completed against the branch files; full repository CI and live-browser checks were not run here.

## What changed

- Fixed a duplicate-title detection weakness: titles are now compared case-insensitively using `Counter`, so `Brand` and `brand` cannot pass as distinct names.
- Added per-card release checks for the search index, market, allowed HOLD/EXCLUDE status, evidence grade, research summary, official-domain field, legal-operator field, regulator field, evidence-grade field, verification checklist, research-context/evidence-limits section, and non-recommendation disclaimer.
- Added a two-way reconciliation between card names and the 100-row image register, catching both missing register rows and orphan rows.
- Added image safeguards for intrinsic dimensions, alt text, lazy loading, async decoding, no-referrer policy, and fallback handler; the HTML image count must equal the number of sourced image candidates in the register.
- Retained the SEO safety gate: `noindex,follow` and exclusion from the sitemap while entries remain unapproved.

## Source snapshot checked

| Check | Result |
|---|---:|
| Directory cards / unique case-insensitive titles | 100 / 100 |
| Required card fields missing | 0 |
| Image register rows / unique names | 100 / 100 |
| Card titles missing from register | 0 |
| HTML remote image elements / register candidates | 63 / 63 |
| Images missing checked accessibility/loading/fallback attributes | 0 |
| Card status | 98 HOLD / 2 EXCLUDE |
| Evidence grades | 20 A / 53 B / 27 C |
| Robots directive | `noindex,follow` |
| Directory URL in sitemap | No |

The source checks passed against the fetched HTML/CSV/sitemap snapshot. This was a direct structural check of those files, **not** execution of the updated Python script in a checked-out repository, GitHub Actions CI, a browser test, or a Cloudflare production test.

## What this does not establish

- The 100 titles are not proven to be 100 distinct eligible legal operators.
- A/B/C are internal evidence grades, not consumer review scores or publication approval.
- The 63 images remain rights-pending; matching a source URL does not grant republication rights or prove the image loads in production.
- All 98 HOLD entries and 2 EXCLUDE entries remain outside publication approval. Approved consumer reviews remain **0/100**.
- No merge, production deployment, indexation, or traffic outcome is claimed.

## Next gate

Run the repository's actual CI workflow against this commit, inspect any failures, then do browser/responsive/accessibility and image-fetch checks on a controlled Cloudflare preview. Keep the directory noindex and out of the sitemap until legal, evidence, image-rights, second-editor and editorial approvals are recorded.
