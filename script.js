(() => {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#primary-nav');
  if (toggle && nav) {
    const closeMenu = (returnFocus = false) => {
      toggle.setAttribute('aria-expanded', 'false');
      nav.classList.remove('open');
      if (returnFocus) toggle.focus();
    };
    toggle.addEventListener('click', () => {
      const expanded = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!expanded));
      nav.classList.toggle('open', !expanded);
    });
    nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => closeMenu()));
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
        closeMenu(true);
      }
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
    summary.querySelector('.review-visual-title').textContent = titleText;
    const market = summary.querySelector('.review-visual-status span:nth-child(2)');
    market.textContent = marketText;
    reviewHero.insertAdjacentElement('afterend', summary);
  }
})();
