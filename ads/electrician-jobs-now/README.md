# Southline × Electricians: "work this week" ad (9:16, 22.9s)

Built with [OpenMontage](https://github.com/calesthio/OpenMontage) (animation pipeline) on the
HyperFrames runtime: a hand-authored HTML + GSAP composition, gated by OpenMontage's
`hyperframes_compose` tool (`check` passes lint, runtime, layout, motion, contrast, craft and audio),
then rendered with `render_existing`.

## Script
1. **Hook**: "For electricians. Someone near you needs a spark this week. Are they calling you?"
2. **Problem**: "It's the pre-Christmas rush. Done before Christmas." Demand chart with "You are here" and "Peak demand: now". "Who are they calling?"
3. **How fast?**: "Days, not months." Day 1 ads go live, day 2 enquiries land (pre-qualified), day 3 you quote, this week jobs booked. "Start this week… booked by Christmas."
4. **Solution**: "We run your Meta ads now. Filtered leads for big jobs, starting this week." The November calendar fills, then the BOOKED stamp.
5. **CTA**: "Want more work this month? Comment JOBS." The comment is typed, Southline replies "Sent you a DM with how it works."

## Rebuild
```bash
python3 build_audio.py                     # score -> composition/assets/audio.wav
# from an OpenMontage checkout, with this folder's composition/ as projects/<name>/hyperframes:
.venv/bin/python -c "from tools.video.hyperframes_compose import HyperFramesCompose as H; print(H().execute({'operation':'render_existing','workspace_path':'projects/<name>/hyperframes','output_path':'out.mp4','quality':'high'}).success)"
```
Or directly: `cd composition && npx hyperframes render --quality high --output ../out.mp4`
