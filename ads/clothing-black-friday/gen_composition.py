#!/usr/bin/env python3
"""Black Friday ad for clothing brands (ad #9): "Your Black Friday sale is a discount for people who'd have paid full price."
Black / Bone / Graphite + silver chrome. One story, 8 scenes, full sentences, on the 139.2 BPM grid (62 beats).
    python3 gen_bf.py <hyperframes dir> <cues.json>"""
import json, sys

P = 0.43103
B = lambda n: round(n * P, 4)
HF, CUES = sys.argv[1], sys.argv[2]
TOTAL = 62
DUR = B(TOTAL)


def words(s):
    out = []
    for w in s.split():
        ch = w.startswith("*"); w = w.lstrip("*")
        out.append(f'<span class="w{" cht" if ch else ""}">{w}</span>')
    return " ".join(out)


def cap(cid, key, top, size=104, lead="", sub="", serif=False):
    ld = f'<span class="ld">{words(lead)}</span>' if lead else ""
    sb = f'<span class="sb">{words(sub)}</span>' if sub else ""
    cls = "kw fr" if serif else "kw"
    return f'<div class="cap" id="{cid}" style="top:{top}px;--ks:{size}px">{ld}<span class="{cls}">{words(key)}</span>{sb}</div>'


def tag(tid, left, top, face_a, face_b="", extra=""):
    fb = f'<div class="tt tb mono">{face_b}</div>' if face_b else ""
    return (f'<div class="tagw" id="{tid}" style="left:{left}px;top:{top}px">'
            f'<i class="str"></i><i class="pin chrome"></i>'
            f'<div class="tag chrome"><i class="hole"></i><div class="tt ta">{face_a}</div>{fb}</div>{extra}</div>')


def field(fid, top):
    return (f'<div class="field" id="{fid}" style="top:{top}px"><div class="fc"><div class="fcl mono">YOUR<br>FOLLOWERS</div>'
            f'<i class="mr" style="left:96px"></i><i class="mr" style="left:136px"></i><i class="mr" style="left:176px"></i></div></div>')


ENV = ('<svg width="150" height="110" viewBox="0 0 150 110"><rect x="4" y="4" width="142" height="102" rx="12" fill="none" stroke="#d6d6d6" stroke-width="6"/>'
       '<path d="M8 12 L75 62 L142 12" fill="none" stroke="#d6d6d6" stroke-width="6" stroke-linejoin="round"/></svg>')
ICO = ('<svg class="ico" viewBox="0 0 74 74"><path d="M14 12 H60 Q66 12 66 18 V46 Q66 52 60 52 H32 L18 64 V52 H14 Q8 52 8 46 V18 Q8 12 14 12 Z" fill="none" '
       'stroke="#ffffff" stroke-width="5" stroke-linejoin="round"/><circle cx="25" cy="32" r="4.2" fill="#ffffff"/><circle cx="37" cy="32" r="4.2" fill="#ffffff"/>'
       '<circle cx="49" cy="32" r="4.2" fill="#ffffff"/></svg>')

def receipt_block(no, name, price):
    return (f'<div class="rb"><div class="r1">ORDER #{no}</div><div class="r2">{name} · €{price}</div>'
            f'<div class="stamp">FOLLOWER SINCE 2023</div></div>')

S = []
S.append(("s1", 0, 5, "dark", f'''
      {tag("tag1", 390, 250, "BLACK<br>FRIDAY")}
      <div class="ttl" id="t1" style="top:840px"><span class="mask"><span class="in">Clothing</span></span><span class="mask"><span class="in" id="t1b">brands.</span></span></div>
      <div class="ctr qq" id="qq">Black Friday's coming.</div>'''))
S.append(("s2", 5, 13, "dark", f'''
      <div class="ghosttag" data-layout-ignore><i class="gs"></i><div class="gt"><i class="gh"></i></div></div>
      {cap("c2", "Who's actually buying your *Black *Friday sale?", 560, 116)}'''))
S.append(("s3", 13, 25, "dark", f'''
      {cap("c3a", "You knock 30% off.", 300, 86)}
      {cap("c3b", "You post it. You email your list.", 300, 86)}
      {cap("c3c", "The orders come in…", 300, 86)}
      {tag("tag3", 390, 470, '<span class="dl mono">DROP 03</span><span class="pr" id="p60">€60<i class="strike" id="strike"></i></span><span class="pr2" id="p42">€42</span>',
           extra='<div class="sticker" id="stk">–30%</div>')}
      <div class="soc" id="story"><i class="ring"></i><span class="mono">STORY</span></div>
      <div class="soc" id="mail" style="top:850px">{ENV}<span class="mono">EMAIL</span></div>
      <div id="printer"><i class="slit"></i></div>
      <div id="rwin"><div id="paper">{receipt_block(1044, "SARAH K.", 42)}{receipt_block(1043, "JACK D.", 42)}{receipt_block(1042, "AOIFE M.", 42)}</div></div>'''))
S.append(("s4", 25, 33, "dark", f'''
      {cap("c4a", "…from people who already follow you.", 300, 86)}
      {cap("c4b", "A lot of them would have paid *full *price.", 300, 86)}
      {field("f4", 640)}
      <div class="ctr mono flab" id="fl4" style="top:1190px">EVERYONE WHO'S NEVER SEEN YOU</div>
      <div class="sticker" id="stk4" style="left:590px;top:720px">–30%</div>'''))
S.append(("s5", 33, 39, "light", f'''
      {tag("tag5", 390, 170, "BLACK<br>FRIDAY", "DISCOUNT<br>FOR<br>REGULARS")}
      {cap("c5", "You gave your regulars a discount.", 850, 112, lead="You didn't get new customers.", serif=True)}'''))
S.append(("s6", 39, 49, "dark", f'''
      {cap("c6", "We run Facebook & Instagram ads", 270, 96, sub="that put your Black Friday drop in front of *new *buyers.")}
      {field("f6", 720)}
      <i class="rip" id="rp1" data-layout-ignore></i><i class="rip" id="rp2" data-layout-ignore></i><i class="rip" id="rp3" data-layout-ignore></i>
      <div class="nc chrome mono" id="nc1" style="left:110px;top:760px">NEW CUSTOMER</div>
      <div class="nc chrome mono" id="nc2" style="left:730px;top:840px">NEW CUSTOMER</div>
      <div class="nc chrome mono" id="nc3" style="left:150px;top:1120px">NEW CUSTOMER</div>
      <div class="nc chrome mono" id="nc4" style="left:700px;top:1150px">NEW CUSTOMER</div>
      <div class="ctr mono flab" id="fl6" style="top:1270px"><i class="dot chrome"></i>NEW BUYERS, FROM YOUR ADS</div>'''))
S.append(("s7", 49, 54, "dark", f'''
      {cap("c7", "Black Friday is *27 *November.", 330, 100)}
      <div id="cal" class="chrome"><div class="cm mono">NOV</div>
        <span class="d" id="d23">23</span><span class="d" id="d24">24</span><span class="d" id="d25">25</span><span class="d" id="d26">26</span><span class="d" id="d27">27</span></div>
      <div class="ctr nite" id="nite">Start your ads now, not the night before.</div>'''))
# end card: the owner's artwork (monogram, "Clothing brands.", FOR MORE INFO.) + our own pill with the Black Friday keyword
SC = 1080 / 1170
def band(i, t0, t1):
    top, bot = round(t0 * SC), round(1735 * SC - t1 * SC)
    return (f'<div class="eb" id="eb{i}" style="clip-path: inset({top}px 0 {bot}px 0); transform-origin: 540px {round((t0 + t1) / 2 * SC)}px">'
            f'<img src="assets/endcard.jpg" alt="" width="1080" height="{round(1735 * SC)}"></div>')
PILL = f'''<div id="pill"><svg class="ol" viewBox="0 0 661 109" data-layout-ignore><rect id="pillR" x="2.75" y="2.75" width="655.5" height="103.5" rx="51.75" fill="none" stroke="#ffffff" stroke-width="5.5"/></svg>
        <div class="row">{ICO}<span class="dv"></span><span class="tx"><span class="cm">Comment</span> <span class="q"><span class="c">“f</span><span class="c">r</span><span class="c">i</span><span class="c">d</span><span class="c">a</span><span class="c">y”</span></span></span></div></div>'''
S.append(("s8", 54, 62, "black", "\n      " + band(1, 441, 802) + "\n      " + band(2, 832, 1150) + "\n      " + PILL + "\n      " + band(4, 1337, 1386)))

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
  :root { --blk: #0a0a0a; --bone: #ede8df; --gra: #4a4a48; --ink: #111111;
    --chrome: linear-gradient(110deg, #7a7a7a 0%, #d9d9d9 16%, #ffffff 28%, #a3a3a3 42%, #f2f2f2 58%, #8c8c8c 76%, #e2e2e2 100%);
    --chrome-t: linear-gradient(110deg, #c4c4c4 0%, #ffffff 22%, #d2d2d2 42%, #ffffff 60%, #bcbcbc 80%, #f2f2f2 100%); }
  html, body { margin: 0; background: var(--blk); }
  body { font-family: "Instrument Sans", sans-serif; -webkit-font-smoothing: antialiased; }
  #root { position: relative; width: 1080px; height: 1920px; overflow: hidden; }
  .full { position: absolute; inset: 0; }
  #bg { z-index: 0; background: var(--blk); }
  #grain { z-index: 90; opacity: .07; mix-blend-mode: overlay; inset: -200px;
    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>"); }
  .scene { position: absolute; inset: 0; z-index: 10; overflow: hidden; --hole: #0a0a0a; }
  .scene.dark { background: var(--blk); color: var(--bone); } .scene.light { background: var(--bone); color: var(--ink); --hole: #ede8df; }
  .scene.black { background: #000; } .black .glow { display: none; }
  .glow { position: absolute; inset: 0; }
  .dark .glow { background: radial-gradient(ellipse 70% 45% at 50% 42%, rgba(255,255,255,.07) 0%, rgba(255,255,255,0) 62%), radial-gradient(ellipse 120% 90% at 50% 45%, rgba(0,0,0,0) 55%, rgba(0,0,0,.6) 100%); }
  .light .glow { background: radial-gradient(ellipse 80% 55% at 50% 40%, rgba(255,255,255,.4) 0%, rgba(255,255,255,0) 65%); }
  .cam { position: absolute; inset: 0; transform-origin: 50% 45%; }
  .mono { font: 500 24px "IBM Plex Mono", monospace; letter-spacing: .14em; }
  .ctr { position: absolute; left: 0; width: 1080px; text-align: center; }
  .chrome { background-color: #d4d4d4; background-image: var(--chrome); background-size: 300% 100%; background-position: 0% 50%; }
  .cht { color: #e4e4e4; background-image: var(--chrome-t); background-size: 300% 100%; background-position: 0% 50%; -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }
  .cap { position: absolute; left: 50px; width: 980px; text-align: center; transform-origin: 50% 50%; --ks: 104px; }
  .cap .ld { font: italic 400 74px/1.05 "Instrument Serif", serif; opacity: .85; display: block; margin-bottom: 18px; }
  .cap .kw { font-weight: 700; font-size: var(--ks); letter-spacing: -0.04em; line-height: 1.02; display: block; }
  .cap .kw.fr { font-family: "Fraunces", serif; font-weight: 900; letter-spacing: -0.03em; }
  .cap .sb { font: italic 400 64px/1.12 "Instrument Serif", serif; display: block; margin-top: 20px; opacity: .9; }
  .cap .w { display: inline-block; padding: 0 0.02em; }
  .ttl { position: absolute; left: 0; width: 1080px; text-align: center; transform-origin: 50% 50%; }
  .ttl .mask { display: block; overflow: hidden; padding: 0 0 30px; margin-bottom: -30px; }
  .ttl .in { display: inline-block; font: 900 200px/1.0 "Fraunces", serif; letter-spacing: -0.035em; color: var(--bone); }
  .qq { top: 1300px; font: italic 400 74px "Instrument Serif", serif; color: var(--bone); opacity: .9; }
  /* swing tag */
  .tagw { position: absolute; width: 300px; height: 560px; transform-origin: 150px 0px; }
  .str { position: absolute; left: 149px; top: 0; width: 2px; height: 150px; background: #bdbdbd; }
  .pin { position: absolute; left: 140px; top: -10px; width: 20px; height: 20px; border-radius: 50%; }
  .tag { position: absolute; left: 0; top: 110px; width: 300px; height: 420px; clip-path: polygon(22% 0, 78% 0, 100% 13%, 100% 100%, 0 100%, 0 13%); color: var(--ink); }
  .hole { position: absolute; left: 131px; top: 22px; width: 38px; height: 38px; border-radius: 50%; background: var(--hole); box-shadow: inset 0 0 0 4px rgba(0,0,0,.25); }
  .tt { position: absolute; left: 0; right: 0; top: 120px; text-align: center; font: 500 40px/1.3 "IBM Plex Mono", monospace; letter-spacing: .18em; color: var(--ink); }
  .tt.tb { opacity: 0; top: 104px; font-size: 34px; }
  .dl { display: block; font-size: 22px; margin-bottom: 18px; color: var(--ink); }
  .pr { position: relative; display: inline-block; font: 900 120px/1 "Fraunces", serif; letter-spacing: -0.03em; color: var(--ink); }
  .strike { position: absolute; left: -10px; right: -10px; top: 52%; height: 10px; border-radius: 5px; background: var(--ink); transform-origin: 0 50%; }
  .pr2 { display: block; margin-top: 18px; font: 900 96px/1 "Fraunces", serif; letter-spacing: -0.03em; color: var(--ink); }
  .sticker { position: absolute; left: 196px; top: 452px; width: 180px; height: 180px; border-radius: 50%; background: var(--bone); color: var(--ink); border: 5px solid var(--ink);
    display: flex; align-items: center; justify-content: center; font: 900 54px "Fraunces", serif; letter-spacing: -0.03em; box-sizing: border-box; transform: rotate(-12deg); }
  .ghosttag { position: absolute; left: 340px; top: 1000px; width: 400px; height: 700px; opacity: .16; transform-origin: 200px 0px; }
  .ghosttag .gs { position: absolute; left: 199px; top: 0; width: 2px; height: 140px; background: #d6d6d6; }
  .ghosttag .gh { position: absolute; left: 176px; top: 30px; width: 48px; height: 48px; border-radius: 50%; border: 4px solid #d6d6d6; box-sizing: border-box; }
  .ghosttag .gt { position: absolute; top: 120px; width: 400px; height: 560px; border: 4px solid #d6d6d6; box-sizing: border-box; clip-path: polygon(22% 0, 78% 0, 100% 13%, 100% 100%, 0 100%, 0 13%); }
  /* relate */
  .soc { position: absolute; left: 700px; top: 620px; width: 200px; display: flex; flex-direction: column; align-items: center; gap: 16px; color: #bdbdbd; }
  .soc .ring { width: 150px; height: 150px; border-radius: 50%; background: #2a2a2a; box-shadow: 0 0 0 7px var(--blk), 0 0 0 14px #d6d6d6; }
  #printer { position: absolute; left: 330px; top: 560px; width: 560px; height: 76px; border-radius: 18px; background: #262626; box-shadow: 0 0 0 2px #3a3a3a inset; }
  #printer .slit { position: absolute; left: 60px; right: 60px; top: 50px; height: 8px; border-radius: 4px; background: #050505; }
  #rwin { position: absolute; left: 390px; top: 614px; width: 440px; height: 780px; overflow: hidden; }
  #paper { position: absolute; left: 0; top: 0; width: 440px; background: var(--bone); color: var(--ink); padding: 10px 28px; box-sizing: border-box;
    background-image: repeating-linear-gradient(0deg, rgba(0,0,0,.025) 0 2px, transparent 2px 6px); }
  .rb { height: 240px; border-bottom: 3px dashed #b9b4aa; position: relative; box-sizing: border-box; padding-top: 34px; }
  .r1 { font: 500 26px "IBM Plex Mono", monospace; letter-spacing: .1em; }
  .r2 { font: 700 40px "Instrument Sans", sans-serif; margin-top: 12px; }
  .stamp { display: inline-block; margin-top: 22px; border: 4px solid var(--ink); border-radius: 8px; padding: 8px 14px 6px; font: 500 22px "IBM Plex Mono", monospace; letter-spacing: .12em; transform: rotate(-4deg); }
  /* field of people who've never seen you */
  .field { position: absolute; left: 83px; width: 914px; height: 506px; }
  .dt { position: absolute; width: 12px; height: 12px; border-radius: 50%; background: #333333; }
  .fc { position: absolute; left: 307px; top: 103px; width: 300px; height: 300px; border-radius: 50%; border: 6px solid #d6d6d6; box-sizing: border-box; background: #121212; }
  .fcl { position: absolute; left: 0; right: 0; top: 70px; text-align: center; font-size: 22px; line-height: 1.4; color: #d6d6d6; }
  .mr { position: absolute; top: 160px; width: 30px; height: 44px; border-radius: 4px; background: var(--bone); }
  .flab { font-size: 24px; color: #a8a8a8; }
  .dot { display: inline-block; width: 18px; height: 18px; border-radius: 50%; margin-right: 14px; vertical-align: -1px; }
  .rip { position: absolute; left: 390px; top: 823px; width: 300px; height: 300px; border-radius: 50%; border: 3px solid #e6e6e6; box-sizing: border-box; opacity: 0; }
  .nc { position: absolute; padding: 12px 18px 10px; border-radius: 10px; font-size: 22px; color: var(--ink); }
  /* urgency */
  #cal { position: absolute; left: 370px; top: 600px; width: 340px; height: 380px; border-radius: 30px; color: var(--ink); overflow: hidden; }
  #cal .cm { position: absolute; left: 0; right: 0; top: 0; height: 84px; line-height: 84px; text-align: center; background: var(--ink); color: #e6e6e6; font-size: 32px; letter-spacing: .3em; }
  #cal .d { position: absolute; left: 0; right: 0; top: 110px; text-align: center; font: 900 210px/1 "Fraunces", serif; letter-spacing: -0.04em; color: var(--ink); }
  .nite { top: 1040px; font: italic 400 70px/1.15 "Instrument Serif", serif; color: var(--bone); padding: 0 90px; box-sizing: border-box; }
  /* end card */
  .eb { position: absolute; left: 0; top: -43px; width: 1080px; }
  .eb img { display: block; width: 1080px; height: auto; }
  #pill { position: absolute; left: 210px; top: 1061px; width: 661px; height: 109px; }
  #pill svg.ol { position: absolute; inset: 0; overflow: visible; }
  #pill .row { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; gap: 26px; }
  #pill .ico { width: 64px; height: 64px; flex: none; }
  #pill .dv { width: 5px; height: 58px; background: #ffffff; border-radius: 2px; flex: none; }
  #pill .tx { font: 700 54px/1 "Instrument Sans", sans-serif; color: #ffffff; letter-spacing: -0.01em; white-space: nowrap; }
  #pill .q .c { display: inline-block; }
  /* overlays */
  #flash { position: absolute; inset: 0; z-index: 70; background: #ffffff; opacity: 0; }
  #wipe { position: absolute; top: 0; bottom: 0; width: 1200px; left: -1200px; z-index: 60; background: var(--blk); }
  #wipe i { position: absolute; right: 0; top: 0; bottom: 0; width: 12px; background-color: #d4d4d4; background-image: var(--chrome); }
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
  const flash = (b, a = 0.35) => { tl.set("#flash", { opacity: a }, B(b)); tl.to("#flash", { opacity: 0, duration: 0.35, ease: "power2.out" }, B(b) + 0.001); };
  const pulse = (sel, b0, b1, amt = 0.025, step = 1) => { for (let b = b0; b < b1; b += step) tl.to(sel, { keyframes: { scale: [1 + amt, 1] }, duration: 0.26, ease: "power2.out" }, B(b)); };
  const pop = (sel, b, f, d = 0.35) => { tl.set(sel, Object.assign({ opacity: 0 }, f), 0); tl.to(sel, { opacity: 1, x: 0, y: 0, scale: 1, duration: d, ease: E.ui }, B(b)); };
  const fadeUp = (sel, b) => { tl.set(sel, { opacity: 0, y: 14 }, 0); tl.to(sel, { opacity: 1, y: 0, duration: 0.3, ease: E.in }, B(b)); };
  const fadeOut = (sel, b) => tl.to(sel, { opacity: 0, y: -10, duration: 0.15, ease: "power2.in" }, B(b));
  // chrome sheen: the highlight glides across a chrome surface
  const sheen = (sel, b, d = 0.9) => tl.fromTo(sel, { backgroundPosition: "100% 50%" }, { backgroundPosition: "0% 50%", duration: d, ease: "power2.inOut" }, B(b));
  // damped swing of a hanging tag
  const swing = (sel, b, a = 16, d = 1.5) => tl.to(sel, { keyframes: { rotation: [a, -a * 0.6, a * 0.32, -a * 0.14, a * 0.05, 0] }, duration: d, ease: "sine.inOut" }, B(b));
  const shot = (cam, b0, b1) => {
    tl.set(cam, { scale: 1.04 }, B(b0));
    tl.to(cam, { keyframes: [{ scale: 1, duration: 0.4, ease: "expo.out" }, { scale: 1.025, duration: Math.max(0.1, B(b1) - B(b0) - 0.4), ease: "none" }] }, B(b0));
  };
  const lineWipe = b => tl.fromTo("#wipe", { x: 0 }, { x: 2400, duration: 0.45, ease: "power2.inOut" }, B(b) - 0.23);
  tl.fromTo("#grain", { x: 0, y: 0 }, { x: 140, y: -120, duration: DUR, ease: `steps(${Math.floor(DUR * 12)})` }, 0);

  // field of dots = people who've never seen the brand; the ring in the middle = followers
  function dots(id) {
    const f = document.getElementById(id); const by = {}; const all = [];
    for (let r = 0; r < 12; r++) for (let c = 0; c < 20; c++) {
      const x = c * 47 + 3, y = r * 44 + 3, dx = x + 6 - 457, dy = y + 6 - 253, d = Math.sqrt(dx * dx + dy * dy);
      if (d < 175) continue;
      const el = document.createElement("i"); el.className = "dt"; el.style.left = x + "px"; el.style.top = y + "px"; f.insertBefore(el, f.firstChild);
      all.push(el); const k = Math.min(3, Math.floor((d - 175) / 110)); (by[k] = by[k] || []).push(el);
    }
    return { all, by };
  }
  const F4 = dots("f4"), F6 = dots("f6");
  [["s2", 5, 13], ["s3", 13, 25], ["s4", 25, 33], ["s5", 33, 39], ["s6", 39, 49], ["s7", 49, 54], ["s8", 54, 62]].forEach(([id, a, b]) => shot("#cam_" + id, a, b));

  // ---------- 1 CALLOUT (beats 0–5): readable at frame 0; the chrome tag drops in and swings ----------
  tl.fromTo("#cam_s1", { scale: 1.16 }, { scale: 1.0, duration: 0.5, ease: "expo.out" }, 0);
  tl.to("#cam_s1", { scale: 1.03, duration: B(5) - 0.5, ease: "none" }, 0.5);
  tl.set("#t1b", { yPercent: 105 }, 0);
  tl.to("#t1b", { yPercent: 0, duration: 0.25, ease: "expo.out" }, B(0.5));
  tl.set("#tag1", { y: -900 }, 0);
  tl.to("#tag1", { y: 0, duration: 0.42, ease: "back.out(1.3)" }, B(1));
  swing("#tag1", 1.6, 18, 1.6);
  sheen("#tag1 .tag", 2.5);
  punch("#t1", 2, 1.05);
  fadeUp("#qq", 3);

  // ---------- 2 OPEN LOOP (beats 5–13) ----------
  wordsAt("#c2", from(5, 7));
  swing("#s2 .ghosttag", 5, 8, 3.4);
  sheen("#c2 .cht", 9, 1.1);

  // ---------- 3 RELATE (beats 13–25): one tag, then the post, then the receipts ----------
  wordsAt("#c3a", from(13, 5, 0.25));
  tl.set("#tag3", { y: -700 }, 0);
  tl.to("#tag3", { y: 0, duration: 0.4, ease: "back.out(1.3)" }, B(13.25));
  swing("#tag3", 13.75, 10, 1.2);
  tl.set("#strike", { scaleX: 0 }, 0);
  tl.to("#strike", { scaleX: 1, duration: 0.2, ease: "power3.out" }, B(14.5));
  pop("#p42", 15, { y: 30, scale: 0.8 });
  tl.set("#stk", { opacity: 0, scale: 2.2, rotation: -40 }, 0);
  tl.to("#stk", { opacity: 1, scale: 1, rotation: -12, duration: 0.22, ease: "power4.in" }, B(15.5) - 0.2);
  punch("#tag3 .tag", 15.5, 1.04);
  fadeOut("#c3a", 16.6);
  wordsAt("#c3b", from(17, 7, 0.25));
  tl.to("#tag3", { x: -230, scale: 0.86, duration: 0.45, ease: "expo.out" }, B(17));
  pop("#story", 17.5, { x: 60 }); pop("#mail", 18, { x: 60 });
  fadeOut("#c3b", 20.6);
  wordsAt("#c3c", from(21, 4, 0.25));
  tl.to(["#story", "#mail"], { opacity: 0, x: 80, duration: 0.25, ease: "power2.in" }, B(21));
  tl.to("#tag3", { x: -330, y: -60, scale: 0.5, duration: 0.45, ease: "expo.out" }, B(21));
  pop("#printer", 21.25, { y: -40 });
  tl.set("#paper", { y: -780 }, 0);
  tl.set("#rwin", { opacity: 0 }, 0); tl.set("#rwin", { opacity: 1 }, B(21.25));
  [[21.75, -500], [22.75, -250], [23.75, 0]].forEach(([b, y]) => tl.to("#paper", { y, duration: 0.32, ease: "steps(6)" }, B(b)));
  tl.to("#printer", { keyframes: { y: [2, -1, 1, 0] }, duration: 0.32, ease: "none" }, B(21.75));
  tl.to("#printer", { keyframes: { y: [2, -1, 1, 0] }, duration: 0.32, ease: "none" }, B(22.75));
  tl.to("#printer", { keyframes: { y: [2, -1, 1, 0] }, duration: 0.32, ease: "none" }, B(23.75));

  // ---------- 4 PROBLEM (beats 25–33): the orders came from inside the follower ring ----------
  wordsAt("#c4a", from(25, 6, 0.25));
  pop("#f4 .fc", 25.5, { scale: 0.6 });
  tl.set(F4.all, { opacity: 0 }, 0);
  tl.to(F4.all, { opacity: 1, duration: 0.25, stagger: { each: 0.004, from: "random" } }, B(26));
  fadeUp("#fl4", 27.5);
  fadeOut("#c4a", 28.6);
  wordsAt("#c4b", from(29, 9, 0.25));
  tl.set("#stk4", { opacity: 0, scale: 2.4, rotation: -50, x: 220, y: -260 }, 0);
  tl.to("#stk4", { opacity: 1, scale: 1, rotation: -12, x: 0, y: 0, duration: 0.25, ease: "power4.in" }, B(31) - 0.24);
  punch("#f4 .fc", 31, 1.06);

  // ---------- 5 THE STING (beats 33–39): bone, big serif, the tag flips ----------
  wordsAt("#c5 .ld", from(33, 5, 0.25));
  wordsAt("#c5 .kw", from(35, 6, 0.25));
  tl.set("#tag5", { y: -640 }, 0);
  tl.to("#tag5", { y: 0, duration: 0.4, ease: "back.out(1.3)" }, B(33));
  swing("#tag5", 33.5, 9, 1.2);
  tl.to("#tag5 .tag", { scaleX: 0, duration: 0.12, ease: "power2.in" }, B(36.5) - 0.12);
  tl.set("#tag5 .ta", { opacity: 0 }, B(36.5)); tl.set("#tag5 .tb", { opacity: 1 }, B(36.5));
  tl.to("#tag5 .tag", { scaleX: 1, duration: 0.16, ease: "power2.out" }, B(36.5));
  sheen("#tag5 .tag", 36.5, 0.8);
  punch("#c5 .kw", 36.5, 1.05);

  // ---------- 6 SOLUTION (beats 39–49): ripple out past the followers, new customers appear ----------
  lineWipe(39);
  wordsAt("#c6 .kw", from(39, 6));
  wordsAt("#c6 .sb", from(42, 10, 0.25));
  [42, 43, 44].forEach((b, i) => { tl.set("#rp" + (i + 1), { opacity: 0.9, scale: 1 }, B(b)); tl.to("#rp" + (i + 1), { opacity: 0, scale: 3.6, duration: 0.9, ease: "power2.out" }, B(b)); });
  [[42.5, 0], [43, 1], [43.5, 2], [44, 3]].forEach(([b, k]) => tl.to(F6.by[k] || [], { backgroundColor: "#e6e6e6", duration: 0.15, stagger: 0.002 }, B(b)));
  [45, 45.5, 46, 46.5].forEach((b, i) => { pop("#nc" + (i + 1), b, { y: 30, scale: 0.6 }, 0.3); sheen("#nc" + (i + 1), b + 0.5, 0.7); });
  fadeUp("#fl6", 47);

  // ---------- 7 URGENCY (beats 49–54): the date lands on the beat after a drop-out ----------
  wordsAt("#c7", from(49, 5));
  tl.set(["#d24", "#d25", "#d26", "#d27"], { opacity: 0 }, 0);
  [[50, "#d23", "#d24"], [50.5, "#d24", "#d25"], [51, "#d25", "#d26"], [52, "#d26", "#d27"]].forEach(([b, a, c]) => { tl.set(a, { opacity: 0 }, B(b)); tl.set(c, { opacity: 1 }, B(b)); });
  pop("#cal", 49.5, { y: 60, scale: 0.9 });
  punch("#cal", 52, 1.1); flash(52, 0.4); sheen("#cal", 52, 0.9);
  fadeUp("#nite", 52.5);

  // ---------- 8 END CARD (beats 54–62): the owner's artwork + the Black Friday keyword ----------
  tl.set("#eb1", { opacity: 0, scale: 1.15 }, 0);
  tl.to("#eb1", { opacity: 1, scale: 1, duration: 0.5, ease: "expo.out" }, B(54));
  tl.set("#eb2", { opacity: 0, y: 60 }, 0);
  tl.to("#eb2", { opacity: 1, y: 0, duration: 0.35, ease: "expo.out" }, B(55));
  const PL = 2 * (655.5 - 103.5) + Math.PI * 103.5;
  tl.set("#pillR", { strokeDasharray: PL, strokeDashoffset: PL }, 0);
  tl.to("#pillR", { strokeDashoffset: 0, duration: 0.45, ease: "power2.inOut" }, B(56));
  tl.set("#pill .ico", { opacity: 0, scale: 0.3 }, 0);
  tl.set("#pill .ico", { opacity: 1 }, B(56.25));
  tl.to("#pill .ico", { scale: 1, duration: 0.3, ease: "back.out(2.5)" }, B(56.25));
  tl.set("#pill .dv", { scaleY: 0 }, 0);
  tl.to("#pill .dv", { scaleY: 1, duration: 0.2, ease: E.in }, B(56.5));
  tl.set("#pill .cm", { opacity: 0, x: -14 }, 0);
  tl.to("#pill .cm", { opacity: 1, x: 0, duration: 0.22, ease: E.in }, B(56.5));
  tl.set("#pill .q .c", { opacity: 0 }, 0);
  [0, 1, 2, 3, 4, 5].forEach(i => tl.set("#pill .q .c:nth-child(" + (i + 1) + ")", { opacity: 1 }, B(57 + i * 0.25)));
  tl.set("#eb4", { opacity: 0, y: 14 }, 0);
  tl.to("#eb4", { opacity: 1, y: 0, duration: 0.3, ease: E.in }, B(58.75));
  pulse("#pill", 59, 62, 0.025);

  window.__timelines["main"] = tl;
'''.replace("__TOTAL__", str(TOTAL))

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1920" />
<title>Southline: Black Friday</title>
<script src="assets/vendor/gsap.min.js"></script>
<style>
  /* Palette: Black #0A0A0A / Bone #EDE8DF / Graphite #4A4A48 / accent silver chrome (gradient) · ad #9 Black Friday */{CSS}</style>
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

ev = [[0.0, "hit", 0.6], [B(0.5), "pop", 0.3], [B(1), "whoosh", 0.35], [B(1.45), "click", 0.35], [B(2.5), "shimmer", 0.25], [B(3), "tick", 0.2]]
ev += [[B(b) - 0.1, "swish", 0.25] for b in (5, 13, 25, 49)] + [[B(39) - 0.22, "whoosh", 0.45], [B(54) - 0.1, "whoosh", 0.35]]
ev += [[B(13.25), "swish", 0.3], [B(14.5), "swish", 0.35], [B(15), "pop", 0.3], [B(15.5), "hit", 0.45], [B(15.5), "click", 0.4]]
ev += [[B(17.5), "pop", 0.3], [B(18), "pop", 0.3], [B(21.25), "click", 0.3]]
ev += [[B(b) + i * 0.05, "tick", 0.28] for b in (21.75, 22.75, 23.75) for i in range(6)]
ev += [[B(25.5), "pop", 0.3], [B(27.5), "tick", 0.25], [B(31) - 0.05, "whoosh", 0.25], [B(31), "hit", 0.5], [B(31), "click", 0.4]]
ev += [[B(33), "swish", 0.3], [B(36.5) - 0.12, "swish", 0.3], [B(36.5), "hit", 0.7], [B(36.5), "shimmer", 0.25]]
ev += [[B(b), "swish", 0.2] for b in (42, 43, 44)] + [[B(b), "coin", 0.3] for b in (45, 45.5, 46, 46.5)] + [[B(47), "tick", 0.25]]
ev += [[B(49.5), "pop", 0.3]] + [[B(b), "click", 0.3] for b in (50, 50.5, 51)] + [[B(52) - 0.62, "riser", 0.4], [B(52), "hit", 0.8], [B(52), "shimmer", 0.3]]
ev += [[B(54), "shimmer", 0.3], [B(55), "hit", 0.5], [B(56), "swish", 0.25], [B(56.25), "pop", 0.35]]
ev += [[B(57 + i * 0.25), "tick", 0.3] for i in range(6)] + [[B(58.75), "ping", 0.3]]
json.dump({"duration": DUR, "bpm": 139.2, "dropouts": [[B(51.5), B(52)]], "events": sorted(ev)}, open(CUES, "w"))
print("wrote", HF + "/index.html", DUR, "s,", len(ev), "cues")
