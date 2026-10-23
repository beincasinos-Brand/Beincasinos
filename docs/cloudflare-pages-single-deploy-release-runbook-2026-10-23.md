# Cloudflare Pages release-safety and single-deploy runbook
Last reviewed: 23 October 2026

## Current repository facts
- Repository: `beincasinos-Brand/BeIncasinos`.
- Production branch documented by the project as `main`.
- Public site uses static HTML/CSS/vanilla JavaScript; CI creates a public-only artifact through an allowlist.
- Last confirmed integrated CI pass documented in README: 21 October 2026, commit `9ca6bdb3f8842a444db2ed807eb5181edb855350`, covering local HTML/link checks, sitemap/public-only artifact checks, headers and Chromium smoke tests for 28 indexable routes. This is historical CI evidence, not a fresh test of today's source or current production.
- The research batches are on non-main branches with commit prefix `[CF-Pages-Skip]` to avoid unnecessary GitHub Actions and Cloudflare Pages builds where the integration recognizes that prefix.

## Cloudflare Pages behavior to preserve
Official docs:
- Git integration: https://developers.cloudflare.com/pages/configuration/git-integration/
- GitHub integration and supported skip-build prefixes: https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/
- Branch deployment controls: https://developers.cloudflare.com/pages/configuration/branch-build-controls/
- Build watch paths: https://developers.cloudflare.com/pages/configuration/build-watch-paths/

Cloudflare Pages Git integration can deploy pushes to configured production and preview branches. The documented `[CF-Pages-Skip]` commit prefix skips a Pages deployment. Preview builds can also be disabled or limited by branch rules. Do not assume GitHub Actions and Cloudflare Pages share identical skip behavior; inspect each system's workflow and check status independently.

## Single-deploy safety procedure
1. **Keep research changes off `main`.** Use a sequential research branch and `[CF-Pages-Skip]` for documentation-only research commits.
2. **Before proposing a merge**, inspect the complete diff against `main`; verify that internal research dossiers, private owner notes, source logs and credentials are excluded from the public artifact.
3. **Run the repository's integrated CI** on the proposed code change. Require the current run to pass; a historic green run is not sufficient.
4. **Pre-deploy verification:** inspect the generated public-only artifact; validate HTML and local links; check canonical host, robots, sitemap, redirects, headers, missing routes and mobile/browser smoke tests.
5. **Release gates:** owner confirmation of domain/hosting control, legal/privacy/editorial sign-off, approved public content, mail/contact functionality, and manual live QA. Do not treat source CI as evidence that these external gates passed.
6. **One production deployment only** after the 100-brand evidence target and release gates are complete, as required by the project owner. Do not manually trigger a production build during research.
7. **Post-deploy checks:** verify apex/WWW canonicalization, HTTP status and redirects for every sitemap URL, robots and sitemap fetches, response headers, representative mobile routes, and error logs. Then verify sitemap submission and actual indexing/performance in Search Console; never equate sitemap submission with indexing or impressions.

## Build-minute protection
- Do not push research-only commits to `main`.
- Use `[CF-Pages-Skip]` for commits intended to skip Pages builds; confirm the exact prefix is supported by the configured integration.
- If build volume remains a concern, inspect Cloudflare Pages > Settings > Builds > Branch control and Build watch paths before changing settings. Exclude research-only documentation paths only if the project’s production source/build truly does not depend on them.
- Changing deployment settings is an owner-controlled hosting action; this document does not change Cloudflare settings.
- Do not burn Actions minutes by repeatedly re-running a successful workflow without a code change or concrete failure hypothesis.

## Release status
- Research branch only; no merge to `main`, no Cloudflare dashboard change, no DNS change, and no production deploy performed by this runbook update.
- Brand/review counts do not change from this operational documentation.
- The latest documented publication-approved review count remains 0/100. Research candidates and held dossiers do not count as approved reviews.
