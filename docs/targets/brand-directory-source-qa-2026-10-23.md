# 100-brand directory source QA — 23 October 2026

**Branch:** `ops/tier1-10-market-100-brand-roadmap-2026-10-22`  
**File checked:** `brand-directory/index.html`  
**Purpose:** Static source audit only. This is not a live-browser test, regulator re-verification, legal sign-off, or proof of Cloudflare deployment.

## Current checks

| Check | Result |
|---|---:|
| Brand cards | 100 |
| Unique brand labels | 100 |
| Cards with legal-operator field | 100/100 |
| Cards with regulator/authority field | 100/100 |
| Cards with evidence-grade field | 100/100 |
| Cards with verification checklist | 100/100 |
| Cards with research-context panel | 100/100 |
| Logo/image candidates | 22 |
| Candidate images with alt text | 22/22 |
| Candidate images with explicit width/height | 22/22 |
| Candidate images with lazy loading | 22/22 |
| Duplicate HTML IDs | 0 |
| New-tab links missing `noopener noreferrer` | 0 |

## Visual asset status

- 22/100 cards have a sourced logo candidate; all remain **rights pending**.
- 78/100 cards use CSS-generated editorial artwork and monograms, not official logos or photographs.
- BigBangBet has no image URL because its official-site fetch failed; no URL was guessed.
- The directory hero now accurately states 100 research entries, 22 logo candidates with rights pending, and 78 editorial card artworks.

## Publication and deployment gates

- The directory remains `noindex,follow` and excluded from the sitemap while brand-level checks remain incomplete.
- The 100 cards are research queue entries, not 100 approved consumer reviews. Publication approval remains 0/100.
- No GitHub Actions run was triggered. No Cloudflare production deployment is confirmed.
- Before publication, verify exact local domain/operator/casino authorisation, current terms and safer-gambling information, complaints/enforcement scope, image reuse rights, and independent editorial sign-off.


## Brand-list scope correction — 23 October 2026

The 100-card list no longer includes the excluded planned Maine placeholder `Caesars online casino brands`. It now includes `Horseshoe Online Casino (Michigan)`, sourced to the Michigan Gaming Control Board's authorized-platform list and exact Michigan casino URL. It remains HOLD, with exact contracting entity, current terms, payment/withdrawal, complaints, safer-gambling and enforcement checks outstanding. This change does not alter the 22-image-candidate count.
