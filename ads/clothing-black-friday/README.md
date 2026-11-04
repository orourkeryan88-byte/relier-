# Southline × clothing brands: Black Friday (9:16, v3 20.7 s, no voiceover)

Made with the `videoad` skill (OpenMontage + HyperFrames); passed all 7 check gates.
**CTA keyword: FRIDAY** (end card = the owner's SA artwork with the pill re-set to Comment "friday"; set the comment
automation to "friday").

**v3 (current, 20.7 s): `southline_black_friday_v3_music.mp4` / `_v3_sfx_only.mp4`, built by `gen_composition_v3.py`
(clearkit).** Changes after reviewing v2: pain-first hook readable on frame 1 ("Your Black Friday sale is costing
you." under a CLOTHING BRANDS label), 31.5 → 20.7 s, story text and labels 2–3× bigger (FOLLOWER SINCE 2023 now
readable), lines land almost whole (no half-empty frames), bigger dashboard/field/calendar, the offer shown
mid-video ("Comment FRIDAY for a free Black Friday ad plan") and on the end card ("FOR A FREE BLACK FRIDAY AD PLAN"),
frame-0 tag sliver fixed. Not done yet: a face or real proof (needs footage from the owner).

| Beats | Time (s) | Scene | On screen |
|---|---|---|---|
| 0–5 | 0–2.2 | Hook | CLOTHING BRANDS · "Your Black Friday sale is costing you." Chrome BLACK FRIDAY tag drops and swings |
| 5–19 | 2.2–8.2 | On the day → what actually happened | "It feels like your best weekend ever." Orders race to 214 → VHS rewind → "But almost every order came from people who already follow you." Toasts flip to FOLLOWER SINCE 2023; NEW CUSTOMERS 3 |
| 19–27 | 8.2–11.6 | The cost (bone) | "You gave away €18 on every order to people who'd have paid full price anyway." €18 coin into GIVEN AWAY €3,852 |
| 27–37 | 11.6–15.9 | The fix + offer | "Here's what to change: put your drop in front of people who've never seen your brand. We run the Facebook & Instagram ads that do it." NEW CUSTOMER tags; "💬 Comment FRIDAY for a free Black Friday ad plan" |
| 37–41 | 15.9–17.7 | Urgency | "Black Friday is 27 November." 25 → 27; "Start now, not the night before." |
| 41–48 | 17.7–20.7 | End card | SA monogram, "Clothing brands.", Comment "friday", FOR A FREE BLACK FRIDAY AD PLAN |

**Caption (v3)**
> Black Friday feels like your best weekend… until you check who actually bought. 🏷️
> If most orders came from your own followers, you didn't grow. You just gave your regulars a discount.
> This year, put your drop in front of people who've never seen your brand.
> Comment "FRIDAY" for a free Black Friday ad plan 👇

---
**v2 (31.5 s): "Black Friday looks like a win. It isn't."** v1 read as if the brand's Black Friday was
working (it showed them discounting, posting and getting orders), so v2 sets up the win, rewinds it, and shows the cost
before the fix: WHAT IT LOOKS LIKE → rewind → WHAT ACTUALLY HAPPENED → the cost → January → "Here's what to change."

**Look:** Black #0A0A0A, Bone #EDE8DF, Graphite #4A4A48, accent silver chrome (gradient with a moving sheen).
Chrome swing tag motif; Fraunces (OFL), Instrument Sans/Serif, IBM Plex Mono.

| Beats | Time (s) | Scene | On screen |
|---|---|---|---|
| 0–6 | 0–2.6 | Callout | "Clothing brands." at frame 0; chrome BLACK FRIDAY tag drops and swings; "Your Black Friday sale might be costing you." |
| 6–13 | 2.6–5.6 | Open loop | "Why does Black Friday never actually grow your brand?" |
| 13–20 | 5.6–8.6 | What it looks like | Label WHAT IT LOOKS LIKE. "On the day, it feels like your best weekend ever." Dashboard: orders race 0→214, sales line climbs, NEW ORDER toasts ping, –30% tag on the panel |
| 20–29 | 8.6–12.5 | What actually happened | VHS rewind (graph runs back, freezes). Label WHAT ACTUALLY HAPPENED. "Almost every order came from people who already follow you." Toasts flip to FOLLOWER SINCE 2023; NEW CUSTOMERS counts to 3 with a thud |
| 29–38 | 12.5–16.4 | The cost (bone) | "A lot of them would have paid full price." / "So you gave away €18 on every order." €60 tag, –30% sticker, €18 coin drops into GIVEN AWAY, which counts to €3,852 |
| 38–43 | 16.4–18.5 | January | "And in January, it's quiet again." Calendar NOV→DEC→JAN, the sales line flatlines, music drops out |
| 43–47 | 18.5–20.3 | The turn | "Here's what to change." Limp tag snaps straight; music slams back in |
| 47–60 | 20.3–25.9 | The fix | "We run Facebook & Instagram ads that put your Black Friday drop in front of people who've never seen your brand." Follower ring in a field, ripples, NEW CUSTOMER tags; then "New customers you can sell to again in January." with the January line climbing |
| 60–66 | 25.9–28.4 | Urgency | "Black Friday is 27 November." Calendar 24→27 lands on the beat; "Start your ads now, not the night before." |
| 66–73 | 28.4–31.5 | End card | SA monogram + "Clothing brands." + Comment "friday" pill (types on) + FOR MORE INFO. |

All figures (214 orders, 3 new customers, €60, 30%, €18, €3,852) are illustrative. No results or guarantees on screen.

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
> Black Friday feels like a win… until you check who actually bought. 🏷️
> If it's all your followers, you just gave your regulars a discount.
> We run Facebook & Instagram ads that put your drop in front of new buyers.
> Comment "FRIDAY" for more info.
