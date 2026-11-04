# Electricians in Ireland · "Your van vs their feed." (9:16, 29.3 s, no voiceover)

Made with the `videoad` skill: `clearkit.py` engine (HyperFrames + GSAP via OpenMontage), clear-story structure, every
scene and word on the 139.2 BPM grid of the owner's track. Passed all 7 check gates.
**CTA keyword: SEEN** (set the comment automation to "seen").

**Look:** Asphalt #161616 / Paper #F3F2EC / Electric lime #C6F432. Motif: the van (YOUR NAME ELECTRICAL), a street of houses, a phone feed. Southline end card.

| Beats | Time (s) | Scene | On screen |
|---|---|---|---|
| 0–6 | 0.0–2.6 | Callout | "Electricians in Ireland." + "Take a look at your van for a second." |
| 6–13 | 2.6–5.6 | Open loop | "Who actually sees your name on the van?" |
| 13–26 | 5.6–11.2 | Relate | Van drives in and parks. "Your van's parked outside a job in Lucan all day." → "Next door, the neighbours are on their phones." (windows glow) |
| 26–37 | 11.2–15.9 | Problem | "When they need an electrician, they don't go outside and check your van." → "They ask online. And they book someone else." Phone: community post asking for an electrician, another electrician's sponsored post, BOOKED |
| 37–43 | 15.9–18.5 | Sting (paper) | "If you're not in their feed, you're not on their list." Dashed empty slot: YOUR NAME ELECTRICAL · not here |
| 43–55 | 18.5–23.7 | Fix | "We run Facebook & Instagram ads that put you in their feed. Homeowners near your jobs see your work. Enquiries come straight to your phone." Your sponsored post, Get a quote, New enquiry · Kitchen rewire · Lucan |
| 55–61 | 23.7–26.3 | Payoff | "Keep the van. Add the feed." Van + phone |
| 61–68 | 26.3–29.3 | End card | Southline: S monogram, "Electricians in Ireland.", Comment "seen", FOR MORE INFO. |

Names, places, prices and counts are illustrative. No results or guarantees on screen.

**Versions**
- `southline_van_feed_music.mp4`: cut to the owner's sound ("Secondhand extended outro", prod. codax). Commercial music:
  organic posts only, not licensed for paid Meta ads.
- `southline_van_feed_sfx_only.mp4`: SFX only, for paid ads / in-app sound.

Re-build (music file lives in `../clothing-same-buyers/music/track_full.wav`, not committed; composition assets come
from the skill template plus `fr-*.woff2`):
```bash
python3 gen_composition.py composition cues.json
python3 ../../.claude/skills/videoad/scripts/build_audio.py cues.json --music ../clothing-same-buyers/music/track_full.wav --music-in 4.8271 --music-out 15.1719 -o composition/assets/audio.wav
cd composition && npx hyperframes render --quality high --output ../southline_van_feed_music.mp4
```
