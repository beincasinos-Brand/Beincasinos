# Batch 30 — production route and crawl-policy release blocker — 25 October 2026

Evidence source: https://github.com/beincasinos-Brand/BeIncasinos/blob/ops/2026-10-24-target-reconciliation-and-release-gates/docs/audits/live-site-release-gate-2026-10-24.md

Current verified state from the dated live-site audit:
- Production https://beincasinos.online/robots.txt allowed crawling and declared https://beincasinos.online/sitemap.xml.
- The production sitemap returned 46 URLs at the time of the audit.
- Production https://beincasinos.online/brand-directory/ returned 404.
- The working branch has a separate brand-directory/index.html research queue marked index,follow, while source robots.txt says Disallow: / as a pre-launch crawl block.
- This is a source/production mismatch. The robots policy must not be changed by assumption; owner intent must be confirmed before the final launch deployment.
- The public /reviews/ page states that no casino profiles are scored or ranked yet. Keep this honest until approved review evidence exists.

Required next actions before any launch:
1. Identify the actual static-site source paths and ensure the intended /brand-directory/ route is generated in the Cloudflare Pages output.
2. Decide the intended crawl policy, then make robots.txt, page-level robots metadata, canonical URL and sitemap consistent.
3. Recheck live HTTP status for /brand-directory/, /robots.txt and /sitemap.xml after the one approved Cloudflare Pages deployment.
4. Keep the research queue clearly labelled as research-only; do not expose it as a scored/recommended casino directory.
5. Complete all review, legal, image-rights, accessibility and QA gates; do not deploy merely to test the route.

No source code or production configuration was changed in this report. No merge or Cloudflare Pages deployment is authorized.
