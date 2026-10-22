# BeInCasinos one-shot release checklist

**Purpose:** prepare one controlled release after the current verification sprint. This document is an internal runbook; it does not certify that production is ready.

## Hard stop: no deploy until all gates pass

- [ ] All planned 100-brand records have a named canonical domain, legal entity, current primary-regulator source, licence/product scope, and explicit target-market status.
- [ ] Any unresolved identity, licence, territory, or domain conflict stays on HOLD and is not represented as approved.
- [ ] Public brand profiles contain original market-specific analysis, dated sources, clear commercial/affiliate disclosure, complaint/support and safer-gambling information, limitations, and a corrections route.
- [ ] No unperformed testing is described as hands-on experience. No unsupported score, bonus claim, withdrawal-speed promise, or “EU-licensed” blanket claim.
- [ ] The review hub links only to real, complete public pages; internal drafts and research ledgers remain private.
- [ ] Canonicals, page titles/descriptions, internal links, mobile layout, keyboard navigation, and 404/redirect behavior are checked.
- [ ] Sitemap lists only canonical public URLs returning successful responses. Do not add internal documents or draft URLs.
- [ ] `robots.txt` allows intended public pages and points to the canonical sitemap; verify robots, sitemap, and canonical host on production.
- [ ] Privacy, terms, affiliate disclosure, editorial policy, about/contact and responsible-gambling pages are reachable and consistent.
- [ ] Existing static-site checks pass on the exact intended release commit; verify that internal-only files are excluded from the generated public artifact.
- [ ] Save the exact release commit SHA, build run, artifact identifier and checksum, sitemap URL count, route smoke-test result, and rollback target.
- [ ] Obtain explicit owner approval before production deploy. A successful preview or CI check alone is not production approval.

## Low-quota execution plan

1. Do content and source review locally/in the branch first; avoid repeated Actions runs for copy-only changes.
2. Run the existing static-site checks once on the final combined candidate, only after the hard gates above are satisfied.
3. Inspect the actual generated artifact, not only the workflow's green status. Confirm draft/ledger exclusion and sitemap contents.
4. If the artifact is wrong or the check fails, fix the issue before any production release; do not repeatedly trigger builds without a specific correction.
5. Deploy once after approval, then run a small post-deploy smoke test on the home page, review hub, key guides, sitemap, robots file and canonical redirect.
6. Verify the public URLs and Search Console reports after release. A crawl request is not a guarantee of indexing, ranking, traffic or impressions.

## Current known blockers

- The ten owner-supplied partner brands have internal drafts and a structured registry, but remain HOLD pending exact domain, target-country and primary-regulator verification.
- Current sprint tracker records 22 internal drafts, 0 publication-ready reviews and 0/100 approved brands.
- Cloudflare API access previously returned an authentication error. Do not claim DNS, redirect or deployment settings were repaired unless a fresh live check confirms it.
- The owner reported GitHub Actions minutes were around 90% consumed. Preserve the remaining budget and avoid unnecessary workflows.
- No production deploy or Google indexing result is claimed by this runbook.
