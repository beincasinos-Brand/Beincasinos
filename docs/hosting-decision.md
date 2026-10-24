# Hosting decision — Cloudflare Pages Free preferred

**Current preferred provider:** Cloudflare Pages Free for the initial static site, subject to preview acceptance.
**Deployment status (latest evidence):** Cloudflare Pages project `beincasinos` is connected to the GitHub repository and has produced successful preview deployments, including a preview for this work branch. This does not mean the latest commit has passed GitHub CI or that production release is approved. Keep production deployment and indexing blocked until all release gates pass.
**Previous account finding:** the connected Vercel team is **BeinCasinos** (slug: bein-casinos), on the **Hobby** plan, with no linked projects. Verified by read-only account inspection on 21 October 2026.

## Plan and commercial-use gate

Vercel's official Fair Use Guidelines restrict Hobby to personal/non-commercial use and explicitly describe affiliate-link sites whose primary purpose is affiliate linking as commercial use: https://vercel.com/docs/limits/fair-use-guidelines

Therefore, **do not deploy the planned commercial BeInCasinos directory to the current Hobby team**. The expected path is Vercel Pro or another Vercel plan whose current terms explicitly permit the planned paid-listing and affiliate business. Before upgrading, review current price, usage/billing terms, limits, and relevant acceptable-use terms at https://vercel.com/pricing. No upgrade, purchase, or billing change has been made.

The owner subsequently preferred Cloudflare Pages Free to avoid the Vercel Pro monthly cost. Later deployment-runbook and Cloudflare check-run evidence record the `beincasinos` Pages project connected to this repository and branch previews being generated. Recheck current project settings and preview freshness before relying on them. Code, content, SEO and test preparation can continue without a production release.

### Current plan-price reference — checked 21 October 2026

Vercel's official pricing page currently lists Pro at **US$20/month**, with **US$20 of included usage credit**; taxes are excluded and usage beyond included amounts can add charges. Confirm the live checkout and usage controls before purchase because prices, included credits, and terms can change: https://vercel.com/pricing

The current Terms of Service also limit Hobby to personal/non-commercial use, and the Fair Use Guidelines explicitly include affiliate linking as commercial use. References: https://vercel.com/legal/terms and https://vercel.com/docs/limits/fair-use-guidelines

**Budget note:** US$20/month is the current listed base subscription reference, not a complete cost forecast or billing approval. Do not upgrade or enable production deployment until the owner reviews usage limits, any additional usage charges, taxes, and account-specific checkout terms.

## Budget-first hosting decision update — 21 October 2026

**Recommendation: do not buy Vercel Pro now. Use Cloudflare Pages Free for the initial static editorial directory, subject to preview/manual acceptance.** Cloudflare Pages is now the preferred and configured host; `vercel.json` remains only an alternative-host configuration. Preview deployment is not production approval.

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
- A Cloudflare Pages project and Git integration are now recorded in the final deployment runbook, with successful branch-preview deployments. No DNS change, paid plan purchase, or production release was performed by this documentation update.

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
2. Verify the owner's Cloudflare account access, 2FA, recovery and billing ownership for the existing Pages project. Never share passwords, 2FA codes, recovery codes or broad API tokens in chat.
3. Verify the existing GitHub integration is connected to the intended repository and that the production branch and preview branch controls are correct. Confirm build command `python3 scripts/build_site.py` and output directory `dist`; validate that the build environment has Python. If not, move artifact building into GitHub Actions and deploy the artifact using a supported Pages workflow.
4. Avoid enabling production auto-deploy until the owner has reviewed the settings and explicitly authorized the release. Use a preview deployment first when available and keep `robots.txt` blocked.
5. Confirm `dist/_headers` is present and that live responses preserve CSP, HSTS and other security headers. Test all 24 indexable routes, tools, real 404 status, HTTPS, canonical URLs, mobile layout, keyboard navigation, and absence of internal files.
6. Add `beincasinos.online` as a custom domain. If Cloudflare asks to onboard the zone, first record existing DNS and mail records at Spaceship. Change nameservers only after confirming the complete DNS set, preserving MX/SPF/DKIM/DMARC. Configure and test a host-aware permanent `www` to apex redirect.
7. After explicit public-launch approval only, deploy production, rerun live acceptance, intentionally remove the crawl block, verify Search Console ownership and submit the sitemap.

## Current implementation note

`cloudflare/_headers` is a source-controlled header rules file and `scripts/build_site.py` copies it to `dist/_headers`. CI validates the policy and artifact inclusion. The `www` redirect is not safely expressible as a host condition in the Pages `_redirects` file, so use a Cloudflare dashboard Redirect Rule or an equivalent verified host-level rule.

## Not done

The Cloudflare Pages project and Git integration exist, and branch-preview deployments have succeeded. The latest preview is not proof of a production release. No paid plan was purchased, no DNS change or production deployment was made by this documentation update, no Search Console submission was made, and no brand outreach was sent. The Vercel team remains unmodified.
