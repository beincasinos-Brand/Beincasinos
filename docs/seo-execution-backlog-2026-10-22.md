# BeInCasinos SEO execution backlog — crawlable pages before scale

**Updated:** 22 October 2026  
**Status:** internal implementation backlog; not a claim of ranking or indexing.  
**Release rule:** this plan does not authorise production deployment. Public pages should only be added after their factual, legal, editorial and technical checks pass.

## Objective

Grow useful, discoverable coverage without manufacturing thin pages, misleading casino rankings, or implying legal availability where a product is not permitted. The 100-brand target is a research target, not permission to publish 100 incomplete profiles.

## Workstream A — technical baseline

Complete on a single release candidate before production:
- [ ] Run the configured static-site build from a clean checkout and save the full log.
- [ ] Check all internal links in built HTML; fail on broken local links, empty anchors, placeholder hrefs and accidental links to internal research docs.
- [ ] Parse generated sitemap as XML; require HTTP URLs on the canonical apex host, unique URLs, no redirecting URLs, no 404/5xx URLs, and no noindex pages.
- [ ] Confirm each indexable HTML page has one descriptive title, one meta description, a canonical URL, a single primary H1, language declaration, viewport, and useful visible text.
- [ ] Verify robots.txt is valid plain text and declares the actual sitemap URL.
- [ ] Check www-to-apex, HTTP-to-HTTPS, trailing-slash policy, unknown-path 404, and query-string canonical behaviour.
- [ ] Check JSON-LD parses and matches visible content; never add ratings/reviews/aggregateRating unless there are genuine published reviews and substantiation.
- [ ] Inspect mobile viewport, keyboard focus, heading order, contrast, accessible names, cookie controls, privacy/affiliate notices, and safer-gambling footer.
- [ ] Confirm build output contains no internal evidence packs, unpublished drafts, tokens, environment values, or credentials.
- [ ] Capture before/after URL inventory and deployment commit so the release is auditable.

## Workstream B — build topic clusters in useful order

Publish a hub only when it has a distinct audience purpose and enough substantive, verified content to be useful.

1. **Trust and methodology:** how reviews are researched; evidence standards; correction policy; affiliate disclosure; responsible gambling; complaints and contact.
2. **Market legality hubs:** one per target market with regulator links, licence/product distinctions, last-checked date, and explicit restrictions. Avoid claiming the whole country has a single uniform licence where regulation is regional.
3. **Product explainers:** slots/RTP/volatility, roulette variants, blackjack rules, baccarat, craps, live dealer, poker, bingo and lottery. Explain rules and odds accurately; do not imply a game guarantees profit.
4. **Payment and account guides:** deposits, withdrawals, KYC, fees, payment-method availability and dispute escalation. Distinguish operator claims from independently observed testing.
5. **Vertical hubs:** sports betting, horse racing, bingo, lottery, poker, land-based venues, social/sweepstakes products and B2B game studios each get separate legal scope and separate review standards. Do not mix them into an “online casino” ranking.
6. **Brand reviews:** only after exact local permission, legal entity/domain match, current terms, payments, bonuses, RG, privacy, support, enforcement and independent second review are evidenced.

## Workstream C — market gates

| Market | Publication rule |
|---|---|
| Australia | No “legal online casinos in Australia” list. Prioritise legal restrictions and consumer protection; treat other permitted gambling verticals separately. |
| Canada | Name the province/territory on every relevant hub and profile. Ontario approval is not nationwide authorisation. |
| Great Britain | Match exact domain and casino permission in the current UKGC register; betting permission alone is not casino permission. |
| Switzerland | Match platform to ESBK/FGB online-casino list and confirm specific game permissions. |
| France | No legal online-casino recommendations. If covering legal online poker/betting, label those verticals accurately and separately. |
| Italy | Match exact domain, concessionaire and casino-game scope to current ADM records. |
| Germany | Distinguish GGL-authorised virtual slots/poker from state-authorised table games and state scope. |
| Austria | Do not infer Austrian authorisation from an EU or foreign licence; require current local legal sign-off. |
| Netherlands | Match exact domain, entity, active Ksa permit and product scope. |
| Sweden | Match exact domain/entity and licence validity in the current Spelinspektionen register. |

## Workstream D — editorial acceptance criteria

A page is not ready because it contains a brand name or long word count. Before it is indexable:
- Its main intent is clear and not a near-duplicate of another market page.
- It answers the reader's decision question with specific, current, sourced facts.
- Material claims have dated primary sources and uncertainty is stated.
- No unperformed deposit, withdrawal, account, support or gameplay test is described as completed.
- Promotional terms include key limitations and are not presented as guaranteed value.
- Commercial links are disclosed and do not determine editorial score.
- Responsible-gambling support and local complaint routes are visible.
- An editor who did not compile the evidence reviews the finished page.
- A last-reviewed date reflects an actual review, not a template date.
- Pages with unresolved legal or material factual gaps remain HOLD and are excluded from public navigation and sitemap.

## Workstream E — search measurement

Use Search Console and server/build evidence as separate signals:
- Crawlability: HTTP status, canonical, robots, sitemap membership and internal links.
- Indexing: Search Console URL Inspection / Pages report; a sitemap submission is not proof of indexation.
- Performance: impressions, clicks, CTR and average position by query/page/country, assessed over meaningful time windows.
- Quality: helpfulness, source freshness, original observations, corrections and reader task completion.
- Business: affiliate clicks and conversion only where legally allowed, consented, disclosed and measured responsibly.

Do not promise a traffic target or infer indexation from a successful fetch. Avoid repeated URL submissions as a ranking tactic; fix the underlying content and technical issue instead.

## Next concrete batch

1. Establish a reproducible local/CI build and crawl check.
2. Fix any build or sitemap/link errors revealed by that check.
3. Create genuinely useful market/legal hubs with current official citations.
4. Complete one brand evidence pack end-to-end, including independent review, before scaling the template.
5. Update the verification ledger only with evidence and actual sign-off.
6. Run release QA, obtain explicit owner approval, then deploy one tested release.

**Current gate:** approved brand reviews remain 0/100 until the ledger and evidence records say otherwise. This document itself does not change that count.
