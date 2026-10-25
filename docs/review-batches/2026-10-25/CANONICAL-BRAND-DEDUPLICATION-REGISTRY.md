# Canonical brand deduplication registry — working version

**Purpose:** separate candidate/file counts from unique brand identities. Generated from the candidate rows in `100-BRAND-TRACKER.md` on 2026-10-25.

## Accounting
- Tracker candidate rows parsed: 100
- Exact-name-normalized brand groups: 79
- Candidate rows that collapse into repeated-name groups: 21
- **Approved reviews: 0 confirmed by the tracker.**
- **This is not a verification list.** A canonical brand identity can still have multiple operators, products, domains and market permissions.

Normalization only folds case and punctuation. Human review is still needed for aliases and group relationships (e.g. brand/product names sharing an operator). Market-specific files must not be counted as distinct global brands.

## Candidate identity table

| Canonical candidate label | Market records | Tracker row IDs | Statuses observed | Unique brand verified? |
|---|---|---|---|---|
| 1xBet | ES | 32 | HOLD | NO — pending evidence |
| 711 | NL | 75 | HOLD | NO — pending evidence |
| 777.be | BE | 86 | HOLD | NO — pending evidence |
| 888casino | DE | 48 | HOLD | NO — pending evidence |
| 888slots | DE | 49 | HOLD | NO — pending evidence |
| AdmiralBet | ES | 27 | HOLD | NO — pending evidence |
| BacanaPlay | ES, DE | 33, 43 | HOLD | NO — pending evidence |
| bet365 | AU, NL | 13, 68 | HOLD | NO — pending evidence |
| BetCity | NL | 70 | HOLD | NO — pending evidence |
| Betclic | FR | 89 | HOLD | NO — pending evidence |
| BetFirst | BE | 87 | HOLD | NO — pending evidence |
| BetMGM | US-Michigan | 22 | HOLD | NO — pending evidence |
| BetNation | NL | 74 | HOLD | NO — pending evidence |
| Betscore | FR | 9 | EXCLUDE / LEGAL REVIEW | NO — pending evidence |
| Betsson | SE, FR | 54, 100 | HOLD | NO — pending evidence |
| Betway | CA-Ontario, SE, BE | 14, 62, 78 | HOLD | NO — pending evidence |
| Bingo.com | SE | 64 | HOLD | NO — pending evidence |
| Binobet | CA-Ontario, CH | 2, 11 | HOLD | NO — pending evidence |
| BullCasino | ES | 7 | HOLD | NO — pending evidence |
| bwin | BE, FR | 81, 96 | HOLD | NO — pending evidence |
| Casinia | DE, BE | 4, 10 | HOLD | NO — pending evidence |
| Casino Barcelona | ES | 29 | HOLD | NO — pending evidence |
| Casino777 | BE | 79 | HOLD | NO — pending evidence |
| Circus | NL, BE | 73, 85 | HOLD | NO — pending evidence |
| Codere | ES | 19 | HOLD | NO — pending evidence |
| ComeOn | SE | 58 | HOLD | NO — pending evidence |
| DrückGlück | DE | 47 | HOLD | NO — pending evidence |
| FDJ | FR | 99 | HOLD | NO — pending evidence |
| Fuego Casino | ES | 26 | HOLD | NO — pending evidence |
| Golden Palace | BE | 84 | HOLD | NO — pending evidence |
| Holland Casino | NL | 65 | HOLD | NO — pending evidence |
| Jack's Casino | NL | 69 | HOLD | NO — pending evidence |
| Jackpotjoy | SE | 63 | HOLD | NO — pending evidence |
| Jokerbet | ES | 30 | HOLD | NO — pending evidence |
| Kansino | NL | 72 | HOLD | NO — pending evidence |
| Kokobet | AU | 1 | HOLD | NO — pending evidence |
| Ladbrokes | BE | 83 | HOLD | NO — pending evidence |
| Legiano | NL | 5 | HOLD | NO — pending evidence |
| LeoVegas | SE | 57 | HOLD | NO — pending evidence |
| Lottomatica | IT | 20 | HOLD | NO — pending evidence |
| Luckia | ES | 28 | HOLD | NO — pending evidence |
| LuckyVegas | ES, DE | 36, 44 | HOLD | NO — pending evidence |
| Luna Casino | ES | 39 | HOLD | NO — pending evidence |
| Maria Casino | SE | 59 | HOLD | NO — pending evidence |
| Metal Casino | ES | 38 | HOLD | NO — pending evidence |
| Millioner | IT | 8 | HOLD | NO — pending evidence |
| Monopoly Casino | ES | 24 | HOLD | NO — pending evidence |
| Mr Green | DE, SE | 50, 60 | HOLD | NO — pending evidence |
| MrPunter | GB, US-New Jersey | 3, 12 | HOLD | NO — pending evidence |
| Napoleon | BE | 21, 77 | HOLD | NO — pending evidence |
| NetBet | FR | 95 | HOLD | NO — pending evidence |
| NordicBet | SE | 61 | HOLD | NO — pending evidence |
| OneCasino | NL | 71 | HOLD | NO — pending evidence |
| Paf | SE | 53 | HOLD | NO — pending evidence |
| ParionsSport | FR | 93 | HOLD | NO — pending evidence |
| Platin Casino | ES | 25 | HOLD | NO — pending evidence |
| PlayKasino | ES | 37 | HOLD | NO — pending evidence |
| PlayOJO | DE | 46 | HOLD | NO — pending evidence |
| PlayUZU | ES | 41 | HOLD | NO — pending evidence |
| PMU | FR | 94 | HOLD | NO — pending evidence |
| PokerStars | FR | 92 | HOLD | NO — pending evidence |
| PrimeCasino | ES | 35 | HOLD | NO — pending evidence |
| SGCasino | SE | 6 | HOLD | NO — pending evidence |
| Slingo | ES | 42 | HOLD | NO — pending evidence |
| Slotmagie | DE | 51 | HOLD | NO — pending evidence |
| SlotStars | ES | 34 | HOLD | NO — pending evidence |
| SpinGenie | ES, DE | 40, 45 | HOLD | NO — pending evidence |
| StarCasino | BE | 80 | HOLD | NO — pending evidence |
| Svenska Spel | SE | 18, 56 | RESEARCHING; HOLD | NO — pending evidence |
| Tipico | DE | 16 | HOLD | NO — pending evidence |
| TOTO Casino | NL | 66 | HOLD | NO — pending evidence |
| Unibet | NL, SE, BE, FR | 17, 55, 67, 82, 91 | HOLD | NO — pending evidence |
| VBet | NL, BE, FR | 76, 88, 98 | HOLD | NO — pending evidence |
| Versus | ES | 31 | HOLD | NO — pending evidence |
| VideoSlots | ES | 23 | HOLD | NO — pending evidence |
| William Hill | GB | 15 | RESEARCHING | NO — pending evidence |
| Winamax | FR | 90 | HOLD | NO — pending evidence |
| Wunderino | DE | 52 | HOLD | NO — pending evidence |
| ZEbet | FR | 97 | HOLD | NO — pending evidence |

## Rules
1. Do not count a brand as verified from a candidate name, affiliate relationship or competitor listing.
2. Keep separate market/operator records under one global brand when the brand is genuinely the same.
3. Keep product variants separate only where they are distinct user-facing products; do not let product pages inflate the global-brand count.
4. If an exact local product is unauthorized or cannot be established, mark EXCLUDE or HOLD for that market.
5. Only APPROVED/PUBLISHED reviews count toward the 100-review goal; current tracker confirms none.
6. Before launch, attach regulator record, official domain, current terms, cashier/withdrawal evidence, games, safety/privacy/support, image rights, score rationale, editor approval and final URL to each approved record.
