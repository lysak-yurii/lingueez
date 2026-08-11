/* The sign-in modal: open it from the nav, authenticate against Supabase here,
   and hand the session to the web app so the visitor lands already signed in.

   This used to be a panel two thirds of the way down the home page, reached by
   a Log in link pointing at #web. A login that lives at an anchor is a page to
   scroll to rather than a thing to do, and it only existed on one page — so
   the same button meant "jump to the home page" everywhere else. It is now
   what a login is on every other site: a modal, one click from the nav, on
   whichever page you are already on.

   Markup: _includes/signin-dialog.html. Loaded with defer, so site.js has run. */
(function(){
  var dialog=document.getElementById('signin-dialog');
  if(!dialog) return;

  var SUPABASE_URL="https://dtyrmkynrideeknsdlrn.supabase.co";
  var SUPABASE_ANON="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR0eXJta3lucmlkZWVrbnNkbHJuIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODE4Njc1MTQsImV4cCI6MjA5NzQ0MzUxNH0.dds5SyMBN9u-0TUumB2nSCx68FJfpm3n63fLq1n9o10";
  var WEB_APP="https://web.lingueez.app/";
  var SDK="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.js";

  function byId(id){ return document.getElementById(id); }
  function t(en,uk){ return document.documentElement.getAttribute("data-lang")==="uk" ? uk : en; }

  var form=byId("signin-form"), errBox=byId("si-err"),
      submit=byId("si-submit"), googleBtn=byId("si-google");

  /* ── opening ───────────────────────────────────────────────────────────── */
  var supported=typeof dialog.showModal==="function";

  function open(origin){
    if(!supported) return false;
    showErr("");
    dialog.returnValue="";
    dialog.showModal();
    loadSdk();                       // warm the SDK while they type
    // Not the close button: landing focus on "dismiss" is a dead end. The
    // email field is what the modal is for.
    var first=byId("si-email");
    if(first) first.focus({preventScroll:true});
    dialog._origin=origin || null;
    return true;
  }

  function close(){
    if(!dialog.open) return;
    dialog.close();
    if(dialog._origin && dialog._origin.isConnected) dialog._origin.focus();
    dialog._origin=null;
  }

  document.querySelectorAll('[data-signin]').forEach(function(btn){
    btn.addEventListener('click', function(e){
      // The control is a real link to the web app; only take over the click
      // when the modal can actually replace it.
      if(e.metaKey || e.ctrlKey || e.shiftKey || e.button) return;
      if(open(btn)) e.preventDefault();
    });
  });
  dialog.querySelectorAll('[data-signin-close]').forEach(function(b){
    b.addEventListener('click', close);
  });
  // A click on the backdrop lands on the <dialog> itself — the card is a child,
  // so anything inside it never matches. Escape is handled by <dialog>.
  dialog.addEventListener('click', function(e){ if(e.target===dialog) close(); });

  /* ── the SDK ────────────────────────────────────────────────────────────
     Loaded on demand rather than on every page view: it is ~120 KB that only
     matters to a visitor who actually opens this. First call starts the fetch,
     later ones wait on the same promise. */
  var sdk=null;
  function loadSdk(){
    if(sdk) return sdk;
    sdk=new Promise(function(resolve, reject){
      if(window.supabase && window.supabase.createClient) return resolve();
      var s=document.createElement('script');
      s.src=SDK;
      s.onload=function(){
        if(window.supabase && window.supabase.createClient) resolve();
        else reject(new Error('sdk'));
      };
      s.onerror=function(){ sdk=null; reject(new Error('sdk')); };  // let a retry try again
      document.head.appendChild(s);
    });
    return sdk;
  }

  var client=null;
  function sb(){
    if(!client){
      client=window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON,
        {auth:{persistSession:false, detectSessionInUrl:false}});
    }
    return client;
  }

  /* ── auth ──────────────────────────────────────────────────────────────── */
  function showErr(msg){ if(errBox) errBox.textContent=msg || ""; }
  function busy(btn,on){ btn.setAttribute("aria-busy", on ? "true" : "false"); }

  function handOff(session){
    var p=new URLSearchParams({
      access_token:session.access_token,
      refresh_token:session.refresh_token,
      expires_in:String(session.expires_in),
      expires_at:String(session.expires_at),
      token_type:session.token_type||"bearer"
    });
    window.location.assign(WEB_APP+"#"+p.toString());
  }

  function mapError(error){
    var m=(error&&error.message||"").toLowerCase();
    if(m==="sdk") return t("Couldn't reach the sign-in service. Please try again.",
                           "Не вдалося звернутися до служби входу. Спробуйте ще раз.");
    if(m.indexOf("confirm")>-1) return t("Confirm your email first — check your inbox for the link.",
                                         "Спершу підтвердьте електронну пошту — перевірте лист із посиланням.");
    if(m.indexOf("invalid")>-1||m.indexOf("credentials")>-1)
      return t("We couldn't sign you in. Check your email and password.",
               "Не вдалося увійти. Перевірте електронну пошту та пароль.");
    return error&&error.message||t("Something went wrong. Please try again.",
                                   "Щось пішло не так. Спробуйте ще раз.");
  }

  if(form){
    form.addEventListener("submit", function(e){
      e.preventDefault();
      showErr("");
      var email=byId("si-email").value.trim(), pass=byId("si-pass").value;
      if(!email||!pass){
        showErr(t("Enter your email and password to continue.",
                  "Введіть пошту та пароль, щоб продовжити."));
        return;
      }
      busy(submit,true);
      loadSdk()
        .then(function(){ return sb().auth.signInWithPassword({email:email, password:pass}); })
        .then(function(res){
          if(res.error){ busy(submit,false); showErr(mapError(res.error)); return; }
          if(res.data&&res.data.session){ handOff(res.data.session); }
          else{ busy(submit,false); showErr(mapError({message:""})); }
        })
        .catch(function(err){ busy(submit,false); showErr(mapError(err)); });
    });
  }

  if(googleBtn){
    googleBtn.addEventListener("click", function(){
      showErr(""); busy(googleBtn,true);
      loadSdk()
        .then(function(){
          return sb().auth.signInWithOAuth({provider:"google", options:{redirectTo:WEB_APP}});
        })
        .then(function(res){
          if(res.error){ busy(googleBtn,false); showErr(mapError(res.error)); }
          /* on success the browser is already navigating to Google */
        })
        .catch(function(err){ busy(googleBtn,false); showErr(mapError(err)); });
    });
  }
})();
