# BeInCasinos — project completion board

**Snapshot:** 20 October 2026  
**Release decision:** BLOCKED — do not deploy publicly or enable indexing.  
**Purpose:** One owner-facing list of work completed, outstanding evidence, and actions that require owner or third-party participation.

## Current verified repository state

- Static English-language site source exists, including homepage, guides, market research, safer-gambling information, editorial and commercial disclosure pages, privacy/contact drafts, 404, two learning tools, robots, sitemap, CSS and JavaScript.
- A public-only build script copies an allowlist into `dist/`; internal docs and trackers are intended to remain out of the public artifact.
- A source-level checker and GitHub Actions workflow exist. The latest verified source/build/artifact plus Chromium smoke run passed: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39501405509. It checked 21 HTML files (including the 404 page), syntax-checked shared JavaScript, built the public-only artifact, verified internal-file exclusion, and ran browser smoke tests over all 20 indexable routes, mobile/desktop overflow, mobile navigation, calculator edge cases, and both tools. The source-level checker reported 0 structural errors and 1 intentional warning because the privacy page remains a pre-launch draft. At the time of that older snapshot, the source check reported 9 warnings. On 20 October 2026, seven general guides/safer-gambling pages received a dated editorial source check and their on-page notices now state the review date and limits. The privacy page remains an explicit pre-launch draft; legal/privacy and live QA gates remain open. The internal pricing-hypothesis, UKGC audit, and media-kit evidence documents are planning aids, not launch approval or proof of audience/demand. This is not production hosting, browser rendering, legal compliance or accessibility sign-off.
- `robots.txt` currently blocks all crawlers as a temporary pre-launch measure.
- The legacy 100-name queue is a research backlog, not 100 verified brands. The Tier 1 tracker currently has 56 rows including 54 brand prospects and two category-level market restrictions; one UK lead (Ivy Casino) is excluded after the UKGC register spot-check showed it inactive. The 100-row generic research template is a candidate queue, not 100 fully verified operators or 100 willing paid-listing buyers. The tracker is not the final 100-brand qualification list. Seven Dutch regulated-operator prospects were added from the Ksa's 17 September 2026 continuation-licence announcement; those renewals are not evidence of new launches or willingness to buy.
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
| Hosting | OWNER DECISION | Confirm provider and its current terms for this commercial directory. Netlify Free is a private preview/staging candidate only because its 300-credit monthly limit can pause the site; the production tier must be selected after a realistic traffic/cost forecast. No account or deployment is connected. Do not use Vercel Hobby for the planned commercial business. |
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

## Latest brand and product work — 20 October 2026

- Owner's positioning is now documented in `docs/brand-identity-and-growth-north-star.md`: premium international casino reviews, BIC monogram, evidence-led editorial voice, and top-10 / 100-million-daily-impressions ambitions treated strictly as aspirations rather than current claims.
- The BIC monogram has been added to the site's primary navigation across public HTML pages and the favicon has been replaced with a matching evergreen/mint mark. Site source changes are committed and the combined source/build/artifact CI passed on run https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39497549965.
- Added `/reviews/` as a review-standard hub, connected it in the primary navigation and sitemap, included it in the public-only build allowlist, and updated the artifact checker to expect 19 sitemap URLs. The hub intentionally does not list unverified casinos as recommendations.
- Homepage positioning now leads with evidence-led casino reviews while keeping educational guides available. No individual casino profile is yet approved for publication; the 100-brand list remains an internal prospect/research queue, not a live verified review database.
- The 100-million daily search-impressions ambition is not a forecast or guarantee. Report only real, dated Search Console metrics after launch.

- Latest combined source/artifact verification passed on GitHub Actions: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39497037760. The check covered 20 HTML pages, built the public-only artifact, and verified the internal-file exclusion and sitemap. This remains source/packaging CI—not real-browser, legal, live-host, accessibility, or launch approval.

- Dated official-source review log added at `docs/editorial-source-review-log-2026-10-20.md`; seven general guides/safer-gambling pages now show a source-check date and retain caveats about current local rules. This is not legal sign-off.
- Added `docs/international-seo-content-architecture.md` with market gates, evidence standards, and SEO guardrails; it explicitly treats top-10 and 100-million daily impressions as ambitions, not forecasts.
- Homepage metadata and positioning now reflect the casino-review and research direction. The public `/reviews/` hub is in navigation and sitemap; individual operator reviews remain unpublished until each passes evidence gates.

- Latest source-check result after the seven editorial notice updates: **20 HTML pages checked, 0 structural errors, 1 warning** (the privacy page is intentionally marked pre-launch draft). See passing run https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39497391660. Artifact build and internal-file exclusion also passed. This is not legal review or live-browser QA.

- Added `docs/editorial-review-scoring-rubric.md` with pass/fail eligibility gates, a weighted 100-point evidence-based rubric, and rules that prohibit paid placement from influencing scores. The public How We Review page now explains the same methodology. This defines a process; it does not mean any casino has been scored or that a top-10 ranking exists yet.

- Public review-scoring methodology passed the source/build/artifact workflow on run https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39497604480. The latest internal profile-template documentation update is still being checked by CI; no deployment or indexing action was performed.
- Added public `/partners/` information page and linked it in the primary navigation across the public HTML pages. It states that paid partnerships are not open yet, discloses that audience data is not established, and prohibits paid influence on editorial scores. The page is included in the public-only build and sitemap; no operator outreach or paid listing sale has occurred.

- The public operator information page `/partners/` is now part of the navigation, public-only build, and sitemap (20 indexable URLs). It explicitly states that paid placements are not yet open and makes no audience-performance claims. Current CI run: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39498716612 (success).

- UK prospect research: ThreeSix Vegas now has an upgraded internal evidence record linking the UKGC active remote-casino licence, active trading-name record, active domain record, and operator site. It remains **Hold** pending full terms/withdrawal/complaints/regulatory-action review; paid-listing willingness remains unconfirmed. See `docs/ukgc-register-audit-2026-10.md` and the tracker. Source/build/artifact CI passed on https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39499260241.

- Added Bet Ahoy Ltd as a held UK prospect because the UKGC register shows active remote Casino permission from 17 December 2025. Exact consumer brand/domain and launch remain unverified, so the licence activity date is not counted as a brand launch and the prospect is not publishable yet.

- Tier 1 prospect research improved with official regulator evidence: BetTOM's active domain and remote-casino permission are matched; Betsuna's 22 May 2026 launch and white-label status are recorded alongside the UKGC's £1m ProgressPlay enforcement action; Swiss prospects admiral.ch and casineo.ch now have official ESBK online-start evidence. All remain on hold pending full editorial/legal review; no prospect has confirmed willingness to pay. See `docs/ukgc-register-audit-2026-10.md` and `docs/swiss-prospect-research-batch-2026.md`.

- Created `docs/brand-profile-casineo-ch-draft.md` from the Swiss regulator's official March 2026 approval/listing. The profile remains unscored and on hold because exact legal entity, terms, withdrawals, complaints, RG controls and enforcement review are incomplete; no commercial willingness is inferred.
- Created `docs/brand-profile-admiral-ch-draft.md` from the ESBK's official July 2025 online-start listing for Casino Mendrisio/admiral.ch. It remains unscored until the exact operating entity, terms, withdrawals, complaints, safer-gambling controls and regulatory history are checked.
- Added `docs/brand-profile-tipico-casino-de-sh-draft.md` and upgraded the internal Tipico prospect with the official 1 April 2026 launch announcement and GGL whitelist evidence. Its online-casino scope is limited to Schleswig-Holstein; full terms/withdrawal/RG/enforcement review remains outstanding and the profile is unscored.
- Added `docs/brand-profile-ember-casino-us-nj-draft.md` after matching the Ember Casino domain against the NJ DGE authorized-sites list and Delaware North's 4 June 2026 launch announcement. The profile remains unscored; it records the difference between the brand owner/group and the DGE-listed casino affiliate, and limits the scope to New Jersey.
- Added `docs/brand-profile-bettom-gb-draft.md` with the current UKGC licence/domain/trading-name match and dated launch announcement. It remains on hold for terms, withdrawal, complaints, safer-gambling and enforcement review; no score or paid-listing interest is claimed.
- Added held profile dossiers for ThreeSix Vegas and Betsuna. ThreeSix Vegas records a matched UKGC domain/licence but no verified consumer launch date; Betsuna records the 2026 launch claim, white-label domain status and material ProgressPlay enforcement history. Both remain unscored, and paid-listing willingness is unconfirmed.

- Latest source/build/artifact CI after the new profile dossiers passed: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39500484315. The run confirms source-level structure/link checks, shared JavaScript syntax, the public-only build, and exclusion of internal research files. The site still has one intentional privacy-draft warning; no live-host/browser/accessibility/legal test is implied.
- Internal held profile dossiers now exist for twenty-seven candidates: Casineo.ch, Admiral.ch, Tipico Casino (Schleswig-Holstein only), Ember Casino (New Jersey only), BetTOM, ThreeSix Vegas, Betsuna, Betinia (New Jersey only), Vegas Club Casino (New Jersey only), Winz.nl, Megaways Casino, BestOdds, Stakewise, 44Aces, Betcrown, BetLegend, BetNero, Casushi, FruitKings, 7Bet Casino, Justin Casino, LuckyMate Casino, Casiku, 247Bet, Midnite, Brillbet and Betty Casino. None is scored or approved for public publication; current terms, withdrawals, complaints, safer-gambling controls, exact legal/domain matches and regulatory histories remain to be completed as applicable.
- Added `docs/brand-profile-betinia-us-nj-draft.md` with the official NJ DGE authorized-site listing, the NJ Casino Control Commission's Q1 2026 skin-agreement report, and the operator's current rules page. The launch date remains unconfirmed by a primary source; profile is unscored and NJ-only.
- Added `docs/brand-profile-vegas-club-us-nj-draft.md` with the current NJ DGE authorized-site listing and state quarterly report. G2 Digital NJ and the Caesars/Boardwalk Regency license affiliate are kept distinct; public launch date remains secondary-source reported, and the profile is unscored/NJ-only.
- Added `docs/brand-profile-winz-nl-draft.md` after locating the official Ksa permit for Orange Gaming B.V. The dossier explicitly keeps Winz.nl on hold until the exact brand/domain notification is verified; a company permit alone is not treated as domain approval.

- Added a Chromium browser smoke suite to CI. It passed on https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39501405509, covering all 20 indexable routes, mobile overflow checks at 390px, desktop homepage overflow at 1440px, mobile menu/Escape behaviour, calculator valid/zero/negative/empty/over-limit inputs, checklist progress/reset, metadata parity, and uncaught page errors. Manual device/accessibility/production-host QA remains open.


- Automated QA was strengthened on 20 October 2026 with Chromium checks for declared page language, exactly one main landmark, skip-to-content links, accessible names for visible form controls and buttons. The enhanced suite passed on run https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39502557582. This is a lightweight smoke test only; WCAG conformance, keyboard/screen-reader review, contrast and real-device/manual testing remain open. See [launch acceptance test plan](launch-acceptance-test-plan.md).


- The expanded six-width responsive smoke suite passed on 20 October 2026: all 20 indexable routes were checked at 320, 375, 390, 768, 1024 and 1440px, alongside the accessibility smoke checks and interactive-tool checks. Run: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39502713824. Manual/device and live-host QA remain outstanding.


- The Chromium suite now fails on uncaught page errors and browser-console errors as well as structural, responsive, accessibility-smoke and interactive-tool checks. The full run passed on https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39502853616. This does not replace manual cross-browser/device, screen-reader, WCAG, legal/privacy or production-host QA.

- Added a baseline Content Security Policy to both prepared host configs and a CI validator (`scripts/check_host_config.py`) to prevent security-header drift. The validator, public-only build and expanded Chromium smoke tests passed on https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39503326238. Live deployed headers still require verification; current CSP permits inline scripts/styles and is not a strict nonce/hash-based policy.

- Added axe-core automated accessibility scans to the Chromium suite. The 20-route WCAG 2.1 A/AA-tag scan initially exposed low-contrast supporting text; the affected homepage/guide/footer colours were corrected. Passing run: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39504107580. Manual accessibility review remains required.

- Expanded the wagering-calculator browser tests to cover decimal values, empty/negative/over-limit multipliers, amount input limits, currency changes, and invalid-input state. The full source/build/security-config/artifact/Chromium/axe suite passed: https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39504606241. Manual production-host and real-device checks remain open.

- Hardened the prepared CSP further: both scripts and styles are now same-origin only (`script-src 'self'; style-src 'self'`); the two learning-tool scripts and styles are external files included by the public-only build, inline style attributes were replaced by classes, and source CI rejects inline scripts/styles. Full CI passed on https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39506143452. Live deployed response headers still need verification.

- UK prospect research batch added eight held leads (Brillbet, Betty Casino, Casushi, FruitKings, Betcrown, BetLegend, BetNero and 247Bet) to the Tier 1 tracker using UKGC licence/domain records where available. Several are white-label domains or have unresolved brand/operator matches; launch dates are secondary-source claims or remain unverified. All are Hold, and willingness to pay remains Unconfirmed. See `docs/tier-1-new-brand-research-seeds.md` and the tracker.

- Follow-up UKGC research added Casiku (White Hat Gaming white-label domain; launch timing is secondary-source only) and Midnite (UKGC search returns both Dribble Media Limited and Midnite Limited for the brand/domain, requiring operator-transition resolution). Both remain Hold; no willingness to pay is inferred.

- A second UKGC-backed research batch added eight more held leads (Stakewise, 44Aces, Casino and Friends, Peachy Games, Play Sunny, Neptune Play, PlayWins and BetFusion). Some are white-label domains or have unresolved current-operator/product scope; launch dates remain secondary-source claims or unverified. All are Hold and none has confirmed willingness to pay.

- A third UK research batch added five leads with active UKGC domain/licence evidence: Megaways Casino (official 24 March 2026 relaunch), BestOdds, LuckyMate Casino, 7Bet Casino and Justin Casino. Launch timing for four of these is secondary-source reported or needs confirmation; all remain Hold and willingness to pay is Unconfirmed.

- Added three internal GB dossiers (BestOdds, Stakewise and 44Aces) with current UKGC licence/domain evidence. Together with the Megaways Casino dossier, this brings the internal dossier set to 14; terms, withdrawals, complaints, safer-gambling controls, enforcement and commercial qualification remain incomplete, so none is approved for public publication.

- Hosting decision clarified: Netlify is the default technical production recommendation on a commercial-capable plan, conditional on owner budget approval and account connection; Netlify Free is preview/staging only, and Vercel Hobby is a no-go for the commercial model. No account, subscription, DNS or deployment action has been taken.
