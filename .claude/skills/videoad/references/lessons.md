# Lessons already paid for

## Cloud session network (claude.ai/code containers)
Blocked by policy in this environment so far (CONNECT 403 / ENOTFOUND): `www.youtube.com`, `*.googlevideo.com`,
`www.instagram.com`, `archive.org`, `huggingface.co` (Whisper models), `elevenlabsusercontent.com` (ElevenLabs
downloads), assorted blogs. Allowed: GitHub, npm, PyPI.
- On a block: stop, name the host, keep working on what doesn't need it. Don't route around it via other services.
- Fix for the user: environment menu (session title bar) → Edit → Network access → add the host under Allowed domains
  (docs: https://code.claude.com/docs/en/cloud-environments#network-access). Or they upload the file in chat.
- Reference reels: the user can send screen recordings; save them to `References/`, crop out app UI when analysing.
- Starting a local web server (`python -m http.server`) was refused by the permission classifier; don't.
- The user's own computer isn't reachable unless they connect it (Claude Desktop app or `claude remote-control`).

## ElevenLabs MCP
- Speech ~17¢/take (eleven_v4), images ~7¢ each (gpt-image-2.5-sunburst, 4 per call by default), transcription free.
- Image models default to 16:9 even if the prompt says 9:16; set the aspect in the node or skip photos.
- Transcripts include the `[direction tag]` as zero-length words at t≈0; skip them.

## HyperFrames / OpenMontage gotchas
- `querySelectorAll` with a template literal (`` `${sel} .w` ``) is a **lint error** (bundler CSS parser crash). Use
  string concatenation. Template literals inside `tl.set()`/`tl.to()` selectors are fine.
- Elements that start hidden then become visible need an explicit `tl.set(el, {opacity:1}, t)`; a `fromTo` with
  opacity only in the from-vars fails the cold-seek lint (`gsap_cold_seek_hidden_fromto_missing_reveal`).
- Full-frame overlays (background, haze, grain, dim, flash, wipes, ghost words, decorative SVG) need
  `data-layout-ignore`, or the layout audit reports "text occluded" / "canvas covered".
- An intentional overlap (stamp over a calendar, caption stack) also needs `data-layout-ignore` on the decorative one.
- Every `font-family` needs an `@font-face`; a fallback like `Impact` is a lint error. Generic `sans-serif`/`monospace`
  are fine. Load fonts and GSAP from local `assets/`, never a CDN at render time.
- Don't animate `letterSpacing`, `display` or `visibility`; animate transforms and opacity. Stroke-dash draws are fine.
- Fast tweens on the same property of the same element fight; put camera drift on `.cam` and punch-ins on the caption.
- `nested_structure_needs_subcomposition` and `timeline_track_too_dense` warnings are fine for single-file ads.
- `npx hyperframes` inside a folder whose `package.json` is named `hyperframes` runs the wrong thing; never `npm init`
  inside the composition folder.
- Render through OpenMontage: `HyperFramesCompose().execute({"operation": "render_existing", ...})` runs the check
  then renders at high quality (~2 min for 25 s). `check` must pass with 0 errors in lint, runtime, layout, motion,
  contrast, craft and audio.
- GSAP `fromTo` renders its from-values immediately at creation (`immediateRender`), so a later `fromTo` on the same
  property overwrites earlier states at seek time (flashes stuck on, rings visible at t=0, scale jumps). For repeated
  hits on one element use `tl.set(el, from, t)` + `tl.to(el, to, t)` or a single `.to` with `keyframes`.
- Snapshots land in `.hyperframes/artifacts/snapshots/<id>/` with a `contact-sheet*.jpg`; Read it.

## Beat-locked edits (ad #8 v2)
- `scripts/beat_grid.py track.wav --start <skip> --bars N` gives bpm, beat length, a downbeat and a bar-aligned loop.
  It can be off by a fraction of a BPM or pick a downbeat two beats out: confirm on a spectrogram/onset plot (the
  hats should sit on the grid lines) before building. Ad #8's verified grid: 139.2 BPM, P = 0.43103 s, downbeat
  4.8271 s, 6-bar loop to 15.1719 s.
- The old music loop overlapped repeats by the crossfade length, so the beat drifted ~80 ms per loop. `build_audio.py`
  now advances exactly one loop each repeat; keep `--music-in/--music-out` on whole bars.
- In the timeline: `const P = <beat>, B = n => +(n * P).toFixed(4)`. Put every scene start, caption word (beats or
  eighths), pulse, flash and cue on `B(n)`; set clip `data-start`/`data-duration` and the root duration to `B(n)` too.
  Total length = whole bars (ad #8: 62 beats = 26.72 s).
- Hook pattern that works: frame 1 is already full-bleed accent colour + big type, drifting; on beat 1 a fast
  `expo.out` pull-back (~0.6 s) reveals the context, with a white flash (0.7 → 0) and a small shake. Things that
  repeat (drops, waves) pulse on the beat, not on a reading pace.

## Reference pacing (measured from References/, ad #8 v4)
- The three reference reels are 12 s long and change frame about every 1–1.5 s, morphing or cutting; each frame
  holds one idea in 2–4 big centred words, built word by word. Our 26 s cuts with 3.5–9.5 s scenes felt slow next to them.
- Pattern that matches: 2-beat frames (≈0.86 s at 139 BPM), 3–4 beats for the open loop, the brand line and the
  payoff; all words of a frame land in the first beat; every shot lands punched in (1.07 → 1 in 0.3 s) then creeps.
- (Superseded by "Clarity beats speed" below.) The user then asked to "slow it down slightly": 3-beat frames (≈1.3 s) for anything with a graphic or 4+ words,
  2 beats only for punchy 2–3 word lines; ~20 s total. Treat that as the default pace.
- Generate clip start times from a beat table (see `ads/clothing-same-buyers/gen_composition.py`) instead of hand-typing them.

## Clarity beats speed (ad #8 v7)
- After the reference-paced cut the user said: "it's too fast to process info and it doesn't really make sense."
  Copying the references' frame rate is wrong for an ad that has to explain something; they are mood pieces.
- What fixed it: one story in full sentences (callout → question → relate → problem that ANSWERS the question →
  solution in plain words → payoff that echoes the question → CTA); 6–8 scenes in ~24 s, each held 2–4 s; finished
  lines held ≥1.5 s; build one object across the relate beats (one post that gets likes, then repeat orders) instead
  of new graphics each beat; label every metaphor (person icons + a legend, not anonymous squares).
- Don't use fragments ("story. reel. post.", "boost it? same crowd.") unless the previous frame set them up.
- If the end card shows a brand mark the copy doesn't name (e.g. the user's "SA" art), keep the body to "we run…"
  rather than naming a different brand mid-video.

## Craft
- User-supplied music (ad #7): "Secondhand extended outro" (fan edit of Don Toliver ft. Rema), screen-recorded, 16 s,
  139.2 BPM, band-limited, first 3.5 s was another clip. Looped 4.8271–15.1719 s (6 bars). Delivered with-music + SFX-only cuts.
- Single-pass `loudnorm` undershoots music-only mixes (got −16.8 instead of −14); `build_audio.py` now measures and corrects.
- Without a VO, every caption must read as a full thought; check each line for words that only existed in the voice.
- Two-line key lines push into graphics below; leave ~360 px under the caption band or move graphics down.
- Count VO words before generating: 3 words/s. A 125-word script ≈ 45 s; 75 words ≈ 24 s.
- Build-on captions (a line growing word by word) wrap fast at 136 px; keep the key line ≤3 short words or let it wrap
  to two lines deliberately.
- Small graphic copies of cards read as "smudges" unless they carry text; scale real copies.
- Earlier engines (`ads/electrician-comment-quality/adkit.py` PIL engine, `ads/electrician-theatre/` Theatre.js
  renderer) still work if HyperFrames is unavailable, but HyperFrames + OpenMontage is the current standard.
