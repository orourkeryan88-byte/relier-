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
- Snapshots land in `.hyperframes/artifacts/snapshots/<id>/` with a `contact-sheet*.jpg`; Read it.

## Craft
- Single-pass `loudnorm` undershoots music-only mixes (got −16.8 instead of −14); `build_audio.py` now measures and corrects.
- Without a VO, every caption must read as a full thought; check each line for words that only existed in the voice.
- Two-line key lines push into graphics below; leave ~360 px under the caption band or move graphics down.
- Count VO words before generating: 3 words/s. A 125-word script ≈ 45 s; 75 words ≈ 24 s.
- Build-on captions (a line growing word by word) wrap fast at 136 px; keep the key line ≤3 short words or let it wrap
  to two lines deliberately.
- Small graphic copies of cards read as "smudges" unless they carry text; scale real copies.
- Earlier engines (`ads/electrician-comment-quality/adkit.py` PIL engine, `ads/electrician-theatre/` Theatre.js
  renderer) still work if HyperFrames is unavailable, but HyperFrames + OpenMontage is the current standard.
