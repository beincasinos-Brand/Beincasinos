#!/usr/bin/env python3
"""Build free calculators from the wagering-calculator page shell, plus the /tools/ hub. Idempotent.

  python3 scripts/build_tools.py && python3 scripts/site_chrome.py
"""
from __future__ import annotations
import html, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
e = html.escape
SHELL = (ROOT / "tools/wagering-calculator/index.html").read_text(encoding="utf-8")
DATE = "2026-10-31"
DISC = ('<p class="fineprint">Educational illustration based on theoretical averages. It is not advice, a prediction or a way to make money. '
        'Gambling is for adults (18+, 21+ in some US states) and can be addictive. <a href="/responsible-gambling/">Find support</a>.</p>')

TOOLS = [
dict(slug="bonus-value-calculator", name="Casino bonus value calculator", short="Work out what a bonus is really worth after wagering",
 title="Casino Bonus Value Calculator: Is the Bonus Worth It?",
 desc="Enter the deposit, bonus percentage, wagering multiple and game RTP to see the turnover required and the theoretical cost of clearing a casino bonus.",
 hero="Enter the offer's terms to see the turnover you must stake and the average cost of doing it. The result is a theoretical average, not a forecast of what you will win or lose.",
 fields=[("deposit","Deposit","number","100",'min="0" step="1"'),("pct","Bonus match (%)","number","100",'min="0" step="1"'),("cap","Maximum bonus (0 = no cap)","number","200",'min="0" step="1"'),
         ("wr","Wagering multiple (×)","number","35",'min="0" step="0.5"'),("rtp","Average RTP of the games you will play (%)","number","96",'min="50" max="100" step="0.1"')],
 selects=[("base","Multiple applies to",[("b","Bonus only"),("db","Deposit + bonus")])],
 outs=[("o1","Bonus received"),("o2","Required turnover"),("o3","Theoretical cost of wagering"),("o4","Theoretical average result")],
 js='''
 var d=n('deposit'),p=n('pct'),c=n('cap'),w=n('wr'),r=n('rtp'),base=document.getElementById('base').value;
 if([d,p,c,w,r].some(function(x){return !isFinite(x)||x<0})||r<50||r>100)return null;
 var b=d*p/100; if(c>0&&b>c)b=c;
 var t=(base==='b'?b:d+b)*w, cost=t*(1-r/100), net=b-cost;
 return [money(b),money(t),money(cost),(net>=0?'+':'−')+money(Math.abs(net))];''',
 explain=[("How the calculation works","<strong>Bonus = deposit × match %, limited by the cap. Turnover = (bonus or deposit + bonus) × wagering multiple. Theoretical cost = turnover × (1 − RTP).</strong> The average result is the bonus minus that cost. A positive figure means the bonus is worth more than the theoretical cost of clearing it; a negative figure means that on average it costs more than it gives."),
  ("Why it is only an average","RTP describes the long run over very large numbers of bets. In a single session you can finish far above or below the figure. Game contribution, maximum-bet rules, expiry, and a cap on withdrawable winnings are not modelled here, and they can change the outcome a lot."),
  ("What a negative result tells you","It does not mean the offer is a trap, only that the arithmetic is unfavourable at that RTP. Offers with a low multiple, a bonus-only base and a high-RTP eligible game score best. You can always decline a bonus.")],
 faq=[("Is a casino bonus ever worth it?","Sometimes, when the multiple is low, it applies to the bonus only, the games you enjoy count in full and there is no tiny cashout cap. This calculator lets you test that with real numbers."),
  ("What RTP should I enter?","Use the RTP shown in the game's information screen. If you are unsure, enter a typical figure such as 96, and check the sensitivity by trying 94 and 98."),
  ("Does the calculator include the max cashout?","No. If the terms cap what you can withdraw from bonus winnings, the real value can be lower than shown."),
  ("Does a higher wagering multiple always mean a worse bonus?","Usually, because turnover rises in proportion. Compare offers by running each through the same calculation.")],
 related=[("/tools/wagering-calculator/","Wagering requirement calculator"),("/guides/what-wagering-requirements-mean/","What wagering requirements mean"),("/guides/how-to-compare-casino-welcome-offers/","7-point welcome offer method"),("/bonuses/","Bonuses we have read")]),
dict(slug="house-edge-calculator", name="Expected loss calculator", short="See the average cost of playing for an hour or a session",
 title="Casino House Edge Calculator: Expected Loss Per Session",
 desc="Estimate the theoretical average cost of a gambling session from stake size, speed of play, hours and RTP. Understand why the house edge always adds up.",
 hero="Every game has a built-in edge. Enter your stake, pace and the game's RTP to see what a session costs on average. The point is to understand the price of entertainment, not to find a way around it.",
 fields=[("stake","Average stake per bet","number","1",'min="0" step="0.1"'),("bph","Bets per hour","number","600",'min="0" step="10"'),("hrs","Hours played","number","2",'min="0" step="0.5"'),("rtp","Game RTP (%)","number","96",'min="50" max="100" step="0.1"')],
 selects=[],
 outs=[("o1","Total amount staked"),("o2","House edge"),("o3","Expected loss per hour"),("o4","Expected loss for the session")],
 js='''
 var s=n('stake'),b=n('bph'),h=n('hrs'),r=n('rtp');
 if([s,b,h,r].some(function(x){return !isFinite(x)||x<0})||r<50||r>100)return null;
 var tot=s*b*h, edge=100-r;
 return [money(tot),edge.toFixed(2)+'%',money(tot*edge/100/(h||1)),money(tot*edge/100)];''',
 explain=[("How the calculation works","<strong>Total staked = stake × bets per hour × hours. Expected loss = total staked × house edge, where house edge = 100% − RTP.</strong> A slot at 96% RTP keeps 4% of everything staked, on average. Because staked money is recycled with every spin, the amount staked is much larger than the amount you deposit."),
  ("Why fast games cost more","The edge applies per bet, so the more bets you place per hour, the more it costs. A game with 600 spins an hour at 96% RTP costs far more per hour than a slower game at the same RTP."),
  ("Averages and real sessions","Results vary widely around the average. You may win in a session, but over many sessions the average cost tends to appear. Decide a budget before you play, set a deposit limit and treat the cost as the price of entertainment.")],
 faq=[("What is the house edge?","The share of each stake the game keeps on average, equal to 100% minus the RTP."),
  ("Is expected loss what I will lose?","No. It is a long-run average. A single session can end higher or lower."),
  ("What is a typical RTP?","Slots often list figures from the mid-90s to the high-90s per cent, and European roulette is about 97.3%. Check the game's own information screen."),
  ("Can a strategy reduce the edge?","In some games, such as blackjack, correct play lowers the edge, but it never removes it.")],
 related=[("/guides/return-to-player-rtp-explained/","Return to player (RTP), explained"),("/guides/how-to-check-slot-rtp/","How to check slot RTP"),("/tools/roulette-odds-calculator/","Roulette odds calculator"),("/guides/casino-deposit-limits-how-to-set/","How to set deposit limits")]),
dict(slug="roulette-odds-calculator", name="Roulette odds calculator", short="Probability, payout and house edge for each roulette bet",
 title="Roulette Odds Calculator: European vs American",
 desc="Choose a wheel and a bet to see the chance of winning, the payout, the house edge and the expected loss. Compares European, American and French roulette.",
 hero="Pick a wheel and a bet. The tool shows the true chance of winning, what the bet pays and what it costs on average, which is why every roulette bet has the same edge on a given wheel.",
 fields=[("stake","Stake per spin","number","10",'min="0" step="1"')],
 selects=[("wheel","Wheel",[("37","European (single zero)"),("38","American (double zero)")]),
          ("bet","Bet",[("1","Straight up (1 number)"),("2","Split (2 numbers)"),("3","Street (3 numbers)"),("4","Corner (4 numbers)"),("6","Six line (6 numbers)"),("12","Dozen or column (12 numbers)"),("18","Red / black, odd / even, high / low (18 numbers)")])],
 outs=[("o1","Chance of winning one spin"),("o2","Payout if it wins"),("o3","House edge"),("o4","Expected loss per spin")],
 js='''
 var s=n('stake'),w=Number(document.getElementById('wheel').value),k=Number(document.getElementById('bet').value);
 if(!isFinite(s)||s<0)return null;
 var pay=36/k-1, pr=k/w, edge=(1-(pr*(pay+1)))*100;
 return [(pr*100).toFixed(2)+'%',(Math.round(pay*100)/100)+' to 1',edge.toFixed(2)+'%',money(s*edge/100)];''',
 explain=[("How the calculation works","<strong>Chance = numbers covered ÷ pockets on the wheel. Payout = 36 ÷ numbers covered − 1 (to 1). House edge = 1 − chance × (payout + 1).</strong> A straight-up bet on a 37-pocket wheel wins 1 time in 37 but pays 35 to 1, so on average the casino keeps 2.70% of every stake."),
  ("European or American","The American wheel adds a 00 pocket without changing the payouts, which raises the edge to about 5.26%. Choose a European or French wheel whenever you have the choice."),
  ("No bet is better than another","On a given wheel every standard bet has the same edge, so betting on red, a dozen or a single number changes volatility, not the average cost. No betting system changes the edge, since every spin is independent.")],
 faq=[("What are the odds of winning at roulette?","A single number wins 1 in 37 on a European wheel and 1 in 38 on an American wheel. Outside bets cover more numbers and pay less."),
  ("Which roulette has better odds?","European, because it has one zero instead of two."),
  ("Do roulette systems like Martingale work?","No. They change how wins and losses are distributed but not the house edge, and they can lead to very large losses."),
  ("Does this include La Partage or En Prison?","No. French rules on even-money bets lower the edge on those bets, so check the table rules.")],
 related=[("/guides/european-vs-american-roulette-odds/","European vs American roulette"),("/tools/house-edge-calculator/","Expected loss calculator"),("/guides/return-to-player-rtp-explained/","Return to player explained"),("/responsible-gambling/","Safer gambling")]),
]

JS = '''(()=>{
  const n=id=>{const el=document.getElementById(id);return el.value===''?NaN:Number(el.value)};
  const money=v=>new Intl.NumberFormat('en',{style:'currency',currency:'USD',minimumFractionDigits:2,maximumFractionDigits:2}).format(v);
  const form=document.querySelector('#tool-form'),err=document.querySelector('#calc-error');
  const calc=()=>{const out=(()=>{ %s })();
    if(!out){err.hidden=false;for(let i=1;i<=4;i++)document.getElementById('o'+i).textContent='—';return}
    err.hidden=true;for(let i=0;i<4;i++)document.getElementById('o'+(i+1)).textContent=out[i]};
  form.addEventListener('submit',ev=>{ev.preventDefault();calc()});
  form.querySelectorAll('input,select').forEach(el=>{el.addEventListener('input',calc);el.addEventListener('change',calc)});
  calc();
})();
'''


def page(t: dict) -> str:
    url = f"https://beincasinos.online/tools/{t['slug']}/"
    head, rest = SHELL.split("<main", 1)
    tail = rest.split("</main>", 1)[1]
    head = re.sub(r"<title>.*?</title>", f"<title>{e(t['title'])} | BeInCasinos</title>", head, flags=re.S)
    head = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + e(t["desc"]), head)
    head = re.sub(r'(<link rel="canonical" href=")[^"]*', lambda m: m.group(1) + url, head)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + e(t["title"]) + " | BeInCasinos", head)
    head = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m.group(1) + e(t["desc"]), head)
    head = re.sub(r'(<meta property="og:url" content=")[^"]*', lambda m: m.group(1) + url, head)
    head = re.sub(r'(<meta name="twitter:title" content=")[^"]*', lambda m: m.group(1) + e(t["title"]) + " | BeInCasinos", head)
    head = re.sub(r'(<meta name="twitter:description" content=")[^"]*', lambda m: m.group(1) + e(t["desc"]), head)
    head = head.replace("/tools/wagering-calculator/calculator.css", f"/tools/{t['slug']}/calculator.css")
    ld = ('<script type="application/ld+json">' + __import__("json").dumps({"@context": "https://schema.org", "@type": "WebApplication", "name": t["name"], "url": url,
          "applicationCategory": "EducationalApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}}) + "</script>"
          + '<script type="application/ld+json">' + __import__("json").dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
              {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}) + "</script>")
    head = head.replace("</head>", ld + "</head>", 1)
    fields = "".join(f'<label for="{i}">{e(l)}</label><input id="{i}" name="{i}" type="{ty}" value="{v}" inputmode="decimal" {ex} required>' for i, l, ty, v, ex in t["fields"])
    sels = "".join(f'<label for="{i}">{e(l)}</label><select id="{i}" name="{i}">' + "".join(f'<option value="{v}">{e(x)}</option>' for v, x in o) + "</select>" for i, l, o in t["selects"])
    outs = "".join(f'<span class="result-label">{e(l)}</span><div class="result-number result-sm" id="{i}">—</div>' for i, l in t["outs"])
    expl = "".join(f"<h2>{e(h)}</h2><p>{p}</p>" for h, p in t["explain"])
    faq = "".join(f"<h3>{e(q)}</h3><p>{e(a)}</p>" for q, a in t["faq"])
    rel = "".join(f'<li><a href="{u}">{e(l)}</a></li>' for u, l in t["related"])
    main = (f'<main id="main"><section class="page-hero"><div class="wrap"><p class="eyebrow">Free learning tool</p><h1>{e(t["name"])}</h1><p>{e(t["hero"])}</p></div></section>'
            f'<section class="wrap calculator"><form class="calc-panel" id="tool-form"><h2>Enter the values</h2>{fields}{sels}'
            f'<button class="button button-primary calc-submit" type="submit">Calculate <span aria-hidden="true">→</span></button>'
            f'<p class="fineprint" id="calc-error" role="alert" hidden>Please enter valid values within the limits shown.</p></form>'
            f'<aside class="result-panel" aria-live="polite" aria-atomic="true">{outs}<div class="result-rule"></div>{DISC}</aside></section>'
            f'<section class="wrap calculator-explainer"><div class="prose">{expl}<h2>Common questions</h2>{faq}<h2>Keep learning</h2><ul>{rel}</ul>'
            f'<p class="fineprint">Last reviewed {DATE}.</p></div></section></main>')
    out = head + main + tail
    out = out.replace('<script src="/tools/wagering-calculator/calculator.js" defer>', f'<script src="/tools/{t["slug"]}/calculator.js" defer>')
    return out


def hub() -> str:
    head, rest = SHELL.split("<main", 1)
    tail = rest.split("</main>", 1)[1].replace('<script src="/tools/wagering-calculator/calculator.js" defer></script>', "")
    title, desc = "Free Casino Calculators and Checklists", "Free tools to understand casino bonuses, house edge and roulette odds, plus a terms checklist. Educational, no sign-up."
    url = "https://beincasinos.online/tools/"
    head = re.sub(r"<title>.*?</title>", f"<title>{title} | BeInCasinos</title>", head, flags=re.S)
    for pat, val in [(r'(<meta name="description" content=")[^"]*', desc), (r'(<link rel="canonical" href=")[^"]*', url), (r'(<meta property="og:title" content=")[^"]*', title + ' | BeInCasinos'),
                     (r'(<meta property="og:description" content=")[^"]*', desc), (r'(<meta property="og:url" content=")[^"]*', url),
                     (r'(<meta name="twitter:title" content=")[^"]*', title + ' | BeInCasinos'), (r'(<meta name="twitter:description" content=")[^"]*', desc)]:
        head = re.sub(pat, lambda m, v=val: m.group(1) + v, head)
    head = head.replace('<link rel="stylesheet" href="/tools/wagering-calculator/calculator.css">', "")
    items = [("/tools/wagering-calculator/", "Wagering requirement calculator", "Turn a wagering multiple into the turnover in the terms."),
             ("/tools/bonus-value-calculator/", "Casino bonus value calculator", "See what a bonus is worth after wagering."),
             ("/tools/house-edge-calculator/", "Expected loss calculator", "The average cost of a session from stake, pace and RTP."),
             ("/tools/roulette-odds-calculator/", "Roulette odds calculator", "Chance, payout and edge for every roulette bet."),
             ("/tools/terms-checklist/", "Casino terms checklist", "13 things to read before accepting an offer.")]
    cards = "".join(f'<a class="tool-card" href="{u}"><h2>{e(n)}</h2><p>{e(d)}</p></a>' for u, n, d in items)
    main = ('<main id="main"><section class="page-hero"><div class="wrap"><p class="eyebrow">Free tools</p><h1>Casino calculators and checklists</h1>'
            '<p>Plain-language tools that show the arithmetic behind bonuses, house edge and roulette. They explain; they do not recommend gambling.</p></div></section>'
            f'<section class="wrap"><div class="tool-grid">{cards}</div></section></main>')
    return head + main + tail


def main() -> None:
    for t in TOOLS:
        d = ROOT / "tools" / t["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(page(t), encoding="utf-8")
        (d / "calculator.js").write_text(JS % t["js"], encoding="utf-8")
        (d / "calculator.css").write_text("/* Tool layout lives in /styles.css */\n", encoding="utf-8")
    (ROOT / "tools/index.html").write_text(hub(), encoding="utf-8")
    sm = ROOT / "sitemap.xml"
    s = sm.read_text(encoding="utf-8")
    add = ["tools/"] + [f"tools/{t['slug']}/" for t in TOOLS]
    for p in add:
        loc = f"https://beincasinos.online/{p}"
        if f"<loc>{loc}</loc>" not in s:
            s = s.replace("</urlset>", f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{DATE}</lastmod></url>\n</urlset>")
    sm.write_text(s, encoding="utf-8")
    print("tools built:", len(TOOLS) + 1)


if __name__ == "__main__":
    main()
