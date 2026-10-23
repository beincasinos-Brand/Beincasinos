# Repository SEO snapshot audit — internal only

**Checked:** 23 October 2026  
**Branch:** ops/brand-research-progress-2026-10-22  
**Scope:** repository files only; not a live production or Search Console audit.

## Observed repository snapshot

- `sitemap.xml` contains **44 URL entries** at this branch snapshot.
- The listed sitemap URLs use the canonical `https://beincasinos.online/` host.
- No sitemap URL contains `internal`, `docs/reviews`, `evidence` or `draft` in its URL path (0 matching entries).
- `robots.txt` allows all crawlers and declares `Sitemap: https://beincasinos.online/sitemap.xml`. It has no explicit disallow rule for internal research paths.
- The internal review/evidence files created in this branch are repository Markdown documents under `docs/reviews/internal/`; they do not appear as entries in the checked sitemap.

## What this does not prove

This is a source-control snapshot only. It does **not** prove that the live sitemap matches this branch, that the branch has been merged/deployed, that internal Markdown files cannot be served through another route, or that Google has indexed any listed URL. A separate production fetch and Search Console check is required for those claims.

## Release recommendations

1. Keep internal evidence documents outside public page-generation globs, navigation, feeds, structured data and sitemap generation.
2. Since `robots.txt` allows all crawlers, do not rely on robots.txt to protect private/internal content. Keep research files outside the deployable public root and verify the build output before release.
3. Before changing sitemap URLs or lastmod values, confirm the corresponding public page is deployed and returns the expected canonical URL and status.
4. Check production URLs for HTTP status, canonical, robots meta, title/description and internal links; use Search Console for indexation confirmation.
5. Avoid triggering GitHub Actions while the repository's included minutes are near exhaustion.

## Result

Repository sitemap entries inspected: 44. Internal/draft-like sitemap path matches: 0. Live deployment/indexation: **not verified by this audit**.
