# Clothing brands · "Don't launch to an empty room." (9:16, 29.7 s, no voiceover)

Made with the `videoad` skill: `clearkit.py` engine (HyperFrames + GSAP via OpenMontage), clear-story structure, every
scene and word on the 139.2 BPM grid of the owner's track. Passed all 7 check gates.
**CTA keyword: LAUNCH** (set the comment automation to "launch").

**Look:** Charcoal #141414 / Cream #F3EEE4 / Amber #FFB020. Motif: design → samples → shoot progress, a launch post, a spotlit stage and seats. SA end card.

| Beats | Time (s) | Scene | On screen |
|---|---|---|---|
| 0–6 | 0.0–2.6 | Callout | "Clothing brands." + "Got a launch coming up?" |
| 6–13 | 2.6–5.6 | Open loop | "Why does launch day feel so quiet after months of work?" |
| 13–27 | 5.6–11.6 | Relate | "Months designing it." → "Weeks waiting on samples." → "A full day shooting it." (progress fills) → "Then you post it." (launch post, LIVE) |
| 27–38 | 11.6–16.4 | Problem | "You launch to a half-empty room." (spotlit stage, a few seats lit: THE SAME FEW FOLLOWERS SHOW UP) → "Most people who'd love it never even see it." |
| 38–44 | 16.4–19.0 | Sting (cream) | "Months of work. Seen by the same few people." |
| 44–56 | 19.0–24.1 | Fix | "We run Facebook & Instagram ads for your launch. Build the buzz before it drops. Fill the room on the day." Seats fill row by row: NEW PEOPLE, FROM YOUR ADS |
| 56–62 | 24.1–26.7 | Payoff | "Launch to a full room." |
| 62–69 | 26.7–29.7 | End card | Owner's SA artwork + Comment "launch" pill + FOR MORE INFO. |

Names, places, prices and counts are illustrative. No results or guarantees on screen.

**Versions**
- `sa_launch_day_music.mp4`: cut to the owner's sound ("Secondhand extended outro", prod. codax). Commercial music:
  organic posts only, not licensed for paid Meta ads.
- `sa_launch_day_sfx_only.mp4`: SFX only, for paid ads / in-app sound.

Re-build (music file lives in `../clothing-same-buyers/music/track_full.wav`, not committed; composition assets come
from the skill template plus `fr-*.woff2` and `endcard.jpg`):
```bash
python3 gen_composition.py composition cues.json
python3 ../../.claude/skills/videoad/scripts/build_audio.py cues.json --music ../clothing-same-buyers/music/track_full.wav --music-in 4.8271 --music-out 15.1719 -o composition/assets/audio.wav
cd composition && npx hyperframes render --quality high --output ../sa_launch_day_music.mp4
```
