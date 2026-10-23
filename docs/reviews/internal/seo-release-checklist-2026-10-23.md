# SEO and release validation checklist — 2026-10-23

Internal operations checklist. A checklist item is not marked complete without fresh evidence.

## Search visibility and crawl
- [ ] Fetch production robots.txt and verify syntax, crawl policy and sitemap directive from raw response.
- [ ] Fetch production sitemap.xml; record timestamp, URL count, parse errors and canonical hosts.
- [ ] Crawl every sitemap URL for raw HTTP status, redirect chain, title, meta description, canonical, robots meta/header, and rendered main content.
- [ ] Verify every canonical is absolute HTTPS and matches the intended canonical host/path.
- [ ] Check internal links for broken targets, redirect chains, orphan pages and inconsistent trailing-slash URLs.
- [ ] Confirm important pages are linked from relevant hubs and use descriptive, non-spammy anchor text.
- [ ] Validate structured data only where it accurately reflects visible page content; no invented ratings, review counts or rankings.
- [ ] Run accessibility checks for headings, keyboard navigation, contrast, form labels and mobile layout.
- [ ] Check duplicate/thin pages, query-parameter duplicates, pagination and noindex/canonical interactions.
- [ ] Keep internal evidence packs, candidate registers, editorial notes and unpublished drafts excluded from the public build and sitemap.

## Helpful content and trust
- [ ] Publish transparent review methodology and explain what was and was not tested.
- [ ] Date each review and distinguish operator claims from independently observed facts.
- [ ] Add source links for regulator, terms, payment, privacy and safer-gambling claims.
- [ ] Make affiliate relationships and commercial disclosures clear near relevant links.
- [ ] Include market-specific legal scope; do not present prohibited or unlicensed products as available recommendations.
- [ ] Avoid fabricated keyword volumes, rankings, payout times, ratings, firsthand tests or guaranteed outcomes.
- [ ] Prioritise genuinely useful guides and calculators, with clear assumptions and limitations, over scaled low-value pages.

## Production release gate
- [ ] All intended source changes reviewed and merged through the agreed workflow.
- [ ] Build output is reproducible and contains no internal documents or secrets.
- [ ] Automated tests and browser smoke tests pass on the exact release commit.
- [ ] Preview URL and intended artifact/commit provenance recorded.
- [ ] Production release explicitly approved only after content, privacy/legal and technical gates pass.
- [ ] After deployment, re-fetch key routes, sitemap and robots; compare against the approved release.
- [ ] Search Console inspection/submission is performed only with explicit authorized access; indexing is verified from Search Console rather than inferred from fetchability.

## Rate-limit and Actions budget
- Prefer local/static analysis and read-only checks that do not consume Actions minutes.
- Do not trigger redundant workflow runs for documentation-only changes.
- Never describe a preview as a production deployment or a crawlable URL as indexed.
- Current verified completion: this file is a checklist only; no production checks were executed by this commit.
