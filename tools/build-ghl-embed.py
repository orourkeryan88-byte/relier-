import re, sys

src = open('index.html', encoding='utf-8').read()
ROOT = '#southline-page'

RESET = """
/* ---------------------------------------------------------------
   Host-theme reset. A GHL template styles bare element selectors
   (h1, p, section...), and those beat anything we merely inherit.
   This neutralises them first; every rule below is equal or higher
   specificity and comes later, so our own styling still wins.
   --------------------------------------------------------------- */
#southline-page h1,#southline-page h2,#southline-page h3,#southline-page h4,
#southline-page h5,#southline-page h6,#southline-page p,#southline-page span,
#southline-page a,#southline-page li,#southline-page ul,#southline-page ol,
#southline-page em,#southline-page strong,#southline-page i,#southline-page b,
#southline-page button,#southline-page summary,#southline-page details,
#southline-page div,#southline-page section,#southline-page article,
#southline-page header,#southline-page footer,#southline-page nav{
  font-family:inherit;
  font-weight:inherit;
  font-style:normal;
  font-size:inherit;
  color:inherit;
  line-height:inherit;
  letter-spacing:inherit;
  text-transform:none;
  text-align:inherit;
  text-decoration:none;
  background:none;
  border:0;
  border-radius:0;
  margin:0;
  padding:0;
  box-shadow:none;
  float:none;
  text-shadow:none;
  max-width:none;
  min-height:0;
}
#southline-page ul,#southline-page ol{list-style:none}
#southline-page img,#southline-page video,#southline-page iframe{border:0;margin:0}
"""

style = re.search(r'<style>(.*?)</style>', src, re.S).group(1)
script = re.search(r'<script>(.*?)</script>', src, re.S).group(1)
body = re.search(r'<body>(.*?)\n<script>', src, re.S).group(1)

def split_selectors(sel):
    """Split a selector list on top-level commas (ignore commas inside parens)."""
    out, depth, cur = [], 0, ''
    for ch in sel:
        if ch == '(': depth += 1
        elif ch == ')': depth -= 1
        if ch == ',' and depth == 0:
            out.append(cur); cur = ''
        else:
            cur += ch
    if cur.strip(): out.append(cur)
    return out

def scope_one(s):
    s = s.strip()
    if not s: return s
    if s.startswith('from') or s.startswith('to') or re.match(r'^\d+%', s):
        return s                                  # keyframe stops
    if s.startswith('html'):
        return ROOT + s[4:]
    if s == 'body':
        return ROOT
    if s.startswith('body'):
        return ROOT + s[4:]
    if s.startswith(':root'):
        rest = s[5:]
        return ROOT + rest if rest else ROOT
    if s.startswith('*'):
        return ROOT + ' ' + s
    return ROOT + ' ' + s

def scope_block(css):
    """Walk the CSS, prefixing selectors but leaving @keyframes stops alone."""
    out, i, n = [], 0, len(css)
    while i < n:
        # a comment sitting before an at-rule used to defeat the @ match below,
        # which then swallowed the at-rule into a selector. Emit comments first.
        cm = re.match(r'\s*/\*.*?\*/', css[i:], re.S)
        if cm:
            out.append(css[i:i + cm.end()])
            i += cm.end()
            continue
        # at-rule?
        m = re.match(r'\s*@([a-zA-Z-]+)([^{;]*)([{;])', css[i:])
        if m:
            name, params, term = m.group(1), m.group(2), m.group(3)
            out.append(css[i:i + m.end()])
            i += m.end()
            if term == ';':
                continue
            depth, start = 1, i
            while i < n and depth:
                if css[i] == '{': depth += 1
                elif css[i] == '}': depth -= 1
                i += 1
            inner = css[start:i-1]
            if name.endswith('keyframes'):
                out.append(inner)                  # stops must stay untouched
            else:
                out.append(scope_block(inner))     # @media / @supports
            out.append('}')
            continue
        # ordinary rule
        j = css.find('{', i)
        if j == -1:
            out.append(css[i:]); break
        sel_raw = css[i:j]
        lead = sel_raw[:len(sel_raw) - len(sel_raw.lstrip())]
        sel = sel_raw.strip()
        depth, k = 1, j + 1
        while k < n and depth:
            if css[k] == '{': depth += 1
            elif css[k] == '}': depth -= 1
            k += 1
        decls = css[j+1:k-1]
        if sel.startswith('/*') and '*/' in sel:      # keep leading comments
            cpos = sel.rindex('*/') + 2
            comment, sel = sel[:cpos], sel[cpos:].strip()
        else:
            comment = ''
        scoped = ', '.join(scope_one(s) for s in split_selectors(sel))
        nl = chr(10) if comment else ''
        out.append(lead + comment + nl + scoped + '{' + decls + '}')
        i = k
    return ''.join(out)

scoped_css = RESET + scope_block(style)



# ---------------------------------------------------------------------------
# GHL hardening: page builders frequently strip <script> from custom-code
# blocks, or only run it on the published page and not in the editor. So the
# GHL build must render fully with JavaScript switched off entirely.
# ---------------------------------------------------------------------------
import html as _html
import re as _re0

# 1. Real <video> in the markup instead of one built by JS.
_pm = _re0.search(r'<div class="player" id="player">.*?</button>\s*</div>', body, _re0.S)
assert _pm, 'player block not found'
old_player = _pm.group(0)
new_player = """<div class="player" id="player">
          <video id="vsl" controls playsinline preload="metadata" poster="PASTE_POSTER_URL_HERE">
            <source src="PASTE_MP4_URL_HERE" type="video/mp4">
            Your browser cannot play this video.
          </video>
          <button class="poster" id="poster" type="button" aria-label="Play the video" hidden>
            <span class="play" aria-hidden="true">
              <svg width="26" height="30" viewBox="0 0 26 30" fill="currentColor"><path d="M25 13.27a2 2 0 0 1 0 3.46L3 29.4A2 2 0 0 1 0 27.66V2.34A2 2 0 0 1 3 .6l22 12.67Z"/></svg>
            </span>
            <span class="poster-label">Play the video</span>
            <span class="poster-note">51 seconds — sound on</span>
          </button>
        </div>"""
body = body.replace(old_player, new_player)

# 2. Calendar iframe in the markup instead of one built by JS.
_cm = _re0.search(r'<div class="calendar-shell" id="calendar-shell">.*?</a>\s*</div>\s*</div>', body, _re0.S)
assert _cm, 'calendar block not found'
cal_start, cal_end = _cm.start(), _cm.end()
new_cal = """<div class="calendar-shell" id="calendar-shell">
        <iframe src="https://api.leadconnectorhq.com/widget/booking/Jyy3OGmnlXllDOv1VZz6"
                id="Jyy3OGmnlXllDOv1VZz6_ghl"
                data-layout='{"id":"INLINE"}' data-trigger-type="alwaysShow"
                title="Book a call with Southline Agency" scrolling="no"></iframe>
      </div>
      <script src="https://link.msgsndr.com/js/form_embed.js"></script>"""
body = body[:cal_start] + new_cal + body[cal_end:]

# 3. Marquee duplicated in the markup so the loop is seamless without JS.
track = _re0.search(r'(<div class="marquee-track" id="marquee-track">)(.*?)(</div>)', body, _re0.S)
body = body.replace(track.group(0), track.group(1) + track.group(2) + track.group(2) + track.group(3))

# 4. Scroll-reveal must not hide content when no script runs: it is now opt-in,
#    switched on only by the enhancement script below.
scoped_css = scoped_css.replace('#southline-page .reveal{', '#southline-page.js .reveal{')
scoped_css = scoped_css.replace('#southline-page .reveal.in{', '#southline-page.js .reveal.in{')
scoped_css += """
/* video fills the frame; the branded overlay only appears if JS is running */
#southline-page #player video{position:absolute;inset:0;width:100%;height:100%;border:0;background:#000}
#southline-page .poster[hidden]{display:none}
#southline-page #ghl-cal,#southline-page .calendar-shell iframe{
  width:100%;min-height:780px;border:0;border-radius:12px;background:#fff;display:block;
}
"""

# 5. Enhancement-only script. Everything it does is optional polish; if GHL
#    drops it, the page still shows the video, the calendar and all content.
script = """
(function () {
  'use strict';
  var root = document.getElementById('southline-page');
  if (!root) return;
  root.classList.add('js');

  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  /* branded play overlay, shown only because JS is available to drive it */
  var poster = document.getElementById('poster');
  var video  = document.getElementById('vsl');
  if (poster && video) {
    poster.hidden = false;
    poster.addEventListener('click', function () {
      poster.hidden = true;
      video.play().catch(function () {});
    });
    video.addEventListener('pause', function () { if (video.currentTime === 0) poster.hidden = false; });
  }

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* header shadow, scroll progress, sticky mobile CTA */
  var header = document.getElementById('site-header');
  var sticky = document.getElementById('sticky');
  var bar    = document.getElementById('progress');
  var stage  = root.querySelector('.stage');
  var ticking = false;
  function onScroll() {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () {
      var sy = window.scrollY;
      var max = document.documentElement.scrollHeight - window.innerHeight;
      if (bar) bar.style.transform = 'scaleX(' + (max > 0 ? Math.min(sy / max, 1) : 0) + ')';
      if (header) header.classList.toggle('scrolled', sy > 8);
      if (sticky) {
        var past = stage ? stage.getBoundingClientRect().bottom < 0 : sy > 600;
        var book = document.getElementById('book');
        var r = book ? book.getBoundingClientRect() : null;
        var at = r ? (r.top < window.innerHeight * 0.75 && r.bottom > 0) : false;
        sticky.classList.toggle('show', past && !at);
      }
      ticking = false;
    });
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll, { passive: true });
  onScroll();

  /* scroll reveal */
  var items = root.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduced) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('in');
        io.unobserve(e.target);
      });
    }, { threshold: 0.14, rootMargin: '0px 0px -50px 0px' });
    items.forEach(function (el, i) {
      el.style.transitionDelay = (i % 4) * 90 + 'ms';
      io.observe(el);
    });
    setTimeout(function () { items.forEach(function (el) { el.classList.add('in'); }); }, 4000);
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  /* pointer-reactive hero blobs */
  if (!reduced && window.matchMedia('(pointer:fine)').matches) {
    var hero = root.querySelector('.hero');
    var blobs = root.querySelectorAll('.hero .blob');
    if (hero) hero.addEventListener('pointermove', function (e) {
      var rc = hero.getBoundingClientRect();
      var dx = (e.clientX - rc.left - rc.width / 2) / rc.width;
      var dy = (e.clientY - rc.top - rc.height / 2) / rc.height;
      blobs.forEach(function (blob, i) {
        var d = (i + 1) * 14;
        blob.style.translate = (dx * d).toFixed(1) + 'px ' + (dy * d).toFixed(1) + 'px';
      });
    }, { passive: true });
  }
})();
"""


out = f'''<!--
  ============================================================
  SOUTHLINE AGENCY — GoHighLevel embed
  ============================================================
  Paste this whole block into a GHL Custom JS/HTML element on
  a blank funnel/website page (full width, no padding).

  BEFORE IT WILL WORK — two find-and-replace edits:
    PASTE_MP4_URL_HERE     -> your GHL Media Library URL for vsl.mp4
    PASTE_POSTER_URL_HERE  -> your GHL Media Library URL for vsl-poster.jpg
  Both appear once each, in the video tag near the top of the markup.

  Then set the page section's padding to 0 so the design runs edge to edge.

  This build needs NO JavaScript. The video, the booking calendar and every
  section are plain HTML, so they still render even if GHL strips the
  scripts (or only runs them on the published page, not in the editor).
  Any script that survives adds polish only: scroll animations, the
  progress bar and the sticky mobile button.

  Every style below is scoped to {ROOT}, so nothing here can
  leak out and restyle the rest of your GHL page.
-->

<div id="southline-page">
<style>
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700;800&display=swap');

/* smooth anchor scrolling — this one line is intentionally global */
html{{scroll-behavior:smooth}}

{scoped_css}
</style>
{body}
<script>{script}</script>
</div>
'''
open('ghl-embed.html', 'w', encoding='utf-8').write(out)
print('written ghl-embed.html')
print('unscoped top-level selectors remaining:',
      len(re.findall(r'(?m)^(?!\s*[@}/])[a-z*:\[][^{}]*\{', scoped_css)))
