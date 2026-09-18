/* =============================================================================
   Dublin Trades — site behaviour
   No third-party code, no external requests, no inline handlers (strict-CSP
   friendly). Everything below runs first-party only.
   ========================================================================== */
(function () {
  "use strict";

  /* ---------------------------------------------------------------------
     Cookie helpers — first-party only, SameSite=Lax, Secure over HTTPS.
     --------------------------------------------------------------------- */
  var SECURE = location.protocol === "https:" ? "; Secure" : "";

  function setCookie(name, value, days) {
    var expires = new Date(Date.now() + days * 864e5).toUTCString();
    document.cookie = name + "=" + encodeURIComponent(value) +
      "; Expires=" + expires + "; Path=/; SameSite=Lax" + SECURE;
  }
  function getCookie(name) {
    var parts = document.cookie ? document.cookie.split("; ") : [];
    for (var i = 0; i < parts.length; i++) {
      var eq = parts[i].indexOf("=");
      if (parts[i].slice(0, eq) === name) {
        try { return decodeURIComponent(parts[i].slice(eq + 1)); } catch (e) { return null; }
      }
    }
    return null;
  }
  function deleteCookie(name) {
    document.cookie = name + "=; Expires=Thu, 01 Jan 1970 00:00:00 GMT; Path=/; SameSite=Lax" + SECURE;
  }

  /* ---------------------------------------------------------------------
     Consent state
     --------------------------------------------------------------------- */
  var CONSENT_COOKIE = "dt_consent";
  var CONSENT_VERSION = 1;
  var CONSENT_DAYS = 180;              /* re-ask every 6 months, per EDPB guidance */
  var OPTIONAL_COOKIES = ["dt_analytics_id"];   /* cleared when consent withdrawn */

  function readConsent() {
    var raw = getCookie(CONSENT_COOKIE);
    if (!raw) return null;
    try {
      var c = JSON.parse(raw);
      if (!c || c.v !== CONSENT_VERSION) return null;
      return { v: c.v, ts: c.ts, analytics: c.analytics === true, marketing: c.marketing === true };
    } catch (e) { return null; }
  }

  function writeConsent(analytics, marketing) {
    var c = { v: CONSENT_VERSION, ts: Date.now(), analytics: !!analytics, marketing: !!marketing };
    setCookie(CONSENT_COOKIE, JSON.stringify(c), CONSENT_DAYS);
    applyConsent(c);
    return c;
  }

  /* Everything non-essential is gated here. Nothing loads without consent. */
  function applyConsent(c) {
    if (!c || (!c.analytics && !c.marketing)) {
      OPTIONAL_COOKIES.forEach(deleteCookie);
    }
    if (c && c.analytics) {
      /* Analytics goes here, and ONLY here — it must never run above this line.
         Whatever you add must also be allowed by the CSP in _headers / .htaccess,
         otherwise the browser will block it. Example:
           var s = document.createElement("script");
           s.src = "https://example-analytics.test/script.js";
           s.defer = true;
           document.head.appendChild(s);
         The site currently ships with NO analytics and NO trackers. */
    }
    document.dispatchEvent(new CustomEvent("dt:consent", { detail: c }));
  }

  /* ---------------------------------------------------------------------
     Consent UI
     --------------------------------------------------------------------- */
  function initConsent() {
    var banner = document.getElementById("cookieBanner");
    var dialog = document.getElementById("cookieDialog");
    if (!banner || !dialog) return;

    var analyticsBox = document.getElementById("ccAnalytics");
    var marketingBox = document.getElementById("ccMarketing");

    /* body.cc-open hides the floating WhatsApp button, which would otherwise
       sit underneath the banner on a phone. */
    function showBanner() { banner.hidden = false; document.body.classList.add("cc-open"); }
    function hideBanner() { banner.hidden = true; document.body.classList.remove("cc-open"); }

    function openDialog() {
      var c = readConsent();
      if (analyticsBox) analyticsBox.checked = !!(c && c.analytics);
      if (marketingBox) marketingBox.checked = !!(c && c.marketing);
      if (typeof dialog.showModal === "function") { dialog.showModal(); }
      else { dialog.setAttribute("open", ""); }
    }
    function closeDialog() {
      if (typeof dialog.close === "function") { dialog.close(); }
      else { dialog.removeAttribute("open"); }
    }

    document.getElementById("ccAcceptAll").addEventListener("click", function () {
      writeConsent(true, true); hideBanner();
    });
    document.getElementById("ccRejectAll").addEventListener("click", function () {
      writeConsent(false, false); hideBanner();
    });
    document.getElementById("ccCustomise").addEventListener("click", openDialog);

    document.getElementById("ccSave").addEventListener("click", function () {
      writeConsent(analyticsBox && analyticsBox.checked, marketingBox && marketingBox.checked);
      closeDialog(); hideBanner();
    });
    document.getElementById("ccDialogReject").addEventListener("click", function () {
      writeConsent(false, false); closeDialog(); hideBanner();
    });
    document.getElementById("ccDialogAccept").addEventListener("click", function () {
      writeConsent(true, true); closeDialog(); hideBanner();
    });

    /* Withdrawing consent must be as easy as giving it (GDPR Art. 7(3)). */
    var reopen = document.querySelectorAll("[data-cookie-settings]");
    for (var i = 0; i < reopen.length; i++) {
      reopen[i].addEventListener("click", function (ev) { ev.preventDefault(); openDialog(); });
    }

    var existing = readConsent();
    if (existing) { applyConsent(existing); } else { showBanner(); }
  }

  /* ---------------------------------------------------------------------
     Testimonials carousel
     --------------------------------------------------------------------- */
  function initTestimonials() {
    var track = document.getElementById("testiTrack");
    var dotsWrap = document.getElementById("testiDots");
    if (!track || !dotsWrap) return;

    var cards = track.querySelectorAll(".testi-card");
    if (!cards.length) return;

    var idx = 0, timer = null;
    var reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    cards.forEach(function (_, i) {
      var d = document.createElement("button");
      d.type = "button";
      d.className = "dot" + (i === 0 ? " active" : "");
      d.setAttribute("aria-label", "Show review " + (i + 1) + " of " + cards.length);
      d.addEventListener("click", function () { go(i); restart(); });
      dotsWrap.appendChild(d);
    });
    var dots = dotsWrap.querySelectorAll(".dot");

    function go(i) {
      cards[idx].classList.remove("active");
      dots[idx].classList.remove("active");
      idx = (i + cards.length) % cards.length;
      cards[idx].classList.add("active");
      dots[idx].classList.add("active");
    }
    function start() { if (!reduced) timer = setInterval(function () { go(idx + 1); }, 5500); }
    function stop() { if (timer) { clearInterval(timer); timer = null; } }
    function restart() { stop(); start(); }

    track.addEventListener("mouseenter", stop);
    track.addEventListener("mouseleave", start);
    track.addEventListener("focusin", stop);
    track.addEventListener("focusout", start);
    dotsWrap.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight") { go(idx + 1); restart(); dots[idx].focus(); }
      if (e.key === "ArrowLeft") { go(idx - 1); restart(); dots[idx].focus(); }
    });
    start();
  }

  /* ---------------------------------------------------------------------
     Quote form
     The site is static, so there is no server to post to. The form validates
     locally and hands the enquiry to WhatsApp or the mail client — nothing is
     sent to a third party. See README.md to wire a real backend endpoint.
     --------------------------------------------------------------------- */
  var WHATSAPP_NUMBER = "353858651313";
  var EMAIL = "dublinservices1@gmail.com";

  function initForm() {
    var form = document.getElementById("quoteForm");
    if (!form) return;
    var status = document.getElementById("formStatus");
    var loadedAt = Date.now();

    function say(msg, state) {
      status.textContent = msg;              /* textContent, never innerHTML */
      status.setAttribute("data-state", state);
    }

    form.addEventListener("submit", function (ev) {
      ev.preventDefault();

      /* Bot traps: hidden field must stay empty, and humans do not submit
         a form within 3 seconds of the page loading. */
      var hp = form.querySelector("#qcompany");
      if (hp && hp.value !== "") return;
      if (Date.now() - loadedAt < 3000) {
        say("Please take a moment to fill in the form, then try again.", "error");
        return;
      }

      var name = form.querySelector("#qname").value.trim();
      var phone = form.querySelector("#qphone").value.trim();
      var msg = form.querySelector("#qmsg").value.trim();

      if (name.length < 2 || name.length > 80) { say("Please enter your name.", "error"); return; }
      if (!/^[0-9+()\s-]{7,20}$/.test(phone)) { say("Please enter a valid phone number.", "error"); return; }
      if (msg.length < 5 || msg.length > 2000) { say("Please tell us a little about the job.", "error"); return; }

      var body = "Quote request from the website\n\nName: " + name +
                 "\nPhone: " + phone + "\n\nJob details:\n" + msg;

      say("Opening WhatsApp with your details. If nothing happens, call 085 865 1313.", "ok");
      var wa = "https://wa.me/" + WHATSAPP_NUMBER + "?text=" + encodeURIComponent(body);
      var win = window.open(wa, "_blank", "noopener,noreferrer");
      if (!win) {
        location.href = "mailto:" + EMAIL +
          "?subject=" + encodeURIComponent("Quote request — " + name) +
          "&body=" + encodeURIComponent(body);
      }
      form.reset();
    });
  }

  /* ---------------------------------------------------------------------
     Mobile menu. The <details> element opens on its own without JavaScript;
     this only adds the closing behaviour.
     --------------------------------------------------------------------- */
  function initMobileNav() {
    var nav = document.getElementById("mobileNav");
    if (!nav) return;
    var panel = nav.querySelector(".mobile-nav-panel");

    panel.addEventListener("click", function (e) {
      if (e.target.tagName === "A") nav.removeAttribute("open");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") nav.removeAttribute("open");
    });
    document.addEventListener("click", function (e) {
      if (nav.hasAttribute("open") && !nav.contains(e.target)) nav.removeAttribute("open");
    });
  }

  /* --------------------------------------------------------------------- */
  function initYear() {
    var el = document.getElementById("year");
    if (el) el.textContent = String(new Date().getFullYear());
  }

  function init() {
    initConsent();
    initMobileNav();
    initTestimonials();
    initForm();
    initYear();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
