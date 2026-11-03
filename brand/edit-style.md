# Southline Edit Style (v2 draft, awaiting approval)

Visual review page: `brand/edit-style-sheet.html` (published as an artifact). Learned from `References/` (three reels). Palette from the Southline offer page.
Inspired by the references, never a copy of them. Section 8 is binding.

## 1. Colour
- Cloud `#ECEEED` (light base) · Pine `#0C2A22` (dark base) · Ink `#0E1412` (text on Cloud) · Graphite `#56605B` (secondary) · Fog `#C6CCC8` (rules/marks)
- Accent: Gold `#C9821F` on Cloud, Gold Bright `#F0B455` on Pine. **Max one accent element per frame.** (No blue or red accents: those belong to the references.)
- Frame share: base 70 % / text+footage 25 % / accent 5 %.
- Grade footage/photos: saturation 0–20 %, contrast +15, blacks tinted toward Pine (never #000). Skin may keep 20 %.
- Alternate Cloud/Pine scenes for story shifts (problem on Pine, solution on Cloud, end card on Pine). One gold haze per Pine scene at 8–12 % opacity. No multi-colour or blue glows.

## 2. Typography
- Key word: Instrument Sans Bold, tracking −4 %, line-height 0.95, lowercase/sentence case, 150–190 px @1080w.
- Lead-in: Instrument Serif Italic, 0.42× key size (64–80 px), 75 % opacity, directly above the key word, left-aligned.
- Body/UI: Instrument Sans Medium 40–48 px. Annotation: IBM Plex Mono 22–26 px, uppercase, +12 % tracking, Graphite.
- Never: all-caps headlines, drop shadows, outlined readable text, >2 weights per frame.

## 3. Captions
- Word-by-word on the spoken syllable (Whisper timings). Each word: rise 24 px from 8 px blur, 180 ms, expo-out.
- One highlight per caption: gold underline sweeps left→right in 220 ms on the stressed word.
- Build-on variant for lists/promises: the line grows word by word while the camera eases along with the newest word.
- Key line max 3 words; lead-in max 4. Break on meaning.
- Position: 30–45 % down, 72 px side margins, left-aligned. Never in bottom 20 %.
- Exit: 120 ms fade + 12 px up as the next lead-in starts. Never two captions at once.

## 4. Cuts and pacing
- Hook: motion in frame 1, core claim readable by 1.0 s. No logo intro, no fade-in.
- Shots 1.2–2.2 s; a smaller change (word, push, mark) every eighth note (~0.24 s at 124 BPM; at least every 0.5 s).
- Cut on a beat or the first syllable of a phrase. Hard cut = new idea; morph = same object continues.
- 12–25 s total. One 2–2.5 s breather before the payoff. End card 1.5–2 s that loops to frame 1.

## 5. Camera, zoom, transitions
- Every shot pushes in 3–6 % (ease in-out). No static frames.
- Punch-in 12 % in 250 ms (expo-out) on key word/reveal.
- Signature: gold line wipe (6 px line, 400 ms ease in-out), max twice per edit.
- Whip: 250 ms directional blur pan in the travel direction for jumps between places/topics, 2 % settle; max twice, never back to back with the line wipe.
- Morph (word→bar→card→end card) 450 ms back-out 1.4. Zoom-through into a letter counter/negative space (300 ms in, 400 ms out).
- Easing: entrances expo-out 0.5 s · exits power-in 0.25 s · camera ease in-out · UI back-out 1.4 · linear only for particles/grain.
- Shake only on impacts: ≤8 px, 200 ms.

## 6. Motion graphics ("measure marks")
- Crop corners (14 px arms, 1.5 px Fog/Graphite), tick rulers, hairlines; draw on in 300 ms at scene open.
- Mono corner labels: "02 — PROBLEM", timecodes, measured facts.
- Ghost word: key idea 600–900 px, 1 px outline, 10–12 % opacity, slides 60 px across the shot.
- Shapes: gold bars/rectangles only (radius 4–8). No circles, suns, rings, stars.
- Path line: solid 3 px line with small ruler ticks that draws along its path, mono label. Never dashed routes, flag pins or avatar bubbles.
- Cutouts: monochrome on Cloud, soft contact shadow, one gold bar behind.
- Numbers count up (power-out 0.8–1.2 s), tabular figures, one hero number per frame.
- UI cards: Pine, 32 px radius, one gold detail, enter with ≤8° 3D tilt.
- Devices: phone/laptop renders only for the user's own product or real screens; 3D turn ≤20°.

## 7. Music and sound
- Minimal electronic / tech-house, 118–128 BPM, warm sub, sparse top, no vocals under VO. Licensed/royalty-free only.
- VO close, dry, cleaned. Final mix −14 LUFS integrated, −1 dBTP. Music ducks 8–10 dB under speech (150 ms release).
- SFX: air whoosh on transitions · soft sub-thump on hook/impacts · faint tick on word reveals (−28 dB) · riser into end card · 200–300 ms music drop-out right before the payoff · one resolved final hit.
- Cuts/punch-ins on beats; caption words on syllables; if they disagree the voice wins.

## 8. Inspired, not copied (binding)
- Always: the Southline palette, our three typefaces, measure-mark graphics, the user's own/licensed footage, original copy.
- Never: red circle/sun motif, dotted rings, QR/barcode decoration; blue or red accents; dashed map routes, flag pins, avatar bubbles;
  Apple, PayPal or any brand's logo/UI/product imagery;
  film/TV stills, celebrities or characters without rights; the references' layouts, caption wording, music or shot order.
- Before each render, compare key frames side by side with `References/`. If a frame could pass for theirs, change it.

## 9. Pre-flight (run before every render)
1. Hook moves in frame 1, readable by 1.0 s.
2. Palette only (Cloud, Pine, Ink, Graphite, Fog); one gold element per frame.
3. Captions: serif-italic lead, ≤3-word bold key line, one underline, voice-synced.
4. Nothing important in the bottom 20 %.
5. Every shot drifts; shots 1.2–2.2 s; change at least every 0.5 s.
6. Line wipe ≤2 uses; whip ≤2 uses.
7. −14 LUFS, −1 dBTP, music ducked.
8. Originality check passed.
9. End card 1.5–2 s, loops cleanly.
