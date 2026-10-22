(() => {
 const boxes = Array.from(document.querySelectorAll('.check-item input[type="checkbox"]'));
 const recordFields = Array.from(document.querySelectorAll('.evidence-record input, .evidence-record textarea'));
 const count = document.getElementById('checked-count');
 const total = document.getElementById('total-count');
 const fill = document.getElementById('progress-fill');
 const track = document.getElementById('progress-track');
 const message = document.getElementById('progress-message');
 total.textContent = String(boxes.length);
 track.setAttribute('aria-valuemax', String(boxes.length));
 function update() {
   const checked = boxes.filter(box => box.checked).length;
   count.textContent = String(checked);
   fill.className = 'progress-fill progress-' + checked;
   track.setAttribute('aria-valuenow', String(checked));
   message.textContent = checked === boxes.length ? 'Checklist complete. Keep the source links and terms for your records.' : checked === 0 ? 'Start by checking the original source for each claim.' : checked >= Math.ceil(boxes.length * .7) ? 'Good progress. Revisit any item you could not verify.' : 'Keep going, and leave any unverified item unchecked.';
 }
 boxes.forEach(box => box.addEventListener('change', update));
 document.getElementById('print-checklist').addEventListener('click', () => window.print());
 document.getElementById('reset-checklist').addEventListener('click', () => { boxes.forEach(box => { box.checked = false; }); recordFields.forEach(field => { field.value = ''; }); update(); });
 update();
})();
