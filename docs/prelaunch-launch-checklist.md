# Pre-launch readiness checklist

This checklist is the release gate for BeInCasinos. It is intentionally conservative because gambling information is jurisdiction-specific and the project plans to earn money from paid listings first and affiliate links later.

## Status key

- `NOT STARTED`: no evidence recorded.
- `IN PROGRESS`: work underway; do not treat as passed.
- `PASS`: evidence is recorded and a reviewer has checked it.
- `BLOCKED`: an owner decision, external account, legal review, or third-party action is required.
- `NOT APPLICABLE`: explain why in the evidence/notes field.

Do not mark an item PASS just because a page exists. Record the evidence, reviewer, and date.

## Gate 1 — Name, ownership, and business decisions

- [ ] Check the proposed name against relevant trademark databases, including WIPO Global Brand Database and Morocco's OMPIC; check relevant markets too.
- [ ] Assess confusion risk with existing media, sports, gambling, and casino brands. Search results alone are not legal clearance.
- [ ] If uncertainty remains, obtain qualified trademark/legal advice before public launch or further branding investment. The owner reports that `beincasinos.online` has now been purchased; acquisition is not trademark clearance.
- [ ] Verify `beincasinos.online` registration, renewal details, and DNS access in Spaceship. The owner reports the purchase is complete; account status has not been independently inspected. Domain purchase is not trademark clearance.
- [ ] Confirm the publisher/legal business identity and verify a monitored contact email. A purchase notification mentions `beincasinos@gmail.com`, but this alone does not establish a public contact process.
- [x] Record intended target markets: AU, US, FR, DE, CH, GB, NL. This is a research scope, not blanket permission to publish or promote casino offers in each market; follow `docs/target-market-regulatory-matrix.md`.
- [ ] Confirm that the owner accepts the business model: listing fees first after audience evidence; affiliate links later and secondary.

## Gate 2 — Editorial evidence and brand profiles

- [ ] Keep the 100-brand queue as research prospects, not recommendations or a verified operator list.
- [ ] For every proposed profile, verify the exact official domain and legal operating entity.
- [ ] Check the applicable regulator's current primary-source register for the target jurisdiction and product type.
- [ ] Record allowed and excluded territories, licence scope, source URL, check date, and reviewer.
- [ ] Review official terms, bonus conditions, payment/withdrawal rules, complaints route, age limits, and safer-gambling tools.
- [ ] Add only useful, original analysis; do not publish 100 thin pages to reach a count.
- [ ] Separate facts from opinion and commercial status. A payment must never buy a positive verdict or override evidence.
- [ ] Do not state that a brand is legal, safe, licensed, available, or recommended unless the claim is narrowly supported for the named market and date.
- [ ] Create a correction/removal process for stale or challenged information.

## Gate 3 — Commercial disclosures

- [ ] Define the paid-listing package, duration, renewal/cancellation, invoicing, refund policy, and what a fee does and does not buy.
- [ ] Label paid placement clearly and close to the placement (for example, “Paid listing”); do not disguise ads as editorial rankings.
- [ ] Publish a commercial disclosure page before accepting payment.
- [ ] Keep editorial review criteria independent of listing fees and affiliate commission.
- [ ] Before any affiliate links go live, check each programme's contract, approved territories, promotion restrictions, and required disclosures.
- [ ] Test all outbound commercial links and maintain a dated register of partners, links, terms, and disclosures.
- [ ] Do not sell placements or promise reach/conversions before real audience data exists.

## Gate 4 — Privacy, cookies, and user safety

- [ ] Review the privacy notice against the actual deployment, forms, analytics, logs, hosting, and third-party services.
- [ ] Do not claim “no tracking” or “no data collected” without verifying the deployed implementation and providers.
- [ ] If non-essential analytics/advertising cookies or similar technologies are used, implement the consent/notice controls required for the target jurisdictions before enabling them.
- [ ] Provide a monitored contact/correction route and a process to handle privacy requests.
- [ ] Review responsible-gambling resources, age-appropriate messaging, and local restrictions for the target market.
- [ ] Make clear that educational tools are not gambling advice, predictions, legal advice, or guarantees.
- [ ] Do not collect financial, identity, gambling-account, or other sensitive data unless necessary, lawful, secured, and explicitly designed for that purpose.

## Gate 5 — Technical QA and SEO

- [x] GitHub Actions source checks, public-only build, and deployment-artifact leak checks passed on commit `76f7a5f3f24d2f29f2197f757f4f663650ca452` (run 39488962203). Repeat on the final release commit; this is not browser or production QA.
- [x] Add canonical URL and Open Graph/Twitter summary metadata to all 18 public HTML pages; CI now checks canonical and `og:url` values against the intended production origin. Review titles, descriptions, headings, links, and mobile navigation as part of release QA.
- [ ] Confirm canonical/social metadata, internal links, assets, redirects, HTTPS, and 404 handling on the actual production domain after a host is selected.
- [ ] Test the wagering calculator with empty, zero, negative, non-numeric, extremely large, and valid inputs.
- [ ] Test the checklist tool on desktop/mobile, keyboard-only, print/PDF, reset, and progress updates.
- [ ] Perform real browser tests at mobile and desktop sizes, including keyboard navigation and focus visibility.
- [ ] Review accessibility manually; automated/source checks are not a full accessibility audit.
- [ ] Check page performance, image sizing, caching, HTTPS, and browser console/network errors.
- [x] Add canonical/social metadata to all 18 public HTML pages and enforce canonical/`og:url` consistency in CI. The source sitemap uses `https://beincasinos.online`; live domain/DNS/HTTPS and final host redirects remain unverified.
- [x] Keep `robots.txt` blocking until explicit launch approval. Sitemap URLs currently use the intended domain; do not submit the sitemap to Search Console until the live site and canonical host are verified.

## Gate 6 — Hosting and security

- [x] Compare hosting options and document the current recommendation in `docs/hosting-decision.md`. The connected Vercel Hobby team is not suitable for this commercial site; Netlify Free is a candidate pending current terms/acceptable-use review and owner approval.
- [ ] Owner explicitly selects a host after reviewing current commercial-use terms, acceptable-use policy, plan limits, and any recurring costs. No hosting account has been connected.
- [ ] If using Vercel, confirm the plan is permitted for commercial use; do not use Hobby for this commercial project.
- [ ] Review repository visibility, branch protections, GitHub Actions permissions, dependency/update practices, and secret handling.
- [ ] Never commit API keys, account credentials, private contact data, or production secrets.
- [ ] Configure HTTPS, DNS, error handling, backups/version recovery, and security/contact ownership as applicable.
- [ ] No domain purchase, paid upgrade, or deployment is authorized by this checklist alone; obtain owner approval first.

## Gate 7 — Launch sequence

1. Record name-clearance decision and selected initial market.
2. Confirm publisher identity, contact, privacy/cookie implementation, editorial policy, and commercial disclosures.
3. Complete the evidence review for every page/operator claim intended for launch.
4. Complete browser/mobile/accessibility and technical QA; record release commit and results.
5. Verify the owner-reported domain registration and access in Spaceship; do not buy the same domain again.
6. Obtain explicit owner approval for hosting/plan costs and deployment.
7. Configure the real domain, HTTPS, canonical/social URLs, and production sitemap.
8. Recheck the production site while indexing remains blocked.
9. Obtain explicit owner approval to remove the robots block and enable indexing.
10. Verify the domain in Google Search Console using DNS TXT, submit the real sitemap, and monitor indexing/errors.
11. Record launch date and establish monthly review for stale brand/regulatory/terms information.

## Launch decision record

- Proposed domain:
- Brand/name clearance evidence:
- Initial target market(s):
- Publisher/legal identity:
- Production host and plan:
- Release commit:
- Source-check run:
- Browser QA evidence:
- Privacy/cookie review:
- Commercial disclosure review:
- Owner approval for purchase:
- Owner approval for deployment:
- Owner approval to enable indexing:
- Decision: `BLOCKED / APPROVED`
- Reviewer and date:
- Open risks:

## Current known blockers

- Brand/name clearance has not been established.
- The owner reports the domain was purchased, but registrar account, renewal settings, and DNS are not independently verified.
- Intended target markets are recorded as AU, US, FR, DE, CH, GB, and NL; market-specific legal and product checks remain outstanding.
- Publisher identity/contact and production privacy/cookie implementation need confirmation.
- No production browser QA has been recorded.
- Production hosting/deployment is not approved.
- Robots blocking must remain in place until the final indexing approval.
