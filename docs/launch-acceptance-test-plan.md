# Launch acceptance test plan

**Status: NOT RUN — manual browser and live-host tests are required.** This plan prevents source-level CI from being mistaken for production QA. Record evidence and a date for each test; a checked box without evidence is not a pass.

## Test record

For each row, record: status (NOT STARTED, PASS, FAIL, BLOCKED), UTC timestamp, tester, browser/device, evidence link or screenshot, defect ID, and retest result. Do not use screenshots that expose credentials, private customer data, or admin interfaces.

## A. Before testing a live host

- [ ] Owner confirms trademark/name decision and publisher/legal identity.
- [ ] Owner confirms domain registration, renewal, DNS control and intended canonical hostname.
- [ ] Owner explicitly approves the selected hosting provider and public deployment.
- [ ] Legal/privacy review approves market scope, advertising, affiliate plan, disclosures and privacy notice.
- [ ] The final artifact is built from the public allowlist (python3 scripts/build_site.py) and passes python3 scripts/check_site.py and python3 scripts/check_deploy_artifact.py.
- [ ] The artifact is inspected for private/internal files, TODOs, placeholders, unapproved contact details, draft policies, secrets and unverified commercial claims.
- [ ] Keep the pre-launch robots block until a separate written launch approval; do not submit the sitemap to Search Console before that approval.

## B. Responsive and cross-browser checks

Run at minimum on current stable Chrome and Firefox desktop, Safari on a real Apple device if available, and Chrome on Android. If a device/browser cannot be tested, record it as not tested rather than passed.

- [ ] Home, Reviews hub, guides, market research, responsible gambling, privacy, editorial policy, about/contact, each tool, and custom 404 render without horizontal overflow at 320px, 375px, 768px, 1024px and 1440px viewport widths.
- [ ] Navigation, footer, external links, breadcrumbs and in-page anchors work with mouse, touch and keyboard.
- [ ] BIC monogram/logo is crisp and legible at favicon, header and compact mobile sizes; full BeInCasinos wordmark remains readable beside it.
- [ ] Reviews hub explains eligibility gates, evidence standards, scoring weights and commercial independence; it does not imply that unverified operators have been scored or ranked.
- [ ] No clipped text, overlapping controls, broken images, console errors, failed local resources or layout shifts that obstruct use.
- [ ] Zoom to 200% and reflow at narrow width; content and controls remain available.
- [ ] Browser back/forward, direct deep links, trailing-slash routes and refresh work on the selected host.
- [ ] The host serves the custom 404 with HTTP 404 status; missing assets return appropriate status codes.

## C. Keyboard, accessibility and safety

- [ ] Tab order follows the visible reading order; every interactive control has a visible focus indicator.
- [ ] All functionality is usable without a mouse; no keyboard trap.
- [ ] Page language is correct, headings are meaningful, link text is descriptive, and labels/instructions are associated with form controls.
- [ ] Check colour contrast against WCAG 2.2 AA targets; do not rely on colour alone to convey state.
- [ ] Use an automated accessibility scan as a supplement, then manually test the calculator and checklist with keyboard and a screen reader where possible.
- [ ] Wagering calculator validates empty, negative, malformed, very large and decimal inputs; output explains its assumptions and does not imply a prediction or guaranteed result.
- [ ] Terms checklist progress updates correctly; reset requires a clear action; print/save output is readable and contains no unexpected navigation controls.
- [ ] Safer-gambling contacts and official regulator links open the intended authoritative resources.

## D. SEO, indexing and canonical host

- [ ] Confirm intended apex/www host behaviour and HTTPS redirects; choose one canonical hostname and ensure no redirect loops.
- [ ] Every indexable page has a self-consistent canonical URL, title, description, social metadata and a single useful H1.
- [ ] 404 and any private/pre-launch routes are not indexable.
- [ ] Confirm robots response and meta robots behaviour match the approved release decision. Do not remove the site-wide crawl block without explicit approval.
- [ ] Sitemap contains only final canonical URLs returning HTTP 200; no draft, redirecting, blocked, duplicate or missing pages.
- [ ] Verify structured metadata, favicon, manifest and social previews using suitable validators.
- [ ] Check the Reviews hub is included in the public build and sitemap and that every sitemap URL resolves to the intended canonical page after deployment.
- [ ] Only after launch approval, connect Search Console, verify domain ownership, inspect a representative URL and submit the sitemap.

## E. Privacy, security and commercial links

- [ ] Inspect deployed requests, cookies, local storage and network traffic. Update the privacy notice to reflect actual host logs, forms, analytics, embedded resources and third parties.
- [ ] Do not enable non-essential analytics/advertising tracking until required consent controls and notices are reviewed for each intended jurisdiction.
- [ ] Verify HTTPS, security headers, content-type behaviour, cache behaviour and host error pages using the selected provider's tools.
- [ ] Check forms (if any) for validation, success/error states, spam protections, secure processing and an owner-monitored destination. If no form exists, confirm no non-functional contact form is shown.
- [ ] Check all external commercial links and affiliate terms against permitted markets. Confirm no unapproved affiliate links, unsupported traffic claims, misleading rankings, or hidden paid placement.
- [ ] Test disclosure visibility on desktop and mobile. Paid placements must be labelled clearly near the placement.
- [ ] Confirm correction, complaint, privacy request and stale-information workflows have a monitored owner.

## F. Release decision

A release is BLOCKED if any of these remain unresolved: brand/trademark clearance, publisher identity/contact, domain/DNS verification, commercial hosting approval, market-specific legal review, privacy implementation, critical accessibility/usability defects, artifact leakage, or owner launch approval.

Release evidence:
- Commit SHA:
- Artifact checksum / build ID:
- Host and canonical URL:
- UTC test date:
- Reviewer:
- Open defects and accepted risks:
- Explicit owner approval reference:
- Indexing approval reference:

A CI pass confirms only the checks that CI actually runs. It does not mean the items above have passed, and this document is not legal advice.
