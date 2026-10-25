# Batch 64 — Target-market coverage and duplicate control
**Purpose:** organise the 12 target markets (AU, CA, GB, US, CH, DE, NL, SE, ES, IT, FR, BE) without inflating the 100-brand target or publishing unlawful availability claims.

## Coverage matrix fields
For every unique brand, track each market separately:
- Market and region granularity (country, province, state, canton where relevant)
- Exact consumer domain and legal entity
- Regulator record and permitted product category
- Age/residency/geolocation constraints
- Product live-check date
- Offer and terms check date
- Payment/cashier check date
- Safeguards/support check date
- Image rights and asset source
- Evidence status and blockers

## Rules by market
- Australia: do not imply offshore online casino availability is legally authorised; verify current ACMA guidance and product type.
- Canada: provincial services are not automatically nationwide; track each province and avoid counting provincial variants as separate global brands.
- Great Britain: check current UK Gambling Commission licence and exact domain; licence categories and operating entities matter.
- United States: check the state regulator and exact state product; a Michigan or New Jersey record is not national approval.
- Switzerland: check the Federal Gaming Board's approved online platform and exact operator/domain.
- Germany: verify GGL listing and category-specific scope.
- Netherlands: verify KSA register and exact domain/operator.
- Sweden: verify Spelinspektionen record and product category.
- Spain: verify DGOJ record and exact operator/domain/product.
- Italy: verify ADM concession and product scope.
- France: do not label online slots/table games as authorised without current primary-source confirmation; distinguish poker/sports/lottery and land-based venues.
- Belgium: verify Belgian Gaming Commission record and exact product/domain.

## Canonical dedupe logic
- Brand alias, spelling variation, parent brand, operator and domain are different attributes—not automatic extra brands.
- A brand appearing in two batches remains one canonical brand.
- A local legal entity/domain may require a distinct market review, but does not automatically increase the global unique-brand count.
- A supplier/game title is not a casino brand.
- A venue and its online product must be distinguished and linked rather than blindly counted twice.

## Current status
The batch files are research drafts and do not prove that 100 unique casino brands have passed all gates. The next completion step is a single canonical inventory with evidence status per brand, followed by page-by-page review QA. Keep production unchanged until that inventory is reconciled.
