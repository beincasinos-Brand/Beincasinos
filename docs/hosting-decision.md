# Hosting decision — Vercel selected

**Provider decision:** Vercel is the selected hosting platform for BeInCasinos.
**Deployment status:** not connected, not deployed, and not public.
**Current account finding:** the connected team is **BeinCasinos** (slug: bein-casinos), on the **Hobby** plan, with no linked projects. Verified by read-only account inspection on 21 October 2026.

## Plan and commercial-use gate

Vercel's official Fair Use Guidelines restrict Hobby to personal/non-commercial use and explicitly describe affiliate-link sites whose primary purpose is affiliate linking as commercial use: https://vercel.com/docs/limits/fair-use-guidelines

Therefore, **do not deploy the planned commercial BeInCasinos directory to the current Hobby team**. The expected path is Vercel Pro or another Vercel plan whose current terms explicitly permit the planned paid-listing and affiliate business. Before upgrading, review current price, usage/billing terms, limits, and relevant acceptable-use terms at https://vercel.com/pricing. No upgrade, purchase, or billing change has been made.

The owner has selected Vercel, so provider choice is no longer open. Plan/billing approval remains a separate consequential step and does not block code, content, SEO, or test preparation.

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
