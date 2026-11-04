#!/usr/bin/env python3
"""Ad #12 · Clothing brands · "Stock you've already paid for."  Ink / Stone / Tangerine. Keyword: STOCK. SA end card.
    python3 gen_composition.py <hyperframes dir> <cues.json>"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../.claude/skills/videoad/scripts"))
from clearkit import build, cap, title2, Cues

HF, CUES = sys.argv[1], sys.argv[2]
PAL = {"--bg": "#121417", "--fg": "#e7e3db", "--paper": "#e7e3db", "--ink": "#121417", "--acc": "#ff7a1a", "--accd": "#c04d00",
       "--endbg": "#000000", "--glow": "rgba(255,122,26,.08)", "--mid": "#5d636b"}
SC = [("s1", 0), ("s2", 6), ("s3", 13), ("s4", 26), ("s5", 37), ("s6", 44), ("s7", 56), ("s8", 62)]
TOTAL = 69
COLS = ["#e7e3db", "#ff7a1a", "#8a8f96", "#3a3f46", "#e7e3db", "#c9c3b8", "#ff7a1a", "#8a8f96", "#e7e3db", "#3a3f46", "#c9c3b8", "#ff7a1a", "#e7e3db", "#8a8f96", "#3a3f46"]


def garment(i, col, left):
    body = ("M8 34 L0 52 L10 58 L14 50 V112 H46 V50 L50 58 L60 52 L52 34 Z" if i % 3 else
            "M8 34 Q30 18 52 34 L60 60 L52 64 L48 56 V114 H12 V56 L8 64 L0 60 Z")
    return (f'<svg class="g" style="left:{left}px" viewBox="0 0 60 120" width="84" height="168">'
            f'<path d="M30 6 q8 0 8 8 t-8 8 v8" fill="none" stroke="#9aa0a6" stroke-width="3"/>'
            f'<path d="M6 36 L30 28 L54 36" fill="none" stroke="#9aa0a6" stroke-width="3"/>'
            f'<path d="{body}" fill="{col}" stroke="#121417" stroke-width="2"/></svg>')


def rail(rid, n, top):
    gs = "".join(garment(i, COLS[i], 10 + i * 90) for i in range(n))
    return f'<div class="rail" id="{rid}" style="top:{top}px"><i class="bar"></i>{gs}</div>'


def post(i, top, left, likes):
    return (f'<div class="post" id="po{i}" style="top:{top}px;left:{left}px"><i class="th"></i><div><b>Still available 🔥</b>'
            f'<span class="mono">LAST FEW SIZES</span></div><div class="lk"><span class="ac">♥</span> {likes}</div></div>')


S = {}
S["s1"] = ("dark", f'''
      {title2("t1", "Clothing", "brands.", 700, 200)}
      <div class="ctr sub" id="sub1" style="top:1180px">Quick look in your stock room.</div>''')
S["s2"] = ("dark", f'''
      {cap("c2", "How much of your last drop is *still *on *the *rail?", 600, 112)}''')
S["s3"] = ("dark", f'''
      {cap("c3a", "You ordered 300 pieces for the drop.", 320, 84)}
      {cap("c3b", "You sold 120 to your followers.", 320, 84)}
      {cap("c3c", "The rest is *still *here.", 320, 84)}
      <div class="cnts"><div class="cn" id="cnA"><span class="mono">ORDERED</span><b id="vA">0</b></div><div class="cn" id="cnB"><span class="mono">SOLD</span><b id="vB">0</b></div></div>
      {rail("r3", 10, 760)}
      <div class="ctr mono tied" id="tied"><span class="ac">180 LEFT</span> · €4,500 OF STOCK SITTING HERE</div>''')
S["s4"] = ("dark", f'''
      {cap("c4a", "Reposting it to the same followers gets fewer likes every time.", 300, 80)}
      {cap("c4b", "Because they've *already *seen *it.", 300, 80)}
      {post(1, 620, 150, 52)}{post(2, 820, 230, 31)}{post(3, 1020, 310, 18)}''')
S["s5"] = ("light", f'''
      <div class="ptag" id="pt5"><i class="hole"></i><span class="pr" id="p45">€45<i class="sk"></i></span><span class="pr" id="p30">€30<i class="sk"></i></span><span class="pr" id="p20">€20</span></div>
      <div class="mg" id="mg"><span class="mono">YOUR MARGIN</span><div class="bar2"><i id="mgf"></i></div></div>
      {cap("c5", "So you discount it… and your margin *disappears.", 1060, 100, serif=True)}''')
S["s6"] = ("dark", f'''
      {cap("c6", "We run Facebook & Instagram ads", 250, 88, sub="that show your stock to people who've *never *seen *your *brand.")}
      {rail("r6", 6, 740)}
      <div class="ships" id="ships"></div>
      <div class="ctr mono tied" id="left6">ON THE RAIL: <b id="v6">180</b></div>''')
S["s7"] = ("dark", f'''
      {cap("c7", "Sell what you've already got. At *full *price.", 400, 120, serif=True)}
      <div class="fp" id="fp"><span>€45</span><b class="mono">✓ FULL PRICE</b></div>''')
S["s8"] = ("end", "")
scenes = [(k, s, S[k][0], S[k][1]) for k, s in SC]

CSS = '''
  .cnts { position: absolute; left: 0; width: 1080px; top: 520px; display: flex; justify-content: center; gap: 60px; }
  .cn { width: 300px; text-align: center; } .cn span { font-size: 22px; opacity: .7; display: block; }
  .cn b { font: 900 120px/1 "Fraunces", serif; letter-spacing: -0.03em; display: block; margin-top: 6px; }
  #cnB b { color: var(--acc); }
  .rail { position: absolute; left: 90px; width: 900px; height: 190px; }
  .rail .bar { position: absolute; left: 0; right: 0; top: 8px; height: 10px; border-radius: 5px; background: #9aa0a6; }
  .rail .g { position: absolute; top: 2px; transform-origin: 42px 8px; }
  .rail .g path:last-child { }
  .tied { top: 1010px; font-size: 26px; }
  #tied { top: 1000px; }
  .post { position: absolute; width: 600px; height: 160px; border-radius: 24px; background: #1e2227; border: 2px solid #2c3138; box-sizing: border-box; display: flex; align-items: center; gap: 22px; padding: 0 26px; }
  .post .th { width: 104px; height: 104px; border-radius: 16px; background: #3a3f46; flex: none; }
  .post b { font: 700 32px "Instrument Sans", sans-serif; display: block; } .post .mono { font-size: 17px; opacity: .6; }
  .post .lk { margin-left: auto; font: 900 52px "Fraunces", serif; }
  .ptag { position: absolute; left: 330px; top: 320px; width: 420px; height: 520px; background: var(--ink); color: var(--paper); clip-path: polygon(22% 0, 78% 0, 100% 13%, 100% 100%, 0 100%, 0 13%);
    display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; }
  .ptag .hole { position: absolute; left: 190px; top: 26px; width: 40px; height: 40px; border-radius: 50%; background: var(--paper); }
  .ptag .pr { position: relative; font: 900 120px/1.05 "Fraunces", serif; letter-spacing: -0.03em; }
  .ptag .sk { position: absolute; left: -10px; right: -10px; top: 50%; height: 12px; border-radius: 6px; background: var(--acc); transform-origin: 0 50%; }
  .mg { position: absolute; left: 240px; top: 880px; width: 600px; color: var(--ink); } .mg span { font-size: 22px; }
  .bar2 { margin-top: 10px; height: 30px; border-radius: 15px; background: #cfc9bd; overflow: hidden; } .bar2 i { display: block; height: 100%; width: 100%; background: var(--ink); transform-origin: 0 50%; }
  .ships { position: absolute; left: 0; top: 990px; width: 1080px; height: 360px; }
  .ship { position: absolute; left: 0; width: 1080px; text-align: center; }
  .ship span { display: inline-block; background: var(--acc); color: var(--ink); border-radius: 12px; padding: 12px 20px 10px; font: 500 22px "IBM Plex Mono", monospace; letter-spacing: .1em; }
  #left6 { top: 1340px; } #left6 b { color: var(--acc); font-weight: 500; }
  .fp { position: absolute; left: 0; width: 1080px; top: 900px; text-align: center; }
  .fp span { display: block; font: 900 200px/1 "Fraunces", serif; letter-spacing: -0.04em; }
  .fp b { display: inline-block; margin-top: 16px; border: 4px solid var(--acc); color: var(--acc); border-radius: 12px; padding: 10px 18px 8px; font-size: 26px; font-weight: 500; transform: rotate(-4deg); }
'''

CITIES = ["CORK", "LEEDS", "DUBLIN 8", "BELFAST"]
JS = r'''
  // ---------- 1 CALLOUT ----------
  cur = "s1";
  tl.set("#t1b", { yPercent: 140 }, 0); tl.to("#t1b", { yPercent: 0, duration: 0.25, ease: "expo.out" }, A(0.5));
  punch("#t1", 1.5, 1.05); fadeUp("#sub1", 2.5);

  // ---------- 2 OPEN LOOP ----------
  cur = "s2";
  wordsAt("#c2", from(0, 10, 0.4));

  // ---------- 3 RELATE: ordered 300, sold 120, the rest is still here ----------
  cur = "s3";
  const G3 = Array.from(document.querySelectorAll("#r3 .g"));
  wordsAt("#c3a", from(0, 7, 0.25));
  fadeUp("#cnA", 0.25); count("#vA", 0.5, 300, B(1.5));
  tl.set("#r3 .bar", { scaleX: 0, transformOrigin: "0 50%" }, 0); tl.to("#r3 .bar", { scaleX: 1, duration: 0.4, ease: "power3.out" }, A(0.25));
  tl.set(G3, { y: -200, opacity: 0 }, 0); tl.to(G3, { y: 0, opacity: 1, duration: 0.35, ease: "back.out(1.6)", stagger: 0.04 }, A(0.75));
  fadeOut("#c3a", 4.6);
  wordsAt("#c3b", from(5, 6, 0.25));
  fadeUp("#cnB", 5.25); count("#vB", 5.5, 120, B(1.5));
  tl.to(G3.slice(0, 4), { x: -1000, rotation: -25, duration: 0.45, ease: "power3.in", stagger: 0.06 }, A(6));
  tl.to(G3.slice(4), { x: -360, duration: 0.4, ease: "power3.out" }, A(7.25));
  fadeOut("#c3b", 8.6);
  wordsAt("#c3c", from(9, 5, 0.25));
  tl.to(G3.slice(4), { keyframes: { rotation: [6, -4, 2, 0] }, duration: 0.8, ease: "sine.inOut", stagger: 0.03 }, A(9.5));
  fadeUp("#tied", 10);

  // ---------- 4 PROBLEM: reposting to the same followers ----------
  cur = "s4";
  wordsAt("#c4a", from(0, 11, 0.25));
  [1, 2, 3].forEach(i => pop("#po" + i, 1.5 + i, { x: 80 }, 0.3));
  fadeOut("#c4a", 6.1);
  wordsAt("#c4b", from(6.5, 5, 0.25));
  punch("#po3", 8, 1.05);

  // ---------- 5 STING: discount it and the margin goes ----------
  cur = "s5";
  pop("#pt5", 0, { y: -80 });
  tl.set(["#p30", "#p20"], { opacity: 0, height: 0 }, 0);
  tl.set(".ptag .sk", { scaleX: 0 }, 0);
  pop("#mg", 0.5, { y: 30 });
  tl.to("#p45 .sk", { scaleX: 1, duration: 0.18, ease: "power3.out" }, A(1.5));
  tl.set("#p30", { opacity: 1, height: "auto" }, A(2)); tl.from("#p30", { y: 30, duration: 0.25, ease: "back.out(2)" }, A(2));
  tl.to("#mgf", { scaleX: 0.55, duration: 0.3, ease: "power2.out" }, A(2));
  tl.to("#p30 .sk", { scaleX: 1, duration: 0.18, ease: "power3.out" }, A(3));
  tl.set("#p20", { opacity: 1, height: "auto" }, A(3.5)); tl.from("#p20", { y: 30, duration: 0.25, ease: "back.out(2)" }, A(3.5));
  tl.to("#mgf", { scaleX: 0.12, duration: 0.3, ease: "power2.out" }, A(3.5));
  wordsAt("#c5", from(0.5, 8, 0.4));

  // ---------- 6 FIX: new people, stock ships ----------
  cur = "s6";
  lineWipe(0);
  wordsAt("#c6 .kw", from(0, 6, 0.5));
  wordsAt("#c6 .sb", from(3.25, 11, 0.25));
  const G6 = Array.from(document.querySelectorAll("#r6 .g"));
  pop("#r6", 0.5, { y: 40 });
  const CITIES = __CITIES__; const ships = document.getElementById("ships");
  CITIES.forEach((c, i) => { const d = document.createElement("div"); d.className = "ship"; d.id = "sh" + i; d.style.top = (i % 3) * 110 + "px";
    d.innerHTML = "<span>NEW CUSTOMER · " + c + "</span>"; ships.appendChild(d); });
  fadeUp("#left6", 1);
  CITIES.forEach((c, i) => { const l = 6 + i * 0.75;
    tl.to(G6[i], { y: -60, x: 900, rotation: 30, opacity: 0, duration: 0.4, ease: "power3.in" }, A(l));
    pop("#sh" + i, l + 0.25, { x: -80, scale: 0.8 }, 0.25);
    if (i >= 3) tl.set("#sh" + (i - 3), { opacity: 0 }, A(l + 0.25)); });
  count("#v6", 6, 60, B(3), n => String(n), "steps(4)", 180);

  // ---------- 7 PAYOFF ----------
  cur = "s7";
  wordsAt("#c7", from(0, 8, 0.4));
  pop("#fp", 1, { y: 40 });
  tl.set(".fp b", { opacity: 0, scale: 2 }, 0); tl.to(".fp b", { opacity: 1, scale: 1, duration: 0.2, ease: "power4.in" }, A(3) - 0.18);
'''.replace("__CITIES__", str(CITIES))

c = Cues(dict(SC))
c.add("s1", 0, "hit", 0.6); c.add("s1", 0.5, "pop", 0.3); c.add("s1", 1.5, "shimmer", 0.25)
for s in ("s2", "s3", "s4", "s5", "s7"): c.add(s, 0, "swish", 0.25, -0.1)
c.add("s3", 0.25, "swish", 0.25)
for i in range(10): c.add("s3", 0.75 + i * 0.093, "tick", 0.18)
c.add("s3", 6, "whoosh", 0.35); c.add("s3", 10, "click", 0.3)
for i in (1, 2, 3): c.add("s4", 1.5 + i, "pop", 0.3)
c.add("s4", 8, "glitch", 0.25)
c.add("s5", 0, "pop", 0.3); c.add("s5", 1.5, "swish", 0.35); c.add("s5", 2, "hit", 0.35); c.add("s5", 3, "swish", 0.35); c.add("s5", 3.5, "hit", 0.45)
c.add("s6", 0, "whoosh", 0.45, -0.22); c.add("s6", 0.5, "pop", 0.3)
for i in range(4): c.add("s6", 6 + i * 0.75, "coin", 0.3)
c.dropout("s6", 11.5, 12); c.add("s7", 0, "hit", 0.75); c.add("s7", 1, "pop", 0.3); c.add("s7", 3, "click", 0.4)

d = build(HF, CUES, "SA: Stock on the rail", PAL, scenes, TOTAL, CSS, JS, c, endcard="sa", keyword="stock",
          comment="Ad #12 · Ink #121417 / Stone #E7E3DB / Tangerine #FF7A1A · 'Stock you've already paid for.'")
print("wrote", HF, d, "s")
