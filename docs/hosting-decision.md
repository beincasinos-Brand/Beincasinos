# Hosting decision note — 20 October 2026

**Recommendation: evaluate Netlify Free only for a private preview/staging build; do not treat it as the production plan for a commercial site with ambitious growth goals. Choose the production tier after a realistic traffic/cost estimate and current acceptable-use review. Do not deploy publicly until launch blockers are closed and the owner explicitly approves publishing.** This is a documented recommendation, not a completed account setup or provider acceptance.

## Current account checks

A read-only inspection of the connected Vercel context on 20 October 2026 returned a team on the Hobby plan with no linked projects. No project was created and no deployment was made.

Vercel's official Fair Use Guidelines restrict Hobby to personal/non-commercial use and explicitly include affiliate-link sites whose primary purpose is affiliate linking among commercial examples: https://vercel.com/docs/limits/fair-use-guidelines . Therefore, do not deploy the intended paid-listing/affiliate business on that Hobby team. Vercel Pro is a paid alternative, but no subscription or upgrade is approved.

## Candidate comparison

| Option | Current published plan facts checked | Fit for this project | Limit / caution |
|---|---|---|---|
| Netlify Free | Official pricing lists $0/month, custom domains with SSL, global CDN, and a 300-credit monthly hard limit: https://www.netlify.com/pricing/ . Netlify's official announcement says the Free plan supports commercial projects: https://www.netlify.com/blog/introducing-netlify-free-plan/ | Suitable for private preview/staging and smoke-testing while keeping recurring spend at $0 | If the credit limit is reached, projects can pause until the next cycle. Not recommended as a production commitment until realistic traffic is forecast; confirm current terms and acceptable-use policy for this gambling-information business. No provider acceptance has been obtained. |
| Vercel Hobby | Official policy restricts Hobby to personal/non-commercial use: https://vercel.com/docs/limits/fair-use-guidelines | Not suitable for the planned commercial site on the currently connected Hobby team | Do not use Hobby for the paid-listing/affiliate business. |
| Vercel Pro | Official pricing and current plan terms: https://vercel.com/pricing | Technically viable if owner prefers to stay on Vercel and approves the recurring cost | Paid plan; price and usage terms must be reviewed at decision time. No upgrade made. |

## Prepared repository state

- `netlify.toml` now runs `python3 scripts/build_site.py`, publishes only `dist/`, and defines baseline security headers including a Content Security Policy (CSP).
- `vercel.json` remains in place as an alternative-host configuration with matching security headers.
- The CSP now uses `script-src 'self'` without allowing inline scripts. Calculator and checklist logic was moved to same-origin JavaScript files, and the source checker fails if an HTML page reintroduces an inline script. Inline styles remain allowed because some tool-page presentation is still embedded; this is a hardened baseline, not a fully strict nonce/hash-based CSP.
- CI runs `scripts/check_host_config.py` to parse the Vercel JSON, validate the expected headers in both host configurations, and detect drift before a deployment. Passing this check verifies configuration text only; deployed response headers still require testing on the chosen host.
- CI successfully built the public-only artifact and checked it for leaks on commit `76f7a5f3f24d2f29f2197f757f4f663650ca452`: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39488962203.
- Neither configuration changes DNS, creates a hosting account, deploys the website, enables indexing, or verifies that the production domain resolves.

## Go/no-go checklist before a provider decision

- [ ] Resolve the BeInCasinos / “BEIN” trademark-name question before public launch.
- [ ] Verify domain registration, renewal, and DNS access in Spaceship.
- [ ] Confirm the publisher identity and monitored contact route.
- [ ] Review the first actual launch market and every commercial content/placement against current primary sources and qualified legal advice where needed.
- [ ] Finalize privacy, disclosures, corrections, and responsible-gambling resources.
- [ ] Test the site locally and in a real browser at desktop/mobile sizes.
- [ ] Owner chooses the provider and approves any cost or account connection.
- [ ] Deploy a private/preview build first if the provider supports it; verify HTTPS, redirects, headers, tools, assets, and 404 before public release.
- [ ] Keep indexing blocked until explicit launch approval.

**Current status: prepared only. No hosting provider has been selected or connected to this repository. Netlify Free is now a preview/staging candidate only, not a production-tier decision.**
