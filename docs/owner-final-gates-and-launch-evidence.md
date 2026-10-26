# Owner final gates and launch evidence — BeInCasinos

**Status:** Internal working checklist. Release remains blocked until every applicable gate has dated evidence and the owner explicitly approves launch. This document is not legal advice and does not itself verify any account, domain, or third-party state.

## How to use this checklist

For each item, record status (NOT STARTED, IN PROGRESS, PASS, BLOCKED, or NOT APPLICABLE), date in UTC, reviewer, evidence URL/file, and any follow-up. A task is not passed because a setting or page merely exists.

## Gate A — Identity, name, and domain

- [ ] Obtain qualified trademark/name clearance for BeInCasinos and the “BEIN” element in intended markets; record advice and scope. Domain ownership alone is not trademark clearance.
- [ ] Confirm the publisher's legal identity, business form, address/contact requirements, and which identity may lawfully appear in the footer and policies.
- [ ] Confirm control of beincasinos.online in the registrar account and record renewal date, DNS state, and recovery method without exposing credentials.
- [ ] Confirm the business mailbox contact@beincasinos.online is accessible, deliverable, monitored, and appropriate for public business contact; configure recovery and spam monitoring.
- [ ] Confirm the public-facing contact and privacy-request process is monitored and has an owner.

## Gate B — hosting, billing, and deployment authority

- [ ] Use Cloudflare Pages Free as the preferred initial host, subject to review of current plan terms, usage limits, and suitability for the commercial directory and affiliate model.
- [ ] Owner explicitly approves any paid subscription, billing change, or plan upgrade before it is made; do not change billing as part of deployment preparation.
- [ ] Connect the GitHub repository to Cloudflare Pages only after confirming whether the action creates a deployment; keep production deployment blocked until the owner has approved that specific action. Vercel remains a fallback, not the current preferred host.
- [ ] Verify build command `python3 scripts/build_site.py`, output directory `dist`, and the explicit public-file allowlist.
- [ ] Keep production deployment and indexing blocked until all other gates pass.
- [ ] Never share API tokens, passwords, recovery codes, private keys, or billing information in chat or repository files.

## Gate C — legal, market, and privacy readiness

- [ ] Complete the market-by-market screening in `docs/tier-1-market-compliance-gate-2026-10-21.md`, then obtain qualified review and attach dated evidence for each intended market/product. The screening matrix is not legal clearance; do not treat a country as approved merely because a regulator page has been collected.

- [ ] Obtain jurisdiction-specific review of publisher obligations, gambling-related advertising, affiliate disclosures, consumer-protection rules, and age/market restrictions.
- [ ] Approve a concrete launch-market list rather than treating “international” as blanket permission. Current intended research markets are AU, US, FR, DE, CH, GB, and NL; each needs separate analysis.
- [ ] Do not present offshore gambling products as locally lawful or available unless primary-source evidence and qualified review support that exact claim.
- [ ] Review privacy notice against actual hosting logs, contact methods, cookies, analytics, embeds, outbound-link tracking, and third-party services that are actually enabled.
- [ ] Do not enable non-essential analytics/advertising trackers until consent and notice requirements have been assessed for each intended market.
- [ ] Define a process for privacy requests, corrections, complaints, takedowns, and retaining/deleting business-contact information.
- [ ] Confirm every commercial link, affiliate programme, and paid placement is permitted for the relevant audience and jurisdiction.

## Gate D — editorial and commercial integrity

- [ ] Review the public review methodology and make clear that paid placement cannot buy a better score, licence conclusion, safety claim, or ranking.
- [ ] Keep research leads and internal dossiers out of the public artifact unless each exact operator/domain/product has passed current primary-source and editorial checks.
- [ ] For each proposed public profile, verify legal entity, exact domain, current regulator record, product scope, terms, withdrawals, complaints, safer-gambling tools, enforcement history, and review date.
- [ ] Do not claim that 100 research leads are 100 approved casinos, customers, partners, or paying advertisers.
- [ ] Do not publish audience numbers, Search Console impressions, traffic, leads, conversion rates, or ROI unless they are real, dated, sourced, and explained.
- [ ] Do not sell paid inventory until audience evidence, offer terms, disclosures, delivery/reporting definitions, cancellation terms, and owner approval are ready.
- [ ] Do not send bulk unsolicited outreach or guessed email addresses. Verify official business contact routes and applicable anti-spam/privacy requirements first.

## Gate E — build, artifact, and live-host acceptance

- [ ] Build from a clean checkout using the documented public build command.
- [ ] Run python3 scripts/check_site.py, python3 scripts/check_deploy_artifact.py, host-config validation, JavaScript checks, Chromium tests, and accessibility automation as available in CI.
- [ ] Inspect the exact deploy artifact for internal prospect trackers, research dossiers, credentials, drafts, placeholders, private notes, and unapproved claims.
- [ ] Record commit SHA, artifact checksum/build ID, and the UTC time of release-candidate build.
- [ ] Test all canonical routes, deep links, trailing slashes, missing pages, custom 404 status, images, local assets, external links, and interactive tools on the actual preview host.
- [ ] Test 320px through desktop widths, zoom/reflow, keyboard-only navigation, visible focus, screen-reader basics, and at least one real mobile device. Record unavailable browsers/devices as not tested.
- [ ] Verify HTTPS, apex/www redirects, canonical tags, sitemap responses, security headers, CSP, caching, and absence of internal files on the live preview.
- [ ] Keep the pre-launch crawl block in place until the owner has explicitly approved public launch and indexing.

## Gate F — indexing and release decision

- [ ] Every sitemap URL is a final canonical URL that returns HTTP 200 on the approved host.
- [ ] Confirm robots.txt and meta robots settings match the documented launch decision.
- [ ] Confirm domain verification for Search Console only after owner approval and control verification.
- [ ] Submit the sitemap only after launch approval; inspect representative URLs and record results.
- [ ] Save dated evidence and unresolved risks for all gates.
- [ ] Owner records explicit approval for production deployment.
- [ ] Owner records separate explicit approval to enable crawling/indexing.

## Release record

- Approved brand/legal identity:
- Domain/DNS verification evidence:
- Hosting plan and billing approval:
- Approved launch markets:
- Legal/privacy reviewer and date:
- Commit SHA:
- Artifact checksum/build ID:
- Preview URL and acceptance-test evidence:
- Production URL:
- Open defects / accepted risks:
- Production-deploy approval reference:
- Indexing approval reference:

**Fail-closed rule:** If any critical identity, trademark, market-law, privacy, artifact-leakage, host/billing, or owner-approval gate is unresolved, keep release blocked.