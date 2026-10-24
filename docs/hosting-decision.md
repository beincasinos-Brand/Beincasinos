# Hosting decision — Cloudflare Pages Free preferred

**Current preferred provider:** Cloudflare Pages Free for the initial static site, subject to preview acceptance.
**Deployment status:** no Cloudflare account connected, no Pages project created, not deployed, and not public.
**Previous account finding:** the connected Vercel team is **BeinCasinos** (slug: bein-casinos), on the **Hobby** plan, with no linked projects. Verified by read-only account inspection on 21 October 2026.

## Plan and commercial-use gate

Vercel's official Fair Use Guidelines restrict Hobby to personal/non-commercial use and explicitly describe affiliate-link sites whose primary purpose is affiliate linking as commercial use: https://vercel.com/docs/limits/fair-use-guidelines

Therefore, **do not deploy the planned commercial BeInCasinos directory to the current Hobby team**. The expected path is Vercel Pro or another Vercel plan whose current terms explicitly permit the planned paid-listing and affiliate business. Before upgrading, review current price, usage/billing terms, limits, and relevant acceptable-use terms at https://vercel.com/pricing. No upgrade, purchase, or billing change has been made.

The owner subsequently preferred Cloudflare Pages Free to avoid the Vercel Pro monthly cost. Cloudflare remains unconnected until the owner creates and authorizes the account. Code, content, SEO and test preparation can continue meanwhile.

### Current plan-price reference — checked 21 October 2026

Vercel's official pricing page currently lists Pro at **US$20/month**, with **US$20 of included usage credit**; taxes are excluded and usage beyond included amounts can add charges. Confirm the live checkout and usage controls before purchase because prices, included credits, and terms can change: https://vercel.com/pricing

The current Terms of Service also limit Hobby to personal/non-commercial use, and the Fair Use Guidelines explicitly include affiliate linking as commercial use. References: https://vercel.com/legal/terms and https://vercel.com/docs/limits/fair-use-guidelines

**Budget note:** US$20/month is the current listed base subscription reference, not a complete cost forecast or billing approval. Do not upgrade or enable production deployment until the owner reviews usage limits, any additional usage charges, taxes, and account-specific checkout terms.

## Budget-first hosting decision update — 21 October 2026

**Recommendation: do not buy Vercel Pro now. Evaluate Cloudflare Pages Free first for the initial static editorial directory, after preview/manual acceptance.** This changes the preferred launch-host evaluation, not the fact that the owner originally selected Vercel; no provider account or deployment has been changed.

Why this fits the current project:
- The public site is built as static files by `python3 scripts/build_site.py` into `dist/`; the public artifact is allowlisted. The initial site does not require server-side rendering or a paid backend for its core pages.
- Cloudflare Pages supports GitHub integration, build commands and custom output directories; its current published Free limits include 500 builds/month, 100 custom domains per project, and 20,000 files. Static asset requests are free and unlimited. Official docs: https://developers.cloudflare.com/pages/configuration/git-integration/ https://developers.cloudflare.com/pages/configuration/build-configuration/ https://developers.cloudflare.com/pages/platform/limits/ https://developers.cloudflare.com/pages/functions/pricing/
- Proposed configuration to validate in a non-production preview: production branch `main`, build command `python3 scripts/build_site.py`, output directory `dist`. Confirm the build environment includes a compatible Python runtime; if not, build `dist` in GitHub Actions and publish the artifact through a supported Pages deployment workflow.
- Keep Vercel configuration in the repository for now; it does not itself force deployment. Do not purchase Vercel Pro merely because it is the existing config.

Comparison:
- **Cloudflare Pages Free — first option to test:** $0 hosting for this static site within published limits; custom domain and TLS supported. Verify the exact domain setup and all security headers/redirects before launch.
- **Netlify Free — fallback:** currently $0 with 300 credits/month and custom domains/SSL, but production deploys cost 15 credits each and sites can pause at the hard monthly limit. That is less predictable if content is updated often. Official pricing: https://www.netlify.com/pricing/
- **Vercel Pro — fallback if the project later needs Vercel-specific features:** currently listed at $20/month with included usage credit; overages/taxes and current checkout terms need review. Hobby is not an acceptable workaround for a commercial directory/affiliate business. Official policy: https://vercel.com/docs/limits/fair-use-guidelines and https://vercel.com/pricing

Important caveats:
- “Free hosting” is not “free business”: domain renewal, email, legal review, content/research, privacy, and payment/partner tools can still cost money.
- Do not move authoritative DNS nameservers blindly. First add the domain to the chosen provider, inspect the generated DNS records, preserve existing MX/SPF/DKIM/DMARC email records, then change only what is needed. Never delete mail records to make the website work.
- A preview deployment is not the public launch. Keep indexing blocked until legal/editorial review, manual live acceptance, domain verification, and the separate owner launch approval are complete.
- No Cloudflare/Netlify account was connected, no project was created, no DNS was changed, and no deployment was performed by this documentation update.

## Repository configuration

- Repository: beincasinos-Brand/Beincasinos, branch main.
- vercel.json runs python3 scripts/build_site.py and publishes dist.
- The build script uses an explicit allowlist and copies only the public static site into dist; internal prospect research, dossiers, source scripts and documentation are not published as output.
- Clean URLs and trailing slashes are enabled.
- Security headers and a same-origin Content Security Policy are configured in vercel.json.
- The Vercel configuration includes a permanent `www.beincasinos.online` to apex redirect. Cloudflare Pages `_headers` is prepared, but the `www` host redirect must be configured and manually verified in Cloudflare (a host-aware Redirect Rule) before launch.
- robots.txt remains set to Disallow: / for pre-launch; do not remove until the launch gate is intentionally cleared.
- GitHub Actions checks source HTML, JavaScript syntax, Vercel configuration, the public-only artifact and Chromium/accessibility smoke tests. These checks do not create a Vercel project, verify live response headers, or authorize deployment.

## Deployment sequence — Cloudflare Pages, preview first

1. Clear non-deployment launch gates: name/trademark review, publisher/contact verification, market/legal review, privacy/disclosure readiness, and publication eligibility for any operator profiles.
2. Owner creates a Cloudflare account, enables 2FA, and retains account/billing/recovery ownership. Never share passwords, 2FA codes, recovery codes or broad API tokens in chat.
3. Connect the private GitHub repository using the owner's authorized account flow. Confirm the GitHub app has only the repository access required. Configure build command `python3 scripts/build_site.py` and output directory `dist`; validate that the build environment has Python. If not, move artifact building into GitHub Actions and deploy the artifact using a supported Pages workflow.
4. Avoid enabling production auto-deploy until the owner has reviewed the settings and explicitly authorized the release. Use a preview deployment first when available and keep `robots.txt` blocked.
5. Confirm `dist/_headers` is present and that live responses preserve CSP, HSTS and other security headers. Test all 24 indexable routes, tools, real 404 status, HTTPS, canonical URLs, mobile layout, keyboard navigation, and absence of internal files.
6. Add `beincasinos.online` as a custom domain. If Cloudflare asks to onboard the zone, first record existing DNS and mail records at Spaceship. Change nameservers only after confirming the complete DNS set, preserving MX/SPF/DKIM/DMARC. Configure and test a host-aware permanent `www` to apex redirect.
7. After explicit public-launch approval only, deploy production, rerun live acceptance, intentionally remove the crawl block, verify Search Console ownership and submit the sitemap.

## Current implementation note

`cloudflare/_headers` is a source-controlled header rules file and `scripts/build_site.py` copies it to `dist/_headers`. CI validates the policy and artifact inclusion. The `www` redirect is not safely expressible as a host condition in the Pages `_redirects` file, so use a Cloudflare dashboard Redirect Rule or an equivalent verified host-level rule.

## Not done

No Cloudflare Pages project was created, no Git integration was enabled, no deployment was made, no paid plan was purchased, no DNS was changed, no Search Console submission was made, and no brand outreach was sent. The Vercel team remains unmodified.

## Status correction — 21 October 2026 (supersedes earlier deployment-status statements above)

The deployment-status statements in the original decision snapshot above are stale and must not be treated as current. The newer `docs/final-deploy-runbook.md` records that Cloudflare Pages project `beincasinos` is connected to this repository on `main`, with build command `python3 scripts/build_site.py`, output directory `dist`, and preview URL https://beincasinos.pages.dev/. The owner-provided Cloudflare Pages Custom Domains screenshot recorded in that runbook showed `beincasinos.online` as Active with SSL enabled. Read-only live checks on 2026-10-21 also retrieved the apex homepage, `robots.txt`, and a sitemap containing 32 canonical HTTPS URLs.

This does **not** mean the site is approved for public launch or indexing. Still unresolved: independent live HTTP status/security-header checks, exact Google verification endpoint and Search Console property status, `www` host redirect, DNS reconciliation before any DNS edits, mobile/accessibility/manual acceptance, credential hygiene/rotation, and legal/privacy/name/market approvals. The privacy and terms pages remain explicitly marked pre-launch drafts. `robots.txt` must remain blocked until the owner separately approves launch after applicable gates are cleared.

The read-only browser inspection of the Cloudflare dashboard is currently blocked because the browser automation wallet has insufficient balance; no dashboard changes, DNS edits, production deploy, or indexing changes were made as part of this status correction. The next safe step is to restore browser-tool wallet credit if the owner wants authenticated dashboard inspection; otherwise continue with read-only repository and public-host checks.

The GitHub Actions run recorded in the latest runbook, run ID `39669114286`, passed its 12 site-check steps on 2026-10-21. This is source/preview validation, not legal clearance or proof of live production HTTP status.
