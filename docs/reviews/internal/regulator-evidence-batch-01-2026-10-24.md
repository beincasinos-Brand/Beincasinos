# Regulator evidence batch — first six candidates
Checked: 2026-10-24
Branch: `ops/2026-10-24-target-reconciliation-and-release-gates`
Scope: primary regulator records only. A regulator record is not a quality rating, not proof of a complete review, and not authorization to publish a bonus claim.

## Findings

1. **bet365 Casino — Great Britain**
   - UK Gambling Commission register: [Hillside (UK Gaming) ENC, account 55149](https://www.gamblingcommission.gov.uk/public-register/business/detail/55149). The current register identifies an active Casino Remote licence; the domain register lists bet365.com as active.
   - Regulatory history: [UKGC settlement, decision 4 April 2024](https://www.gamblingcommission.gov.uk/public-register/regulatory-action/detail/224). The published outcome required £343,035 in lieu of a financial penalty and costs after historic AML and customer-harm-prevention failings.
   - Editorial consequence: include this enforcement record in the evidence log and assess remediation/current controls; do not infer current poor or good quality from the historical action alone.
   - Sources: [licence](https://www.gamblingcommission.gov.uk/public-register/business/detail/55149), [active domain](https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/55149), [settlement](https://www.gamblingcommission.gov.uk/public-register/regulatory-action/detail/224).

2. **Casino777.be — Belgium**
   - Belgian Gaming Commission's [current A+ register](https://data.gamingcommission.be/licenses/APLUS/latest/table.html?lang=en), last updated 8 October 2026, lists casino777.be under Casino de Spa / SA/NV CASINO DE SPA, with expiry 1 January 2032.
   - Editorial consequence: supports the listed domain/operator association in the A+ register; still verify the live customer contract and capture all product/consumer-protection evidence.
   - Source: [Belgian Gaming Commission A+ list](https://data.gamingcommission.be/licenses/APLUS/latest/table.html?lang=en).

3. **ComeOn Casino — Sweden**
   - Swedish Gambling Authority's [URL licence lookup](https://www.spelinspektionen.se/licens-o-tillstand/licensregister/licensurl/?url=comeon.com) lists comeon.com / ComeOn Sweden Ltd with commercial online and commercial betting licences valid 30 October 2025 through 29 October 2030.
   - Editorial consequence: evidence is specific to Sweden; it does not establish permission for other countries or prove service quality.
   - Source: [Spelinspektionen URL lookup](https://www.spelinspektionen.se/licens-o-tillstand/licensregister/licensurl/?url=comeon.com).

4. **TOTO Casino — Netherlands**
   - The Dutch Gambling Authority (Ksa) published a [permit decision for TOTO Online B.V.](https://kansspelautoriteit.nl/vergunning-kansspelen-op-afstand-toto-online-b-v) dated 30 July 2026. It grants a remote-gambling permit for 1 October 2026 through 30 September 2031, including casino games against the licence holder and peer-to-peer casino games.
   - Editorial consequence: update the evidence timeline and reconcile any prior decision-date/appeal notes; confirm the live domain and contracting entity.
   - Source: [Ksa permit decision](https://kansspelautoriteit.nl/vergunning-kansspelen-op-afstand-toto-online-b-v).

5. **MERKUR Spiel — Schleswig-Holstein, Germany**
   - The [GGL/state whitelist](https://www.gluecksspiel-behoerde.de/de/fuer-spielende/uebersicht-erlaubter-anbieter-whitelist) lists merkur-spiel.de for online casino games under Merkur Bets Malta Limited in Schleswig-Holstein, with first permission date 18 September 2024.
   - Editorial consequence: state scope matters. Do not describe this record as nationwide German online-casino authorization.
   - Source: [official whitelist](https://www.gluecksspiel-behoerde.de/de/fuer-spielende/uebersicht-erlaubter-anbieter-whitelist).

6. **Jackpots.ch — Switzerland**
   - The Swiss Federal Gaming Board's [online gambling page](https://www.esbk.admin.ch/en/online-gambling/) lists jackpots.ch as Casino Baden's online offer, operating since 5 July 2019.
   - Editorial consequence: the overview is useful official evidence of the listed offer; still inspect current concession/permit detail and the exact contracting entity before approval.
   - Source: [Swiss Federal Gaming Board](https://www.esbk.admin.ch/en/online-gambling/).

## State after this batch

- Six primary regulator-source checks documented and reflected in the production ledger's blockers/evidence notes.
- These are six source checks, not six completed reviews.
- All six remain **NOT SCORED / HOLD** pending the remaining market-specific terms, payments, bonus, complaints/ADR, safer-gambling, privacy/cookies, accessibility, enforcement and image-rights checks, plus actual test evidence where claimed and independent second-editor sign-off.
- No customer accounts opened, deposits made, gameplay/support/withdrawal tests performed, images copied, public content changed, DNS changed, indexing enabled, merge or production deployment performed.
