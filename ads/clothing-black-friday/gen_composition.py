#!/usr/bin/env python3
"""Black Friday ad v2 (ad #9 v2): "Black Friday looks like a win. It isn't."
callout -> open loop -> WHAT IT LOOKS LIKE (dashboard) -> rewind -> WHAT ACTUALLY HAPPENED -> the cost -> January ->
"Here's what to change." -> the fix -> 27 Nov urgency -> SA end card (Comment "friday").
Black / Bone / Graphite + silver chrome; on the 139.2 BPM grid. Scene timings are local beats from SC[scene].
    python3 gen_bf2.py <hyperframes dir> <cues.json>"""
import json, sys

P = 0.43103
HF, CUES = sys.argv[1], sys.argv[2]
SC = {"s1": 0, "s2": 6, "s3": 13, "s5": 29, "s6": 38, "s7": 43, "s8": 47, "s9": 60, "s10": 66}
TOTAL = 73
ORDER = ["s1", "s2", "s3", "s5", "s6", "s7", "s8", "s9", "s10"]
END = {k: (SC[ORDER[i + 1]] if i + 1 < len(ORDER) else TOTAL) for i, k in enumerate(ORDER)}
B = lambda n: round(n * P, 4)
A = lambda s, l: B(SC[s] + l)          # absolute seconds of local beat l in scene s
DUR = B(TOTAL)


def words(s):
    out = []
    for w in s.split():
        ch = w.startswith("*"); w = w.lstrip("*")
        out.append(f'<span class="w{" cht" if ch else ""}">{w}</span>')
    return " ".join(out)


def cap(cid, key, top, size=84, lead="", sub="", serif=False):
    ld = f'<span class="ld">{words(lead)}</span>' if lead else ""
    sb = f'<span class="sb">{words(sub)}</span>' if sub else ""
    return f'<div class="cap" id="{cid}" style="top:{top}px;--ks:{size}px">{ld}<span class="kw{" fr" if serif else ""}">{words(key)}</span>{sb}</div>'


def tag(tid, left, top, face):
    return (f'<div class="tagw" id="{tid}" style="left:{left}px;top:{top}px"><i class="str"></i><i class="pin chrome"></i>'
            f'<div class="tag chrome"><i class="hole"></i><div class="tt">{face}</div></div></div>')


def field(fid, top):
    return (f'<div class="field" id="{fid}" style="top:{top}px"><div class="fc"><div class="fcl mono">YOUR<br>FOLLOWERS</div>'
            f'<i class="mr" style="left:96px"></i><i class="mr" style="left:136px"></i><i class="mr" style="left:176px"></i></div></div>')


def toast(i, top):
    return (f'<div class="ts" id="ts{i}" style="top:{top}px"><div class="fa"><i class="dot chrome"></i>NEW ORDER · €42</div>'
            f'<div class="bk">↺ FOLLOWER SINCE 2023</div></div>')


ICO = ('<svg class="ico" viewBox="0 0 74 74"><path d="M14 12 H60 Q66 12 66 18 V46 Q66 52 60 52 H32 L18 64 V52 H14 Q8 52 8 46 V18 Q8 12 14 12 Z" fill="none" '
       'stroke="#ffffff" stroke-width="5" stroke-linejoin="round"/><circle cx="25" cy="32" r="4.2" fill="#ffffff"/><circle cx="37" cy="32" r="4.2" fill="#ffffff"/>'
       '<circle cx="49" cy="32" r="4.2" fill="#ffffff"/></svg>')
HIGH = "0,180 110,168 220,150 330,118 440,92 550,64 660,36 780,12"
LOW = "0,250 130,252 260,249 390,253 520,251 650,252 800,250"
SPIKE = "0,70 130,48 260,26 390,12 520,30 650,44 800,58"

S = {}
S["s1"] = ("dark", f'''
      {tag("tag1", 390, 250, "BLACK<br>FRIDAY")}
      <div class="ttl" id="t1" style="top:840px"><span class="mask"><span class="in">Clothing</span></span><span class="mask"><span class="in" id="t1b">brands.</span></span></div>
      <div class="ctr qq" id="qq">Your Black Friday sale might be costing you.</div>''')
S["s2"] = ("dark", f'''
      <div class="ghosttag" data-layout-ignore><i class="gs"></i><div class="gt"><i class="gh"></i></div></div>
      {cap("c2", "Why does Black Friday never *actually *grow your brand?", 560, 112)}''')
S["s3"] = ("dark", f'''
      <div class="ctr lbl mono" id="lbl"><span id="lb1">WHAT IT LOOKS LIKE</span><span id="lb2">WHAT ACTUALLY HAPPENED</span></div>
      {cap("c3a", "On the day, it feels like your best weekend ever.", 360, 80)}
      {cap("c3b", "Almost every order came from people who *already *follow you.", 360, 80)}
      <div id="dash">
        <div class="dh mono"><i class="dot chrome" id="live"></i>BLACK FRIDAY · ORDERS</div>
        <div id="cnt"><span class="mono">ORDERS</span><b id="cn">0</b></div>
        <svg id="ch" viewBox="0 0 780 200" data-layout-ignore><polyline id="ln" points="{HIGH}" fill="none" stroke="#e8e8e8" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>
        {toast(1, 86)}{toast(2, 166)}{toast(3, 246)}
        <div id="tally"><span class="mono">NEW CUSTOMERS</span><b id="nc" class="cht">0</b></div>
        {tag("tag3", 690, -52, "–30%")}
      </div>
      <div id="vhs" data-layout-ignore></div>''')
S["s5"] = ("light", f'''
      {cap("c5a", "A lot of them would have paid full price.", 320, 80)}
      {cap("c5b", "So you gave away €18 on every order.", 320, 80)}
      {tag("tag5", 390, 480, '<span class="dl">DROP 03</span><span class="pr">€60</span>')}
      <div class="sticker" id="stk5">–30%</div>
      <div id="coin" class="chrome">€18</div>
      <div id="gaw"><span class="mono">GIVEN AWAY</span><b id="gv">€0</b></div>''')
S["s6"] = ("dark", f'''
      {cap("c6", "And in January, it's quiet again.", 360, 92)}
      <div id="cal6" class="chrome"><div class="yr mono">2026</div><span class="mo" id="mNOV">NOV</span><span class="mo" id="mDEC">DEC</span><span class="mo" id="mJAN">JAN</span></div>
      <svg id="ch6" viewBox="0 0 800 270" data-layout-ignore><polyline id="ln6" points="{SPIKE}" fill="none" stroke="#e8e8e8" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>
      <div class="ctr mono flab" id="fl6" style="top:1260px">YOUR SALES</div>''')
S["s7"] = ("dark", f'''
      {tag("tag7", 390, 250, "BLACK<br>FRIDAY")}
      {cap("c7", "Here's what to *change.", 960, 130, serif=True)}''')
S["s8"] = ("dark", f'''
      {cap("c8", "We run Facebook & Instagram ads", 230, 88, sub="that put your Black Friday drop in front of people who've *never *seen your brand.")}
      {cap("c8b", "New customers you can sell to *again in January.", 300, 92)}
      {field("f8", 690)}
      <i class="rip" id="rp1" data-layout-ignore></i><i class="rip" id="rp2" data-layout-ignore></i><i class="rip" id="rp3" data-layout-ignore></i>
      <div class="nc chrome mono" id="nc1" style="left:110px;top:720px">NEW CUSTOMER</div>
      <div class="nc chrome mono" id="nc2" style="left:730px;top:800px">NEW CUSTOMER</div>
      <div class="nc chrome mono" id="nc3" style="left:150px;top:1080px">NEW CUSTOMER</div>
      <div class="nc chrome mono" id="nc4" style="left:700px;top:1110px">NEW CUSTOMER</div>
      <svg id="ch8" viewBox="0 0 800 270" data-layout-ignore><polyline id="ln8" points="{LOW}" fill="none" stroke="#e8e8e8" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>
      <div class="ctr mono flab" id="fl8a" style="top:1230px">EVERYONE WHO'S NEVER SEEN YOU</div>
      <div class="ctr mono flab" id="fl8b" style="top:1230px"><i class="dot chrome"></i>NEW CUSTOMERS, FROM YOUR ADS</div>
      <div class="ctr mono flab" id="fl8c" style="top:1230px">YOUR SALES · JANUARY</div>''')
S["s9"] = ("dark", f'''
      {cap("c9", "Black Friday is *27 *November.", 330, 100)}
      <div id="cal" class="chrome"><div class="cm mono">NOV</div>
        <span class="d" id="d24">24</span><span class="d" id="d25">25</span><span class="d" id="d26">26</span><span class="d" id="d27">27</span></div>
      <div class="ctr nite" id="nite">Start your ads now, not the night before.</div>''')
SCL = 1080 / 1170
def band(i, t0, t1):
    top, bot = round(t0 * SCL), round(1735 * SCL - t1 * SCL)
    return (f'<div class="eb" id="eb{i}" style="clip-path: inset({top}px 0 {bot}px 0); transform-origin: 540px {round((t0 + t1) / 2 * SCL)}px">'
            f'<img src="assets/endcard.jpg" alt="" width="1080" height="{round(1735 * SCL)}"></div>')
PILL = f'''<div id="pill"><svg class="ol" viewBox="0 0 661 109" data-layout-ignore><rect id="pillR" x="2.75" y="2.75" width="655.5" height="103.5" rx="51.75" fill="none" stroke="#ffffff" stroke-width="5.5"/></svg>
        <div class="row">{ICO}<span class="dv"></span><span class="tx"><span class="cm">Comment</span> <span class="q"><span class="c">“f</span><span class="c">r</span><span class="c">i</span><span class="c">d</span><span class="c">a</span><span class="c">y”</span></span></span></div></div>'''
S["s10"] = ("black", "\n      " + band(1, 441, 802) + "\n      " + band(2, 832, 1150) + "\n      " + PILL + "\n      " + band(4, 1337, 1386))

clips = "\n".join(
    f'''  <section id="{k}" class="clip scene {S[k][0]}" data-start="{B(SC[k])}" data-duration="{round(B(END[k]) - B(SC[k]), 4)}" data-track-index="1">
    <div class="glow" data-layout-ignore></div>
    <div class="cam" id="cam_{k}">{S[k][1]}
    </div>
  </section>''' for k in ORDER)

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
  .light .cht { color: var(--ink); background: none; -webkit-text-fill-color: currentColor; }
  .cap { position: absolute; left: 50px; width: 980px; text-align: center; transform-origin: 50% 50%; --ks: 84px; }
  .cap .ld { font: italic 400 74px/1.05 "Instrument Serif", serif; opacity: .85; display: block; margin-bottom: 18px; }
  .cap .kw { font-weight: 700; font-size: var(--ks); letter-spacing: -0.04em; line-height: 1.04; display: block; }
  .cap .kw.fr { font-family: "Fraunces", serif; font-weight: 900; letter-spacing: -0.03em; }
  .cap .sb { font: italic 400 58px/1.12 "Instrument Serif", serif; display: block; margin-top: 18px; opacity: .9; }
  .cap .w { display: inline-block; padding: 0 0.02em; }
  .ttl { position: absolute; left: 0; width: 1080px; text-align: center; transform-origin: 50% 50%; }
  .ttl .mask { display: block; overflow: hidden; padding: 0 0 30px; margin-bottom: -30px; }
  .ttl .in { display: inline-block; font: 900 200px/1.0 "Fraunces", serif; letter-spacing: -0.035em; color: var(--bone); }
  .qq { top: 1290px; font: italic 400 66px/1.1 "Instrument Serif", serif; color: var(--bone); opacity: .92; padding: 0 120px; box-sizing: border-box; }
  /* swing tag */
  .tagw { position: absolute; width: 300px; height: 560px; transform-origin: 150px 0px; }
  .str { position: absolute; left: 149px; top: 0; width: 2px; height: 150px; background: #bdbdbd; }
  .pin { position: absolute; left: 140px; top: -10px; width: 20px; height: 20px; border-radius: 50%; }
  .tag { position: absolute; left: 0; top: 110px; width: 300px; height: 420px; clip-path: polygon(22% 0, 78% 0, 100% 13%, 100% 100%, 0 100%, 0 13%); color: var(--ink); }
  .hole { position: absolute; left: 131px; top: 22px; width: 38px; height: 38px; border-radius: 50%; background: var(--hole); box-shadow: inset 0 0 0 4px rgba(0,0,0,.25); }
  .tt { position: absolute; left: 0; right: 0; top: 120px; text-align: center; font: 500 40px/1.3 "IBM Plex Mono", monospace; letter-spacing: .18em; color: var(--ink); }
  #tag3 .tt { font: 900 110px/1 "Fraunces", serif; letter-spacing: -0.03em; top: 150px; }
  .dl { display: block; font: 500 22px "IBM Plex Mono", monospace; letter-spacing: .14em; margin-bottom: 22px; color: var(--ink); }
  .pr { display: inline-block; font: 900 130px/1 "Fraunces", serif; letter-spacing: -0.03em; color: var(--ink); }
  .ghosttag { position: absolute; left: 340px; top: 1000px; width: 400px; height: 700px; opacity: .16; transform-origin: 200px 0px; }
  .ghosttag .gs { position: absolute; left: 199px; top: 0; width: 2px; height: 140px; background: #d6d6d6; }
  .ghosttag .gh { position: absolute; left: 176px; top: 30px; width: 48px; height: 48px; border-radius: 50%; border: 4px solid #d6d6d6; box-sizing: border-box; }
  .ghosttag .gt { position: absolute; top: 120px; width: 400px; height: 560px; border: 4px solid #d6d6d6; box-sizing: border-box; clip-path: polygon(22% 0, 78% 0, 100% 13%, 100% 100%, 0 100%, 0 13%); }
  /* dashboard */
  .lbl { top: 280px; }
  .lbl span { display: inline-block; border: 2px solid #8a8a8a; border-radius: 30px; padding: 8px 22px 6px; color: #d6d6d6; font-size: 22px; }
  #lb2 { position: absolute; left: 50%; top: 0; transform: translateX(-50%); white-space: nowrap; border-color: #e6e6e6; color: #ffffff; }
  #dash { position: absolute; left: 120px; top: 650px; width: 840px; height: 560px; border-radius: 30px; background: #131313; border: 2px solid #2b2b2b; box-sizing: border-box; }
  .dh { position: absolute; left: 36px; top: 30px; font-size: 20px; color: #9a9a9a; display: flex; align-items: center; gap: 12px; }
  #cnt { position: absolute; left: 36px; top: 96px; display: flex; flex-direction: column; color: #9a9a9a; }
  #cnt span { font-size: 20px; } #cnt b { font: 900 150px/1 "Fraunces", serif; letter-spacing: -0.03em; color: var(--bone); margin-top: 8px; }
  #ch { position: absolute; left: 30px; top: 330px; width: 780px; height: 200px; overflow: visible; }
  .ts { position: absolute; left: 450px; width: 350px; height: 64px; }
  .ts .fa, .ts .bk { position: absolute; inset: 0; border-radius: 14px; display: flex; align-items: center; gap: 12px; padding: 0 18px; font: 500 20px "IBM Plex Mono", monospace; letter-spacing: .1em; }
  .ts .fa { background: #232323; color: #e6e6e6; } .ts .bk { background: var(--bone); color: var(--ink); opacity: 0; }
  #tally { position: absolute; left: 450px; top: 86px; width: 350px; height: 220px; border-radius: 20px; border: 3px solid #d6d6d6; box-sizing: border-box; padding: 22px 26px; display: flex; flex-direction: column; color: #cfcfcf; }
  #tally span { font-size: 20px; } #tally b { font: 900 140px/1 "Fraunces", serif; margin-top: 10px; }
  #tag3 { transform-origin: 150px 0px; }
  #vhs { position: absolute; inset: 0; opacity: 0; z-index: 5; background: repeating-linear-gradient(0deg, rgba(255,255,255,.10) 0 2px, transparent 2px 7px); }
  .dot { display: inline-block; width: 14px; height: 14px; border-radius: 50%; flex: none; }
  /* cost */
  .sticker { position: absolute; left: 600px; top: 840px; width: 170px; height: 170px; border-radius: 50%; background: var(--bone); color: var(--ink); border: 5px solid var(--ink);
    display: flex; align-items: center; justify-content: center; font: 900 50px "Fraunces", serif; letter-spacing: -0.03em; box-sizing: border-box; transform: rotate(-12deg); }
  #coin { position: absolute; left: 470px; top: 850px; width: 140px; height: 140px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font: 900 46px "Fraunces", serif; color: var(--ink); box-shadow: 0 0 0 4px var(--ink); }
  #gaw { position: absolute; left: 330px; top: 1180px; width: 420px; height: 180px; border-radius: 24px; background: var(--blk); color: var(--bone); display: flex; flex-direction: column; align-items: center; justify-content: center; }
  #gaw span { font-size: 22px; color: #bdbdbd; } #gaw b { font: 900 92px/1 "Fraunces", serif; letter-spacing: -0.03em; margin-top: 10px; }
  /* january */
  #cal6 { position: absolute; left: 390px; top: 620px; width: 300px; height: 270px; border-radius: 26px; overflow: hidden; color: var(--ink); }
  #cal6 .yr { position: absolute; left: 0; right: 0; top: 0; height: 70px; line-height: 70px; text-align: center; background: var(--ink); color: #e6e6e6; font-size: 26px; letter-spacing: .3em; }
  #cal6 .mo { position: absolute; left: 0; right: 0; top: 100px; text-align: center; font: 900 120px/1 "Fraunces", serif; letter-spacing: -0.02em; color: var(--ink); }
  #ch6, #ch8 { position: absolute; left: 140px; top: 960px; width: 800px; height: 270px; overflow: visible; }
  #ch8 { top: 790px; }
  .flab { font-size: 24px; color: #a8a8a8; }
  /* fix */
  .field { position: absolute; left: 83px; width: 914px; height: 506px; }
  .dt { position: absolute; width: 12px; height: 12px; border-radius: 50%; background: #333333; }
  .fc { position: absolute; left: 307px; top: 103px; width: 300px; height: 300px; border-radius: 50%; border: 6px solid #d6d6d6; box-sizing: border-box; background: #121212; }
  .fcl { position: absolute; left: 0; right: 0; top: 70px; text-align: center; font-size: 22px; line-height: 1.4; color: #d6d6d6; }
  .mr { position: absolute; top: 160px; width: 30px; height: 44px; border-radius: 4px; background: var(--bone); }
  .rip { position: absolute; left: 390px; top: 793px; width: 300px; height: 300px; border-radius: 50%; border: 3px solid #e6e6e6; box-sizing: border-box; opacity: 0; }
  .nc { position: absolute; padding: 12px 18px 10px; border-radius: 10px; font-size: 22px; color: var(--ink); }
  /* urgency */
  #cal { position: absolute; left: 370px; top: 580px; width: 340px; height: 380px; border-radius: 30px; color: var(--ink); overflow: hidden; }
  #cal .cm { position: absolute; left: 0; right: 0; top: 0; height: 84px; line-height: 84px; text-align: center; background: var(--ink); color: #e6e6e6; font-size: 32px; letter-spacing: .3em; }
  #cal .d { position: absolute; left: 0; right: 0; top: 110px; text-align: center; font: 900 210px/1 "Fraunces", serif; letter-spacing: -0.04em; color: var(--ink); }
  .nite { top: 1020px; font: italic 400 70px/1.15 "Instrument Serif", serif; color: var(--bone); padding: 0 90px; box-sizing: border-box; }
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
  const P = 0.43103, SC = __SC__, DUR = +(__TOTAL__ * P).toFixed(4);
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
  const fadeOut = (sel, l) => tl.to(sel, { opacity: 0, y: -10, duration: 0.15, ease: "power2.in" }, A(l));
  const sheen = (sel, l, d = 0.9) => tl.fromTo(sel, { backgroundPosition: "100% 50%" }, { backgroundPosition: "0% 50%", duration: d, ease: "power2.inOut" }, A(l));
  const swing = (sel, l, a = 16, d = 1.5) => tl.to(sel, { keyframes: { rotation: [a, -a * 0.6, a * 0.32, -a * 0.14, a * 0.05, 0] }, duration: d, ease: "sine.inOut" }, A(l));
  const count = (sel, l, to, d, fmt = n => String(n), ease = "power3.out") => { const o = { v: 0 }; const el = document.querySelector(sel);
    tl.to(o, { v: to, duration: d, ease, onUpdate: () => { el.textContent = fmt(Math.round(o.v)); } }, A(l)); };
  const euro = n => "€" + (n >= 1000 ? Math.floor(n / 1000) + "," + String(n % 1000).padStart(3, "0") : n);
  const draw = (sel, l, d, from = 1, to = 0) => { const el = document.querySelector(sel); const L = el.getTotalLength ? el.getTotalLength() : 1200;
    tl.set(sel, { strokeDasharray: L, strokeDashoffset: L * from }, 0); tl.to(sel, { strokeDashoffset: L * to, duration: d, ease: "power2.inOut" }, A(l)); return L; };
  const shot = (cam, s) => { const a = B(SC[s]), b = B(__END__[s]);
    tl.set(cam, { scale: 1.04 }, a);
    tl.to(cam, { keyframes: [{ scale: 1, duration: 0.4, ease: "expo.out" }, { scale: 1.025, duration: Math.max(0.1, b - a - 0.4), ease: "none" }] }, a); };
  const lineWipe = l => tl.fromTo("#wipe", { x: 0 }, { x: 2400, duration: 0.45, ease: "power2.inOut" }, A(l) - 0.23);
  tl.fromTo("#grain", { x: 0, y: 0 }, { x: 140, y: -120, duration: DUR, ease: `steps(${Math.floor(DUR * 12)})` }, 0);
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
  const F8 = dots("f8");
  ["s2", "s3", "s5", "s6", "s7", "s8", "s9", "s10"].forEach(s => shot("#cam_" + s, s));

  // ---------- 1 CALLOUT ----------
  cur = "s1";
  tl.fromTo("#cam_s1", { scale: 1.16 }, { scale: 1.0, duration: 0.5, ease: "expo.out" }, 0);
  tl.to("#cam_s1", { scale: 1.03, duration: A(6) - 0.5, ease: "none" }, 0.5);
  tl.set("#t1b", { yPercent: 105 }, 0); tl.to("#t1b", { yPercent: 0, duration: 0.25, ease: "expo.out" }, A(0.5));
  tl.set("#tag1", { y: -900 }, 0); tl.to("#tag1", { y: 0, duration: 0.42, ease: "back.out(1.3)" }, A(1));
  swing("#tag1", 1.6, 18, 1.6); sheen("#tag1 .tag", 2.5); punch("#t1", 2, 1.05);
  fadeUp("#qq", 2.5);

  // ---------- 2 OPEN LOOP ----------
  cur = "s2";
  wordsAt("#c2", from(0, 9)); swing("#s2 .ghosttag", 0, 8, 3); sheen("#c2 .cht", 4, 1.1);

  // ---------- 3 WHAT IT LOOKS LIKE -> rewind -> WHAT ACTUALLY HAPPENED ----------
  cur = "s3";
  fadeUp("#lb1", 0); tl.set("#lb2", { opacity: 0 }, 0);
  wordsAt("#c3a", from(0, 10, 0.25));
  pop("#dash", 0.25, { y: 80, scale: 0.94 });
  tl.set("#tag3", { scale: 0.42, rotation: 0 }, 0); swing("#tag3", 1, 14, 1.4);
  count("#cn", 0.75, 214, B(4));
  const LL = draw("#ln", 0.75, B(4.25));
  [1, 2, 3].forEach(i => pop("#ts" + i, 1 + i, { x: 60 }, 0.28));
  tl.to("#live", { keyframes: { opacity: [0.3, 1] }, duration: 0.4, repeat: 6 }, A(0.5));
  fadeOut("#c3a", 6.75);
  // rewind: VHS stripes, jitter, the graph runs backwards and freezes
  tl.set("#vhs", { opacity: 0.8 }, A(7)); tl.to("#vhs", { opacity: 0, duration: B(0.6), ease: "steps(4)" }, A(7.05));
  tl.to("#dash", { keyframes: { x: [-16, 12, -8, 5, 0] }, duration: B(0.5), ease: "none" }, A(7));
  tl.to("#ln", { strokeDashoffset: LL * 0.55, duration: B(0.5), ease: "power1.in" }, A(7));
  tl.to("#ln", { opacity: 0.35, duration: 0.2 }, A(7.5));
  tl.to("#lb1", { opacity: 0, duration: 0.1 }, A(7.5)); tl.set("#lb2", { opacity: 1 }, A(7.5));
  tl.to("#lb2", { keyframes: { scale: [1.12, 1] }, duration: 0.3, ease: "expo.out" }, A(7.5));
  wordsAt("#c3b", from(7.5, 10, 0.25));
  [1, 2, 3].forEach((i, k) => { const l = 10 + k * 0.5;
    tl.to("#ts" + i, { scaleY: 0, duration: 0.1, ease: "power2.in" }, A(l) - 0.1);
    tl.set("#ts" + i + " .fa", { opacity: 0 }, A(l)); tl.set("#ts" + i + " .bk", { opacity: 1 }, A(l));
    tl.to("#ts" + i, { scaleY: 1, duration: 0.14, ease: "power2.out" }, A(l)); });
  tl.to(["#ts1", "#ts2", "#ts3"], { opacity: 0, x: 60, duration: 0.2, stagger: 0.05, ease: "power2.in" }, A(12));
  pop("#tally", 12.25, { x: 60 });
  count("#nc", 12.5, 3, B(0.75), n => String(n), "steps(3)");
  punch("#tally", 13.25, 1.08);
  sheen("#nc", 13.25, 0.8);

  // ---------- 5 THE COST (bone) ----------
  cur = "s5";
  wordsAt("#c5a", from(0, 9, 0.25));
  tl.set("#tag5", { y: -700 }, 0); tl.to("#tag5", { y: 0, duration: 0.4, ease: "back.out(1.3)" }, A(0.25));
  swing("#tag5", 0.75, 9, 1.2);
  tl.set("#stk5", { opacity: 0, scale: 2.2, rotation: -40 }, 0);
  tl.to("#stk5", { opacity: 1, scale: 1, rotation: -12, duration: 0.22, ease: "power4.in" }, A(1.5) - 0.2);
  fadeOut("#c5a", 4.6);
  wordsAt("#c5b", from(5, 8, 0.25));
  pop("#gaw", 5, { y: 60 });
  tl.set("#coin", { opacity: 0, scale: 0.3 }, 0);
  tl.to("#coin", { opacity: 1, scale: 1, duration: 0.2, ease: "back.out(2)" }, A(5.5));
  tl.to("#coin", { y: 330, rotation: 220, scale: 0.6, duration: 0.35, ease: "power2.in" }, A(5.5) + 0.25);
  tl.to("#coin", { opacity: 0, duration: 0.05 }, A(5.5) + 0.6);
  punch("#gaw", 5.5 + 0.6 / P, 1.06);
  count("#gv", 6.25, 3852, B(2.25), euro);

  // ---------- 6 JANUARY ----------
  cur = "s6";
  wordsAt("#c6", from(0, 6, 0.25));
  pop("#cal6", 0.25, { y: 50, scale: 0.92 });
  tl.set(["#mDEC", "#mJAN"], { opacity: 0 }, 0);
  tl.set("#mNOV", { opacity: 0 }, A(0.75)); tl.set("#mDEC", { opacity: 1 }, A(0.75));
  tl.set("#mDEC", { opacity: 0 }, A(1.25)); tl.set("#mJAN", { opacity: 1 }, A(1.25));
  draw("#ln6", 0, B(0.5));
  tl.to("#ln6", { attr: { points: "__LOW__" }, duration: B(1), ease: "power3.inOut" }, A(2));
  fadeUp("#fl6", 0.5);

  // ---------- 7 THE TURN ----------
  cur = "s7";
  tl.set("#tag7", { rotation: 38 }, 0);
  tl.to("#tag7", { rotation: 0, duration: 0.9, ease: "elastic.out(1, 0.35)" }, A(0));
  sheen("#tag7 .tag", 1);
  wordsAt("#c7", from(0.25, 4, 0.25)); punch("#c7", 2, 1.05);

  // ---------- 8 THE FIX ----------
  cur = "s8";
  lineWipe(0);
  wordsAt("#c8 .kw", from(0, 6));
  wordsAt("#c8 .sb", from(2.75, 14, 0.25));
  fadeUp("#fl8a", 1);
  [3, 4, 5].forEach((l, i) => { tl.set("#rp" + (i + 1), { opacity: 0.9, scale: 1 }, A(l)); tl.to("#rp" + (i + 1), { opacity: 0, scale: 3.6, duration: 0.9, ease: "power2.out" }, A(l)); });
  [[3.5, 0], [4, 1], [4.5, 2], [5, 3]].forEach(([l, k]) => tl.to(F8.by[k] || [], { backgroundColor: "#e6e6e6", duration: 0.15, stagger: 0.002 }, A(l)));
  [6, 6.5, 7, 7.5].forEach((l, i) => { pop("#nc" + (i + 1), l, { y: 30, scale: 0.6 }, 0.3); sheen("#nc" + (i + 1), l + 0.5, 0.7); });
  tl.to("#fl8a", { opacity: 0, duration: 0.1 }, A(7.75)); fadeUp("#fl8b", 7.75);
  fadeOut("#c8", 8.25);
  tl.to(["#f8", ".nc"], { opacity: 0.12, duration: 0.3 }, A(8.25)); tl.to("#fl8b", { opacity: 0, duration: 0.15 }, A(8.25));
  wordsAt("#c8b", from(8.5, 8, 0.25));
  tl.set("#ln8", { opacity: 0 }, 0); tl.set("#ln8", { opacity: 1 }, A(8.75));
  tl.to("#ln8", { attr: { points: "__HIGH8__" }, duration: B(1.5), ease: "power3.out" }, A(9));
  fadeUp("#fl8c", 9);
  sheen("#c8b .cht", 10.5, 0.9);

  // ---------- 9 URGENCY ----------
  cur = "s9";
  wordsAt("#c9", from(0, 5));
  tl.set(["#d25", "#d26", "#d27"], { opacity: 0 }, 0);
  [[1, "#d24", "#d25"], [1.5, "#d25", "#d26"], [3, "#d26", "#d27"]].forEach(([l, a, c]) => { tl.set(a, { opacity: 0 }, A(l)); tl.set(c, { opacity: 1 }, A(l)); });
  pop("#cal", 0.5, { y: 60, scale: 0.9 });
  punch("#cal", 3, 1.1); flash(3, 0.4); sheen("#cal", 3, 0.9);
  fadeUp("#nite", 3.25);

  // ---------- 10 END CARD ----------
  cur = "s10";
  tl.set("#eb1", { opacity: 0, scale: 1.15 }, 0); tl.to("#eb1", { opacity: 1, scale: 1, duration: 0.5, ease: "expo.out" }, A(0));
  tl.set("#eb2", { opacity: 0, y: 60 }, 0); tl.to("#eb2", { opacity: 1, y: 0, duration: 0.35, ease: "expo.out" }, A(1));
  const PL = 2 * (655.5 - 103.5) + Math.PI * 103.5;
  tl.set("#pillR", { strokeDasharray: PL, strokeDashoffset: PL }, 0); tl.to("#pillR", { strokeDashoffset: 0, duration: 0.45, ease: "power2.inOut" }, A(2));
  tl.set("#pill .ico", { opacity: 0, scale: 0.3 }, 0); tl.set("#pill .ico", { opacity: 1 }, A(2.25)); tl.to("#pill .ico", { scale: 1, duration: 0.3, ease: "back.out(2.5)" }, A(2.25));
  tl.set("#pill .dv", { scaleY: 0 }, 0); tl.to("#pill .dv", { scaleY: 1, duration: 0.2, ease: E.in }, A(2.5));
  tl.set("#pill .cm", { opacity: 0, x: -14 }, 0); tl.to("#pill .cm", { opacity: 1, x: 0, duration: 0.22, ease: E.in }, A(2.5));
  tl.set("#pill .q .c", { opacity: 0 }, 0);
  [0, 1, 2, 3, 4, 5].forEach(i => tl.set("#pill .q .c:nth-child(" + (i + 1) + ")", { opacity: 1 }, A(3 + i * 0.25)));
  tl.set("#eb4", { opacity: 0, y: 14 }, 0); tl.to("#eb4", { opacity: 1, y: 0, duration: 0.3, ease: E.in }, A(4.75));
  pulse("#pill", 5, 7, 0.025);

  window.__timelines["main"] = tl;
'''
JS = (JS.replace("__SC__", json.dumps(SC)).replace("__TOTAL__", str(TOTAL)).replace("__END__", json.dumps(END))
      .replace("__LOW__", LOW).replace("__HIGH8__", "0,250 130,236 260,214 390,176 520,128 650,74 800,20"))

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=1080, height=1920" />
<title>Southline: Black Friday</title>
<script src="assets/vendor/gsap.min.js"></script>
<style>
  /* Palette: Black #0A0A0A / Bone #EDE8DF / Graphite #4A4A48 / accent silver chrome · ad #9 v2 "Black Friday looks like a win. It isn't." */{CSS}</style>
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

# ---------- cues ----------
ev = []
def e(s, l, name, g): ev.append([A(s, l), name, g])
e("s1", 0, "hit", 0.6); e("s1", 0.5, "pop", 0.3); e("s1", 1, "whoosh", 0.35); e("s1", 1.45, "click", 0.35); e("s1", 2.5, "shimmer", 0.25)
for s in ("s2", "s3", "s6", "s9"): ev.append([B(SC[s]) - 0.1, "swish", 0.25])
ev.append([B(SC["s8"]) - 0.22, "whoosh", 0.45]); ev.append([B(SC["s10"]) - 0.1, "whoosh", 0.35])
e("s3", 0.25, "pop", 0.3)
for i in (2, 3, 4): e("s3", i, "coin", 0.3)
for k in range(8): e("s3", 0.75 + k * 0.5, "tick", 0.18)              # counter racing
e("s3", 7, "glitch", 0.35); ev.append([A("s3", 7) - 0.3, "whoosh", 0.3])  # rewind
e("s3", 7.5, "click", 0.35)
for l in (10, 10.5, 11): e("s3", l, "swish", 0.2)
e("s3", 12.25, "pop", 0.3); e("s3", 13.25, "hit", 0.45)                 # dull thud on NEW CUSTOMERS: 3
e("s5", 0.25, "swish", 0.3); e("s5", 1.5, "hit", 0.4); e("s5", 1.5, "click", 0.4)
e("s5", 5, "pop", 0.3); e("s5", 5.5, "coin", 0.4); ev.append([A("s5", 5.5) + 0.6, "hit", 0.35])
for k in range(5): e("s5", 6.25 + k * 0.5, "tick", 0.2)
e("s6", 0.25, "pop", 0.25); e("s6", 0.75, "click", 0.25); e("s6", 1.25, "click", 0.25)
for l in (2, 3, 4): e("s6", l, "tick", 0.22)
ev.append([B(SC["s7"]) - 0.62, "riser", 0.45]); e("s7", 0, "hit", 0.8); e("s7", 1, "shimmer", 0.3)
for l in (3, 4, 5): e("s8", l, "swish", 0.2)
for l in (6, 6.5, 7, 7.5): e("s8", l, "coin", 0.3)
e("s8", 9, "shimmer", 0.25)
e("s9", 0.5, "pop", 0.3); e("s9", 1, "click", 0.3); e("s9", 1.5, "click", 0.3)
ev.append([A("s9", 3) - 0.62, "riser", 0.35]); e("s9", 3, "hit", 0.8)
e("s10", 0, "shimmer", 0.3); e("s10", 1, "hit", 0.5); e("s10", 2, "swish", 0.25); e("s10", 2.25, "pop", 0.35)
for i in range(6): e("s10", 3 + i * 0.25, "tick", 0.3)
e("s10", 4.75, "ping", 0.3)
drop = [[A("s6", 2), A("s6", 5)], [A("s9", 2.5), A("s9", 3)]]
json.dump({"duration": DUR, "bpm": 139.2, "dropouts": drop, "events": sorted(ev)}, open(CUES, "w"))
print("wrote", HF + "/index.html", DUR, "s,", len(ev), "cues")
