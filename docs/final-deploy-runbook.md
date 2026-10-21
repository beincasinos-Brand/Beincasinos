# Final deployment runbook — BeInCasinos on Cloudflare Pages Free

**Status: prepared, not executed.** This runbook does not authorize a purchase, project creation that triggers a deployment, DNS change, public deployment, indexing, or external outreach.

## Current technical defaults

- Repository: beincasinos-Brand/Beincasinos, branch main.
- Preferred host: Cloudflare Pages Free, pending owner setup and preview acceptance. The connected Vercel team (BeinCasinos / bein-casinos) remains on Hobby with no linked projects; do not use Hobby for the planned commercial site.
- Canonical domain: https://beincasinos.online (apex); permanently redirect www.beincasinos.online to apex.
- Build command: python3 scripts/build_site.py.
- Output directory: dist, assembled from a public-file allowlist.
- `cloudflare/_headers` is copied by the build into `dist/_headers` and validated in CI; `vercel.json` remains as an alternative-host configuration.
- Cloudflare still requires a host-aware permanent `www`-to-apex Redirect Rule and live verification. No Cloudflare project exists yet.
- robots.txt blocks all crawling. Do not remove that block before explicit launch approval.

## Gate A — before connecting production hosting

- [ ] Trademark/name review for BeInCasinos / “BEIN”; domain ownership alone is not clearance.
- [ ] Legal review of publisher identity, target-market rules, advertising/affiliate disclosures, privacy and Moroccan CNDP / Law 09-08 implications.
- [ ] Complete the primary-source market screening in `docs/tier-1-market-compliance-gate-2026-10-21.md`; obtain qualified legal review and dated evidence for every market/product. This screening is not itself legal clearance.
- [ ] Verify the publisher contact mailbox is accessible and monitored; temporary address is beincasinos@gmail.com.
- [ ] Approve a final privacy notice based on the actual host, logging, analytics and third-party services.
- [ ] Review every public brand profile's exact domain/operator/licence, market scope, terms, withdrawals, complaints, safer-gambling controls and regulatory history.
- [ ] Keep commercial willingness-to-pay unconfirmed unless a brand directly confirms it; do not imply paid placements are open when they are not.
- [ ] Complete manual desktop/mobile, keyboard, screen-reader and real-host checks. Automated axe/Chromium tests are not a WCAG conformance claim.
- [ ] Confirm the hosting provider's current terms, free-tier limits, and any usage/billing controls before configuration.

## Gate B — Cloudflare Pages project and preview

- [ ] When ready for infrastructure setup, link beincasinos-Brand/Beincasinos to the intended BeinCasinos team in Vercel. Project creation can trigger an initial preview build, so do this only when ready for that controlled preview step.
- [ ] Keep production deployment disabled/held until the final launch gate is cleared.
- [ ] Use vercel.json: build command python3 scripts/build_site.py, output directory dist. No runtime framework or package dependencies are required.
- [ ] Deploy a preview first when authorized, keeping robots.txt blocked.
- [ ] Verify HTTPS, the host-aware apex/www redirect, all CSS/JS assets, calculator and checklist under the real response headers, CSP, HSTS and other security headers, canonical URLs, 404 status and mobile layout.
- [ ] Confirm the deployed output does not expose docs/, research CSVs, source scripts, provider configuration or other internal files.
- [ ] Record preview URL and test evidence internally; do not submit it to Search Console.

## Gate C — custom domain and final public deployment

- [ ] Confirm Gate A is cleared and the owner explicitly authorizes public deployment.
- [ ] Add `beincasinos.online` as a custom domain in Cloudflare Pages. If Cloudflare asks to onboard the DNS zone, first record the current Spaceship DNS records and preserve MX/SPF/DKIM/DMARC. Change nameservers only after reviewing the complete record set.
- [ ] Verify HTTPS and permanent redirect from www.beincasinos.online to beincasinos.online.
- [ ] Re-run launch acceptance checks on the live host, including real HTTP response headers and every public route/tool.
- [ ] Only after explicit launch approval, remove the Disallow: / pre-launch block from robots.txt and verify intended indexability.
- [ ] Verify every sitemap URL uses https://beincasinos.online and resolves to the intended canonical page.
- [ ] Only after launch approval, verify the Google Search Console Domain property using the exact DNS TXT token provided by Google, then submit https://beincasinos.online/sitemap.xml.
- [ ] Monitor indexing, crawl errors, security headers, contact inbox and user feedback after launch.

## Not authorized by this runbook

No Cloudflare project was created, no provider integration was enabled, no DNS changed, no deployment or public indexing performed, and no brand outreach sent. The Vercel team remains unchanged. These are gated infrastructure/release actions, not missing code tasks.
