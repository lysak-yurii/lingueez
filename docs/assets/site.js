/* Shared site behaviour: language, theme, nav, lightbox, reveal-on-scroll. */
(function(){
  var root=document.documentElement;
  var reduced=window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ── strings ───────────────────────────────────────────────────────────
     Text the scripts build instead of finding in the markup. _includes/i18n-js.html
     drops the page's language into #i18n-js; the English is both the key and
     the fallback, so a missing blob still reads. hero.js uses this too. */
  var strings={};
  try{
    var blob=document.getElementById('i18n-js');
    if(blob) strings=JSON.parse(blob.textContent);
  }catch(e){ /* a broken blob must not take the rest of the page with it */ }
  function t(s){ return strings[s] || s; }
  window.lzT=t;

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

  /* ── swipe ─────────────────────────────────────────────────────────────
     Every gallery on the site steps with dashes and arrow keys; on a phone
     neither is the gesture anyone reaches for first. swipe(el, step) adds the
     one that is: step(+1) for a flick to the left, step(-1) to the right.

     Touch and pen only — a mouse drag across a picture means selection, not
     "next". The element gives up only the horizontal gesture: `pan-y` leaves
     the page scrolling under the finger and `pinch-zoom` leaves a screenshot
     zoomable, which matters most in the lightbox. Declaring it is also what
     stops the browser from taking the pointer stream away mid-swipe.

     `step` is only called once the gesture is unambiguously horizontal, and
     the click that a finger-up would otherwise synthesise is swallowed — the
     same elements are all clickable (open the lightbox, close the device), and
     a swipe must not trip that. */
  function swipe(el, step){
    if(!window.PointerEvent) return;
    el.style.touchAction='pan-y pinch-zoom';
    if(!el.style.touchAction) el.style.touchAction='pan-y';   // older parser

    var id=null, x0=0, y0=0, t0=0, lock=0;   // lock: 0 undecided, 1 across, -1 down

    /* The click a finger-up synthesises, eaten in the capture phase before it
       reaches the button underneath. It is dropped again the moment the next
       gesture begins rather than after a timeout: a tap that lands soon after
       a swipe is an ordinary tap and has to work, and a swipe that somehow
       synthesises no click at all must not leave the trap armed. */
    var killer=null;
    function disarm(){
      if(!killer) return;
      el.removeEventListener('click', killer, true);
      killer=null;
    }
    function swallowClick(){
      disarm();
      killer=function(e){ e.stopPropagation(); e.preventDefault(); disarm(); };
      el.addEventListener('click', killer, true);
    }

    el.addEventListener('pointerdown', function(e){
      disarm();                                    // any new press, mouse included
      if(e.pointerType==='mouse' || !e.isPrimary) return;
      id=e.pointerId; x0=e.clientX; y0=e.clientY; t0=Date.now(); lock=0;
    });

    el.addEventListener('pointermove', function(e){
      if(e.pointerId!==id || lock) return;
      var dx=e.clientX-x0, dy=e.clientY-y0;
      if(Math.abs(dx) < 8 && Math.abs(dy) < 8) return;   // still inside the slop
      // A drag that is mostly downward is the visitor scrolling past, not
      // stepping; deciding once and sticking to it keeps a diagonal from
      // flickering between the two.
      lock=Math.abs(dx) > Math.abs(dy) * 1.2 ? 1 : -1;
      // With the direction settled the gesture is ours to the end, even if the
      // finger wanders off the element.
      if(lock===1){ try{ el.setPointerCapture(id); }catch(err){} }
    });

    el.addEventListener('pointerup', function(e){
      if(e.pointerId!==id) return;
      var dx=e.clientX-x0, dt=Date.now()-t0, across=lock===1;
      id=null; lock=0;
      if(!across) return;
      // Either a deliberate drag or a quick flick — a slow 20px wobble is
      // neither, and stepping on it would feel like the page misread a tap.
      if(Math.abs(dx) < 44 && !(Math.abs(dx) > 18 && dt < 260)) return;
      swallowClick();
      step(dx < 0 ? 1 : -1);
    });

    el.addEventListener('pointercancel', function(e){
      if(e.pointerId===id){ id=null; lock=0; }
    });
  }
  window.lzSwipe=swipe;

  /* ── language ──────────────────────────────────────────────────────────
     Each language is its own page, so this only opens and closes the list —
     and records the pick on the way out. */
  (function(){
    /* Written before the browser leaves, so lang-preinit.html on the next page
       sees the new choice rather than the old one. Cookie and localStorage
       writes are synchronous, so a click handler is early enough; the English
       link also carries ?lang=en in case this script has not run yet. */
    document.querySelectorAll('.lang-menu a[data-lang]').forEach(function(a){
      a.addEventListener('click', function(){
        var code=a.getAttribute('data-lang');
        try{ localStorage.setItem('lz-lang', code); }catch(e){}
        shareCookie('lz-lang', code);
      });
    });

    /* There are two — one in the nav, one in the footer — and opening either
       closes the other, so they never sit open at the same time. */
    var shut=[];
    document.querySelectorAll('.lang').forEach(function(box){
      var btn=box.querySelector('.lang-current'), menu=box.querySelector('.lang-menu');
      if(!btn||!menu) return;
      function open(on){
        menu.hidden=!on;
        btn.setAttribute('aria-expanded', String(on));
      }
      shut.push(function(){ open(false); });
      btn.addEventListener('click', function(e){
        e.stopPropagation();
        var show=menu.hidden;
        shut.forEach(function(f){ f(); });
        open(show);
      });
      document.addEventListener('click', function(e){
        if(!box.contains(e.target)) open(false);
      });
    });
    document.addEventListener('keydown', function(e){
      if(e.key==='Escape') shut.forEach(function(f){ f(); });
    });
  })();

  /* ── theme ─────────────────────────────────────────────────────────────
     Three modes; 'system' is the absence of data-theme, so the light-dark()
     tokens fall back to prefers-color-scheme. theme-preinit.html applies the
     stored mode before paint — this only handles changes. */
  var MODES=['system','light','dark'];

  /* lingueez.app and web.lingueez.app are separate origins and do not share
     localStorage, but a cookie scoped to the parent domain is sent to both. So
     every preference that should survive the crossing is written twice:
     localStorage as the same-origin fast path, a cookie as the bridge. The web
     app reads the cookie in its own pre-paint script and in src/lib/theme.ts.

     Domain is only set on the real site — a Domain of .lingueez.app would be
     rejected outright on localhost or a preview host. */
  function shareCookie(name, value){
    var dom = /(^|\.)lingueez\.app$/.test(location.hostname) ? '; domain=.lingueez.app' : '';
    var age = value ? 31536000 : 0;
    try{
      document.cookie = name+'='+(value||'')+'; path=/'+dom+'; max-age='+age+'; SameSite=Lax';
    }catch(e){}
  }

  function cookieValue(name){
    var m = document.cookie.match(new RegExp('(?:^|;\\s*)'+name+'=([^;]*)'));
    return m ? m[1] : null;
  }

  function storedMode(){
    var s; try{ s=localStorage.getItem('lz-theme'); }catch(e){}
    if(s!=='light' && s!=='dark') s = cookieValue('lz-theme');
    return (s==='light'||s==='dark') ? s : 'system';
  }

  /* Mirror the language into the cookie on every view — that is what lets the
     web app, on its own origin, link back here in the language the visitor was
     reading.

     A stored choice comes first and the page's own language is only the
     fallback, because pages exist with no translated twin (the legal pages,
     404). Publishing their `en` unconditionally would quietly reset a visitor
     who had chosen Deutsch and then opened the privacy policy. */
  (function(){
    var s; try{ s=localStorage.getItem('lz-lang'); }catch(e){}
    if(!s) s=cookieValue('lz-lang');
    shareCookie('lz-lang', s || root.getAttribute('data-lang') || 'en');
  })();

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
    shareCookie('lz-theme', mode==='system' ? '' : mode);

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
                   t('Close'));
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
                    t('Previous'));
      var next=icon('<path d="M9 5l7 7-7 7"/>',
                    t('Next'));
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
      // The whole sheet, not just the image: full size leaves a picture much
      // narrower than the screen on a phone, and a swipe that only counted
      // over the screenshot itself would mostly miss.
      swipe(box, function(dir){ go(at + dir); });
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
    // Swipe across the pictures themselves, which is the whole block bar the
    // dashes; the click that would otherwise open the lightbox is swallowed.
    swipe(box.querySelector('.ss-stack') || box, function(dir){ go(at + dir); start(); });

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

  /* ── feature rails ──────────────────────────────────────────────────────
     Each feature group lays its cards out as a horizontal track. Three of them
     measure exactly the track's width, so most groups never overflow and get no
     controls at all — this only wakes up for a group that carries more, and
     then it adds dots into the group heading, marks which edges have more behind
     them, and cycles so the extra cards are met rather than waited for.

     Two things keep the movement from being rude. It stops dead while the
     pointer or the keyboard focus is on the rail, because these cards are prose
     someone may be halfway through reading — unlike the showcase shots, which
     are one feature photographed twice. And it turns round at the ends instead
     of wrapping: rewinding four cards in one sweep reads as a jolt, where
     reversing reads as the same calm drift going the other way. */
  var RAIL_DWELL=3400;   // shorter than the showcase's 5200 — a card, not a page
  document.querySelectorAll('.fgroup > .grid').forEach(function(track){
    var head=track.parentNode.querySelector('h3');
    var cards=Array.prototype.slice.call(track.querySelectorAll('.card'));
    var dots=null, lead=[], at=0, queued=false;
    var timer=null, hot=false, seen=false, dir=1;

    /* Pages are counted in cards, not in viewport widths: the track carries a
       gap between cards, so scrollWidth/clientWidth is not a whole number of
       screens and rounding it strands an extra dot that scrolls nowhere. */
    function measure(){
      if(!cards.length || limit() <= 1) return [];
      var step=cards.length > 1 ? cards[1].offsetLeft - cards[0].offsetLeft
                                : cards[0].offsetWidth;
      var per=Math.max(1, Math.round(track.clientWidth / step));
      var out=[], last=-1;
      for(var i=0; i<cards.length; i+=per){
        // A last page holding fewer than a full view cannot scroll its card to
        // the left edge — it stops at the end of the track. Two pages that land
        // on the same place are one page.
        var target=Math.min(offsetOf(cards[i]), limit());
        if(target - last < 1) continue;
        out.push(cards[i]);
        last=target;
      }
      return out;
    }
    function offsetOf(card){ return card.offsetLeft - cards[0].offsetLeft; }
    function limit(){ return track.scrollWidth - track.clientWidth; }
    /* Where page *i* actually comes to rest. Everything compares against this
       rather than the card's own offset: the browser clamps a scroll to the end
       of the track, so a final page asked for further than that would be read
       back as some earlier page and the rail would deadlock there. */
    function targetOf(i){ return Math.min(offsetOf(lead[i]), limit()); }

    function edges(){
      track.classList.toggle('has-prev', track.scrollLeft > 1);
      track.classList.toggle('has-next', track.scrollLeft < limit() - 1);
    }

    function mark(){
      var best=0, dist=Infinity;
      lead.forEach(function(card, i){
        var d=Math.abs(targetOf(i) - track.scrollLeft);
        if(d < dist){ dist=d; best=i; }
      });
      at=best;
      if(!dots) return;
      Array.prototype.forEach.call(dots.children, function(d, i){
        d.classList.toggle('is-on', i===at);
        d.setAttribute('aria-pressed', String(i===at));
      });
    }

    function go(i){
      track.scrollTo({left:targetOf(i), behavior:reduced ? 'auto' : 'smooth'});
    }

    /* A chained timeout rather than setInterval: each step is armed only once
       the last has been taken, so a rail that was paused mid-dwell does not
       fire the moment it is released. */
    function stop(){ if(timer){ clearTimeout(timer); timer=null; } }
    function start(){
      stop();
      if(reduced || hot || !seen || lead.length < 2) return;
      timer=setTimeout(function(){
        if(at + dir >= lead.length || at + dir < 0) dir=-dir;
        go(at + dir);
        start();
      }, RAIL_DWELL);
    }

    /* One dot per page, labelled with the card that page opens on — already
       translated in the markup, so the control needs no string of its own. */
    function build(){
      var next=measure();
      var same=dots && next.length === lead.length
               && next.every(function(c, i){ return c === lead[i]; });
      lead=next;
      if(same){ mark(); edges(); return; }
      if(dots){ dots.remove(); dots=null; }
      if(lead.length < 2 || !head){
        // A resize can widen a rail back into a plain row — nothing left to
        // advance to, so the clock has to be stopped and not just left armed.
        stop();
        track.classList.remove('has-prev', 'has-next');
        return;
      }
      dots=document.createElement('span');
      dots.className='screen-dots';
      dots.setAttribute('role', 'group');
      lead.forEach(function(card, i){
        var name=(card.querySelector('h3')||{}).textContent || '';
        var d=document.createElement('button');
        d.type='button';
        d.className='screen-dot';
        d.setAttribute('aria-pressed', 'false');
        if(name) d.setAttribute('aria-label', name.trim());
        d.addEventListener('click', function(){
          // Step where asked, and carry on from there in the same direction.
          dir=i >= at ? 1 : -1;
          go(i);
          start();                             // a manual step restarts the dwell
        });
        dots.appendChild(d);
      });
      head.appendChild(dots);
      mark();
      edges();
      start();
    }

    // Arrow keys and Home/End come free once the track can hold focus.
    track.tabIndex=0;
    track.setAttribute('role', 'group');
    track.addEventListener('scroll', function(){
      if(queued) return;
      queued=true;
      requestAnimationFrame(function(){ queued=false; mark(); edges(); });
    });

    /* Hovering or focusing the rail holds it still — and keeps holding it, so a
       visitor reading the fourth card is never carried off it. Touch counts as
       hover until the finger leaves, which is what a drag wants too. */
    function hold(){ hot=true; stop(); }
    function release(){ hot=false; start(); }
    track.addEventListener('pointerenter', hold);
    track.addEventListener('pointerleave', release);
    track.addEventListener('focusin', hold);
    track.addEventListener('focusout', release);

    if('IntersectionObserver' in window){
      new IntersectionObserver(function(es){
        es.forEach(function(e){
          seen=e.isIntersecting;
          if(seen) start(); else stop();
        });
      },{threshold:.25}).observe(track);
    } else {
      seen=true;
    }
    if('ResizeObserver' in window) new ResizeObserver(build).observe(track);
    else window.addEventListener('resize', build);
    build();
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
