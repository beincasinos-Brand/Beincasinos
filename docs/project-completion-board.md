# BeInCasinos — project completion board

**Snapshot:** 20 October 2026  
**Release decision:** BLOCKED — do not deploy publicly or enable indexing.  
**Purpose:** One owner-facing list of work completed, outstanding evidence, and actions that require owner or third-party participation.

## Current verified repository state

- Static English-language site source exists, including homepage, guides, market research, safer-gambling information, editorial and commercial disclosure pages, privacy/contact drafts, 404, two learning tools, robots, sitemap, CSS and JavaScript.
- A public-only build script copies an allowlist into `dist/`; internal docs and trackers are intended to remain out of the public artifact.
- A source-level checker and GitHub Actions workflow exist. The latest verified run passed: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39494123987. It checked 19 HTML pages, built the public-only artifact, and verified internal files were excluded. The source check still reports 9 warnings: seven guides/safer-gambling pages need final primary-source review, and privacy/contact remain explicit pre-launch drafts. The internal pricing-hypothesis, UKGC audit, and media-kit evidence documents are planning aids, not launch approval or proof of audience/demand. This is not production hosting, browser rendering, legal compliance or accessibility sign-off.
- `robots.txt` currently blocks all crawlers as a temporary pre-launch measure.
- The legacy 100-name queue is a research backlog, not 100 verified brands. The Tier 1 tracker currently has 32 rows including 30 brand prospects and two category-level market restrictions; one UK lead (Ivy Casino) is excluded after the UKGC register spot-check showed it inactive. The tracker is not the final 100-brand qualification list. Seven Dutch regulated-operator prospects were added from the Ksa's 17 September 2026 continuation-licence announcement; those renewals are not evidence of new launches or willingness to buy.
- No brand has confirmed willingness to pay a BeInCasinos listing fee. No outreach was sent in this work.
- An internal [paid-listing offer framework](paid-listing-offer-framework.md) now defines tentative test-price hypotheses, disclosure rules, reporting boundaries, and the readiness gates for any future sales test. Prices are unvalidated hypotheses; no rate card was published and no outreach was sent.
- A dated [UKGC register spot-check audit](ukgc-register-audit-2026-10.md) documents operator permission vs. brand launch/domain proof, including Bet Ahoy, BetLegend, BetTOM, and the inactive Ivy Casino trading-name entry. These remain research leads/holds, not qualified paid buyers.
- An internal [media-kit evidence template](media-kit-evidence-template.md) now requires dated, source-backed audience metrics and explicitly prohibits invented traffic figures; it is a template, not a completed media kit.

## Gate board

| Gate | Status | Evidence needed to close |
|---|---|---|
| Brand/name risk | BLOCKED | Complete the [name-clearance workpaper](name-clearance-research.md) and obtain a qualified trademark review of “BeInCasinos” / “BEIN” in relevant markets; decision recorded before public branding. |
| Domain control | OWNER ACTION | Owner verifies active registration, renewal, auto-renew and DNS access in Spaceship. No credentials or account screenshots should be shared here. |
| Publisher identity | OWNER ACTION | Legal publisher/business identity and a monitored contact route. |
| Hosting | OWNER DECISION | Confirm provider and its current terms for this commercial directory. Netlify Free is a candidate to evaluate; no account or deployment is connected. Do not use Vercel Hobby for the planned commercial business. |
| Market/legal scope | IN PROGRESS | Select initial launch markets and obtain appropriate review of gambling listings, paid placement, affiliate/advertising rules, privacy and consumer protection. AU and FR online-casino promotions must not be treated as ordinary eligible markets. US casino products need state-specific verification. ACMA reports Australian gambling reforms passed on 19 August 2026, with a range of measures expected to commence 1 January 2027; re-check detailed commencement and guidance before any AU activity. |
| Prospect qualification | IN PROGRESS | Expand the master tracker; verify exact domain, legal operator, regulator record, product scope, enforcement history, source dates and commercial contact for every candidate. |
| Paid-listing demand | NOT VALIDATED | Direct operator response, rate-card/media-kit evidence, signed agreement or payment. Launches, affiliate programmes and supplier deals alone are not evidence of willingness to pay. |
| Privacy/contact/disclosures | BLOCKED | Finalise notices to match actual hosting, logs, contact method, analytics, cookies and any tracking; publish real publisher contact and a correction/privacy request process. |
| Source checks | CI PASS, SCOPE LIMITED | Keep CI green after each change. It does not replace manual browser/device, screen-reader, legal, or live-host checks. |
| Live acceptance testing | NOT RUN | Complete the manual test plan against the selected live host and retain evidence for each test. |
| Search indexing | BLOCKED | Only after the owner’s separate launch approval: remove the pre-launch crawl block, verify canonical host/HTTPS, inspect URLs and submit sitemap. |

## Next work sequence

1. Expand and qualify the Tier 1 master tracker; keep unknown evidence blank or explicitly marked `VERIFY`.
2. Reconcile the legacy 100-name queue with the selected markets, excluding unsuitable categories and removing duplicates.
3. Prepare a source-backed, per-brand evidence packet before drafting any public operator profile.
4. Finalise the commercial offer and media kit only after real audience data exists; do not invent traffic, conversion, pricing acceptance or testimonials.
5. Resolve name, identity, domain and hosting gates with the owner.
6. Run source checks, build the public-only artifact, inspect it for internal-file leakage and placeholders, then complete manual production acceptance testing.
7. Launch and enable indexing only after documented approval.

## Do not do without owner approval

- Buy a subscription, start a paid trial, or incur any cost.
- Change nameservers/DNS or email records.
- Deploy the site, expose the internal research files, remove the crawl block, or submit Search Console.
- Send commercial outreach, sign agreements, or represent any brand as a paying partner.
- Publish a legal/licensing claim that has not been verified against the current official register.

## Project references

- [README](../README.md)
- [Tier 1 master prospect tracker](tier-1-master-prospect-tracker.csv)
- [Target-market regulatory matrix](target-market-regulatory-matrix.md)
- [Commercial prospect qualification rubric](commercial-prospect-qualification.md)
- [Commercial outreach pipeline](commercial-outreach-pipeline.md)
- [Hosting decision note](hosting-decision.md)
- [Domain and hosting runbook](domain-and-hosting-setup.md)
- [Pre-launch checklist](prelaunch-launch-checklist.md)
- [Release-readiness audit](release-readiness-audit.md)
- [Manual launch acceptance test plan](launch-acceptance-test-plan.md)
