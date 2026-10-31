(()=>{
  const n=id=>{const el=document.getElementById(id);return el.value===''?NaN:Number(el.value)};
  const money=v=>new Intl.NumberFormat('en',{style:'currency',currency:'USD',minimumFractionDigits:2,maximumFractionDigits:2}).format(v);
  const form=document.querySelector('#tool-form'),err=document.querySelector('#calc-error');
  const calc=()=>{const out=(()=>{ 
 var d=n('deposit'),p=n('pct'),c=n('cap'),w=n('wr'),r=n('rtp'),base=document.getElementById('base').value;
 if([d,p,c,w,r].some(function(x){return !isFinite(x)||x<0})||r<50||r>100)return null;
 var b=d*p/100; if(c>0&&b>c)b=c;
 var t=(base==='b'?b:d+b)*w, cost=t*(1-r/100), net=b-cost;
 return [money(b),money(t),money(cost),(net>=0?'+':'−')+money(Math.abs(net))]; })();
    if(!out){err.hidden=false;for(let i=1;i<=4;i++)document.getElementById('o'+i).textContent='—';return}
    err.hidden=true;for(let i=0;i<4;i++)document.getElementById('o'+(i+1)).textContent=out[i]};
  form.addEventListener('submit',ev=>{ev.preventDefault();calc()});
  form.querySelectorAll('input,select').forEach(el=>{el.addEventListener('input',calc);el.addEventListener('change',calc)});
  calc();
})();
