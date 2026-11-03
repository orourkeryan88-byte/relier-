# Southline × clothing brands: "Why does every drop sell to the same people?" (9:16, 24.1 s, no voiceover)

Made with the `videoad` skill (OpenMontage + HyperFrames); passed all 7 check gates.
**CTA keyword: SCALE** (from the owner's end-card artwork; set the comment automation to "scale").

**v7 (current): clear cut.** v4–v6 had 16 ideas in 17–21 s and the owner said it was too fast to process and didn't
make sense. v7 tells one story in full sentences across 7 scenes, each held 2–4 s, still on the 139.2 BPM grid
(56 beats = 14 bars). People are drawn as person icons with a legend, so the crowd metaphor explains itself.

| Beats | Time (s) | Scene | On screen |
|---|---|---|---|
| 0–4 | 0–1.7 | Callout | "Clothing brands." (Fraunces, white/pink) + arc, then "quick question…" |
| 4–12 | 1.7–5.2 | Open loop | "Why does every drop sell to the same people?" |
| 12–24 | 5.2–10.3 | Relate | One post that grows: "You post the drop." (post) → "Your followers like it." (41 likes, AM/JK/RB) → "The same few people buy." (orders from AM and JK: "bought your last drop too") |
| 24–32 | 10.3–13.8 | Problem | "Because only your followers ever see it." Crowd of people, followers in pink; legend: YOUR FOLLOWERS / EVERYONE ELSE · NEVER SEEN YOUR BRAND |
| 32–42 | 13.8–18.1 | Solution | "We run Facebook & Instagram ads" / "that show your drop to new buyers." New people light up outward; legend: NEW BUYERS, FROM YOUR ADS |
| 42–48 | 18.1–20.7 | Payoff | "So your next drop sells to new people." Whole crowd lit after a half-beat drop-out |
| 48–56 | 20.7–24.1 | End card | Owner's artwork (`composition/assets/endcard.jpg`): SA monogram, "Clothing brands.", Comment "scale", FOR MORE INFO. |

Names, likes and orders are illustrative.

**Versions**
- `southline_clothing_same_buyers_music.mp4`: the user's sound ("Secondhand extended outro", prod. codax, fan edit
  of Don Toliver ft. Rema), looped on bars 4.8271–15.1719 s. Commercial music: organic posts only, not licensed for
  paid Meta ads.
- `southline_clothing_same_buyers_sfx_only.mp4`: SFX only, for adding the sound in-app or licensed music.

Re-build (music file not committed; supply it at music/track_full.wav):
```bash
python3 gen_composition.py composition cues.json
python3 ../../.claude/skills/videoad/scripts/build_audio.py cues.json --music music/track_full.wav --music-in 4.8271 --music-out 15.1719 -o composition/assets/audio.wav
cd composition && npx hyperframes render --quality high --output ../southline_clothing_same_buyers_music.mp4
```

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
