# Final deployment runbook — BeInCasinos

**Status: prepared, not executed.** This runbook is intentionally the final infrastructure checklist. It does not authorize a purchase, DNS change, public deployment, indexing, or external outreach.

## Current technical defaults

- Repository: `beincasinos-Brand/Beincasinos`, branch `main`.
- Canonical domain: `https://beincasinos.online` (apex); redirect `www` permanently to apex.
- Preferred production target: Netlify on a commercial-capable plan, after the owner approves the current plan/usage budget and connects the account.
- Netlify Free is for preview/staging only. Do not use Vercel Hobby for the planned commercial site.
- Build/publish configuration is in `netlify.toml`; it runs `python3 scripts/build_site.py` and publishes only `dist/`.
- `robots.txt` currently blocks crawling. Do not remove the block until the launch gate is intentionally cleared.

## Gate A — must be cleared before public launch

- [ ] Trademark/name review for BeInCasinos / “BEIN”; domain ownership alone is not clearance.
- [ ] Legal review of publisher identity, target-market rules, advertising/affiliate disclosures, privacy and Moroccan CNDP / Law 09-08 implications.
- [ ] Verify the publisher contact mailbox is accessible and monitored; the temporary address is `beincasinos@gmail.com`.
- [ ] Approve a final privacy notice based on the actual host, logging, analytics and any third-party services.
- [ ] Approve every public brand profile only after exact domain/operator/licence, market scope, terms, withdrawals, complaints, safer-gambling controls and regulatory history are reviewed.
- [ ] Keep commercial willingness-to-pay unconfirmed unless a brand directly confirms it. Do not imply paid placements are open when they are not.
- [ ] Complete manual desktop/mobile, keyboard, screen-reader and real-host checks. Automated axe/Chromium tests are not a WCAG conformance claim.

## Gate B — private preview / staging

- [ ] Owner approves the hosting plan and connects the intended hosting account to the repository.
- [ ] Use the repository's `netlify.toml` as-is; do not enable automatic production publishing before the owner intends to deploy.
- [ ] Deploy a private/preview build first if supported, keeping `robots.txt` blocked.
- [ ] Verify HTTPS, apex/www redirects, all CSS/JS assets, calculator and checklist under the real response headers, CSP, security headers, canonical URLs, 404 behaviour and mobile layout.
- [ ] Confirm the deployed site does not expose `docs/`, scripts, trackers, prospect CSVs or other internal files.
- [ ] Record the preview URL and test evidence internally; do not submit it to Search Console.

## Gate C — final public deployment

- [ ] Confirm Gate A is cleared and the owner explicitly authorizes public deployment.
- [ ] Configure DNS in Spaceship only using the exact records provided by the chosen host. Verify ownership before changing existing records; do not invent record values.
- [ ] Configure HTTPS and permanent redirect from `www.beincasinos.online` to `beincasinos.online`.
- [ ] Re-run the launch acceptance checklist on the live host, including real HTTP response headers and all public routes/tools.
- [ ] Only after explicit launch approval, remove the `Disallow: /` pre-launch block from `robots.txt` and verify intended indexability.
- [ ] Rebuild the sitemap and verify every canonical URL uses `https://beincasinos.online`.
- [ ] Only after launch approval, verify the Google Search Console Domain property using the exact DNS TXT token provided by Google, then submit `https://beincasinos.online/sitemap.xml`.
- [ ] Monitor indexing, crawl errors, security headers, contact inbox and any user feedback after launch.

## Not authorized by this runbook

No hosting purchase, account connection, DNS change, deployment, public indexing, Search Console submission, brand outreach or public paid-listing offer has been executed. These remain gated actions, not missing code tasks.
