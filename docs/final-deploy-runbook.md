# Final deployment runbook — BeInCasinos on Cloudflare Pages Free

**Status updated 2026-10-21: owner-provided Cloudflare Pages screenshot shows `beincasinos.online` Active with SSL enabled; live fetches now confirm the apex homepage, robots.txt, sitemap.xml, and core routes respond. Indexing remains intentionally blocked pending legal/privacy approval and the remaining acceptance checks.** This runbook records observed project setup, not legal clearance or authorization to publish/index the production domain. The file `google05b7a00eb84d7acb.html` is included in the public build allowlist. The latest workflow run, [39663653723](https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39663653723), completed successfully after the production-route-check notes were committed. This validates repository tests, not production HTTP responses. The owner reports completing the Google Search Console step, but this runbook does not claim direct access to or verified status inside that property. No paid service or brand outreach is authorized.

## Current technical defaults

- Repository: beincasinos-Brand/BeIncasinos, branch main.
- Preferred host: Cloudflare Pages Free. The Cloudflare Pages project `beincasinos` is connected to this repository and branch `main`; the preview URL is https://beincasinos.pages.dev/. Build command and output are configured below. The connected Vercel team (BeinCasinos / bein-casinos) remains on Hobby with no linked projects; Cloudflare remains the selected host.
- Canonical domain: https://beincasinos.online (apex); permanently redirect www.beincasinos.online to apex.
- Build command: `python3 scripts/build_site.py`.
- Output directory: `dist`, assembled from a public-file allowlist.
- `cloudflare/_headers` is copied by the build into `dist/_headers` and validated in CI; `vercel.json` is retained only as an alternative-host configuration and is not the Cloudflare Pages deployment configuration.
- Nameservers were submitted at Spaceship as `keenan.ns.cloudflare.com` and `serena.ns.cloudflare.com`. An owner-provided screenshot of the Cloudflare Pages project's Custom Domains screen on 2026-10-21 showed `beincasinos.online` as **Active** with **SSL enabled**. A prior read-only DNS dashboard inspection found two proxied apex A records (`54.149.79.189`, `34.216.117.25`), no AAAA/CNAME/MX/TXT records, and DNSSEC disabled; public DNS-over-HTTPS had returned different Cloudflare edge A answers (`104.21.20.145`, `172.67.193.33`), so reconcile this discrepancy before editing DNS. A fresh production fetch on 2026-10-21 confirms `https://beincasinos.online/` returns the homepage and its canonical is `https://beincasinos.online/`; `/robots.txt` returns `Disallow: /`; `/sitemap.xml` returns 32 canonical URLs; and `/privacy/` and `/terms/` both explicitly remain pre-launch drafts. The attempted `https://www.beincasinos.online/` check failed with `invalid_url`, so this is inconclusive rather than proof that the redirect works or fails. The verification-file content and selected core routes were confirmed in earlier spot checks. GitHub Actions run [39664433783](https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/39664433783) completed successfully, including the repository's configured site checks; CI does not verify production HTTP behavior or Google indexing. Still unresolved: independent HTTP status/headers, exact verification-file URL behavior, `www` routing, all 32 individual sitemap destinations, mobile/accessibility review, credential rotation, and legal/privacy sign-off. Before changing DNS, verify the Pages custom-domain mapping and whether email is intended to use this domain; do not invent mail records or enable DNSSEC without reconciling registrar settings.
- `robots.txt` blocks all crawling. Do not remove that block before explicit launch approval.

## Gate A — before connecting hosting

- [ ] Security hygiene: revoke and rotate any Cloudflare API token or R2 credential previously pasted into chat or otherwise exposed; create least-privilege replacements only if needed, keep them out of Git and public build output, and confirm no credential is present in tracked files or deployment artifacts.
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
- [x] Confirm preview URL https://beincasinos.pages.dev/ responds; the latest repository site-check workflow passed (run `39648226113`, commit `60ded6aefe10a3e6ee2a6c60f789cd96a8fb2715`; [workflow run](https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39648226113)). All 12 workflow steps completed successfully, including HTML/local-link checks, paid-listing hard-gate tests, build-artifact privacy checks and Chromium smoke tests. This is a CI result, not proof that the Cloudflare Pages deployment is current.
- [x] Keep `robots.txt` blocked while production checks remain incomplete. The Pages project's Custom Domains screen has no custom domains listed; the apex custom domain still needs to be added through Pages after DNS is reconciled. Do not enable public indexing during this gate.
- [x] **Deployment freshness discrepancy rechecked 2026-10-21:** after the follow-up repository commits, the live `https://beincasinos.pages.dev/sitemap.xml` returned 32 URLs and included `/guides/casino-affiliate-deal-models/` on a cache-busting fetch. The specific sitemap mismatch is resolved in the preview. Production domain, HTTPS and the remaining launch gates are still unverified; do not treat preview success as production-domain confirmation.
- [x] Fetch production apex homepage, `robots.txt`, and `sitemap.xml` over HTTPS; they returned content. Spot-checks of `/about/`, `/how-we-review/`, `/reviews/`, `/guides/`, both educational tools, `/privacy/`, `/terms/`, `/contact/`, and `/affiliate-disclosure/` returned page content and expected canonical metadata.
- [ ] Verify HTTP status codes and response headers (CSP, HSTS and other security headers), all CSS/JS assets, every sitemap URL, calculator/checklist behavior, 404 status and mobile layout.
- [ ] Confirm the deployed output does not expose `docs/`, research CSVs, source scripts, provider configuration or other internal files.
- [ ] Record preview URL and test evidence internally; do not submit it to Search Console.
- [ ] If GitHub integration cannot be used, do not substitute Vercel instructions silently; document the blocker and agree on an approved alternative deployment path.

## Gate C — custom domain and final public deployment (domain shows Active/SSL enabled; acceptance checks remain)

- [ ] Confirm Gate A is cleared and the owner explicitly authorizes public deployment.
- [ ] Verify nameserver propagation and DNSSEC/DS records first. Nameservers were already submitted in Spaceship; if DNSSEC is enabled at the registrar, reconcile its DS record with Cloudflare before troubleshooting TLS.
- [x] Owner screenshot confirms Cloudflare Pages → Custom domains lists `beincasinos.online` as Active with SSL enabled. Still verify the real homepage, verification file, and all routes over HTTPS.
- [ ] Resolve the conflicting apex A records (`54.149.79.189`, `34.216.117.25`) only after Pages displays the required target and the owner confirms whether domain email is expected. Preserve any mail-related records; none were visible during the dashboard inspection, so do not invent mail records or delete records blindly.
- [ ] Verify `www.beincasinos.online` is configured and permanently redirects to the apex while preserving path and query. Current automated fetch could not resolve/check the `www` URL, so this remains unconfirmed.
- [ ] Configure a host-aware permanent redirect from `www.beincasinos.online` to `https://beincasinos.online`, and verify it live.
- [ ] Re-run launch acceptance checks on the live host, including real HTTP response headers and every public route/tool.
- [ ] Only after explicit launch approval, remove the `Disallow: /` pre-launch block from `robots.txt` and verify intended indexability.
- [ ] Verify every sitemap URL uses `https://beincasinos.online` and resolves to the intended canonical page. The sitemap itself returns 32 URLs; only a subset of routes has been spot-checked so far.
- [ ] Only after launch approval, verify the Google Search Console Domain property using the exact DNS TXT token provided by Google, then submit `https://beincasinos.online/sitemap.xml`.
- [ ] Monitor indexing, crawl errors, security headers, contact inbox and user feedback after launch.

## Not authorized by this runbook

Cloudflare Pages project creation and nameserver submission have occurred. An owner screenshot confirms the apex custom domain is Active with SSL enabled, but live HTTP responses, DNS consistency, the `www` redirect, legal review, final privacy/terms notices, public launch, Search Console status as directly observed, indexing, and brand outreach remain unconfirmed or intentionally gated. The Vercel team remains unchanged.
