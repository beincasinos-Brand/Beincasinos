# Latest verified work checkpoint — 24 October 2026, 17:56 UTC

- **Main brand registry:** 205 market-specific rows, 154 distinct `global_brand_id` values, 203 HOLD and 2 rejected. The separate 100-name candidate register now has a candidate-to-ID map: 36 provisional mappings (20 exact normalized slugs and 16 explicitly listed aliases), with 64 candidate names still unresolved. This map is not review approval or proof of current eligibility.
- **Tier-1 prospect tracker:** 112 rows, 18 columns, zero malformed-width rows and zero duplicate brand/market keys. Four IDs are filled (Casineo.ch → `casineo`, Jollie.de → `jollie`, BetRivers Casino PA → `betrivers-casino`, Hollywood Casino Online PA → `hollywood-casino`); 108 remain blank. There are 110 rows in the active international/supplemental US-state research scope and two category exclusions (FR/AU). Domain values: 58 `VERIFY`, two `NOT APPLICABLE`, zero `UNKNOWN`.
- **International board:** restored to the original ten-market roadmap — GB, BE, SE, DK, ES, IT, NL, DE-SH, CH and Ontario. US-NJ, US-PA and US-MI remain supplemental and do not replace the ten roadmap markets.
- **Directory QA:** source contains 100 cards with 100 unique titles, including one BetRivers Casino and one Hollywood Casino Online card; Ivy Casino is absent. The Cloudflare branch preview has canonical `https://beincasinos.online/brand-directory/`, robots `noindex,follow`, and its 44-URL sitemap excludes `/brand-directory/`. Production `https://beincasinos.online/brand-directory/` returns 404. No production deployment or indexing release occurred.
- **Pennsylvania accuracy:** the PGCB's 13 February 2026 certificate-holder list names `http://www.hollywoodcasino.com` for slots/table games from 19 Dec 2024; the old `pa.hollywoodcasino.com` URL ended 14 Dec 2023. Current HTTPS canonical/redirect and customer-contracting entity remain open. BetRivers remains a separate HOLD lead.
- **CI:** recent Static site checks runs fail before any step runs and logs are unavailable. The root cause is unconfirmed; GitHub Status currently reports all systems operational and no incident for 24 October. The repository owner should inspect Actions settings, runner availability and workflow permissions. Do not bypass checks.
- **PR #141:** open, Draft, unmerged, with 126 changed files at this checkpoint. **Approved consumer reviews remain 0/100.** No merge or production deployment was performed.

---


# Tracker reconciliation checkpoint — 24 October 2026, 19:45 UTC

- Added six market-specific target records to `docs/tier-1-master-prospect-tracker.csv` so the tracker represents all ten roadmap markets, not only GB/NL/CH/DE and US-state leads: Betano Casino Belgium (BE), Betsson Casino Sweden (SE), Danske Licens Spil Casino (DK), Luckia Casino Spain (ES), Sisal Casino Italy (IT), and Caesars Casino Ontario (CA-ON). Each row has regulator/source references, explicit HOLD status, market-specific blockers, and no inferred willingness-to-pay claim.
- Re-parsed the full CSV with quote-aware handling: **112 data rows, 18 columns, zero width errors, zero duplicate brand/market keys, 108 blank global brand IDs, 58 VERIFY domains, zero UNKNOWN and two NOT APPLICABLE**. The six new rows are source-backed research leads, not completed reviews.
- Updated the international priority board count to match the tracker. Approved reviews remain **0/100**. The PR is still Draft/unmerged and CI remains blocked by runner allocation; no deployment was made.
