# BeInCasinos — project completion board

**Snapshot:** 20 October 2026  
**Release decision:** BLOCKED — do not deploy publicly or enable indexing.  
**Purpose:** One owner-facing list of work completed, outstanding evidence, and actions that require owner or third-party participation.

## Current verified repository state

- Static English-language site source exists, including homepage, guides, market research, safer-gambling information, editorial and commercial disclosure pages, privacy/contact drafts, 404, two learning tools, robots, sitemap, CSS and JavaScript.
- A public-only build script copies an allowlist into `dist/`; internal docs and trackers are intended to remain out of the public artifact.
- A source-level checker and GitHub Actions workflow exist. The latest observed workflow run for commit `b000bb85ebb0de62be45a7730f46ecc0ca5e5503` completed successfully: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39492866852. This validates only the checks in that workflow, not production hosting, browser rendering, legal compliance or accessibility.
- `robots.txt` currently blocks all crawlers as a temporary pre-launch measure.
- The legacy 100-name queue is a research backlog, not 100 verified brands. The new Tier 1 tracker is a first batch of 25 rows including 23 brand leads and two category-level market restrictions; it is not the final 100-brand qualification list.
- No brand has confirmed willingness to pay a BeInCasinos listing fee. No outreach was sent in this work.

## Gate board

| Gate | Status | Evidence needed to close |
|---|---|---|
| Brand/name risk | BLOCKED | Qualified trademark review of “BeInCasinos” / “BEIN” in relevant markets; decision recorded before public branding. |
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
