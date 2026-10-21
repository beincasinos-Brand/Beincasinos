# Final deployment runbook — BeInCasinos on Vercel

**Status: prepared, not executed.** This runbook does not authorize a purchase, project creation that triggers a deployment, DNS change, public deployment, indexing, or external outreach.

## Current technical defaults

- Repository: beincasinos-Brand/Beincasinos, branch main.
- Vercel team: BeinCasinos / bein-casinos, currently Hobby, with no linked projects as of 21 October 2026.
- Canonical domain: https://beincasinos.online (apex); permanently redirect www.beincasinos.online to apex.
- Build command: python3 scripts/build_site.py.
- Output directory: dist, assembled from a public-file allowlist.
- vercel.json defines clean URLs, trailing slashes, security headers/CSP and the www-to-apex redirect.
- **Commercial-plan blocker:** do not deploy the planned paid-listing/affiliate business on Hobby. Review Vercel's current commercial-use terms and Pro pricing; no upgrade has been purchased.
- robots.txt blocks all crawling. Do not remove that block before explicit launch approval.

## Gate A — before connecting production hosting

- [ ] Trademark/name review for BeInCasinos / “BEIN”; domain ownership alone is not clearance.
- [ ] Legal review of publisher identity, target-market rules, advertising/affiliate disclosures, privacy and Moroccan CNDP / Law 09-08 implications.
- [ ] Verify the publisher contact mailbox is accessible and monitored; temporary address is beincasinos@gmail.com.
- [ ] Approve a final privacy notice based on the actual host, logging, analytics and third-party services.
- [ ] Review every public brand profile's exact domain/operator/licence, market scope, terms, withdrawals, complaints, safer-gambling controls and regulatory history.
- [ ] Keep commercial willingness-to-pay unconfirmed unless a brand directly confirms it; do not imply paid placements are open when they are not.
- [ ] Complete manual desktop/mobile, keyboard, screen-reader and real-host checks. Automated axe/Chromium tests are not a WCAG conformance claim.
- [ ] Review current Vercel plan cost, usage limits and commercial acceptable-use terms; approve the plan separately before billing changes.

## Gate B — Vercel project and private preview

- [ ] When ready for infrastructure setup, link beincasinos-Brand/Beincasinos to the intended BeinCasinos team in Vercel. Project creation can trigger an initial preview build, so do this only when ready for that controlled preview step.
- [ ] Keep production deployment disabled/held until the final launch gate is cleared.
- [ ] Use vercel.json: build command python3 scripts/build_site.py, output directory dist. No runtime framework or package dependencies are required.
- [ ] Deploy a preview first when authorized, keeping robots.txt blocked.
- [ ] Verify HTTPS, apex/www redirects, all CSS/JS assets, calculator and checklist under the real response headers, CSP, security headers, canonical URLs, 404 status and mobile layout.
- [ ] Confirm the deployed output does not expose docs/, research CSVs, source scripts, provider configuration or other internal files.
- [ ] Record preview URL and test evidence internally; do not submit it to Search Console.

## Gate C — final public deployment

- [ ] Confirm Gate A is cleared and the owner explicitly authorizes public deployment.
- [ ] Configure the domain in Vercel and copy the exact DNS instructions shown by Vercel. Apply only those records in Spaceship; verify existing records first and preserve mail records.
- [ ] Verify HTTPS and permanent redirect from www.beincasinos.online to beincasinos.online.
- [ ] Re-run launch acceptance checks on the live host, including real HTTP response headers and every public route/tool.
- [ ] Only after explicit launch approval, remove the Disallow: / pre-launch block from robots.txt and verify intended indexability.
- [ ] Verify every sitemap URL uses https://beincasinos.online and resolves to the intended canonical page.
- [ ] Only after launch approval, verify the Google Search Console Domain property using the exact DNS TXT token provided by Google, then submit https://beincasinos.online/sitemap.xml.
- [ ] Monitor indexing, crawl errors, security headers, contact inbox and user feedback after launch.

## Not authorized by this runbook

No Vercel project was created, no plan was purchased, no DNS changed, no deployment or public indexing performed, and no brand outreach sent. These are gated infrastructure/release actions, not missing code tasks.
