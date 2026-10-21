# BeInCasinos — owner action pack for final launch

**Snapshot:** 21 October 2026  
**Release state:** BLOCKED. This document makes the remaining owner-controlled decisions explicit; it does not authorize deployment.

The source repository already has a passing automated build/browser-smoke record. Do not repeat source changes merely to make the project look more complete while the actual launch gates remain unresolved.

## Latest automated evidence — 21 October 2026, 13:16 UTC

The full GitHub Actions workflow passed on commit `41c01a57ba2d7923b5fe67389e35be322fe0c79a`: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39606573744. The run covers source/local-link checks, sales-pipeline hard gates and regression tests, JavaScript syntax, Vercel configuration, public-only artifact leakage, and Chromium browser smoke tests. It is not a live deployment or legal/privacy review.

The README and project completion board now point to this latest passing run. The Vercel team still has no linked project. No deployment, DNS edit, paid-plan purchase, indexing, or prospect outreach has been performed. Keep release blocked until the evidence and owner-controlled decisions below are resolved.

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
- [ ] Verify access, recovery protection, and monitoring of beincasinos@gmail.com.

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
- [ ] Re-test the live host and preserve the crawl block until a separate indexing decision.
- [ ] Explicitly approve indexing, then verify Search Console ownership and submit the canonical sitemap.

## Fail-closed rule

If brand/legal identity, market permission, privacy, commercial hosting/billing, artifact integrity, live-host acceptance, or owner approval is unresolved, do not publicly deploy or enable indexing. These steps require owner account access, third-party review, or explicit decisions; source-code changes cannot honestly substitute for them.
