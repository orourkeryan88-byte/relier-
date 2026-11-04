#!/usr/bin/env python3
"""Ad #11 · Electricians in Ireland · "Your van vs their feed."  Asphalt / Paper / Electric lime. Keyword: SEEN.
    python3 gen_composition.py <hyperframes dir> <cues.json>"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../.claude/skills/videoad/scripts"))
from clearkit import build, cap, title2, phone, Cues

HF, CUES = sys.argv[1], sys.argv[2]
PAL = {"--bg": "#161616", "--fg": "#f3f2ec", "--paper": "#f3f2ec", "--ink": "#161616", "--acc": "#c6f432", "--accd": "#5b7600",
       "--endbg": "#0f0f0f", "--glow": "rgba(198,244,50,.07)", "--mid": "#5a5a55"}
SC = [("s1", 0), ("s2", 6), ("s3", 13), ("s4", 26), ("s5", 37), ("s6", 43), ("s7", 55), ("s8", 61)]
TOTAL = 68

VAN = '''<svg viewBox="0 0 520 250" width="{w}" height="{h}">
  <path d="M20 60 Q20 40 40 40 H370 Q392 40 404 58 L470 128 Q500 134 500 160 V196 Q500 206 490 206 H30 Q20 206 20 196 Z" fill="#ecebe4"/>
  <path d="M386 62 H402 L452 124 H386 Z" fill="#2a2a2a"/>
  <rect x="20" y="170" width="364" height="12" fill="#c6f432"/>
  <text x="44" y="104" style="font: 900 46px Fraunces, serif; letter-spacing: -1px" fill="#161616">YOUR NAME</text>
  <text x="46" y="142" style="font: 500 26px 'IBM Plex Mono', monospace; letter-spacing: 6px" fill="#161616">ELECTRICAL</text>
  <text x="300" y="142" style="font: 500 18px 'IBM Plex Mono', monospace" fill="#5a5a55">087 XXX XXXX</text>
  <circle cx="120" cy="208" r="34" fill="#111" stroke="#f3f2ec" stroke-width="6"/><circle cx="120" cy="208" r="11" fill="#8a8a85"/>
  <circle cx="410" cy="208" r="34" fill="#111" stroke="#f3f2ec" stroke-width="6"/><circle cx="410" cy="208" r="11" fill="#8a8a85"/>
</svg>'''


def house(hid, left):
    return (f'<div class="hs" id="{hid}" style="left:{left}px"><svg viewBox="0 0 200 200" width="200" height="200">'
            f'<path d="M12 86 L100 16 L188 86" fill="none" stroke="#5a5a55" stroke-width="6" stroke-linejoin="round"/>'
            f'<rect x="30" y="78" width="140" height="116" rx="6" fill="#1f1f1f" stroke="#5a5a55" stroke-width="5"/>'
            f'<rect class="win" x="52" y="104" width="44" height="40" rx="4" fill="#2b2b2b"/><rect class="win" x="108" y="104" width="44" height="40" rx="4" fill="#2b2b2b"/></svg></div>')


FEED = '''
  <div class="card" id="cd1" style="top:70px"><div class="hd"><i class="av"></i><span>Lucan Community<span class="sp">GROUP POST</span></span></div>
    <div class="tx2">Anyone know a good electrician? Need a few sockets moved 🙏</div><div class="cm2 mono">14 COMMENTS</div></div>
  <div class="card" id="cd2" style="top:380px"><div class="hd"><i class="av"></i><span>Another electrician<span class="sp">SPONSORED</span></span></div>
    <div class="im"></div><div class="btn">Book now</div></div>
  <div class="bk2 mono" id="bk2">✓ BOOKED</div>'''
OURS = f'''
  <div class="card ours" id="cd3" style="top:140px"><div class="hd"><i class="av lime"></i><span>YOUR NAME Electrical<span class="sp">SPONSORED</span></span></div>
    <div class="im vanim">{VAN.format(w=360, h=173)}</div><div class="btn lime" id="btn3">Get a quote</div></div>
  <div class="note" id="nt6" style="top:24px"><b>New enquiry</b>Kitchen rewire · Lucan</div>'''

S = {}
S["s1"] = ("dark", f'''
      {title2("t1", "Electricians", "in Ireland.", 700, 150)}
      <div class="ctr sub" id="sub1" style="top:1150px">Take a look at your van for a second.</div>''')
S["s2"] = ("dark", f'''
      {cap("c2", "Who actually sees your *name on the van?", 600, 116)}''')
S["s3"] = ("dark", f'''
      {cap("c3a", "Your van's parked outside a job in *Lucan all day.", 300, 82)}
      {cap("c3b", "Next door, the neighbours are on their *phones.", 300, 82)}
      <div class="street">{house("h1", 30)}{house("h2", 300)}{house("h3", 580)}{house("h4", 850)}</div>
      <i class="road"></i>
      <div class="van" id="van">{VAN.format(w=780, h=375)}</div>''')
S["s4"] = ("dark", f'''
      {cap("c4a", "When they need an electrician, they don't go outside and check your van.", 250, 76)}
      {cap("c4b", "They ask online. And they *book *someone *else.", 250, 76)}
      {phone("ph4", 300, 540, FEED, 480, 840)}''')
S["s5"] = ("light", f'''
      {cap("c5", "If you're not in their feed, you're not on their *list.", 520, 108, serif=True)}
      <div class="slot" id="slot"><span class="mono">YOUR NAME ELECTRICAL</span><b>not here</b></div>''')
S["s6"] = ("dark", f'''
      {cap("c6", "We run Facebook & Instagram ads that put you in their *feed.", 220, 80, sub="Homeowners near your jobs see your work. Enquiries come straight to your phone.")}
      {phone("ph6", 300, 650, OURS, 480, 780)}''')
S["s7"] = ("dark", f'''
      {cap("c7", "Keep the van. Add the *feed.", 430, 140, serif=True)}
      <div class="duo" id="duo"><div class="mv">{VAN.format(w=330, h=159)}</div><b class="plus">+</b><div class="mp" id="mp"><i></i><i></i><i></i></div></div>''')
S["s8"] = ("end", "")
scenes = [(k, s, S[k][0], S[k][1]) for k, s in SC]

CSS = '''
  .street { position: absolute; left: 0; top: 600px; width: 1080px; height: 220px; }
  .hs { position: absolute; top: 0; width: 200px; }
  .road { position: absolute; left: 0; right: 0; top: 1270px; height: 6px; background: #2b2b2b; }
  .van { position: absolute; left: 150px; top: 900px; width: 780px; }
  .card .hd { font-size: 24px; } .card .sp { font-size: 17px; } .card .tx2 { font-size: 29px; }
  .card .cm2 { margin-top: 12px; font-size: 17px; color: #777; }
  .note { font-size: 22px; } .note b { font-size: 26px; }
  .card .btn { margin-top: 12px; height: 46px; border-radius: 12px; background: #161616; color: #f3f2ec; display: flex; align-items: center; justify-content: center; font: 700 20px "Instrument Sans", sans-serif; }
  .card .btn.lime { background: #c6f432; color: #161616; }
  .card .av.lime { background: #c6f432; }
  .card.ours { box-shadow: 0 0 0 4px #c6f432; }
  .vanim { display: flex; align-items: center; justify-content: center; background: #2a2a2a; height: 190px; }
  .bk2 { position: absolute; left: 250px; top: 560px; background: #161616; color: #c6f432; padding: 10px 16px 8px; border-radius: 10px; font-size: 20px; transform: rotate(-6deg); }
  .slot { position: absolute; left: 190px; top: 960px; width: 700px; height: 220px; border: 5px dashed #a9a8a1; border-radius: 28px; box-sizing: border-box;
    display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 12px; color: #77766f; }
  .slot b { font: italic 400 64px "Instrument Serif", serif; }
  .duo { position: absolute; left: 0; width: 1080px; top: 960px; display: flex; align-items: center; justify-content: center; gap: 40px; }
  .plus { font: 900 120px/1 "Fraunces", serif; color: var(--acc); }
  .mp { position: relative; width: 150px; height: 270px; border-radius: 28px; border: 6px solid var(--fg); box-sizing: border-box; padding: 26px 14px; display: flex; flex-direction: column; gap: 12px; }
  .mp i { display: block; height: 52px; border-radius: 10px; background: #2b2b2b; }
  .mp i:first-child { background: var(--acc); }
'''

JS = r'''
  // ---------- 1 CALLOUT ----------
  cur = "s1";
  tl.set("#t1b", { yPercent: 140 }, 0); tl.to("#t1b", { yPercent: 0, duration: 0.25, ease: "expo.out" }, A(0.5));
  punch("#t1", 1.5, 1.05); fadeUp("#sub1", 2.5);

  // ---------- 2 OPEN LOOP ----------
  cur = "s2";
  wordsAt("#c2", from(0, 8));

  // ---------- 3 RELATE: the van outside a job, the neighbours on their phones ----------
  cur = "s3";
  wordsAt("#c3a", from(0, 10, 0.25));
  pop(".street", 0.25, { y: 30 });
  tl.set("#van", { x: 1100 }, 0); tl.to("#van", { x: 0, duration: 0.9, ease: "power3.out" }, A(0.5));
  tl.to("#van", { keyframes: { y: [-6, 0] }, duration: 0.3, ease: "power2.out" }, A(0.5) + 0.9);
  fadeOut("#c3a", 6.4);
  wordsAt("#c3b", from(6.75, 8, 0.25));
  ["#h1", "#h2", "#h3", "#h4"].forEach((h, i) => tl.to(h + " .win", { attr: { fill: "#c6f432" }, duration: 0.12, stagger: 0.05 }, A(8 + i * 0.5)));
  pulse(".street", 10, 13, 0.02);

  // ---------- 4 PROBLEM: they ask online and book someone else ----------
  cur = "s4";
  wordsAt("#c4a", from(0, 13, 0.25));
  pop("#ph4", 0.5, { y: 120 });
  pop("#cd1", 1.25, { y: 30 });
  fadeOut("#c4a", 5.6);
  wordsAt("#c4b", from(6, 7, 0.25));
  pop("#cd2", 7, { y: 60 });
  tl.set("#bk2", { opacity: 0, scale: 2 }, 0); tl.to("#bk2", { opacity: 1, scale: 1, duration: 0.2, ease: "power4.in" }, A(8.5) - 0.18);

  // ---------- 5 STING ----------
  cur = "s5";
  wordsAt("#c5", from(0, 12, 0.25));
  pop("#slot", 2.5, { scale: 0.9 });
  tl.to("#slot", { keyframes: { x: [-10, 8, -5, 0] }, duration: 0.3, ease: "none" }, A(3.5));

  // ---------- 6 FIX: in their feed ----------
  cur = "s6";
  lineWipe(0);
  wordsAt("#c6 .kw", from(0, 11, 0.25));
  wordsAt("#c6 .sb", from(3.5, 13, 0.25));
  pop("#ph6", 0.75, { y: 120 });
  pop("#cd3", 2, { y: 60, scale: 0.95 });
  tl.to("#btn3", { keyframes: { scale: [0.9, 1] }, duration: 0.2, ease: "power2.out" }, A(7.5));
  tl.set("#nt6", { opacity: 0, y: -90 }, 0); tl.to("#nt6", { opacity: 1, y: 0, duration: 0.35, ease: "back.out(1.6)" }, A(8));
  punch("#ph6", 8, 1.03);

  // ---------- 7 PAYOFF ----------
  cur = "s7";
  wordsAt("#c7", from(0, 6, 0.5));
  pop("#duo", 1, { y: 40 });
  tl.from(".duo .plus", { scale: 0, duration: 0.3, ease: "back.out(2)" }, A(1.75));
  pulse("#mp", 3, 6, 0.04);
'''

c = Cues(dict(SC))
c.add("s1", 0, "hit", 0.6); c.add("s1", 0.5, "pop", 0.3); c.add("s1", 1.5, "shimmer", 0.25)
for s in ("s2", "s3", "s4", "s5", "s7"): c.add(s, 0, "swish", 0.25, -0.1)
c.add("s3", 0.25, "pop", 0.25); c.add("s3", 0.5, "whoosh", 0.4); c.add("s3", 2.6, "click", 0.3)
for i in range(4): c.add("s3", 8 + i * 0.5, "tick", 0.25)
c.add("s4", 0.5, "swish", 0.3); c.add("s4", 1.25, "pop", 0.3); c.add("s4", 7, "pop", 0.3); c.add("s4", 8.5, "hit", 0.5); c.add("s4", 8.5, "click", 0.4)
c.add("s5", 2.5, "pop", 0.3); c.add("s5", 3.5, "glitch", 0.25)
c.add("s6", 0, "whoosh", 0.45, -0.22); c.add("s6", 0.75, "swish", 0.3); c.add("s6", 2, "pop", 0.35); c.add("s6", 7.5, "click", 0.4); c.add("s6", 8, "ping", 0.45)
c.dropout("s6", 11.5, 12); c.add("s7", 0, "hit", 0.75); c.add("s7", 1, "pop", 0.3); c.add("s7", 1.75, "click", 0.3)

d = build(HF, CUES, "Southline: Van vs feed", PAL, scenes, TOTAL, CSS, JS, c, endcard="southline", keyword="seen",
          end_lines=("Electricians", "in Ireland."), end_size=128,
          comment="Ad #11 · Asphalt #161616 / Paper #F3F2EC / Electric lime #C6F432 · 'Your van vs their feed.'")
print("wrote", HF, d, "s")
