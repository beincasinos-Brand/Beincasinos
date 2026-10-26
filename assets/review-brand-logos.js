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
