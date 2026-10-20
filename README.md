# BeInCasinos

An English-language educational resource for understanding online casino terms, licensing, withdrawals, bonuses, and safer gambling.

## Stack
- Static HTML, CSS, and vanilla JavaScript
- No build step or runtime dependencies
- Prepared for static hosting once launch blockers and commercial-use terms are cleared
- Includes a client-side wagering calculator and a terms-review checklist; no user entries are sent to a server

## Local preview
Open `index.html` directly, or run `python -m http.server 8080` from the project root.

## Source-level quality check
Run `python3 scripts/check_site.py` from the repository root. The dependency-free checker scans HTML pages for missing titles/descriptions, unexpected H1 counts, duplicate page titles or IDs, missing image alt attributes, broken local navigation/resource references, and known launch placeholders. GitHub Actions runs this check on pushes and pull requests to `main`. The deployment-artifact check also scans the public-only `dist/` text assets for common accidental-secret patterns and obvious placeholders; this lightweight pattern check is not a dedicated secret scanner. These checks are guardrails—not a replacement for browser testing, accessibility review, checking external links, or legal/privacy review.

## Launch blockers — domain acquired, do not deploy yet
The owner has reported completing the `beincasinos.online` purchase through Spaceship. The sitemap now uses that domain, but this does **not** mean the brand name is legally cleared or the site is ready to launch.

1. **Resolve brand risk before public launch or further branding investment.** The name contains “BEIN”, which is an established mark associated with beIN Media Group. A WIPO domain-name decision describes beIN marks registered in Morocco and records a dispute over a domain incorporating BEIN. This does not by itself decide whether “BeInCasinos” infringes, but it makes a proper clearance review particularly important. Search WIPO and OMPIC records for the exact and similar marks in relevant classes and markets, and get qualified trademark advice if uncertain. References: https://www.wipo.int/amc/en/domains/decisions/text/2018/dma2018-0003.html and https://www.wipo.int/en/web/global-brand-database/index.
2. Confirm the domain is active in the registrar account, then add and test canonical/OG URLs after name clearance and before launch.
3. Verify every legal/regulatory statement against current primary sources for each target market.
4. Add the real publisher identity and a monitored contact address.
5. Update privacy/cookie wording to match the actual analytics, tracking, affiliate links, and vendors in use.
6. Review affiliate program rules, allowed geographies, marketing restrictions, and required disclosures.
7. Keep the temporary `robots.txt` disallow rule until the launch review is complete.
8. Confirm the chosen hosting plan permits commercial affiliate use. Vercel Hobby is restricted to personal/non-commercial use, and Vercel explicitly includes affiliate-link sites whose primary purpose is affiliate linking in its commercial-use examples. If Vercel remains the host, plan for Pro before commercial deployment; alternatively, choose a host whose current terms allow the intended business model.

## Hosting decision

A read-only check found the connected Vercel team is on Hobby with no linked projects; do not use that plan for the commercial site. `docs/hosting-decision.md` compares current options, and `netlify.toml` is prepared as a candidate configuration only. Before any deploy, `scripts/build_site.py` builds a public-only `dist/` artifact and CI checks that internal research docs, CSV trackers, scripts, and provider configs are excluded from that artifact. No host is connected and no deployment has been made.
- Do not deploy the monetized affiliate publication to Vercel Hobby. The official policy says Hobby is personal/non-commercial; see https://vercel.com/docs/limits/fair-use-guidelines#commercial-usage.
- No host has been selected or connected yet. Keep deployment paused until the commercial-use plan and recurring cost are approved. Do not add optional Spaceship trial products or enable auto-renewing add-ons unless intentionally needed; review recurring charges and renewal settings in the registrar account.

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

Use docs/audience-growth-measurement-plan.md for the six-month audience/measurement framework (a review plan, not a traffic or revenue forecast). See docs/listing-fee-business-model.md for the commercial plan and docs/paid-listing-pricing-validation.md for the internal, evidence-led pricing validation process, docs/brand-prospect-list.md for the initial 100-name research queue, docs/brand-research-template.csv for the row-by-row research tracker, and docs/paid-listing-sales-pipeline.csv plus docs/paid-listing-sales-pipeline.md for the internal sales workflow (use only after audience evidence and owner approval). The prospect list is not a recommendation or licensing verification. Use docs/brand-profile-template.md before publishing any profile and docs/paid-listing-media-kit-template.md only after real audience data exists. The draft for a future operator partnership page is internal only: docs/operator-partnership-page-draft.md. For release decisions, use docs/prelaunch-launch-checklist.md, the [current release-readiness audit](docs/release-readiness-audit.md), and the [manual launch acceptance test plan](docs/launch-acceptance-test-plan.md); the acceptance plan is intentionally marked NOT RUN until real browser/device and live-host tests are performed. See the [hosting decision note](docs/hosting-decision.md) before choosing a provider; for carefully verified first-contact outreach after audience evidence exists, use docs/brand-outreach-email-template.md.

## Content policy
No invented ratings, bonus offers, licensing claims, or claims of independent testing. Any future commercial recommendation must be verified, dated, market-specific, and clearly disclosed.

## Domain and hosting setup

See [the domain and hosting setup runbook](docs/domain-and-hosting-setup.md) for the ordered steps after the owner-reported Spaceship purchase. Do not add trial products, change nameservers, publish DNS records, deploy, or enable indexing until the relevant decision and launch gates are complete.

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

- [Tier 1 master prospect tracker (CSV)](docs/tier-1-master-prospect-tracker.csv) — consolidated first batch with market/product scope, evidence grade, exact next actions, and explicit publication holds. It is not yet a 100-qualified-brand list; unresolved fields are intentionally marked VERIFY/Unknown.

**Publication gate:** verify the exact domain, legal operator, licence/product scope, target-market permission, regulatory history, and relevant advertising/affiliate rules against current primary sources. Keep commercial willingness-to-pay marked **Unknown** until directly evidenced. Do not copy these internal research notes into the public site or sitemap.
