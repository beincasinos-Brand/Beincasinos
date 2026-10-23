# Global brand deduplication audit — 23 October 2026

**Purpose:** prevent market-specific registry rows from being misreported as distinct brands toward the 100-brand target.  
**Scope:** active research CSV only; not an eligibility or publication audit.

## Snapshot

- Active registry: **175 market-specific rows**, 31 columns, no ragged CSV rows, no exact duplicate brand-name cells, and no publication-approved rows.
- A preliminary normalization that strips a trailing market code in parentheses (for example, (DE), (IT), (ES), (MI)) produces **148 provisional brand labels**.
- That preliminary normalization identifies **20 repeat-brand groups** and 27 excess market-specific rows beyond one row per normalized label.
- **148 is not the number of eligible brands.** It is a label-normalization estimate only. The registry still includes leads, unverified permission records, excluded records, shared legal operators and brands with incomplete casino-vertical checks.
- Publication-approved reviews remain **0/100**. All candidate rows remain HOLD or rejected as recorded in the registry.

## Repeat-brand groups found by market-suffix normalization

| Provisional brand label | Market-specific rows |
|---|---|
| bet365 Casino | bet365 Casino; Bet365 Casino (NL); bet365 Casino (MI); bet365 Casino (DE) |
| 888casino | 888casino; 888casino (SE); 888casino (IT) |
| Betway Casino | Betway Casino; Betway Casino (DE) |
| William Hill Casino | William Hill Casino; William Hill Casino (ES) |
| Ladbrokes Casino | Ladbrokes Casino; Ladbrokes Casino (BE) |
| LeoVegas | LeoVegas; LeoVegas (IT); LeoVegas (DE) |
| Unibet Casino | Unibet Casino; Unibet Casino (BE); Unibet Casino (SE) |
| PokerStars Casino | PokerStars Casino; PokerStars Casino (BE); PokerStars Casino (ES) |
| Betfair Casino | Betfair Casino; Betfair Casino (ES) |
| bwin Casino | bwin Casino; bwin Casino (BE); Bwin Casino (ES) |
| Casumo | Casumo; Casumo (DE) |
| BetMGM Casino | BetMGM Casino; BetMGM Casino (MI) |
| DraftKings Casino | DraftKings Casino; DraftKings Casino (MI) |
| FanDuel Casino | FanDuel Casino; FanDuel Casino (MI) |
| BetRivers Casino | BetRivers Casino; BetRivers Casino (MI) |
| Hard Rock Bet Casino | Hard Rock Bet Casino; Hard Rock Bet Casino (MI) |
| Fanatics Casino | Fanatics Casino; Fanatics Casino (MI) |
| Winamax | Winamax; Winamax (ES) |
| Betano Casino | Betano Casino (BE); Betano Casino (DE) |
| Betsson | Betsson (IT); Betsson (SE) |

## Additional manual identity checks

- **Same legal operator, multiple brands:** Bwin and PartyCasino are mapped to ELECTRAWORKS CEUTA, S.A. in Spain; PlatinCasino and Fuegocasino are mapped to 8PE ESPAÑA, PLC. Distinct brand reviews require materially distinct products/terms/evidence; operator counts must not be inflated.
- **Same legal operator, multiple Dutch brands:** TOTO and Winnitt share TOTO Online B.V. A second brand label is not automatically a second distinct operator.
- **Same legal operator, multiple German brands:** Casumo, Winfest, Lapalingo, Lord Lucky and Tigerspin appear under Rabbit Entertain IT Limited in the GGL whitelist. They may be distinct customer-facing brands but are not distinct licensees.
- **Market-specific records are necessary for legal accuracy:** one international brand can have different local contracting entities, permissions, terms and consumer protections. Do not collapse those rows when reviewing jurisdictional compliance; instead keep a global brand ID plus separate market-specific evidence.

## Required counting model

Use two distinct counts in the project dashboard:

1. **Distinct global brands:** deduplicated customer-facing brands, after manual alias review.
2. **Eligible brand-market pairs:** unique brand × jurisdiction combinations with a current, exact permission for the casino vertical being reviewed.

The 100-review goal should count only a completed, evidence-backed review for a defined brand-market pair, with current terms, payments/withdrawals, complaints/ADR, safer-gambling, privacy/cookies, accessibility, enforcement history and independent second review. A candidate row, regulator-list entry, or internal draft does not count as a completed review.

## Next reconciliation steps

1. Add a stable global brand ID to each registry record, while preserving market-specific rows.
2. Manually reconcile aliases and brand spelling, including brands whose name changes are not expressed as a simple country suffix.
3. Confirm current casino vertical and local permission before counting an eligible brand-market pair.
4. Record each review as draft, second review, approved, or rejected; never infer approval from evidence collection alone.
5. Keep all 175 rows as a research buffer until the eligible count is reconciled; do not present the buffer as 100 verified brands.
