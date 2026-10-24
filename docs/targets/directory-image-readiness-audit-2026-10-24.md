# Directory image and asset readiness audit — 24 October 2026

**Branch:** `feature/directory-global-brand-count-disclosure-2026-10-23`  
**Scope:** Static audit of `docs/targets/brand-image-asset-register-2026-10-23.csv` and targeted official-page image discovery. This checks source metadata and register consistency only; it does not fetch every image file, validate pixel rendering, establish trademark rights, or approve public reuse.

## Current register results

- Asset register: **100 brand-market rows**.
- Remote image candidates: **64** (64%).
- No remote image URL / intended CSS artwork or monogram fallback: **36** (36%).
- Rows with explicit alt text: **100/100**.
- Sourced rows missing a source-page URL: **0**.
- Sourced rows without a rights/permission note: **0**.
- Asset status: **64 SOURCE FOUND — RIGHTS PENDING**; **36 NOT SOURCED**.

## Targeted official-page discovery — 24 October 2026

Fetched ten candidate official-site pages for brands that previously had no image URL in the register. Four additional image candidates were recorded:

- **Los Vegas:** official page metadata exposed a 128px favicon. It is a small-icon candidate, not a full wordmark; the page did not fully render during this check.
- **LottoGo Casino:** the official page exposed a default logo SVG, but redirected to a location-unavailable page from the check environment.
- **Alfobet:** the official homepage exposed its logo image. This is image-source evidence only; the existing UKGC record describes `lobby.alfobet.com` as a white-label domain, so the exact consumer-facing domain/operator match remains open.
- **Rollerbet:** the UK sports page exposed a favicon. This is a small-icon candidate; the fetched page does not prove the casino product/domain relationship.

The other checks returned a country-block page for Neptune Play or errors/blocking for 247Bet, Casino and Friends, BigBangBet, Betta Bet and PricedUp. No asset was guessed for those brands. The image register and directory now contain 64 candidate assets; the four new ones are all explicitly rights-pending.

## Interpretation

Finding a logo or favicon on an official site establishes a discovery lead, not permission to republish it. A public page being reachable does not prove that the casino product is authorised in the listed market. Small favicons are not automatically suitable for full-size presentation. Keep each brand on HOLD until its exact domain, operator and local casino-product permission are independently confirmed.

The 36 NOT SOURCED rows should retain original CSS artwork or monogram fallbacks. Do not guess asset URLs or substitute unrelated images. Remote candidates should only be activated in a public release after identity, direct rendering, responsive crop, accessible alternative text and a defensible reuse basis have been reviewed.

## Required next pass

1. Test all 64 candidate assets for response, content type, dimensions, redirects and hotlink behaviour.
2. Review the source page and asset identity together; flag stale, ambiguous, distorted or market-mismatched images.
3. Record a defensible rights basis per asset (explicit permission/licence, documented public-domain basis with trademark caveat, or replacement with original artwork).
4. Keep the no-image fallback for unresolved cases and verify alt text against the actual asset.
5. Run responsive visual review and accessibility checks before any indexing or production release.

**Status: OPEN / HOLD.** The directory has 100 cards, but image-source presence is not image-rights clearance or evidence of 100 eligible distinct global brands.
