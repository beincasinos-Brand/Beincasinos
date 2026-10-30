"""20 commercial-intent guides. Facts are limited to well-established, checkable rules and always point to the official source.
Each entry: slug, kw (primary query), title (H1), eyebrow, desc, motif, lede, sections[(h2, [paragraph or ('ul',[...])])], faq[(q,a)], sources[(label,url)], related[(url,label)]."""

UKGC = ("UK Gambling Commission public register", "https://www.gamblingcommission.gov.uk/public-register/business/index")
KSA = ("Kansspelautoriteit (KSA)", "https://kansspelautoriteit.nl/")
GGL = ("GGL: Gemeinsame Glücksspielbehörde der Länder", "https://www.gluecksspiel-behoerde.de/")
ESBK = ("ESBK / FGB (Swiss Federal Gaming Board)", "https://www.esbk.admin.ch/")
MGCB = ("Michigan Gaming Control Board", "https://www.michigan.gov/mgcb")
GAMSTOP = ("GAMSTOP", "https://www.gamstop.co.uk/")
IBAS = ("IBAS", "https://www.ibas-uk.com/")
CRUKS = ("Cruks", "https://cruks.nl/")
BGA = ("BeGambleAware", "https://www.begambleaware.org/")

R_LIC = ("/guides/how-to-check-a-casino-licence/", "How to check a casino licence")
R_BON = ("/guides/bonus-terms-explained/", "Bonus terms, explained")
R_WAG = ("/guides/what-wagering-requirements-mean/", "What wagering requirements mean")
R_WD = ("/guides/withdrawal-processing-times/", "Withdrawal processing times")
R_VER = ("/guides/casino-withdrawal-verification-explained/", "Withdrawal verification explained")
R_COMP = ("/guides/how-to-complain-about-a-casino/", "How to complain about a casino")
R_SELF = ("/guides/online-gambling-self-exclusion/", "Self-exclusion and support")
R_RTP = ("/guides/return-to-player-rtp-explained/", "Return to player (RTP), explained")
R_MAX = ("/guides/maximum-cashout-clauses/", "Maximum cashout clauses")
R_PAY = ("/guides/payment-method-ownership-checks/", "Payment-method ownership checks")
R_BONUSES = ("/bonuses/", "Bonuses we have read")
R_CALC = ("/tools/wagering-calculator/", "Wagering calculator")
R_REV = ("/reviews/", "All reviews")
R_B365 = ("/reviews/bet365-casino-gb/", "bet365 GB review (80/100)")

GUIDES = [
dict(slug="how-to-find-a-legit-online-casino-uk", kw="legit online casino UK", title="How to Find a Legit Online Casino in the UK", eyebrow="UK safety check", motif="shield",
 desc="Five checks to tell whether a UK online casino is legitimately licensed: exact domain, legal entity, UKGC record, product scope and payout terms.",
 lede="“Legit” has a testable meaning in Great Britain: the exact site must be run by an entity that holds a UK Gambling Commission licence covering remote casino. Here is the quick way to test it.",
 sections=[("Why a logo or badge proves nothing", ["Any site can display a licence badge. The only proof is the regulator's own public register. A badge, a footer sentence or a review site saying “licensed” is a pointer, not evidence."]),
 ("The five checks", [("ul", ["Domain: the address you are on must appear against the operator's record (the register lists domain names).", "Legal entity: the terms and conditions name the company that contracts with you. Find the same name on the register.", "Licence type: the record must include remote casino, not only betting or bingo.", "Status: look for an active licence and read any regulatory actions or financial penalties listed.", "Terms: withdrawal rules, bonus conditions and a complaints route should be easy to find."])]),
 ("Where to look", ["Use the Gambling Commission's public register and search by operator or licence account number, which operators must show in the site footer. If the number or company does not match, stop."]),
 ("What a licence does not tell you", ["A licence shows the operator is regulated, not that it is the best value or that every payout will be quick. Regulators also fine licensed operators; read the regulatory history before you decide.", "In our reviews we apply the same five checks and publish the result before any score."]),
 ("Red flags", [("ul", ["No licence number, or one that does not match the company in the terms.", "A domain that is not listed under the operator's record.", "Promises of “no verification” or “no limits”: UK licensees must verify customers and offer safer-gambling tools.", "Pressure to pay by methods that are not in your own name."])])],
 faq=[("How do I know if a UK online casino is licensed?", "Match the exact domain, the legal entity in the terms and the licence number to the UK Gambling Commission public register, and confirm the record includes remote casino."), ("Is a Malta or Curaçao licence enough for UK players?", "To offer gambling to people in Great Britain, an operator needs a Gambling Commission licence. Other licences do not replace it."), ("Does a licence guarantee fast payouts?", "No. It shows regulation, not performance. Read withdrawal terms and complaint routes separately.")],
 sources=[UKGC, BGA], related=[R_LIC, R_COMP, R_B365]),

dict(slug="fastest-withdrawal-casinos-how-to-check", kw="fastest withdrawal casino", title="Fastest Withdrawal Casinos: How to Check Speed Before You Deposit", eyebrow="Payments", motif="clock",
 desc="Fast-payout claims are hard to compare. Learn which published figures matter, which stage causes delays and how to test speed safely before you commit.",
 lede="“Instant withdrawals” is one of the most common casino claims and one of the least comparable. Speed is the sum of several stages, and only some of them are in the operator's control.",
 sections=[("The four stages", [("ul", ["Pending or review period set by the operator.", "Identity and source-of-funds checks, if not completed earlier.", "Dispatch of the payment.", "Settlement by your bank, card scheme or e-wallet."])]),
 ("What to look for on the operator's page", ["A good payments page lists each method with a minimum, a maximum and a processing time. Treat a single headline such as “within minutes” with caution if it does not say which stage it covers or which methods qualify."]),
 ("How method choice changes speed", ["E-wallets and instant bank transfers often settle faster than cards or standard bank transfers, but each operator publishes its own estimates. Withdrawal usually goes back to the method you deposited with, in your own name."]),
 ("Reduce avoidable delay", [("ul", ["Complete identity verification before your first withdrawal request.", "Use a payment method registered in your own name.", "Check any bonus conditions before you request a payout, because an active bonus can restrict withdrawals.", "Keep screenshots of the terms and your request time."])]),
 ("How we treat speed in reviews", ["We record the operator's published times and limits and label them as estimates. We do not claim a payout speed we have not tested. See our reviews for the published figures per method."])],
 faq=[("Which casino has the fastest withdrawals?", "That depends on method, verification status and the operator's current process. We publish stated times per operator and flag them as estimates rather than rank on unverified speed claims."), ("Why was my withdrawal pending?", "Operators may hold a request for review, or ask for verification documents. Check the pending period in the terms."), ("Do e-wallets pay faster than cards?", "Often, but not always; use the operator's published table for your market.")],
 sources=[UKGC], related=[R_WD, R_VER, R_PAY, R_B365]),

dict(slug="no-wagering-free-spins-explained", kw="no wagering free spins", title="No Wagering Free Spins: What They Are and What to Check", eyebrow="Bonus terms", motif="calc",
 desc="No-wagering free spins let you keep winnings without playing them through. Learn what still applies: caps, expiry, eligible games and deposit rules.",
 lede="“No wagering” means the winnings from the spins do not have to be staked a set number of times before withdrawal. It does not mean there are no conditions.",
 sections=[("What “no wagering” removes", ["With a normal bonus, winnings are locked until you stake a multiple of an amount (the wagering requirement). With no-wagering spins, winnings are paid as cash or withdrawable balance without that multiple. Read the offer page to see exactly how the operator words it."]),
 ("What can still apply", [("ul", ["A minimum deposit or a qualifying spend to unlock the spins.", "A claim window and an expiry for the spins themselves.", "A fixed game or stake per spin.", "A maximum amount you can win or withdraw from the spins.", "Verification before payout."])]),
 ("Example of how to read an offer", ["If an offer says 50 free spins with a 10p stake, no wagering and a £10 minimum deposit, then the value of the spins is bounded by the stake and the game's payout structure, and you must meet the deposit rule first. This is an illustration, not a current offer."]),
 ("Why it matters in Great Britain", ["The UK Gambling Commission limits wagering requirements on incentives to 10 times, which has made no-wagering and low-wagering offers more visible. Rules differ elsewhere, so check your market."]),
 ("Where we list real offers", ["Our bonuses page shows offers only after we have read them on the operator's own page, with the date seen and the conditions we could confirm."])],
 faq=[("Are no wagering free spins really free?", "They may still require a deposit, have an expiry and cap winnings. Read the offer page."), ("Can I withdraw free spin winnings immediately?", "Under a true no-wagering offer you can, subject to verification and any stated cap."), ("Is there a limit on winnings?", "Some offers cap them. The cap, if any, is in the terms.")],
 sources=[("UKGC Licence Condition 5.1.1", "https://www.gamblingcommission.gov.uk/licensees-and-businesses/lccp/condition/5-1-1-sr-code")], related=[R_BON, R_WAG, R_BONUSES, R_CALC]),

dict(slug="how-to-compare-casino-welcome-offers", kw="best casino welcome offer", title="How to Compare Casino Welcome Offers: A 7-Point Method", eyebrow="Bonus terms", motif="calc",
 desc="A seven-point method to compare casino welcome offers fairly: value, wagering base, expiry, game rules, stake limits, cashout caps and withdrawal terms.",
 lede="The biggest headline is rarely the best offer. Use the same seven checks on every offer and the comparison becomes clear.",
 sections=[("1. Value actually available", ["Separate the maximum from what you would realistically claim. A “100% up to a large amount” offer only pays 100% of what you deposit."]),
 ("2. Wagering and its base", ["Check the multiple and what it applies to: bonus only, or deposit plus bonus. Use the wagering calculator to turn it into turnover."]),
 ("3. Time limits", ["Note the window to opt in, the days to complete wagering and the expiry of free spins."]),
 ("4. Game contribution and exclusions", ["Slots, table games and live games often contribute differently, and some games are excluded."]),
 ("5. Maximum bet while a bonus is active", ["Breaking a stake limit can void winnings. Find the number before you play."]),
 ("6. Maximum cashout or winnings cap", ["Some offers limit what you can withdraw from bonus winnings."]),
 ("7. Withdrawal conditions", ["Check verification, method rules and any minimum balance. A good offer on a restrictive payout policy is a poor offer."]),
 ("Score your own shortlist", ["Write the seven answers side by side for each offer. If an operator does not state one of them, treat that as a negative until it is clarified."])],
 faq=[("What is the best casino welcome bonus?", "There is no universal best; the best offer for you has terms you can meet comfortably. Compare using the seven points."), ("Should I choose a bigger bonus or lower wagering?", "Run both through the same calculation of turnover required relative to the value you could keep."), ("Are bonuses mandatory?", "No. You can decline any bonus.")],
 sources=[("UKGC Licence Condition 5.1.1", "https://www.gamblingcommission.gov.uk/licensees-and-businesses/lccp/condition/5-1-1-sr-code")], related=[R_BON, R_WAG, R_MAX, R_BONUSES]),

dict(slug="online-casinos-netherlands-legal-ksa", kw="legaal online casino Nederland", title="Legal Online Casinos in the Netherlands: How to Check KSA Licences", eyebrow="Netherlands", motif="doc",
 desc="Online casino games are regulated in the Netherlands by the Kansspelautoriteit. See how to check a KSA permit, Cruks, deposit limits and what to avoid.",
 lede="The Dutch online gambling market opened to licensed operators on 1 October 2021 under the Remote Gambling Act. A legal operator needs a permit from the Kansspelautoriteit (KSA).",
 sections=[("The legal test", ["Check that the operator holds a KSA permit for remote casino games, that the legal entity matches the one in the terms, and that the domain is the one the operator uses under that permit."]),
 ("Where to look", ["The KSA publishes information on permit holders and on enforcement decisions. Use it, not an operator's footer, as the source."]),
 ("Player protections you should see", [("ul", ["Registration with Cruks, the central exclusion register, is checked by licensed operators.", "A mandatory deposit limit and tools for time and spending.", "Age rules: 18+ in general, with specific rules on advertising to young adults.", "A formal complaints procedure."])]),
 ("What to avoid", ["Sites without a KSA permit that still accept Dutch players are illegal to market in the Netherlands, and players have no Dutch regulatory protection there."]),
 ("Our Dutch reviews", ["We review KSA-permitted operators market by market and publish the eligibility checks. Open items stay unscored."])],
 faq=[("Are online casinos legal in the Netherlands?", "Yes, when operated under a permit from the Kansspelautoriteit."), ("What is Cruks?", "The Centraal Register Uitsluiting Kansspelen, where you can register to be excluded from gambling."), ("Can I play at foreign casinos from the Netherlands?", "Only licensed ones are lawful to offer there; unlicensed offers carry no Dutch protection.")],
 sources=[KSA, CRUKS], related=[R_LIC, R_SELF, R_REV]),

dict(slug="legal-online-casinos-germany-ggl", kw="legale Online Casinos Deutschland", title="Legal Online Casinos in Germany: GGL Licence, Limits and OASIS", eyebrow="Germany", motif="doc",
 desc="Germany regulates online slots and casino games under the Interstate Treaty. Learn how to check a GGL licence, the whitelist, OASIS and player limits.",
 lede="Since the Interstate Treaty on Gambling took effect on 1 July 2021, online slots and some other casino products can be offered in Germany only with a licence from the GGL (Gemeinsame Glücksspielbehörde der Länder).",
 sections=[("Check the licence and the whitelist", ["The GGL publishes a list of authorised providers and products. Match the operator, the domain and the product, because a licence for one product does not cover another."]),
 ("Rules players notice", [("ul", ["Deposit limit across licensed providers, checked through a central system.", "Reduced stakes per spin on online slots and a pause between spins.", "Participation in the OASIS exclusion system.", "Restrictions on features such as autoplay and some jackpots."]), "Details change; check the GGL for the current numbers."]),
 ("What this means for bonuses", ["Germany's rules shape what operators can offer. Do not assume UK or Malta terms apply."]),
 ("Unlicensed sites", ["Offers without a GGL authorisation for the product are not covered by German player protection."]),
 ("In our reviews", ["For German operators we check the whitelist entry, the legal entity and the terms before scoring."])],
 faq=[("Are online casinos legal in Germany?", "Online slots and certain casino products are legal only with a GGL licence; check the whitelist."), ("What is OASIS?", "The German central self-exclusion system licensed operators must query."), ("Does a Malta licence work in Germany?", "It does not replace a German licence for the products it covers.")],
 sources=[GGL], related=[R_LIC, R_SELF, R_REV]),

dict(slug="swiss-online-casinos-legal-esbk", kw="Online Casino Schweiz legal", title="Swiss Online Casinos: Which Are Legal and How to Check", eyebrow="Switzerland", motif="doc",
 desc="Swiss law lets only licensed casinos offer online games. See how to check an ESBK concession, the blocking list and how foreign sites are treated.",
 lede="In Switzerland, online casino games may be offered only by casinos that hold the right concession, supervised by the Federal Gaming Board (ESBK).",
 sections=[("Who can offer online games", ["The ESBK lists the licensed providers and their online offers. In practice these are Swiss land-based casinos with an online extension."]),
 ("Blocking of foreign sites", ["Under the Money Gaming Act, internet providers block access to unauthorised foreign gambling sites based on a list. A foreign site that is not on the licensed list is not authorised for Swiss players."]),
 ("How to check", [("ul", ["Open the ESBK's list of authorised online casinos.", "Match the brand, domain and the licensed casino named in the terms.", "Read the safer-gambling tools and exclusion options."])]),
 ("Our Swiss reviews", ["We cover Swiss licensed operators and publish each eligibility check. We leave criteria unrated until we have read the operator's own terms."])],
 faq=[("Are online casinos legal in Switzerland?", "Yes, when operated by a casino with an ESBK concession and online authorisation."), ("Can I use foreign casinos from Switzerland?", "Foreign providers without Swiss authorisation can be blocked and offer no Swiss protection.")],
 sources=[ESBK], related=[R_LIC, R_SELF, R_REV]),

dict(slug="michigan-online-casinos-legal-mgcb", kw="legal online casino Michigan", title="Are Online Casinos Legal in Michigan? MGCB Rules Explained", eyebrow="United States", motif="doc",
 desc="Michigan allows online casino games through MGCB-licensed operators for adults 21+ located in the state. See how to verify an operator and what to expect.",
 lede="Michigan regulates internet gaming under the Lawful Internet Gaming Act. Operators are licensed by the Michigan Gaming Control Board (MGCB) and serve adults located in Michigan.",
 sections=[("Check the operator", ["The MGCB publishes the list of licensed internet gaming operators and platform providers. Match the brand to the licensed entity."]),
 ("Rules players notice", [("ul", ["Players must be 21 or older.", "Geolocation confirms that you are physically in Michigan.", "Operators must offer responsible gaming tools and self-exclusion."])]),
 ("State by state", ["US online casino law is state-specific. A licence in one state does not authorise play in another, so we review each state separately."]),
 ("Offshore sites", ["Sites that are not on the MGCB's list are not licensed in Michigan and the MGCB has taken action against illegal operators."])],
 faq=[("What age do you have to be to play online casino in Michigan?", "21."), ("Can I play if I travel outside Michigan?", "No. Geolocation confirms you are in the state."), ("How do I check if a Michigan casino is legal?", "Check the MGCB's list of licensed operators.")],
 sources=[MGCB], related=[R_LIC, R_SELF, R_REV]),

dict(slug="paypal-casinos-withdrawals-what-to-check", kw="PayPal casino withdrawals", title="PayPal Casinos: What to Check Before You Use PayPal", eyebrow="Payments", motif="clock",
 desc="PayPal is a popular casino payment method. Check availability, limits, fees, withdrawal rules and the bonus exclusions that often apply.",
 lede="Many players prefer PayPal for speed and separation from their bank account. Availability and rules vary by operator and country.",
 sections=[("Is it offered in your market?", ["Operators choose their methods per country. Look at the payments page for your market, not a global page."]),
 ("Limits and processing times", ["Check minimum deposit, minimum and maximum withdrawal and the stated processing time. Treat times as estimates."]),
 ("Bonus exclusions", ["Some offers exclude certain e-wallets from qualifying deposits. Read the offer conditions before depositing."]),
 ("Withdraw to the same account", ["Operators generally return funds to the method you used and require it to be in your own name."]),
 ("Alternatives", ["Debit cards, bank transfer and instant bank payments are other options; compare limits and times for each."])],
 faq=[("Do PayPal casino withdrawals take longer?", "Often they are among the faster methods, but the operator's own estimate and verification status decide."), ("Can I claim a bonus with PayPal?", "Only if the offer terms allow it.")],
 sources=[UKGC], related=[R_WD, R_PAY, R_B365]),

dict(slug="casino-withdrawal-methods-compared", kw="casino withdrawal methods", title="Casino Withdrawal Methods Compared: Card, Bank, E-wallet", eyebrow="Payments", motif="clock",
 desc="Compare debit card, bank transfer, e-wallet and instant bank payments for casino withdrawals: speed, limits, fees and what to check in each.",
 lede="The method you choose changes the limit, the timing and sometimes the fee. Compare these factors rather than the headline claim.",
 sections=[("Debit card", ["Widely accepted. Funds return to the card you deposited with, and bank settlement can add days."]),
 ("Bank transfer", ["Often the highest maximum, sometimes slower. Check the name on the account matches yours."]),
 ("E-wallets", ["Commonly quicker to settle, with their own limits and sometimes bonus exclusions."]),
 ("Instant bank payments", ["Payments initiated from your bank can be fast and are usually returned to the same account."]),
 ("A simple comparison table in your head", [("ul", ["Minimum and maximum amounts", "Published processing time", "Fees (operator and provider)", "Name-on-account rule", "Bonus eligibility"])])],
 faq=[("What is the best way to withdraw from an online casino?", "The one with limits, times and fees that suit you and that the operator states clearly for your market."), ("Why must I withdraw to the same method?", "Operators follow anti-money-laundering rules and generally return funds to the original method.")],
 sources=[UKGC], related=[R_WD, R_PAY, R_VER]),

dict(slug="casino-kyc-documents-what-to-expect", kw="casino KYC verification documents", title="Casino KYC: Which Documents You Will Be Asked For and Why", eyebrow="Verification", motif="doc",
 desc="Licensed casinos must verify identity. See typical documents, why checks happen at withdrawal, and how to submit them safely and avoid delays.",
 lede="Verification is a legal requirement for licensed operators, not an optional extra. Knowing what to expect avoids the most common withdrawal delay.",
 sections=[("Typical documents", [("ul", ["Photo ID such as a passport or driving licence.", "Proof of address such as a recent utility bill or bank statement.", "Proof of the payment method, for example a card or account statement with some details hidden.", "In some cases, evidence of source of funds."])]),
 ("Why it often happens at withdrawal", ["Operators may request documents when you first withdraw or when thresholds are reached. Doing it earlier removes delay."]),
 ("Submit safely", ["Use the official upload area inside your account, not email attachments to an unknown address. Never send documents to anyone who contacts you first."]),
 ("If your documents are refused", ["Ask which requirement was not met and keep the conversation in writing. If unresolved, see our complaint guide."])],
 faq=[("Why does a casino ask for ID?", "Licensed operators must verify age and identity and comply with anti-money-laundering rules."), ("Can a casino refuse to pay while verifying?", "Terms usually allow holding withdrawals until checks are complete.")],
 sources=[UKGC], related=[R_VER, R_PAY, R_COMP]),

dict(slug="should-you-claim-a-casino-bonus", kw="should I claim a casino bonus", title="Should You Claim a Casino Bonus? When to Take It and When to Skip It", eyebrow="Bonus terms", motif="calc",
 desc="A bonus is a contract with conditions. Learn when a bonus is worth claiming, when playing without one is simpler and how to decide before you deposit.",
 lede="A bonus adds conditions to your money. Whether it is worth it depends on how comfortable you are with those conditions.",
 sections=[("When a bonus can make sense", [("ul", ["The wagering base and multiple are low and clearly stated.", "You are happy with the eligible games and the stake limit.", "Expiry fits how often you play.", "You can read the full terms and they are fair."])]),
 ("When to skip it", [("ul", ["You may want to withdraw soon, because active bonuses can restrict withdrawals.", "Terms are long, vague or change often.", "A cashout cap makes the potential gain small."]), "You can always decline a bonus or opt out before depositing."]),
 ("A quick test", ["Work out the turnover required with the calculator, and decide whether you would be comfortable playing that much."]),
 ("Remember", ["A bonus is not free money and does not change the odds of the games."])],
 faq=[("Is it better to play without a bonus?", "It keeps withdrawals simple. A bonus can still be fine if you accept the conditions."), ("Can I cancel a bonus?", "Often before you wager; the terms say how and what happens to winnings.")],
 sources=[BGA], related=[R_BON, R_WAG, R_CALC]),

dict(slug="no-deposit-bonus-what-to-know", kw="no deposit casino bonus", title="No Deposit Casino Bonuses: What the Catch Usually Is", eyebrow="Bonus terms", motif="calc",
 desc="No-deposit bonuses let you play without paying first. Check the wagering, caps, verification and expiry that usually come with them.",
 lede="A no-deposit offer gives you something before you pay. In return, the terms are usually tighter.",
 sections=[("What to look for", [("ul", ["Wagering multiple and what it applies to.", "Maximum winnings or cashout cap.", "Expiry of the bonus and of the winnings.", "Eligible games and maximum stake.", "Verification needed before payout."])]),
 ("Why caps exist", ["Operators limit exposure, so the amount you can withdraw is often small."]),
 ("Is it worth it?", ["It can be a low-risk way to try a site if you read the terms. Treat it as a trial, not income."]),
 ("Regional differences", ["Rules on incentives differ by country; in Great Britain wagering is capped at 10 times."])],
 faq=[("Can you win real money with a no deposit bonus?", "Yes, if you meet the terms and any cap, then pass verification."), ("Do no-deposit bonuses require ID?", "Operators generally verify before paying out.")],
 sources=[("UKGC Licence Condition 5.1.1", "https://www.gamblingcommission.gov.uk/licensees-and-businesses/lccp/condition/5-1-1-sr-code")], related=[R_BON, R_MAX, R_BONUSES]),

dict(slug="casino-cashback-bonus-explained", kw="casino cashback bonus", title="Casino Cashback Bonuses Explained: Net Loss, Caps and Wagering", eyebrow="Bonus terms", motif="calc",
 desc="Cashback returns a percentage of losses. Learn how net loss is calculated, whether cashback is cash or bonus money and what caps and conditions apply.",
 lede="Cashback sounds simple, but the definition of “loss”, the period and the form of payment decide its value.",
 sections=[("The three questions", [("ul", ["How is net loss calculated and over what period?", "Is the cashback paid as cash or as bonus money with wagering?", "Is there a minimum loss and a maximum payout?"])]),
 ("Example", ["If a terms page offers 10% weekly cashback on net losses, and your net loss is 100 units, you would receive 10 units. If it is paid as bonus with wagering, those 10 units carry conditions. This is an illustration."]),
 ("Why it is not a safety net", ["Cashback reduces a loss only partly and can encourage extra play. Set limits first."])],
 faq=[("Is cashback better than a deposit bonus?", "It depends on the terms: cash cashback without wagering is simpler than bonus-money cashback."), ("When is cashback paid?", "The terms state the period and the payout day.")],
 sources=[BGA], related=[R_BON, R_WAG, R_BONUSES]),

dict(slug="live-casino-what-to-check", kw="live dealer casino online", title="Live Dealer Casinos: What to Check Before You Play", eyebrow="Games", motif="dice",
 desc="Live dealer games use real studios and presenters. Check table limits, game rules, bonus contribution, studio licensing and safer-gambling tools.",
 lede="Live casino is the same regulated product with a video dealer. The checks are about rules and limits, not about the stream.",
 sections=[("Table limits", ["Every table shows minimum and maximum stakes. Pick one that fits your budget."]),
 ("Rules and payouts", ["Rules differ by variant: for example, blackjack payouts and roulette zero rules change the house edge. Open the rules before you play."]),
 ("Bonus contribution", ["Live games often contribute little or nothing to wagering. Check before you play with a bonus."]),
 ("Licensing", ["Operators must hold the right licence for the product and market. See our licence guide."]),
 ("Control", ["Use deposit and time limits. Live games move quickly, so set limits before you begin."])],
 faq=[("Is live casino fair?", "Licensed operators and studios are regulated and tested, but the house edge still applies."), ("Do live games count for wagering?", "Check the contribution table in the bonus terms.")],
 sources=[UKGC, BGA], related=[R_LIC, R_BON, R_RTP]),

dict(slug="how-to-check-slot-rtp", kw="check slot RTP", title="How to Check a Slot's RTP Before You Play", eyebrow="Games", motif="dice",
 desc="RTP can differ between casinos for the same slot. Find the game's info screen, understand what the percentage means and what volatility adds.",
 lede="Return to player is a long-run theoretical average. Some slots are offered in more than one RTP version, so check the version at your casino.",
 sections=[("Where to find it", ["Open the game's information or help screen. It normally lists the RTP and the rules."]),
 ("Versions", ["Providers can supply several RTP settings, and an operator chooses one. The same title can therefore differ between sites."]),
 ("What the number means", ["96% does not mean you receive 96 for every 100 staked in a session. It describes the long-run average over a very large number of plays."]),
 ("Volatility", ["Volatility describes how uneven the results are. Two slots with the same RTP can feel very different."]),
 ("Use it carefully", ["RTP helps compare games; it does not predict your result. Set limits regardless."])],
 faq=[("Where do I find a slot's RTP?", "In the game information screen, not usually on the lobby tile."), ("Is a higher RTP better?", "In theory it loses less over the long run, but results in short sessions vary widely.")],
 sources=[BGA], related=[R_RTP, ("/guides/rtp-vs-volatility/", "RTP vs volatility")]),

dict(slug="can-a-casino-confiscate-winnings", kw="casino confiscated winnings", title="Can a Casino Confiscate Your Winnings? Common Reasons and Your Options", eyebrow="Complaints", motif="scales",
 desc="Operators may void winnings for rule breaches such as bonus abuse, duplicate accounts or false details. Learn the common reasons and what to do if you disagree.",
 lede="Terms allow an operator to void winnings in specific cases. Whether a particular decision is fair depends on the clause relied on and the evidence.",
 sections=[("Common stated reasons", [("ul", ["Breaking a maximum-bet rule while a bonus was active.", "More than one account or shared household or device issues.", "Incorrect or false registration details.", "Playing from a restricted country or using a location bypass.", "Malfunction clauses where a game error caused a payout."])]),
 ("Ask for the clause", ["Request in writing which term was applied and what evidence the operator holds."]),
 ("Keep evidence", ["Save terms, screenshots, chat logs and timestamps."]),
 ("Escalation", ["Use the operator's complaint procedure, then the independent dispute body for your market."]),
 ("Prevention", ["Read stake limits and eligibility before you play, and provide accurate details."])],
 faq=[("Why was my casino win cancelled?", "Operators cite specific terms. Ask which one and see whether it applies."), ("What can I do if I think it was unfair?", "Complain formally, then use the independent dispute service for your market.")],
 sources=[UKGC, IBAS], related=[R_COMP, R_MAX, R_PAY]),

dict(slug="ibas-casino-complaints-uk", kw="IBAS casino complaint", title="IBAS: How to Escalate a UK Casino Complaint", eyebrow="Complaints", motif="scales",
 desc="IBAS is a free alternative dispute resolution service for many UK-licensed gambling operators. Learn when you can use it and what evidence to prepare.",
 lede="If you cannot resolve a complaint with a UK-licensed operator, an independent service can review it. IBAS is one of the approved providers.",
 sections=[("When you can use it", [("ul", ["You have complained to the operator first.", "The operator has given a final response, or eight weeks have passed without resolution.", "The operator participates in the scheme."])]),
 ("What to prepare", [("ul", ["Account details and a timeline.", "Copies of the terms in force at the time.", "Screenshots and communications.", "Your desired outcome."])]),
 ("What it can and cannot do", ["An adjudicator reviews the evidence and issues a decision. It is not a court and cannot consider every type of dispute."]),
 ("Other routes", ["Other approved ADR providers exist; the operator's terms name the one that applies."])],
 faq=[("Is IBAS free?", "It is free for players."), ("How long before I can go to IBAS?", "After the operator's final response or eight weeks without resolution, according to the typical route.")],
 sources=[IBAS, UKGC], related=[R_COMP, ("/guides/alternative-dispute-resolution-gambling/", "Alternative dispute resolution")]),

dict(slug="gamstop-self-exclusion-explained", kw="GAMSTOP self exclusion", title="GAMSTOP Explained: Free Self-Exclusion for UK Online Gambling", eyebrow="Safer gambling", motif="shield",
 desc="GAMSTOP is a free UK service that blocks you from online gambling with licensed sites. Learn how it works, the periods available and extra support.",
 lede="GAMSTOP lets you exclude yourself in one step from online gambling companies licensed in Great Britain.",
 sections=[("How it works", ["You register once, choose a period, and licensed operators must stop marketing to you and prevent you from opening or using accounts."]),
 ("Periods", ["You choose a fixed period. When it ends, you can ask to be removed only after the period has expired."]),
 ("Limits to know", ["It covers GB-licensed sites, not offshore ones, and it does not block land-based venues. Consider pairing it with blocking software for devices."]),
 ("Get support", ["If gambling is causing harm, free confidential help is available from services such as BeGambleAware and GamCare."])],
 faq=[("Is GAMSTOP free?", "Yes."), ("Does it cover all sites?", "It covers online gambling companies licensed in Great Britain.")],
 sources=[GAMSTOP, BGA], related=[R_SELF, R_COMP]),

dict(slug="cruks-self-exclusion-netherlands-explained", kw="Cruks registreren", title="Cruks Explained: Self-Exclusion for Online Gambling in the Netherlands", eyebrow="Safer gambling", motif="shield",
 desc="Cruks is the Dutch central exclusion register. Learn how registration works, the exclusion periods, and how licensed operators must check it.",
 lede="Cruks is the Centraal Register Uitsluiting Kansspelen. Registered people are excluded from online gambling with licensed Dutch operators and from many land-based venues.",
 sections=[("How registration works", ["You can register yourself, and in some cases a third party or a court can request registration. Licensed operators must check Cruks before letting you play."]),
 ("Periods", ["Exclusion periods start at six months and can be much longer."]),
 ("What it does not cover", ["It covers the regulated Dutch market. Unlicensed sites are outside it, which is why checking the licence matters."]),
 ("Support", ["If you want help, Dutch addiction care and helplines are available; ask your GP or find them via the KSA."])],
 faq=[("What is Cruks?", "The Dutch central register to exclude yourself from gambling."), ("Do licensed operators check it?", "Yes, they must.")],
 sources=[CRUKS, KSA], related=[R_SELF, R_LIC]),
]
