# BeInCasinos — owner action pack for final launch

**Snapshot:** 21 October 2026  
**Release state:** BLOCKED. This document makes the remaining owner-controlled decisions explicit; it does not authorize deployment.

The source repository already has a passing automated build/browser-smoke record. Do not repeat source changes merely to make the project look more complete while the actual launch gates remain unresolved.

## Automated evidence — updated 21 October 2026, 23:15 UTC

- Last fully completed successful static-check run before the latest content updates: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39689501457 on commit `c2c937816daccef6e4dcbb0ef9d5a2660640d5d2`. That run passed the HTML/local-link checks, sales-pipeline checks, JavaScript syntax, build/security configuration, public-only artifact check, Chromium smoke tests, and artifact storage.
- A later withdrawal-guide update introduced a mobile horizontal-overflow failure at 320px; the failure was traced to the new comparison table. Responsive table CSS was added in commit `e003f755069410e446ffdd3428f578327af3f220`, and later runs are checking the fix alongside subsequent documentation changes. The latest static-check run passed on commit `be7ff9c3f4b21c727b4b1a202df7dad369901e8f`: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39690835975. Read-only Cloudflare diagnostics also passed on that commit: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39690835990. The source sitemap now has 36 URLs, including the bonus-expiry and maximum-cashout guides. The bonus-expiry guide is verified live. The maximum-cashout page content is visible, but its latest live title/Open Graph metadata and sitemap were still cached from the prior deployment during the last check; final CI and post-deploy verification remain pending. Search Console still needs a fresh 36-URL sitemap submission; browser automation could not start because the TinyFish wallet is negative. Actual Google index coverage is not verified.
- The latest completed read-only Cloudflare diagnostic, https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39689728447, passed DNS, token validation and Pages deployment inspection. These checks do not establish Google indexing or clear legal/privacy gates.

The README and project completion board point to the latest successful source-check run noted above. The Vercel team still has no linked project. On 21 October 2026, the owner explicitly requested full-site discoverability and the public robots.txt was changed to Allow: /; the source sitemap now contains 36 URLs. This permits crawling but does not prove Google has indexed any URL. Search Console currently reports a prior sitemap submission of 32 URLs; the updated 36-URL sitemap still needs resubmission/verification. The Search Console connector is read-only and browser resubmission is blocked until the TinyFish wallet is topped up. DNS was not edited, no paid hosting plan was purchased, and no prospect outreach was sent. Scored casino reviews and commercial promotion remain blocked until the evidence and owner-controlled decisions below are resolved.

## What is already prepared

- Static HTML/CSS/JavaScript site with 23 planned indexable content routes, a public-only build allowlist, canonical metadata, sitemap, crawl block, security-header configuration, and a configured Vercel build.
- Educational calculator and terms checklist, editorial policy, review methodology, affiliate disclosure, operator information, complaint/licensing guides, and privacy/terms pages marked for pre-launch review where appropriate.
- Internal brand research queue and a separate paid-listing pipeline with evidence/status validation. Leads are not confirmed buyers, and no outreach has been sent.
- Automated checks for source structure, local links, public artifact leakage, configuration, and Chromium browser behaviour.

## Required owner decisions and evidence

Mark each item complete only when evidence exists. Never put passwords, tokens, recovery codes, private inbox contents, or billing details in GitHub.

### 1. Brand and publisher identity
- [ ] Decide whether to retain BeInCasinos after qualified trademark review of “BeInCasinos” and “BEIN” in intended classes/markets.
- [ ] Confirm the legal publisher/controller identity and required public business disclosures; “Anass Amir” is currently recorded as the chosen display identity, not independently verified as the full legal publisher disclosure.
- [ ] Verify access, recovery protection, and monitoring of contact@beincasinos.online.

### 2. Domain and hosting
- [ ] In Spaceship, verify beincasinos.online registration, renewal, DNS access, and current records; preserve existing mail records.
- [ ] Review current Vercel commercial plan terms, price, usage and potential extra charges. Hobby is not the intended plan for this commercial model.
- [ ] Explicitly approve any paid plan or billing change before purchase.
- [ ] Only after the above, authorize creation/linking of a Vercel project for a controlled preview. Project creation may trigger a build.
- [ ] Keep the production release held and robots.txt blocking crawlers.

### 3. Legal, privacy, and markets
- [ ] Obtain qualified review of publisher obligations, gambling advertising/affiliate rules, consumer disclosures, and Moroccan Law 09-08/CNDP requirements based on the actual data flows and host.
- [ ] Select the first intended market(s) explicitly. “International” is not blanket approval.
- [ ] Keep Australia and France online-casino promotion blocked unless qualified review confirms a specific lawful model; US requires state/product review. Complete equivalent exact-operator/domain checks for GB, DE, CH, and NL.
- [ ] Approve the privacy notice against actual host logs, email/contact workflow, analytics, cookies, third parties, and any future affiliate tracking.
- [ ] Keep non-essential analytics, advertising pixels, and affiliate tracking disabled until their applicable reviews and disclosures are complete.

### 4. Editorial and commercial integrity
- [ ] Keep unverified casino dossiers internal; publish a profile only after exact entity, domain, regulator, product, territory, terms, withdrawals, complaints, and safer-gambling checks pass.
- [ ] Do not describe research leads as verified casinos, customers, partners, or confirmed buyers.
- [ ] Do not promise a top-10 position, favourable rating, audience, traffic, leads, conversions, or return on spend in exchange for payment.
- [ ] Before selling any placement, approve a written offer covering label/placement, duration, deliverables, reporting definitions, cancellation/removal, invoice/payment terms, market scope, and editorial independence.
- [ ] Obtain legal review of the relevant fixed-fee, CPA, revenue-share, hybrid, and affiliate terms. No price or willingness-to-pay is verified until directly supported by evidence.
- [ ] Do not send bulk unsolicited outreach or guessed email addresses. Verify official contact routes, market eligibility, and applicable anti-spam rules first.

### 5. Release candidate and manual acceptance
- [ ] Build a clean release candidate using `python3 scripts/build_site.py`.
- [ ] Run `python3 scripts/check_site.py`, `python3 scripts/check_deploy_artifact.py`, host-config checks, JavaScript checks, and the Chromium browser suite.
- [ ] Inspect the exact public artifact for internal research, drafts, secrets, placeholders, and unsupported claims.
- [ ] After a preview is authorized, record commit SHA/build ID and test every route/tool, 404 status, HTTPS, canonical/redirect behaviour, security headers/CSP, mobile widths, keyboard navigation, and live network/cookie behaviour.
- [ ] Perform manual keyboard, zoom/reflow, and screen-reader checks; automated axe results are not a full accessibility certification.
- [ ] Test official outbound links and ensure the privacy notice matches the deployed behaviour.

### 6. Separate launch and indexing approvals
- [ ] Record dated evidence for every applicable blocker in `docs/launch-evidence-register-template.csv`.
- [ ] Explicitly approve public production deployment only after all critical gates pass.
- [x] Owner approved public discoverability on 21 October 2026; robots.txt allows crawling. Re-test the live host and verify deployment before relying on the new sitemap.
- [x] Owner requested full-site discoverability on 21 October 2026.
- [ ] Verify Search Console ownership, submit the current 36-URL canonical sitemap, and confirm indexing status.

## Fail-closed rule

If brand/legal identity, market permission, privacy, commercial hosting/billing, artifact integrity, live-host acceptance, or owner approval is unresolved, do not publicly deploy or enable indexing. These steps require owner account access, third-party review, or explicit decisions; source-code changes cannot honestly substitute for them.
