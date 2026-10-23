# Official-site image candidate QA — 23 October 2026

**Current scope:** 21 sourced logo candidates are now registered in the 100-brand directory. The original 20-candidate spot-check is retained below as historical QA; Silkbet was added afterward from an image link exposed by its official homepage. This is a source-presence check, not a legal review, licence verification, or guarantee of long-term URL availability.

## Current image inventory

- 21/100 brand cards have sourced logo candidates; each is visibly marked **SOURCE FOUND · RIGHTS PENDING** and has a fallback monogram.
- The original 20-candidate spot-check found 18 candidates on successfully extracted official pages; two pages timed out (Admiral Switzerland and Betinia NJ). Silkbet's homepage subsequently exposed `https://silkbet.bet/assets/silkbet-gold.svg`, bringing the current count to 19 candidates found in extracted official-page image links, with the same two original timeouts.
- Jollie's card and asset register use `https://jollie.de/Assets/Images/jollie-logo-white-1.svg`, an official logo asset present on the Jollie website. The previously used `og-default.png` was a social-preview image rather than the preferred logo.
- All 21 assets remain **rights pending**. Source-page presence does not prove direct asset uptime, exact legal identity, or permission to reuse.


## Candidate pages checked

Successful page extraction: Casineo, Jollie, Betsuna, Vegas Club Casino, Casushi, FruitKings, Betcrown, BetLegend, BetNero, Casiku, Peachy Games, PlaySunny, PlayWins, BetFusion, Megaways Casino, LuckyMate, 7Bet, and Justin Casino.

Timed out: Admiral Switzerland and Betinia NJ.

## Publication gate

Do not describe any logo as licensed for reuse based on this check. Keep permissions pending until terms, written permission, or another valid reuse basis is recorded. Keep the directory `noindex,follow` until brand-level legal scope, evidence, image rights, and editorial approval are complete. Image-source presence does not validate a brand's licence or availability in every market.

## Reproduction

Asset register: `docs/targets/brand-image-asset-register-2026-10-23.csv`  
Directory: `brand-directory/index.html`


## Directory image-layout pass — 23 October 2026

- Added explicit `width="160"` and `height="64"` dimension hints to all 20 remote logo candidates and fixed the CSS image box to a contained 160×64 slot. This gives the browser a stable reserved image ratio before the remote asset loads and avoids stretching logos; `object-fit: contain` preserves the asset proportions.
- Added/retained asynchronous image decoding and the existing lazy loading, descriptive alt text, fallback monograms, and visible `SOURCE FOUND · RIGHTS PENDING` labels.
- Source-level verification after the change: 100 cards; 20 image elements; 20 dimension pairs; 20 fallback spans; 20 rights-pending labels; no missing image alt text; no duplicate HTML IDs; external links opened in new tabs carry `noopener` protection.
- This is markup/layout QA only. It does not prove remote image uptime, exact brand ownership, permission to reuse, or production deployment. Keep all image rights pending until permission/licence is documented.

- Final markup recheck after the image-dimension edit: 100 unique card labels; all 100 cards include operator, regulator/authority, evidence grade, verification checklist, and research-context panel; all 20 image tags have dimensions and alt text; no malformed `height/src` attribute boundaries remain; no unsafe new-tab links were detected. The page intentionally remains `noindex,follow` until the review and asset-rights gates are cleared.


## Brand-list integrity correction — 23 October 2026

- Replaced the two non-brand placeholders `France online casino category` and `Australia online casino category` with two distinct Great Britain research leads: Silkbet and BigBangBet. Both have official UK Gambling Commission register/domain evidence in the tracker, but remain HOLD because consumer-product status/terms are not fully reviewed.
- Preserved an explicit market-scope guardrail: France and Australia are excluded from this casino directory. The page remains `noindex,follow` and is not a consumer recommendation list.
- Source-level check after replacement: 100 cards, 100 unique card labels, both new brand entries present, both category placeholders absent. This verifies list integrity only; it does not change publication approvals or image rights.


## Latest image candidate update — 23 October 2026

- Added Silkbet's `https://silkbet.bet/assets/silkbet-gold.svg` after the official Silkbet homepage exposed it as an image link. It is labelled `SOURCE FOUND · RIGHTS PENDING` and has a monogram fallback. This does not grant republication rights.
- Tried the tracker-listed BigBangBet homepage, but the fetch returned `invalid_url`; no image URL was guessed. Its directory card retains the custom artwork and the asset register marks it `NOT SOURCED`.
- Current directory count: 21 candidate logo image tags across 100 cards; all remain subject to direct-load, identity and rights checks. The two replaced category placeholders are removed from the 100-brand list.


## Inventory reconciliation — 23 October 2026

The current HTML and asset register were re-counted after adding Silkbet: **100 brand cards, 21 image elements, 21 visible rights-pending labels, and 21 asset-register rows with a sourced candidate**. BigBangBet remains without an image URL because the official-site fetch failed; no URL was guessed. The remaining 79 cards use original CSS-generated decorative artwork and monograms, not brand-owned logos or photographs. No image reuse permission has been established by this source check. The directory remains `noindex,follow`, and production deployment is not confirmed.
