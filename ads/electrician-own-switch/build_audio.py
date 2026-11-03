"""Score for the 'own the switch' ad: synthesized SFX on the composition's cue times + a 120bpm beat bed.
Writes hyperframes/assets/audio.wav. Cue times mirror the GSAP timeline in hyperframes/index.html."""
import os, sys, wave
import numpy as np
sys.path.insert(0, "/home/user/relier-/ads/electrician-comment-quality")
import adkit as A

D = 23.3; SR = A.SR
S = dict(s1=0.0, s2=2.8, s3=8.4, s4=12.0, s5=18.3)
ev = []
e = lambda t, k, g=0.6: ev.append((t, k, g))
# S1 bulb swings in, title, flicker + power cut
e(0.0, "whoosh", 0.5); e(0.2, "pop", 0.5); e(0.35, "swish", 0.4); e(0.7, "hit", 0.9); e(1.2, "swish", 0.5)
e(2.25, "glitch", 0.6); e(2.5, "glitch", 0.5); e(2.72, "hit", 0.8)
# S2 power back, board, four trips
T = S["s2"]; e(T + 0.02, "glitch", 0.4); e(T + 0.3, "swish", 0.4); e(T + 0.8, "whoosh", 0.5)
for i in range(4): e(T + 1.25 + i * 0.08, "tick", 0.4)
for tt in (2.0, 2.65, 3.3, 3.95): e(T + tt + 0.1, "click", 1.0); e(T + tt + 0.12, "hit", 0.7); e(T + tt + 0.13, "glitch", 0.3)
e(T + 4.55, "swish", 0.5)
# S2 -> S3 surge scanline
e(S["s3"] - 0.3, "whoosh", 0.6); e(S["s3"] - 0.05, "shimmer", 0.4)
# S3 skill -> control
T = S["s3"]; e(T + 0.15, "swish", 0.4); e(T + 0.45, "hit", 0.8); e(T + 1.15, "swish", 0.6); e(T + 1.7, "whoosh", 0.5); e(T + 2.2, "hit", 0.9)
e(S["s4"] - 0.32, "whoosh", 0.6)
# S4 new circuit installed + ON, leads flow
T = S["s4"]; e(T + 0.15, "hit", 0.7); e(T + 0.6, "swish", 0.4); e(T + 1.2, "whoosh", 0.6); e(T + 1.75, "hit", 0.9); e(T + 1.9, "pop", 0.7)
ON = T + 2.35; e(ON + 0.08, "click", 1.0); e(ON + 0.1, "shimmer", 0.8); e(ON + 0.1, "hit", 0.6); e(ON + 0.3, "swish", 0.4)
for i in range(3): e(ON + 0.75 + i * 0.62, "swish", 0.35); e(ON + 1.17 + i * 0.62, "ping", 0.7)
# S4 -> S5 power cut, switch flip
e(S["s5"] - 0.32, "glitch", 0.6)
T = S["s5"]; F = T + 0.75; e(F, "click", 1.0); e(F + 0.08, "shimmer", 0.8); e(F + 0.08, "hit", 0.7)
e(F + 0.12, "swish", 0.4); e(F + 0.72, "pop", 0.8)
for i in range(6): e(F + 1.35 + i * 0.09, "tick", 0.5)
e(F + 2.05, "click", 0.8); e(F + 2.15, "ping", 0.7)

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
