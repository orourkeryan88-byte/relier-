#!/usr/bin/env python3
"""Ad #10 · Electricians in Ireland · "You can't turn word of mouth up."  Slate / Chalk / Copper. Keyword: BUSY.
    python3 gen_composition.py <hyperframes dir> <cues.json>"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../.claude/skills/videoad/scripts"))
from clearkit import build, cap, title2, phone, Cues

HF, CUES = sys.argv[1], sys.argv[2]
PAL = {"--bg": "#1c2127", "--fg": "#f1eee8", "--paper": "#f1eee8", "--ink": "#1c2127", "--acc": "#e08a4e", "--accd": "#a5561f",
       "--endbg": "#14181d", "--glow": "rgba(224,138,78,.10)", "--mid": "#5c6670"}
SC = [("s1", 0), ("s2", 6), ("s3", 13), ("s4", 26), ("s5", 36), ("s6", 43), ("s7", 55), ("s8", 61)]
TOTAL = 68


def house(hid, left, top, place):
    return (f'<div class="hs" id="{hid}" style="left:{left}px;top:{top}px"><svg viewBox="0 0 200 180" width="200" height="180">'
            f'<path d="M14 82 L100 14 L186 82" fill="none" stroke="#f1eee8" stroke-width="6" stroke-linejoin="round"/>'
            f'<rect x="34" y="74" width="132" height="98" rx="6" fill="#262c33" stroke="#f1eee8" stroke-width="5"/>'
            f'<rect class="win" x="54" y="96" width="40" height="34" rx="4" fill="#3a424b"/><rect x="112" y="112" width="34" height="60" rx="4" fill="#3a424b"/></svg>'
            f'<div class="hl mono">{place}</div></div>')


def week(wid, label, top, light=False):
    days = "".join(f'<div class="cell" id="{wid}c{i}"><span class="dn mono">{d}</span><span class="jb">JOB</span></div>'
                   for i, d in enumerate(["MON", "TUE", "WED", "THU", "FRI"]))
    return f'<div class="wk{" lt" if light else ""}" id="{wid}" style="top:{top}px"><div class="wl mono">{label}</div><div class="cells">{days}</div></div>'


def dial(did, left, top, label, light=False):
    track = "#d6cfc4" if light else "#353d46"
    return (f'<div class="dial" id="{did}" style="left:{left}px;top:{top}px"><svg viewBox="0 0 400 330" width="400" height="330">'
            f'<path d="M70.1 275 A150 150 0 1 1 329.9 275" fill="none" stroke="{track}" stroke-width="26" stroke-linecap="round"/>'
            f'<path class="fill" id="{did}f" d="M70.1 275 A150 150 0 1 1 329.9 275" fill="none" stroke="var(--acc)" stroke-width="26" stroke-linecap="round"/>'
            f'<line class="ndl" id="{did}n" x1="200" y1="200" x2="320" y2="200" stroke="{"#1c2127" if light else "#f1eee8"}" stroke-width="10" stroke-linecap="round"/>'
            f'<circle cx="200" cy="200" r="20" fill="{"#1c2127" if light else "#f1eee8"}"/>'
            f'<text x="62" y="318" class="dt">LOW</text><text x="300" y="318" class="dt">BUSY</text></svg>'
            f'<div class="dl mono">{label}</div></div>')


NOTE = lambda i, top, job, place: (f'<div class="note" id="n{i}" style="top:{top}px"><b>New enquiry</b>{job} · {place}<br>'
                                   f'<span style="opacity:.6">Checked · wants a quote</span></div>')

S = {}
S["s1"] = ("dark", f'''
      {title2("t1", "Electricians", "in Ireland.", 720, 150)}
      <svg class="wire" viewBox="0 0 1080 1920" data-layout-ignore><path id="w0" d="M-20 1130 Q270 1210 540 1130 T1100 1130" fill="none" stroke="var(--acc)" stroke-width="6" stroke-linecap="round"/></svg>
      <div class="ctr sub" id="sub1" style="top:1230px">This one's for you.</div>''')
S["s2"] = ("dark", f'''
      {cap("c2", "Where's your *next *month of work coming from?", 620, 112)}''')
S["s3"] = ("dark", f'''
      {cap("c3a", "Right now, most of your work comes from *word *of *mouth.", 330, 80)}
      {cap("c3b", "One good job leads to the *next.", 330, 80)}
      <svg class="wire" viewBox="0 0 1080 1920" data-layout-ignore>
        <path id="w1" d="M290 1000 Q400 1080 500 1000" fill="none" stroke="var(--acc)" stroke-width="6" stroke-linecap="round"/>
        <path id="w2" d="M620 1000 Q720 1080 820 1000" fill="none" stroke="var(--acc)" stroke-width="6" stroke-linecap="round"/></svg>
      {house("h1", 90, 900, "JOB · NAAS")}{house("h2", 440, 900, "JOB · NEWBRIDGE")}{house("h3", 790, 900, "JOB · KILDARE")}
      <div class="rec mono" id="rec1" style="left:250px;top:830px">★ "Ring this lad"</div>
      <div class="rec mono" id="rec2" style="left:615px;top:830px">★ "He did ours"</div>''')
S["s4"] = ("dark", f'''
      {cap("c4a", "But you can't control *when people mention you.", 330, 80)}
      {cap("c4b", "Some weeks are packed. Some weeks are *dead *quiet.", 330, 80)}
      {week("wa", "THIS WEEK", 680)}{week("wb", "NEXT WEEK", 940)}
      <div class="stamp" id="quiet">QUIET</div>''')
S["s5"] = ("light", f'''
      {dial("d5", 340, 330, "WORD OF MOUTH", light=True)}
      {cap("c5", "And you can't turn word of mouth *up when it's quiet.", 930, 96, serif=True)}''')
S["s6"] = ("dark", f'''
      {cap("c6", "We run Facebook & Instagram ads for your *business.", 230, 82, sub="Homeowners near you see your work. Enquiries come *straight *to *your *phone.")}
      {dial("d6", 60, 820, "YOUR ADS")}
      {phone("ph6", 560, 700, '<div class="lk">09:41</div>' + NOTE(1, 170, "Rewire", "Naas") + NOTE(2, 300, "EV charger", "Newbridge") + NOTE(3, 430, "Fuse board", "Kildare"), 420, 700)}''')
S["s7"] = ("dark", f'''
      {cap("c7", "Keep the referrals. Stop *relying on them.", 380, 120, serif=True)}
      {week("wc", "THIS WEEK", 840)}{week("wd", "NEXT WEEK", 1100)}''')
S["s8"] = ("end", "")
scenes = [(k, s, S[k][0], S[k][1]) for k, s in SC]

CSS = '''
  .wire { position: absolute; left: 0; top: 0; width: 1080px; height: 1920px; overflow: visible; }
  .hs { position: absolute; width: 200px; text-align: center; }
  .hl { margin-top: 10px; font-size: 20px; color: var(--acc); }
  .rec { position: absolute; background: #2a3139; color: var(--fg); border: 2px solid var(--acc); border-radius: 22px; padding: 8px 16px 6px; font-size: 18px; letter-spacing: .06em; }
  .wk { position: absolute; left: 90px; width: 900px; }
  .wl { font-size: 20px; opacity: .7; margin-bottom: 12px; }
  .cells { display: flex; gap: 14px; }
  .cell { position: relative; width: 168px; height: 150px; border-radius: 18px; border: 3px solid #3a424b; box-sizing: border-box; background: #232930; }
  .cell .dn { position: absolute; left: 14px; top: 12px; font-size: 18px; opacity: .6; }
  .cell .jb { position: absolute; left: 0; right: 0; bottom: 22px; text-align: center; font: 900 46px "Fraunces", serif; color: var(--bg); opacity: 0; }
  .stamp { position: absolute; left: 330px; top: 1010px; width: 420px; text-align: center; font: 900 110px/1 "Fraunces", serif; color: var(--fg);
    border: 8px solid var(--fg); border-radius: 18px; padding: 10px 0 18px; transform: rotate(-8deg); background: rgba(28,33,39,.8); }
  .dial { position: absolute; width: 400px; text-align: center; }
  .dial .dt { font: 500 18px "IBM Plex Mono", monospace; letter-spacing: .12em; fill: currentColor; opacity: .6; }
  .dial .dl { font-size: 24px; margin-top: 8px; }
  .light .dial .dl { color: var(--ink); }
  #ph6 .scr { background: linear-gradient(180deg, #2a3038 0%, #1a1e23 100%); color: #f1eee8; }
  .lk { position: absolute; left: 0; right: 0; top: 60px; text-align: center; font: 700 64px "Instrument Sans", sans-serif; letter-spacing: -0.02em; }
'''

JS = r'''
  // ---------- 1 CALLOUT ----------
  cur = "s1";
  tl.set("#t1b", { yPercent: 140 }, 0); tl.to("#t1b", { yPercent: 0, duration: 0.25, ease: "expo.out" }, A(0.5));
  draw("#w0", 1, 0.6); punch("#t1", 2, 1.05); fadeUp("#sub1", 2.5);

  // ---------- 2 OPEN LOOP ----------
  cur = "s2";
  wordsAt("#c2", from(0, 8));

  // ---------- 3 RELATE: one job leads to the next ----------
  cur = "s3";
  wordsAt("#c3a", from(0, 11, 0.25));
  pop("#h1", 0.5, { y: 60, scale: 0.9 });
  tl.set("#h1 .win", { attr: { fill: "#3a424b" } }, 0); tl.to("#h1 .win", { attr: { fill: "#e08a4e" }, duration: 0.2 }, A(1));
  draw("#w1", 3, 0.45); pop("#rec1", 3.25, { y: 20, scale: 0.8 });
  pop("#h2", 3.5, { y: 60, scale: 0.9 }); tl.set("#h2 .win", { attr: { fill: "#3a424b" } }, 0); tl.to("#h2 .win", { attr: { fill: "#e08a4e" }, duration: 0.2 }, A(4));
  fadeOut("#c3a", 6.5);
  wordsAt("#c3b", from(7, 7, 0.25));
  draw("#w2", 7.5, 0.45); pop("#rec2", 7.75, { y: 20, scale: 0.8 });
  pop("#h3", 8, { y: 60, scale: 0.9 }); tl.set("#h3 .win", { attr: { fill: "#3a424b" } }, 0); tl.to("#h3 .win", { attr: { fill: "#e08a4e" }, duration: 0.2 }, A(8.5));
  pulse(["#h1", "#h2", "#h3"], 9, 13, 0.03);

  // ---------- 4 PROBLEM: packed weeks, dead weeks ----------
  cur = "s4";
  wordsAt("#c4a", from(0, 8, 0.25));
  pop("#wa", 0.5, { y: 40 }); pop("#wb", 1, { y: 40 });
  [0, 1, 2, 3, 4].forEach(i => { tl.to("#wac" + i, { backgroundColor: "#e08a4e", borderColor: "#e08a4e", duration: 0.12 }, A(2 + i * 0.25));
    tl.set("#wac" + i + " .jb", { opacity: 1 }, A(2 + i * 0.25)); });
  fadeOut("#c4a", 4.6);
  wordsAt("#c4b", from(5, 9, 0.25));
  tl.set("#quiet", { opacity: 0, scale: 2, rotation: -20 }, 0);
  tl.to("#quiet", { opacity: 1, scale: 1, rotation: -8, duration: 0.22, ease: "power4.in" }, A(7.25) - 0.2);
  punch("#wb", 7.25, 1.03);

  // ---------- 5 STING: the dial you can't turn up ----------
  cur = "s5";
  draw("#d5f", 0, 0.01, 1, 0.85);
  tl.set("#d5n", { rotation: 186, svgOrigin: "200 200" }, 0);
  tl.to("#d5f", { strokeDashoffset: () => document.querySelector("#d5f").getTotalLength() * 0.3, duration: 0.5, ease: "power2.out" }, A(1));
  tl.to("#d5n", { rotation: 318, svgOrigin: "200 200", duration: 0.5, ease: "power2.out" }, A(1));
  tl.to("#d5f", { strokeDashoffset: () => document.querySelector("#d5f").getTotalLength() * 0.85, duration: 0.7, ease: "elastic.out(1, 0.4)" }, A(2));
  tl.to("#d5n", { rotation: 186, svgOrigin: "200 200", duration: 0.7, ease: "elastic.out(1, 0.4)" }, A(2));
  wordsAt("#c5", from(0.5, 11, 0.25));

  // ---------- 6 FIX: a dial you control ----------
  cur = "s6";
  lineWipe(0);
  wordsAt("#c6 .kw", from(0, 8, 0.5));
  wordsAt("#c6 .sb", from(4, 12, 0.25));
  draw("#d6f", 0, 0.01, 1, 0.9);
  tl.set("#d6n", { rotation: 174, svgOrigin: "200 200" }, 0);
  pop("#d6", 0.5, { scale: 0.85 });
  tl.to("#d6f", { strokeDashoffset: () => document.querySelector("#d6f").getTotalLength() * 0.1, duration: 0.8, ease: "power3.out" }, A(1.5));
  tl.to("#d6n", { rotation: 366, svgOrigin: "200 200", duration: 0.8, ease: "power3.out" }, A(1.5));
  pop("#ph6", 1, { x: 80 });
  [1, 2, 3].forEach(i => pop("#n" + i, 5 + i * 1, { y: -30, scale: 0.9 }, 0.3));

  // ---------- 7 PAYOFF ----------
  cur = "s7";
  wordsAt("#c7", from(0, 6, 0.5));
  pop("#wc", 0.5, { y: 40 }); pop("#wd", 0.75, { y: 40 });
  ["wc", "wd"].forEach((w, k) => [0, 1, 2, 3, 4].forEach(i => { const l = 1 + k * 1.25 + i * 0.25;
    tl.to("#" + w + "c" + i, { backgroundColor: "#e08a4e", borderColor: "#e08a4e", duration: 0.12 }, A(l)); tl.set("#" + w + "c" + i + " .jb", { opacity: 1 }, A(l)); }));
'''

c = Cues(dict(SC))
c.add("s1", 0, "hit", 0.6); c.add("s1", 0.5, "pop", 0.3); c.add("s1", 1, "whoosh", 0.3); c.add("s1", 2.5, "shimmer", 0.25)
for s in ("s2", "s3", "s4", "s7"): c.add(s, 0, "swish", 0.25, -0.1)
c.add("s3", 0.5, "pop", 0.3); c.add("s3", 3, "whoosh", 0.25); c.add("s3", 3.25, "ping", 0.25); c.add("s3", 3.5, "pop", 0.3)
c.add("s3", 7.5, "whoosh", 0.25); c.add("s3", 7.75, "ping", 0.25); c.add("s3", 8, "pop", 0.3)
c.add("s4", 0.5, "pop", 0.25); c.add("s4", 1, "pop", 0.25)
for i in range(5): c.add("s4", 2 + i * 0.25, "tick", 0.3)
c.add("s4", 7.25, "hit", 0.6); c.add("s4", 7.25, "click", 0.4)
c.add("s5", 0, "swish", 0.3, -0.1); c.add("s5", 1, "riser", 0.25); c.add("s5", 2, "glitch", 0.3); c.add("s5", 2, "click", 0.35)
c.add("s6", 0, "whoosh", 0.45, -0.22); c.add("s6", 1, "pop", 0.3); c.add("s6", 1.5, "shimmer", 0.35); c.add("s6", 1.5, "riser", 0.3)
for i in (6, 7, 8): c.add("s6", i, "ping", 0.35)
c.dropout("s6", 11.5, 12); c.add("s7", 0, "hit", 0.75)
for k in range(10): c.add("s7", 1 + (k // 5) * 1.25 + (k % 5) * 0.25, "tick", 0.25)

d = build(HF, CUES, "Southline: Word of mouth", PAL, scenes, TOTAL, CSS, JS, c, endcard="southline", keyword="busy",
          end_lines=("Electricians", "in Ireland."), end_size=128,
          comment="Ad #10 · Slate #1C2127 / Chalk #F1EEE8 / Copper #E08A4E · 'You can't turn word of mouth up.'")
print("wrote", HF, d, "s")
