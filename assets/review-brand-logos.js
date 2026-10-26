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
    '888slots': {
      src: 'https://www.888.com/content/dam/holdings888/umbrella/com/en/hp/888.com-logo.png',
      alt: '888 official brand logo'
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
