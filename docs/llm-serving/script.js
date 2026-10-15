
const progress=document.getElementById('progress');const topBtn=document.getElementById('topBtn');const links=[...document.querySelectorAll('.toc a[href^="#"]')];const sections=links.map(a=>document.querySelector(a.getAttribute('href'))).filter(Boolean);
function update(){const d=document.documentElement;const max=d.scrollHeight-d.clientHeight;progress.style.width=(max?d.scrollTop/max*100:0)+'%';topBtn.style.display=d.scrollTop>700?'block':'none';let cur='';for(const s of sections){if(s.getBoundingClientRect().top<150)cur='#'+s.id;}links.forEach(a=>a.classList.toggle('active',a.getAttribute('href')===cur));}
window.addEventListener('scroll',update,{passive:true});update();topBtn.onclick=()=>window.scrollTo({top:0,behavior:'smooth'});
