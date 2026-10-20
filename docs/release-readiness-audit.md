# Release readiness audit — 20 October 2026

**Decision: BLOCKED — do not deploy, publish, or enable indexing yet.**

This is a source/repository review, not a live production audit. Repository files and CI runs were inspected on 20 October 2026. The domain registration, DNS, hosting account, live browser rendering, and legal position have not been independently verified.

## Confirmed project decisions

- Brand/project label: BeInCasinos.
- Intended domain: `beincasinos.online`. The owner reports that it was purchased through Spaceship; registrar access and status remain unverified here.
- Intended research markets: AU, US, FR, DE, CH, GB, NL.
- Language: English.
- Monetisation priority: paid listings first after audience evidence; affiliate links later and secondary.
- No paid hosting purchase, deployment, DNS change, outbound brand outreach, or indexing change has been performed.
- A read-only Vercel account check showed the connected team is on Hobby with no linked projects. A Netlify static-host configuration is prepared in the repository, but no Netlify account has been connected and no deployment has been made.
- `robots.txt` continues to block crawling.
- The sitemap now contains the intended domain rather than the former placeholder. This does not establish that the domain resolves or the sitemap is production-ready.

## Repository work confirmed

- Static educational website with homepage, guides, tools, policy pages, contact/about pages, 404 page, robots and sitemap.
- Wagering calculator and terms checklist tools.
- Source-level checker for HTML structure, local links, sitemap consistency, canonical/Open Graph/Twitter metadata, 404 noindex, static-host security headers, pre-launch guards, tracker schemas, and calculator-related safeguards.
- Internal docs for target markets, brand qualification, sales pipeline, listing-fee model, operator outreach, hosting, and launch checklist.
- A research queue with leads; this is not a verified list of 100 eligible brands and not a list of confirmed buyers.
- GitHub Actions passed on the latest checked commit `69fb45d399edb8b3c8c2c7b357a574096be58ca7` (run 39487750220). This is a source-level check, not live-browser or production verification.

## Release blockers — all must be evidenced, not assumed

### 1. Name and identity
- Obtain a proper trademark/name review for the “BEIN” element in intended markets, including the [WIPO Global Brand Database](https://www.wipo.int/en/web/global-brand-database/index) and Morocco's [OMPIC](https://www.ompic.ma/fr); get qualified advice if risk remains. WIPO notes that its database coverage depends on participating offices and recommends checking national/regional registers too.
- Decide whether to keep the brand/domain or change course after that review.
- Confirm publisher/legal identity and a monitored business contact. Do not assume an address mentioned on a purchase receipt is monitored or approved for public display.

### 2. Market/legal/product scope
- Do not market offshore online casino services as available in Australia or France; consult the market matrix and obtain legal review before any commercial placement.
- For the US, assess state-by-state and product-by-product; there is no single nationwide online-casino permission.
- For Germany, Switzerland, Great Britain, and the Netherlands, verify exact entity, domain, product permission, and current official regulator evidence.
- The research queue cannot be turned into public brand pages until each proposed claim is sourced and reviewed for its named market.

### 3. Brand qualification and revenue
- No brand is currently evidenced as willing to pay BeInCasinos a listing fee.
- A launch date, licence, affiliate programme, or partnership announcement does not establish willingness to buy a paid directory listing.
- Before selling, define package, price, duration, cancellation/refund/invoice terms, sponsorship label, and the exact benefits. Do not promise traffic or conversions without measured audience data.
- Keep paid placement visibly labelled and independent of verification/editorial conclusions.

### 4. Privacy, contact, and disclosures
- Replace the privacy pre-launch draft only after actual host, logs, analytics, cookies, affiliate tracking, and vendors are known.
- Establish a monitored corrections/privacy contact.
- Finalise affiliate and sponsored-content disclosures before any links or paid placements go live.
- Do not add tracking/analytics or third-party forms without reviewing consent and privacy requirements.

### 5. Technical readiness
- Canonical, Open Graph URL/title/description, and Twitter summary metadata have been added to all 18 public HTML pages using the intended origin. CI checks canonical and `og:url` consistency; the live host, redirects, and actual social-card rendering still need production checks.
- Verify the registrar, DNS, host, HTTPS, preferred host redirects, 404 handling, asset loading, and production sitemap after a host is chosen.
- Perform actual browser tests on desktop and mobile, keyboard-only testing, calculator edge cases, checklist print/reset/progress tests, and an accessibility review.
- CI source checks are useful but are not browser QA or a full accessibility audit.
- Choose hosting whose terms permit the planned commercial listing/affiliate activity; do not assume Vercel Hobby permits this business model.

## Safe launch sequence

1. Resolve name/brand decision and publisher identity.
2. Verify registrar access and renewal details; choose a commercially permitted host.
3. Complete legal/privacy/disclosure review for the first actual market and all content to be published.
4. Qualify individual brands with primary-source evidence; keep paid-buyer status unknown until direct evidence exists.
5. Complete metadata and run CI on the exact release commit.
6. Obtain owner approval for any paid plan and deployment.
7. Deploy with indexing blocked; run live DNS/HTTPS, browser, mobile, and accessibility checks.
8. Obtain separate explicit owner approval to remove the crawl block.
9. Verify the domain in Google Search Console, submit the final sitemap, and monitor indexing.
10. Keep dated evidence and schedule ongoing regulatory/content reviews.

## Current decision

**BLOCKED.** No external account changes or public launch actions have been made. The next release decision depends on evidence for the name, publisher/contact, host, privacy implementation, market scope, and live QA—not on the number of pages or research leads alone.
