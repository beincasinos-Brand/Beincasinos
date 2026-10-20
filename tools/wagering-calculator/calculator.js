(() => {
  const form = document.querySelector('#wager-form');
  const amount = document.querySelector('#eligible');
  const multiplier = document.querySelector('#multiplier');
  const currency = document.querySelector('#currency');
  const output = document.querySelector('#turnover');
  const summary = document.querySelector('#result-summary');
  const error = document.querySelector('#calc-error');
  const format = (value) => new Intl.NumberFormat('en', {style:'currency',currency:currency.value,minimumFractionDigits:2,maximumFractionDigits:2}).format(value);
  const showError = () => {
    error.hidden = false;
    output.textContent = '—';
    summary.textContent = 'Correct the values marked as invalid to calculate required turnover.';
  };
  const calculate = () => {
    const a = Number(amount.value), m = Number(multiplier.value);
    const amountInvalid = amount.value === '' || !Number.isFinite(a) || a < 0 || a > 100000000;
    const multiplierInvalid = multiplier.value === '' || !Number.isFinite(m) || m < 0 || m > 100000;
    amount.setAttribute('aria-invalid', String(amountInvalid));
    multiplier.setAttribute('aria-invalid', String(multiplierInvalid));
    if (amountInvalid || multiplierInvalid) {
      showError();
      return;
    }
    const result = a * m;
    if (!Number.isFinite(result)) {
      showError();
      return;
    }
    error.hidden = true;
    output.textContent = format(result);
    summary.textContent = m.toLocaleString('en', {maximumFractionDigits:2}) + '× applied to ' + format(a) + ' means ' + format(result) + ' in qualifying turnover.';
  };
  form.addEventListener('submit', (event) => { event.preventDefault(); calculate(); });
  // Keep the result in sync with edits so a previously valid figure never remains visible for changed inputs.
  amount.addEventListener('input', calculate);
  multiplier.addEventListener('input', calculate);
  currency.addEventListener('change', calculate);
  calculate();
})();
