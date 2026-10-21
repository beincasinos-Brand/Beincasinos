# Hosting decision — Vercel selected

**Provider decision:** Vercel is the selected hosting platform for BeInCasinos.
**Deployment status:** not connected, not deployed, and not public.
**Current account finding:** the connected team is **BeinCasinos** (slug: bein-casinos), on the **Hobby** plan, with no linked projects. Verified by read-only account inspection on 21 October 2026.

## Plan and commercial-use gate

Vercel's official Fair Use Guidelines restrict Hobby to personal/non-commercial use and explicitly describe affiliate-link sites whose primary purpose is affiliate linking as commercial use: https://vercel.com/docs/limits/fair-use-guidelines

Therefore, **do not deploy the planned commercial BeInCasinos directory to the current Hobby team**. The expected path is Vercel Pro or another Vercel plan whose current terms explicitly permit the planned paid-listing and affiliate business. Before upgrading, review current price, usage/billing terms, limits, and relevant acceptable-use terms at https://vercel.com/pricing. No upgrade, purchase, or billing change has been made.

The owner has selected Vercel, so provider choice is no longer open. Plan/billing approval remains a separate consequential step and does not block code, content, SEO, or test preparation.

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
- A permanent www.beincasinos.online to https://beincasinos.online redirect is configured and validated in CI.
- robots.txt remains set to Disallow: / for pre-launch; do not remove until the launch gate is intentionally cleared.
- GitHub Actions checks source HTML, JavaScript syntax, Vercel configuration, the public-only artifact and Chromium/accessibility smoke tests. These checks do not create a Vercel project, verify live response headers, or authorize deployment.

## Deployment sequence — when the final stage is authorized

1. Clear non-deployment launch gates: name/trademark review, publisher/contact verification, market/legal review, privacy/disclosure readiness, and publication eligibility for any operator profiles.
2. Confirm an appropriate Vercel commercial plan and billing/usage budget.
3. Create/link the Vercel project to the GitHub repository in the intended team, using the existing vercel.json. Avoid enabling production deployment until the owner is ready for that final stage.
4. Set build command to python3 scripts/build_site.py and output directory to dist; confirm no framework preset overrides the static build.
5. Use a preview/staging deployment first when authorized, keeping crawling blocked. Test all routes/tools, 404 status, CSP and security headers, HTTPS, redirects, canonical URLs, mobile layout and absence of internal files.
6. Configure the custom domain in Vercel and then apply only the exact DNS records Vercel supplies in Spaceship; preserve existing mail-related records.
7. After explicit public-launch approval, perform production deployment, re-run live acceptance tests, remove the crawl block only when approved, and only then verify Search Console and submit the sitemap.

## Not done

No Vercel project was created, no Git integration was enabled, no deployment was made, no paid plan was purchased, no DNS was changed, no Search Console submission was made, and no brand outreach was sent.
