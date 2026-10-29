(() => {
  const root = document.documentElement;

  // Theme: saved choice, else the system setting. The toggle lives in the header markup.
  let saved = null;
  try { saved = localStorage.getItem('bic-theme'); } catch (_) {}
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  const applyTheme = theme => {
    const next = theme === 'dark' ? 'dark' : 'light';
    root.setAttribute('data-theme', next);
    document.querySelectorAll('[data-theme-toggle]').forEach(btn => {
      btn.setAttribute('aria-pressed', String(next === 'dark'));
      btn.textContent = next === 'dark' ? 'Light mode' : 'Dark mode';
    });
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', next === 'dark' ? '#0a101a' : '#f1f3f6');
  };
  applyTheme(saved || (prefersDark ? 'dark' : 'light'));
  document.querySelectorAll('[data-theme-toggle]').forEach(btn => btn.addEventListener('click', () => {
    const next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    applyTheme(next);
    try { localStorage.setItem('bic-theme', next); } catch (_) {}
  }));

  // Mobile menu.
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#primary-nav');
  if (toggle && nav) {
    const closeMenu = restoreFocus => {
      toggle.setAttribute('aria-expanded', 'false');
      nav.classList.remove('open');
      if (restoreFocus) toggle.focus();
    };
    toggle.addEventListener('click', () => {
      if (toggle.getAttribute('aria-expanded') === 'true') { closeMenu(false); return; }
      toggle.setAttribute('aria-expanded', 'true');
      nav.classList.add('open');
    });
    nav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => closeMenu(false)));
    document.addEventListener('keydown', event => { if (event.key === 'Escape') closeMenu(true); });
    document.addEventListener('click', e => { if (!nav.contains(e.target) && !toggle.contains(e.target)) closeMenu(false); });
    window.matchMedia('(min-width: 861px)').addEventListener('change', () => closeMenu(false));
  }

  // Operator logos: hotlinked or local images fall back to the monogram if they fail.
  const brokenLogo = img => { const frame = img.closest('.bx-logo'); if (frame) frame.classList.add('is-broken'); };
  document.querySelectorAll('.bx-logo img').forEach(img => {
    img.addEventListener('error', () => brokenLogo(img), { once: true });
    if (img.complete && img.naturalWidth === 0) brokenLogo(img);
  });

  // Review directory filter.
  const search = document.querySelector('#review-search');
  const market = document.querySelector('#review-market');
  const grid = document.querySelector('#review-product-grid');
  if (search && market && grid) {
    const clear = document.querySelector('#review-clear-filters');
    const count = document.querySelector('#review-results-count');
    const empty = document.querySelector('#review-no-results');
    const cards = Array.from(grid.querySelectorAll('.bx-card'));
    const norm = v => String(v || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/\s+/g, ' ').trim();
    const update = () => {
      const q = norm(search.value), m = market.value;
      let shown = 0;
      cards.forEach(card => {
        const ok = (!q || norm(card.dataset.search).includes(q)) && (!m || card.dataset.market === m);
        card.hidden = !ok;
        if (ok) shown += 1;
      });
      grid.querySelectorAll('.bx-market').forEach(sec => { sec.hidden = !sec.querySelector('.bx-card:not([hidden])'); });
      if (count) count.textContent = shown + (shown === 1 ? ' review' : ' reviews');
      if (empty) empty.hidden = shown !== 0;
      if (clear) clear.disabled = !q && !m;
    };
    search.addEventListener('input', update);
    market.addEventListener('change', update);
    if (clear) clear.addEventListener('click', () => { search.value = ''; market.value = ''; update(); search.focus(); });
    update();
  }
})();
