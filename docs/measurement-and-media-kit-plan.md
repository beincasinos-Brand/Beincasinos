# Measurement and media-kit plan — internal, pre-launch

**Status:** Planning only. No analytics or tracking is currently approved by this document. Do not enable a vendor, cookie, pixel, affiliate identifier, or audience-sharing integration until the owner and qualified privacy reviewer approve the actual data flow and notices.

## Purpose

Measure whether the public site is useful and whether any future advertising inventory can be described truthfully. Measurement is not permission to promote gambling products in a restricted market. Do not collect player-level gambling behaviour or build profiles of vulnerable people.

## Stage 0 — no measurement before launch approval

Until the site is live and the privacy review is complete:
- Record audience metrics as **Not measured**.
- Do not invent sessions, unique users, impressions, clicks, countries, conversions, or revenue.
- Keep robots.txt blocked and do not submit the sitemap.
- Do not add third-party analytics scripts, advertising pixels, affiliate tracking, fingerprinting, or non-essential cookies.
- A source-code configuration or a vendor account does not prove that tracking is lawful or correctly deployed.

## Stage 1 — minimum technical baseline

After launch and explicit approval, choose the minimum set of metrics needed. Prefer aggregate, first-party or provider-native reporting where it can meet the purpose without unnecessary identifiers. Have the privacy reviewer assess provider location, controller/processor roles, retention, international transfers, cookies/local storage, opt-out, and data-subject request handling before activation.

Suggested aggregate measures:
- Search performance: clicks, impressions, click-through rate and average position, with reporting period and property scope.
- Content usefulness: page views or visits, top landing pages, device category and broad country grouping only where lawfully available.
- Technical health: canonical URLs indexed, crawl errors, broken routes, page response status and security-header checks.
- Commercial readiness: number of evidence-approved inventory pages and their actual reportable delivery.
- Partner pipeline: verified contacts, replies, qualified interest, proposals, signed agreements, invoices and paid invoices as separate counts.

Avoid collecting exact location, cross-site browsing histories, player identifiers, sensitive inferred traits, or individual gambling activity. Do not share visitor-level data with operators.

## Stage 2 — reporting definitions

Every report must state:
- Start/end date and timezone.
- Data source and access date.
- Whether a measure counts events, page views, sessions, users, clicks or impressions.
- Known bot filtering, consent limitations, sampling, attribution windows and reporting delays.
- Market and page scope, including whether the metric is available only in an aggregate report.
- Any material changes to tracking, consent, URLs, or measurement methodology.

Do not combine incompatible measures or compare different time windows without explaining limitations. Search Console impressions are not unique people; clicks are not conversions; operator-reported conversions are not independently verified revenue unless reconciled against the contract and source.

## Stage 3 — media kit evidence table

Populate only from real, dated source exports. Leave all unavailable values as “Not measured”.

| Field | Required evidence |
|---|---|
| Reporting period | Exact dates and timezone |
| Domain/property | Verified property and canonical host |
| Organic search clicks/impressions | Dated Search Console export; define scope |
| Visits/page views | Approved analytics report and measurement definition |
| Top content | Report export plus the date range |
| Country/device mix | Aggregate report only, subject to privacy approval |
| Engagement | Defined metric, methodology and known limitations |
| Inventory | Exact live page/placement, format, label, market and term |
| Delivery report | Real impressions/clicks for the contracted period, if lawfully measured |
| Audience claims | No extrapolated reach, guaranteed outcomes, or unsupported audience profile |
| Commercial proof | Only signed/paid deals that can be disclosed with permission; never imply an operator relationship before agreement |

## Stage 4 — paid inventory go/no-go

Do not sell inventory until all are true:
1. The public site is live and passes live-host and manual accessibility checks.
2. At least one specific market/product scope has passed qualified legal review.
3. The publisher identity, business contact, privacy notice and correction/removal process are confirmed.
4. The inventory is live, useful, clearly labelled, and independent of editorial scoring.
5. A dated baseline exists and is sufficient to describe actual performance without exaggeration.
6. The buyer's exact operator/domain/product is verified for that market.
7. Contract, price, tax, cancellation, reporting and link attributes are approved.
8. The owner authorises the offer and the relevant outreach channel is compliant.

If any item is missing, keep the package in research-only status.

## Monthly owner report

- Site/search: actual values + source + period.
- Content quality: stale pages, corrections, broken links and review dates.
- Compliance: approved market scope, holds, source rechecks and changes.
- Privacy/security: requests, incidents, retention/deletion actions and unresolved vendor issues.
- Commercial funnel: researched, contact verified, contacted, replied, qualified, proposal, signed, invoiced and paid — each a separate count.
- Inventory: live placements, disclosure checks, expiry dates, delivery and removals.
- Open risks: owner, next action, due date and evidence needed.

**Hard rule:** “Not measured” is a valid answer. A missing number must never be replaced with an estimate presented as fact.
