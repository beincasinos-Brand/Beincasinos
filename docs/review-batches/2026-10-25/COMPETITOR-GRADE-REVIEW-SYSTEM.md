# BeInCasinos — competitor-grade review system
**Internal editorial specification | 25 October 2026 | Do not publish this document as a consumer review**

This specification translates common competitor review patterns into an evidence-first workflow. Casino.org describes a multi-step review process covering security/licensing, games and promotions; Casinos.org describes fixed-weight scores and real withdrawal testing. BeInCasinos must not claim to have performed tests it has not actually performed.

## 1. One brand, one evidence record, market-specific eligibility
Create one global brand identity record and separate market eligibility records. Do not count country-specific duplicates as separate unique brands. Never carry a licence, bonus, payment method, operator entity or domain from one market into another without evidence.

For each market record:
- brand and exact URL/domain
- legal operator and company number if available
- regulator, licence/reference, product scope, status and date checked
- first-party terms URL and capture date
- bonus URL, offer end date and full material terms
- payments/withdrawals URL, limits, fees and processing claims
- support and complaint routes; ADR or regulator escalation
- safer-gambling, self-exclusion, privacy and security links
- enforcement/complaint research with source dates
- image asset URL/source, licence/permission and alt text
- reviewer, second reviewer, evidence confidence and change log

## 2. Score model — 100 points
Only calculate a score after the legal eligibility gate passes and minimum evidence is present. Mark incomplete records **HOLD — NOT RATED**. If the product is not legally eligible for the target market, mark **EXCLUDE**, not a low numeric score.

| Dimension | Weight | What evidence must support the score |
|---|---:|---|
| Legal eligibility and operator transparency | 25 | Live regulator register, exact operator/domain, product scope, terms and corporate disclosures |
| Bonus clarity and fairness | 15 | Wagering basis, contribution, expiry, max bet, excluded games, withdrawal caps and eligibility |
| Payments and withdrawals transparency | 15 | Methods, limits, fees, stated processing, KYC; label practical tests separately |
| Player protection | 15 | Limits, time-outs, self-exclusion, reality checks, help and account closure |
| Games and fairness evidence | 10 | Current catalogue, named providers, RNG/certification evidence where verifiable |
| Support and complaints | 10 | Channels, hours, complaint route, ADR and verified complaint/enforcement evidence |
| Usability and accessibility | 5 | Mobile layout, accessibility and navigation; say desk research if not hands-on |
| Privacy and security transparency | 5 | HTTPS, privacy notice, data controller, account/security information |

Score each dimension 0–10 with a short rationale and source. Weighted points = dimension score / 10 × dimension weight. Overall is the sum, out of 100. Show category points and review date; never display a score without its basis.

### Confidence labels
- **High:** current primary records captured, all critical fields verified and independently checked.
- **Medium:** core legal/terms evidence captured but a non-critical field remains uncertain; disclose the limitation.
- **Low / Hold:** critical information is missing, stale or contradictory. Do not publish a numeric score.
- **Excluded:** the target product fails the market eligibility gate.

A public star rating is only a visual conversion of the same overall score, not a separate judgment. Do not imply user-review stars or hands-on testing where neither exists.

## 3. Bonus facts — mandatory field list
Never copy a headline bonus alone. Record:
- exact amount/percentage/spins and currency
- minimum deposit and qualifying method
- wagering multiple and whether applied to deposit, bonus or both
- eligible games and contribution rates
- expiry window and any activation code
- maximum bet while wagering
- max cashout/withdrawal restrictions
- excluded payment methods, countries, account types and games
- offer end date, source URL, capture date and reviewer
If not verified, display “Current offer not verified” on internal workbench; never use a guessed value in public schema or snippets.

## 4. Required consumer-review structure
1. Unique title, meta description and single H1, naming the target market.
2. Short verdict with review date and confidence.
3. At-a-glance facts: operator, market eligibility, licence source, bonus status, payment disclosure status.
4. Pros and cons with evidence, not generic claims.
5. Licensing and operator identity.
6. Bonus terms explained in plain language.
7. Deposits, withdrawals, fees, limits and KYC.
8. Slots, live casino, table games, jackpots and providers only where confirmed.
9. Mobile and usability; distinguish observed facts from testing.
10. Customer support, complaints and dispute escalation.
11. Safer gambling and self-exclusion.
12. Privacy/security, affiliate disclosure and conflicts policy.
13. FAQ based on genuine user intent, answered with verified facts.
14. Primary sources, checked date, correction route and reviewer/editor sign-off.

Write original prose. Do not spin the same generic article across 100 domains. Add a meaningful market-specific explanation and factual comparison for each page.

## 5. SEO and technical release gate
- Unique title/meta/H1; useful canonical URL; descriptive URL slug.
- Relevant internal links from market hub and related category pages.
- Sitemap inclusion only after approval; drafts stay noindex.
- Structured data must match visible content and applicable search guidelines; never invent ratings or review counts.
- Optimize original or properly licensed images: descriptive filename, useful alt text, responsive sizes and compressed files.
- Avoid doorway pages, mass-produced near-duplicates, false urgency, “guaranteed wins,” unsupported “best/safest” claims and keyword stuffing.
- Add transparent affiliate disclosure near commercial links; commissions cannot influence score.
- Check mobile layout, keyboard accessibility, broken links, page speed, canonical/index directives and source links before release.

## 6. Image policy
For each image, record source, owner, licence or written permission, allowed uses, retrieval date and attribution requirement. Prefer original brand-provided media only when terms permit the intended use, licensed stock, or original editorial graphics. Do not scrape competitor screenshots/logos, remove watermarks, or hotlink images. Alt text should describe the image's function, not stuff keywords. If rights cannot be confirmed, do not publish it.

## 7. Competitor-grade quality assurance
Before a review is approved:
- exact domain and operator independently matched to regulator/official source
- all bonus and payment claims have dated first-party citations
- no test is claimed without a logged test record
- no blank required sections or placeholder text
- score recalculated from rubric and rationale
- sources and links opened and checked
- image rights confirmed
- affiliate disclosure and safer-gambling notice present
- second editor signs off; changes to scores are logged
- target market and legal constraints reviewed
- title, canonical, index directive and internal links checked

## 8. Honest counting
Track separate counts for unique candidate brands, verified operators, market eligibility passes, complete evidence dossiers, complete draft reviews, independently approved reviews and published/indexable reviews. Only an independently approved review counts toward the 100-review goal. A profile, a duplicated market page, a research dossier or an empty template does not count.
