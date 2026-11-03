"""Score for the 'work this week' ad: synthesized SFX on the composition's cue times + a 120bpm beat bed.
Writes hyperframes/assets/audio.wav. Cue times mirror the GSAP timeline in hyperframes/index.html."""
import os, sys, wave
import numpy as np
sys.path.insert(0, "/home/user/relier-/ads/electrician-comment-quality")
import adkit as A

D = 22.9; SR = A.SR
S = dict(s1=0.0, s2=2.95, s3=7.5, s4=12.9, s5=17.9)
ev = []
e = lambda t, k, g=0.6: ev.append((t, k, g))
# S1 hook slams
e(0.05, "pop", 0.7); e(0.15, "hit", 0.9); e(0.42, "hit", 0.8); e(0.72, "hit", 1.0); e(0.74, "glitch", 0.35); e(1.12, "swish", 0.6)
# transitions (sheet covers)
for c in (S["s2"], S["s3"], S["s4"], S["s5"]): e(c - 0.4, "whoosh", 0.6)
# S2 the dip
T = S["s2"]; e(T + 0.25, "hit", 0.7); e(T + 0.4, "hit", 0.7)
for i in range(6): e(T + 0.6 + i * 0.06, "tick", 0.35)
e(T + 0.8, "swish", 0.4); e(T + 1.3, "pop", 0.6); e(T + 1.8, "whoosh", 0.4); e(T + 2.38, "hit", 0.9); e(T + 2.5, "pop", 0.8); e(T + 2.75, "hit", 0.8)
# S3 the catch
T = S["s3"]; e(T + 0.1, "hit", 0.8); e(T + 0.35, "swish", 0.5)
for i, v in enumerate([0.75, 1.65, 2.55, 3.45]):
    if i: e(T + v - 0.45, "swish", 0.45)
    e(T + v, "pop", 0.7)
e(T + 4.0, "shimmer", 0.6); e(T + 4.3, "hit", 0.8)
# S4 the month fills
T = S["s4"]; e(T + 0.1, "hit", 0.8); e(T + 0.28, "hit", 0.7); e(T + 0.55, "whoosh", 0.5)
for i in range(18): e(T + 1.25 + i * 0.1, "pop" if i % 2 else "tick", 0.35)
e(T + 3.15, "coin", 0.6); e(T + 3.59, "hit", 1.0); e(T + 3.6, "glitch", 0.4)
# S5 CTA
T = S["s5"]; e(T + 0.1, "swish", 0.5); e(T + 0.3, "hit", 0.8); e(T + 0.55, "swish", 0.5)
for i in range(4): e(T + 0.7 + i * 0.05, "tick", 0.4)
e(T + 1.0, "whoosh", 0.4)
for i in range(4): e(T + 1.5 + i * 0.09, "tick", 0.5)
e(T + 2.45, "ping", 0.7); e(T + 2.47, "pop", 0.5)

N = int(D * SR); mix = np.zeros(N + SR, np.float32); V = A._synth()
def add(sig, at, g):
    s = int(at * SR); t = min(len(mix), s + len(sig))
    if t > s: mix[s:t] += sig[:t - s] * g
b = 0.0
while b < D - 0.2:
    if b >= 0.45: add(V["kick"], b, 0.34)
    add(V["hat"], b + 0.25, 0.5); b += 0.5
pt = np.arange(len(mix)) / SR
mix += (np.sin(2 * np.pi * 55 * pt) + 0.5 * np.sin(2 * np.pi * 82.4 * pt)) * 0.05 * np.minimum(pt, 1) * np.clip((D - pt) / 0.8, 0, 1)
for t, k, g in ev: add(V[k], t, g)
mix = mix[:N]; mix = np.tanh(mix * 1.2) / np.tanh(1.2); mix /= max(1e-6, np.abs(mix).max()) / 0.89
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "composition", "assets", "audio.wav")
with wave.open(out, "wb") as wf:
    wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes((mix * 32767).astype(np.int16).tobytes())
print("wrote", out, len(ev), "cues")
