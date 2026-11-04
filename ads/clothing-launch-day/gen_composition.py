#!/usr/bin/env python3
"""Ad #13 · Clothing brands · "Don't launch to an empty room."  Charcoal / Cream / Amber spotlight. Keyword: LAUNCH. SA end card.
    python3 gen_composition.py <hyperframes dir> <cues.json>"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../.claude/skills/videoad/scripts"))
from clearkit import build, cap, title2, Cues

HF, CUES = sys.argv[1], sys.argv[2]
PAL = {"--bg": "#141414", "--fg": "#f3eee4", "--paper": "#f3eee4", "--ink": "#141414", "--acc": "#ffb020", "--accd": "#9a6200",
       "--endbg": "#000000", "--glow": "rgba(255,176,32,.08)", "--mid": "#5b5852"}
SC = [("s1", 0), ("s2", 6), ("s3", 13), ("s4", 27), ("s5", 38), ("s6", 44), ("s7", 56), ("s8", 62)]
TOTAL = 69
ROWS, COLS = 6, 12
LIT = {(0, 4), (0, 5), (0, 6), (0, 7), (1, 3), (1, 5), (1, 8), (2, 6), (2, 2), (3, 9), (4, 4), (5, 7)}   # the few followers who show up

ICON = {
    "sketch": '<path d="M18 62 L52 28 L64 40 L30 74 L14 78 Z" fill="none" stroke="currentColor" stroke-width="6" stroke-linejoin="round"/><path d="M46 34 L58 46" stroke="currentColor" stroke-width="6"/>',
    "box": '<path d="M16 34 L46 20 L76 34 L76 66 L46 80 L16 66 Z M16 34 L46 48 L76 34 M46 48 V80" fill="none" stroke="currentColor" stroke-width="6" stroke-linejoin="round"/>',
    "camera": '<rect x="12" y="32" width="68" height="44" rx="8" fill="none" stroke="currentColor" stroke-width="6"/><circle cx="46" cy="54" r="13" fill="none" stroke="currentColor" stroke-width="6"/><path d="M30 32 L36 22 H56 L62 32" fill="none" stroke="currentColor" stroke-width="6" stroke-linejoin="round"/>',
}
HOODIE = ('<svg viewBox="0 0 120 130" width="150" height="162"><path d="M30 26 Q60 0 90 26 L116 70 L100 78 L92 62 V126 H28 V62 L20 78 L4 70 Z" fill="#f3eee4"/>'
          '<path d="M44 26 Q60 44 76 26" fill="none" stroke="#141414" stroke-width="5"/><rect x="40" y="88" width="40" height="22" rx="6" fill="#d9d2c4"/></svg>')


def steps():
    out = []
    for i, (k, lab) in enumerate([("sketch", "DESIGN"), ("box", "SAMPLES"), ("camera", "SHOOT")]):
        out.append(f'<div class="st" id="st{i}" style="left:{140 + i * 300}px"><div class="ic"><svg viewBox="0 0 92 92" width="92" height="92">{ICON[k]}</svg></div>'
                   f'<span class="mono">{lab}</span></div>')
    return "".join(out)


def seats(sid, top):
    cells = []
    for r in range(ROWS):
        for c in range(COLS):
            cls = "seat lit0" if (r, c) in LIT else "seat"
            cells.append(f'<i class="{cls}" data-r="{r}" style="left:{c * 70 + (r % 2) * 0}px;top:{r * 58}px"></i>')
    return f'<div class="seats" id="{sid}" style="top:{top}px">{"".join(cells)}</div>'


def stage(sid, top):
    return (f'<div class="stage" id="{sid}" style="top:{top}px"><i class="cone"></i><div class="hood">{HOODIE}</div><i class="ped"></i></div>')


S = {}
S["s1"] = ("dark", f'''
      {title2("t1", "Clothing", "brands.", 700, 200)}
      <div class="ctr sub" id="sub1" style="top:1180px">Got a launch coming up?</div>''')
S["s2"] = ("dark", f'''
      {cap("c2", "Why does launch day feel *so *quiet after months of work?", 580, 110)}''')
S["s3"] = ("dark", f'''
      {cap("c3a", "Months designing it.", 330, 96)}
      {cap("c3b", "Weeks waiting on samples.", 330, 96)}
      {cap("c3c", "A full day shooting it.", 330, 96)}
      {cap("c3d", "Then you *post *it.", 330, 96)}
      <div class="steps">{steps()}<div class="pb"><i id="pbf"></i></div></div>
      <div class="lpost" id="lpost"><div class="lh"><i></i><b>yourbrand</b><span class="live mono" id="live">LIVE</span></div><div class="li">{HOODIE}</div>
        <div class="lt">THE DROP IS LIVE 🔥 Link in bio.</div></div>''')
S["s4"] = ("dark", f'''
      {cap("c4a", "You launch to a *half-empty room.", 300, 88)}
      {cap("c4b", "Most people who'd love it never even *see *it.", 300, 88)}
      {stage("stg4", 590)}
      {seats("seat4", 1010)}
      <div class="ctr mono flab" id="fl4" style="top:1380px">THE SAME FEW FOLLOWERS SHOW UP</div>''')
S["s5"] = ("light", f'''
      {cap("c5", "Months of work. Seen by the *same *few *people.", 640, 116, serif=True)}''')
S["s6"] = ("dark", f'''
      {cap("c6", "We run Facebook & Instagram ads for your *launch.", 220, 82, sub="Build the buzz before it drops. Fill the room on the day.")}
      {stage("stg6", 680)}
      {seats("seat6", 1060)}
      <div class="ctr mono flab" id="fl6" style="top:1415px"><i class="dot"></i> NEW PEOPLE, FROM YOUR ADS</div>''')
S["s7"] = ("dark", f'''
      {cap("c7", "Launch to a *full *room.", 420, 150, serif=True)}
      {seats("seat7", 900)}''')
S["s8"] = ("end", "")
scenes = [(k, s, S[k][0], S[k][1]) for k, s in SC]

CSS = '''
  .steps { position: absolute; left: 0; top: 560px; width: 1080px; height: 360px; }
  .st { position: absolute; top: 0; width: 200px; text-align: center; }
  .st .ic { width: 150px; height: 150px; margin: 0 auto 16px; border-radius: 50%; border: 4px solid #3a3833; display: flex; align-items: center; justify-content: center; color: var(--fg); box-sizing: border-box; }
  .st.on .ic { border-color: var(--acc); color: var(--acc); }
  .st span { font-size: 22px; opacity: .8; }
  .pb { position: absolute; left: 190px; top: 260px; width: 700px; height: 14px; border-radius: 7px; background: #2b2a27; overflow: hidden; }
  .pb i { display: block; height: 100%; width: 100%; background: var(--acc); transform-origin: 0 50%; transform: scaleX(0); }
  .lpost { position: absolute; left: 290px; top: 880px; width: 500px; border-radius: 28px; background: #1f1e1c; border: 2px solid #33312d; box-sizing: border-box; padding: 18px; }
  .lh { display: flex; align-items: center; gap: 12px; } .lh i { width: 44px; height: 44px; border-radius: 50%; background: var(--acc); }
  .lh b { font: 700 26px "Instrument Sans", sans-serif; } .live { margin-left: auto; background: var(--acc); color: var(--ink); border-radius: 8px; padding: 6px 12px 4px; font-size: 18px; }
  .li { margin-top: 14px; height: 260px; border-radius: 18px; background: #2b2a27; display: flex; align-items: center; justify-content: center; }
  .lt { margin-top: 14px; font: 500 26px "Instrument Sans", sans-serif; }
  .stage { position: absolute; left: 0; width: 1080px; height: 400px; }
  .cone { position: absolute; left: 290px; top: -40px; width: 500px; height: 420px; clip-path: polygon(42% 0, 58% 0, 100% 100%, 0 100%);
    background: linear-gradient(180deg, rgba(255,176,32,.55) 0%, rgba(255,176,32,.08) 100%); }
  .hood { position: absolute; left: 465px; top: 160px; }
  .ped { position: absolute; left: 400px; top: 330px; width: 280px; height: 50px; border-radius: 50%; background: #2b2a27; box-shadow: 0 0 0 3px #3a3833; }
  .seats { position: absolute; left: 125px; width: 840px; height: 340px; }
  .seat { position: absolute; width: 52px; height: 40px; border-radius: 12px 12px 6px 6px; background: #2a2926; }
  .seat.lit0 { background: var(--acc); }
  #stg6 .cone { top: 40px; height: 340px; }
  #stg6 .hood { top: 170px; }
'''

JS = r'''
  // ---------- 1 CALLOUT ----------
  cur = "s1";
  tl.set("#t1b", { yPercent: 140 }, 0); tl.to("#t1b", { yPercent: 0, duration: 0.25, ease: "expo.out" }, A(0.5));
  punch("#t1", 1.5, 1.05); fadeUp("#sub1", 2.5);

  // ---------- 2 OPEN LOOP ----------
  cur = "s2";
  wordsAt("#c2", from(0, 11, 0.4));

  // ---------- 3 RELATE: months of work, then one post ----------
  cur = "s3";
  const capsR = ["#c3a", "#c3b", "#c3c", "#c3d"];
  [0, 3.5, 7, 10.5].forEach((l, i) => { wordsAt(capsR[i], from(l, 5, 0.25)); if (i < 3) fadeOut(capsR[i], l + 3.3); });
  [0, 1, 2].forEach(i => { pop("#st" + i, 0.25 + i * 3.5, { y: 40, scale: 0.85 });
    tl.call(() => {}, [], A(0.5 + i * 3.5));
    tl.to("#st" + i + " .ic", { borderColor: "#ffb020", color: "#ffb020", duration: 0.2 }, A(0.75 + i * 3.5));
    tl.to("#pbf", { scaleX: (i + 1) / 3, duration: 0.5, ease: "power2.out" }, A(1 + i * 3.5)); });
  tl.to(".steps", { y: -40, scale: 0.8, opacity: 0.35, duration: 0.4, ease: "power2.inOut" }, A(10.5));
  pop("#lpost", 10.75, { y: 120, scale: 0.92 });
  tl.set("#live", { opacity: 0, scale: 2 }, 0); tl.to("#live", { opacity: 1, scale: 1, duration: 0.2, ease: "power4.in" }, A(12) - 0.18);

  // ---------- 4 PROBLEM: half-empty room ----------
  cur = "s4";
  wordsAt("#c4a", from(0, 6, 0.25));
  pop("#stg4", 0.25, { y: -40 });
  const S4 = Array.from(document.querySelectorAll("#seat4 .seat"));
  tl.set(S4, { opacity: 0, y: 20 }, 0); tl.to(S4, { opacity: 1, y: 0, duration: 0.2, stagger: { each: 0.006, from: "start" } }, A(1));
  tl.set("#seat4 .lit0", { backgroundColor: "#2a2926" }, 0); tl.to("#seat4 .lit0", { backgroundColor: "#ffb020", duration: 0.1, stagger: 0.06 }, A(2.5));
  fadeUp("#fl4", 3.5);
  fadeOut("#c4a", 4.6);
  wordsAt("#c4b", from(5, 9, 0.25));
  tl.to("#stg4 .cone", { keyframes: { opacity: [0.6, 1, 0.75, 1] }, duration: 1.2, ease: "none" }, A(7));

  // ---------- 5 STING ----------
  cur = "s5";
  wordsAt("#c5", from(0, 9, 0.3)); punch("#c5", 3.5, 1.04);

  // ---------- 6 FIX: fill the room ----------
  cur = "s6";
  lineWipe(0);
  wordsAt("#c6 .kw", from(0, 8, 0.4));
  wordsAt("#c6 .sb", from(3.5, 12, 0.25));
  pop("#stg6", 0.5, { y: -40 });
  pop("#seat6", 0.75, { y: 40 });
  for (let r = 0; r < 6; r++) tl.to("#seat6 .seat[data-r='" + r + "']", { backgroundColor: "#ffb020", duration: 0.12, stagger: 0.012 }, A(6.5 + r * 0.5));
  fadeUp("#fl6", 8);
  tl.to("#stg6 .cone", { opacity: 1, scaleX: 1.15, duration: 0.6, ease: "power2.out" }, A(6.5));

  // ---------- 7 PAYOFF ----------
  cur = "s7";
  wordsAt("#c7", from(0, 5, 0.4));
  tl.set("#seat7 .seat", { backgroundColor: "#ffb020" }, 0);
  pop("#seat7", 1, { y: 40 });
  pulse("#seat7", 2, 6, 0.02);
'''

c = Cues(dict(SC))
c.add("s1", 0, "hit", 0.6); c.add("s1", 0.5, "pop", 0.3); c.add("s1", 1.5, "shimmer", 0.25)
for s in ("s2", "s3", "s4", "s5", "s7"): c.add(s, 0, "swish", 0.25, -0.1)
for i in range(3): c.add("s3", 0.25 + i * 3.5, "pop", 0.3); c.add("s3", 1 + i * 3.5, "tick", 0.25)
c.add("s3", 10.75, "whoosh", 0.3); c.add("s3", 12, "hit", 0.45); c.add("s3", 12, "click", 0.35)
c.add("s4", 0.25, "riser", 0.2); c.add("s4", 2.5, "tick", 0.2); c.add("s4", 7, "glitch", 0.2)
c.add("s6", 0, "whoosh", 0.45, -0.22); c.add("s6", 0.5, "pop", 0.3)
for r in range(6): c.add("s6", 6.5 + r * 0.5, "tick", 0.3)
c.add("s6", 9.5, "shimmer", 0.35)
c.dropout("s6", 11.5, 12); c.add("s7", 0, "hit", 0.75); c.add("s7", 1, "pop", 0.3)

d = build(HF, CUES, "SA: Launch day", PAL, scenes, TOTAL, CSS, JS, c, endcard="sa", keyword="launch",
          comment="Ad #13 · Charcoal #141414 / Cream #F3EEE4 / Amber #FFB020 · 'Don't launch to an empty room.'")
print("wrote", HF, d, "s")
