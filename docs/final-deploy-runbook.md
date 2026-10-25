# BeInCasinos deployment and launch runbook

**Current review: 25 October 2026.** This document distinguishes repository state from the live deployment. It is an operational checklist, not legal clearance.

## Current verified state

- Repository: `beincasinos-Brand/BeInCasinos`, branch `main`.
- Hosting target: Cloudflare Pages Free, project `beincasinos`, build command `python3 scripts/build_site.py`, output directory `dist`. The project was previously reported connected to `main`; this session cannot directly access the Cloudflare API or dashboard to start a deployment manually.
- Current main commit before this launch-readiness update: `bf7f8c14c4a6a6042cd5c135c23830a6696f0e56`.
- Repository contains 100 review cards and 100 individual review routes. Repository sitemap contains 146 total URL entries (review pages plus other public pages).
- Live checks using a browser fetch on 25 October: apex homepage responds and its canonical is `https://beincasinos.online/`; `www.beincasinos.online` redirects to the apex; privacy and terms pages return content; key CSS assets return content; a nonexistent route returns 404.
- **Deployment is stale:** the live production sitemap and `beincasinos.pages.dev` sitemap each report 139 URLs. The latest seven pages added in PR #193 (Ahti Games, GeckoPlay, BacanaPlay, SlotStars, SpinGenie, Slingo Casino, EU Casino Spain) return 404 on both live hosts. Do not claim the latest repository commit has deployed until these routes return page content and the sitemap reflects 146 entries.
- GitHub Actions run [40240124154](https://github.com/beincasinos-Brand/BeInCasinos/actions/runs/40240124154) failed within three seconds and exposed no job steps/logs through the available connection. The failure cause is unconfirmed; do not spend repeated Actions minutes rerunning it blindly. The workflow's build and browser tests must pass when Actions are available.
- `robots.txt` is set to `Disallow: /` until the launch gates below are cleared. The sitemap remains listed for later use. This blocks crawling; it does not remove the site from the public internet or guarantee de-indexing of previously known URLs.
- Google Search Console property/verification and sitemap submission were reported by the owner earlier, but live GSC status is not directly verified here.

## Required release build

- Build command: `python3 scripts/build_site.py`.
- Output: `dist/`, created from the explicit public-file allowlist. `cloudflare/_headers` is copied to `dist/_headers`.
- Never deploy internal docs, research ledgers, source scripts, secrets, environment files, or provider configuration.
- Cloudflare Pages normally deploys from the connected GitHub `main` branch. After a merge, verify deployment in the Cloudflare dashboard or wait for the host to finish, then test the exact new routes on both `https://beincasinos.pages.dev/` and `https://beincasinos.online/`. A GitHub merge alone is not proof of deployment.
- Required post-deploy checks: homepage, favicon/logo, CSS/JS assets, all 100 review routes, sitemap entry count and route consistency, canonical URLs, security headers, HTTPS, `www` redirect, and 404 status. The automated repository checks do not prove Google indexing or legal readiness.

## Launch gates — not cleared

- [ ] Rotate/revoke any Cloudflare API or R2 credentials previously exposed in chat or elsewhere; confirm they are absent from tracked files and public artifacts. Do not paste secrets into chat.
- [ ] Verify the publisher contact mailbox `beincasinos@gmail.com` is accessible and monitored.
- [ ] Obtain qualified legal review of publisher identity, BeInCasinos/BEIN name/trademark risk, Moroccan CNDP/Law 09-08 implications, affiliate disclosures and each target market/product.
- [ ] Apply the market gate in `docs/tier-1-market-compliance-gate-2026-10-21.md`. In particular, online-casino promotion to Australia and France is marked BLOCK; US is hold-by-state/product; Germany, Switzerland and other markets require exact operator/domain/product review.
- [ ] Review all 100 profiles for exact domain/entity/current game-specific licence, terms, regulatory history, market eligibility, and any affiliate or commercial links. A register-level domain association is not proof of every game permission.
- [ ] Confirm the privacy notice matches the actual hosting, logging, email, analytics and third-party setup; have counsel review it where required.
- [ ] Perform manual mobile, keyboard and accessibility review. Automated checks are not a WCAG conformance claim.
- [ ] Verify Cloudflare security response headers and check no secrets or internal files are published.
- [ ] Obtain explicit approval before enabling indexing. Only after all gates pass, change robots to allow crawling, check GSC property status, and submit `https://beincasinos.online/sitemap.xml`.

## DNS and domain safety

- The owner previously reported Cloudflare Pages custom domain `beincasinos.online` Active with SSL enabled. A fresh browser fetch confirmed the `www` URL resolves by redirect to the apex.
- Do not change nameservers, DNS records, DNSSEC, MX, TXT or other mail records by guesswork. Reconcile the current DNS target and email requirements in Cloudflare/Spaceship first.
- No paid service, brand outreach, or unsupported licence/bonus/rating claims are authorized by this runbook.
