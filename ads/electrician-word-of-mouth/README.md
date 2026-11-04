# Electricians in Ireland · "You can't turn word of mouth up." (9:16, 29.3 s, no voiceover)

Made with the `videoad` skill: `clearkit.py` engine (HyperFrames + GSAP via OpenMontage), clear-story structure, every
scene and word on the 139.2 BPM grid of the owner's track. Passed all 7 check gates.
**CTA keyword: BUSY** (set the comment automation to "busy").

**Look:** Slate #1C2127 / Chalk #F1EEE8 / Copper #E08A4E. Motif: copper wire between houses, two dials (WORD OF MOUTH vs YOUR ADS). Southline end card.

| Beats | Time (s) | Scene | On screen |
|---|---|---|---|
| 0–6 | 0.0–2.6 | Callout | "Electricians in Ireland." A copper wire draws across. "This one's for you." |
| 6–13 | 2.6–5.6 | Open loop | "Where's your next month of work coming from?" |
| 13–26 | 5.6–11.2 | Relate | "Right now, most of your work comes from word of mouth." → "One good job leads to the next." Copper wire runs house to house (Naas → Newbridge → Kildare) with "Ring this lad" chips |
| 26–36 | 11.2–15.5 | Problem | "But you can't control when people mention you." → "Some weeks are packed. Some weeks are dead quiet." This week fills with JOB, next week stays empty, QUIET stamp |
| 36–43 | 15.5–18.5 | Sting (chalk) | Dial labelled WORD OF MOUTH tries to rise and springs back. "And you can't turn word of mouth up when it's quiet." |
| 43–55 | 18.5–23.7 | Fix | "We run Facebook & Instagram ads for your business. Homeowners near you see your work. Enquiries come straight to your phone." YOUR ADS dial turns up; three enquiries land on a phone |
| 55–61 | 23.7–26.3 | Payoff | "Keep the referrals. Stop relying on them." Both weeks fill with JOB |
| 61–68 | 26.3–29.3 | End card | Southline: S monogram, "Electricians in Ireland.", Comment "busy", FOR MORE INFO. |

Names, places, prices and counts are illustrative. No results or guarantees on screen.

**Versions**
- `southline_word_of_mouth_music.mp4`: cut to the owner's sound ("Secondhand extended outro", prod. codax). Commercial music:
  organic posts only, not licensed for paid Meta ads.
- `southline_word_of_mouth_sfx_only.mp4`: SFX only, for paid ads / in-app sound.

Re-build (music file lives in `../clothing-same-buyers/music/track_full.wav`, not committed; composition assets come
from the skill template plus `fr-*.woff2`):
```bash
python3 gen_composition.py composition cues.json
python3 ../../.claude/skills/videoad/scripts/build_audio.py cues.json --music ../clothing-same-buyers/music/track_full.wav --music-in 4.8271 --music-out 15.1719 -o composition/assets/audio.wav
cd composition && npx hyperframes render --quality high --output ../southline_word_of_mouth_music.mp4
```
