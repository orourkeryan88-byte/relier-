# Southline × Irish electricians: "Your own leads" (9:16, 25.6 s)

Built to the Southline Edit Style v2 (`brand/edit-style.md`) with OpenMontage + HyperFrames. It passed all 7
`hyperframes_compose check` gates (lint, runtime, layout, motion, contrast, craft, audio).

**Angle:** the work is out there; stop fighting four other lads for it (shared leads, price shopping),
and stop losing the big grant-era jobs to whoever is found first.

**VO** (ElevenLabs, voice "Sean – Laid Back & Friendly", eleven_v4, take 1, 24.4 s). Captions are timed to its word timestamps:
"Sparks… people all over Ireland need an electrician right now. So why are you fighting for scraps? You pay for a lead…
four other lads get it too, and the cheapest wins. And the big jobs, solar, batteries, rewires, go to whoever they find
first. Southline runs ads for your business. Your own leads… checked before your phone even rings. You only quote the
jobs worth the drive. Comment LEADS, and we'll show you how."

`southline_leads_ireland_no_vo.mp4` has the music bed and SFX only. The VO file is in the ElevenLabs flow but couldn't be
downloaded into the cloud session (network policy blocks elevenlabsusercontent.com).

## Finish with the voiceover
```bash
python3 build_audio.py path/to/vo_take1.mp3      # ducks music 9 dB under speech, mixes to -14 LUFS / -1 dBTP
cd composition && npx hyperframes render --quality high --output ../southline_leads_ireland.mp4
```
