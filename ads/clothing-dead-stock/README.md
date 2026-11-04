# Clothing brands · "Stock you've already paid for." (9:16, 29.7 s, no voiceover)

Made with the `videoad` skill: `clearkit.py` engine (HyperFrames + GSAP via OpenMontage), clear-story structure, every
scene and word on the 139.2 BPM grid of the owner's track. Passed all 7 check gates.
**CTA keyword: STOCK** (set the comment automation to "stock").

**Look:** Ink #121417 / Stone #E7E3DB / Tangerine #FF7A1A. Motif: a clothes rail (each garment = 30 pieces), repost cards, a price tag. SA end card.

| Beats | Time (s) | Scene | On screen |
|---|---|---|---|
| 0–6 | 0.0–2.6 | Callout | "Clothing brands." + "Quick look in your stock room." |
| 6–13 | 2.6–5.6 | Open loop | "How much of your last drop is still on the rail?" |
| 13–26 | 5.6–11.2 | Relate | "You ordered 300 pieces for the drop." (rail fills, ORDERED 300) → "You sold 120 to your followers." (4 garments go, SOLD 120) → "The rest is still here." (180 LEFT · €4,500 of stock sitting here) |
| 26–37 | 11.2–15.9 | Problem | "Reposting it to the same followers gets fewer likes every time." (Still available 🔥 ♥52 → 31 → 18) → "Because they've already seen it." |
| 37–44 | 15.9–19.0 | Sting (stone) | Price tag €45 → €30 → €20, YOUR MARGIN bar shrinks. "So you discount it… and your margin disappears." |
| 44–56 | 19.0–24.1 | Fix | "We run Facebook & Instagram ads that show your stock to people who've never seen your brand." Garments ship: NEW CUSTOMER · Cork / Leeds / Dublin 8 / Belfast; ON THE RAIL 180 → 60 |
| 56–62 | 24.1–26.7 | Payoff | "Sell what you've already got. At full price." €45 ✓ FULL PRICE |
| 62–69 | 26.7–29.7 | End card | Owner's SA artwork + Comment "stock" pill + FOR MORE INFO. |

Names, places, prices and counts are illustrative. No results or guarantees on screen.

**Versions**
- `sa_dead_stock_music.mp4`: cut to the owner's sound ("Secondhand extended outro", prod. codax). Commercial music:
  organic posts only, not licensed for paid Meta ads.
- `sa_dead_stock_sfx_only.mp4`: SFX only, for paid ads / in-app sound.

Re-build (music file lives in `../clothing-same-buyers/music/track_full.wav`, not committed; composition assets come
from the skill template plus `fr-*.woff2` and `endcard.jpg`):
```bash
python3 gen_composition.py composition cues.json
python3 ../../.claude/skills/videoad/scripts/build_audio.py cues.json --music ../clothing-same-buyers/music/track_full.wav --music-in 4.8271 --music-out 15.1719 -o composition/assets/audio.wav
cd composition && npx hyperframes render --quality high --output ../sa_dead_stock_music.mp4
```
