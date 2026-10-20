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
- A public-only build now copies only approved site assets/pages into `dist/`; CI verifies internal research docs, CSV trackers, scripts, and host configuration are not included in that artifact.
- GitHub Actions passed on commit `f6468ffffd7b9bbe6988f12ab81add40efdc0d50` (run 39489204289), including source checks, a public-only build, deployment-artifact leak checks, and upload of the sanitized site artifact. The artifact was confirmed present with a 7-day retention window (expires 27 October 2026 UTC). The latest documentation-only commit `d1325e3f1be0c8f5432736225000fe96aeee55b0` also passed CI (run 39490025309). This is not live-browser or production verification.
- Added `docs/launch-acceptance-test-plan.md` and linked it from README. It explicitly remains NOT RUN until real browser/device and live-host testing is completed.
- The safer-gambling page now links official support resources for all seven intended markets and clarifies the limits of Australia's BetStop scheme. The market-research page now links primary regulators for each target market.

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
- A public-only deployment artifact is built into `dist/`, and CI checks that internal research docs, CSV trackers, scripts, and provider configuration are not published.
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


## Follow-up update — 20 October 2026, 20:44 UTC

This addendum supersedes the older CI commit/run references in the repository-work section above.

- Latest reviewed commit: `ab77110c70c653bb3df02ca0c8cca0fb5819de51` — `docs: add UKGC domain cross-check for new brand leads`.
- Latest GitHub Actions run: [39494517144](https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39494517144) — **completed successfully** on the latest commit.
- The public deployment-artifact checker includes a lightweight scan of text files in `dist/` for selected secret/token patterns and unresolved placeholder markers. It is a guardrail, not a dedicated secret scanner and not a substitute for manual review.
- The brand research notes now distinguish a verified GB licence/domain match from a verified launch date and from evidence of willingness to pay. In the current UKGC cross-check, Bet Ahoy has a declared active domain; Stakewise and Proper Bet still lack a matching declared domain in the register search and remain on hold pending official identity/domain evidence.
- No browser/device QA, live-host test, domain/DNS check, trademark clearance, privacy/legal approval, outreach, deployment, or indexing change has occurred.

**Decision remains BLOCKED.** The successful CI run verifies repository/build checks only. It does not clear any release blocker listed above.


## Owner decisions and privacy follow-up — 20 October 2026

- **Brand decision:** the owner has chosen to retain the name BeInCasinos for now because the domain was purchased. This is a recorded business preference, not trademark clearance; the name-review release gate remains open.
- **Publisher display identity:** Anass Amir, as specified by the owner. This does not by itself establish a legal business entity or satisfy every jurisdiction's publisher disclosure requirements.
- **Temporary public contact:** beincasinos@gmail.com, as explicitly selected by the owner. The mailbox has not been tested by this workflow; accessibility, account security and regular monitoring remain to be confirmed.
- The About, Contact and pre-launch Privacy pages now reflect the supplied publisher identity/contact. The Privacy page remains a draft and is not a claim of legal compliance.
- Added `docs/privacy-and-data-handling-review.md` based on official Moroccan CNDP guidance for websites and Law 09-08. It flags controller identity, data mapping, hosting locations, CNDP formalities and possible cross-border transfer requirements for review before relevant processing begins. Applicability must be confirmed against the actual setup; no filing or legal conclusion is claimed.
- The latest site-check run on the current contact-page commit is [39495222821](https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39495222821). HTML/local-link checks, public-only build and artifact-exclusion checks have passed; artifact upload is still running at the time of this update.

**Decision remains BLOCKED.** No deployment, DNS change, public indexing, paid hosting purchase, or brand outreach has been performed.
