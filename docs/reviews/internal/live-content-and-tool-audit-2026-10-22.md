# Live content, market hub and tools audit — 22 October 2026

**Scope:** Read-only live fetch of the homepage, review directory, methodology, market hub, wagering calculator, terms checklist, key guides, safer-gambling page and contact page. No workflow, deployment, DNS change, or Search Console submission was triggered.

## Results

### Strong points confirmed
- Homepage is crawlable, self-canonical, and links to the main educational guides, tools, review directory, policies and market research.
- Review directory clearly says no casino profiles are currently scored or ranked and explains the pass/fail eligibility gates before scoring.
- Methodology publishes the weighted 100-point rubric (terms 25, payments 20, safer gambling 20, complaints/support 15, operator/licence 10, usability/accessibility 10) and says hands-on tests must not be claimed unless performed.
- Market hub has ten jurisdictions and explicit restrictions: Australia and France are not presented as open online-casino markets; Canada is province-specific; Great Britain requires exact operator/domain/product matching.
- Wagering calculator explains its formula and limitations and does not present the result as a prediction.
- These are positive content/trust foundations, not proof of ranking, indexing, traffic, legal compliance or completed brand reviews.

### Release risks / gaps
1. **Tool behavior not fully tested in browser.** Text extraction confirms the wagering calculator and terms checklist pages load, but does not prove interactive calculations, keyboard operation, mobile layout, invalid-input handling, or screen-reader accessibility. Test these before calling the tools production-verified.
2. **Review methodology is a promise, not a completed database.** Do not label the site as having 100 reviews, active 90-day monitoring, or tested payout performance. No live profiles are scored/ranked.
3. **Time-sensitive market claims need dated official-source review.** The markets page states a specific Australian 2026 reform milestone. Recheck the official ACMA/parliament source and commencement date immediately before republishing that claim; do not infer that an enacted law is already in force.
4. **Internal-link crawl coverage is incomplete.** The homepage links to important routes and the sitemap lists 45 URLs, but a full automated status/canonical/orphan-page crawl has not been run. Do not claim zero broken links.
5. **Safer-gambling resource coverage is market-specific.** Before publishing a market page or review, verify locally relevant help and self-exclusion resources, age rules, product legality and advertising restrictions. Avoid generic global assurances.
6. **Commercial and privacy statements must match reality.** Affiliate disclosure and privacy notice say active affiliate tracking/paid placements are not currently enabled. Reconcile them before adding affiliate links, pixels, analytics, embedded third-party content or forms.
7. **The review directory's scoring rubric should not be mistaken for a ranking.** A numerical score is only valid after every eligibility gate and evidence review pass; missing criteria means withhold the total.

## Next work queue
- Run a no-deploy, no-build HTTP status/canonical crawl over all 45 sitemap URLs if a low-cost read-only browser/HTTP tool is available.
- Manually test both interactive tools for blank, zero, negative, non-numeric, and unusually large values; keyboard navigation; mobile viewport; and formula outputs.
- Recheck official market-regulator sources and date-sensitive legal claims, especially the Australian reform commencement statement.
- Complete one brand evidence pack at a time; hold until legal entity, exact domain, active product-specific licence, terms, payments, complaints, safer-gambling, privacy and enforcement checks are complete.
- Use Search Console for index status; public fetches and sitemap inclusion alone are not indexing evidence.
- Preserve Actions minutes: no CI run, build, deploy, cache purge, DNS update or public brand-profile publication was done in this audit.

## Status
- Live sitemap last observed: 45 URLs.
- Interactive tools: page fetchable; functional/browser accessibility tests not completed.
- Approved casino reviews: 0/100.
- Google indexation: not verified here.
- Deployment triggered: no.

## Sources checked
- https://beincasinos.online/
- https://beincasinos.online/reviews/
- https://beincasinos.online/how-we-review/
- https://beincasinos.online/markets/
- https://beincasinos.online/tools/wagering-calculator/
- https://beincasinos.online/tools/terms-checklist/
- https://beincasinos.online/guides/how-to-check-a-casino-licence/
- https://beincasinos.online/guides/how-to-complain-about-a-casino/
- https://beincasinos.online/responsible-gambling/
- https://beincasinos.online/contact/
