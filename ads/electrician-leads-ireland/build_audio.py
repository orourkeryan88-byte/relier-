"""Score for 'Your own leads' (Southline Edit Style v2 §7). 124 BPM minimal bed + SFX on cue times.
Optional VO: python3 build_audio.py vo.mp3  -> music ducks 8–10 dB under speech, final mix loudnormed to -14 LUFS / -1 dBTP.
Writes hyperframes/assets/audio.wav."""
import os, subprocess, sys, tempfile, wave
import numpy as np
sys.path.insert(0, "/home/user/relier-/ads/electrician-comment-quality")
import adkit as A

D = 25.6; SR = A.SR; N = int(D * SR); BPM = 124; B = 60 / BPM
V = A._synth(); t = np.arange(N) / SR
music = np.zeros(N + SR, np.float32); sfx = np.zeros(N + SR, np.float32)
def add(buf, sig, at, g):
    s = int(at * SR); e = min(len(buf), s + len(sig))
    if e > s: buf[s:e] += sig[:e - s] * g

# ---- bed: kick on beats, offbeat hats, sub bass line, soft pad
roots = [55.0, 43.65, 65.41, 49.0]                       # A1 F1 C2 G1, one per bar
b = 0.0; i = 0
while b < D - 0.3:
    add(music, V["kick"], b, 0.42)
    add(music, V["hat"], b + B / 2, 0.38)
    if i % 2 == 0:
        f = roots[(i // 4) % 4]; n = int(B * 0.95 * SR); tt = np.arange(n) / SR
        add(music, (np.sin(2 * np.pi * f * tt) + 0.25 * np.sin(4 * np.pi * f * tt)) * np.exp(-tt * 2.2) * 0.32, b, 1.0)
    b += B; i += 1
pad = sum(np.sin(2 * np.pi * f * t) for f in (220.0, 261.63, 329.63)) * 0.012
music[:N] += pad * np.clip(t / 2, 0, 1) * np.clip((D - t) / 1.5, 0, 1)
# 250 ms drop-out before the payoff card lands (19.19–19.44)
d0, d1 = int(19.19 * SR), int(19.44 * SR); music[d0:d1] *= np.linspace(1, 0.05, d1 - d0) ** 0.5 * 0 + 0.05

# ---- SFX palette
for c in (4.3, 6.1, 9.85, 14.68, 22.5): add(sfx, V["whoosh"], c - 0.2, 0.55)      # transitions
add(sfx, V["hit"], 3.76, 0.9)                                                      # sub-thump on "now"
add(sfx, V["hit"], 0.24, 0.6)
word_times = [0.24, 1.2, 1.6, 1.92, 2.24, 3.44, 3.76, 4.32, 4.48, 4.6, 4.72, 4.88, 5.12, 5.28, 6.16, 6.4, 6.56, 6.68, 6.8, 7.36, 7.6, 7.84,
              8.04, 8.16, 8.32, 8.64, 8.84, 8.92, 9.28, 10.0, 10.12, 10.24, 10.4, 11.04, 11.6, 12.24, 13.12, 13.28, 13.44, 13.76, 13.96, 14.16,
              15.0, 15.44, 15.68, 16.0, 16.16, 16.44, 17.04, 17.2, 17.36, 18.08, 18.4, 18.64, 18.84, 19.44, 20.24, 20.4, 20.64, 21.28, 21.56, 21.8, 22.56, 22.8]
for w in word_times: add(sfx, V["tick"], w, 0.07)                                 # faint ticks on word reveals
for c in (6.8, 11.04, 11.6, 12.24, 15.44, 16.0): add(sfx, V["pop"], c, 0.35)
for k in range(5): add(sfx, V["swish"], 7.36 + k * 0.07, 0.18)
for c in (18.08, 18.4, 18.64): add(sfx, V["click"], c, 0.5)
add(sfx, V["hit"], 19.44, 0.85); add(sfx, V["coin"], 19.46, 0.35)                 # card lands after the drop-out
rn = np.random.default_rng(5).standard_normal(int(0.6 * SR)).astype(np.float32); rt = np.linspace(0, 1, len(rn))
riser = np.convolve(rn, np.ones(30) / 30, "same") * rt ** 2 * 0.5
add(sfx, riser, 21.9, 0.6)                                                         # riser into end card
for k in range(5): add(sfx, V["tick"], 23.0 + k * 0.09, 0.3)                       # typing LEADS
add(sfx, V["click"], 23.6, 0.6); add(sfx, V["hit"], 22.8, 0.8); add(sfx, V["shimmer"], 22.82, 0.4)

# ---- optional VO + ducking
vo = np.zeros(N + SR, np.float32)
if len(sys.argv) > 1:
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", sys.argv[1], "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
    v = np.frombuffer(raw, np.float32); vo[:min(len(v), len(vo))] = v[:len(vo)]
    env = np.sqrt(np.convolve(vo ** 2, np.ones(int(0.03 * SR)) / int(0.03 * SR), "same"))
    talk = (env > 0.02).astype(np.float32)
    # 20 ms attack, 150 ms release
    g = np.zeros_like(talk); a_c, r_c = np.exp(-1 / (0.02 * SR)), np.exp(-1 / (0.15 * SR)); prev = 0.0
    for k in range(len(talk)):
        c = a_c if talk[k] > prev else r_c; prev = c * prev + (1 - c) * talk[k]; g[k] = prev
    music *= 10 ** (-9 * g / 20)
mix = (music + sfx * 0.9 + vo * 1.0)[:N]
mix = np.tanh(mix * 1.1) / np.tanh(1.1)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "composition", "assets", "audio.wav")
tmp = tempfile.mktemp(suffix=".wav")
with wave.open(tmp, "wb") as wf:
    wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(SR); wf.writeframes((np.clip(mix / max(1e-6, np.abs(mix).max()) * 0.9, -1, 1) * 32767).astype(np.int16).tobytes())
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", tmp, "-af", "loudnorm=I=-14:TP=-1:LRA=9", "-ar", str(SR), "-ac", "2", out], check=True)
print("wrote", out, "| VO:", "yes" if len(sys.argv) > 1 else "no (bed + SFX only)")
