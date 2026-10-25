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
    const update = () => {
      const query = reviewSearch.value.trim().toLocaleLowerCase();
      const market = reviewMarket.value;
      let shown = 0;
      cards.forEach(card => {
        const matches = (!query || (card.dataset.search || '').includes(query)) &&
          (!market || card.dataset.market === market);
        card.hidden = !matches;
        if (matches) shown += 1;
      });
      if (count) count.textContent = shown + (shown === 1 ? ' profile' : ' profiles');
    };
    reviewSearch.addEventListener('input', update);
    reviewMarket.addEventListener('change', update);
  }
})();
