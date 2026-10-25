# Batch 35 — image-rights remediation policy and acceptance gate

Date: 2026-10-25. Internal editorial operations. This report does not establish copyright ownership or permission.

## Ledger snapshot
The 100-row ledger currently records image-source gaps and unresolved reuse rights. A source URL alone is not a licence, and an accessible logo/image is not automatically available for commercial reuse.

## Mandatory remediation
1. Treat every asset as blocked until ownership, permission, or a reviewed legal basis is documented.
2. For an asset with no source, use an original neutral editorial illustration or typography-only placeholder while research continues.
3. For an asset with a source but no rights evidence, do not publish it until the licence/permission scope is confirmed.
4. Record asset source, licence or permission evidence, permitted use, territories, duration, attribution requirements and date checked in the evidence bundle.
5. Do not imitate a real brand's logo/trade dress with generated art or imply sponsorship, endorsement, regulator approval or verification.
6. Keep the asset decision separate from operator licensing, bonus verification, scoring and publication approval.

## Suggested ledger improvement
Add explicit fields for:
- `image_license_or_permission_evidence`
- `image_rights_checked_utc`
- `image_permitted_territories`
- `image_attribution_required`
- `image_asset_type` (licensed logo / original illustration / typography fallback / screenshot)
- `image_reviewer`

Do not modify the existing CSV schema until downstream consumers and validation scripts are checked.

## Acceptance criteria
- Every public image has traceable permission/ownership evidence appropriate for the use and target territories, or is an original asset created for BeInCasinos with documented ownership.
- Alt text is descriptive and does not make unsupported claims.
- Essential legal, bonus and safety details remain in accessible text, not embedded only in an image.
- Unresolved asset rights keep the row on HOLD.

No public assets changed in this batch. No merge/deploy performed.
