# Directory image and asset readiness audit — 24 October 2026

**Branch:** `feature/directory-global-brand-count-disclosure-2026-10-23`  
**Scope:** Static audit of `docs/targets/brand-image-asset-register-2026-10-23.csv` for the 100-card research directory. This checks register completeness only; it does not fetch assets, validate pixels, establish trademark rights, or approve public reuse.

## Results

- Asset register: **100 brand-market rows**.
- Remote image candidates: **60** (60%).
- No remote image URL / intended CSS artwork or monogram fallback: **40** (40%).
- Rows with explicit alt text: **100/100**.
- Sourced rows missing a source-page URL: **0**.
- Sourced rows without a rights/permission note: **0**.
- Asset status in register: **60 SOURCE FOUND — RIGHTS PENDING**; **40 NOT SOURCED**.

## Interpretation

Finding a logo on an official site establishes a discovery lead, not a licence to republish it. Trademark, copyright, terms-of-use and attribution questions remain open unless explicitly documented by a reliable rights basis. A public-domain text mark may still be a trademark. Do not remove the RIGHTS PENDING status merely because an image loads.

The 40 NOT SOURCED rows should retain original CSS artwork or monogram fallbacks. Do not guess asset URLs or substitute unrelated favicons. Remote candidates should only be activated in a public release after identity, direct rendering, responsive crop, accessible alternative text and permission/attribution have been reviewed.

## Required next pass

1. Fetch each of the 60 candidate assets in a low-cost, read-only audit and record success/failure, content type, dimensions and redirect outcome.
2. Review official source page and asset identity together; mark logos that are stale, ambiguous, distorted, or unrelated to the market-specific product.
3. Record a defensible rights basis per asset (explicit permission/licence, documented public-domain basis with trademark caveat, or replacement with original artwork).
4. Keep the no-image fallback for unresolved cases and verify alt text describes the image's function rather than adding unsupported endorsement claims.
5. Run responsive visual review and accessibility checks before removing `noindex,follow`; this static register audit does not authorize indexing, merge or production deployment.

**Status: OPEN / HOLD.** The directory may have 100 cards, but image-source presence is not image-rights clearance or evidence of 100 eligible distinct global brands.
