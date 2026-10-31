#!/usr/bin/env python3
"""Dutch and German guides with hreflang pairs to the English originals. Idempotent.

  python3 scripts/build_localized.py && python3 scripts/site_chrome.py
"""
from __future__ import annotations
import html, json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import site_chrome as sc  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
e = html.escape
DATE = "2026-10-31"
BASE = "https://beincasinos.online"

L = {
 "nl": dict(lang="nl", eyebrow="Gids", h_faq="Veelgestelde vragen", h_src="Officiële bronnen", back="← Alle Nederlandse gidsen", hub="/nl/", related="Gerelateerd", read="Leestijd 5 minuten",
            note="Algemene informatie, geen juridisch of financieel advies. Regels veranderen; controleer altijd de officiële bron. Gokken is alleen voor volwassenen (18+) en kan verslavend zijn. Hulp vind je bij je huisarts of bij Jellinek."),
 "de": dict(lang="de", eyebrow="Ratgeber", h_faq="Häufige Fragen", h_src="Offizielle Quellen", back="← Alle deutschen Ratgeber", hub="/de/", related="Verwandt", read="5 Minuten Lesezeit",
            note="Allgemeine Informationen, keine Rechts- oder Finanzberatung. Regeln ändern sich; prüfe immer die offizielle Quelle. Glücksspiel ist nur für Erwachsene (18+) und kann süchtig machen. Hilfe gibt es bei der BZgA (check-dein-spiel.de) und bei lokalen Beratungsstellen."),
}
KSA = ("Kansspelautoriteit (KSA)", "https://kansspelautoriteit.nl/")
CRUKS = ("Cruks", "https://cruks.nl/")
GGL = ("Gemeinsame Glücksspielbehörde der Länder (GGL)", "https://www.gluecksspiel-behoerde.de/")
BZGA = ("BZgA: check-dein-spiel.de", "https://www.check-dein-spiel.de/")

PAGES = [
dict(loc="nl", slug="legale-online-casinos-nederland", en="/guides/online-casinos-netherlands-legal-ksa/",
 title="Legale online casino's in Nederland: KSA-vergunning",
 desc="Online casino's mogen in Nederland alleen met een KSA-vergunning. Zo controleer je een aanbieder, het domein en de bescherming die je hoort te krijgen.",
 lede="Sinds 1 oktober 2021 mag een online casino in Nederland alleen aanbieden met een vergunning van de Kansspelautoriteit (KSA). Zo controleer je dat in een paar minuten.",
 sections=[("De wet in het kort", ["De Wet kansspelen op afstand (Koa) maakte online casinospellen legaal voor aanbieders met een vergunning. De KSA geeft de vergunningen af en houdt toezicht. Zonder vergunning mag een aanbieder zich niet op de Nederlandse markt richten.", "Een logo van een vergunning op een website bewijst niets. Alleen het officiële register van de toezichthouder telt."]),
 ("Zo controleer je een aanbieder", [("ul", ["Zoek de naam van het bedrijf in de algemene voorwaarden van het casino.", "Open het register van vergunninghouders op de website van de KSA en zoek dat bedrijf.", "Controleer dat het exacte domein waarop je speelt bij de aanbieder staat.", "Controleer dat het product (casino) onder de vergunning valt.", "Vind je het bedrijf of het domein niet? Stort dan niet."])]),
 ("Welke bescherming hoor je te zien", ["Vergunde aanbieders moeten spelers de mogelijkheid geven limieten in te stellen, moeten aansluiten op Cruks, het centrale register voor uitsluiting, en moeten verantwoord spelen actief ondersteunen. Ze moeten ook je leeftijd en identiteit controleren voordat je kunt spelen.", "Bij een klacht kun je eerst terecht bij de aanbieder en daarna bij een erkende geschillencommissie. Buiten het Nederlandse systeem is die route zwakker."]),
 ("Waar je op moet letten", [("ul", ["Een casino zonder Nederlandse vergunning dat toch Nederlandse spelers accepteert.", "Beloftes van “geen verificatie” of “geen limieten”.", "Een domein dat niet in het register staat.", "Een bedrijfsnaam in de voorwaarden die niet overeenkomt met de vergunninghouder."])]),
 ("Wat de vergunning niet zegt", ["Een vergunning betekent dat de aanbieder gereguleerd is. Het zegt niet dat uitbetalingen altijd snel gaan of dat de bonus gunstig is. Lees de voorwaarden en kijk altijd naar het moment waarop het materiaal is gecontroleerd."])],
 faq=[("Zijn online casino's legaal in Nederland?", "Ja, maar alleen met een vergunning van de Kansspelautoriteit. Controleer het register van vergunninghouders."), ("Wat is Cruks?", "Het Centraal Register Uitsluiting Kansspelen. Vergunde aanbieders moeten het raadplegen voordat iemand mag spelen."), ("Is een buitenlandse vergunning genoeg?", "Nee. Wie zich op de Nederlandse markt richt, heeft een Nederlandse vergunning nodig."), ("Moet ik belasting betalen over winst?", "De regels hangen af van je situatie. Kijk voor actuele informatie bij de Belastingdienst.")],
 sources=[KSA, CRUKS], related=[("/nl/cruks-zelfuitsluiting-uitleg/", "Cruks uitgelegd"), ("/nl/bonusvoorwaarden-uitleg/", "Bonusvoorwaarden uitgelegd"), ("/reviews/", "Onze reviews (Engels)")]),
dict(loc="nl", slug="cruks-zelfuitsluiting-uitleg", en="/guides/cruks-self-exclusion-netherlands-explained/",
 title="Cruks uitgelegd: jezelf uitsluiten van online gokken",
 desc="Cruks is het centrale register om jezelf uit te sluiten van kansspelen in Nederland. Lees hoe het werkt, wat het dekt en waar je hulp vindt.",
 lede="Met één inschrijving in Cruks sluit je jezelf uit bij alle vergunde aanbieders van online kansspelen in Nederland.",
 sections=[("Wat is Cruks?", ["Cruks staat voor Centraal Register Uitsluiting Kansspelen. Vergunde aanbieders van online casino's moeten het register raadplegen voordat iemand mag spelen. Staat iemand ingeschreven, dan mag de aanbieder die persoon niet laten spelen."]),
 ("Zo werkt het", ["Je kunt jezelf inschrijven via de officiële website van Cruks. Je kiest zelf hoe lang de uitsluiting geldt, binnen de regels die op de website staan. Controleer daar altijd de actuele minimale duur en de voorwaarden om de uitsluiting te beëindigen.", "Omdat de uitsluiting voor alle vergunde aanbieders geldt, hoef je niet bij elke aanbieder apart iets te doen."]),
 ("Wat Cruks niet doet", ["Cruks werkt alleen waar aanbieders verplicht zijn het register te raadplegen. Een casino zonder Nederlandse vergunning hoeft dat niet. Daarom is het belangrijk geen alternatieve sites te zoeken.", "Cruks neemt het verlangen om te gokken ook niet weg. Overweeg daarom extra stappen."]),
 ("Aanvullende stappen", [("ul", ["Verwijder opgeslagen betaalgegevens en zet reclame-e-mails van aanbieders uit.", "Gebruik blokkeringssoftware op je telefoon en computer.", "Praat met iemand die je vertrouwt.", "Neem contact op met je huisarts of met Jellinek voor professionele hulp."])]),
 ("Hulp voor naasten", ["Ook als je je zorgen maakt over iemand anders is er hulp. Begin bij de huisarts of bij een verslavingszorginstelling en zorg ook goed voor jezelf."])],
 faq=[("Is Cruks gratis?", "Ja. Inschrijven bij Cruks kost niets."), ("Geldt Cruks ook voor buitenlandse sites?", "Nee. Het geldt voor vergunde aanbieders in Nederland."), ("Kan ik me snel weer uitschrijven?", "Dat hangt af van de regels. Lees de voorwaarden op de officiële website voordat je je inschrijft.")],
 sources=[CRUKS, KSA], related=[("/nl/legale-online-casinos-nederland/", "Legale online casino's"), ("/nl/bonusvoorwaarden-uitleg/", "Bonusvoorwaarden uitgelegd"), ("/responsible-gambling/", "Safer gambling (Engels)")]),
dict(loc="nl", slug="bonusvoorwaarden-uitleg", en="/guides/what-wagering-requirements-mean/",
 title="Casinobonus en omzetvoorwaarden uitgelegd",
 desc="Wat zijn omzetvoorwaarden bij een casinobonus? Leer rekenen met een omzetfactor, maximale inzet, looptijd en maximale uitbetaling voordat je een bonus accepteert.",
 lede="Een bonus klinkt aantrekkelijk, maar de voorwaarden bepalen wat hij waard is. Lees deze vijf punten voordat je accepteert.",
 sections=[("Wat is een omzetvoorwaarde?", ["Een omzetvoorwaarde bepaalt hoeveel je moet inzetten voordat bonusgeld of de winst daarvan uitbetaald kan worden. Bij een bonus van 100 euro met een omzetfactor van 35 moet je in totaal 3.500 euro inzetten."]),
 ("De vijf punten", [("ul", ["Waarover geldt de omzetfactor: alleen de bonus of storting plus bonus?", "Hoe lang heb je de tijd?", "Wat is de maximale inzet per spin of hand zolang de bonus actief is?", "Tellen alle spellen volledig mee?", "Is er een maximum aan wat je mag uitbetalen?"])]),
 ("Zelf narekenen", ["Vermenigvuldig het bedrag waarop de factor geldt met de omzetfactor. Gebruik onze gratis rekentool (in het Engels) om dit snel te doen en om te zien wat de bonus gemiddeld kost."]),
 ("Je hoeft een bonus niet te nemen", ["Je kunt elke bonus weigeren. Wie zonder bonus speelt, heeft geen omzetvoorwaarde en geen maximale inzet. Stel altijd een limiet in en speel alleen met geld dat je kunt missen."]),
 ("Let op de regels in Nederland", ["Voor vergunde aanbieders gelden aanvullende regels voor reclame en bonussen. Het aanbod en de regels veranderen, dus controleer altijd de actuele voorwaarden op de website van de aanbieder en de informatie van de KSA."])],
 faq=[("Wat is een omzetfactor?", "Het aantal keer dat je het genoemde bedrag moet inzetten."), ("Is een lagere omzetfactor altijd beter?", "Meestal wel, maar kijk ook naar de maximale inzet, de looptijd en de maximale uitbetaling."), ("Tellen alle spellen mee?", "Niet altijd. Veel aanbieders laten live spellen weinig of niet meetellen.")],
 sources=[KSA], related=[("/tools/bonus-value-calculator/", "Bonus value calculator (Engels)"), ("/tools/wagering-calculator/", "Wagering calculator (Engels)"), ("/nl/legale-online-casinos-nederland/", "Legale online casino's")]),
dict(loc="de", slug="legale-online-casinos-deutschland", en="/guides/legal-online-casinos-germany-ggl/",
 title="Legale Online-Casinos in Deutschland: GGL-Lizenz prüfen",
 desc="Seit dem Glücksspielstaatsvertrag 2021 brauchen Online-Slots eine deutsche Lizenz. So prüfst du Anbieter, Whitelist, Einzahlungslimit und Spielerschutz.",
 lede="Seit dem 1. Juli 2021 dürfen virtuelle Automatenspiele und Online-Poker in Deutschland nur mit deutscher Erlaubnis angeboten werden. So prüfst du das.",
 sections=[("Die Rechtslage in Kürze", ["Der Glücksspielstaatsvertrag 2021 regelt Online-Glücksspiel bundesweit. Die Gemeinsame Glücksspielbehörde der Länder (GGL) erteilt Erlaubnisse und führt eine Liste der zugelassenen Anbieter (Whitelist). Ein Logo auf der Webseite beweist nichts; entscheidend ist die offizielle Liste."]),
 ("So prüfst du einen Anbieter", [("ul", ["Suche den Firmennamen in den Allgemeinen Geschäftsbedingungen.", "Finde das Unternehmen in der Whitelist der GGL.", "Prüfe, dass die genaue Domain, auf der du spielst, zum Anbieter gehört.", "Prüfe, dass das Produkt (zum Beispiel virtuelle Automatenspiele) erlaubt ist.", "Findest du Firma, Domain oder Produkt nicht, zahle nicht ein."])]),
 ("Regeln, die Spieler spüren", [("ul", ["Ein anbieterübergreifendes Einzahlungslimit, das über das System LUGAS geprüft wird (in der Regel 1.000 Euro pro Monat).", "Eine Einsatzgrenze von 1 Euro pro Spin bei virtuellen Automatenspielen und eine Mindestdauer pro Spiel von fünf Sekunden.", "Keine Autoplay-Funktion bei Automatenspielen.", "Anbindung an das Spielersperrsystem OASIS."]), "Einzelheiten ändern sich. Prüfe die aktuellen Werte bei der GGL."]),
 ("Nicht lizenzierte Anbieter", ["Wer sich an Spieler in Deutschland richtet, braucht eine deutsche Erlaubnis. Eine Lizenz aus einem anderen Land ersetzt sie für die erfassten Produkte nicht. Bei nicht lizenzierten Anbietern gelten Limits, Sperrsystem und Beschwerdewege nicht in der gleichen Weise."]),
 ("Was die Lizenz nicht sagt", ["Eine Lizenz zeigt, dass der Anbieter reguliert ist. Sie sagt nichts über die Auszahlungsgeschwindigkeit oder den Wert eines Bonus. Lies die Bedingungen und achte auf das Prüfdatum."])],
 faq=[("Sind Online-Casinos in Deutschland legal?", "Ja, wenn der Anbieter für das jeweilige Produkt eine deutsche Erlaubnis hat. Prüfe die Whitelist der GGL."), ("Was ist OASIS?", "Das zentrale Spielersperrsystem. Lizenzierte Anbieter müssen es abfragen."), ("Gilt eine Malta-Lizenz in Deutschland?", "Nein. Sie ersetzt die deutsche Erlaubnis für die erfassten Produkte nicht."), ("Wie hoch ist das Einzahlungslimit?", "In der Regel 1.000 Euro im Monat über alle Anbieter. Prüfe die aktuellen Regeln bei der GGL.")],
 sources=[GGL, BZGA], related=[("/de/oasis-sperrsystem-erklaert/", "OASIS erklärt"), ("/de/bonusbedingungen-umsatzbedingungen-erklaert/", "Bonusbedingungen erklärt"), ("/reviews/", "Unsere Reviews (Englisch)")]),
dict(loc="de", slug="oasis-sperrsystem-erklaert", en="/guides/legal-online-casinos-germany-ggl/", pair=False,
 title="OASIS-Sperrsystem erklärt: So sperrst du dich selbst",
 desc="OASIS ist das bundesweite Spielersperrsystem. Erfahre, wie die Selbstsperre funktioniert, was sie abdeckt und wo du Hilfe bekommst.",
 lede="Mit einer Sperre im System OASIS bist du bei allen lizenzierten Anbietern in Deutschland gesperrt.",
 sections=[("Was ist OASIS?", ["OASIS ist das übergreifende Sperrsystem für Glücksspiel in Deutschland. Lizenzierte Anbieter müssen vor jedem Spiel abfragen, ob eine Sperre vorliegt. Ist das der Fall, darf der Anbieter dich nicht spielen lassen."]),
 ("So funktioniert die Selbstsperre", ["Du kannst dich selbst sperren lassen, zum Beispiel über einen lizenzierten Anbieter oder die dafür vorgesehenen Stellen. Die Mindestdauer und die Bedingungen für die Aufhebung findest du bei der GGL und den Landesbehörden. Prüfe diese vor der Sperre, denn sie sind bewusst nicht kurzfristig umkehrbar."]),
 ("Grenzen der Sperre", ["OASIS wirkt nur bei Anbietern, die daran angeschlossen sind. Bei nicht lizenzierten Seiten gibt es diesen Schutz nicht. Suche deshalb keine Alternativen.", "Die Sperre nimmt den Drang zu spielen nicht weg. Ergänze sie mit weiteren Schritten."]),
 ("Weitere Schritte", [("ul", ["Gespeicherte Zahlungsdaten entfernen und Werbe-E-Mails abbestellen.", "Sperrsoftware auf Handy und Computer nutzen.", "Mit einer Vertrauensperson sprechen.", "Beratung nutzen, etwa über check-dein-spiel.de der BZgA oder lokale Beratungsstellen."])]),
 ("Hilfe für Angehörige", ["Auch wenn du dir Sorgen um jemand anderen machst, gibt es Beratung. Achte dabei auch auf dich selbst."])],
 faq=[("Ist die Selbstsperre kostenlos?", "Ja."), ("Gilt die Sperre für alle Anbieter?", "Für alle lizenzierten Anbieter, die an OASIS angeschlossen sind."), ("Kann ich die Sperre schnell aufheben?", "Das ist bewusst erschwert. Lies vorher die Bedingungen.")],
 sources=[GGL, BZGA], related=[("/de/legale-online-casinos-deutschland/", "Legale Online-Casinos"), ("/de/bonusbedingungen-umsatzbedingungen-erklaert/", "Bonusbedingungen erklärt"), ("/responsible-gambling/", "Safer gambling (Englisch)")]),
dict(loc="de", slug="bonusbedingungen-umsatzbedingungen-erklaert", en="/guides/what-wagering-requirements-mean/",
 title="Casino-Bonus: Umsatzbedingungen einfach erklärt",
 desc="Was bedeuten Umsatzbedingungen bei einem Casino-Bonus? So rechnest du mit dem Umsatzfaktor und prüfst Maximaleinsatz, Laufzeit und Auszahlungslimit.",
 lede="Ein Bonus klingt gut, aber die Bedingungen bestimmen seinen Wert. Prüfe diese fünf Punkte, bevor du annimmst.",
 sections=[("Was sind Umsatzbedingungen?", ["Eine Umsatzbedingung legt fest, wie viel du einsetzen musst, bevor Bonusgeld oder daraus erzielte Gewinne ausgezahlt werden können. Bei 100 Euro Bonus und Faktor 35 musst du insgesamt 3.500 Euro umsetzen."]),
 ("Die fünf Punkte", [("ul", ["Worauf gilt der Faktor: nur auf den Bonus oder auf Einzahlung plus Bonus?", "Wie lange hast du Zeit?", "Wie hoch ist der Maximaleinsatz pro Spiel, solange der Bonus aktiv ist?", "Zählen alle Spiele voll?", "Gibt es eine Obergrenze für die Auszahlung?"])]),
 ("Selbst nachrechnen", ["Multipliziere den Betrag, auf den der Faktor gilt, mit dem Umsatzfaktor. Mit unserem kostenlosen Rechner (auf Englisch) siehst du schnell, was der Bonus im Schnitt kostet."]),
 ("Du musst keinen Bonus nehmen", ["Du kannst jeden Bonus ablehnen. Ohne Bonus gibt es keine Umsatzbedingung und keinen Maximaleinsatz. Setze immer ein Limit und spiele nur mit Geld, das du entbehren kannst."]),
 ("Beachte die deutschen Regeln", ["Für lizenzierte Anbieter gelten in Deutschland besondere Regeln, etwa für Einsatzhöhe und Spielgeschwindigkeit. Angebote und Regeln ändern sich. Prüfe deshalb die aktuellen Bedingungen auf der Seite des Anbieters und die Informationen der GGL."])],
 faq=[("Was ist ein Umsatzfaktor?", "Wie oft du den genannten Betrag einsetzen musst."), ("Ist ein niedrigerer Faktor immer besser?", "Meistens ja, aber achte auch auf Maximaleinsatz, Laufzeit und Auszahlungslimit."), ("Zählen alle Spiele?", "Nicht immer. Live-Spiele zählen oft wenig oder gar nicht.")],
 sources=[GGL], related=[("/tools/bonus-value-calculator/", "Bonus-Rechner (Englisch)"), ("/tools/wagering-calculator/", "Wagering-Rechner (Englisch)"), ("/de/legale-online-casinos-deutschland/", "Legale Online-Casinos")]),
]
HUBS = {"nl": ("Online casino's in Nederland: gidsen en uitleg", "Gidsen over legale online casino's, Cruks en bonusvoorwaarden in Nederland. Onafhankelijk en met links naar officiële bronnen.", "Gidsen voor Nederland", "Duidelijke uitleg over vergunningen, uitsluiting en bonusvoorwaarden, met links naar de officiële bron."),
        "de": ("Online-Casinos in Deutschland: Ratgeber und Erklärungen", "Ratgeber zu legalen Online-Casinos, OASIS und Bonusbedingungen in Deutschland. Unabhängig und mit Links zu offiziellen Quellen.", "Ratgeber für Deutschland", "Klare Erklärungen zu Lizenzen, Sperrsystem und Bonusbedingungen, mit Links zu den offiziellen Quellen.")}


def head(lang, url, title, desc, extra="", alts=""):
    t = f"{title} | BeInCasinos"
    return (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<meta name="description" content="{e(desc)}"><title>{e(t)}</title><link rel="icon" href="/favicon.svg" type="image/svg+xml">'
            f'<link rel="canonical" href="{url}">{alts}<meta property="og:type" content="article"><meta property="og:title" content="{e(t)}">'
            f'<meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{url}"><meta name="twitter:card" content="summary">'
            f'<meta name="twitter:title" content="{e(t)}"><meta name="twitter:description" content="{e(desc)}"><meta name="color-scheme" content="light dark">{extra}{sc.HEAD_LINKS}</head>')


def page(p):
    c = L[p["loc"]]
    url = f"{BASE}/{p['loc']}/{p['slug']}/"
    en = BASE + p["en"]
    alts = f'<link rel="alternate" hreflang="{c["lang"]}" href="{url}"><link rel="alternate" hreflang="en" href="{en}">' if p.get("pair", True) else ""
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]]}
    art = {"@context": "https://schema.org", "@type": "Article", "headline": p["title"], "description": p["desc"], "datePublished": DATE, "dateModified": DATE, "inLanguage": c["lang"],
           "mainEntityOfPage": {"@type": "WebPage", "@id": url}, "author": {"@type": "Organization", "name": "BeInCasinos", "url": BASE + "/about/"}, "publisher": {"@type": "Organization", "name": "BeInCasinos", "url": BASE + "/"}}
    ld = "".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False, separators=(",", ":"))}</script>' for x in (art, faq))
    body = []
    for h, parts in p["sections"]:
        body.append(f"<h2>{e(h)}</h2>")
        for x in parts:
            body.append("<ul>" + "".join(f"<li>{e(i)}</li>" for i in x[1]) + "</ul>" if isinstance(x, tuple) else f"<p>{e(x)}</p>")
    body.append(f"<h2>{c['h_faq']}</h2>" + "".join(f"<h3>{e(q)}</h3><p>{e(a)}</p>" for q, a in p["faq"]))
    body.append(f"<h2>{c['h_src']}</h2><ul>" + "".join(f'<li><a href="{e(u)}" rel="noopener noreferrer">{e(l)}</a></li>' for l, u in p["sources"]) + "</ul>")
    body.append(f'<p class="site-note">{e(c["note"])}</p><p><a href="{c["hub"]}">{c["back"]}</a></p><p><a href="{p["en"]}" hreflang="en" lang="en">English version →</a></p>')
    side = "".join(f'<a href="{u}">{e(l)}</a>' for u, l in p["related"])
    return (head(c["lang"], url, p["title"], p["desc"], ld, alts) + f'<body><a class="skip-link" href="#main">Skip to content</a>{sc.header(p["loc"] + "/" + p["slug"] + "/")}<main id="main">'
            f'<section class="page-hero"><div class="wrap"><p class="eyebrow">{c["eyebrow"]} · {c["read"]}</p><h1>{e(p["title"])}</h1><p>{e(p["lede"])}</p></div></section>'
            f'<div class="wrap content-layout"><article class="prose">{"".join(body)}</article><aside class="sidebar"><b>{c["related"]}</b>{side}</aside></div></main>'
            f'{sc.FOOTER}<script src="/script.js?v={sc.VERSION}" defer></script></body></html>')


def hub(loc):
    c = L[loc]; title, desc, h1, lede = HUBS[loc]
    url = f"{BASE}/{loc}/"
    cards = "".join(f'<a class="tool-card" href="/{loc}/{p["slug"]}/"><h2>{e(p["title"])}</h2><p>{e(p["desc"])}</p></a>' for p in PAGES if p["loc"] == loc)
    return (head(c["lang"], url, title, desc) + f'<body><a class="skip-link" href="#main">Skip to content</a>{sc.header(loc + "/")}<main id="main">'
            f'<section class="page-hero"><div class="wrap"><p class="eyebrow">{c["eyebrow"]}</p><h1>{e(h1)}</h1><p>{e(lede)}</p></div></section>'
            f'<section class="wrap"><div class="tool-grid">{cards}</div><p><a href="/guides/">English guides →</a></p></section></main>{sc.FOOTER}<script src="/script.js?v={sc.VERSION}" defer></script></body></html>')


def main():
    for p in PAGES:
        d = ROOT / p["loc"] / p["slug"]; d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(page(p), encoding="utf-8")
    for loc in ("nl", "de"):
        (ROOT / loc).mkdir(exist_ok=True)
        (ROOT / loc / "index.html").write_text(hub(loc), encoding="utf-8")
    # hreflang on the English originals (pairs that are true equivalents)
    pairs = {}
    for p in [x for x in PAGES if x.get("pair", True)]:
        pairs.setdefault(p["en"], []).append((p["loc"], f"{BASE}/{p['loc']}/{p['slug']}/"))
    for en, alts in pairs.items():
        f = ROOT / en.strip("/") / "index.html"
        t = f.read_text(encoding="utf-8")
        t = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">', "", t)
        tags = f'<link rel="alternate" hreflang="en" href="{BASE}{en}">' + "".join(f'<link rel="alternate" hreflang="{l}" href="{u}">' for l, u in alts)
        t = t.replace("</head>", tags + "</head>", 1)
        f.write_text(t, encoding="utf-8")
    sm = ROOT / "sitemap.xml"; s = sm.read_text(encoding="utf-8")
    locs = [f"{BASE}/nl/", f"{BASE}/de/"] + [f"{BASE}/{p['loc']}/{p['slug']}/" for p in PAGES]
    for u in locs:
        if f"<loc>{u}</loc>" not in s:
            s = s.replace("</urlset>", f"  <url>\n    <loc>{u}</loc>\n    <lastmod>{DATE}</lastmod></url>\n</urlset>")
    sm.write_text(s, encoding="utf-8")
    print(len(PAGES) + 2, "localized pages")


if __name__ == "__main__":
    main()
