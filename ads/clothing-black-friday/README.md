# Southline × clothing brands: Black Friday (9:16, 26.7 s, no voiceover)

Made with the `videoad` skill (OpenMontage + HyperFrames); passed all 7 check gates.
**CTA keyword: FRIDAY** (end card = the owner's SA artwork with the pill re-set to Comment "friday"; set the comment
automation to "friday").

**Angle:** "Your Black Friday sale is a discount for people who'd have paid full price anyway." The sale goes to the
brand's own followers, so it rewards regulars instead of winning new customers. Southline runs Facebook & Instagram
ads that put the Black Friday drop in front of new buyers. Urgency: Black Friday is Fri 27 Nov 2026.

**Look:** Black #0A0A0A, Bone #EDE8DF, Graphite #4A4A48, accent silver chrome (gradient with a moving sheen).
Recurring motif: a chrome swing tag on a string. Fraunces (OFL) for statements, Instrument Sans/Serif, IBM Plex Mono.

| Beats | Time (s) | Scene | On screen |
|---|---|---|---|
| 0–5 | 0–2.2 | Callout | "Clothing brands." at frame 0; chrome BLACK FRIDAY tag drops and swings; "Black Friday's coming." |
| 5–13 | 2.2–5.6 | Open loop | "Who's actually buying your Black Friday sale?" |
| 13–25 | 5.6–10.8 | Relate | One tag: "You knock 30% off." (€60 struck, €42, –30% sticker) → "You post it. You email your list." (story, email) → "The orders come in…" (receipt printer: three orders, each stamped FOLLOWER SINCE 2023) |
| 25–33 | 10.8–14.2 | Problem | "…from people who already follow you." / "A lot of them would have paid full price." Follower ring inside a field of people who've never seen you; the –30% sticker slaps onto the ring |
| 33–39 | 14.2–16.8 | Sting | Bone: "You didn't get new customers. You gave your regulars a discount." Tag flips to DISCOUNT FOR REGULARS |
| 39–49 | 16.8–21.1 | Solution | "We run Facebook & Instagram ads that put your Black Friday drop in front of new buyers." Ripples out of the ring, field lights up, four NEW CUSTOMER chrome tags |
| 49–54 | 21.1–23.3 | Urgency | "Black Friday is 27 November." Chrome calendar flips 23→27 on the beat after a drop-out; "Start your ads now, not the night before." |
| 54–62 | 23.3–26.7 | End card | SA monogram + "Clothing brands." + Comment "friday" pill (types on) + FOR MORE INFO. |

Names, prices and the 30% are illustrative. No results or guarantees on screen.

**Versions**
- `southline_black_friday_music.mp4`: cut to the owner's sound ("Secondhand extended outro", prod. codax), 139.2 BPM,
  looped on bars 4.8271–15.1719 s. Commercial music: organic posts only, not licensed for paid Meta ads.
- `southline_black_friday_sfx_only.mp4`: SFX only, for paid ads / in-app sound.

Re-build (music file lives in `../clothing-same-buyers/music/track_full.wav`, not committed):
```bash
python3 gen_composition.py composition cues.json
python3 ../../.claude/skills/videoad/scripts/build_audio.py cues.json --music ../clothing-same-buyers/music/track_full.wav --music-in 4.8271 --music-out 15.1719 -o composition/assets/audio.wav
cd composition && npx hyperframes render --quality high --output ../southline_black_friday_music.mp4
```

**Caption**
> Your Black Friday sale shouldn't just be a discount for people who already follow you. 🏷️
> We run Facebook & Instagram ads that put your drop in front of new buyers.
> Comment "FRIDAY" for more info.
