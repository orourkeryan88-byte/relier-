"""Mix the ad's sound: synthesized SFX at the times the Theatre timeline emitted, over a 120bpm beat bed.
usage: python3 mix_audio.py sfx.json out.wav"""
import json, os, sys, wave
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "electrician-comment-quality"))
import adkit as A   # reuse the synth voices (ping, pop, click, tick, coin, whoosh, swish, hit, shimmer, glitch, kick, hat)

spec = json.load(open(sys.argv[1])); total = spec["duration"]; SR = A.SR
N = int(total * SR); mix = np.zeros(N + SR, np.float32); S = A._synth()
def add(sig, at, g):
    s = int(at * SR); e = min(len(mix), s + len(sig))
    if e > s: mix[s:e] += sig[:e - s] * g
beat = 60 / 120; b = 0.0
while b < total - 0.2:
    if b >= 0.45: add(S["kick"], b, 0.32)
    add(S["hat"], b + beat / 2, 0.5); b += beat
pt = np.arange(len(mix)) / SR
mix += (np.sin(2 * np.pi * 55 * pt) + 0.5 * np.sin(2 * np.pi * 82.4 * pt)) * 0.05 * np.minimum(pt, 1) * np.clip((total - pt) / 0.8, 0, 1)
for at, k, g in spec["events"]: add(S[k], at, g)
mix = mix[:N]; mix = np.tanh(mix * 1.2) / np.tanh(1.2); mix /= max(1e-6, np.abs(mix).max()) / 0.89
with wave.open(sys.argv[2], "wb") as wf:
    wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes((mix * 32767).astype(np.int16).tobytes())
