# 12-market casino review eligibility sprint

**Created:** 25 October 2026  
**Scope:** BeInCasinos' stated target markets: AU, CA, GB, US, CH, DE, NL, SE, ES, IT, FR and BE.

## What this batch adds

- Twelve market-specific eligibility protocols with official regulator starting points.
- A common evidence log and pass/hold/exclude decision model.
- Explicit treatment of markets where online casino is prohibited or highly restricted, and of the US/Canada's subnational licensing structures.
- No public pages, bonus claims, ratings, sitemap changes, deployment or workflow runs.

## Critical market distinctions

| Market | Key issue | Initial publication rule |
|---|---|---|
| AU | Offshore online casino services are generally restricted under federal interactive-gambling law | Default exclude online-casino offers unless specific legal review establishes otherwise |
| CA | Province-by-province; Ontario registration is not nationwide approval | Name and verify province |
| GB | UKGC permissions and exact operator/domain matter | Match the current UKGC register |
| US | State/tribal and product-specific permissions | Separate dossier per state |
| CH | Swiss authorisation and approved online offers | Match exact domain to Swiss records |
| DE | GGL whitelist and product-specific permission | Check current whitelist |
| NL | KSA register and enforcement status | Check exact entity/domain |
| SE | Swedish licence and marketing rules | Check current Spelinspektionen records |
| ES | DGOJ operator/domain permission | Check exact domain and product |
| IT | ADM concession and approved domain | Verify exact concession/domain |
| FR | Online casino games are not generally authorised like online poker/sports betting | Default exclude online-casino targeting absent specialist legal confirmation |
| BE | Belgian licence class and authorised-domain lists | Match exact entity/domain and licence class |

## Existing repository coverage snapshot

A tree inspection of main at bdc1a4421d59c4c49b37ebb466bc04cd86d0270f found **97 files named docs/brand-profile-*.md**, including a template and regulatory follow-ups. These are files, not 97 unique verified brands or approved public reviews. The filenames are heavily GB/UK-labelled, with only a small number tagged CH, US, IT, DE and NL, and no obvious AU, CA, SE, ES or BE profile filenames in the inspected list. Filename tags are a rough inventory signal, not a legal or content audit.

## Batch files

- [AU — Australia](market-gates/au-australia-eligibility-gate.md)
- [CA — Canada](market-gates/ca-canada-eligibility-gate.md)
- [GB — Great Britain](market-gates/gb-great-britain-eligibility-gate.md)
- [US — United States](market-gates/us-united-states-eligibility-gate.md)
- [CH — Switzerland](market-gates/ch-switzerland-eligibility-gate.md)
- [DE — Germany](market-gates/de-germany-eligibility-gate.md)
- [NL — Netherlands](market-gates/nl-netherlands-eligibility-gate.md)
- [SE — Sweden](market-gates/se-sweden-eligibility-gate.md)
- [ES — Spain](market-gates/es-spain-eligibility-gate.md)
- [IT — Italy](market-gates/it-italy-eligibility-gate.md)
- [FR — France](market-gates/fr-france-eligibility-gate.md)
- [BE — Belgium](market-gates/be-belgium-eligibility-gate.md)

## Execution order

1. **Eligibility before content:** apply the market gate to every brand candidate.
2. **Resolve identity:** exact domain, contracting operator, regulator record and product.
3. **Prioritise clean passes:** write full reviews only when evidence supports the intended market.
4. **Exclude unlawful/unavailable products:** do not make pages just to fill a geographic quota.
5. **Score only after evidence:** use the repository's weighted scorecard and mark unavailable evidence explicitly.
6. **Keep internal drafts out of sitemap:** public pages must pass editorial, legal, image-rights and technical release gates.

## Count reporting standard

Always report separate counts for: unique candidate brands, dossiers created, identity verified, market eligible, complete evidence files, second-editor approved reviews, public review pages and indexed URLs. Never collapse these into a single “brands completed” number.
