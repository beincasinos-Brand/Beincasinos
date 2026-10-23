# Brand-card image rights and quality gate

**Prepared:** 23 October 2026  
**Status:** Internal implementation checklist — not a publication approval.

## Purpose

Prevent placeholder artwork, unlicensed third-party logos, misleading screenshots, and mismatched images from being treated as finished brand-card assets. A card is not image-complete merely because an image URL exists.

## Per-brand image record

Record the following for every one of the 100 planned brand cards:

| Field | Required evidence |
|---|---|
| Canonical brand and market | Exact brand + local product/market; do not reuse a market-specific asset for another jurisdiction without checking |
| Asset type | Official logo, original illustration, licensed photo, or CSS monogram fallback |
| Source | Exact source page or asset URL; identify whether first-party or third-party |
| Rights basis | Written permission, explicit licence, documented terms permitting reuse, or original artwork |
| Attribution | Required credit and licence details, where applicable |
| Capture date | Date the asset and rights statement were checked |
| Technical quality | Readable at card size, correct aspect ratio, no broken URL, no watermark, no unrelated product |
| Accessibility | Meaningful alt text for informative images; empty alt text for decorative art |
| Fallback | Branded text/monogram or CSS illustration that works if the remote asset fails |
| Review state | VERIFIED, ORIGINAL, FALLBACK, RIGHTS-PENDING, or REJECTED |

## Release rules

1. **Do not treat search-engine image results as reuse permission.** A visible logo or screenshot is not automatically licensed for republication.
2. Prefer official media/press assets only when the source's terms permit the intended use. Keep a source URL and rights note with each asset.
3. If permission is unclear, use a neutral CSS monogram or original artwork; label the asset internally as RIGHTS-PENDING and do not present it as an official logo.
4. Never use screenshots of a real-money product to imply hands-on testing unless the capture is genuine, dated, lawfully obtained, and the relevant test is documented.
5. Do not use one generic casino image to imply a specific operator's lobby, games, bonus, payment options, or licence.
6. Avoid image filenames and alt text that make unsupported claims such as “official”, “licensed”, “best”, or “safe”.
7. Validate remote image URLs, responsive crop, loading behaviour, contrast and alt text before release.
8. Keep decorative fallbacks visually consistent, but ensure the brand name remains available as text and is not embedded only in the image.

## QA checklist

- [ ] All 100 card records have an explicit image state.
- [ ] Every official/logo asset has a source URL and documented reuse basis.
- [ ] Rights-pending assets are not described as official or approved.
- [ ] No broken, watermarked, mismatched, or duplicated stock images.
- [ ] Alt text is accurate, concise and market-appropriate.
- [ ] CSS fallback works with images blocked and on small screens.
- [ ] Screenshots do not imply testing that was not performed.
- [ ] Final image inventory is reviewed independently before production.

## Counting

Report image readiness separately from brand eligibility and review approvals. Do not count a CSS fallback as a licensed logo; do not count an image as verified merely because it renders. Brand identity, local authorisation, editorial review and asset rights are separate release gates.
