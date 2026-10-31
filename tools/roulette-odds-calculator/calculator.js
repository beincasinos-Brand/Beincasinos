(()=>{
  const n=id=>{const el=document.getElementById(id);return el.value===''?NaN:Number(el.value)};
  const money=v=>new Intl.NumberFormat('en',{style:'currency',currency:'USD',minimumFractionDigits:2,maximumFractionDigits:2}).format(v);
  const form=document.querySelector('#tool-form'),err=document.querySelector('#calc-error');
  const calc=()=>{const out=(()=>{ 
 var s=n('stake'),w=Number(document.getElementById('wheel').value),k=Number(document.getElementById('bet').value);
 if(!isFinite(s)||s<0)return null;
 var pay=36/k-1, pr=k/w, edge=(1-(pr*(pay+1)))*100;
 return [(pr*100).toFixed(2)+'%',(Math.round(pay*100)/100)+' to 1',edge.toFixed(2)+'%',money(s*edge/100)]; })();
    if(!out){err.hidden=false;for(let i=1;i<=4;i++)document.getElementById('o'+i).textContent='—';return}
    err.hidden=true;for(let i=0;i<4;i++)document.getElementById('o'+(i+1)).textContent=out[i]};
  form.addEventListener('submit',ev=>{ev.preventDefault();calc()});
  form.querySelectorAll('input,select').forEach(el=>{el.addEventListener('input',calc);el.addEventListener('change',calc)});
  calc();
})();
