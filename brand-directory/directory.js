(()=>{const search=document.getElementById('brand-search'),market=document.getElementById('market-filter'),status=document.getElementById('status-filter'),evidence=document.getElementById('evidence-filter'),clear=document.getElementById('clear-filters'),cards=[...document.querySelectorAll('.brand-card')],count=document.getElementById('results-count'),grid=document.getElementById('brand-grid');function filter(){const q=search.value.trim().toLowerCase(),m=market.value,s=status.value,e=evidence.value;let n=0;for(const c of cards){const visible=(!q||c.dataset.search.includes(q)||c.textContent.toLowerCase().includes(q))&&(!m||c.dataset.market===m)&&(!s||c.dataset.status===s)&&(!e||c.dataset.evidence===e);c.hidden=!visible;if(visible)n++;}let empty=grid.querySelector('.empty-state');if(!n&&!empty){empty=document.createElement('p');empty.className='empty-state';empty.setAttribute('role','status');empty.textContent='No entries match these filters. Clear filters or try another search.';grid.append(empty);}if(n&&empty)empty.remove();count.textContent='Showing '+n+' of '+cards.length+' research entries';}function reset(){search.value='';market.value='';status.value='';evidence.value='';filter();search.focus();}search.addEventListener('input',filter);market.addEventListener('change',filter);status.addEventListener('change',filter);evidence.addEventListener('change',filter);clear.addEventListener('click',reset);})();

// Only load a remote brand mark after its usage rights are explicitly cleared.
// Pending candidates stay as metadata for research; the visible card uses a neutral monogram.
function showLogoFallback(img) {
  img.hidden = true;
  const fallback = img.nextElementSibling;
  if (fallback) fallback.hidden = false;
}
document.querySelectorAll('.brand-logo-image').forEach((img) => {
  if (img.dataset.imageRights !== 'cleared' || !img.dataset.candidateSrc) {
    showLogoFallback(img);
    return;
  }
  img.src = img.dataset.candidateSrc;
  img.hidden = false;
  img.addEventListener('error', () => showLogoFallback(img), { once: true });
  if (img.complete && img.naturalWidth === 0) showLogoFallback(img);
});
