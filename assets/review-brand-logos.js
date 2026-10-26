(() => {
  const logoSources = {
    'Kansino': {
      src: 'https://www.kansino.nl/assets/icons/kansino_mobile.svg',
      alt: 'Kansino official brand mark',
      dark: true
    },
    'Starvegas': {
      src: 'https://starvegas-ch-cdn-static.gt-cdn.net/web_assets/svch/assets/img/logos/main-logo-header.a71ddc3d.svg',
      alt: 'StarVegas official logo',
      dark: true
    },
    'AdmiralBet': {
      src: 'https://admiralbet-es-cdn-static.gt-cdn.net/web_assets/abes/assets/img/favicon/favicon-32x32.050c8b41.png',
      alt: 'AdmiralBet official brand icon',
      icon: true
    },
    'Betway': {
      src: 'https://betway.es/assets/images/icons/favicon-16x16.png',
      alt: 'Betway official brand icon',
      icon: true
    },
    '7melons': {
      src: 'https://7melons.ch/favicon.ico',
      alt: '7Melons official brand icon',
      icon: true
    },
    'Casino777.be': {
      src: 'https://static.casino777.es/site/logo.webp',
      alt: 'Casino777 official logo'
    },
    'Luckia Casino': {
      src: 'https://www.luckiagaminggroup.com/wp-content/uploads/2024/02/Logo-LuckiaGamingGroup_Positivo-1.svg',
      alt: 'Luckia Gaming Group logo'
    },
    'Casino Gran Madrid Online': {
      src: 'https://casinogranmadrid.com/wp-content/uploads/2026/05/Logo-berenjena.png.webp',
      alt: 'Gran Madrid official logo'
    },
    '888casino': {
      src: 'https://www.888.com/content/dam/holdings888/umbrella/com/en/hp/888.com-logo.png',
      alt: '888 official brand logo'
    },
    'William Hill': {
      src: 'https://apps.static-cs.williamhill.com/inter-splash/static/images/16x16.png',
      alt: 'William Hill official brand icon',
      icon: true
    },
    'William Hill Casino': {
      src: 'https://apps.static-cs.williamhill.com/inter-splash/static/images/16x16.png',
      alt: 'William Hill official brand icon',
      icon: true
    },
    'BetMGM Casino': {
      src: 'https://scmedia.nj.betmgm.com/$-$/5ff5107775984e9fbad8eec0b9efb25e.png',
      alt: 'BetMGM official brand icon',
      icon: true
    },
    'BetCity': {
      src: 'https://club.betcity.nl/assets/img/icons/bc-logo-black.svg',
      alt: 'BetCity official logo'
    },
    '44 Aces': {
      src: 'https://44-aces.es/wp-content/themes/44aces-es-theme/assets/images/header/logo-44aces.png',
      alt: '44 Aces official logo'
    },
    'Casino Gran Vía': {
      src: 'https://www.casinogranvia.com/wp-content/uploads/2020/09/LOGO-CGV-2022_web.png',
      alt: 'Casino Gran Vía official logo'
    },
    'SlotsMagic': {
      src: 'https://aws-origin.image-tech-storage.com/tenants/slotsmagic/slotsmagic.com/_nuxt/logo.CFccvnTQ.png',
      alt: 'SlotsMagic official logo'
    },
    'Lapalingo': {
      src: 'https://www.lapalingo.com/build/assets/images/lapalingo-logo-white.svg?a679e571',
      alt: 'Lapalingo official logo',
      dark: true
    },
    'GGPoker': {
      src: 'https://ssl.gg-global-cdn.com/bd/front/img/web/logo/img_GGpoker.webp',
      alt: 'GGPoker official logo'
    },
    'Casineo': {
      src: 'https://casineo.ch/images/casineo-logo.svg',
      alt: 'Casineo official logo'
    },
    'Goldenbull Spain': {
      src: 'https://www.goldenbull.es/_next/static/chunks/goldenbull-horizontal-logo-DxVjO1F7.png',
      alt: 'GoldenBull official logo'
    },
    'Royale500': {
      src: 'https://aws-origin.image-tech-storage.com/tenants/royale500/royale500.com/_nuxt/logo.CoGRaEHp.webp',
      alt: 'Royale500 official logo'
    },
    'Casino Marbella Online': {
      src: 'https://www.casinomarbella.es/library/.customization/preloader_logo_bg.svg?t=1792751684289',
      alt: 'Casino Marbella official logo',
      dark: true
    },
    'OlyBet Spain': {
      src: 'https://welcome.olybet.es/wp-content/uploads/2023/10/logoOlybet.png',
      alt: 'OlyBet official logo'
    },
    'AupaBet': {
      src: 'https://promociones.aupabet.es/wp-content/uploads/2025/08/logoheader.png',
      alt: 'AupaBet official logo'
    },
    'AupaBet Spain': {
      src: 'https://promociones.aupabet.es/wp-content/uploads/2025/08/logoheader.png',
      alt: 'AupaBet official logo'
    },
    'Bingoal': {
      src: 'https://www.bingoal.com/images/favicon/favicon-32x32.png',
      alt: 'Bingoal official brand icon',
      icon: true
    },
    'Holland Casino Online': {
      src: 'https://corporate.hollandcasino.nl/favicon-32x32.png?v=29c351ad98b792041d60ea31c059c3f0',
      alt: 'Holland Casino official brand icon',
      icon: true
    },
    'Lord Lucky': {
      src: 'https://www.lordlucky.com/favicon-32x32.png',
      alt: 'Lord Lucky official brand icon',
      icon: true
    },
    'Solcasino': {
      src: 'https://images.ctfassets.net/yru0bhhzza0c/18pY8VjVhrQbI8e0rH3TTc/d10044d469609e36b250a299844f0f45/logo-solcasino-app-menu-base.svg',
      alt: 'Solcasino official logo',
      dark: true
    },
    'Solcasino Spain': {
      src: 'https://images.ctfassets.net/yru0bhhzza0c/18pY8VjVhrQbI8e0rH3TTc/d10044d469609e36b250a299844f0f45/logo-solcasino-app-menu-base.svg',
      alt: 'Solcasino official logo',
      dark: true
    },
    'LuckyVegas Spain': {
      src: 'https://www.luckyvegas.com/wp-content/uploads/luckyvegas-logo-2.png.webp',
      alt: 'LuckyVegas official logo',
      dark: true
    },
    'PlayKasino Spain': {
      src: 'https://www.playkasino.es/wp-content/uploads/2025/10/Logo-1.png',
      alt: 'PlayKasino official logo'
    },
    'Ahti Games Spain': {
      src: 'https://aws-origin.image-tech-storage.com/tenants/ahtigames/ahtigames.com/_nuxt/logo.Buz4M4Ay.webp',
      alt: 'Ahti Games official logo',
      dark: true
    },
    'GeckoPlay Spain': {
      src: 'https://www.geckoplay.com/logo.webp',
      alt: 'GeckoPlay official logo',
      dark: true
    },
    'BacanaPlay Spain': {
      src: 'https://aws-origin.image-tech-storage.com/tenants/bacanaplay/bacanaplay.es/_nuxt/logo.CNaiE4v1.png',
      alt: 'BacanaPlay official logo',
      dark: true
    },
    'SlotStars Spain': {
      src: 'https://www.slotstars.es/wp-content/uploads/2024/05/Slotstars-Logo.png',
      alt: 'SlotStars official logo'
    },
    'SpinGenie Spain': {
      src: 'https://www.spingenie.com/img/logos/logo.png',
      alt: 'Spin Genie official logo',
      dark: true
    },
    'bet365 Casino': {
      src: 'https://www.bet365.com/favicon.ico',
      alt: 'bet365 official brand icon',
      icon: true
    },
    'PokerStars Casino': {
      src: 'https://www.pokerstars.com/favicon.ico',
      alt: 'PokerStars official brand icon',
      icon: true
    },
    'Lord Ping': {
      src: 'https://www.lordping.com/img/icons/favicon-16x16.png',
      alt: 'Lord Ping official brand icon',
      icon: true
    },
    'Admiral': {
      src: 'https://www.admiral.at/assets/images/favicon/favicon.ico',
      alt: 'Admiral official brand icon',
      icon: true
    },
    'Slingo Casino Spain': {
      src: 'https://cdn.slingo.com/img/logos/logo.png',
      alt: 'Slingo official logo'
    },
    'eBingo Spain': {
      src: 'https://www.ebingo.es/img/header/ebingoLogo.svg',
      alt: 'eBingo official logo'
    },
    'ComeOn Casino': {
      src: 'https://www.comeoncasino.com/wp-content/themes/comeon/vectors/logos/logo.svg',
      alt: 'ComeOn Casino official logo',
      dark: true
    },
    'Lottomatica Casino': {
      src: 'https://commons.wikimedia.org/wiki/Special:FilePath/Lottomatica_Logo.svg',
      alt: 'Lottomatica official logo'
    },
    'PlayNow Casino': {
      src: '/assets/brands/playnow-logo.svg',
      alt: 'PlayNow official logo'
    },
    'Casino777.es': {
      src: 'https://static.casino777.es/site/logo.webp',
      alt: 'Casino777 official logo'
    },
    '888slots': {
      src: 'https://www.888.com/content/dam/holdings888/umbrella/com/en/hp/888.com-logo.png',
      alt: '888 official brand logo'
    },
    'Fuego Casino': {
      src: 'https://s3.eu-central-1.amazonaws.com/www.united-remote.com/logo.svg',
      alt: 'Fuego Casino official logo'
    },
    'Metal Casino': {
      src: 'https://delivery2.objectic.io/jfMYQOLTGWiKB5ocOVpcTH/wI7jjRHhArF0/EkV8i1H1VxMCo5vCZbcH1JfsE73610SZQZ0ZGui1.svg',
      alt: 'Metal Casino official logo'
    },
    'OneCasino': {
      src: 'https://www.onecasino.es/img/website/layout/logo.svg',
      alt: 'OneCasino official logo'
    },
    'LuckyCasino': {
      src: 'https://www.luckycasino.es/img/website/layout/logo.svg',
      alt: 'LuckyCasino official logo'
    },
    'Monopoly Casino': {
      src: 'https://assets.ballys.com/m/4f1e761d8685fd86/original/monopolycasinoes-logo-new.svg',
      alt: 'Monopoly Casino Spain official logo'
    },
    'LunaCasino': {
      src: 'https://www.lunacasino.es/wp-content/uploads/2023/10/Logo.png',
      alt: 'Luna Casino official logo'
    },
    'Genting Casino': {
      src: 'https://www.gentingcasino.es/img/logos/logo.png',
      alt: 'Genting Casino Spain official logo'
    },
    'PlayToro': {
      src: 'https://playtoro.es/uploads/playtoro_logo_horizo.png',
      alt: 'PlayToro official logo'
    },
    'PlayUZU': {
      src: 'https://aws-origin.image-tech-storage.com/tenants/playuzu/playuzu.es/_nuxt/logo.C7q6Stlx.png',
      alt: 'PlayUZU official logo'
    },
    'Sportium': {
      src: 'https://www.sportium.es/library/.customization/preloader_logo_bg.svg?t=1792751723285',
      alt: 'Sportium official logo'
    },
    'Botemanía': {
      src: 'https://assets.ballys.com/m/b722ece616c8555/original/botemaniaes-logo.svg',
      alt: 'Botemanía official logo'
    },
    'Enracha': {
      src: 'https://www.enracha.es/images/logo_negative.svg?ts=en0980',
      alt: 'Enracha official logo'
    },
    'Juegging': {
      src: 'https://www.juegging.es/wp-content/uploads/2019/06/logo-juegging-basico-1-300-96-300x96.png',
      alt: 'Juegging official logo'
    },
    'LeoVegas': {
      src: 'https://www.leovegas.es/static/img/brand_logo_on_light_bg_small.svg',
      alt: 'LeoVegas official logo'
    },
    'Mr Green': {
      src: 'https://cgp-cdn.safe-iplay.com/cgp-assets/full/skins/mrgreen/defaults/images/mrgreenlogo.svg',
      alt: 'Mr Green official logo'
    },
    'Casino777': {
      src: 'https://static.casino777.es/site/logo.webp',
      alt: 'Casino777 Spain official logo'
    },
    'Codere': {
      src: 'https://www.codere.es/assets1/logosAndSponsors/logoHalloweenGreen.svg',
      alt: 'Codere official logo'
    },
    'Jackpots.ch': {
      src: 'https://assets.jackpots.ch/jp-content/logo_original_positiv_by_GCB_1_514a6acea2/logo-original-positiv_by_GCB-(1).svg_logo_original_positiv_by_GCB_1_514a6acea2.svg',
      alt: 'Jackpots.ch official logo'
    },
    'mycasino.ch': {
      src: 'https://www.mycasino.ch/_next/static/chunks/mycasino-logo-horizontal-Blx3ovSn.svg',
      alt: 'mycasino.ch official logo'
    },
    'Casino777.ch': {
      src: 'https://www.casino777.ch/assets/img/header/logo.svg?ver=2',
      alt: 'Casino777 Switzerland official logo'
    },
    'Swiss4Win': {
      src: 'https://www.swiss4win.ch/lugano_lugano-theme/images/preloader_logo_bg_black.svg?t=1792749276314',
      alt: 'Swiss4Win official logo'
    },
    'TOTO Casino': {
      src: 'https://www.toto.nl/images/logo-toto.svg',
      alt: 'TOTO official logo'
    },
    'Betsson': {
      src: 'https://www.betsson.com/maintenance-pages/betsson.com/betsson-logo.svg',
      alt: 'Betsson official logo'
    },
    'Winamax': {
      src: 'https://operator-front-static-cdn.winamax.fr/img/content/poker/2024/20241104_logo/winamax-logo.png',
      alt: 'Winamax official logo'
    },
    'PAF': {
      src: 'https://www.paf.fi/_next/static/chunks/paf-modern-inverted-CwPlhzaQ.svg',
      alt: 'Paf official logo'
    },
    'Casino Barcelona Online': {
      src: 'https://www.casinobarcelona.com/assets/img/casino-barcelona-logo.png?v=9193025',
      alt: 'Casino Barcelona official brand logo'
    }
  };

  document.querySelectorAll('.review-product-card').forEach(card => {
    const heading = card.querySelector('.review-card-heading h2 a');
    const art = card.querySelector('.review-card-art');
    if (!heading || !art || art.querySelector('.review-card-official-logo')) return;
    const logo = logoSources[heading.textContent.trim()];
    if (!logo) return;

    const image = document.createElement('img');
    image.className = 'review-card-official-logo';
    if (logo.dark) image.classList.add('review-card-official-logo--dark');
    if (logo.icon) image.classList.add('review-card-official-logo--icon');
    image.src = logo.src;
    image.alt = logo.alt;
    image.loading = 'lazy';
    image.decoding = 'async';
    image.referrerPolicy = 'no-referrer';
    image.addEventListener('error', () => {
      image.remove();
      art.classList.add('review-card-logo-unavailable');
    });
    art.appendChild(image);
  });
})();
