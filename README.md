# BeInCasinos

**Latest confirmed integrated verification (21 October 2026, 13:33 UTC):** The integrated GitHub Actions workflow passed on commit `9ca6bdb3f8842a444db2ed807eb5181edb855350`, including HTML/local-link checks, paid-listing pipeline gates and regression tests, JavaScript syntax, Cloudflare header validation, public-only artifact and sitemap checks, and Chromium browser smoke tests across the 28 indexable routes: https://github.com/beincasinos-Brand/BeIncasinos/actions/runs/39608954109. This validates source/build behaviour only; it does not establish live-host behaviour, legal/privacy compliance, domain/mailbox control, buyer demand, or launch approval. Later SEO planning documents are awaiting their own CI runs.

An English-language, evidence-led casino reviews and research brand focused on operator identity, market-specific licensing, terms, withdrawals, and safer gambling. Individual reviews must pass the internal evidence and publication gate before they can go live.

**Official website:** [BeInCasinos.online](https://beincasinos.online/) — public-facing casino research and review hub. Use the live site for published material; this repository contains development notes and internal research that may not be publication-ready.

## Brand and editorial direction
- Public brand: BeInCasinos; compact monogram: BIC.
- Positioning, visual identity, review evidence standard, and growth ambitions: `docs/brand-identity-and-growth-north-star.md`.
- Competitive benchmark and differentiation roadmap for Casino.org and leading review publishers: `docs/competitive-review-publishers-benchmark-2026-10-21.md`.
- International review-page architecture, SEO guardrails, and market gates: `docs/international-seo-content-architecture.md`.
- SEO growth plan toward the 1,000,000-daily-impression ambition: `docs/seo-growth-plan-1m-daily-impressions.md`; staged measurement and launch gates, not a forecast.
- Search Console, sitemap, canonical-host and indexing verification checklist: `docs/search-discovery-indexing-verification-2026-10-22.md`; production fetches do not establish Google indexing or traffic.
- SEO topic map: `docs/seo-topic-map.csv`; planned topics are research ideas, not keyword-volume claims or permission to publish market-specific legal content.
- Evidence-gated scoring, eligibility rules, and ranking independence: `docs/editorial-review-scoring-rubric.md`.
- Current UK and Swiss primary-source prospect audits: `docs/ukgc-register-audit-2026-10.md` and `docs/swiss-prospect-research-batch-2026.md`.
- Held profile dossiers (not public reviews): `docs/brand-profile-casineo-ch-draft.md`, `docs/brand-profile-admiral-ch-draft.md`, `docs/brand-profile-tipico-casino-de-sh-draft.md`, `docs/brand-profile-ember-casino-us-nj-draft.md`, `docs/brand-profile-bettom-gb-draft.md`, `docs/brand-profile-threesix-vegas-gb-draft.md`, `docs/brand-profile-betsuna-gb-draft.md`, `docs/brand-profile-betinia-us-nj-draft.md`, `docs/brand-profile-vegas-club-us-nj-draft.md`, and `docs/brand-profile-winz-nl-draft.md`.
- Public operator listing information and commercial-independence policy: `/partners/` (not accepting paid placements yet).
- Owner-facing release gates and evidence record: `docs/owner-final-gates-and-launch-evidence.md`.
- Consolidated owner action pack for the final launch sequence: `docs/owner-action-pack-final-launch.md`; it separates prepared work from decisions/evidence that require owner, legal, registrar, or hosting access.
- Fillable launch evidence register (CSV): `docs/launch-evidence-register-template.csv`; keep private account evidence outside the repository.
- Current launch evidence status (CSV): `docs/launch-evidence-register-current-status-2026-10-21.csv`; records source/CI passes separately from unverified owner, legal, hosting, live-QA, and indexing gates. Do not store credentials or private account evidence here.
- Primary-source Tier 1 market compliance gate for AU, US, FR, DE, CH, GB and NL: `docs/tier-1-market-compliance-gate-2026-10-21.md` (internal screening only; does not clear any market).
- Internal fixed-fee, CPA, revenue-share, hybrid, qualification, and outreach playbook: `docs/commercial-partnership-operating-playbook.md`.
- Step-by-step, evidence-gated prospect outreach pipeline and commercial-model controls: `docs/commercial-outreach-pipeline.md`; preparation only, no outreach authorised or sent.
- Public review-standard hub: `/reviews/`. It deliberately does not present unverified operators as recommendations.
- The owner's north-star ambition is 100,000,000 daily Google Search impressions. This is an extreme long-term goal only—not a current metric, forecast, or guaranteed result. Track actual impressions, clicks, CTR, average position, queries, pages, country and device in Search Console; do not treat published URLs or indexed-page counts as impressions.

## Stack
- Static HTML, CSS, and vanilla JavaScript
- No runtime dependencies; CI assembles a public-only deployment artifact through an allowlist build
- Prepared for static hosting once launch blockers and commercial-use terms are cleared
- Includes a client-side wagering calculator and a terms-review checklist; no user entries are sent to a server

## Internal commercial planning
- Paid-listing offer framework and pricing hypotheses: `docs/paid-listing-offer-framework.md`. This is an internal research draft, not a public rate card; pricing and demand remain unvalidated.
- Operator prospect qualification scorecard: `docs/operator-prospect-qualification-scorecard.md`. This keeps legal/evidence gates separate from research priority and unconfirmed commercial demand.
- Media-kit evidence template: `docs/media-kit-evidence-template.md`. Fill only from real, dated reports; no audience metrics are asserted until measured.
- Measurement and media-kit plan: `docs/measurement-and-media-kit-plan.md`. Privacy-first reporting stages; no tracking or audience claims are enabled by this plan.
- Paid-placement order-form checklist: `docs/paid-placement-order-form-internal-draft.md`. Internal counsel-review draft only; not a contract or offer.

## Local preview
Open `index.html` directly, or run `python -m http.server 8080` from the project root.

## Source-level quality check
Run `python3 scripts/check_site.py` from the repository root. The dependency-free checker scans HTML pages for missing titles/descriptions, unexpected H1 counts, duplicate page titles or IDs, missing image alt attributes, broken local navigation/resource references, and known launch placeholders. GitHub Actions runs this check on pushes and pull requests to `main`. The deployment-artifact check also scans the public-only `dist/` text assets for common accidental-secret patterns and obvious placeholders; this lightweight pattern check is not a dedicated secret scanner. GitHub Actions validates the Vercel build settings, redirect, and security headers, builds the public-only artifact, verifies internal-file exclusion, and runs Chromium smoke tests against all 28 indexable routes at six viewport widths. The browser suite checks metadata, mobile navigation, the wagering calculator and terms checklist, runtime/console errors, structural accessibility and axe-core WCAG 2.1 A/AA-tag rules. The axe scan caught colour-contrast failures which were fixed; the integrated 23-route suite passed on https://github.com/beincasinos-Brand/Beincasinos/actions/runs/39583259274. These automated tests are guardrails—not a WCAG conformance claim or replacement for manual browser/device and screen-reader testing, external-link checks, live-host checks, or legal/privacy review.

## Launch blockers — domain acquired, do not deploy yet
The owner has reported completing the `beincasinos.online` purchase through Spaceship. The sitemap now uses that domain, but this does **not** mean the brand name is legally cleared or the site is ready to launch.

1. **Owner decision: retain the BeInCasinos name for now.** The owner has chosen to keep the brand after purchasing the domain. This is a project decision, not trademark clearance. **Resolve brand risk before public launch or further branding investment.** The name contains “BEIN”, which is an established mark associated with beIN Media Group. A WIPO domain-name decision describes beIN marks registered in Morocco and records a dispute over a domain incorporating BEIN. This does not by itself decide whether “BeInCasinos” infringes, but it makes a proper clearance review particularly important. Search WIPO and OMPIC records for the exact and similar marks in relevant classes and markets, and get qualified trademark advice if uncertain. References: https://www.wipo.int/amc/en/domains/decisions/text/2018/dma2018-0003.html and https://www.wipo.int/en/web/global-brand-database/index.
2. Confirm the domain is active in the registrar account, then add and test canonical/OG URLs after name clearance and before launch.
3. Verify every legal/regulatory statement against current primary sources for each target market.
4. The owner has specified the publisher display identity as **Anass Amir** and the temporary contact email as **beincasinos@gmail.com**. Verify that the mailbox is accessible and monitored, and determine whether additional legal publisher details are required before launch.
5. Update privacy/cookie wording to match the actual analytics, tracking, affiliate links, and vendors in use.
6. Review affiliate program rules, allowed geographies, marketing restrictions, and required disclosures.
7. Keep the temporary `robots.txt` disallow rule until the launch review is complete.
8. Cloudflare Pages Free is the preferred first host for the static site, pending preview validation. Do not deploy the commercial site to the connected Vercel Hobby team; that plan is not suitable for the planned affiliate/paid-listing business. See `docs/hosting-decision.md` for Cloudflare setup, security headers, DNS and redirect gates.

## Hosting decision

Cloudflare Pages Free is the preferred initial host to avoid a recurring hosting subscription for the static site, subject to preview acceptance. `scripts/build_site.py` builds a public-only `dist/` artifact and now copies `cloudflare/_headers` into `dist/_headers`; CI validates the Cloudflare security-header rules and artifact inclusion. The `www` to apex redirect still needs a Cloudflare host-aware Redirect Rule and live verification. The Vercel team remains on Hobby with no linked project; no Cloudflare project is connected and no deployment has been made. See `docs/hosting-decision.md` and the [final deployment runbook](docs/final-deploy-runbook.md).
- Do not deploy the monetized affiliate publication to Vercel Hobby. The official policy says Hobby is personal/non-commercial; see https://vercel.com/docs/limits/fair-use-guidelines#commercial-usage.
- Vercel has been selected but no project has been created or connected. Keep deployment paused until commercial-use plan terms and recurring costs are reviewed. Do not add optional Spaceship trial products or enable auto-renewing add-ons unless intentionally needed; review recurring charges and renewal settings in the registrar account.

## Quality checks
- Check every new page for a unique title/description, one clear H1, mobile layout, keyboard operation, and working internal links.
- Tools run in the browser only. The shared stylesheet uses system fonts and makes no third-party font request. Do not add analytics, cookies, affiliate tracking, remote fonts, or third-party scripts without updating the privacy notice and checking applicable consent requirements.
- The terms checklist is a personal review aid, not legal advice or a substitute for regulator records or the operator’s full terms.

## Target markets and regulatory research

BeInCasinos targets **Tier 1 audiences only** in AU, US, FR, DE, CH, GB, and NL. Tier 1 is an informal marketing classification, not a legal category. Every operator and product must be reviewed against each market's current official sources; US checks must be state- and product-specific. France and Australia require particular care for online-casino promotions. Use [docs/target-market-regulatory-matrix.md](docs/target-market-regulatory-matrix.md) as an internal source guide and [docs/tier-1-market-strategy.md](docs/tier-1-market-strategy.md) for the Tier-1-only strategy and editorial gates. Neither document is legal advice or publication approval. Keep profiles unpublished when market permission or affiliate/advertising rules are unresolved.

## Business model and directory strategy

The intended commercial sequence is **audience first, paid listings second, affiliate revenue later**. Do not present listing fees as available or charge brands until the site has measurable traffic and a documented media kit. The initial research target is 100 casino brands, but a brand is not publishable merely because its name is on a prospect list.

### Staged plan
1. **Before public launch:** resolve the BEIN trademark/name risk and choose the initial target market(s). The owner reports the domain purchase is complete, but a purchase does not clear the name legally.
2. **Build the 100-brand prospect list:** record the brand, exact operating/legal entity, official website, regulator/register evidence, permitted territories, source URLs, date checked, contact route, and research status. Unknown fields stay marked unknown; never infer licence status.
3. **Publish verified profiles only:** each profile needs unique useful content, market-specific caveats, clear update dates, official source links, and an editorial review. Avoid 100 thin or near-duplicate pages. Keep unverified prospects out of the public sitemap.
4. **First six months:** focus on genuinely useful guides, tools, technical SEO, indexation, and audience measurement. No promise of traffic or revenue; use the first six months as a review period, not a guarantee.
5. **Paid listings after evidence of audience:** prepare a transparent media kit from real Search Console/analytics data. Clearly label paid placements as sponsored/paid listings; payment must not buy a licence claim, safety verdict, editorial rating, or undisclosed ranking advantage.
6. **Affiliate links later and secondary:** only add after the listing model and disclosure workflow are ready. Verify each affiliate program's rules, allowed markets, tracking, and legal requirements. Clearly disclose affiliate links near them and update the privacy notice for any tracking.

### Minimum profile review fields
- Brand name and official domain checked against the brand's own site.
- Legal operating entity and regulator record independently checked where applicable.
- Exact jurisdiction/product scope and whether the audience market is permitted.
- Terms/withdrawal/complaints information and official source links.
- Last checked date, reviewer, evidence notes, unresolved questions.
- Commercial relationship: none / paid listing / affiliate / both, disclosed on the profile.

Use [docs/tier-1-new-brand-research-seeds.md](docs/tier-1-new-brand-research-seeds.md) as a **secondary-source discovery list only** for possible GB brands launched/rebranded in 2022–2026. Each candidate still needs primary-source launch evidence, an exact-domain UKGC check, and a commercial contact/signal review; no candidate is confirmed to want a paid listing.

Use [docs/brand-partner-qualification.md](docs/brand-partner-qualification.md) for the partner-ready 100-brand qualification scorecard, new-brand (2022–2026) evidence rules, and the distinction between prospects and confirmed willing buyers. The research CSV has separate launch-year, launch-source, partnership-signal, listing-fit, and decision-maker-source columns; blank values mean unknown, not assumed.

Use docs/audience-growth-measurement-plan.md for the six-month audience/measurement framework (a review plan, not a traffic or revenue forecast). See docs/listing-fee-business-model.md for the commercial plan and docs/paid-listing-pricing-validation.md for the internal, evidence-led pricing validation process, docs/brand-prospect-list.md for the initial 100-name research queue, docs/brand-research-template.csv for the row-by-row research tracker, and docs/paid-listing-sales-pipeline.csv plus docs/paid-listing-sales-pipeline.md for the internal sales workflow (use only after audience evidence and owner approval). The prospect list is not a recommendation or licensing verification. Use docs/brand-profile-template.md before publishing any profile and docs/paid-listing-media-kit-template.md only after real audience data exists. The draft for a future operator partnership page is internal only: docs/operator-partnership-page-draft.md. For release decisions, use docs/prelaunch-launch-checklist.md, the [current release-readiness audit](docs/release-readiness-audit.md), and the [manual launch acceptance test plan](docs/launch-acceptance-test-plan.md); the acceptance plan is intentionally marked NOT RUN until real browser/device and live-host tests are performed. See the [hosting decision note](docs/hosting-decision.md) for Vercel setup and plan gates; for carefully verified first-contact outreach after audience evidence exists, use docs/brand-outreach-email-template.md.

## Content policy
No invented ratings, bonus offers, licensing claims, or claims of independent testing. Any future commercial recommendation must be verified, dated, market-specific, and clearly disclosed.

## Domain and hosting setup

See [the domain and hosting setup runbook](docs/domain-and-hosting-setup.md) for the ordered steps after the owner-reported Spaceship purchase. The [final deployment runbook](docs/final-deploy-runbook.md) consolidates the last release gates and the preview-to-public sequence. Do not add trial products, change nameservers, publish DNS records, deploy, or enable indexing until the relevant decision and launch gates are complete.

## Commercial outreach

See [the internal operator outreach playbook](docs/operator-outreach-playbook.md). It is a gated template only; it must not be sent before the stated legal, privacy, audience and owner-approval checks pass.


- [Project completion board](docs/project-completion-board.md) — single status page for release blockers, owner actions, evidence gates, and the next work sequence.

## Recent prospect-research updates (internal only)

These are research notes and candidate queues, not public listings, legal advice, or evidence that any brand will pay a listing fee.

- [UK prospect research batch (2025–2026)](docs/uk-prospect-research-batch-2025-2026.md) — secondary-source discovery leads requiring exact-domain and UKGC verification.
- [Netherlands prospect research batch (2025–2026)](docs/netherlands-prospect-research-batch-2025-2026.md) — Ksa domain/brand checks and launch-versus-rebrand distinctions.
- [Tier 1 market research update (20 October 2026)](docs/tier-1-market-research-update-2026-10.md) — primary-source leads and market-specific guardrails for Switzerland, Germany, the US, and Australia.
- [Commercial prospect qualification rubric](docs/commercial-prospect-qualification.md) — evidence grades and qualification rules.
- [Commercial outreach pipeline](docs/commercial-outreach-pipeline.md) — internal workflow and email templates; no outreach is sent automatically.
- [Brand prospect leads (2025–2026)](docs/brand-prospect-leads-2025-2026.md) — research queue, not approved public copy.

- [Tier 1 master prospect tracker (CSV)](docs/tier-1-master-prospect-tracker.csv) — consolidated first batch with market/product scope, evidence grade, exact next actions, and explicit publication holds. The separate paid-listing sales pipeline now has 100 research candidates, all held at `hold` / `not_contacted`; this is not a 100-qualified-brand or buyer list. Unresolved fields are intentionally marked VERIFY/Unknown.
- [Megaways Casino — internal GB profile dossier](docs/brand-profile-megaways-casino-gb-draft.md) — official 2026 relaunch announcement and UKGC domain match recorded; terms, withdrawals, complaints and safer-gambling review remain incomplete, so no score or public profile is approved.
- [BestOdds — internal GB profile dossier](docs/brand-profile-bestodds-gb-draft.md), [Stakewise — internal GB profile dossier](docs/brand-profile-stakewise-gb-draft.md), and [44Aces — internal GB profile dossier](docs/brand-profile-44aces-gb-draft.md) — UKGC licence/domain matches documented; terms, withdrawals, complaints, safer-gambling and enforcement reviews remain incomplete, so all stay on Hold.
- Additional held internal profiles: [Betcrown](docs/brand-profile-betcrown-gb-draft.md), [BetLegend](docs/brand-profile-betlegend-gb-draft.md), [BetNero](docs/brand-profile-betnero-gb-draft.md), [Casushi](docs/brand-profile-casushi-gb-draft.md) and [FruitKings](docs/brand-profile-fruitkings-gb-draft.md). White-label and operator-identity caveats are explicit; none is scored or approved for publication.
- Further held internal profiles: [7Bet Casino](docs/brand-profile-7bet-gb-draft.md), [Justin Casino](docs/brand-profile-justin-casino-gb-draft.md), and [LuckyMate Casino](docs/brand-profile-luckymate-gb-draft.md) — current UKGC domain/licence evidence is recorded; launch timing remains secondary-source reported, and terms/withdrawals/complaints review is still open.
- Further internal drafts: [Casiku](docs/brand-profile-casiku-gb-draft.md), [247Bet](docs/brand-profile-247bet-gb-draft.md), and [Midnite](docs/brand-profile-midnite-gb-draft.md). All remain on Hold pending operator, launch, terms and consumer-protection checks.
- Recent launch leads on hold: [Brillbet](docs/brand-profile-brillbet-gb-draft.md) and [Betty Casino](docs/brand-profile-betty-casino-gb-draft.md). UKGC records are linked, but launch timing is secondary-source reported and consumer-term review remains incomplete.

**Publication gate:** verify the exact domain, legal operator, licence/product scope, target-market permission, regulatory history, and relevant advertising/affiliate rules against current primary sources. Keep commercial willingness-to-pay marked **Unknown** until directly evidenced. Do not copy these internal research notes into the public site or sitemap.


## Publisher and privacy decisions

- The owner has chosen to retain the BeInCasinos name for now; this is not trademark clearance.
- Publisher display identity supplied by the owner: **Anass Amir**.
- Temporary contact email selected by the owner: **beincasinos@gmail.com**; mailbox access and monitoring must be tested before public launch.
- Privacy/data-handling review: [docs/privacy-and-data-handling-review.md](docs/privacy-and-data-handling-review.md). This remains an open release gate, including review of Moroccan CNDP Law 09-08 requirements and any cross-border data-transfer formalities applicable to the actual setup.


## Operator qualification scorecard

- [Internal operator qualification scorecard](docs/operator-qualification-scorecard.md) — hard legal/identity/privacy gates, weighted evidence checklist, evidence-record template, decision outcomes, and recheck cadence. Internal only; it does not certify any operator or establish willingness to pay.
