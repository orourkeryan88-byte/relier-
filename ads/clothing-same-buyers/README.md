# Southline × clothing brands: "Clothing brands." fast cut (9:16, 17.2 s, no voiceover)

Made with the `videoad` skill (OpenMontage + HyperFrames); passed all 7 check gates.

**v4 (current): reference pacing.** Opens on the callout, then the open loop, then the rest, with a new frame every
2 beats (0.86 s) like the reference reels in `References/`: 2–5 big centred words per frame, words landing on the beat,
hard cuts on the beat, two line wipes, two whips. 40 beats at 139.2 BPM = 17.24 s; the end card repeats the opening
callout so the reel loops.

| Beats | Time (s) | Frame |
|---|---|---|
| 0–2 | 0–0.86 | CALLOUT: "Clothing brands." (Fraunces, white/pink), "brands." slams on beat ½, arc + flash on beat 1 |
| 2–6 | 0.86–2.59 | OPEN LOOP: "why does every drop / sell to the same people?" |
| 6–8 | 2.59–3.45 | "every. single. drop." Buyer grid, same cluster lit on DROP 01/02/03 |
| 8–16 | 3.45–6.90 | RELATE: "you post the new drop." / "story. reel. post." / "and you get the same likes." / "and the orders? same faces." |
| 16–22 | 6.90–9.48 | PROBLEM: "it's not the clothes." / "it's who sees them." / "boost it? same crowd." |
| 22–31 | 9.48–13.36 | SOLUTION: "here's what we do. Southline" (Facebook + Instagram ads for clothing brands) / "new ads every week." / "shown to new buyers." / "+ reminders for anyone who looked." |
| 31–34 | 13.36–14.66 | PAYOFF: "so your next drop reaches new people." Grid goes all pink on beat 32 after a half-beat drop-out |
| 34–40 | 14.66–17.24 | CTA end card: S monogram + arc, "Clothing brands.", Comment "DROP" pill, FOR MORE INFO. |

`gen_composition.py` generates `composition/index.html` and `cues.json` from that beat table:
```bash
python3 gen_composition.py composition cues.json
```

---
## Earlier version (v2/v3, 26.7 s)

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

**End card (v3):** monogram layout after the user's reference: serif "S" with a pink arc (South-*line*), small
"SOUTHLINE · FACEBOOK + INSTAGRAM ADS", big Fraunces "Clothing / brands." (white / pink), an outlined pill with a
comment icon and Comment "DROP", then "FOR MORE INFO." Built on beats 54–62: S lands 54, arc 54.5, title 55.5/56
(hit + flash), pill draws 57, DROP types 58–58.75, sign-off 59.5, pill pulses 60–61. Fraunces is SIL OFL
(`composition/assets/fonts/Fraunces-OFL.txt`).

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
