#!/usr/bin/env python3
"""Clothing-brands ad, clear cut (v7): one simple story, full sentences, 7 scenes, ~24 s, on the 139.2 BPM grid.
callout -> open loop -> relate (one post that grows) -> problem (answers the question) -> solution -> payoff -> end card.
    python3 gen_clear.py <hyperframes dir> <cues.json>"""
import json, sys

P = 0.43103
B = lambda n: round(n * P, 4)
HF, CUES = sys.argv[1], sys.argv[2]
TOTAL = 56
DUR = B(TOTAL)


def words(s):
    out = []
    for w in s.split():
        pk = w.startswith("*"); w = w.lstrip("*")
        out.append(f'<span class="w{" pk" if pk else ""}">{w}</span>')
    return " ".join(out)


def cap(cid, key, top, size=112, lead="", sub=""):
    ld = f'<span class="ld">{words(lead)}</span>' if lead else ""
    sb = f'<span class="sb">{words(sub)}</span>' if sub else ""
    return f'<div class="cap" id="{cid}" style="top:{top}px;--ks:{size}px">{ld}<span class="kw">{words(key)}</span>{sb}</div>'


HEART = '<svg width="34" height="34" viewBox="0 0 24 24"><path d="M12 21s-7-4.5-9.5-9A5.5 5.5 0 0 1 12 6a5.5 5.5 0 0 1 9.5 6c-2.5 4.5-9.5 9-9.5 9z" fill="#ff3d8b"/></svg>'
TEE = '<svg width="220" height="212" viewBox="0 0 260 250" fill="#111111"><path d="M90 20 L60 28 L10 70 L40 115 L65 98 L65 235 L195 235 L195 98 L220 115 L250 70 L200 28 L170 20 C160 42 100 42 90 20 Z"/></svg>'

S = []
S.append(("s1", 0, 4, "dark", '''
      <div class="ttl" id="t1" style="top:600px"><span class="mask"><span class="in">Clothing</span></span><span class="mask"><span class="in pk" id="t1b">brands.</span></span></div>
      <svg class="arc" id="arc1" style="top:1130px" viewBox="0 0 840 84" data-layout-ignore><path d="M0 74 Q420 -14 840 74 Q420 4 0 74 Z" fill="#ff3d8b"/></svg>
      <div class="ctr qq" id="qq">quick question…</div>'''))
S.append(("s2", 4, 12, "dark", f'''
      <div class="qghost" data-layout-ignore>?</div>
      {cap("c2", "Why does every drop sell to the *same *people?", 600, 112)}'''))
S.append(("s3", 12, 24, "dark", f'''
      {cap("c3a", "You post the drop.", 430, 78)}
      {cap("c3b", "Your followers like it.", 430, 78)}
      {cap("c3c", "The same few people buy.", 430, 78)}
      <div id="postc">
        <div class="ph"><span class="pav"></span><span class="mono">YOUR BRAND</span><span class="dtag mono">DROP 03</span></div>
        <div class="pimg">{TEE}</div>
        <div class="pf" id="likes"><span class="lk">{HEART}<b>41 likes</b></span>
          <span class="avs"><span class="av" id="avAM">AM</span><span class="av" id="avJK">JK</span><span class="av">RB</span></span></div>
      </div>
      <div class="ord" id="or1" style="top:1196px"><span class="av rep">AM</span><span class="ot mono"><b>NEW ORDER · AOIFE M.</b><br><span class="pk">BOUGHT YOUR LAST DROP TOO</span></span></div>
      <div class="ord" id="or2" style="top:1316px"><span class="av rep">JK</span><span class="ot mono"><b>NEW ORDER · JACK K.</b><br><span class="pk">BOUGHT YOUR LAST DROP TOO</span></span></div>'''))
S.append(("s4", 24, 32, "dark", f'''
      {cap("c4", "Because only your *followers ever see it.", 470, 108)}
      <div class="grid" id="g4"></div>
      <div class="legend" id="lg4"><div id="lg4a"><i class="dot pkd"></i>YOUR FOLLOWERS</div><div id="lg4b"><i class="dot gr"></i>EVERYONE ELSE · NEVER SEEN YOUR BRAND</div></div>'''))
S.append(("s5", 32, 42, "light", f'''
      {cap("c5", "We run Facebook & Instagram ads", 430, 108, sub="that show your drop to *new *buyers.")}
      <div class="grid" id="g5"></div>
      <div class="legend" id="lg5"><div id="lg5a"><i class="dot jt"></i>YOUR FOLLOWERS</div><div id="lg5b"><i class="dot pkl"></i>NEW BUYERS, FROM YOUR ADS</div></div>'''))
S.append(("s6", 42, 48, "light", f'''
      {cap("c6", "So your next drop sells to *new *people.", 470, 120)}
      <div class="grid" id="g6"></div>'''))
SC = 1080 / 1170; BANDS = [(441, 802), (832, 1150), (1184, 1326), (1337, 1386)]
def band(i, t0, t1):
    top, bot = round(t0 * SC), round(1735 * SC - t1 * SC)
    return (f'<div class="eb" id="eb{i}" style="clip-path: inset({top}px 0 {bot}px 0); transform-origin: 540px {round((t0 + t1) / 2 * SC)}px">'
            f'<img src="assets/endcard.jpg" alt="" width="1080" height="{round(1735 * SC)}"></div>')
S.append(("s7", 48, 56, "black", "\n      " + "\n      ".join(band(i + 1, *b) for i, b in enumerate(BANDS))))

clips = "\n".join(
    f'''  <section id="{i}" class="clip scene {tone}" data-start="{B(b0)}" data-duration="{round(B(b1) - B(b0), 4)}" data-track-index="1">
    <div class="glow" data-layout-ignore></div>
    <div class="cam" id="cam_{i}">{inner}
    </div>
  </section>''' for i, b0, b1, tone, inner in S)

CSS = '''
  @font-face { font-family: "Instrument Sans"; src: url(assets/fonts/is-500.woff2) format("woff2"); font-weight: 500; }
  @font-face { font-family: "Instrument Sans"; src: url(assets/fonts/is-700.woff2) format("woff2"); font-weight: 700; }
  @font-face { font-family: "Instrument Serif"; src: url(assets/fonts/iserif-italic.woff2) format("woff2"); font-style: italic; font-weight: 400; }
  @font-face { font-family: "Fraunces"; src: url(assets/fonts/fr-700.woff2) format("woff2"); font-weight: 700; }
  @font-face { font-family: "Fraunces"; src: url(assets/fonts/fr-900.woff2) format("woff2"); font-weight: 900; }
  @font-face { font-family: "IBM Plex Mono"; src: url(assets/fonts/plex-500.woff2) format("woff2"); font-weight: 500; }
  :root { --con: #d9d8d3; --jet: #111111; --gra: #5c5c5a; --fog: #bebdb8; --pink: #ff3d8b; --pinkd: #d81b6a; --paper: #efeee9; --jet2: #1d1d1d; --wh: #f4f3ef; }
  html, body { margin: 0; background: var(--jet); }
  body { font-family: "Instrument Sans", sans-serif; -webkit-font-smoothing: antialiased; }
  #root { position: relative; width: 1080px; height: 1920px; overflow: hidden; }
  .full { position: absolute; inset: 0; }
  #bg { z-index: 0; background: var(--jet); }
  #grain { z-index: 90; opacity: .06; mix-blend-mode: overlay; inset: -200px;
    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>"); }
  .scene { position: absolute; inset: 0; z-index: 10; overflow: hidden; }
  .scene.dark { background: var(--jet); color: var(--con); } .scene.light { background: var(--con); color: var(--jet); }
  .scene.black { background: #000; } .black .glow { display: none; }
  .glow { position: absolute; inset: 0; }
  .dark .glow { background: radial-gradient(ellipse 75% 50% at 50% 46%, rgba(255,61,139,.10) 0%, rgba(17,17,17,0) 62%), radial-gradient(ellipse 120% 90% at 50% 45%, rgba(0,0,0,0) 55%, rgba(0,0,0,.5) 100%); }
  .light .glow { background: radial-gradient(ellipse 80% 55% at 50% 45%, rgba(255,255,255,.35) 0%, rgba(255,255,255,0) 65%); }
  .cam { position: absolute; inset: 0; transform-origin: 50% 45%; }
  .mono { font: 500 24px "IBM Plex Mono", monospace; letter-spacing: .12em; }
  .ctr { position: absolute; left: 0; width: 1080px; text-align: center; }
  .cap { position: absolute; left: 60px; width: 960px; text-align: center; transform-origin: 50% 50%; --ks: 112px; }
  .cap .ld { font: italic 400 72px/1.05 "Instrument Serif", serif; opacity: .85; display: block; margin-bottom: 14px; }
  .cap .kw { font-weight: 700; font-size: var(--ks); letter-spacing: -0.04em; line-height: 1.0; display: block; }
  .cap .sb { font: italic 400 70px/1.1 "Instrument Serif", serif; display: block; margin-top: 22px; opacity: .9; }
  .cap .w { display: inline-block; }
  .dark .pk { color: var(--pink); } .light .pk { color: var(--pinkd); }
  .ttl { position: absolute; left: 0; width: 1080px; text-align: center; transform-origin: 50% 50%; }
  .ttl .mask { display: block; overflow: hidden; padding: 0 0 30px; margin-bottom: -30px; }
  .ttl .in { display: inline-block; font: 900 210px/1.0 "Fraunces", serif; letter-spacing: -0.035em; color: var(--wh); }
  .ttl .in.pk { color: var(--pink); }
  .arc { position: absolute; left: 120px; width: 840px; height: 84px; transform-origin: 50% 50%; }
  .qq { top: 1250px; font: italic 400 76px "Instrument Serif", serif; color: var(--con); }
  .qghost { position: absolute; right: -60px; top: 820px; font: 900 1100px/1 "Fraunces", serif; color: transparent; -webkit-text-stroke: 3px var(--pink); opacity: .14; }
  /* relate: one post that grows */
  #postc { position: absolute; left: 270px; top: 560px; width: 540px; height: 600px; border-radius: 30px; background: var(--jet2); color: var(--con); overflow: hidden; }
  #postc .ph { display: flex; align-items: center; gap: 16px; padding: 22px 24px; }
  #postc .pav { width: 46px; height: 46px; border-radius: 50%; background: var(--pink); flex: none; }
  #postc .dtag { margin-left: auto; background: var(--pink); color: var(--jet); padding: 6px 12px 4px; border-radius: 8px; font-size: 20px; }
  #postc .pimg { height: 360px; background: var(--con); display: flex; align-items: center; justify-content: center; }
  #postc .pf { display: flex; align-items: center; justify-content: space-between; padding: 30px 26px; }
  .lk { display: flex; align-items: center; gap: 12px; font-size: 40px; color: var(--wh); } .lk b { font-weight: 700; }
  .avs { display: flex; }
  .av { width: 66px; height: 66px; border-radius: 50%; background: #3a3a3a; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 26px; color: var(--wh); flex: none; border: 3px solid var(--jet2); box-sizing: border-box; }
  .avs .av { margin-left: -4px; }
  .av.rep, .av.hot { box-shadow: 0 0 0 4px var(--pink); }
  .ord { position: absolute; left: 170px; width: 740px; height: 104px; border-radius: 22px; background: var(--jet2); display: flex; align-items: center; gap: 24px; padding: 0 28px; box-sizing: border-box; }
  .ot { font-size: 22px; line-height: 1.6; color: #c9c8c3; } .ot b { color: var(--wh); font-weight: 500; }
  /* crowd of people */
  .grid { position: absolute; left: 172px; top: 960px; width: 736px; height: 400px; transform-origin: 50% 50%; }
  .p { position: absolute; width: 36px; height: 42px; }
  .p::before { content: ""; position: absolute; left: 11px; top: 0; width: 15px; height: 15px; border-radius: 50%; background: currentColor; }
  .p::after { content: ""; position: absolute; left: 3px; top: 18px; width: 31px; height: 20px; border-radius: 16px 16px 5px 5px; background: currentColor; }
  .legend { position: absolute; left: 0; width: 1080px; top: 1400px; text-align: center; font: 500 26px "IBM Plex Mono", monospace; letter-spacing: .12em; line-height: 1.9; }
  .dark .legend { color: #c9c8c3; } .light .legend { color: var(--gra); }
  .dot { display: inline-block; width: 18px; height: 18px; border-radius: 50%; margin-right: 14px; vertical-align: -1px; }
  .dot.pkd { background: var(--pink); } .dot.gr { background: #4a4a4a; } .dot.jt { background: var(--jet); } .dot.pkl { background: var(--pinkd); }
  /* end card: the owner's artwork */
  .eb { position: absolute; left: 0; top: -43px; width: 1080px; }
  .eb img { display: block; width: 1080px; height: auto; }
  /* overlays */
  #flash { position: absolute; inset: 0; z-index: 70; background: #ffffff; opacity: 0; }
  #wipe { position: absolute; top: 0; bottom: 0; width: 1200px; left: -1200px; z-index: 60; background: var(--con); }
  #wipe i { position: absolute; right: 0; top: 0; bottom: 0; width: 10px; background: var(--pink); }
'''

JS = r'''
  window.__timelines = window.__timelines || {};
  const tl = gsap.timeline({ paused: true });
  // Beat grid of the music: 139.2 BPM; the loop starts on a downbeat, so beat n is at n * P seconds.
  const P = 0.43103, B = n => +(n * P).toFixed(4), DUR = B(__TOTAL__);
  const E = { in: "expo.out", ui: "back.out(1.5)" };
  function wordsAt(sel, beats) {
    const ws = document.querySelectorAll(sel + " .w");
    ws.forEach((w, i) => tl.fromTo(w, { y: 24, opacity: 0 }, { y: 0, opacity: 1, duration: 0.22, ease: E.in }, B(beats[Math.min(i, beats.length - 1)])));
  }
  const from = (b0, n, step = 0.5) => Array.from({ length: n }, (_, i) => b0 + i * step);
  const punch = (sel, b, k = 1.06) => tl.to(sel, { keyframes: { scale: [k, 1] }, duration: 0.35, ease: "expo.out" }, B(b));
  const flash = (b, a = 0.4) => { tl.set("#flash", { opacity: a }, B(b)); tl.to("#flash", { opacity: 0, duration: 0.35, ease: "power2.out" }, B(b) + 0.001); };
  const pulse = (sel, b0, b1, amt = 0.025, step = 1) => { for (let b = b0; b < b1; b += step) tl.to(sel, { keyframes: { scale: [1 + amt, 1] }, duration: 0.26, ease: "power2.out" }, B(b)); };
  const pop = (sel, b, f, d = 0.35) => { tl.set(sel, Object.assign({ opacity: 0 }, f), 0); tl.to(sel, { opacity: 1, x: 0, y: 0, scale: 1, duration: d, ease: E.ui }, B(b)); };
  const fadeUp = (sel, b) => { tl.set(sel, { opacity: 0, y: 14 }, 0); tl.to(sel, { opacity: 1, y: 0, duration: 0.3, ease: E.in }, B(b)); };
  const fadeOut = (sel, b) => tl.to(sel, { opacity: 0, y: -10, duration: 0.15, ease: "power2.in" }, B(b));
  // calm camera: each scene lands a touch close and creeps in slowly
  const shot = (cam, b0, b1) => {
    tl.set(cam, { scale: 1.04 }, B(b0));
    tl.to(cam, { keyframes: [{ scale: 1, duration: 0.4, ease: "expo.out" }, { scale: 1.025, duration: Math.max(0.1, B(b1) - B(b0) - 0.4), ease: "none" }] }, B(b0));
  };
  const lineWipe = b => tl.fromTo("#wipe", { x: 0 }, { x: 2400, duration: 0.45, ease: "power2.inOut" }, B(b) - 0.23);
  tl.fromTo("#grain", { x: 0, y: 0 }, { x: 140, y: -120, duration: DUR, ease: `steps(${Math.floor(DUR * 12)})` }, 0);

  // crowd: 16 x 8 people; the followers are the same small group every time
  const COLS = 16, ROWS = 8, CX = 46, CY = 50;
  const inCl = (r, c) => r >= 2 && r <= 5 && c >= 2 && c <= 6 && !((r === 2 || r === 5) && (c === 2 || c === 6));
  const dist = (r, c) => Math.max(Math.max(2 - r, r - 5, 0), Math.max(2 - c, c - 6, 0));
  function crowd(id, base) {
    const g = document.getElementById(id); const all = [], cl = [], rest = [], by = {};
    for (let r = 0; r < ROWS; r++) for (let c = 0; c < COLS; c++) {
      const d = document.createElement("div"); d.className = "p"; d.style.left = (c * CX) + "px"; d.style.top = (r * CY) + "px"; d.style.color = base; g.appendChild(d);
      all.push(d); (inCl(r, c) ? cl : rest).push(d); const k = dist(r, c); (by[k] = by[k] || []).push(d);
    }
    return { all, cl, rest, by };
  }
  const G4 = crowd("g4", "#3a3a3a"), G5 = crowd("g5", "#bdbcb7"), G6 = crowd("g6", "#d81b6a");
  [["s2", 4, 12], ["s3", 12, 24], ["s4", 24, 32], ["s5", 32, 42], ["s6", 42, 48], ["s7", 48, 56]].forEach(([id, a, b]) => shot("#cam_" + id, a, b));

  // ---------- 1 CALLOUT (beats 0–4) ----------
  tl.fromTo("#cam_s1", { scale: 1.18 }, { scale: 1.0, duration: 0.5, ease: "expo.out" }, 0);   // on screen at t=0
  tl.to("#cam_s1", { scale: 1.03, duration: B(4) - 0.5, ease: "none" }, 0.5);
  tl.set("#t1b", { yPercent: 105 }, 0);
  tl.to("#t1b", { yPercent: 0, duration: 0.25, ease: "expo.out" }, B(0.5));
  tl.set("#arc1", { scaleX: 0 }, 0);
  tl.to("#arc1", { scaleX: 1, duration: 0.45, ease: "expo.out" }, B(1));
  punch("#t1", 1, 1.06); flash(1, 0.25);
  fadeUp("#qq", 2);

  // ---------- 2 OPEN LOOP (beats 4–12) ----------
  wordsAt("#c2", from(4, 9));
  tl.fromTo(".qghost", { rotation: -6, y: 30 }, { rotation: 5, y: -30, duration: B(8), ease: "none" }, B(4));

  // ---------- 3 RELATE (beats 12–24): one post, three beats of the story ----------
  wordsAt("#c3a", from(12, 4, 0.25)); pop("#postc", 12.5, { y: 80, scale: 0.94 });
  fadeOut("#c3a", 15.6);
  wordsAt("#c3b", from(16, 4, 0.25)); pop("#likes", 16.5, { y: 20 });
  tl.to("#likes .lk", { keyframes: { scale: [1.15, 1] }, duration: 0.3, ease: "expo.out" }, B(17.5));
  fadeOut("#c3b", 19.6);
  wordsAt("#c3c", from(20, 5, 0.25));
  pop("#or1", 21, { y: 60 }); pop("#or2", 21.5, { y: 60 });
  tl.set(["#avAM", "#avJK"], { boxShadow: "0 0 0 4px #ff3d8b" }, B(22));

  // ---------- 4 PROBLEM (beats 24–32): answers the question ----------
  wordsAt("#c4", from(24, 7));
  fadeUp("#g4", 24.5);
  tl.set(G4.cl, { color: "#ff3d8b" }, B(26));
  pulse("#g4", 26, 27, 0.04);
  fadeUp("#lg4a", 27.5); fadeUp("#lg4b", 28.5);
  tl.to(G4.rest, { keyframes: { opacity: [0.4, 1] }, duration: 0.35, stagger: { each: 0.002, from: "random" } }, B(28.5));

  // ---------- 5 SOLUTION (beats 32–42) ----------
  lineWipe(32);
  tl.set(G5.cl, { color: "#111111" }, B(32));
  wordsAt("#c5 .kw", from(32, 6));
  wordsAt("#c5 .sb", from(35.5, 7));
  [[37, [1]], [37.5, [2]], [38, [3, 4]], [38.5, [5, 6, 7, 8, 9]]].forEach(([b, ks]) => {
    const ps = []; ks.forEach(k => (G5.by[k] || []).forEach(d => ps.push(d)));
    tl.to(ps, { color: "#d81b6a", duration: 0.15, stagger: 0.002 }, B(b));
  });
  fadeUp("#lg5a", 35); fadeUp("#lg5b", 39);

  // ---------- 6 PAYOFF (beats 42–48): closes the open loop ----------
  wordsAt("#c6", from(42, 8, 0.25));
  tl.set(G6.cl, { color: "#111111" }, B(42));
  tl.fromTo("#g6", { scale: 0.9, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.4, ease: "expo.out" }, B(42));
  flash(42, 0.35); pulse("#g6", 44, 48, 0.02);

  // ---------- 7 END CARD (beats 48–56): the owner's artwork, built on the beat ----------
  tl.set("#eb1", { opacity: 0, scale: 1.15 }, 0);
  tl.to("#eb1", { opacity: 1, scale: 1, duration: 0.5, ease: "expo.out" }, B(48));
  tl.set("#eb2", { opacity: 0, y: 60 }, 0);
  tl.to("#eb2", { opacity: 1, y: 0, duration: 0.35, ease: "expo.out" }, B(49));
  tl.set("#eb3", { opacity: 0, scale: 0.88 }, 0);
  tl.to("#eb3", { opacity: 1, scale: 1, duration: 0.4, ease: E.ui }, B(50));
  tl.set("#eb4", { opacity: 0, y: 14 }, 0);
  tl.to("#eb4", { opacity: 1, y: 0, duration: 0.3, ease: E.in }, B(51));
  pulse("#eb3", 52, 56, 0.025);

  window.__timelines["main"] = tl;
'''.replace("__TOTAL__", str(TOTAL))

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1920" />
<title>Southline: Clothing Brands</title>
<script src="assets/vendor/gsap.min.js"></script>
<style>
  /* Palette: Concrete #D9D8D3 / Jet #111111 / Graphite #5C5C5A / accent Signal Pink #FF3D8B (dark) #D81B6A (light)
     clear cut: callout, open loop, relate, problem, solution, payoff, end card (139.2 BPM grid) */{CSS}</style>
</head>
<body>
<div id="root" data-composition-id="main" data-width="1080" data-height="1920" data-duration="{DUR}">
  <div id="bg" class="full" data-layout-ignore></div>

{clips}

  <div id="flash" data-layout-ignore></div>
  <div id="wipe" data-layout-ignore><i></i></div>
  <div id="grain" class="full" data-layout-ignore></div>
  <audio id="score" src="assets/audio.wav" data-start="0" data-duration="{DUR}" data-track-index="10" data-volume="1"></audio>
</div>

<script>{JS}</script>
</body>
</html>
'''
open(HF + "/index.html", "w").write(html)

ev = [[0.0, "hit", 0.6], [B(0.5), "pop", 0.35], [B(1), "shimmer", 0.25], [B(2), "tick", 0.25]]
ev += [[B(b) - 0.1, "swish", 0.25] for b in (4, 12, 24, 42)] + [[B(32) - 0.22, "whoosh", 0.45], [B(48) - 0.1, "whoosh", 0.35]]
ev += [[B(12.5), "pop", 0.35], [B(16.5), "pop", 0.3], [B(17.5), "ping", 0.25], [B(21), "coin", 0.25], [B(21.5), "coin", 0.25]]
ev += [[B(26), "pop", 0.3], [B(27.5), "tick", 0.25], [B(28.5), "tick", 0.25]]
ev += [[B(b), "pop", 0.2] for b in (37, 37.5, 38, 38.5)] + [[B(39), "tick", 0.25]]
ev += [[B(42) - 0.62, "riser", 0.4], [B(42), "hit", 0.75]]
ev += [[B(48), "shimmer", 0.3], [B(49), "hit", 0.55], [B(50), "pop", 0.4], [B(51), "tick", 0.25]]
json.dump({"duration": DUR, "bpm": 139.2, "dropouts": [[B(41.5), B(42)]], "events": sorted(ev)}, open(CUES, "w"))
print("wrote", HF + "/index.html", DUR, "s,", len(ev), "cues")
