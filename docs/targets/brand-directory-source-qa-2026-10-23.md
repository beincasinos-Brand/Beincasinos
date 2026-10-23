# 100-brand directory source QA — 23 October 2026

**Branch:** `ops/tier1-10-market-100-brand-roadmap-2026-10-22`  
**File checked:** `brand-directory/index.html`  
**Purpose:** Static source audit only. This is not a live-browser test, regulator re-verification, image-rights clearance, legal sign-off, or proof of Cloudflare deployment.

## Latest measured state

| Check | Result |
|---|---:|
| Brand cards | 100 |
| Unique brand labels | 100 |
| Visible research snapshots | 100/100 |
| Legal-operator field populated | 46/100 |
| Official-domain field populated | 48/100 |
| Regulator/authority field | 100/100 |
| Evidence-grade field | 100/100 |
| Verification checklist | 100/100 |
| Research-context panel | 100/100 |
| Sourced image candidates | 45/100 |
| Candidate images with alt text | 45/45 |
| Candidate images with explicit width/height | 45/45 |
| Candidate images with lazy loading | 45/45 |
| Candidate images with error fallback | 45/45 |
| Visible rights-pending labels | 45 |
| Rows in image asset register | 100 |
| Rows with a sourced candidate | 45 |
| Duplicate HTML IDs | 0 |
| New-tab links missing `noopener noreferrer` | 0 |

## Interpretation and gaps

- 45 cards have a sourced image candidate. All 45 remain **SOURCE FOUND · RIGHTS PENDING**; the asset register does not establish permission to republish.
- 55 cards use original CSS artwork and monograms, not official brand logos or photographs.
- A populated official-domain field does not mean that the exact brand/domain is approved for the named jurisdiction. TOTO and Kansino retain explicit Ksa brand/domain and casino-scope caveats.
- The legal-operator field is populated on 46 cards. Some values are reported permit holders whose exact brand/domain match remains pending; they are not legal sign-off.
- Evidence-grade distribution: A 44, B 7, C 49. These are evidence grades, not quality scores. Current status distribution is 99 HOLD and 1 EXCLUDE.
- Market split: CH 2, DE 2, NL 18, GB 66, US-NJ 7, US-MI 2, US-PA 3. US entries are state-specific; no nationwide authorisation is implied.
- Fanatics has an image candidate from the official Fanatics Sports & Casino homepage, but its exact New Jersey authorized-product/domain mapping remains unconfirmed.
- Official-site fetch failures were not worked around by guessing asset URLs: 247Bet returned `content_too_large`, Tipico returned HTTP 403, Casino and Friends was bot-blocked, BigBangBet returned an invalid URL, and Neptune Play redirected to a blocked-country page.

## Publication and deployment gates

- The directory remains `noindex,follow` and excluded from the sitemap while brand-level legal scope, source evidence, image rights and editorial sign-off remain incomplete.
- These 100 cards are a research queue, not 100 approved consumer reviews. **Review approval remains 0/100.**
- PR #36 is open, draft, unmerged and currently not mergeable.
- No GitHub Actions run was triggered for this work. No Cloudflare production deployment is confirmed.
- Before publication, verify exact local domain/operator/casino authorisation, current terms, payments and withdrawals, complaints/enforcement scope, safer-gambling information, image reuse rights and independent editorial sign-off.

## Note on earlier counts

Earlier sections and commits record historical snapshots from before the image-candidate batches were completed. The measured source state above is the current count for this branch and supersedes those earlier inventory figures.


## Authoritative current directory state — 23 October 2026

Latest branch-source audit: **100 unique brand cards, 100 visible research snapshots, 45 sourced image candidates, 45 rights-pending labels and 55 CSS artwork/monogram fallbacks**. The image register has 100 rows, 45 with sourced candidates. All image tags have alt text, dimensions, lazy loading and fallback handling. The official-domain field is populated on 48/100 cards; the legal-operator field is populated on 46/100 cards. These are field-coverage counts, not licensing approvals. Evidence grades: A 44, B 7, C 49; statuses: 99 HOLD, 1 EXCLUDE. Review approval remains 0/100. The page is noindex, PR #36 is open/draft/unmerged and not mergeable, and no Cloudflare production deployment is confirmed. Historical counts above describe earlier batch checkpoints only.
