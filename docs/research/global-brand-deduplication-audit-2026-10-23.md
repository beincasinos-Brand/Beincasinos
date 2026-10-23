# Global brand deduplication audit — 23 October 2026

**Snapshot:** `docs/brand-research-template.csv` on branch `feature/directory-global-brand-count-disclosure-2026-10-23`. This is a reproducible structural count, not a regulator-eligibility or publication audit.

## Current structural snapshot

- CSV data rows: **204**.
- Columns: **33**.
- Distinct non-empty `global_brand_id` values: **154**.
- IDs appearing on multiple market-specific rows: **30 groups**, covering **80 rows**. Those groups contain **50 excess rows** beyond one row per ID.
- IDs appearing on exactly one row: **124**.
- Rows missing `global_brand_id`: **0**.
- Rows missing `market_code`: **0**.
- Publication decision values: `HOLD`: **202**; `rejected`: **2**.
- Publication-approved reviews: **0/100**.

The earlier 175-row / 140-ID summary and 24-group table were stale. The table below is regenerated from the current 204-row CSV. The 154 IDs are provisional identifiers, **not 154 eligible brands**. A shared ID indicates the current data model's intended brand grouping; it does not certify the alias group is correct.

## Repeated global IDs in the current CSV

| Provisional global brand ID | Rows | Market codes | Market-specific labels in CSV |
|---|---:|---|---|
| `888casino` | 4 | GB, ES, SE, IT | 888casino; 888casino.es; 888casino (SE); 888casino (IT) |
| `bally-bet-casino` | 2 | CA-ON, US-NJ | Bally Bet Casino; Bally Bet Casino (NJ) |
| `bet365-casino` | 5 | GB, NL, US-MI, DE, US-NJ | bet365 Casino; Bet365 Casino (NL); bet365 Casino (MI); bet365 Casino (DE); bet365 Casino (NJ) |
| `betano` | 3 | GB, BE, DE | Betano; Betano Casino (BE); Betano Casino (DE) |
| `betfair-casino` | 2 | GB, ES | Betfair Casino; Betfair Casino (ES) |
| `betmgm-casino` | 3 | GB, US-MI, US-NJ | BetMGM Casino; BetMGM Casino (MI); BetMGM Casino (NJ) |
| `betparx-casino` | 2 | US-PA, US-NJ | betPARX Casino; BetParx Casino (NJ) |
| `betrivers-casino` | 3 | CA-ON, US-MI, US-NJ | BetRivers Casino; BetRivers Casino (MI); BetRivers Casino (NJ) |
| `betsson` | 4 | UNCONFIRMED, BE, IT, SE | Betsson Casino; Betsson Casino (BE); Betsson (IT); Betsson (SE) |
| `betway` | 3 | GB, ES, DE | Betway Casino; Betway (ES); Betway Casino (DE) |
| `bwin` | 3 | GB, BE, ES | bwin Casino; bwin Casino (BE); Bwin Casino (ES) |
| `caesars-palace-online-casino` | 2 | CA-ON, US-NJ | Caesars Palace Online Casino; Caesars Palace Online Casino (NJ) |
| `casino777` | 2 | CH, BE | Casino777.ch; Casino777.be (BE) |
| `casumo` | 2 | GB, DE | Casumo; Casumo (DE) |
| `codere` | 2 | ES, IT | Codere (ES); Codere.it (IT) |
| `draftkings-casino` | 3 | CA-ON, US-MI, US-NJ | DraftKings Casino; DraftKings Casino (MI); DraftKings Casino (NJ) |
| `fanatics-casino` | 3 | CA-ON, US-MI, US-NJ | Fanatics Casino; Fanatics Casino (MI); Fanatics Casino (NJ) |
| `fanduel-casino` | 3 | CA-ON, US-MI, US-NJ | FanDuel Casino; FanDuel Casino (MI); FanDuel Casino (NJ) |
| `golden-nugget-casino` | 2 | US-MI, US-NJ | Golden Nugget Casino (MI); Golden Nugget Casino (NJ) |
| `hard-rock-bet-casino` | 3 | CA-ON, US-MI, US-NJ | Hard Rock Bet Casino; Hard Rock Bet Casino (MI); Hard Rock Bet Casino (NJ) |
| `horseshoe-online-casino` | 2 | US-MI, US-NJ | Horseshoe Online Casino (MI); Horseshoe Online Casino (NJ) |
| `ladbrokes-casino` | 2 | GB, BE | Ladbrokes Casino; Ladbrokes Casino (BE) |
| `leovegas` | 3 | GB, IT, DE | LeoVegas; LeoVegas (IT); LeoVegas (DE) |
| `partycasino` | 2 | ES, US-NJ | PartyCasino (ES); PartyCasino (NJ) |
| `pokerstars-casino` | 4 | GB, BE, ES, US-NJ | PokerStars Casino; PokerStars Casino (BE); PokerStars Casino (ES); PokerStars Casino (NJ) |
| `starcasino` | 2 | BE, IT | Starcasino.be (BE); StarCasino (IT) |
| `starvegas` | 2 | CH, IT | Starvegas.ch; StarVegas (IT) |
| `unibet-casino` | 3 | GB, BE, SE | Unibet Casino; Unibet Casino (BE); Unibet Casino (SE) |
| `william-hill-casino` | 2 | GB, ES | William Hill Casino; William Hill Casino (ES) |
| `winamax` | 2 | FR, ES | Winamax; Winamax (ES) |

## Counting and eligibility rules

Keep one row per market-specific brand candidate because licences, domains, contracting entities, consumer terms and protections differ by jurisdiction. Deduplicate only the global brand count; never merge away market-specific evidence.

Count a brand-market pair as eligible only after checking the current primary regulator record for the exact online-casino vertical, customer-facing domain and contracting entity. Mark excluded, historical, unconfirmed, sportsbook-only, poker-only, or otherwise out-of-scope leads explicitly. A research lead, registry row, image candidate or internal draft does not count as an approved review.

## Remaining gates

1. Manually validate every repeated-ID group and any brand-family / alias relationship that is not obvious from the label.
2. Review the three market-unconfirmed rows and the excluded/historical rows; do not count them toward eligibility.
3. Verify exact current local casino permission and customer-facing domain for every candidate market.
4. Reconcile the tracker and directory counts from this same dated CSV snapshot.
5. Approve each consumer review only after current terms, payments/withdrawals, complaints/ADR, safer-gambling tools, privacy/cookies, accessibility, enforcement history and independent second review are complete.

**Status: OPEN / HOLD.** No brand is promoted to eligible by this structural audit. No production deployment is implied.
