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
    const themeMeta = document.querySelector('meta[name="theme-color"]');
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
})();
