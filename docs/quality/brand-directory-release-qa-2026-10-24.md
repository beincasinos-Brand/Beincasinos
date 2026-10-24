# Brand directory release QA snapshot — reconciled 24 October 2026

**Branch:** `feature/directory-global-brand-count-disclosure-2026-10-23`  
**Scope:** Static source inspection of `brand-directory/index.html` and reconciliation against `docs/targets/brand-image-asset-register-2026-10-23.csv`. This is not a live-site test.

## Current source counts

- Brand cards: **100**.
- Unique displayed card titles: **100**. This does **not** prove 100 distinct legal operators or 100 eligible casino brands.
- Status: **98 HOLD / 2 EXCLUDE**.
- Expandable research snapshots/checklists: **100/100**.
- Remote image elements/candidates: **64**; CSS artwork/monogram fallbacks: **36**.
- Image elements with alt text, explicit dimensions, lazy loading, async decoding, referrer policy and an error fallback: **64/64**.
- Asset-register rows: **100**; sourced image candidates: **64**; not sourced: **36**.
- External-link anchors in cards: **323**. This is a source count only; destinations were not all fetched or checked.
- Evidence-grade filter and image-state filter are present; the clear-filters control resets the filter inputs.
- One H1 is present in the page source.
- Robots meta: **`noindex,follow`**.
- Directory URL: **excluded from the sitemap in the current working-branch release state**.
- Release state: draft PR #52; merge and Cloudflare production deployment are not confirmed.

## Important reconciliation

An earlier version of this audit incorrectly recorded `index,follow` and a sitemap entry for this page. Those values do not match the current `brand-directory/index.html` source, which explicitly sets `noindex,follow`. The directory is intentionally held out of the sitemap while brand identity, local casino permission, product scope, editorial review and image-rights checks remain incomplete. Use the current HTML and release tracker as the authoritative working-branch snapshot; do not reuse the earlier indexable/sitemap statements.

## Image and content interpretation

All 64 remote images remain **rights pending** in the asset register. Finding an asset on an official site does not establish permission to republish it; a favicon is also not automatically a suitable full-size logo. Keep the CSS/monogram fallback available until identity, direct rendering, accessibility text, trademark/copyright terms and a defensible reuse basis have been checked. No image should be labelled rights-cleared based only on this source audit.

The 100 cards are market-scoped research entries, not 100 verified distinct global brands, consumer recommendations, or completed reviews. The current internal review tracker records **62 evidence-draft packages and 0/100 publication-approved reviews**. Do not convert HOLD/EXCLUDE entries into recommendations, ratings, structured review claims, affiliate calls to action, or indexable pages.

## Required checks before a release decision

1. Run a browser review at desktop, tablet and mobile widths; test keyboard-only navigation, filters, clear-filters focus return, empty states and image fallback behaviour.
2. Fetch and verify every official-domain/regulator link; the 323-anchor count is not a link check.
3. Test all 64 image URLs for response, content type, dimensions, visual match and redirect/hotlink behaviour.
4. Resolve rights for each image or replace it with original CSS/typographic art; retain alt text appropriate to the actual asset.
5. Reconcile the visible cards against the deduplicated global-ID work queue and market-specific legal gates before claiming a target of 100 eligible brands.
6. Keep `noindex,follow` and sitemap exclusion until an explicit release decision and all required evidence gates pass.
7. Verify the deployed Cloudflare response, canonical URL, robots directive and sitemap only after an approved deployment. No live-host, Search Console, browser, Lighthouse or deployment result is asserted by this report.

## Limitations

This is static source QA only. It does not verify live rendering, image fetching, current regulator status, image reuse rights, consumer-product experience, search-engine indexation, or production deployment.

**Status: OPEN / HOLD.**
