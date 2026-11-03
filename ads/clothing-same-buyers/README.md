# Southline × clothing brands: "Same buyers. Every drop." (9:16, 26.7 s, no voiceover)

Made with the `videoad` skill (OpenMontage + HyperFrames); passed all 7 check gates.

**Angle:** every drop sells to the same people (your followers); boosting reaches the same crowd and your best ad
dies in a week. Southline runs Meta ads for clothing brands: new ads every week, shown to people who've never seen
you, reminders for anyone who looked but didn't buy, so the next drop reaches new people. CTA: Comment DROP.

**Hook (v2):** opens *inside* one buyer's square ("your buyer." / ONE OF 200 · DROP 01), drifting, then on the
first beat the camera rips back (flash + shake) to reveal the whole 200-square audience with only that small pink
cluster lit. The same cluster pulses on beats 4, 6, 8 as DROP 01 → 02 → 03 sell to it again.

**Beat-locked edit:** the track is 139.2 BPM (beat = 0.43103 s; `beat.txt`: bpm, beat, downbeat-in-track, loop-out).
The loop is cut on whole bars (4.8271–15.1719 s, 6 bars) and repeated exactly, so the grid never drifts. In the
timeline every scene change, caption word, pulse, flash and SFX sits on `B(n) = n × 0.43103` (beats or eighths);
cuts at beats 12, 24, 32, 48, 54; payoff hit on beat 52 after a half-beat music drop-out. 62 beats = 26.72 s.

**Palette:** Concrete #D9D8D3, Jet #111111, Graphite #5C5C5A, Fog #BEBDB8, accent Signal Pink #FF3D8B / #D81B6A.

**Versions**
- `southline_clothing_same_buyers_music.mp4`: the user's sound ("Secondhand extended outro", prod. codax, fan edit
  of Don Toliver ft. Rema), looped on bars 4.8271–15.1719 s. Commercial music: organic posts only, not licensed for paid Meta ads.
- `southline_clothing_same_buyers_sfx_only.mp4`: SFX only, for adding the sound in-app or licensed music.

Re-render (music file not committed; supply it at music/track_full.wav):
```bash
python3 ../../.claude/skills/videoad/scripts/build_audio.py cues.json --music music/track_full.wav --music-in 4.8271 --music-out 15.1719 -o composition/assets/audio.wav
cd composition && npx hyperframes render --quality high --output ../southline_clothing_same_buyers_music.mp4
```
