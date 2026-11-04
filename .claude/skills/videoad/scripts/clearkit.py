#!/usr/bin/env python3
"""clearkit: shared engine for Southline "clear story" ads (HyperFrames HTML + GSAP, beat-locked, no VO).

An ad spec imports this module and calls build(...) with its palette, scene table (local-beat timings), HTML, CSS,
JS and cues. Every scene starts on the music's beat grid (139.2 BPM by default); inside JS use `cur = "sX"` then
A(localBeat) for absolute seconds. Helpers: wordsAt, from, punch, flash, pulse, pop, fadeUp, fadeOut, swing, count,
draw, shot (auto for every scene), lineWipe. Components: cap(), title2(), phone(), endcard_sa(), endcard_southline().
Rules baked in (lessons.md): full-sentence captions, hold each finished line >=1.5 s, hidden elements revealed with
tl.set, decorative overlays carry data-layout-ignore, no template-literal querySelectorAll.
"""
import json

P = 0.43103          # beat length of the user's track (139.2 BPM); override with build(..., beat=...)


def words(s):
    out = []
    for w in s.split():
        ac = w.startswith("*"); w = w.lstrip("*")
        out.append(f'<span class="w{" ac" if ac else ""}">{w}</span>')
    return " ".join(out)


def cap(cid, key, top, size=88, lead="", sub="", serif=False, extra=""):
    ld = f'<span class="ld">{words(lead)}</span>' if lead else ""
    sb = f'<span class="sb">{words(sub)}</span>' if sub else ""
    return (f'<div class="cap" id="{cid}" style="top:{top}px;--ks:{size}px;{extra}">{ld}'
            f'<span class="kw{" fr" if serif else ""}">{words(key)}</span>{sb}</div>')


def title2(tid, l1, l2, top, size=190):
    """Two-line heavy-serif callout; second line in the accent colour, rises in on the half beat."""
    return (f'<div class="ttl" id="{tid}" style="top:{top}px;--ts:{size}px"><span class="mask"><span class="in">{l1}</span></span>'
            f'<span class="mask"><span class="in ac" id="{tid}b">{l2}</span></span></div>')


ICO = ('<svg class="ico" viewBox="0 0 74 74"><path d="M14 12 H60 Q66 12 66 18 V46 Q66 52 60 52 H32 L18 64 V52 H14 Q8 52 8 46 V18 Q8 12 14 12 Z" fill="none" '
       'stroke="currentColor" stroke-width="5" stroke-linejoin="round"/><circle cx="25" cy="32" r="4.2" fill="currentColor"/><circle cx="37" cy="32" r="4.2" fill="currentColor"/>'
       '<circle cx="49" cy="32" r="4.2" fill="currentColor"/></svg>')


def _pill(keyword, left, top, w, h, color):
    chars = list(keyword)
    spans = [f'<span class="c">“{chars[0]}</span>'] + [f'<span class="c">{c}</span>' for c in chars[1:-1]] + [f'<span class="c">{chars[-1]}”</span>']
    sw = 5.5
    return (f'<div id="pill" style="left:{left}px;top:{top}px;width:{w}px;height:{h}px;color:{color}">'
            f'<svg class="ol" viewBox="0 0 {w} {h}" data-layout-ignore><rect id="pillR" x="{sw/2}" y="{sw/2}" width="{w-sw}" height="{h-sw}" rx="{(h-sw)/2}" '
            f'fill="none" stroke="{color}" stroke-width="{sw}"/></svg>'
            f'<div class="row">{ICO}<span class="dv"></span><span class="tx"><span class="cm">Comment</span> <span class="q">{"".join(spans)}</span></span></div></div>'), (w, h)


def endcard_sa(keyword, tagline=None):
    """The owner's SA artwork (assets/endcard.jpg) in bands, with our own pill carrying the keyword."""
    sc = 1080 / 1170
    def band(i, t0, t1):
        top, bot = round(t0 * sc), round(1735 * sc - t1 * sc)
        return (f'<div class="eb" id="eb{i}" style="clip-path: inset({top}px 0 {bot}px 0); transform-origin: 540px {round((t0 + t1) / 2 * sc)}px">'
                f'<img src="assets/endcard.jpg" alt="" width="1080" height="{round(1735 * sc)}"></div>')
    pill, (w, h) = _pill(keyword, 210, 1061, 661, 109, "#ffffff")
    last = (f'<div class="ctr tagl" id="eb4">{tagline}</div>' if tagline else band(4, 1337, 1386))
    html = "\n      ".join(["", band(1, 441, 802), band(2, 832, 1150), pill, last])
    return html, w, h


def endcard_southline(l1, l2, keyword, acc, size=150):
    """Southline end card in the same layout: S monogram + arc, line, two-line serif, keyword pill, FOR MORE INFO."""
    pill, (w, h) = _pill(keyword, 190, 1100, 700, 116, "#ffffff")
    html = f'''
      <div class="ctr" id="smono">S</div>
      <svg class="arc" id="sarc" style="top:470px" viewBox="0 0 840 84" data-layout-ignore><path d="M0 74 Q420 -14 840 74 Q420 4 0 74 Z" fill="{acc}"/></svg>
      <div class="ctr mono" id="sline">SOUTHLINE · FACEBOOK + INSTAGRAM ADS</div>
      <div class="ttl" id="stitle" style="top:700px;--ts:{size}px"><span class="mask" id="st1"><span class="in">{l1}</span></span><span class="mask" id="st2"><span class="in">{l2}</span></span></div>
      {pill}
      <div class="ctr mono" id="fmi">FOR MORE INFO.</div>'''
    return html, w, h


def phone(pid, left, top, inner, w=400, h=780):
    return (f'<div class="phone" id="{pid}" style="left:{left}px;top:{top}px;width:{w}px;height:{h}px">'
            f'<i class="notch"></i><div class="scr">{inner}</div></div>')


BASE_CSS = '''
  @font-face { font-family: "Instrument Sans"; src: url(assets/fonts/is-500.woff2) format("woff2"); font-weight: 500; }
  @font-face { font-family: "Instrument Sans"; src: url(assets/fonts/is-700.woff2) format("woff2"); font-weight: 700; }
  @font-face { font-family: "Instrument Serif"; src: url(assets/fonts/iserif-italic.woff2) format("woff2"); font-style: italic; font-weight: 400; }
  @font-face { font-family: "Fraunces"; src: url(assets/fonts/fr-700.woff2) format("woff2"); font-weight: 700; }
  @font-face { font-family: "Fraunces"; src: url(assets/fonts/fr-900.woff2) format("woff2"); font-weight: 900; }
  @font-face { font-family: "IBM Plex Mono"; src: url(assets/fonts/plex-500.woff2) format("woff2"); font-weight: 500; }
  html, body { margin: 0; background: var(--bg); }
  body { font-family: "Instrument Sans", sans-serif; -webkit-font-smoothing: antialiased; }
  #root { position: relative; width: 1080px; height: 1920px; overflow: hidden; }
  .full { position: absolute; inset: 0; }
  #bg { z-index: 0; background: var(--bg); }
  #grain { z-index: 90; opacity: .07; mix-blend-mode: overlay; inset: -200px;
    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>"); }
  .scene { position: absolute; inset: 0; z-index: 10; overflow: hidden; }
  .scene.dark { background: var(--bg); color: var(--fg); } .scene.light { background: var(--paper); color: var(--ink); }
  .scene.end { background: var(--endbg); color: #ffffff; } .end .glow { display: none; }
  .glow { position: absolute; inset: 0; }
  .dark .glow { background: radial-gradient(ellipse 70% 45% at 50% 42%, var(--glow) 0%, rgba(0,0,0,0) 62%), radial-gradient(ellipse 120% 90% at 50% 45%, rgba(0,0,0,0) 55%, rgba(0,0,0,.5) 100%); }
  .light .glow { background: radial-gradient(ellipse 80% 55% at 50% 40%, rgba(255,255,255,.4) 0%, rgba(255,255,255,0) 65%); }
  .cam { position: absolute; inset: 0; transform-origin: 50% 45%; }
  .mono { font: 500 24px "IBM Plex Mono", monospace; letter-spacing: .14em; }
  .ctr { position: absolute; left: 0; width: 1080px; text-align: center; }
  .ac { color: var(--acc); } .light .ac { color: var(--accd); }
  .cap { position: absolute; left: 50px; width: 980px; text-align: center; transform-origin: 50% 50%; --ks: 88px; }
  .cap .ld { font: italic 400 72px/1.05 "Instrument Serif", serif; opacity: .85; display: block; margin-bottom: 16px; }
  .cap .kw { font-weight: 700; font-size: var(--ks); letter-spacing: -0.04em; line-height: 1.05; display: block; }
  .cap .kw.fr { font-family: "Fraunces", serif; font-weight: 900; letter-spacing: -0.03em; }
  .cap .sb { font: italic 400 58px/1.12 "Instrument Serif", serif; display: block; margin-top: 18px; opacity: .9; }
  .cap .w { display: inline-block; padding: 0 0.02em; }
  .ttl { position: absolute; left: 0; width: 1080px; text-align: center; transform-origin: 50% 50%; --ts: 190px; }
  .ttl .mask { display: block; overflow: hidden; padding: 0 0 28px; margin-bottom: -28px; }
  .ttl .in { display: inline-block; font: 900 var(--ts)/1.0 "Fraunces", serif; letter-spacing: -0.035em; }
  .sub { font: italic 400 66px/1.12 "Instrument Serif", serif; opacity: .92; padding: 0 110px; box-sizing: border-box; }
  .lbl span { display: inline-block; border: 2px solid currentColor; border-radius: 30px; padding: 8px 22px 6px; font-size: 22px; opacity: .85; }
  .flab { font-size: 24px; opacity: .7; }
  .dot { display: inline-block; width: 14px; height: 14px; border-radius: 50%; flex: none; background: var(--acc); }
  /* phone */
  .phone { position: absolute; border-radius: 56px; background: #0c0c0c; box-shadow: 0 0 0 4px #2c2c2c, 0 30px 80px rgba(0,0,0,.45); overflow: hidden; }
  .phone .notch { position: absolute; left: 50%; top: 14px; width: 120px; height: 30px; margin-left: -60px; border-radius: 15px; background: #000; z-index: 3; }
  .phone .scr { position: absolute; inset: 10px; border-radius: 46px; overflow: hidden; background: #f6f5f1; color: #111; }
  .card { position: absolute; left: 18px; right: 18px; border-radius: 22px; background: #ffffff; box-shadow: 0 2px 0 rgba(0,0,0,.06); padding: 16px; box-sizing: border-box; color: #111; }
  .card .hd { display: flex; align-items: center; gap: 10px; font: 700 20px "Instrument Sans", sans-serif; }
  .card .av { width: 40px; height: 40px; border-radius: 50%; background: #cfcac0; flex: none; }
  .card .sp { font: 500 15px "IBM Plex Mono", monospace; letter-spacing: .08em; color: #777; display: block; }
  .card .tx2 { font: 500 24px/1.3 "Instrument Sans", sans-serif; margin-top: 12px; }
  .card .im { margin-top: 12px; height: 150px; border-radius: 14px; background: #e3dfd6; }
  .note { position: absolute; left: 16px; right: 16px; border-radius: 20px; background: rgba(255,255,255,.96); color: #111; padding: 14px 16px; box-sizing: border-box;
    box-shadow: 0 8px 24px rgba(0,0,0,.18); font: 500 19px/1.35 "IBM Plex Mono", monospace; letter-spacing: .04em; }
  .note b { font: 700 22px "Instrument Sans", sans-serif; letter-spacing: 0; display: block; margin-bottom: 4px; }
  /* end cards */
  .eb { position: absolute; left: 0; top: -43px; width: 1080px; }
  .eb img { display: block; width: 1080px; height: auto; }
  #smono { top: 250px; font: 700 300px/1 "Fraunces", serif; color: #ffffff; letter-spacing: -0.02em; }
  .arc { position: absolute; left: 120px; width: 840px; height: 84px; transform-origin: 50% 50%; }
  #sline { top: 610px; color: rgba(255,255,255,.7); font-size: 22px; letter-spacing: .22em; }
  #stitle .in { color: #ffffff; }
  .tagl { top: 1192px; color: #ffffff; font: 500 28px "Instrument Sans", sans-serif; letter-spacing: .26em; }
  #fmi { top: 1262px; color: #ffffff; font-size: 30px; letter-spacing: .3em; }
  #pill { position: absolute; }
  #pill svg.ol { position: absolute; inset: 0; overflow: visible; }
  #pill .row { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; gap: 26px; }
  #pill .ico { width: 64px; height: 64px; flex: none; }
  #pill .dv { width: 5px; height: 58px; background: currentColor; border-radius: 2px; flex: none; }
  #pill .tx { font: 700 54px/1 "Instrument Sans", sans-serif; letter-spacing: -0.01em; white-space: nowrap; }
  #pill .q .c { display: inline-block; }
  /* overlays */
  #flash { position: absolute; inset: 0; z-index: 70; background: #ffffff; opacity: 0; }
  #wipe { position: absolute; top: 0; bottom: 0; width: 1200px; left: -1200px; z-index: 60; background: var(--bg); }
  #wipe i { position: absolute; right: 0; top: 0; bottom: 0; width: 12px; background: var(--acc); }
'''

JS_HEAD = r'''
  window.__timelines = window.__timelines || {};
  const tl = gsap.timeline({ paused: true });
  const P = __BEAT__, SC = __SC__, END = __END__, DUR = +(__TOTAL__ * P).toFixed(4);
  const B = n => +(n * P).toFixed(4);
  let cur = "s1"; const A = l => B(SC[cur] + l);      // local beat -> seconds in the current scene
  const E = { in: "expo.out", ui: "back.out(1.5)" };
  function wordsAt(sel, beats) {
    const ws = document.querySelectorAll(sel + " .w");
    ws.forEach((w, i) => tl.fromTo(w, { y: 24, opacity: 0 }, { y: 0, opacity: 1, duration: 0.22, ease: E.in }, A(beats[Math.min(i, beats.length - 1)])));
  }
  const from = (b0, n, step = 0.5) => Array.from({ length: n }, (_, i) => b0 + i * step);
  const punch = (sel, l, k = 1.06) => tl.to(sel, { keyframes: { scale: [k, 1] }, duration: 0.35, ease: "expo.out" }, A(l));
  const flash = (l, a = 0.35) => { tl.set("#flash", { opacity: a }, A(l)); tl.to("#flash", { opacity: 0, duration: 0.35, ease: "power2.out" }, A(l) + 0.001); };
  const pulse = (sel, l0, l1, amt = 0.025, step = 1) => { for (let l = l0; l < l1; l += step) tl.to(sel, { keyframes: { scale: [1 + amt, 1] }, duration: 0.26, ease: "power2.out" }, A(l)); };
  const pop = (sel, l, f, d = 0.35) => { tl.set(sel, Object.assign({ opacity: 0 }, f), 0); tl.to(sel, { opacity: 1, x: 0, y: 0, scale: 1, duration: d, ease: E.ui }, A(l)); };
  const fadeUp = (sel, l) => { tl.set(sel, { opacity: 0, y: 14 }, 0); tl.to(sel, { opacity: 1, y: 0, duration: 0.3, ease: E.in }, A(l)); };
  const fadeOut = (sel, l, d = 0.15) => tl.to(sel, { opacity: 0, y: -10, duration: d, ease: "power2.in" }, A(l));
  const swing = (sel, l, a = 16, d = 1.5) => tl.to(sel, { keyframes: { rotation: [a, -a * 0.6, a * 0.32, -a * 0.14, a * 0.05, 0] }, duration: d, ease: "sine.inOut" }, A(l));
  const count = (sel, l, to, d, fmt = n => String(n), ease = "power3.out", fromV = 0) => { const o = { v: fromV }; const el = document.querySelector(sel);
    tl.to(o, { v: to, duration: d, ease, onUpdate: () => { el.textContent = fmt(Math.round(o.v)); } }, A(l)); };
  const euro = n => "€" + (n >= 1000 ? Math.floor(n / 1000) + "," + String(n % 1000).padStart(3, "0") : n);
  const draw = (sel, l, d, fromF = 1, toF = 0) => { const el = document.querySelector(sel); const L = el.getTotalLength ? el.getTotalLength() : 1200;
    tl.set(sel, { strokeDasharray: L, strokeDashoffset: L * fromF }, 0); if (fromF >= 1) { tl.set(sel, { opacity: 0 }, 0); tl.set(sel, { opacity: 1 }, A(l)); } tl.to(sel, { strokeDashoffset: L * toF, duration: d, ease: "power2.inOut" }, A(l)); return L; };
  const shot = (cam, s) => { const a = B(SC[s]), b = B(END[s]);
    tl.set(cam, { scale: 1.04 }, a);
    tl.to(cam, { keyframes: [{ scale: 1, duration: 0.4, ease: "expo.out" }, { scale: 1.025, duration: Math.max(0.1, b - a - 0.4), ease: "none" }] }, a); };
  const lineWipe = l => tl.fromTo("#wipe", { x: 0 }, { x: 2400, duration: 0.45, ease: "power2.inOut" }, A(l) - 0.23);
  tl.fromTo("#grain", { x: 0, y: 0 }, { x: 140, y: -120, duration: DUR, ease: `steps(${Math.floor(DUR * 12)})` }, 0);
  Object.keys(SC).forEach(s => { if (s !== "s1") shot("#cam_" + s, s); });
  // callout scene: on screen at t=0, slams in, then creeps
  tl.fromTo("#cam_s1", { scale: 1.16 }, { scale: 1.0, duration: 0.5, ease: "expo.out" }, 0);
  tl.to("#cam_s1", { scale: 1.03, duration: B(END.s1) - 0.5, ease: "none" }, 0.5);
'''

END_SA_JS = r'''
  tl.set("#eb1", { opacity: 0, scale: 1.15 }, 0); tl.to("#eb1", { opacity: 1, scale: 1, duration: 0.5, ease: "expo.out" }, A(0));
  tl.set("#eb2", { opacity: 0, y: 60 }, 0); tl.to("#eb2", { opacity: 1, y: 0, duration: 0.35, ease: "expo.out" }, A(1));
  pillIn(2);
  tl.set("#eb4", { opacity: 0, y: 14 }, 0); tl.to("#eb4", { opacity: 1, y: 0, duration: 0.3, ease: E.in }, A(2.75 + NCH * 0.25));
'''
END_SL_JS = r'''
  tl.set("#smono", { opacity: 0, y: 40, scale: 1.18 }, 0); tl.to("#smono", { opacity: 1, y: 0, scale: 1, duration: 0.45, ease: "expo.out" }, A(0));
  tl.set("#sarc", { scaleX: 0 }, 0); tl.to("#sarc", { scaleX: 1, duration: 0.5, ease: "expo.out" }, A(0.25));
  fadeUp("#sline", 0.5);
  tl.set("#st1 .in", { yPercent: 115 }, 0); tl.to("#st1 .in", { yPercent: 0, duration: 0.35, ease: "expo.out" }, A(0.75));
  tl.set("#st2 .in", { yPercent: 115 }, 0); tl.to("#st2 .in", { yPercent: 0, duration: 0.35, ease: "expo.out" }, A(1));
  punch("#stitle", 1, 1.05);
  pillIn(2);
  fadeUp("#fmi", 2.75 + NCH * 0.25);
'''
PILL_JS = r'''
  function pillIn(l) {
    const r = document.getElementById("pillR"); const PL = 2 * (r.width.baseVal.value - r.height.baseVal.value) + Math.PI * r.height.baseVal.value;
    tl.set("#pillR", { strokeDasharray: PL, strokeDashoffset: PL }, 0); tl.to("#pillR", { strokeDashoffset: 0, duration: 0.45, ease: "power2.inOut" }, A(l));
    tl.set("#pill .ico", { opacity: 0, scale: 0.3 }, 0); tl.set("#pill .ico", { opacity: 1 }, A(l + 0.25)); tl.to("#pill .ico", { scale: 1, duration: 0.3, ease: "back.out(2.5)" }, A(l + 0.25));
    tl.set("#pill .dv", { scaleY: 0 }, 0); tl.to("#pill .dv", { scaleY: 1, duration: 0.2, ease: E.in }, A(l + 0.5));
    tl.set("#pill .cm", { opacity: 0, x: -14 }, 0); tl.to("#pill .cm", { opacity: 1, x: 0, duration: 0.22, ease: E.in }, A(l + 0.5));
    tl.set("#pill .q .c", { opacity: 0 }, 0);
    for (let i = 0; i < NCH; i++) tl.set("#pill .q .c:nth-child(" + (i + 1) + ")", { opacity: 1 }, A(l + 1 + i * 0.25));
    pulse("#pill", Math.ceil(l + 1.5 + NCH * 0.25), END[cur] - SC[cur], 0.025);
  }
'''


class Cues:
    def __init__(self, sc, beat=P):
        self.sc, self.beat, self.ev, self.drop = sc, beat, [], []
    def at(self, s, l):
        return round((self.sc[s] + l) * self.beat, 4)
    def add(self, s, l, name, g, dt=0.0):
        self.ev.append([max(0.0, self.at(s, l) + dt), name, g])
    def dropout(self, s, l0, l1):
        self.drop.append([self.at(s, l0), self.at(s, l1)])


def build(hf, cues_path, title, palette, scenes, total, css, js, cues, endcard="southline", keyword="", end_lines=("", ""), beat=P, comment="", end_size=150, sa_tagline=None):
    """scenes: list of (id, start_beat, tone, html). The last scene is the end card (html generated here)."""
    sc = {s[0]: s[1] for s in scenes}
    order = [s[0] for s in scenes]
    end = {k: (sc[order[i + 1]] if i + 1 < len(order) else total) for i, k in enumerate(order)}
    B = lambda n: round(n * beat, 4)
    dur = B(total)
    last = order[-1]
    if endcard == "sa":
        ec_html, _, _ = endcard_sa(keyword, sa_tagline); ec_js = END_SA_JS
    else:
        ec_html, _, _ = endcard_southline(end_lines[0], end_lines[1], keyword, palette["--acc"], end_size); ec_js = END_SL_JS
    scenes = [(i, s, t, (ec_html if i == last else h)) for i, s, t, h in scenes]
    clips = "\n".join(
        f'''  <section id="{i}" class="clip scene {t}" data-start="{B(s)}" data-duration="{round(B(end[i]) - B(s), 4)}" data-track-index="1">
    <div class="glow" data-layout-ignore></div>
    <div class="cam" id="cam_{i}">{h}
    </div>
  </section>''' for i, s, t, h in scenes)
    root = ":root { " + " ".join(f"{k}: {v};" for k, v in palette.items()) + " }"
    head = (JS_HEAD.replace("__BEAT__", str(beat)).replace("__SC__", json.dumps(sc)).replace("__END__", json.dumps(end))
            .replace("__TOTAL__", str(total)))
    nch = len(keyword)
    js_all = head + f"\n  const NCH = {nch};\n" + PILL_JS + js + f'\n  // ---------- END CARD ----------\n  cur = "{last}";\n' + ec_js + '\n  window.__timelines["main"] = tl;\n'
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1920" />
<title>{title}</title>
<script src="assets/vendor/gsap.min.js"></script>
<style>
  /* {comment} */
  {root}{BASE_CSS}{css}</style>
</head>
<body>
<div id="root" data-composition-id="main" data-width="1080" data-height="1920" data-duration="{dur}">
  <div id="bg" class="full" data-layout-ignore></div>

{clips}

  <div id="flash" data-layout-ignore></div>
  <div id="wipe" data-layout-ignore><i></i></div>
  <div id="grain" class="full" data-layout-ignore></div>
  <audio id="score" src="assets/audio.wav" data-start="0" data-duration="{dur}" data-track-index="10" data-volume="1"></audio>
</div>

<script>{js_all}</script>
</body>
</html>
'''
    open(hf + "/index.html", "w").write(html)
    # end-card cues (shared)
    c = cues
    c.add(last, 0, "whoosh", 0.35, -0.1); c.add(last, 0, "shimmer", 0.3); c.add(last, 1, "hit", 0.5)
    c.add(last, 2, "swish", 0.25); c.add(last, 2.25, "pop", 0.35)
    for i in range(nch):
        c.add(last, 3 + i * 0.25, "tick", 0.3)
    c.add(last, 3 + nch * 0.25, "ping", 0.3)
    json.dump({"duration": dur, "bpm": round(60 / beat, 2), "dropouts": c.drop, "events": sorted(c.ev)}, open(cues_path, "w"))
    return dur
