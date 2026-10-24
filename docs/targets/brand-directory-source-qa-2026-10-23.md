# Brand directory source QA — 24 October 2026

**Branch checked:** `ops/2026-10-24-target-reconciliation-and-release-gates`  
**Source checked:** `brand-directory/index.html` and `brand-directory/directory.js`  
**Scope:** static-source audit only. This is not a browser/accessibility test, regulator re-verification, image-rights clearance, legal sign-off or proof that Cloudflare serves the latest commit.

## Current measured state

| Check | Result |
|---|---:|
| Brand cards | 100 |
| Unique card headings | 100 |
| Visible research snapshots | 100/100 |
| Market labels | 7 represented markets |
| Legal-operator / concession-recipient field | 99/100 |
| Official-domain field | 99/100 |
| Regulator/authority field | 100/100 |
| Evidence-grade field | 100/100 |
| Verification checklist | 100/100 |
| Research-context panel | 100/100 |
| Sourced image candidates | 50/100 |
| Candidate images with alt text | 50/50 |
| Candidate images with explicit width/height | 50/50 |
| Candidate images with lazy loading | 50/50 |
| Candidate images with error fallback | 50/50 |
| Visible rights-pending labels | 50 |
| Rows in image asset register | 100 |
| Rows with a sourced candidate in the register | 50 |
| Duplicate HTML IDs | 0 (latest source scan) |
| New-tab links missing `noopener noreferrer` | 0 (latest source scan) |

## Market and status distribution

| Market | Cards |
|---|---:|
| Great Britain (GB) | 65 |
| Netherlands (NL) | 18 |
| New Jersey (US-NJ) | 7 |
| Pennsylvania (US-PA) | 4 |
| Switzerland (CH) | 2 |
| Germany, state-specific (DE) | 2 |
| Michigan (US-MI) | 2 |
| **Total** | **100** |

All 100 visible cards are currently marked **HOLD**. Evidence grades are A: 19, B: 6, C: 52, and UNKNOWN: 23. These are source-evidence grades, not casino quality scores. The directory is intentionally marked `noindex,follow` and excluded from the sitemap while the queue is unapproved.

## Findings and risks

- Fifty cards display an official-site image candidate; all 50 are labelled **SOURCE FOUND · RIGHTS PENDING**. Finding an image on an official site does not establish permission to reuse it. Fifty other cards use CSS artwork/monograms rather than brand logos or photographs.
- The image tags have alt text, width/height, lazy loading, and a fallback to text if a remote logo fails. They still depend on third-party image hosts; this audit does not establish uptime, rights, privacy effects, or mobile rendering.
- Legal-operator and official-domain fields are populated on 99/100 cards, but a populated field is not a verified current customer-contracting entity or product-specific permission.
- The market set includes US state-specific cards. No US-wide authorisation is implied; Pennsylvania, New Jersey and Michigan require independent regulator/domain/contract checks.
- France and Australia remain outside the 100-card directory scope; their filter options are retained for audit context only.
- The source HTML is included in the current branch build allowlist and would be publicly reachable if deployed; noindex is not access control. A separate read-only production fetch on 24 October 2026 found that the live `/brand-directory/` route returns 404, so the source QA below must not be described as a live production feature check. Its content identifies the entries as an unapproved research queue and does not present them as consumer recommendations.

## Release gates

1. Verify each current brand/domain/legal-entity/product relationship in the applicable regulator's primary source.
2. Capture dated current terms, bonus rules, deposit/withdrawal methods and restrictions, complaints/support, safer-gambling controls, privacy/cookies, and accessibility.
3. Clear image reuse rights or replace the candidate with approved assets/original artwork before treating it as a production asset.
4. Complete independent review and editorial/legal approval before publishing consumer scores or recommendations.
5. Run the full static and browser test suite on an actual CI runner. Current PR #141 checks are failing before runner allocation (runner ID 0, zero steps); this is unresolved and no passing CI result is claimed.
6. Do not merge or deploy production without explicit approval and completion of the 100-review publication gates.

**Decision:** source structure is consistently labelled as research, not recommendations. The 100 cards are not 100 approved reviews; approved review count remains **0/100**.
