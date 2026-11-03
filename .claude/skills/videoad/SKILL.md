---
name: videoad
description: >
  Make Southline's short-form video ads (9:16 Meta / Instagram / TikTok reels) end to end: research the audience's real
  problem, pick a fresh angle, write a hook → open loop → relate → problem → solution → CTA script, voice it (Irish
  ElevenLabs VO with word timings), build an on-brand HyperFrames composition through OpenMontage following the Southline
  Edit Style, score it with ducked music and SFX, run the quality gates, render, QA the frames, and deliver.
  Use this skill whenever the user asks for a video, ad, reel, promo, "video prompt", new angle/hook, or re-edit for
  Southline, for electricians, plumbers or other tradespeople, or for anything targeting tradesmen, even when they just
  say "make a video", "make a new one", "different angle", "change the colours" or paste a video brief.
---

# videoad: Southline video ads, end to end

Southline sells Meta ads (Facebook + Instagram) that bring tradespeople, mostly electricians in Ireland, their **own,
pre-checked enquiries for big jobs**. It also targets **clothing brands** (new ads every week, new buyers beyond their followers,
reminders for browsers; see ad #8 in the angles log); confirm offer details for any new vertical. The user (Ryan, Southline's founder) wants scroll-stopping 9:16 ads that relate to
the trade and sell that outcome. This skill is the whole production line we built and refined together; follow it so
every ad is on-brand, honest, and different from the last one.

Work in the user's repo (`ads/<slug>/` for each ad). Deliver the MP4 with `SendUserFile`, commit and push to the
session's branch, and end with a short summary (scenes table, what to check, files).

## 0. Read before every ad

1. `references/brand-southline-edit-style.md`, the house style (palette, type, captions, pacing, motion, sound,
   originality rules, pre-render checklist). If the repo has a newer `brand/edit-style.md`, that one wins; it is the
   user's brand sheet and may have been edited.
2. `references/angles-log.md`, every angle, hook, CTA keyword and look already used, plus the user's feedback. **A
   new ad must not reuse an angle, hook, CTA keyword or visual system from that log** unless the user asks for a
   re-edit. Append the new ad to the log when you deliver.
3. `references/lessons.md`: bugs, blocked hosts and fixes we already paid for. Skim it so you don't repeat them.

## 1. Understand the brief (don't over-ask)

The user writes short, fast messages ("make a new one", "improve motion design", "i want them now"). Infer intent from
the conversation and these defaults, and only ask when a choice changes the outcome *and* can't be undone cheaply
(e.g. spending a lot of credits, publishing). Defaults:
- Audience: self-employed electricians / small firms (1–5 vans) in Ireland, Safe Electric registered.
- Offer: Southline runs Meta ads for their business; leads are theirs (not shared), checked first (job, county,
  timeframe), sent to their phone. **They want clients now, not later**: never frame results as next month/January.
- Format: 9:16, 1080×1920, 20–26 s, sound-on with captions, Comment-<KEYWORD> CTA.
- Don't put prices, guarantees, client results or "no contract" on screen unless the user confirms them for Meta ads.
  (The €800/€350 and "live in a day" claims on the site belong to the AI-receptionist product, not Meta ads.)

**Clarity rule (the user's standing feedback):** a viewer must know within the first seconds *who this is for*,
and by the end exactly *what Southline sells* and *which problem it fixes*. Name the audience out loud and on screen
("Electricians in Ireland"), name their problem in their own words so they recognise themselves, and say the offer
plainly: "Southline runs Facebook and Instagram ads for your business. The enquiries come to you, not five other lads."
Prefer plain statements to clever metaphors; if a metaphor is used, translate it in the next line.

If the user pastes a full video prompt/brief, treat it as the spec and build it; fix only what can't work (e.g. a VO
longer than the runtime) and say what you changed.

## 2. Research the problem (when the angle needs it)

Find the audience's real pain before writing. Use `WebSearch` (extended mode for niche/recent facts). Start from
`references/research-electricians-ireland.md`, which holds the findings, figures and sources we already have, and
check that grant figures are still current. Rules:
- Separate what sources say from your inference; flag weak sources (lead-platform rivals, installer blogs).
- Never put an unverified statistic on screen. Use it to shape the angle; keep on-screen claims to things the viewer
  will recognise from their own life ("four other lads get it too").
- If a site fails with ENOTFOUND/403, it's the session's network policy: stop trying more sites, name the host, and
  carry on (see lessons.md).

## 3. Angle → script

Use `references/script-framework.md`. In short:
- Beats: **Hook** (motion + claim readable by 1.0 s) → **open loop** question → **relate** (their evening, their van,
  their words) → **problem** (concrete, visual) → **solution** (Southline, in plain words) → **payoff** breather →
  **CTA** "Comment <KEYWORD>" with a new keyword.
- Word budget: ~3 words/second of VO. A 24 s VO is ~75 words. Count before generating; a long script is the most
  common mistake.
- Talk like the trade: sparks, lads, the van, pricing jobs at the kitchen table, worth the drive. Real Irish places
  (Naas, Swords, Lucan, Bray, Douglas, Salthill, Navan).
- If the user only asked for a *prompt*, deliver the research summary + script + shot list + AI B-roll prompts as text
  (see script-framework.md for the prompt template) and offer to produce it.

## 4. Voiceover (only if asked) + timings

**Default: no voiceover.** The user said "dont need voiceovers": ads are text-led with music and SFX, so the captions
must carry the whole message on their own (full sentences, no line that only made sense with a voice). Time caption
words from a reading pace instead: ~0.15–0.3 s between words, hold each finished line ≥ 0.4 s + 0.3 s per word,
scene changes on phrase ends. Skip the ElevenLabs steps below unless the user asks for a voice.

ElevenLabs steps (when a VO is wanted):

1. `creative_create_flow` (one flow per ad) → `creative_list_voices` (language en, accent irish). Default voice:
   **"Sean – Laid Back & Friendly" `kU1Fu9pyfEvPnMpoV67R`** (natural, not stage-Irish). Say which voice you used.
2. `creative_generate_speech` with `eleven_v4`, a short direction tag at the start
   (`[casual, straight-talking, like a mate in the trade]`), default 2 takes (~17¢ each).
3. Pin the take: `creative_add_flow_asset_node` (modality audio, generation_id) → `creative_transcribe_audio`
   (`eleven_scribe_v1`, connect_from that node; free). Read per-word `start` times from the status result. The
   direction tag shows up as near-zero-length "words" at t≈0; ignore them.
4. Download the MP3 for the mix. **In cloud sessions `elevenlabsusercontent.com` is usually blocked.** If the download
   fails, don't route around it: build and render everything else (captions are already timed), deliver a no-VO cut,
   and ask the user to either allow `elevenlabsusercontent.com` in the environment's network settings or upload the
   take. Then run step 7 with the VO and re-render.
5. Images: only generate if the edit needs photos, and price first with `estimate_only` (~7¢/image). The image models
   return 16:9 by default; set a 9:16 aspect explicitly or the crop will be soft. Graphics-led edits don't need them.

### Colours
Change the palette for every new ad unless the user asks to keep one: keep the brand sheet's *structure* (two
neutrals + one accent, roles, one accent element per frame, contrast) and pick a new palette not in the angles log
(no red or blue accents: those belong to the references). Record it in the log.

## 5. Build the composition (HyperFrames via OpenMontage)

OpenMontage (`github.com/calesthio/OpenMontage`) is the production system; HyperFrames is its HTML+GSAP renderer.
If it isn't installed: `git clone --depth 1 https://github.com/calesthio/OpenMontage.git` into the scratchpad, then
`make setup` (≈5 min, background it). Set `OM=<path to OpenMontage>`.

1. `bash scripts/new_project.sh <OM>/projects/<slug>` copies `assets/template/` (fonts, GSAP, a brand-styled
   starter `index.html` with the caption/motion helpers) into `<slug>/hyperframes/`.
2. Author scenes in `index.html`. Start from the template's helpers: `words(capSel, times)`, `under()`, `exit()`,
   `drift()`, `punch()`, plus the gold line wipe and whip. `assets/examples/leads-ireland.html` is a complete,
   passing 25.6 s ad to copy patterns from (VO-timed captions, lead cards fanning to vans, path line → checks → phone,
   CTA end card).
3. Time every caption word to the VO word timings (or the beat grid). **Pace like the references:** open on the
   audience callout ("Clothing brands." / "Electricians in Ireland.") readable at frame 0, then the open-loop question by
   ~1 s, then a new frame every ~0.8–1.7 s with 2–5 big centred words (15–18 s total). Something moves every ~0.5 s;
   each shot lands punched in and creeps 3–6 %. See lessons.md → "Reference pacing".
4. **Make the visuals new each time.** The template is a starting kit, not a look to reuse: invent new graphics and
   motion for the angle while staying inside the brand sheet. Check angles-log.md for what's been done.
5. Keep the authoring rules in `references/lessons.md` → "HyperFrames gotchas" (no template-literal
   `querySelector`, `tl.set` before revealing hidden elements, `data-layout-ignore` on full-frame overlays, local
   fonts only, etc.).

## 6. Score

**If the user supplies a track** (often a screen recording of a TikTok/Instagram sound): extract it with ffmpeg, find the
steady section (skip any other clip at the start; check a spectrogram), run `scripts/beat_grid.py track.wav --start <s>`
for tempo, downbeat and a bar-aligned loop (verify it against an onset plot), and run
`build_audio.py cues.json --music track.wav --music-in <downbeat> --music-out <loop_out>`; drop word ticks under a real song.
**Cut to the beat** (the user asks for it): build the timeline on `B(n) = n × beat`, with every scene change, caption
word, pulse and cue on beats or eighths, and the runtime a whole number of bars. See lessons.md → "Beat-locked edits".
Name the track and warn plainly: commercial songs are not licensed for paid Meta ads (expect rejection or muting); the
legitimate route is an organic post with the in-app sound. Also render a `--no-bed` SFX-only cut so they can add the
sound in-app or swap in licensed music.

Otherwise:

`python3 scripts/build_audio.py cues.json [vo.mp3] -o <slug>/hyperframes/assets/audio.wav`
- `cues.json`: `{"duration": 25.6, "bpm": 124, "dropouts": [[19.19, 19.44]], "events": [[t, "whoosh", 0.55], …]}`.
  Voices: ping pop click tick coin whoosh swish hit shimmer glitch riser.
- Follow the sheet: whoosh on transitions, sub "hit" on the hook word, faint ticks (gain ~0.07) on word reveals,
  250 ms music drop-out before the payoff, riser into the end card, one resolved hit.
- With a VO it ducks the music ~9 dB under speech (20 ms attack / 150 ms release) and loudnorms to −14 LUFS / −1 dBTP.

## 7. Gates, render, QA

1. Lint fast: `cd <slug>/hyperframes && npx --yes hyperframes lint --json`.
2. Look before rendering: `npx --yes hyperframes snapshot --at t1,t2,…` (one per scene + mid-transition), then
   **Read the contact sheet image** and fix overflow, collisions, empty-looking frames, illegible small text.
3. Full gate + render through OpenMontage: `bash scripts/check_and_render.sh <OM> projects/<slug>/hyperframes <out.mp4>`
   (runs `hyperframes_compose` `check`, which needs lint, runtime, layout, motion, contrast, craft and audio all OK,
   then `render_existing` at high quality). Fix every error; warnings are judgement calls.
4. QA the MP4: `bash scripts/qa.sh <out.mp4> t1 t2 …` (ffprobe, loudness, frame strip). Read the strip.
5. Run the brand sheet's pre-render checklist (§9) and the originality check against `References/` if it exists.

## 8. Deliver

- Save source to the repo: `ads/<slug>/composition/` (index.html + assets minus audio.wav), `build_audio.py`
  + `cues.json`, a short `README.md` (angle, VO text + voice, how to re-render). Commit with a clear message and push
  to the session branch (retry on network errors).
- `SendUserFile` the MP4 (`display: render`), with a one-line caption.
- Reply briefly: what it is (runtime, angle), a scenes table with timings and on-screen lines, what you changed from
  their brief and why, credits spent, anything blocked and the one-step fix, things to check before running (claims,
  comment automation for the CTA keyword), and files. Append the ad to `references/angles-log.md`.

## Honesty and originality (always)

- Inspired by the references, never a copy: no other brands' logos/UI, no film/TV stills or characters, no reference
  layouts or wording (brand sheet §8).
- No invented client results or numbers presented as real; illustrative jobs/areas are fine and should be called
  illustrative in your reply.
- Blocked host or permission denial → report it and continue with what doesn't depend on it; never work around policy.
- Say what you couldn't verify (e.g. you can't hear audio; loudness/spectrum are measurements).
