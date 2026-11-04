#!/usr/bin/env python3
"""Ad #9 v3 · Clothing brands · Black Friday, tightened (~21 s).
Changes from v2 (owner feedback review): pain-first hook readable at frame 0, 20.7 s instead of 31.5 s, story text and
labels 2-3x bigger, whole lines land fast (no half-empty frames), bigger graphics, the CTA + offer shown mid-video,
"free Black Friday ad plan" offer on the end card, frame-0 tag sliver fixed. Black / Bone / silver chrome.
    python3 gen_composition_v3.py <hyperframes dir> <cues.json>"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../.claude/skills/videoad/scripts"))
from clearkit import build, cap, Cues

HF, CUES = sys.argv[1], sys.argv[2]
PAL = {"--bg": "#0a0a0a", "--fg": "#ede8df", "--paper": "#ede8df", "--ink": "#111111", "--acc": "#d4d4d4", "--accd": "#111111",
       "--endbg": "#000000", "--glow": "rgba(255,255,255,.07)", "--mid": "#4a4a48",
       "--chrome": "linear-gradient(110deg, #7a7a7a 0%, #d9d9d9 16%, #ffffff 28%, #a3a3a3 42%, #f2f2f2 58%, #8c8c8c 76%, #e2e2e2 100%)",
       "--chrome-t": "linear-gradient(110deg, #c4c4c4 0%, #ffffff 22%, #d2d2d2 42%, #ffffff 60%, #bcbcbc 80%, #f2f2f2 100%)"}
SC = [("s1", 0), ("s2", 5), ("s4", 19), ("s5", 27), ("s6", 37), ("s7", 41)]
TOTAL = 48
Q = 0.125   # word step (beats): lines land almost whole, with a quick ripple


def tag(tid, left, top, face, cls=""):
    return (f'<div class="tagw {cls}" id="{tid}" style="left:{left}px;top:{top}px"><i class="str"></i><i class="pin chrome"></i>'
            f'<div class="tag chrome"><i class="hole"></i><div class="tt">{face}</div></div></div>')


def toast(i, top):
    return (f'<div class="ts" id="ts{i}" style="top:{top}px"><div class="fa"><i class="dot"></i>NEW ORDER · €42</div>'
            f'<div class="bk">↺ FOLLOWER SINCE 2023</div></div>')


S = {}
S["s1"] = ("dark", f'''
      {tag("tag1", 390, 110, "BLACK<br>FRIDAY", "sm")}
      <div class="ctr lbl mono" id="who" style="top:700px"><span>CLOTHING BRANDS</span></div>
      <div class="hook" id="hook">Your Black Friday sale is <span class="ac">costing you.</span></div>''')
S["s2"] = ("dark", f'''
      <div class="ctr lbl mono" id="lbl"><span id="lb1">ON THE DAY</span><span id="lb2">WHAT ACTUALLY HAPPENED</span></div>
      {cap("c2a", "It feels like your best weekend ever.", 370, 96)}
      {cap("c2b", "But almost every order came from people who *already *follow *you.", 360, 80)}
      <div id="dash">
        <div class="dh mono"><i class="dot"></i>BLACK FRIDAY · LIVE</div>
        <div id="cnt"><span class="mono">ORDERS</span><b id="cn">0</b></div>
        <svg id="ch" viewBox="0 0 880 200" data-layout-ignore><polyline id="ln" points="0,190 120,176 240,158 360,124 480,96 600,66 720,36 880,10" fill="none" stroke="#e8e8e8" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/></svg>
        {toast(1, 96)}{toast(2, 188)}{toast(3, 280)}
        <div id="tally"><span class="mono">NEW CUSTOMERS</span><b id="nc" class="cht">0</b></div>
      </div>
      <div id="vhs" data-layout-ignore></div>''')
S["s4"] = ("light", f'''
      {cap("c4", "You gave away €18 on every order", 280, 96, sub="to people who'd have paid full price anyway.")}
      {tag("tag4", 150, 640, '<span class="dl">DROP 03</span><span class="pr">€60</span>')}
      <div class="sticker" id="stk4">–30%</div>
      <div id="coin" class="chrome">€18</div>
      <div id="gaw"><span class="mono">GIVEN AWAY</span><b id="gv">€0</b></div>''')
S["s5"] = ("dark", f'''
      {cap("c5", "Put your drop in front of people who've *never *seen *your *brand.", 230, 90, lead="Here's what to change:", sub="We run the Facebook & Instagram ads that do it.")}
      <div class="field" id="f5" style="top:810px"><div class="fc"><div class="fcl mono">YOUR<br>FOLLOWERS</div></div></div>
      <i class="rip" id="rp1" data-layout-ignore></i><i class="rip" id="rp2" data-layout-ignore></i><i class="rip" id="rp3" data-layout-ignore></i>
      <div class="nc chrome mono" id="nc1" style="left:90px;top:840px">NEW CUSTOMER</div>
      <div class="nc chrome mono" id="nc2" style="left:700px;top:910px">NEW CUSTOMER</div>
      <div class="nc chrome mono" id="nc3" style="left:120px;top:1200px">NEW CUSTOMER</div>
      <div class="nc chrome mono" id="nc4" style="left:680px;top:1230px">NEW CUSTOMER</div>
      <div class="remind" id="remind">💬 Comment <b>FRIDAY</b> for a free Black Friday ad plan</div>''')
S["s6"] = ("dark", f'''
      {cap("c6", "Black Friday is *27 *November.", 330, 112)}
      <div id="cal" class="chrome"><div class="cm mono">NOV</div><span class="d" id="d25">25</span><span class="d" id="d26">26</span><span class="d" id="d27">27</span></div>
      <div class="ctr nite" id="nite">Start now, not the night before.</div>''')
S["s7"] = ("end", "")
scenes = [(k, s, S[k][0], S[k][1]) for k, s in SC]

CSS = '''
  .chrome { background-color: #d4d4d4; background-image: var(--chrome); background-size: 300% 100%; background-position: 0% 50%; }
  .cht, .dark .ac { color: #e4e4e4; background-image: var(--chrome-t); background-size: 300% 100%; background-position: 0% 50%; -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; }
  .light .ac { color: var(--ink); background: none; -webkit-text-fill-color: currentColor; text-decoration: underline; text-decoration-thickness: 8px; text-underline-offset: 10px; }
  .hook { position: absolute; left: 60px; width: 960px; top: 790px; text-align: center; font: 900 136px/1.0 "Fraunces", serif; letter-spacing: -0.035em; color: var(--fg); }
  .lbl { top: 280px; } .lbl span { font-size: 28px; }
  #lb2 { position: absolute; left: 50%; top: 0; transform: translateX(-50%); white-space: nowrap; }
  #who span { font-size: 30px; letter-spacing: .2em; }
  /* swing tag */
  .tagw { position: absolute; width: 300px; height: 560px; transform-origin: 150px 0px; }
  .str { position: absolute; left: 149px; top: 0; width: 2px; height: 150px; background: #bdbdbd; }
  .pin { position: absolute; left: 140px; top: -10px; width: 20px; height: 20px; border-radius: 50%; }
  .tag { position: absolute; left: 0; top: 110px; width: 300px; height: 420px; clip-path: polygon(22% 0, 78% 0, 100% 13%, 100% 100%, 0 100%, 0 13%); color: var(--ink); }
  .hole { position: absolute; left: 131px; top: 22px; width: 38px; height: 38px; border-radius: 50%; background: var(--bg); box-shadow: inset 0 0 0 4px rgba(0,0,0,.25); }
  .light .hole { background: var(--paper); }
  .tt { position: absolute; left: 0; right: 0; top: 120px; text-align: center; font: 500 40px/1.3 "IBM Plex Mono", monospace; letter-spacing: .18em; color: var(--ink); }
  .dl { display: block; font: 500 24px "IBM Plex Mono", monospace; letter-spacing: .14em; margin-bottom: 22px; color: var(--ink); }
  .pr { display: inline-block; font: 900 130px/1 "Fraunces", serif; letter-spacing: -0.03em; color: var(--ink); }
  /* dashboard (bigger than v2) */
  #dash { position: absolute; left: 60px; top: 680px; width: 960px; height: 650px; border-radius: 34px; background: #131313; border: 2px solid #2b2b2b; box-sizing: border-box; }
  .dh { position: absolute; left: 40px; top: 34px; font-size: 24px; color: #a8a8a8; display: flex; align-items: center; gap: 14px; }
  #cnt { position: absolute; left: 40px; top: 100px; display: flex; flex-direction: column; color: #a8a8a8; }
  #cnt span { font-size: 26px; } #cnt b { font: 900 190px/1 "Fraunces", serif; letter-spacing: -0.03em; color: var(--fg); margin-top: 10px; }
  #ch { position: absolute; left: 40px; top: 400px; width: 880px; height: 200px; overflow: visible; }
  .ts { position: absolute; left: 470px; width: 450px; height: 78px; }
  .ts .fa, .ts .bk { position: absolute; inset: 0; border-radius: 16px; display: flex; align-items: center; gap: 14px; padding: 0 22px; font: 500 27px "IBM Plex Mono", monospace; letter-spacing: .06em; }
  .ts .fa { background: #232323; color: #ededed; } .ts .bk { background: var(--fg); color: var(--ink); opacity: 0; }
  #tally { position: absolute; left: 470px; top: 96px; width: 450px; height: 262px; border-radius: 22px; border: 4px solid #d6d6d6; box-sizing: border-box; padding: 24px 30px; display: flex; flex-direction: column; color: #d6d6d6; }
  #tally span { font-size: 28px; } #tally b { font: 900 170px/1 "Fraunces", serif; margin-top: 6px; }
  #vhs { position: absolute; inset: 0; opacity: 0; z-index: 5; background: repeating-linear-gradient(0deg, rgba(255,255,255,.10) 0 2px, transparent 2px 7px); }
  /* cost */
  .sticker { position: absolute; left: 330px; top: 1100px; width: 180px; height: 180px; border-radius: 50%; background: var(--paper); color: var(--ink); border: 5px solid var(--ink);
    display: flex; align-items: center; justify-content: center; font: 900 54px "Fraunces", serif; letter-spacing: -0.03em; box-sizing: border-box; transform: rotate(-12deg); }
  #coin { position: absolute; left: 230px; top: 1000px; width: 150px; height: 150px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font: 900 50px "Fraunces", serif; color: var(--ink); box-shadow: 0 0 0 5px var(--ink); }
  #gaw { position: absolute; left: 560px; top: 900px; width: 420px; height: 240px; border-radius: 28px; background: var(--bg); color: var(--fg); display: flex; flex-direction: column; align-items: center; justify-content: center; }
  #gaw span { font-size: 28px; color: #c4c4c4; } #gaw b { font: 900 104px/1 "Fraunces", serif; letter-spacing: -0.03em; margin-top: 12px; }
  /* fix */
  .field { position: absolute; left: 83px; width: 914px; height: 506px; }
  .dt { position: absolute; width: 14px; height: 14px; border-radius: 50%; background: #333333; }
  .fc { position: absolute; left: 297px; top: 93px; width: 320px; height: 320px; border-radius: 50%; border: 6px solid #d6d6d6; box-sizing: border-box; background: #121212; }
  .fcl { position: absolute; left: 0; right: 0; top: 108px; text-align: center; font-size: 30px; line-height: 1.35; color: #e6e6e6; }
  .rip { position: absolute; left: 380px; top: 903px; width: 320px; height: 320px; border-radius: 50%; border: 3px solid #e6e6e6; box-sizing: border-box; opacity: 0; }
  .nc { position: absolute; padding: 14px 20px 12px; border-radius: 12px; font-size: 28px; color: var(--ink); }
  .remind { position: absolute; left: 60px; width: 960px; top: 1360px; white-space: nowrap; border: 4px solid var(--fg); border-radius: 60px; box-sizing: border-box; padding: 22px 30px; text-align: center;
    font: 700 34px "Instrument Sans", sans-serif; color: var(--fg); }
  #c5 .sb { font-size: 52px; }
  /* urgency */
  #cal { position: absolute; left: 340px; top: 620px; width: 400px; height: 440px; border-radius: 34px; color: var(--ink); overflow: hidden; }
  #cal .cm { position: absolute; left: 0; right: 0; top: 0; height: 96px; line-height: 96px; text-align: center; background: var(--ink); color: #e6e6e6; font-size: 36px; letter-spacing: .3em; }
  #cal .d { position: absolute; left: 0; right: 0; top: 130px; text-align: center; font: 900 240px/1 "Fraunces", serif; letter-spacing: -0.04em; color: var(--ink); }
  .nite { top: 1120px; font: italic 400 76px/1.15 "Instrument Serif", serif; color: var(--fg); padding: 0 90px; box-sizing: border-box; }
'''

JS = r'''
  const Q = __Q__;
  const sheen = (sel, l, d = 0.9) => tl.fromTo(sel, { backgroundPosition: "100% 50%" }, { backgroundPosition: "0% 50%", duration: d, ease: "power2.inOut" }, A(l));
  // ---------- 1 HOOK: the pain is readable on frame 1 ----------
  cur = "s1";
  tl.set("#tag1", { y: -1100, opacity: 0 }, 0); tl.set("#tag1", { opacity: 1 }, A(0.5));
  tl.to("#tag1", { y: 0, duration: 0.42, ease: "back.out(1.3)" }, A(0.5));
  swing("#tag1", 1.1, 18, 1.5); sheen("#tag1 .tag", 2);
  tl.fromTo("#hook", { scale: 1.12 }, { scale: 1, duration: 0.45, ease: "expo.out" }, 0);
  sheen("#hook .ac", 1.5, 1.0); punch("#hook", 2, 1.04);

  // ---------- 2 ON THE DAY -> rewind -> WHAT ACTUALLY HAPPENED ----------
  cur = "s2";
  fadeUp("#lb1", 0); tl.set("#lb2", { opacity: 0 }, 0);
  wordsAt("#c2a", from(0, 7, Q));
  pop("#dash", 0.25, { y: 80, scale: 0.95 });
  count("#cn", 0.5, 214, B(3.5));
  const LL = draw("#ln", 0.5, B(3.75));
  [1, 2, 3].forEach(i => pop("#ts" + i, 0.5 + i * 0.75, { x: 60 }, 0.28));
  fadeOut("#c2a", 5.75);
  tl.set("#vhs", { opacity: 0.8 }, A(6)); tl.to("#vhs", { opacity: 0, duration: B(0.6), ease: "steps(4)" }, A(6.05));
  tl.to("#dash", { keyframes: { x: [-16, 12, -8, 5, 0] }, duration: B(0.5), ease: "none" }, A(6));
  tl.to("#ln", { strokeDashoffset: LL * 0.55, duration: B(0.5), ease: "power1.in" }, A(6));
  tl.to("#ln", { opacity: 0.3, duration: 0.2 }, A(6.5));
  tl.to("#lb1", { opacity: 0, duration: 0.1 }, A(6.5)); tl.set("#lb2", { opacity: 1 }, A(6.5));
  tl.to("#lb2", { keyframes: { scale: [1.12, 1] }, duration: 0.3, ease: "expo.out" }, A(6.5));
  wordsAt("#c2b", from(6.5, 11, Q));
  [1, 2, 3].forEach((i, k) => { const l = 8 + k * 0.5;
    tl.to("#ts" + i, { scaleY: 0, duration: 0.1, ease: "power2.in" }, A(l) - 0.1);
    tl.set("#ts" + i + " .fa", { opacity: 0 }, A(l)); tl.set("#ts" + i + " .bk", { opacity: 1 }, A(l));
    tl.to("#ts" + i, { scaleY: 1, duration: 0.14, ease: "power2.out" }, A(l)); });
  tl.to(["#ts1", "#ts2", "#ts3"], { opacity: 0, x: 60, duration: 0.2, stagger: 0.05, ease: "power2.in" }, A(10.5));
  pop("#tally", 10.75, { x: 60 });
  count("#nc", 11, 3, B(0.75), n => String(n), "steps(3)");
  punch("#tally", 11.75, 1.08); sheen("#nc", 11.75, 0.8);

  // ---------- 4 THE COST (bone) ----------
  cur = "s4";
  wordsAt("#c4 .kw", from(0, 7, Q)); wordsAt("#c4 .sb", from(1, 8, Q));
  tl.set("#tag4", { y: -900, opacity: 0 }, 0); tl.set("#tag4", { opacity: 1 }, A(0.25)); tl.to("#tag4", { y: 0, duration: 0.4, ease: "back.out(1.3)" }, A(0.25));
  swing("#tag4", 0.75, 9, 1.2);
  tl.set("#stk4", { opacity: 0, scale: 2.2, rotation: -40 }, 0);
  tl.to("#stk4", { opacity: 1, scale: 1, rotation: -12, duration: 0.22, ease: "power4.in" }, A(1.5) - 0.2);
  pop("#gaw", 2, { y: 60 });
  tl.set("#coin", { opacity: 0, scale: 0.3 }, 0);
  tl.to("#coin", { opacity: 1, scale: 1, duration: 0.2, ease: "back.out(2)" }, A(2.5));
  tl.to("#coin", { x: 340, y: -40, scale: 0.5, rotation: 200, duration: 0.4, ease: "power2.in" }, A(2.5) + 0.25);
  tl.to("#coin", { opacity: 0, duration: 0.05 }, A(2.5) + 0.65);
  punch("#gaw", 2.5 + 0.65 / P, 1.06);
  count("#gv", 3.25, 3852, B(2.5), euro);

  // ---------- 5 THE FIX + the offer, shown mid-video ----------
  cur = "s5";
  lineWipe(0);
  wordsAt("#c5 .ld", from(0, 4, Q)); wordsAt("#c5 .kw", from(0.75, 12, Q)); wordsAt("#c5 .sb", from(2.5, 10, Q));
  const f = document.getElementById("f5"); const by = {};
  for (let r = 0; r < 12; r++) for (let c = 0; c < 20; c++) { const x = c * 47 + 3, y = r * 44 + 3, d = Math.hypot(x + 7 - 457, y + 7 - 253);
    if (d < 190) continue; const el = document.createElement("i"); el.className = "dt"; el.style.left = x + "px"; el.style.top = y + "px"; f.insertBefore(el, f.firstChild);
    const k = Math.min(3, Math.floor((d - 190) / 110)); (by[k] = by[k] || []).push(el); }
  pop("#f5 .fc", 0.5, { scale: 0.6 });
  [2, 3, 4].forEach((l, i) => { tl.set("#rp" + (i + 1), { opacity: 0.9, scale: 1 }, A(l)); tl.to("#rp" + (i + 1), { opacity: 0, scale: 3.4, duration: 0.9, ease: "power2.out" }, A(l)); });
  [[2.5, 0], [3, 1], [3.5, 2], [4, 3]].forEach(([l, k]) => tl.to(by[k] || [], { backgroundColor: "#e6e6e6", duration: 0.15, stagger: 0.002 }, A(l)));
  [4.5, 5, 5.5, 6].forEach((l, i) => { pop("#nc" + (i + 1), l, { y: 30, scale: 0.6 }, 0.3); sheen("#nc" + (i + 1), l + 0.5, 0.7); });
  pop("#remind", 6.5, { y: 40, scale: 0.9 }); pulse("#remind", 8, 10, 0.03);

  // ---------- 6 URGENCY ----------
  cur = "s6";
  wordsAt("#c6", from(0, 5, Q));
  pop("#cal", 0.25, { y: 60, scale: 0.9 });
  tl.set(["#d26", "#d27"], { opacity: 0 }, 0);
  tl.set("#d25", { opacity: 0 }, A(1)); tl.set("#d26", { opacity: 1 }, A(1));
  tl.set("#d26", { opacity: 0 }, A(2)); tl.set("#d27", { opacity: 1 }, A(2));
  punch("#cal", 2, 1.1); flash(2, 0.4); sheen("#cal", 2, 0.9);
  fadeUp("#nite", 2.25);
'''.replace("__Q__", str(Q))

c = Cues(dict(SC))
c.add("s1", 0, "hit", 0.65); c.add("s1", 0.5, "whoosh", 0.3); c.add("s1", 0.95, "click", 0.35); c.add("s1", 1.5, "shimmer", 0.3)
for s in ("s2", "s4", "s6"): c.add(s, 0, "swish", 0.25, -0.1)
c.add("s2", 0.25, "pop", 0.3)
for i in (1, 2, 3): c.add("s2", 0.5 + i * 0.75, "coin", 0.3)
for k in range(7): c.add("s2", 0.5 + k * 0.5, "tick", 0.16)
c.add("s2", 6, "glitch", 0.35); c.add("s2", 6, "whoosh", 0.3, -0.3); c.add("s2", 6.5, "click", 0.35)
for l in (8, 8.5, 9): c.add("s2", l, "swish", 0.22)
c.add("s2", 10.75, "pop", 0.3); c.add("s2", 11.75, "hit", 0.5)
c.add("s4", 0.25, "swish", 0.3); c.add("s4", 1.5, "hit", 0.4); c.add("s4", 1.5, "click", 0.4); c.add("s4", 2, "pop", 0.3); c.add("s4", 2.5, "coin", 0.4)
for k in range(5): c.add("s4", 3.25 + k * 0.5, "tick", 0.2)
c.add("s5", 0, "whoosh", 0.45, -0.22); c.add("s5", 0.5, "pop", 0.3)
for l in (2, 3, 4): c.add("s5", l, "swish", 0.2)
for l in (4.5, 5, 5.5, 6): c.add("s5", l, "coin", 0.3)
c.add("s5", 6.5, "ping", 0.4)
c.add("s6", 0.25, "pop", 0.3); c.add("s6", 1, "click", 0.3); c.dropout("s6", 1.5, 2); c.add("s6", 2, "riser", 0.35, -0.62); c.add("s6", 2, "hit", 0.8)

d = build(HF, CUES, "SA: Black Friday v3", PAL, scenes, TOTAL, CSS, JS, c, endcard="sa", keyword="friday",
          sa_tagline="FOR A FREE BLACK FRIDAY AD PLAN",
          comment="Ad #9 v3 · Black / Bone / silver chrome · pain-first hook, 20.7 s, bigger text, offer shown mid-video")
print("wrote", HF, d, "s")
