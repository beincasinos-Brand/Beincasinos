(()=>{
  const n=id=>{const el=document.getElementById(id);return el.value===''?NaN:Number(el.value)};
  const money=v=>new Intl.NumberFormat('en',{style:'currency',currency:'USD',minimumFractionDigits:2,maximumFractionDigits:2}).format(v);
  const form=document.querySelector('#tool-form'),err=document.querySelector('#calc-error');
  const calc=()=>{const out=(()=>{ 
 var s=n('stake'),b=n('bph'),h=n('hrs'),r=n('rtp');
 if([s,b,h,r].some(function(x){return !isFinite(x)||x<0})||r<50||r>100)return null;
 var tot=s*b*h, edge=100-r;
 return [money(tot),edge.toFixed(2)+'%',money(tot*edge/100/(h||1)),money(tot*edge/100)]; })();
    if(!out){err.hidden=false;for(let i=1;i<=4;i++)document.getElementById('o'+i).textContent='—';return}
    err.hidden=true;for(let i=0;i<4;i++)document.getElementById('o'+(i+1)).textContent=out[i]};
  form.addEventListener('submit',ev=>{ev.preventDefault();calc()});
  form.querySelectorAll('input,select').forEach(el=>{el.addEventListener('input',calc);el.addEventListener('change',calc)});
  calc();
})();
