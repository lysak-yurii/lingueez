/* Shared site behaviour: language, theme, nav, lightbox, reveal-on-scroll. */
(function(){
  var root=document.documentElement;
  var reduced=window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── platform ──────────────────────────────────────────────────────────
     One sniff, shared by the download CTA, the download-page card order and
     the hero's "this is your device" highlight. Returns '' when unsure —
     every caller must degrade to something sensible. */
  function platform(){
    var ua=navigator.userAgent||'';
    var p=(navigator.userAgentData && navigator.userAgentData.platform) || navigator.platform || '';
    if(/android/i.test(ua)) return 'android';
    if(/iphone|ipad|ipod/i.test(ua) || (/mac/i.test(p) && navigator.maxTouchPoints>1)) return 'ios';
    if(/win/i.test(p)) return 'win';
    if(/mac/i.test(p)) return 'mac';
    if(/linux|x11/i.test(p)) return 'linux';
    return '';
  }
  window.lzPlatform=platform;

  /* ── language ──────────────────────────────────────────────────────────── */
  function setLang(l){
    root.setAttribute('data-lang',l);
    try{localStorage.setItem('lz-lang',l);}catch(e){}
    document.querySelectorAll('[data-lang-btn]').forEach(function(b){
      b.setAttribute('aria-pressed', String(b.getAttribute('data-lang-btn')===l));
    });
    // For text that cannot be authored as bilingual spans — aria-label and
    // friends take a string, not markup. hero.js listens for this.
    document.dispatchEvent(new CustomEvent('lz:lang', {detail:l}));
  }
  document.querySelectorAll('[data-lang-btn]').forEach(function(b){
    b.addEventListener('click', function(){ setLang(b.getAttribute('data-lang-btn')); });
  });
  if(document.querySelector('[data-lang-btn]')){
    setLang(root.getAttribute('data-lang') || 'en');
  }

  /* ── theme ─────────────────────────────────────────────────────────────
     Three modes; 'system' is the absence of data-theme, so the light-dark()
     tokens fall back to prefers-color-scheme. theme-preinit.html applies the
     stored mode before paint — this only handles changes. */
  var MODES=['system','light','dark'];

  function storedMode(){
    var s; try{ s=localStorage.getItem('lz-theme'); }catch(e){}
    return (s==='light'||s==='dark') ? s : 'system';
  }

  function resolved(mode){
    if(mode!=='system') return mode;
    return (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches)
      ? 'dark' : 'light';
  }

  function paintMode(mode){
    if(mode==='system'){ root.removeAttribute('data-theme'); }
    else{ root.setAttribute('data-theme',mode); }
    document.querySelectorAll('.theme').forEach(function(t){ t.setAttribute('data-mode',mode); });
    var meta=document.getElementById('theme-color');
    if(meta){ meta.setAttribute('content', resolved(mode)==='dark' ? '#101418' : '#f4f6f9'); }
  }

  function setTheme(mode, origin){
    try{
      if(mode==='system'){ localStorage.removeItem('lz-theme'); }
      else{ localStorage.setItem('lz-theme',mode); }
    }catch(e){}

    /* The new theme wipes in as a circle growing from the button. Without
       View Transitions (or with reduced motion) the swap is simply instant. */
    if(reduced || !document.startViewTransition || !origin){ paintMode(mode); return; }

    var r=origin.getBoundingClientRect();
    var x=r.left+r.width/2, y=r.top+r.height/2;
    var reach=Math.hypot(Math.max(x, innerWidth-x), Math.max(y, innerHeight-y));
    var vt=document.startViewTransition(function(){ paintMode(mode); });
    vt.ready.then(function(){
      root.animate(
        {clipPath:['circle(0px at '+x+'px '+y+'px)','circle('+reach+'px at '+x+'px '+y+'px)']},
        {duration:520, easing:'cubic-bezier(.2,.8,.25,1)',
         pseudoElement:'::view-transition-new(root)'});
    }).catch(function(){});
  }

  var themeBtns=document.querySelectorAll('[data-theme-btn]');
  if(themeBtns.length){
    paintMode(storedMode());
    themeBtns.forEach(function(b){
      b.addEventListener('click', function(){
        var next=MODES[(MODES.indexOf(storedMode())+1) % MODES.length];
        setTheme(next, b);
      });
    });
    /* Following the OS means following it as it changes. */
    if(window.matchMedia){
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(){
        if(storedMode()==='system') paintMode('system');
      });
    }
  }

  /* ── nav ───────────────────────────────────────────────────────────────── */
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

  /* ── lightbox ───────────────────────────────────────────────────────────
     A [data-zoom] trigger opens its full-size source over the page. The
     trigger's own <img> supplies the alt text and a placeholder to show while
     the (larger) zoom source loads. hero.js reuses openZoom() for the
     "view full screenshot" affordance. */
  var box=null, opener=null, gallery=null, onClose=null;

  function closeZoom(){
    if(!box) return;
    var gone=box, done=onClose;
    box=null; gallery=null; onClose=null;
    gone.classList.remove('in');
    root.style.overflow='';
    setTimeout(function(){ gone.remove(); }, 200);
    if(opener){ opener.focus(); opener=null; }
    if(done) done();
  }

  function icon(path, label){
    var b=document.createElement('button');
    b.type='button';
    b.innerHTML='<svg viewBox="0 0 24 24" width="22" height="22" fill="none" '+
      'stroke="currentColor" stroke-width="2" stroke-linecap="round" '+
      'stroke-linejoin="round" aria-hidden="true">'+path+'</svg>'+
      '<span class="sr-only">'+label+'</span>';
    return b;
  }

  /* opts: {src, alt, placeholder, returnTo, items, index, onChange, onClose}
     `items` turns the lightbox into a gallery: [{full, label}] with dashes to
     step through and arrow keys bound. `onChange(index)` lets the opener follow
     along — the hero keeps the device underneath on the same screen. Without
     `items` this is the plain viewer the [data-zoom] triggers have always used. */
  function openZoom(opts){
    if(box) return;
    opener=opts.returnTo || null;
    onClose=opts.onClose || null;

    box=document.createElement('div');
    box.className='lightbox';
    box.setAttribute('role','dialog');
    box.setAttribute('aria-modal','true');

    var frame=document.createElement('div');
    frame.className='lightbox-frame';
    var full=document.createElement('img');
    full.alt=opts.alt || '';
    if(opts.placeholder) full.src=opts.placeholder;
    frame.appendChild(full);

    function load(src){
      var big=new Image();
      big.onload=function(){ full.src=big.src; };
      big.src=src;
    }
    load(opts.src);

    var close=icon('<path d="M6 6l12 12M18 6L6 18"/>',
                   '<span lang="en">Close</span><span lang="uk">Закрити</span>');
    close.className='lightbox-close';
    close.addEventListener('click', closeZoom);

    // Anywhere off the screenshot dismisses — the backdrop, the padding around
    // the image, the caption. Only the image itself and the controls are
    // exempt, so a mis-aimed click never costs the viewer their place.
    box.addEventListener('click', function(e){
      if(e.target.closest('img, button, a')) return;
      closeZoom();
    });

    box.appendChild(frame);
    box.appendChild(close);

    var items=opts.items || [];
    if(items.length > 1){
      var at=opts.index || 0;
      var caption=document.createElement('p');
      caption.className='lightbox-caption';
      var dots=document.createElement('span');
      dots.className='lightbox-dots';
      var marks=items.map(function(item, i){
        var d=document.createElement('button');
        d.type='button';
        d.className='screen-dot';
        d.innerHTML='<span class="sr-only">'+item.label+'</span>';
        d.addEventListener('click', function(e){ e.stopPropagation(); go(i); });
        dots.appendChild(d);
        return d;
      });
      var label=document.createElement('span');
      label.className='lightbox-label';
      caption.appendChild(label);
      caption.appendChild(dots);

      var prev=icon('<path d="M15 5l-7 7 7 7"/>',
                    '<span lang="en">Previous</span><span lang="uk">Попередній</span>');
      var next=icon('<path d="M9 5l7 7-7 7"/>',
                    '<span lang="en">Next</span><span lang="uk">Наступний</span>');
      prev.className='lightbox-step prev';
      next.className='lightbox-step next';
      prev.addEventListener('click', function(e){ e.stopPropagation(); go(at - 1); });
      next.addEventListener('click', function(e){ e.stopPropagation(); go(at + 1); });

      function go(i){
        at=(i + items.length) % items.length;
        load(items[at].full);
        label.innerHTML=items[at].label;
        marks.forEach(function(d, n){
          d.classList.toggle('is-on', n===at);
          d.setAttribute('aria-pressed', String(n===at));
        });
        if(opts.onChange) opts.onChange(at);
      }
      box.appendChild(prev);
      box.appendChild(next);
      box.appendChild(caption);
      gallery={go:function(step){ go(at + step); }};
      go(at);
    }

    document.body.appendChild(box);
    root.style.overflow='hidden';
    requestAnimationFrame(function(){ if(box) box.classList.add('in'); });
    close.focus();
  }
  window.lzZoom=openZoom;

  /* The page loads WebP because that is what fits a showcase row; the lightbox
     wants the untouched PNG beside it. Same stem, so derive it rather than
     carrying a second path through the markup that could fall out of step.
     currentSrc, not src: it is the one the browser actually picked, which is
     how the light/dark pair resolves to the right file. */
  function fullSize(img){
    return (img.currentSrc || img.src).split('?')[0].replace(/\.webp$/, '.png');
  }
  function visibleImg(scope){
    return Array.prototype.filter.call(scope.querySelectorAll('img'), function(im){
      return getComputedStyle(im).display !== 'none';
    })[0];
  }

  // Single screenshots: click to see it full size.
  document.querySelectorAll('[data-shot-zoom]').forEach(function(trigger){
    trigger.addEventListener('click', function(){
      var img=visibleImg(trigger);
      if(!img) return;
      openZoom({src:fullSize(img), alt:img.alt,
                placeholder:img.currentSrc || img.src, returnTo:trigger});
    });
  });

  var zoomTriggers=document.querySelectorAll('[data-zoom]');
  if(zoomTriggers.length){
    Array.prototype.forEach.call(zoomTriggers, function(t){
      t.addEventListener('click', function(){
        var thumb=t.querySelector('img');
        openZoom({src:t.getAttribute('data-zoom'),
                  alt:thumb ? thumb.alt : '',
                  placeholder:thumb ? (thumb.currentSrc || thumb.src) : '',
                  returnTo:t});
      });
    });
  }
  document.addEventListener('keydown', function(e){
    if(e.key==='Escape'){ closeZoom(); return; }
    if(!gallery) return;
    if(e.key==='ArrowLeft'){ e.preventDefault(); gallery.go(-1); }
    else if(e.key==='ArrowRight'){ e.preventDefault(); gallery.go(1); }
  });

  /* ── two-shot showcase ──────────────────────────────────────────────────
     A [data-shot-switch] block holds several .ss-slide screenshots, one label
     per slide and one dot per slide, and steps through them together. It only
     runs while the block is on screen: a carousel that cycled below the fold
     would just be met half-finished, and under reduced motion it never
     advances on its own — the dots still work. */
  document.querySelectorAll('[data-shot-switch]').forEach(function(box){
    var slides=box.querySelectorAll('.ss-slide');
    var labels=box.querySelectorAll('.ss-label');
    var dots=box.querySelectorAll('.screen-dot');
    if(slides.length < 2) return;

    var at=0, timer=null;
    function go(i){
      at=(i + slides.length) % slides.length;
      [slides, labels, dots].forEach(function(set){
        Array.prototype.forEach.call(set, function(el, n){
          el.classList.toggle('is-on', n===at);
          if(el.hasAttribute('aria-pressed')) el.setAttribute('aria-pressed', String(n===at));
        });
      });
    }
    function stop(){ if(timer){ clearInterval(timer); timer=null; } }
    function start(){
      stop();
      if(reduced) return;
      timer=setInterval(function(){ go(at + 1); }, 5200);
    }

    Array.prototype.forEach.call(dots, function(d, i){
      d.addEventListener('click', function(){ go(i); start(); });  // a step restarts the dwell
    });

    /* Click the picture to see it full size — as a gallery, so the lightbox can
       step between the same shots. onChange keeps the row underneath on
       whichever one is being looked at, so closing it leaves the page showing
       what the visitor just had open. */
    var trigger=box.querySelector('[data-ss-zoom]');
    if(trigger){
      trigger.addEventListener('click', function(){
        var items=Array.prototype.map.call(slides, function(s, i){
          var img=visibleImg(s);
          return {full:img ? fullSize(img) : '',
                  label:labels[i] ? labels[i].innerHTML : ''};
        });
        var here=visibleImg(slides[at]);
        stop();                       // nothing should move behind an open lightbox
        openZoom({src:items[at].full, alt:here ? here.alt : '',
                  placeholder:here ? (here.currentSrc || here.src) : '',
                  returnTo:trigger, items:items, index:at,
                  onChange:function(i){ go(i); },
                  onClose:function(){ start(); }});
      });
    }

    if('IntersectionObserver' in window){
      new IntersectionObserver(function(es){
        es.forEach(function(e){ if(e.isIntersecting) start(); else stop(); });
      },{threshold:.25}).observe(box);
    } else {
      start();
    }
  });

  /* ── reveal on scroll ───────────────────────────────────────────────────
     [data-stagger] promotes its children to individually revealed items, so
     a grid fans in instead of appearing as one slab. */
  document.querySelectorAll('[data-stagger]').forEach(function(group){
    Array.prototype.forEach.call(group.children, function(child, i){
      child.classList.add('stagger-item');   // not .reveal — the group drives them
      child.style.setProperty('--i', i);
    });
  });

  function revealAll(el){
    el.classList.add('in');
    if(el.hasAttribute('data-stagger')){
      Array.prototype.forEach.call(el.children, function(c){ c.classList.add('in'); });
    }
  }

  var targets=document.querySelectorAll('.reveal, [data-stagger]');
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){ if(e.isIntersecting){ revealAll(e.target); io.unobserve(e.target); } });
    },{threshold:.12});
    targets.forEach(function(e){ io.observe(e); });
  } else {
    targets.forEach(revealAll);
  }
})();
