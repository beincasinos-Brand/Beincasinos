# BeInCasinos brand-review evidence gate v1

**Purpose:** consistent quality control for the 100-brand research target. This is an internal editorial checklist, not a public ranking or a claim that any brand has passed.

## Non-negotiable evidence gates

A brand is not “verified” solely because its name appears in a list or a regulator search returns a licence. Record the exact market, domain, legal contracting entity, licence/account identifier, authorised remote activities, domain status, evidence date and primary-source links.

### Gate A — identity and authorisation
- [ ] Exact consumer domain captured from the live site.
- [ ] Current legal footer/terms name the contracting entity for the relevant product.
- [ ] Exact domain matched to the regulator's public register.
- [ ] Correct legal entity's licence status and authorised product type confirmed.
- [ ] Related group companies and sister brands kept separate.
- [ ] Domain redirects, inactive domains and white-label arrangements recorded.
- [ ] All regulator claims dated; re-check immediately before publication.

### Gate B — regulatory history and fairness
- [ ] Search the verified entity's enforcement/actions page.
- [ ] Search official regulator announcements for historical actions not obvious on the current register view.
- [ ] Record dates, findings, financial penalties, warnings, remediation and mitigating context accurately.
- [ ] Never turn “no actions currently listed” into “never had enforcement”.
- [ ] Never infer current product quality from licence status alone or infer current misconduct solely from historic findings.

### Gate C — live product terms
- [ ] Current general terms and product-specific terms captured with date.
- [ ] Promotions archived separately with eligibility, qualifying activity, wagering, max stake, game contribution, expiry and withdrawal restrictions.
- [ ] Payment methods, limits, fees, processing stages, verification and withdrawal rules checked from current official pages.
- [ ] Complaints procedure, escalation route and applicable ADR provider verified.
- [ ] Responsible-gambling controls documented from official pages and, where possible, usability tested without real-money gambling.

### Gate D — independent review quality
- [ ] Dated mobile and desktop observations recorded.
- [ ] Independent feedback sample method, date range, sample size and limitations documented.
- [ ] Anecdotes distinguished from independently verified outcomes.
- [ ] Each factual statement has a source or is labelled as an observation.
- [ ] Score rationale is transparent, reproducible and not based on brand familiarity.
- [ ] Second editor verifies identity, sources, calculations, claims and scoring.

## Status labels

- **Prospect:** brand name found; identity not yet established.
- **Identity matched:** domain, legal entity and regulator record aligned.
- **Research in progress:** some evidence gates remain open.
- **Editorial review:** all substantive gates evidenced; awaiting independent review.
- **Approved review:** second review completed; publication owner explicitly approved.
- **Hold / exclude:** material identity mismatch, missing evidence or other unresolved publication risk.

## Counting rule

Only **Approved review** counts toward the target of 100 completed high-quality reviews. Prospects, drafts, licence-only profiles, untested brand pages and files with open evidence gates must not be counted. Maintain separate totals for prospects, identity-matched candidates, dossiers in progress, editorial reviews and approved reviews.

## Low-CI-budget operating rule

- Do not trigger deployments or GitHub Actions solely to update internal research documents.
- Prefer small, traceable commits to the default branch when authorised.
- Before creating a file, check whether it already exists; update it rather than creating duplicate drafts.
- Avoid workflow-file changes and large automated batches while Actions minutes are constrained.
- Do not claim indexing, rankings, traffic or impressions without direct measurements from the relevant analytics/search-console source.
- Keep a checkpoint after each research batch with commit hashes, file links, open blockers and exact counts.
