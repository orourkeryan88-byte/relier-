# Southline × clothing brands: "Same buyers. Every drop." (9:16, 26.5 s, no voiceover)

Made with the `videoad` skill (OpenMontage + HyperFrames); passed all 7 check gates.

**Angle:** every drop sells to the same people (your followers); boosting reaches the same crowd and your best ad
dies in a week. Southline runs Meta ads for clothing brands: new ads every week, shown to people who've never seen
you, reminders for anyone who looked but didn't buy, so the next drop reaches new people. CTA: Comment DROP.

**Palette:** Concrete #D9D8D3, Jet #111111, Graphite #5C5C5A, Fog #BEBDB8, accent Signal Pink #FF3D8B / #D81B6A.

**Versions**
- `southline_clothing_same_buyers_music.mp4`: the user's sound ("Secondhand extended outro", prod. codax, fan edit
  of Don Toliver ft. Rema), looped 3.6–15.95 s. Commercial music: organic posts only, not licensed for paid Meta ads.
- `southline_clothing_same_buyers_sfx_only.mp4`: SFX only, for adding the sound in-app or licensed music.

Re-render (music file not committed; supply it at music/track_full.wav):
```bash
python3 ../../.claude/skills/videoad/scripts/build_audio.py cues.json --music music/track_full.wav --music-in 3.6 --music-out 15.95 -o composition/assets/audio.wav
cd composition && npx hyperframes render --quality high --output ../southline_clothing_same_buyers_music.mp4
```
