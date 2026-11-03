# Southline × Electricians: "Own the switch" ad (9:16, 23.3s)

Built with [OpenMontage](https://github.com/calesthio/OpenMontage) (animation pipeline) on the HyperFrames
runtime: hand-authored HTML + GSAP (with MotionPath) composition. It passed OpenMontage `hyperframes_compose`
`check` (lint, runtime, layout, motion, contrast, craft, audio) and was rendered with `render_existing`.

**Angle:** control and dependence. Most electricians run on someone else's power (the builder, word of
mouth, old customers, luck). Southline adds their own circuit.

**Theme:** midnight navy, electric cyan, LED green and trip red. Space Grotesk + JetBrains Mono.

## Script
1. **Hook:** a bulb swings in. "Electricians. Who controls your work?" The bulb flickers and the power cuts.
2. **Problem:** "Most sparks run on someone else's power." Fuse board breakers labelled The Builder, Word of
   Mouth, Old Customers and Luck trip one by one ("Builder goes quiet." / "Referrals dry up." / "Old customers are sorted." / "Luck runs out.")
   as the screen dims. "A quiet month you didn't choose."
3. **Insight:** "You're not short on ~~skill.~~ control." "Every job still comes through someone else's door."
4. **Solution:** "Add your own circuit." A new breaker, "Your own leads", slots into the spare slot and flips ON.
   Leads run down the wire: rewire, EV charger and fuse board, each marked CHECKED.
5. **CTA:** "Take back the switch." A wall switch flips on. "Comment SWITCH". Typed comment, then "We'll DM you how it works."

## Rebuild
```bash
python3 build_audio.py                        # score -> composition/assets/audio.wav
cd composition && npx hyperframes render --quality high --output ../out.mp4
```
