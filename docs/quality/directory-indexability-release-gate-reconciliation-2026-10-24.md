# Directory indexability release-gate reconciliation — 2026-10-24

## Change

The branch previously declared `index,follow` for `brand-directory/index.html` and included `https://beincasinos.online/brand-directory/` in `sitemap.xml`. That conflicted with the existing PR description and tracker notes that the directory must remain noindex while its entries, legal scope, evidence and image rights are unresolved.

This pass restored the directory page directive to:

```html
<meta name="robots" content="noindex,follow">
```

and removed the directory URL from the branch sitemap. The site-level `robots.txt` continues to allow crawling and points to the main sitemap; this change is specifically about not presenting this unapproved research directory as an index-ready landing page.

## Why

Current static QA records 100 displayed research cards, not 100 qualified casino operators or approved reviews. The directory has 98 HOLD and 2 EXCLUDE statuses, and image-rights records remain incomplete. The review target remains 0/100 approved consumer reviews. Publishing an index directive and sitemap entry before the qualification and editorial gates pass could overstate readiness.

## Release conditions

Keep the directory noindex and out of the sitemap until:
- each counted brand is deduplicated and matched to a current, market-specific casino product and contracting entity;
- current official licensing and consumer-policy sources are checked;
- each consumer-facing review has evidence for terms, payments/withdrawals, complaints/ADR, safer gambling, privacy/cookies, accessibility and support as relevant;
- imagery has documented rights or is replaced with properly cleared assets;
- a second reviewer and editorial/legal sign-off approve the page; and
- the branch is merged through the approved release path and Cloudflare production behaviour is verified.

No merge, GitHub Actions run, Cloudflare deployment, live indexing check, or Google indexing result is claimed by this source edit.
