# Final deployment runbook — BeInCasinos on Cloudflare Pages Free

**Status: controlled preview configured; custom-domain launch still pending.** This runbook records observed project setup, not legal clearance or authorization to publish/index the production domain. No paid service or brand outreach is authorized.

## Current technical defaults

- Repository: beincasinos-Brand/BeIncasinos, branch main.
- Preferred host: Cloudflare Pages Free. The Cloudflare Pages project `beincasinos` is connected to this repository and branch `main`; the preview URL is https://beincasinos.pages.dev/. Build command and output are configured below. The connected Vercel team (BeinCasinos / bein-casinos) remains on Hobby with no linked projects; Cloudflare remains the selected host.
- Canonical domain: https://beincasinos.online (apex); permanently redirect www.beincasinos.online to apex.
- Build command: `python3 scripts/build_site.py`.
- Output directory: `dist`, assembled from a public-file allowlist.
- `cloudflare/_headers` is copied by the build into `dist/_headers` and validated in CI; `vercel.json` is retained only as an alternative-host configuration and is not the Cloudflare Pages deployment configuration.
- Nameservers were submitted at Spaceship as `keenan.ns.cloudflare.com` and `serena.ns.cloudflare.com`. Propagation, DNSSEC/DS state, and live authoritative DNS still require verification. The custom domain `beincasinos.online` and `www.beincasinos.online` have not been confirmed attached to Pages; do not assume either host is live.
- `robots.txt` blocks all crawling. Do not remove that block before explicit launch approval.

## Gate A — before connecting hosting

- [ ] Trademark/name review for BeInCasinos / “BEIN”; domain ownership alone is not clearance.
- [ ] Legal review of publisher identity, target-market rules, advertising/affiliate disclosures, privacy and Moroccan CNDP / Law 09-08 implications.
- [ ] Complete the primary-source market screening in `docs/tier-1-market-compliance-gate-2026-10-21.md`; obtain qualified legal review and dated evidence for every market/product. This screening is not itself legal clearance.
- [ ] Verify the publisher contact mailbox is accessible and monitored; temporary address is beincasinos@gmail.com.
- [ ] Approve a final privacy notice based on the actual host, logging, analytics and third-party services.
- [ ] Review every public brand profile's exact domain/operator/licence, market scope, terms, withdrawals, complaints, safer-gambling controls and regulatory history.
- [ ] Keep commercial willingness-to-pay unconfirmed unless a brand directly confirms it; do not imply paid placements are open when they are not.
- [ ] Complete manual desktop/mobile, keyboard, screen-reader and real-host checks. Automated axe/Chromium tests are not a WCAG conformance claim.
- [ ] Confirm the hosting provider's current terms, free-tier limits, and any usage/billing controls before configuration.

## Gate B — Cloudflare Pages project and controlled preview (project created; validate remaining items)

- [x] Confirm the intended Cloudflare account and GitHub repository; Pages project `beincasinos` exists and is connected to `beincasinos-Brand/BeIncasinos`, branch `main`.
- [x] Configure the build command as `python3 scripts/build_site.py` and build output directory as `dist`.
- [x] Confirm preview URL https://beincasinos.pages.dev/ responds; the latest repository site-check workflow passed (run 39636460758, commit `2cac7e8c7d41fb5c2a4aa473fe62fb2879595620`). This is a CI result, not proof that the Cloudflare Pages deployment is current.
- [ ] Keep the preview non-public where possible and keep `robots.txt` blocked. Do not configure a production custom domain or enable public indexing during this gate.
- [x] **Deployment freshness discrepancy rechecked 2026-10-21:** after the follow-up repository commits, the live `https://beincasinos.pages.dev/sitemap.xml` returned 32 URLs and included `/guides/casino-affiliate-deal-models/` on a cache-busting fetch. The specific sitemap mismatch is resolved in the preview. Production domain, HTTPS and the remaining launch gates are still unverified; do not treat preview success as production-domain confirmation.
- [ ] Verify HTTPS, all CSS/JS assets, calculator and checklist under the real response headers, CSP, HSTS and other security headers, canonical URLs, 404 status and mobile layout.
- [ ] Confirm the deployed output does not expose `docs/`, research CSVs, source scripts, provider configuration or other internal files.
- [ ] Record preview URL and test evidence internally; do not submit it to Search Console.
- [ ] If GitHub integration cannot be used, do not substitute Vercel instructions silently; document the blocker and agree on an approved alternative deployment path.

## Gate C — custom domain and final public deployment (not complete)

- [ ] Confirm Gate A is cleared and the owner explicitly authorizes public deployment.
- [ ] Verify nameserver propagation and DNSSEC/DS records first. Nameservers were already submitted in Spaceship; if DNSSEC is enabled at the registrar, reconcile its DS record with Cloudflare before troubleshooting TLS.
- [ ] Add `beincasinos.online` as a custom domain in Cloudflare Pages. Inspect conflicting apex A records before applying Cloudflare's exact Pages instructions. Preserve any mail-related MX/SPF/DKIM/DMARC records; do not delete records blindly.
- [ ] Configure a host-aware permanent redirect from `www.beincasinos.online` to `https://beincasinos.online`, and verify it live.
- [ ] Re-run launch acceptance checks on the live host, including real HTTP response headers and every public route/tool.
- [ ] Only after explicit launch approval, remove the `Disallow: /` pre-launch block from `robots.txt` and verify intended indexability.
- [ ] Verify every sitemap URL uses `https://beincasinos.online` and resolves to the intended canonical page.
- [ ] Only after launch approval, verify the Google Search Console Domain property using the exact DNS TXT token provided by Google, then submit `https://beincasinos.online/sitemap.xml`.
- [ ] Monitor indexing, crawl errors, security headers, contact inbox and user feedback after launch.

## Not authorized by this runbook

Cloudflare Pages project creation and nameserver submission have occurred. The production custom domain, DNS propagation, DNSSEC state, www redirect, legal review, final privacy/terms notices, public launch, Search Console verification, indexing, and brand outreach remain unconfirmed or intentionally gated. The Vercel team remains unchanged.
