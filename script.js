(() => {
  // Keep featured cards readable when an operator blocks hotlinking or changes its logo URL.
  const installFeaturedLogoFallbacks = () => {
    document.querySelectorAll('.casino-brand .casino-brand-logo').forEach(image => {
      const useFallback = () => {
        const brand = image.closest('.casino-brand');
        if (!brand || brand.classList.contains('logo-unavailable')) return;
        brand.classList.add('logo-unavailable');
        image.remove();
      };
      image.addEventListener('error', useFallback, { once: true });
      if (image.complete && image.naturalWidth === 0) useFallback();
    });
  };
  installFeaturedLogoFallbacks();
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
    // Mark the current internal navigation destination for both visual and
    // assistive-technology context; keep trailing-slash variants equivalent.
    const currentPath = window.location.pathname.replace(/\/+$/, '') || '/';
    nav.querySelectorAll('a[href]').forEach(link => {
      try {
        const target = new URL(link.href, window.location.href);
        const targetPath = target.pathname.replace(/\/+$/, '') || '/';
        if (target.origin === window.location.origin && targetPath === currentPath) {
          link.classList.add('active');
          link.setAttribute('aria-current', 'page');
        }
      } catch (_) {
        // Ignore malformed navigation links rather than blocking menu setup.
      }
    });
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
  const clearReviewFilters = document.querySelector('#review-clear-filters');
  if (reviewSearch && reviewMarket && reviewGrid) {
    const cards = Array.from(reviewGrid.querySelectorAll('.review-product-card'));
    const count = document.querySelector('#review-results-count');
    const empty = document.querySelector('#review-no-results');
    const normalizeSearch = value => String(value || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLocaleLowerCase().replace(/\s+/g, ' ').trim();
    const update = () => {
      const query = normalizeSearch(reviewSearch.value);
      const market = reviewMarket.value;
      let shown = 0;
      cards.forEach(card => {
        const searchable = normalizeSearch((card.dataset.search || '') + ' ' + (card.querySelector('.review-card-heading h2')?.textContent || ''));
        const matches = (!query || searchable.includes(query)) && (!market || card.dataset.market === market);
        card.hidden = !matches;
        if (matches) shown += 1;
      });
      if (count) count.textContent = shown + (shown === 1 ? ' profile' : ' profiles');
      if (empty) empty.hidden = shown !== 0;
      if (clearReviewFilters) clearReviewFilters.disabled = !query && !market;
    };
    reviewSearch.addEventListener('input', update);
    reviewMarket.addEventListener('change', update);
    if (clearReviewFilters) clearReviewFilters.addEventListener('click', () => {
      reviewSearch.value = '';
      reviewMarket.value = '';
      update();
      reviewSearch.focus();
    });
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
  // Review directory brand art is handled by /assets/review-brand-logos.js only.
  // Keeping one owner avoids duplicate external logos and repeated wordmarks.

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
      /^\/reviews\/[^/]+\/?$/.test(window.location.pathname)) {
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
    const displayBrand = titleText.replace(/\s+review.*$/i, '').replace(/:\s*.*$/, '').replace(/\s+2026$/i, '').trim();
    visualWordmark.textContent = displayBrand || titleText;
    visualWordmark.setAttribute('aria-hidden', 'true');
    visualArt.appendChild(visualWordmark);

    // Use a real operator logo only where the site has a known brand-specific source.
    // The branded text treatment remains visible if a remote image fails or is unmapped.
    const visualLogoSources = {
      '888casino': 'https://www.888.com/content/dam/holdings888/umbrella/com/en/hp/888.com-logo.png',
      'Casino777.be': 'https://static.casino777.es/site/logo.webp',
      'Casino777.ch': 'https://www.casino777.ch/assets/img/header/logo.svg?ver=2',
      'Casino777.es': 'https://static.casino777.es/site/logo.webp',
      'Bet365 Casino': 'https://commons.wikimedia.org/wiki/Special:FilePath/Bet365_Logo.svg',
      'bet365 Casino': 'https://commons.wikimedia.org/wiki/Special:FilePath/Bet365_Logo.svg',
      'Holland Casino': 'https://corporate.hollandcasino.nl/favicon-32x32.png?v=29c351ad98b792041d60ea31c059c3f0',
      'ComeOn Casino': 'https://www.comeoncasino.com/wp-content/themes/comeon/vectors/logos/logo.svg',
      'Lottomatica': 'https://commons.wikimedia.org/wiki/Special:FilePath/Lottomatica_Logo.svg',
      'Kansino': 'https://www.kansino.nl/assets/icons/kansino_mobile.svg',
      'BetCity': 'https://club.betcity.nl/assets/img/icons/bc-logo-black.svg',
      'GGPoker': 'https://ssl.gg-global-cdn.com/bd/front/img/web/logo/img_GGpoker.webp',
      'Casineo': 'https://casineo.ch/images/casineo-logo.svg',
      '44 Aces': 'https://44-aces.es/wp-content/themes/44aces-es-theme/assets/images/header/logo-44aces.png',
      'Jackpots.ch': 'https://assets.jackpots.ch/jp-content/logo_original_positiv_by_GCB_1_514a6acea2/logo-original-positiv_by_GCB-(1).svg_logo_original_positiv_by_GCB_1_514a6acea2.svg',
      'mycasino.ch': 'https://www.mycasino.ch/_next/static/chunks/mycasino-logo-horizontal-Blx3ovSn.svg',
      'Swiss4Win': 'https://www.swiss4win.ch/lugano_lugano-theme/images/preloader_logo_bg_black.svg?t=1792749276314',
      'TOTO Casino': 'https://www.toto.nl/images/logo-toto.svg',
      'Betsson': 'https://www.betsson.com/maintenance-pages/betsson.com/betsson-logo.svg',
      'Winamax': 'https://operator-front-static-cdn.winamax.fr/img/content/poker/2024/20241104_logo/winamax-logo.png',
      'PAF': 'https://www.paf.fi/_next/static/chunks/paf-modern-inverted-CwPlhzaQ.svg',
      'PlayNow Casino': 'https://www.playnow.com/resources/images/global/logo_PlayNow2-hz.svg?v=1',
      'Fuego Casino': 'https://s3.eu-central-1.amazonaws.com/www.united-remote.com/logo.svg',
      'Metal Casino': 'https://delivery2.objectic.io/jfMYQOLTGWiKB5ocOVpcTH/wI7jjRHhArF0/EkV8i1H1VxMCo5vCZbcH1JfsE73610SZQZ0ZGui1.svg',
      'OneCasino': 'https://www.onecasino.es/img/website/layout/logo.svg',
      'LuckyCasino': 'https://www.luckycasino.es/img/website/layout/logo.svg',
      'Monopoly Casino': 'https://assets.ballys.com/m/4f1e761d8685fd86/original/monopolycasinoes-logo-new.svg',
      'PlayUZU': 'https://aws-origin.image-tech-storage.com/tenants/playuzu/playuzu.es/_nuxt/logo.C7q6Stlx.png',
      'Sportium': 'https://www.sportium.es/library/.customization/preloader_logo_bg.svg?t=1792751723285',
      'Botemanía': 'https://assets.ballys.com/m/b722ece616c8555/original/botemaniaes-logo.svg',
      'LeoVegas': 'https://www.leovegas.es/static/img/brand_logo_on_light_bg_small.svg',
      'Mr Green': 'https://cgp-cdn.safe-iplay.com/cgp-assets/full/skins/mrgreen/defaults/images/mrgreenlogo.svg',
      'Codere': 'https://www.codere.es/assets1/logosAndSponsors/logoHalloweenGreen.svg',
      'Casino Barcelona': 'https://www.casinobarcelona.com/assets/img/casino-barcelona-logo.png?v=9193025'
      'Starvegas': 'https://starvegas-ch-cdn-static.gt-cdn.net/web_assets/svch/assets/img/logos/main-logo-header.a71ddc3d.svg',
      'AdmiralBet': 'https://admiralbet-es-cdn-static.gt-cdn.net/web_assets/abes/assets/img/favicon/favicon-32x32.050c8b41.png',
      'Betway': 'https://betway.es/assets/images/icons/favicon-16x16.png',
      '7melons': 'https://7melons.ch/favicon.ico',
      'Luckia Casino': 'https://www.luckiagaminggroup.com/wp-content/uploads/2024/02/Logo-LuckiaGamingGroup_Positivo-1.svg',
      'Casino Gran Madrid Online': 'https://casinogranmadrid.com/wp-content/uploads/2026/05/Logo-berenjena.png.webp',
      'William Hill': 'https://apps.static-cs.williamhill.com/inter-splash/static/images/16x16.png',
      'William Hill Casino': 'https://apps.static-cs.williamhill.com/inter-splash/static/images/16x16.png',
      'BetMGM Casino': 'https://scmedia.nj.betmgm.com/$-$/5ff5107775984e9fbad8eec0b9efb25e.png',
      'Casino Gran Vía': 'https://www.casinogranvia.com/wp-content/uploads/2020/09/LOGO-CGV-2022_web.png',
      'SlotsMagic': 'https://aws-origin.image-tech-storage.com/tenants/slotsmagic/slotsmagic.com/_nuxt/logo.CFccvnTQ.png',
      'Lapalingo': 'https://www.lapalingo.com/build/assets/images/lapalingo-logo-white.svg?a679e571',
      'Goldenbull Spain': 'https://www.goldenbull.es/_next/static/chunks/goldenbull-horizontal-logo-DxVjO1F7.png',
      'Royale500': 'https://aws-origin.image-tech-storage.com/tenants/royale500/royale500.com/_nuxt/logo.CoGRaEHp.webp',
      'Casino Marbella Online': 'https://www.casinomarbella.es/library/.customization/preloader_logo_bg.svg?t=1792751684289',
      'OlyBet Spain': 'https://welcome.olybet.es/wp-content/uploads/2023/10/logoOlybet.png',
      'AupaBet': 'https://promociones.aupabet.es/wp-content/uploads/2025/08/logoheader.png',
      'AupaBet Spain': 'https://promociones.aupabet.es/wp-content/uploads/2025/08/logoheader.png',
      'Bingoal': 'https://www.bingoal.com/images/favicon/favicon-32x32.png',
      'Holland Casino Online': 'https://corporate.hollandcasino.nl/favicon-32x32.png?v=29c351ad98b792041d60ea31c059c3f0',
      'Lord Lucky': 'https://www.lordlucky.com/favicon-32x32.png',
      'Solcasino': 'https://images.ctfassets.net/yru0bhhzza0c/18pY8VjVhrQbI8e0rH3TTc/d10044d469609e36b250a299844f0f45/logo-solcasino-app-menu-base.svg',
      'Solcasino Spain': 'https://images.ctfassets.net/yru0bhhzza0c/18pY8VjVhrQbI8e0rH3TTc/d10044d469609e36b250a299844f0f45/logo-solcasino-app-menu-base.svg',
      'LuckyVegas Spain': 'https://www.luckyvegas.com/wp-content/uploads/luckyvegas-logo-2.png.webp',
      'PlayKasino Spain': 'https://www.playkasino.es/wp-content/uploads/2025/10/Logo-1.png',
      'Ahti Games Spain': 'https://aws-origin.image-tech-storage.com/tenants/ahtigames/ahtigames.com/_nuxt/logo.Buz4M4Ay.webp',
      'GeckoPlay Spain': 'https://www.geckoplay.com/logo.webp',
      'BacanaPlay Spain': 'https://aws-origin.image-tech-storage.com/tenants/bacanaplay/bacanaplay.es/_nuxt/logo.CNaiE4v1.png',
      'SlotStars Spain': 'https://www.slotstars.es/wp-content/uploads/2024/05/Slotstars-Logo.png',
      'SpinGenie Spain': 'https://www.spingenie.com/img/logos/logo.png',
      'PokerStars Casino': 'https://www.pokerstars.com/favicon.ico',
      'Lord Ping': 'https://www.lordping.com/img/icons/favicon-16x16.png',
      'Admiral': 'https://www.admiral.at/assets/images/favicon/favicon.ico',
      'Slingo Casino Spain': 'https://cdn.slingo.com/img/logos/logo.png',
      'eBingo Spain': 'https://www.ebingo.es/img/header/ebingoLogo.svg',
      'Lottomatica Casino': 'https://commons.wikimedia.org/wiki/Special:FilePath/Lottomatica_Logo.svg',
      '888slots': 'https://www.888.com/content/dam/holdings888/umbrella/com/en/hp/888.com-logo.png',
      'LunaCasino': 'https://www.lunacasino.es/wp-content/uploads/2023/10/Logo.png',
      'Genting Casino': 'https://www.gentingcasino.es/img/logos/logo.png',
      'PlayToro': 'https://playtoro.es/uploads/playtoro_logo_horizo.png',
      'Enracha': 'https://www.enracha.es/images/logo_negative.svg?ts=en0980',
      'Juegging': 'https://www.juegging.es/wp-content/uploads/2019/06/logo-juegging-basico-1-300-96-300x96.png',
      'Casino777': 'https://static.casino777.es/site/logo.webp',
      'Botemania': 'https://assets.ballys.com/m/b722ece616c8555/original/botemaniaes-logo.svg',
      'Jokerbet': 'https://www.jokerbet.es/img/09.%20Elementos%20web/Aviso/no-disponible/JOKERBET_logotipo-blanco.svg',
      'Marathonbet': 'https://web.mbstatic.org/008AE5/1-356/images/favicon/favicon.svg',
      'Videoslots': 'https://www.videoslots.com/diamondbet/images/mobile/favicon-16x16.png',
      'FairPlay Casino Online': 'https://fairplaycasino.nl/favicons/favicon.ico',
      'Casino Barcelona Online': 'https://www.casinobarcelona.com/assets/img/casino-barcelona-logo.png?v=9193025'
    };
    const normalizeBrandName = value => String(value || '').toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g, '').replace(/[^a-z0-9]/g, '');
    const normalizedDisplayBrand = normalizeBrandName(displayBrand);
    const logoKey = Object.keys(visualLogoSources).find(key => normalizeBrandName(key) === normalizedDisplayBrand)
      || Object.keys(visualLogoSources).find(key => {
        const normalizedKey = normalizeBrandName(key);
        return normalizedKey.length >= 5 && normalizedDisplayBrand.length >= 5
          && (normalizedDisplayBrand.includes(normalizedKey) || normalizedKey.includes(normalizedDisplayBrand));
      });
    // Derive fallback imagery only from the operator domain cited in this review.
    const domainRow = Array.from(document.querySelectorAll('main tr')).find(row =>
      /^(exact domain checked|domain|official website|website)$/i.test((row.cells[0]?.textContent || '').trim())
    );
    let officialUrl = domainRow?.querySelector('a[href]')?.href || '';
    if (!officialUrl) {
      const candidates = Array.from(document.querySelectorAll('main a[rel~="nofollow"][href^="http"]'));
      const excluded = /ordenacionjuego|gamblingcommission|swisscasinos|esbk|egba|gamcare|begambleaware|gamblingtherapy|wikipedia|google\.com\/s2/i;
      officialUrl = candidates.find(a => {
        try { return !excluded.test(new URL(a.href).hostname); } catch (_) { return false; }
      })?.href || '';
    }
    let fallbackFaviconTried = false;
    const addBrandLogo = (src, sourceLabel) => {
      if (!src || visualArt.querySelector('.review-visual-official-logo')) return;
      const logo = document.createElement('img');
      logo.className = 'review-visual-official-logo';
      logo.src = src;
      logo.alt = displayBrand + (sourceLabel ? ' official-site icon' : ' logo');
      logo.loading = 'lazy';
      logo.decoding = 'async';
      logo.referrerPolicy = 'no-referrer';
      logo.addEventListener('error', () => {
        logo.remove();
        if (!sourceLabel && !fallbackFaviconTried) {
          fallbackFaviconTried = true;
          try {
            const domain = new URL(officialUrl).origin;
            addBrandLogo('https://www.google.com/s2/favicons?domain_url=' + encodeURIComponent(domain) + '&sz=128', true);
            return;
          } catch (_) {}
        }
        visualArt.classList.add('review-visual-logo-unavailable');
        const wordmark = document.createElement('span');
        wordmark.className = 'review-visual-wordmark review-visual-wordmark--fallback';
        wordmark.textContent = displayBrand;
        wordmark.setAttribute('aria-label', displayBrand + ' brand name');
        visualArt.appendChild(wordmark);
      }, { once: true });
      visualArt.appendChild(logo);
    };
    if (logoKey) {
      addBrandLogo(visualLogoSources[logoKey], false);
    } else {
      try {
        const domain = new URL(officialUrl).origin;
        addBrandLogo('https://www.google.com/s2/favicons?domain_url=' + encodeURIComponent(domain) + '&sz=128', true);
      } catch (_) {
        visualArt.classList.add('review-visual-logo-unavailable');
        const wordmark = document.createElement('span');
        wordmark.className = 'review-visual-wordmark review-visual-wordmark--fallback';
        wordmark.textContent = displayBrand;
        visualArt.appendChild(wordmark);
      }
    }
    summary.querySelector('.review-visual-title').textContent = titleText;
    const market = summary.querySelector('.review-visual-status span:nth-child(2)');
    market.textContent = marketText;
    reviewHero.insertAdjacentElement('afterend', summary);
  }

  // Shared appearance and language controls are injected into every page that
  // loads this script, keeping navigation consistent without editing each route.
  const root = document.documentElement;
  let savedTheme = null;
  try { savedTheme = window.localStorage.getItem('bic-theme'); } catch (_) {}
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  const applyTheme = theme => {
    const next = theme === 'dark' ? 'dark' : 'light';
    root.setAttribute('data-theme', next);
    const toggle = document.querySelector('[data-theme-toggle]');
    if (toggle) {
      toggle.setAttribute('aria-pressed', String(next === 'dark'));
      toggle.setAttribute('aria-label', next === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
      toggle.innerHTML = next === 'dark'
        ? '<span aria-hidden="true">☀</span><span>Light mode</span>'
        : '<span aria-hidden="true">◐</span><span>Dark mode</span>';
    }
    let themeMeta = document.querySelector('meta[name="theme-color"]');
    if (!themeMeta && document.head) {
      themeMeta = document.createElement('meta');
      themeMeta.name = 'theme-color';
      document.head.appendChild(themeMeta);
    }
    if (themeMeta) themeMeta.setAttribute('content', next === 'dark' ? '#0b1210' : '#174d3e');
  };
  applyTheme(savedTheme || (prefersDark ? 'dark' : 'light'));

  const primaryNav = document.querySelector('#primary-nav');
  if (primaryNav && !primaryNav.querySelector('.site-controls')) {
    const controls = document.createElement('div');
    controls.className = 'site-controls';
    controls.innerHTML = '<button class="theme-toggle" type="button" data-theme-toggle aria-pressed="false"><span aria-hidden="true">◐</span><span>Dark mode</span></button><details class="language-picker"><summary aria-label="Language options">EN ▾</summary><div class="language-menu" role="group" aria-label="Available languages"><p>Site language · English is currently available. Translations are being prepared.</p><span class="language-option" aria-current="true"><span>English</span><span>Current</span></span><span class="language-option" aria-disabled="true"><span>Français</span><span>Coming soon</span></span><span class="language-option" aria-disabled="true"><span>Deutsch</span><span>Coming soon</span></span><span class="language-option" aria-disabled="true"><span>Español</span><span>Coming soon</span></span><span class="language-option" aria-disabled="true"><span>Italiano</span><span>Coming soon</span></span><span class="language-option" aria-disabled="true"><span>Nederlands</span><span>Coming soon</span></span><span class="language-option" aria-disabled="true"><span>Svenska</span><span>Coming soon</span></span></div></details>';
    primaryNav.appendChild(controls);
    applyTheme(root.getAttribute('data-theme') || 'light');
    const picker = controls.querySelector('.language-picker');
    document.addEventListener('click', event => {
      if (picker.open && event.target instanceof Node && !picker.contains(event.target)) picker.open = false;
    });
    picker.addEventListener('keydown', event => {
      if (event.key === 'Escape') { picker.open = false; picker.querySelector('summary').focus(); }
    });
  }
  // Some pages may load a different cached script instance; keep the control
  // wired even if another shared initializer already inserted the controls.
  const themeControl = document.querySelector('[data-theme-toggle]');
  if (themeControl && !themeControl.dataset.bound) {
    themeControl.dataset.bound = 'true';
    themeControl.addEventListener('click', () => {
      const next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      applyTheme(next);
      try { window.localStorage.setItem('bic-theme', next); } catch (_) {}
    });
  }

  // 2026-10-26: ensure every individual review has a consistent operator-image frame.
  if (!document.querySelector('.review-product-card') && document.querySelector('main h1') && !document.documentElement.dataset.operatorLogoChecked) {
    document.documentElement.dataset.operatorLogoChecked = '1';
    const excluded = /ordenacionjuego|gamblingcommission|swisscasinos|esbk|egba|gamcare|begambleaware|gamblingtherapy|wikipedia/i;
    const rows = Array.from(document.querySelectorAll('main tr'));
    const row = rows.find(r => /^(exact domain checked|domain|official website|website)$/i.test((r.cells[0]?.textContent || '').trim()));
    const hrefs = [];
    const direct = row?.querySelector('a[href^="http"]')?.href;
    if (direct) hrefs.push(direct);
    if (!hrefs.length) Array.from(document.querySelectorAll('main a[rel~="nofollow"][href^="http"]')).forEach(a => hrefs.push(a.href));
    let origin = '';
    for (const href of hrefs) { try { const u = new URL(href); if (!excluded.test(u.hostname)) { origin = u.origin; break; } } catch (_) {} }
    const h1 = document.querySelector('main h1');
    const brand = h1.textContent.trim().replace(/\\s+(casino\\s+)?review.*$/i, '').replace(/\\s*\\|.*$/, '').trim() || 'Casino operator';
    let figure = document.querySelector('main .operator-logo-figure');
    const frameStyles = 'width:min(100%,360px);min-height:132px;box-sizing:border-box;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:9px;text-align:center;margin:22px 0 28px;padding:18px 20px;background:linear-gradient(180deg,#fff,#f7faf7);border:1px solid #d8e2d8;border-radius:14px;box-shadow:0 8px 24px rgba(13,40,27,.07)';

    if (!figure) {
      figure = document.createElement('figure');
      figure.className = 'operator-logo-figure operator-logo-figure--auto';
      h1.parentNode.insertBefore(figure, h1.nextSibling);
    }
    figure.style.cssText += ';' + frameStyles;
    let img = figure.querySelector('img');
    if (!img && origin) {
      img = document.createElement('img'); img.src = origin + '/favicon.ico';
      img.alt = brand + ' official website icon'; img.loading = 'lazy'; img.decoding = 'async'; img.referrerPolicy = 'no-referrer';
      figure.prepend(img);
    }
    if (img) {
      img.classList.add('operator-logo-image'); img.alt = brand + ' official brand image';
      img.style.cssText += ';display:block;width:100%;height:82px;max-width:280px;max-height:82px;object-fit:contain;object-position:center;background:#fff;border-radius:10px;padding:10px;box-sizing:border-box';
      if (window.matchMedia && window.matchMedia('(max-width:600px)').matches) { img.style.height='70px'; img.style.maxHeight='70px'; }
      img.addEventListener('error', () => {
        if (origin && !img.dataset.triedOfficialIcon && !img.src.startsWith(origin + '/favicon.ico')) {
          img.dataset.triedOfficialIcon = '1'; img.src = origin + '/favicon.ico';
        } else { img.remove(); figure.classList.add('operator-logo-text-only'); }
      });
    } else figure.classList.add('operator-logo-text-only');
    if (!figure.querySelector('.operator-logo-name')) {
      const label = document.createElement('span'); label.className = 'operator-logo-name'; label.textContent = brand; figure.appendChild(label);
    }
    let caption = figure.querySelector('figcaption');
    if (!caption) { caption = document.createElement('figcaption'); figure.appendChild(caption); }
    caption.textContent = origin
      ? 'Operator identity image from the official website domain. Logos and trademarks belong to their respective owners; BeInCasinos is independent.'
      : 'No official image could be confidently matched from this page; the brand name is shown instead of an invented logo.';
  }

})();
