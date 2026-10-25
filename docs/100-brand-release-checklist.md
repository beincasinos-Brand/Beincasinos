# 100-brand release checklist

Use this checklist for the final batch only. Do not deploy just because a PR merges.

## Content inventory
- [ ] Exactly 100 distinct canonical consumer brands; duplicate aliases and suppliers removed.
- [ ] Every brand counted has a brand-market row and a primary-source evidence record.
- [ ] Every market variant is separate where legal status, terms or products differ.
- [ ] Exactly 100 full reviews have passed the evidence gate and independent second-editor review.
- [ ] Every review includes a defensible score breakdown or clearly remains unrated.
- [ ] Current offer is evidenced or explicitly shown as not verified.
- [ ] Payment/withdrawal claims, complaints and player-protection details have official sources.
- [ ] Every image has commercial-use rights recorded; unverified assets are excluded.
- [ ] Affiliate and paid-placement disclosures are visible and accurate.
- [ ] No invented hands-on tests, customer ratings, payment performance or licensing claims.

## Site and UX
- [ ] Comparison cards are consistent and readable on mobile.
- [ ] Navigation, filters and CTAs work by keyboard and touch.
- [ ] Colour contrast, focus indicators, heading hierarchy and alt text checked.
- [ ] No placeholder copy, empty score blocks, broken images or dead links.
- [ ] Canonicals, titles, descriptions and internal links are unique and accurate.
- [ ] Structured data matches visible content and contains no fabricated review/rating fields.
- [ ] Robots directives, sitemap entries and 404 behaviour checked.
- [ ] Affiliate disclosure, methodology, contact/corrections and responsible-gambling resources are linked.

## Technical release (Cloudflare Pages)
- [ ] Review the exact diff and build output before merge.
- [ ] Do not run redundant workflows; preserve the GitHub Actions allowance.
- [ ] Confirm intended branch and build command/output directory from the existing project config.
- [ ] Run local/static checks and available browser smoke tests before deployment.
- [ ] Do not change DNS, redirect rules, secrets or Cloudflare settings without a verified reason.
- [ ] After deployment, verify apex and www behaviour, HTTPS, canonical redirects and key pages from an external client.
- [ ] Check sitemap fetch and a sample of canonical review URLs.
- [ ] Treat Google Search Console indexing as a separate observation; a successful sitemap submission is not proof that URLs are indexed.

## Status reporting
Report separately: candidate count, verified brand-market count, approved review count, pages built, pages live, sitemap URLs, and URLs observed indexed. Do not collapse them into one percentage.
