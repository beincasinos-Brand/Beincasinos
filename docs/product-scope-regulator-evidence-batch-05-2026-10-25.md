# Product-scope regulator evidence — batch 05 — 25 October 2026

**Purpose:** Record fresh official-source findings for DE, SE, BE and FR. These are legal/product-scope leads, not player reviews, endorsements or public scores.

## Germany (DE): GGL whitelist distinguishes game categories

Official source: https://www.gluecksspiel-behoerde.de/de/fuer-spielende/uebersicht-erlaubter-anbieter-whitelist

The GGL page says the whitelist is the official list under § 9(8) GlüStV 2021 of gambling organisers/intermediaries with a permit or concession. It has separate categories, including sports betting, virtual slot games, online poker, online horse betting, state lotteries, land-based casino games and online casino games. The source displayed **“last updated 02.10.2026”** when checked.

Examples directly visible in the fetched official whitelist:
- **Aurora Alea A/S — jollie.de — virtual slot games**; first permit date displayed as 28 September 2026.
- **Bet-at-home.com Internet Limited — bet-at-home.de — sports betting and virtual slot games**; distinct permit records/dates shown.
- **Betkick Sportsbetting Limited — betano.de — sports betting and virtual slot games**; distinct permit records/dates shown.
- **Betway Limited — betway.de — sports betting and virtual slot games**; virtual slot entry displayed first permit date 2 October 2026.

**Important:** This is evidence that these named domain/product combinations appear in the German official whitelist as fetched. It does not establish authorisation for every game type, every corporate domain, or other countries. Capture the current whitelist entry and product filter at publication time. Never infer online casino table-game permission from a virtual-slot listing.

## Sweden (SE): official directory includes licences, permits and URLs

Official source: https://www.spelinspektionen.se/en/licence-and-permit/licence-and-permit-directory/

The Swedish Gambling Authority describes its directory as a list of licensees/permit holders; the Swedish-language regulator page states that active licences/permits include gambling venues and website addresses. The English directory provides downloads for the gambling operators and search results.

**Workflow for each SE candidate:** search exact legal entity and brand, export the current result, capture all listed domains, confirm licence category and status, then match the domain to the live consumer site. The page extraction did not expose the underlying result rows, so this batch does not claim any individual brand was matched to an active Swedish licence. No brand-specific SE clearance is recorded yet.

## Belgium (BE): supplementary online licences

Official source: https://www.gamingcommission.be/en/online-gambling

The Belgian Gaming Commission explains that it uses a supplementary-licence system: existing gambling establishments already licensed for real-world gambling can apply for an additional internet licence. This is a meaningful gate; a general offshore licence or an online brand name alone is not enough.

**Workflow for each BE candidate:** match the exact domain to the Gaming Commission's current operator register; capture the legal operator, underlying licence and supplementary online licence/category; verify the exact permitted product. Do not publish “Belgium licensed” based on a foreign licence or on the brand’s presence in another country.

## France (FR): authorised online categories are product-specific

Official source: https://anj.fr/offre-de-jeu-et-marche/operateurs-agrees

The ANJ page's current authorised-operator list shows product categories for each website. Examples visible in the fetched list:
- **betclic.fr** — sports betting, horse betting and circle games.
- **pokerstars.fr / pokerstarsmobile.fr / betstars.fr / pokerstarssports.fr** — sports betting and circle games.
- **bet365.fr** — sports betting, horse betting and circle games.
- **bwin.fr / partypoker.fr** — sports betting and circle games.

The page does not list these as general online casino slot/table-game authorisations. France's market gate must therefore distinguish authorised sports betting / horse betting / circle games from online casino games. Do not create a French “online casino” recommendation or use a casino score where the relevant product is not legally authorised.

## Score and publication implications

- Eligibility gate comes before the 100-point score.
- Exact consumer domain + operator + jurisdiction + product permission must match.
- An official regulator record verifies only its stated scope, not withdrawal reliability, bonus value, game fairness beyond the regulator's remit, customer service, or editorial quality.
- A licence/whitelist row is not proof that a bonus is current or that a payment test was performed.
- When a required gate is unresolved, retain **“Not rated — verification incomplete”** and explain the missing evidence.
- This is an internal document only. It does not change public profile text, public scores, sitemap, robots.txt or deployment.

## Official source URLs
- Germany GGL whitelist: https://www.gluecksspiel-behoerde.de/de/fuer-spielende/uebersicht-erlaubter-anbieter-whitelist
- Sweden Spelinspektionen directory: https://www.spelinspektionen.se/en/licence-and-permit/licence-and-permit-directory/
- Belgium Gaming Commission online gambling: https://www.gamingcommission.be/en/online-gambling
- France ANJ authorised operators: https://anj.fr/offre-de-jeu-et-marche/operateurs-agrees
- Google Search Central people-first content guidance: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
