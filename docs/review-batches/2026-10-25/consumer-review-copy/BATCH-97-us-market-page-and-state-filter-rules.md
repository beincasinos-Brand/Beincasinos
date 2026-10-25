# Batch 97 — United States: state filters and review architecture
**Scope:** prevent a national page from implying state-wide availability.

## Candidate names to reconcile
BetMGM Casino, DraftKings Casino, FanDuel Casino. Each exact online casino product must be checked against the regulator in every state shown as eligible.

## Data model
For each brand-state pair, store operator, official domain, product category, current regulator source, eligibility status, terms URL, date checked, and caveats. Keep state-specific evidence separate even if the brand's marketing site is shared.

## UI rules
- A state filter must not default to “available” without evidence.
- Use explicit statuses such as eligible, not available, and pending verification.
- Hide or disable a commercial CTA when eligibility is not confirmed.
- Don't display a generic US welcome bonus where state-specific terms differ.
- Keep the source and check date available to editors.

## SEO
Create state landing pages only if they answer real local questions with current state-specific information. Don't produce thin doorway pages or claim nationwide legality. The review must not encourage circumvention of geolocation or eligibility restrictions.

Sources to begin with: Michigan MGCB and New Jersey DGE official resources, then each other state's regulator.
