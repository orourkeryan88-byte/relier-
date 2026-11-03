#!/usr/bin/env python3
"""Generate the fast-cut (reference-paced) clothing ad: callout -> open loop -> relate -> problem -> solution -> CTA.
Every clip starts on the 139.2 BPM beat grid. Writes index.html + cues.json."""
import json, sys

P = 0.43103
B = lambda n: round(n * P, 4)
HF = sys.argv[1]          # hyperframes dir
CUES = sys.argv[2]
TOTAL = 40
DUR = B(TOTAL)


def cap(cid, lead, key, top, size=None, extra=""):
    def ws(s):
        out = []
        for w in s.split():
            pk = w.startswith("*"); w = w.lstrip("*")
            out.append(f'<span class="w{" pk" if pk else ""}">{w}</span>')
        return " ".join(out)
    st = f'top:{top}px;' + (f'--ks:{size}px;' if size else "")
    ld = f'<span class="ld">{ws(lead)}</span>' if lead else ""
    return f'<div class="cap{extra}" id="{cid}" style="{st}">{ld}<span class="kw">{ws(key)}</span></div>'


# (id, b0, b1, tone, inner html)
F = []
F.append(("f1", 0, 2, "dark", f'''
      <div class="ttl" id="t1" style="top:640px"><span class="mask"><span class="in" id="t1a">Clothing</span></span><span class="mask"><span class="in pk" id="t1b">brands.</span></span></div>
      <svg class="arc" id="arc1" style="top:1170px" viewBox="0 0 840 84" data-layout-ignore><path d="M0 74 Q420 -14 840 74 Q420 4 0 74 Z" fill="#ff3d8b"/></svg>'''))
F.append(("f2", 2, 6, "dark", f'''
      <div class="qghost" data-layout-ignore>?</div>
      {cap("c2", "why does every drop", "sell to the *same people?", 600, 132)}'''))
F.append(("f3", 6, 8, "dark", f'''
      {cap("c3", "", "every. single. *drop.", 560, 124)}
      <div class="gtag mono" id="tag3"><span>DROP 01 · SOLD TO</span><span>DROP 02 · SOLD TO</span><span>DROP 03 · SOLD TO</span></div>
      <div class="grid" id="g3"><div class="ring" id="ring3"></div></div>'''))
F.append(("f4", 8, 10, "light", f'''
      {cap("c4", "you post the", "new drop.", 470)}
      <div id="tee"><div class="live mono">DROP 03 · LIVE</div>
        <svg width="250" height="240" viewBox="0 0 260 250" fill="#d9d8d3"><path d="M90 20 L60 28 L10 70 L40 115 L65 98 L65 235 L195 235 L195 98 L220 115 L250 70 L200 28 L170 20 C160 42 100 42 90 20 Z"/></svg>
        <div class="tn">Heavyweight tee</div></div>'''))
F.append(("f5", 10, 12, "light", f'''
      {cap("c5", "", "story. reel. *post.", 560, 128)}
      <div class="tiles"><div class="tile" id="ti1"><div class="sh story"></div><div class="mono tl">STORY</div></div>
        <div class="tile" id="ti2"><div class="sh reel"></div><div class="mono tl">REEL</div></div>
        <div class="tile" id="ti3"><div class="sh post"></div><div class="mono tl">POST</div></div></div>'''))
heart = '<svg width="38" height="38" viewBox="0 0 24 24"><path d="M12 21s-7-4.5-9.5-9A5.5 5.5 0 0 1 12 6a5.5 5.5 0 0 1 9.5 6c-2.5 4.5-9.5 9-9.5 9z" fill="#ff3d8b"/></svg>'
F.append(("f6", 12, 14, "dark", f'''
      {cap("c6", "and you get", "the *same likes.", 470)}
      <div class="lrow" id="lr1" style="top:960px"><span class="mono">DROP 01</span><span class="lk">{heart}41</span></div>
      <div class="lrow" id="lr2" style="top:1076px"><span class="mono">DROP 02</span><span class="lk">{heart}39</span></div>
      <div class="lrow" id="lr3" style="top:1192px"><span class="mono">DROP 03</span><span class="lk">{heart}42</span></div>'''))
def order(i, top, ini, name, rep):
    return (f'<div class="ord" id="or{i}" style="top:{top}px"><div class="av{" rep" if rep else ""}">{ini}</div>'
            f'<div class="ot mono"><b>NEW ORDER</b> · {name}<br><span class="pk">RETURNING CUSTOMER</span></div></div>')
F.append(("f7", 14, 16, "dark", f'''
      {cap("c7", "and the orders?", "*same faces.", 470)}
      {order(1, 950, "AM", "AOIFE M.", True)}
      {order(2, 1080, "JK", "JACK K.", False)}
      {order(3, 1210, "AM", "AOIFE M.", True)}'''))
F.append(("f8", 16, 18, "light", f'''
      <div class="ghost" data-layout-ignore>clothes</div>
      {cap("c8", "it's not", "the clothes.", 640, 168)}'''))
F.append(("f9", 18, 20, "dark", f'''
      {cap("c9", "it's", "*who sees them.", 520)}
      <div class="grid" id="g9"></div>
      <div class="ctr mono" id="never" style="top:1410px">MOST PEOPLE NEVER SEE IT</div>'''))
F.append(("f10", 20, 22, "dark", f'''
      {cap("c10", "boost it?", "*same crowd.", 470)}
      <div id="boost">Boost post</div><div class="rip" id="rip" data-layout-ignore></div>
      <div class="grid" id="g10" style="top:1030px"></div>'''))
F.append(("f11", 22, 25, "light", f'''
      {cap("c11", "here's what we do.", "Southline", 600, 168)}
      <div class="ctr mono" id="tag11" style="top:950px;line-height:1.6;font-size:30px">FACEBOOK + INSTAGRAM ADS<br>FOR CLOTHING BRANDS</div>'''))
def wk(i, h, t):
    return f'<div class="wk" id="wk{i}"><div class="h mono">WK {i} · NEW AD</div><div class="t">{t}</div></div>'
F.append(("f12", 25, 27, "light", f'''
      {cap("c12", "new ads", "every *week.", 470)}
      {wk(1, "", "Heavyweight tee")}{wk(2, "", "Behind the drop")}{wk(3, "", "Back in stock")}'''))
F.append(("f13", 27, 29, "light", f'''
      {cap("c13", "shown to", "*new buyers.", 520)}
      <div class="grid" id="g13"></div>
      <div class="ctr mono" id="nb" style="top:1410px">+ PEOPLE WHO'VE NEVER SEEN YOU</div>'''))
F.append(("f14", 29, 31, "light", f'''
      {cap("c14", "+ reminders for", "anyone who *looked.", 470)}
      <div id="remind"><div class="h mono">REMINDER · SAW IT, DIDN'T BUY</div><div class="t">Still thinking about the heavyweight tee? Size M left.</div></div>'''))
F.append(("f15", 31, 34, "light", f'''
      {cap("c15", "so your next drop", "reaches *new people.", 470)}
      <div class="grid" id="g15" style="top:1030px"></div>'''))
F.append(("f16", 34, 40, "dark", '''
      <div class="ctr" id="mono">S</div>
      <svg class="arc" id="arc" style="top:468px" viewBox="0 0 840 84" data-layout-ignore><path d="M0 74 Q420 -14 840 74 Q420 4 0 74 Z" fill="#ff3d8b"/></svg>
      <div class="ctr mono" id="sl" style="top:628px;letter-spacing:.22em;color:#a8a7a2">SOUTHLINE · FACEBOOK + INSTAGRAM ADS</div>
      <div class="ttl" id="title" style="top:690px"><span class="mask" id="cl"><span class="in e">Clothing</span></span><span class="mask" id="br"><span class="in e pk">brands.</span></span></div>
      <div id="pill">
        <svg class="ol" viewBox="0 0 780 132" data-layout-ignore><rect id="pillR" x="2" y="2" width="776" height="128" rx="64" fill="none" stroke="#ff3d8b" stroke-width="4"/></svg>
        <div class="row">
          <svg class="ico" viewBox="0 0 74 74"><path d="M14 12 H60 Q66 12 66 18 V46 Q66 52 60 52 H32 L18 64 V52 H14 Q8 52 8 46 V18 Q8 12 14 12 Z" fill="none" stroke="#f4f3ef" stroke-width="4.5" stroke-linejoin="round"/><circle cx="25" cy="32" r="4" fill="#f4f3ef"/><circle cx="37" cy="32" r="4" fill="#f4f3ef"/><circle cx="49" cy="32" r="4" fill="#f4f3ef"/></svg>
          <span class="div"></span>
          <span class="tx"><span class="cm">Comment</span> <span class="q"><span class="c">“D</span><span class="c">R</span><span class="c">O</span><span class="c">P”</span></span></span>
        </div>
      </div>
      <div class="ctr mono" id="fmi" style="top:1292px;font-size:30px;letter-spacing:.3em;color:#d8d7d2">FOR MORE INFO.</div>'''))

clips = "\n".join(
    f'''  <section id="{i}" class="clip scene {tone}" data-start="{B(b0)}" data-duration="{round(B(b1) - B(b0), 4)}" data-track-index="1">
    <div class="glow" data-layout-ignore></div>
    <div class="cam" id="cam_{i}">{inner}
    </div>
  </section>''' for i, b0, b1, tone, inner in F)

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
  #grain { z-index: 90; opacity: .07; mix-blend-mode: overlay; inset: -200px;
    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>"); }
  .scene { position: absolute; inset: 0; z-index: 10; overflow: hidden; }
  .scene.dark { background: var(--jet); color: var(--con); } .scene.light { background: var(--con); color: var(--jet); }
  .glow { position: absolute; inset: 0; }
  .dark .glow { background: radial-gradient(ellipse 75% 50% at 50% 46%, rgba(255,61,139,.11) 0%, rgba(17,17,17,0) 62%), radial-gradient(ellipse 120% 90% at 50% 45%, rgba(0,0,0,0) 55%, rgba(0,0,0,.5) 100%); }
  .light .glow { background: radial-gradient(ellipse 80% 55% at 50% 45%, rgba(255,255,255,.35) 0%, rgba(255,255,255,0) 65%); }
  .cam { position: absolute; inset: 0; transform-origin: 50% 45%; }
  .mono { font: 500 26px "IBM Plex Mono", monospace; letter-spacing: .14em; }
  .ctr { position: absolute; left: 0; width: 1080px; text-align: center; }
  .dark .ctr.mono { color: #a8a7a2; } .light .ctr.mono { color: var(--gra); }
  .cap { position: absolute; left: 50px; width: 980px; text-align: center; transform-origin: 50% 50%; --ks: 124px; }
  .cap .ld { font: italic 400 76px/1.05 "Instrument Serif", serif; opacity: .85; display: block; margin-bottom: 14px; }
  .cap .kw { font-weight: 700; font-size: var(--ks); letter-spacing: -0.045em; line-height: .98; display: block; }
  .cap .w { display: inline-block; }
  .dark .pk { color: var(--pink); } .light .pk { color: var(--pinkd); }
  .ul { position: absolute; left: 0; right: 0; bottom: -6px; height: 14px; border-radius: 4px; background: var(--pinkd); transform-origin: 0 50%; display: block; }
  .ttl { position: absolute; left: 0; width: 1080px; text-align: center; transform-origin: 50% 50%; }
  .ttl .mask { display: block; overflow: hidden; padding: 0 0 30px; margin-bottom: -30px; }
  .ttl .in { display: inline-block; font: 900 210px/1.0 "Fraunces", serif; letter-spacing: -0.035em; color: var(--wh); }
  .ttl .in.e { font-size: 184px; }
  .ttl .in.pk { color: var(--pink); }
  .arc { position: absolute; left: 120px; width: 840px; height: 84px; transform-origin: 50% 50%; }
  .qghost { position: absolute; right: -60px; top: 760px; font: 900 1100px/1 "Fraunces", serif; color: transparent; -webkit-text-stroke: 3px var(--pink); opacity: .16; }
  .ghost { position: absolute; left: -30px; top: 1080px; font-weight: 700; font-size: 330px; letter-spacing: -0.06em; line-height: 1; white-space: nowrap;
    color: transparent; -webkit-text-stroke: 2px currentColor; opacity: .1; }
  /* buyer grid */
  .grid { position: absolute; left: 164px; top: 1000px; width: 752px; height: 372px; transform-origin: 50% 50%; }
  .sq { position: absolute; width: 30px; height: 30px; border-radius: 6px; }
  .dark .sq { background: #2b2b2b; } .light .sq { background: #c4c3be; }
  .ring { position: absolute; left: 104px; top: 104px; width: 202px; height: 164px; border: 4px solid var(--pink); border-radius: 18px; box-sizing: border-box; z-index: 2; }
  .gtag { position: absolute; left: 164px; top: 950px; height: 34px; width: 500px; color: #9d9c97; }
  .gtag span { position: absolute; left: 0; top: 0; }
  /* relate */
  #tee { position: absolute; left: 330px; top: 900px; width: 420px; height: 470px; border-radius: 34px; background: var(--jet); color: var(--con); }
  #tee svg { display: block; margin: 92px auto 0; }
  #tee .live { position: absolute; left: 24px; top: 24px; background: var(--pink); color: var(--jet); padding: 8px 14px 6px; border-radius: 10px; font-size: 20px; }
  #tee .tn { text-align: center; font-weight: 700; font-size: 36px; margin-top: 14px; }
  .tiles { position: absolute; left: 0; top: 960px; width: 1080px; height: 320px; }
  .tile { position: absolute; top: 0; width: 260px; height: 320px; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; }
  #ti1 { left: 140px; } #ti2 { left: 410px; } #ti3 { left: 680px; }
  .sh { flex: none; } .tl { margin-top: 20px; color: var(--gra); }
  .story { width: 190px; height: 190px; border-radius: 50%; background: #c4c3be; box-shadow: 0 0 0 8px var(--con), 0 0 0 16px var(--pinkd); margin-bottom: 30px; }
  .reel { width: 150px; height: 260px; border-radius: 22px; background: var(--jet); }
  .post { width: 210px; height: 210px; border-radius: 18px; background: #c4c3be; border: 4px solid var(--jet); box-sizing: border-box; margin-bottom: 25px; }
  .lrow { position: absolute; left: 230px; width: 620px; height: 96px; border-radius: 22px; background: var(--jet2); display: flex; align-items: center; justify-content: space-between;
    padding: 0 34px; box-sizing: border-box; color: #c9c8c3; }
  .lk { display: flex; align-items: center; gap: 14px; font-weight: 700; font-size: 50px; color: var(--wh); }
  .ord { position: absolute; left: 150px; width: 780px; height: 112px; border-radius: 22px; background: var(--jet2); display: flex; align-items: center; gap: 24px; padding: 0 28px; box-sizing: border-box; }
  .av { width: 68px; height: 68px; border-radius: 50%; background: #3a3a3a; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 28px; color: var(--wh); flex: none; }
  .av.rep { box-shadow: 0 0 0 4px var(--pink); }
  .ot { font-size: 23px; line-height: 1.5; color: #c9c8c3; } .ot b { color: var(--wh); font-weight: 500; }
  /* problem */
  #boost { position: absolute; left: 380px; top: 860px; width: 320px; height: 100px; border-radius: 50px; background: var(--con); color: var(--jet); font-weight: 700; font-size: 44px;
    display: flex; align-items: center; justify-content: center; }
  .rip { position: absolute; left: 480px; top: 850px; width: 120px; height: 120px; border-radius: 50%; border: 4px solid var(--pink); box-sizing: border-box; opacity: 0; }
  /* solution */
  .wk { position: absolute; left: 240px; top: 1060px; width: 600px; height: 220px; border-radius: 24px; background: var(--jet); color: var(--con); padding: 26px; box-sizing: border-box; transform-origin: 50% 0%; }
  .wk .h { font-size: 20px; color: #9d9c97; } .wk:not(#wk3) { background: #262626; } .wk .t { font-weight: 700; font-size: 52px; margin-top: 22px; letter-spacing: -0.02em; }
  #remind { position: absolute; left: 140px; top: 1010px; width: 800px; padding: 28px 30px; border-radius: 24px; background: var(--paper); border: 2px solid #c4c3be; color: var(--jet); box-sizing: border-box; }
  #remind .h { font-size: 20px; color: var(--gra); } #remind .t { font-weight: 700; font-size: 44px; margin-top: 12px; line-height: 1.1; }
  /* end card */
  #mono { top: 268px; font: 700 340px/1 "Fraunces", serif; color: var(--wh); letter-spacing: -0.02em; }
  #pill { position: absolute; left: 150px; top: 1104px; width: 780px; height: 132px; }
  #pill svg.ol { position: absolute; inset: 0; overflow: visible; }
  #pill .row { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; gap: 30px; }
  #pill .ico { width: 74px; height: 74px; flex: none; }
  #pill .div { width: 4px; height: 66px; background: var(--pink); border-radius: 2px; flex: none; }
  #pill .tx { font: 700 58px/1 "Instrument Sans", sans-serif; color: var(--wh); letter-spacing: -0.01em; white-space: nowrap; }
  #pill .q { color: var(--pink); } #pill .q .c { display: inline-block; }
  /* overlays */
  #flash { position: absolute; inset: 0; z-index: 70; background: #ffffff; opacity: 0; }
  #wipe { position: absolute; top: 0; bottom: 0; width: 1200px; left: -1200px; z-index: 60; background: var(--con); }
  #wipe i { position: absolute; right: 0; top: 0; bottom: 0; width: 10px; background: var(--pink); }
  #streak { position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; z-index: 60; opacity: 0;
    background: repeating-linear-gradient(0deg, rgba(217,216,211,.16) 0 3px, transparent 3px 22px); }
'''

JS = r'''
  window.__timelines = window.__timelines || {};
  const tl = gsap.timeline({ paused: true });
  // Beat grid of the music: 139.2 BPM; the loop starts on a downbeat, so beat n is at n * P seconds.
  const P = 0.43103, B = n => +(n * P).toFixed(4), DUR = B(__TOTAL__);
  const E = { in: "expo.out", ui: "back.out(1.6)" };
  function wordsAt(capSel, beats) {
    const ws = document.querySelectorAll(capSel + " .w");
    ws.forEach((w, i) => tl.fromTo(w, { y: 30, opacity: 0, scale: 1.1 }, { y: 0, opacity: 1, scale: 1, duration: 0.16, ease: E.in }, B(beats[Math.min(i, beats.length - 1)])));
  }
  const punch = (sel, b, k = 1.12) => tl.to(sel, { keyframes: { scale: [k, 1] }, duration: 0.3, ease: "expo.out" }, B(b));
  const flash = (b, a = 0.5) => { tl.set("#flash", { opacity: a }, B(b)); tl.to("#flash", { opacity: 0, duration: 0.3, ease: "power2.out" }, B(b) + 0.001); };
  const pulse = (sel, b0, b1, amt = 0.035, step = 1) => { for (let b = b0; b < b1; b += step) tl.to(sel, { keyframes: { scale: [1 + amt, 1] }, duration: 0.24, ease: "power2.out" }, B(b)); };
  const pop = (sel, b, from, d = 0.3) => { tl.set(sel, Object.assign({ opacity: 0 }, from), 0); tl.to(sel, { opacity: 1, x: 0, y: 0, scale: 1, duration: d, ease: E.ui }, B(b)); };
  const fadeUp = (sel, b) => { tl.set(sel, { opacity: 0, y: 16 }, 0); tl.to(sel, { opacity: 1, y: 0, duration: 0.25, ease: E.in }, B(b)); };
  // every shot: lands punched-in, settles fast, then keeps creeping in (no static frames)
  const shot = (cam, b0, b1, k = 1.07) => {
    tl.set(cam, { scale: k }, B(b0));
    tl.to(cam, { keyframes: [{ scale: 1, duration: 0.3, ease: "expo.out" }, { scale: 1.035, duration: Math.max(0.1, B(b1) - B(b0) - 0.3), ease: "none" }] }, B(b0));
  };
  const lineWipe = b => tl.fromTo("#wipe", { x: 0 }, { x: 2400, duration: 0.42, ease: "power2.inOut" }, B(b) - 0.22);
  const whip = (outCam, b) => {
    tl.fromTo("#streak", { opacity: 0, x: 0 }, { keyframes: { opacity: [0, 1, 0], x: [0, -220, -440] }, duration: 0.3, ease: "power2.inOut" }, B(b) - 0.15);
    tl.to(outCam, { x: -320, duration: 0.15, ease: "power3.in" }, B(b) - 0.15);
  };
  tl.fromTo("#grain", { x: 0, y: 0 }, { x: 140, y: -120, duration: DUR, ease: `steps(${Math.floor(DUR * 12)})` }, 0);

  // buyer grid: 20 x 10 squares; the "followers" cluster is the same block every time
  const COLS = 20, ROWS = 10, CELL = 38;
  const inCluster = (r, c) => r >= 3 && r <= 6 && c >= 3 && c <= 7 && !((r === 3 || r === 6) && (c === 3 || c === 7));
  const dist = (r, c) => Math.max(Math.max(3 - r, r - 6, 0), Math.max(3 - c, c - 7, 0));
  function grid(id) {
    const g = document.getElementById(id); const all = [], cl = [], rest = [], by = {};
    for (let r = 0; r < ROWS; r++) for (let c = 0; c < COLS; c++) {
      const d = document.createElement("div"); d.className = "sq"; d.style.left = (c * CELL) + "px"; d.style.top = (r * CELL) + "px"; g.appendChild(d);
      all.push(d); (inCluster(r, c) ? cl : rest).push(d); const k = dist(r, c); (by[k] = by[k] || []).push(d);
    }
    return { all, cl, rest, by };
  }
  const G3 = grid("g3"), G9 = grid("g9"), G10 = grid("g10"), G13 = grid("g13"), G15 = grid("g15");
  const shotsAt = [["f1",0,2],["f2",2,6],["f3",6,8],["f4",8,10],["f5",10,12],["f6",12,14],["f7",14,16],["f8",16,18],["f9",18,20],["f10",20,22],["f11",22,25],["f12",25,27],["f13",27,29],["f14",29,31],["f15",31,34],["f16",34,40]];
  shotsAt.slice(1).forEach(([id, a, b]) => shot("#cam_" + id, a, b));

  // ---------- 01 CALLOUT (beats 0–2): "Clothing brands." readable in frame 1 ----------
  tl.fromTo("#cam_f1", { scale: 1.22 }, { scale: 1.0, duration: 0.45, ease: "expo.out" }, 0);       // already on screen at t=0, slamming in
  tl.to("#cam_f1", { scale: 1.04, duration: B(2) - 0.45, ease: "none" }, 0.45);
  tl.set("#t1b", { yPercent: 105 }, 0);
  tl.to("#t1b", { yPercent: 0, duration: 0.2, ease: "expo.out" }, B(0.5));
  tl.set("#arc1", { scaleX: 0 }, 0);
  tl.to("#arc1", { scaleX: 1, duration: 0.4, ease: "expo.out" }, B(1));
  punch("#t1", 1, 1.08); flash(1, 0.3);

  // ---------- 02 OPEN LOOP (beats 2–6) ----------
  wordsAt("#c2", [2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 4, 4.5]); punch("#c2", 4);
  tl.fromTo(".qghost", { rotation: -8, y: 40 }, { rotation: 6, y: -40, duration: B(4), ease: "none" }, B(2));

  // ---------- 03 every single drop (beats 6–8) ----------
  wordsAt("#c3", [6, 6.5, 7]);
  tl.set(G3.cl, { backgroundColor: "#ff3d8b" }, B(6));
  tl.set("#tag3 span", { opacity: 0 }, 0);
  [6, 6.5, 7].forEach((b, i) => { tl.set("#tag3 span:nth-child(" + (i + 1) + ")", { opacity: 1 }, B(b)); if (i) tl.set("#tag3 span:nth-child(" + i + ")", { opacity: 0 }, B(b)); });
  tl.set("#ring3", { opacity: 0 }, 0); tl.set("#ring3", { opacity: 1 }, B(6));
  pulse("#g3", 6, 8, 0.05, 0.5);

  // ---------- 04 relate: new drop (beats 8–10) ----------
  lineWipe(8);
  wordsAt("#c4", [8, 8.25, 8.5, 9]);
  pop("#tee", 8, { y: 120, scale: 0.9 });
  // ---------- 05 story. reel. post. (beats 10–12) ----------
  wordsAt("#c5", [10, 10.5, 11]);
  pop("#ti1", 10, { y: 80 }); pop("#ti2", 10.5, { y: 80 }); pop("#ti3", 11, { y: 80 });
  pulse("#c5", 11, 12, 0.04, 0.5);
  // ---------- 06 same likes (beats 12–14) ----------
  whip("#cam_f5", 12);
  wordsAt("#c6", [12, 12.25, 12.5, 12.75, 13, 13.25]);
  pop("#lr1", 12.5, { x: -80 }); pop("#lr2", 13, { x: 80 }); pop("#lr3", 13.5, { x: -80 });
  // ---------- 07 same faces (beats 14–16) ----------
  wordsAt("#c7", [14, 14.25, 14.5, 15, 15.25]); punch("#c7", 15);
  pop("#or1", 14, { y: 60 }); pop("#or2", 14.5, { y: 60 }); pop("#or3", 15, { y: 60 });

  // ---------- 08 problem: it's not the clothes (beats 16–18) ----------
  whip("#cam_f7", 16);
  wordsAt("#c8", [16, 16.25, 16.75, 17]); punch("#c8", 17);
  tl.fromTo("#f8 .ghost", { x: 0 }, { x: -160, duration: B(2), ease: "none" }, B(16));
  // ---------- 09 it's who sees them (beats 18–20) ----------
  wordsAt("#c9", [18, 18.5, 18.75, 19]); punch("#c9", 19);
  tl.set(G9.cl, { backgroundColor: "#ff3d8b" }, B(18));
  tl.to(G9.rest, { keyframes: { opacity: [0.35, 1] }, duration: 0.3, stagger: { each: 0.0015, from: "random" } }, B(19));
  fadeUp("#never", 19.5);
  // ---------- 10 boost it? same crowd (beats 20–22) ----------
  wordsAt("#c10", [20, 20.25, 21, 21.25]);
  tl.to("#boost", { keyframes: { scale: [0.88, 1] }, duration: 0.2, ease: "power2.out" }, B(20.25));
  tl.set("#rip", { opacity: 0 }, 0);
  tl.set("#rip", { opacity: 1, scale: 1 }, B(20.5));
  tl.to("#rip", { scale: 7, opacity: 0, duration: 0.5, ease: "power2.out" }, B(20.5));
  [20.75, 21, 21.5].forEach(b => { tl.set(G10.cl, { backgroundColor: "#ff3d8b" }, B(b)); tl.to(G10.cl, { backgroundColor: "#2b2b2b", duration: 0.18 }, B(b) + 0.06); });
  tl.set(G10.cl, { backgroundColor: "#ff3d8b" }, B(21.75));

  // ---------- 11 solution: Southline (beats 22–25) ----------
  lineWipe(22);
  wordsAt("#c11", [22, 22.25, 22.5, 22.75, 23]); punch("#c11", 23); flash(23, 0.25);
  fadeUp("#tag11", 23.5);
  // ---------- 12 new ads every week (beats 25–27) ----------
  wordsAt("#c12", [25, 25.25, 25.5, 26]);
  [25, 25.5, 26].forEach((b, i) => {
    pop("#wk" + (i + 1), b, { y: 140 }, 0.2);
    for (let j = 0; j < i; j++) {
      tl.to("#wk" + (j + 1), { y: -(i - j) * 58, scale: 1 - (i - j) * 0.06, duration: 0.2, ease: "power2.out" }, B(b));
      if (j === i - 1) tl.to("#wk" + (j + 1) + " .t", { opacity: 0, duration: 0.12 }, B(b));   // only the front card shows its title
    }
  });
  // ---------- 13 shown to new buyers (beats 27–29) ----------
  wordsAt("#c13", [27, 27.25, 27.5, 28]);
  tl.set(G13.cl, { backgroundColor: "#111111" }, B(27));
  [[27.5, [1, 2]], [28, [3, 4, 5]], [28.5, [6, 7, 8, 9]], [28.75, [10, 11, 12]]].forEach(([b, ks]) => {
    const sq = []; ks.forEach(k => (G13.by[k] || []).forEach(d => sq.push(d)));
    tl.to(sq, { backgroundColor: "#d81b6a", duration: 0.12, stagger: 0.001 }, B(b));
  });
  fadeUp("#nb", 28);
  // ---------- 14 reminders (beats 29–31) ----------
  wordsAt("#c14", [29, 29.25, 29.5, 29.75, 30]); punch("#c14", 30);
  pop("#remind", 29.5, { y: 90, scale: 0.94 });

  // ---------- 15 payoff (beats 31–34): the whole grid lights on beat 32 ----------
  wordsAt("#c15", [31, 31.25, 31.5, 31.75, 32, 32.25, 32.5]);
  tl.set(G15.cl, { backgroundColor: "#111111" }, B(31));
  tl.to(G15.all, { backgroundColor: "#d81b6a", duration: 0.08, stagger: { each: 0.0016, from: "center" } }, B(32));
  flash(32, 0.5); punch("#c15", 32);
  pulse("#g15", 32, 34, 0.04);

  // ---------- 16 CTA end card (beats 34–40): loops back to the opening callout ----------
  tl.set("#mono", { opacity: 0, y: 40, scale: 1.18 }, 0);
  tl.to("#mono", { opacity: 1, y: 0, scale: 1, duration: 0.45, ease: "expo.out" }, B(34));
  tl.set("#arc", { scaleX: 0 }, 0);
  tl.to("#arc", { scaleX: 1, duration: 0.5, ease: "expo.out" }, B(34.25));
  fadeUp("#sl", 34.5);
  tl.set("#cl .in", { yPercent: 115 }, 0);
  tl.to("#cl .in", { yPercent: 0, duration: 0.35, ease: "expo.out" }, B(34.75));
  tl.set("#br .in", { yPercent: 115 }, 0);
  tl.to("#br .in", { yPercent: 0, duration: 0.35, ease: "expo.out" }, B(35));
  punch("#title", 35); flash(35, 0.3);
  const PL = 2 * (776 - 128) + Math.PI * 128;
  tl.set("#pillR", { strokeDasharray: PL, strokeDashoffset: PL }, 0);
  tl.to("#pillR", { strokeDashoffset: 0, duration: 0.45, ease: "power2.inOut" }, B(35.5));
  tl.set("#pill .ico", { opacity: 0, scale: 0.3 }, 0);
  tl.set("#pill .ico", { opacity: 1 }, B(35.75));
  tl.to("#pill .ico", { scale: 1, duration: 0.3, ease: "back.out(2.5)" }, B(35.75));
  tl.set("#pill .div", { scaleY: 0 }, 0);
  tl.to("#pill .div", { scaleY: 1, duration: 0.2, ease: E.in }, B(36));
  tl.set("#pill .cm", { opacity: 0, x: -14 }, 0);
  tl.to("#pill .cm", { opacity: 1, x: 0, duration: 0.22, ease: E.in }, B(36));
  tl.set("#pill .q .c", { opacity: 0 }, 0);
  [0, 1, 2, 3].forEach(i => tl.set("#pill .q .c:nth-child(" + (i + 1) + ")", { opacity: 1 }, B(36.5 + i * 0.25)));
  fadeUp("#fmi", 37.5);
  pulse("#pill", 38, 40, 0.025);

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
  /* Palette: Concrete #D9D8D3 / Jet #111111 / Graphite #5C5C5A / Fog #BEBDB8 / accent Signal Pink #FF3D8B (dark) #D81B6A (light)
     Southline Edit Style · clothing brands · fast cut: callout, open loop, relate, problem, solution, CTA (139.2 BPM grid) */{CSS}</style>
</head>
<body>
<div id="root" data-composition-id="main" data-width="1080" data-height="1920" data-duration="{DUR}">
  <div id="bg" class="full" data-layout-ignore></div>

{clips}

  <div id="flash" data-layout-ignore></div>
  <div id="wipe" data-layout-ignore><i></i></div>
  <div id="streak" data-layout-ignore></div>
  <div id="grain" class="full" data-layout-ignore></div>
  <audio id="score" src="assets/audio.wav" data-start="0" data-duration="{DUR}" data-track-index="10" data-volume="1"></audio>
</div>

<script>{JS}</script>
</body>
</html>
'''
open(HF + "/index.html", "w").write(html)

ev = [[0.0, "hit", 0.65], [B(0.5), "pop", 0.4], [B(1), "shimmer", 0.3]]
for b in [2, 6, 10, 14, 18, 20, 25, 27, 29, 31]:
    ev.append([max(0, B(b) - 0.08), "swish", 0.22])
for b in [8, 22]: ev.append([B(b) - 0.2, "whoosh", 0.45])
for b in [12, 16]: ev.append([B(b) - 0.15, "whoosh", 0.4])
ev += [[B(4), "click", 0.3]] + [[B(b), "pop", 0.3] for b in (6, 6.5, 7)] + [[B(8), "pop", 0.35]]
ev += [[B(b), "click", 0.3] for b in (10, 10.5, 11)] + [[B(b), "pop", 0.25] for b in (12.5, 13, 13.5)]
ev += [[B(b), "coin", 0.22] for b in (14, 14.5, 15)] + [[B(17), "click", 0.3], [B(19), "click", 0.3]]
ev += [[B(20.25), "click", 0.45], [B(20.5), "swish", 0.3]] + [[B(b), "glitch", 0.15] for b in (20.75, 21, 21.5)]
ev += [[B(23), "shimmer", 0.35], [B(23), "click", 0.3]] + [[B(b), "pop", 0.3] for b in (25, 25.5, 26)]
ev += [[B(b), "pop", 0.2] for b in (27.5, 28, 28.5, 28.75)] + [[B(29.5), "ping", 0.35]]
ev += [[B(32) - 0.62, "riser", 0.45], [B(32), "hit", 0.8]]
ev += [[B(34) - 0.1, "whoosh", 0.35], [B(34.25), "shimmer", 0.3], [B(35), "hit", 0.65], [B(35.5), "swish", 0.25], [B(35.75), "pop", 0.35]]
ev += [[B(36.5 + i * 0.25), "tick", 0.3] for i in range(4)] + [[B(37.5), "ping", 0.3]]
json.dump({"duration": DUR, "bpm": 139.2, "dropouts": [[B(31.5), B(32)]], "events": sorted(ev)}, open(CUES, "w"))
print("wrote", HF + "/index.html", DUR, "s,", len(ev), "cues")
