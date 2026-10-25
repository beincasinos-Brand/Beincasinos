# BeInCasinos review card specification

**Purpose:** consistent reusable schema for casino review cards and full review pages. This is an editorial specification, not production UI code and not a claim that candidate reviews are approved.

## Required card fields
- `brand_name`: canonical brand name.
- `market_code`: one of AU, CA, GB, US, CH, DE, NL, SE, ES, IT, FR, BE.
- `jurisdiction_scope`: precise country/province/state; never imply country-wide approval where permissions are regional.
- `operator_legal_name`: exact legal entity from current official record.
- `official_domain`: exact domain confirmed against regulator and operator terms.
- `eligibility_status`: APPROVED / HOLD / EXCLUDE; include checked date and evidence URL.
- `score_total`: null until the approved evidence-based rubric is completed.
- `score_breakdown`: every dimension score, weight, evidence pointer, limitations and reviewer.
- `confidence`: HIGH / MEDIUM / LOW based on evidence freshness and coverage; no confidence badge without rules.
- `bonus`: null unless a current offer and binding terms have been archived.
- `payments_summary`: documented methods, limits, fees and stated times; separate published claims from measured outcomes.
- `reviewed_at` and `last_verified_at`: actual dates, never generated dates.
- `pros`, `cons`: each item backed by a specific source or dated test note.
- `image_asset`: original/licensed image path, rights owner, permission, attribution, alt text and retrieval date.
- `affiliate_disclosure`: visible text/link adjacent to commercial links.
- `reviewer`, `editor`, `sources`, `limitations`: all required for approval.

## Visual hierarchy
1. Brand/title and market-specific eligibility status.
2. Score and confidence shown only after approval; clicking the score opens its evidence-backed breakdown.
3. Bonus card only for a currently verified offer, with key terms and last-checked date.
4. Quick facts: operator, regulator, payment terms and review date.
5. Evidence-led pros/cons.
6. Sections for licence, bonus terms, payments, games/software, support, player protection, privacy and complaints.
7. FAQ with sourced answers; affiliate disclosure and responsible-gambling note visible.

## Rating model
Use the approved shared 100-point rubric consistently:
- Operator identity and legal eligibility: 25%
- Bonus fairness and terms transparency: 15%
- Payments and withdrawal transparency: 15%
- Player protection: 15%
- Games and fairness disclosures: 10%
- Support and complaints: 10%
- Usability and accessibility: 5%
- Privacy and security: 5%

A failed market-eligibility gate means EXCLUDE from that market's promotion, regardless of arithmetic. Missing critical evidence means HOLD / NOT RATED. A numeric score must not be reverse-engineered to fit a visual design. Do not claim real-money withdrawal testing unless a dated test record exists.

## SEO and structured data
- One useful, unique title/H1/meta description per approved page.
- Exact market scope, operator and legal status in visible copy; avoid generic templated copy.
- Canonical and sitemap entry only after final publication approval.
- Structured data must mirror visible facts. Never invent aggregate ratings, review counts, offers, prices or licence properties.
- Noindex drafts and pages that fail evidence/legal gates.
- Use descriptive alt text and responsive compressed images. Do not hotlink competitor images.
- Add sources, review date, affiliate disclosure, corrections route and safer-gambling information.
- Test mobile rendering, accessible keyboard navigation, contrast, internal links and page performance.

## Release checklist
- [ ] Legal register matched to exact entity/domain/product.
- [ ] Current terms and offer archived with date.
- [ ] Payment terms and testing limits documented.
- [ ] Every material claim has a source/test note.
- [ ] Score calculated from rubric and independently checked.
- [ ] Images are original or rights-cleared.
- [ ] SEO, canonical, schema, links, accessibility and mobile QA pass.
- [ ] Affiliate disclosure and safer-gambling info visible.
- [ ] Reviewer and second editor approve.
- [ ] Only then mark APPROVED and include in sitemap.
