/* Shared site behaviour: language toggle, nav scroll-shadow, reveal-on-scroll. */
(function(){
  function setLang(l){
    document.documentElement.setAttribute('data-lang',l);
    try{localStorage.setItem('lz-lang',l);}catch(e){}
    document.querySelectorAll('[data-lang-btn]').forEach(function(b){
      b.setAttribute('aria-pressed', String(b.getAttribute('data-lang-btn')===l));
    });
  }
  document.querySelectorAll('[data-lang-btn]').forEach(function(b){
    b.addEventListener('click', function(){ setLang(b.getAttribute('data-lang-btn')); });
  });
  if(document.querySelector('[data-lang-btn]')){
    setLang(document.documentElement.getAttribute('data-lang') || 'en');
  }

  var nav=document.querySelector('.nav');
  if(nav){
    var onScroll=function(){ nav.classList.toggle('scrolled', window.scrollY>8); };
    window.addEventListener('scroll', onScroll, {passive:true}); onScroll();
  }

  // Mobile nav: toggle the hamburger dropdown.
  var navToggle=document.querySelector('.nav-toggle');
  if(nav && navToggle){
    var navMenu=document.getElementById('nav-menu');
    var setNavOpen=function(open){
      nav.classList.toggle('open', open);
      navToggle.setAttribute('aria-expanded', String(open));
    };
    navToggle.addEventListener('click', function(){ setNavOpen(!nav.classList.contains('open')); });
    if(navMenu){ navMenu.addEventListener('click', function(e){ if(e.target.closest('a')) setNavOpen(false); }); }
    document.addEventListener('keydown', function(e){ if(e.key==='Escape') setNavOpen(false); });
  }

  // Lightbox: a [data-zoom] trigger opens its full-size source over the page.
  // The trigger's own <img> supplies the alt text and a placeholder to show
  // while the (larger) zoom source loads.
  var zoomTriggers=document.querySelectorAll('[data-zoom]');
  if(zoomTriggers.length){
    var box=null, opener=null;

    var closeZoom=function(){
      if(!box) return;
      var gone=box; box=null;
      gone.classList.remove('in');
      document.documentElement.style.overflow='';
      setTimeout(function(){ gone.remove(); }, 200);
      if(opener){ opener.focus(); opener=null; }
    };

    var openZoom=function(trigger){
      if(box) return;
      opener=trigger;
      var thumb=trigger.querySelector('img');

      box=document.createElement('div');
      box.className='lightbox';
      box.setAttribute('role','dialog');
      box.setAttribute('aria-modal','true');

      var full=document.createElement('img');
      full.alt=thumb ? thumb.alt : '';
      if(thumb) full.src=thumb.currentSrc || thumb.src;   // show something immediately
      var big=new Image();
      big.onload=function(){ full.src=big.src; };
      big.src=trigger.getAttribute('data-zoom');

      var close=document.createElement('button');
      close.type='button';
      close.className='lightbox-close';
      close.innerHTML='<svg viewBox="0 0 24 24" width="20" height="20" fill="none" '+
        'stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true">'+
        '<path d="M6 6l12 12M18 6L6 18"/></svg>'+
        '<span class="sr-only"><span lang="en">Close</span><span lang="uk">Закрити</span></span>';
      close.addEventListener('click', closeZoom);

      // Clicking the backdrop dismisses; clicking the image itself does not.
      box.addEventListener('click', function(e){ if(e.target===box) closeZoom(); });

      box.appendChild(full);
      box.appendChild(close);
      document.body.appendChild(box);
      document.documentElement.style.overflow='hidden';
      requestAnimationFrame(function(){ if(box) box.classList.add('in'); });
      close.focus();
    };

    Array.prototype.forEach.call(zoomTriggers, function(t){
      t.addEventListener('click', function(){ openZoom(t); });
    });
    document.addEventListener('keydown', function(e){ if(e.key==='Escape') closeZoom(); });
  }

  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
    },{threshold:.12});
    document.querySelectorAll('.reveal').forEach(function(e){ io.observe(e); });
  } else {
    document.querySelectorAll('.reveal').forEach(function(e){ e.classList.add('in'); });
  }
})();
