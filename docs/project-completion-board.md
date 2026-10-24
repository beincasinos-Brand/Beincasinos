# Latest verified work checkpoint — 24 October 2026, 17:58 UTC

- **Main brand registry:** 207 market-specific rows, 156 distinct global-brand IDs, 205 HOLD and 2 rejected. The 100-name candidate register has a candidate-to-ID map with **39 provisional mappings** (22 exact normalized slugs and 17 explicitly listed aliases) and **61 unresolved names**. These mappings support deduplication only; they do not prove market eligibility or approve reviews.
- **Tier-1 prospect tracker:** 112 rows, 18 columns, zero malformed-width rows and zero duplicate brand/market keys. Four IDs are filled (Casineo.ch → `casineo`, Jollie.de → `jollie`, BetRivers Casino PA → `betrivers-casino`, Hollywood Casino Online PA → `hollywood-casino`); 108 remain blank. There are 110 rows in the international/supplemental US-state research scope and two category exclusions (FR/AU). Domain values: 58 `VERIFY`, two `NOT APPLICABLE`, zero `UNKNOWN`.
- **International board:** ten roadmap markets — GB, BE, SE, DK, ES, IT, NL, DE-SH, CH and Ontario. US-NJ, US-PA and US-MI are supplemental, not replacements for the ten markets. The board has exactly ten priority brand-market targets, all HOLD.
- **Directory QA:** source contains 100 cards with 100 unique titles, including one BetRivers Casino and one Hollywood Casino Online card; Ivy Casino is absent. The Cloudflare branch preview has canonical `https://beincasinos.online/brand-directory/`, robots `noindex,follow`, and a 44-URL sitemap excluding `/brand-directory/`. Production `https://beincasinos.online/brand-directory/` returns 404. No production deployment or indexing release occurred.
- **Pennsylvania accuracy:** the PGCB's 13 February 2026 certificate-holder list names `http://www.hollywoodcasino.com` for slots/table games from 19 Dec 2024; the old `pa.hollywoodcasino.com` URL ended 14 Dec 2023. Current HTTPS canonical/redirect and customer-contracting entity remain open. BetRivers remains a separate HOLD lead.
- **CI:** recent Static site checks runs fail before any step runs and logs are unavailable. The root cause is unconfirmed; GitHub Status currently reports all systems operational and no incident for 24 October. The repository owner should inspect Actions settings, runner availability and workflow permissions. Do not bypass checks.
- **PR #141:** open, Draft, unmerged, with 126 changed files at this checkpoint. **Approved consumer reviews remain 0/100.** No merge or production deployment was performed.

---



# Tracker reconciliation checkpoint — 24 October 2026, 19:45 UTC

- Added six market-specific target records to `docs/tier-1-master-prospect-tracker.csv` so the tracker represents all ten roadmap markets, not only GB/NL/CH/DE and US-state leads: Betano Casino Belgium (BE), Betsson Casino Sweden (SE), Danske Licens Spil Casino (DK), Luckia Casino Spain (ES), Sisal Casino Italy (IT), and Caesars Casino Ontario (CA-ON). Each row has regulator/source references, explicit HOLD status, market-specific blockers, and no inferred willingness-to-pay claim.
- Re-parsed the full CSV with quote-aware handling: **112 data rows, 18 columns, zero width errors, zero duplicate brand/market keys, 108 blank global brand IDs, 58 VERIFY domains, zero UNKNOWN and two NOT APPLICABLE**. The six new rows are source-backed research leads, not completed reviews.
- Updated the international priority board count to match the tracker. Approved reviews remain **0/100**. The PR is still Draft/unmerged and CI remains blocked by runner allocation; no deployment was made.
---

# Tracker coverage guardrail — 24 October 2026, 19:50 UTC

- `scripts/check_prospect_tracker.py` now requires at least one tracker row in each roadmap market: GB, BE, SE, DK, ES, IT, NL, DE, CH and CA-ON. The goal is to prevent the six-market omission identified during the latest audit.
- The latest quote-aware tracker audit reports 112 data rows, 18 columns, zero malformed-width rows, zero duplicate brand/market keys, 108 blank global IDs, 58 VERIFY domains, zero UNKNOWN and two NOT APPLICABLE.
- Latest observed PR head `dda674d2f744d868a60b27bcfa70a658da152383` still has no successful CI: run `40118399486` failed before runner allocation. Release remains blocked; approved reviews remain 0/100.
