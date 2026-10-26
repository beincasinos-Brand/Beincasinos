(() => {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#primary-nav');
  if (toggle && nav) {
    const closeMenu = (returnFocus = false) => {
      toggle.setAttribute('aria-expanded', 'false');
      nav.classList.remove('open');
      if (returnFocus) toggle.focus();
    };
    const openMenu = () => {
      toggle.setAttribute('aria-expanded', 'true');
      nav.classList.add('open');
    };
    toggle.setAttribute('aria-controls', nav.id || 'primary-nav');
    toggle.setAttribute('aria-label', 'Toggle main navigation');
    toggle.addEventListener('click', () => {
      const expanded = toggle.getAttribute('aria-expanded') === 'true';
      if (expanded) closeMenu(); else openMenu();
    });
    nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => closeMenu()));
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        closeMenu(true);
      }
    });
    document.addEventListener('click', event => {
      if (toggle.getAttribute('aria-expanded') !== 'true') return;
      if (event.target instanceof Node && !nav.contains(event.target) && !toggle.contains(event.target)) closeMenu();
    });
    window.addEventListener('resize', () => {
      if (window.matchMedia('(min-width: 901px)').matches) closeMenu();
    });
  }
  document.querySelectorAll('[data-year]').forEach(el => { el.textContent = String(new Date().getFullYear()); });

  const reviewSearch = document.querySelector('#review-search');
  const reviewMarket = document.querySelector('#review-market');
  const reviewGrid = document.querySelector('#review-product-grid');
  if (reviewSearch && reviewMarket && reviewGrid) {
    const cards = Array.from(reviewGrid.querySelectorAll('.review-product-card'));
    const count = document.querySelector('#review-results-count');
    const empty = document.querySelector('#review-no-results');
    const update = () => {
      const query = reviewSearch.value.trim().toLocaleLowerCase();
      const market = reviewMarket.value;
      let shown = 0;
      cards.forEach(card => {
        const searchable = (card.dataset.search || '').toLocaleLowerCase();
        const matches = (!query || searchable.includes(query)) &&
          (!market || card.dataset.market === market);
        card.hidden = !matches;
        if (matches) shown += 1;
      });
      if (count) count.textContent = shown + (shown === 1 ? ' profile' : ' profiles');
      if (empty) empty.hidden = shown !== 0;
    };
    reviewSearch.addEventListener('input', update);
    reviewMarket.addEventListener('change', update);
    update();
  }

  // Brand-specific wordmark treatment: deterministic, accessible and never presented as an official logo.
  const brandInitials = (name) => {
    const clean = String(name || '').replace(/\b(review|casino|online|for|in|2026|spain|belgium|switzerland|netherlands|sweden|germany|italy|france|australia|canada|great britain)\b/ig, ' ')
      .replace(/[^A-Za-z0-9 ]/g, ' ').trim().split(/\s+/).filter(Boolean);
    if (!clean.length) return 'BIC';
    return (clean.length > 1 ? clean[0][0] + clean[1][0] : clean[0].slice(0, 2)).toUpperCase();
  };
  const brandHue = (name) => {
    let hash = 0;
    for (const ch of String(name || '')) hash = ((hash << 5) - hash + ch.charCodeAt(0)) | 0;
    return Math.abs(hash) % 360;
  };
  document.querySelectorAll('.review-product-card').forEach(card => {
    const heading = card.querySelector('.review-card-heading h2 a');
    const art = card.querySelector('.review-card-art');
    if (!heading || !art || art.querySelector('.review-card-wordmark')) return;
    const name = heading.textContent.trim();
    const hue = brandHue(name);
    art.style.setProperty('--brand-hue', hue);
    art.querySelectorAll('img').forEach(img => { img.setAttribute('aria-hidden', 'true'); img.alt = ''; });
    const mark = art.querySelector('.review-card-monogram');
    if (mark) mark.textContent = brandInitials(name);
    const logoSources = {
      'OneCasino': { src: 'https://www.onecasino.es/img/website/layout/logo.svg', alt: 'OneCasino official logo' },
      'LuckyCasino': { src: 'https://www.luckycasino.es/img/website/layout/logo.svg', alt: 'LuckyCasino official logo' },
      'Monopoly Casino': { src: 'https://assets.ballys.com/m/4f1e761d8685fd86/original/monopolycasinoes-logo-new.svg', alt: 'Monopoly Casino Spain official logo' },
      'LunaCasino': { src: 'https://www.lunacasino.es/wp-content/uploads/2023/10/Logo.png', alt: 'Luna Casino official logo' },
      'Genting Casino': { src: 'https://www.gentingcasino.es/img/logos/logo.png', alt: 'Genting Casino Spain official logo' },
      'PlayToro': { src: 'https://playtoro.es/uploads/playtoro_logo_horizo.png', alt: 'PlayToro official logo' },
      'PlayUZU': { src: 'https://aws-origin.image-tech-storage.com/tenants/playuzu/playuzu.es/_nuxt/logo.C7q6Stlx.png', alt: 'PlayUZU official logo' },
      'Sportium': { src: 'https://www.sportium.es/library/.customization/preloader_logo_bg.svg?t=1792751723285', alt: 'Sportium official logo' },
      'Botemanía': { src: 'https://assets.ballys.com/m/b722ece616c8555/original/botemaniaes-logo.svg', alt: 'Botemanía official logo' },
      'Enracha': { src: 'https://www.enracha.es/images/logo_negative.svg?ts=en0980', alt: 'enracha official logo' },
      'Juegging': { src: 'https://www.juegging.es/wp-content/uploads/2019/06/logo-juegging-basico-1-300-96-300x96.png', alt: 'Juegging official logo' },
      'LeoVegas': { src: 'https://www.leovegas.es/static/img/brand_logo_on_light_bg_small.svg', alt: 'LeoVegas official logo' },
      'Mr Green': { src: 'https://cgp-cdn.safe-iplay.com/cgp-assets/full/skins/mrgreen/defaults/images/mrgreenlogo.svg', alt: 'Mr Green official logo' },
      'Casino777': { src: 'https://static.casino777.es/site/logo.webp', alt: 'Casino777 Spain official logo' },
      'Codere': { src: 'https://www.codere.es/assets1/logosAndSponsors/logoHalloweenGreen.svg', alt: 'Codere official logo' },
      'Jackpots.ch': { src: 'https://assets.jackpots.ch/jp-content/logo_original_positiv_by_GCB_1_514a6acea2/logo-original-positiv_by_GCB-(1).svg_logo_original_positiv_by_GCB_1_514a6acea2.svg', alt: 'Jackpots.ch official logo' },
      'mycasino.ch': { src: 'https://www.mycasino.ch/_next/static/chunks/mycasino-logo-horizontal-Blx3ovSn.svg', alt: 'mycasino.ch official logo' },
      'Casino777.ch': { src: 'https://www.casino777.ch/assets/img/header/logo.svg?ver=2', alt: 'Casino777 Switzerland official logo' },
      'Swiss4Win': { src: 'https://www.swiss4win.ch/lugano_lugano-theme/images/preloader_logo_bg_black.svg?t=1792749276314', alt: 'Swiss4Win official logo' },
      'TOTO Casino': { src: 'https://www.toto.nl/images/logo-toto.svg', alt: 'TOTO official logo' },
      'Betsson': { src: 'https://www.betsson.com/maintenance-pages/betsson.com/betsson-logo.svg', alt: 'Betsson official logo' },
      'Botemania': { src: 'https://assets.ballys.com/m/b722ece616c8555/original/botemaniaes-logo.svg', alt: 'Botemanía official logo' },
      'Casino777.es': { src: 'https://static.casino777.es/site/logo.webp', alt: 'Casino777 Spain official logo' },
      'Winamax': { src: 'https://operator-front-static-cdn.winamax.fr/img/content/poker/2024/20241104_logo/winamax-logo.png', alt: 'Winamax official logo' },
      'PAF': { src: 'https://www.paf.fi/_next/static/chunks/paf-modern-inverted-CwPlhzaQ.svg', alt: 'Paf official logo' },
      'PlayNow Casino': { src: 'https://www.playnow.com/resources/images/global/logo_PlayNow2-hz.svg?v=1', alt: 'PlayNow official logo' },
    };
    const logo = logoSources[name];
    if (logo && !art.querySelector('.review-card-official-logo')) {
      const logoImage = document.createElement('img');
      logoImage.className = 'review-card-official-logo';
      logoImage.src = logo.src;
      logoImage.alt = logo.alt;
      logoImage.loading = 'lazy';
      logoImage.decoding = 'async';
      logoImage.referrerPolicy = 'no-referrer';
      // Some operator CDNs rotate or block hotlinked assets. Keep the card polished
      // by removing failed images and retaining the branded monogram/wordmark fallback.
      logoImage.addEventListener('error', () => {
        logoImage.remove();
        art.classList.add('review-card-logo-unavailable');
      }, { once: true });
      art.appendChild(logoImage);
    }
    const wordmark = document.createElement('span');
    wordmark.className = 'review-card-wordmark';
    wordmark.textContent = name;
    wordmark.setAttribute('aria-hidden', 'true');
    art.appendChild(wordmark);
  });

  document.querySelectorAll('.casino-card').forEach(card => {
    const brand = card.querySelector('.casino-brand');
    if (!brand) return;
    const name = brand.dataset.brand || brand.textContent.trim();
    brand.setAttribute('aria-label', name + ' brand');
    // Verified operator-logo images take precedence over decorative monograms.
    // If an image fails to load, its accessible label remains and the card layout stays intact.
    if (brand.querySelector('.casino-brand-logo')) return;
    if (brand.querySelector('.casino-brand-mark')) return;
    brand.style.setProperty('--brand-hue', brandHue(name));
    const mark = document.createElement('span');
    mark.className = 'casino-brand-mark';
    mark.setAttribute('aria-hidden', 'true');
    mark.textContent = brandInitials(name);
    brand.prepend(mark);
  });

  // Give every individual review route a visual summary panel while preserving
  // the evidence-led "Not rated" status when hands-on/product evidence is absent.
  const reviewHero = document.querySelector('main .page-hero');
  const reviewHeading = reviewHero && reviewHero.querySelector('h1');
  if (reviewHero && reviewHeading && !document.querySelector('#review-visual-summary') &&
      !/^\/reviews\/?$/.test(window.location.pathname)) {
    const titleText = reviewHeading.textContent.trim();
    const eyebrow = reviewHero.querySelector('.eyebrow');
    const marketText = eyebrow ? eyebrow.textContent.trim() : 'Market-specific research';
    const monogram = titleText.replace(/\s+(review|casino|online|for|in|2026).*/i, '')
      .replace(/[^A-Za-z0-9]/g, '').slice(0, 2).toUpperCase() || 'BIC';
    const summary = document.createElement('section');
    summary.id = 'review-visual-summary';
    summary.className = 'review-visual-summary wrap';
    summary.setAttribute('aria-label', 'Casino review summary');
    summary.innerHTML = '<div class="review-visual-art"><img src="/assets/review-card-art.svg" alt="" width="640" height="260"><span class="review-visual-monogram"></span><span class="review-visual-label">BEINCASINOS · RESEARCH PROFILE</span></div><div class="review-visual-data"><p class="review-visual-kicker">Evidence-led review snapshot</p><h2 class="review-visual-title"></h2><div class="review-visual-status"><span>● Not rated</span><span>Market-specific</span><span>Desk research</span></div><div class="review-visual-metrics"><div class="review-visual-metric"><small>Overall score</small><strong>Pending evidence</strong></div><div class="review-visual-metric"><small>Current bonus</small><strong>Not verified</strong></div><div class="review-visual-metric"><small>Testing status</small><strong>No hands-on test</strong></div></div><p class="review-visual-note">We do not invent a numeric score, promotional amount or product-test claim. “Not rated” means the evidence gates or required criteria are incomplete—not that the casino scored zero.</p><a class="review-visual-method-link" href="/how-we-review/">How our six weighted criteria work →</a></div>';
    summary.querySelector('.review-visual-monogram').textContent = monogram;
    summary.style.setProperty('--brand-hue', brandHue(titleText));
    const visualArt = summary.querySelector('.review-visual-art');
    const visualWordmark = document.createElement('span');
    visualWordmark.className = 'review-visual-wordmark';
    visualWordmark.textContent = titleText.replace(/\s+(review|2026).*/i, '');
    visualWordmark.setAttribute('aria-hidden', 'true');
    visualArt.appendChild(visualWordmark);
    summary.querySelector('.review-visual-title').textContent = titleText;
    const market = summary.querySelector('.review-visual-status span:nth-child(2)');
    market.textContent = marketText;
    reviewHero.insertAdjacentElement('afterend', summary);
  }
})();
