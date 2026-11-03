#!/usr/bin/env python3
"""Find a track's tempo, beat phase and a bar-aligned loop so the edit can be locked to the beat.

    python3 beat_grid.py track.wav [--start 3.5] [--end 16] [--bars 4] [--lo 70 --hi 180]

Prints:  bpm  beat_seconds  downbeat_in_track  loop_out
and writes the same line to beat.txt next to the track. Use them like this:
    build_audio.py cues.json --music track.wav --music-in <downbeat> --music-out <loop_out>
    timeline:  const P = <beat_seconds>, B = n => +(n * P).toFixed(4);   // put every cut / word / pulse on B(n)
Video t=0 is then the downbeat. The loop is a whole number of bars, so repeats never drift.

Method: spectral-flux onset envelope (smoothed) → comb search over BPM (0.25 then 0.02 BPM steps, octave check) → phase that maximises onset energy
on the beat. "Downbeat" is the strongest beat in the first bar (kick-heavy), a good guess but check by ear or
spectrogram. --start skips any other clip at the head of a screen recording. Needs numpy + ffmpeg.
"""
import argparse, os, subprocess
import numpy as np

SR = 22050; HOP = 256


def load(path):
    raw = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", path, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).copy()


def onset_env(x):
    n = 1024; win = np.hanning(n).astype(np.float32)
    frames = np.lib.stride_tricks.sliding_window_view(x, n)[::HOP] * win
    mag = np.log1p(np.abs(np.fft.rfft(frames, axis=1)) * 10)
    flux = np.maximum(0, np.diff(mag, axis=0)).sum(axis=1)
    flux = flux - np.convolve(flux, np.ones(16) / 16, "same")       # remove slow loudness swings
    flux = np.maximum(flux, 0)
    g = np.exp(-0.5 * (np.arange(-6, 7) / 2.0) ** 2)                   # tolerate a few ms of human/sample jitter
    flux = np.convolve(flux, g / g.sum(), "same")
    return flux / (flux.max() + 1e-9)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("track"); ap.add_argument("--start", type=float, default=0.0); ap.add_argument("--end", type=float)
    ap.add_argument("--bars", type=int, default=0, help="loop length in bars (0 = as many whole bars as fit)")
    ap.add_argument("--lo", type=float, default=70); ap.add_argument("--hi", type=float, default=180)
    a = ap.parse_args()
    x = load(a.track); x = x[int(a.start * SR): int(a.end * SR) if a.end else len(x)]
    env = onset_env(x); fps = SR / HOP; t = np.arange(len(env)) / fps

    def score(bpm):
        P = 60 / bpm; best = (-1, 0.0)
        for ph in np.linspace(0, P, 96, endpoint=False):
            idx = np.round(np.arange(ph, t[-1], P) * fps).astype(int); idx = idx[idx < len(env)]
            sc = env[idx].mean()
            if sc > best[0]: best = (sc, ph)
        return best

    coarse = {b: score(b) for b in np.arange(a.lo, a.hi, 0.25)}
    bpm = max(coarse, key=lambda b: coarse[b][0])
    if bpm * 2 <= a.hi + 1 and score(bpm * 2)[0] >= 0.8 * coarse[bpm][0]:
        bpm *= 2                                                       # octave check: prefer the faster pulse
    fine = {b: score(b) for b in np.arange(bpm - 0.6, bpm + 0.6, 0.02)}
    bpm = max(fine, key=lambda b: fine[b][0]); ph = fine[bpm][1]; P = 60 / bpm
    # downbeat: strongest of the first 4 beats, measured on the low band (kicks)
    lo = np.convolve(np.abs(x), np.ones(256) / 256, "same")
    cand = [ph + k * P for k in range(4)]
    db = max(cand, key=lambda c: sum(lo[int((c + j * 4 * P) * SR)] for j in range(4) if int((c + j * 4 * P) * SR) < len(lo)))
    bar = 4 * P; avail = (len(x) / SR) - db
    nb = a.bars or int(avail // bar)
    nb = min(nb, int(avail // bar))
    din = a.start + db; dout = din + nb * bar
    line = f"{bpm:.4f} {P:.5f} {din:.4f} {dout:.4f}"
    print(f"bpm {bpm:.1f}  beat {P:.5f}s  downbeat {din:.4f}s  loop {din:.4f}–{dout:.4f}s ({nb} bars)")
    print(line)
    open(os.path.join(os.path.dirname(os.path.abspath(a.track)), "beat.txt"), "w").write(line + "\n")


if __name__ == "__main__":
    main()
