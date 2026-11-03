# Southline × Irish electricians: "Business check" (9:16, 27.3 s, no voiceover)

Made with the `videoad` skill (OpenMontage + HyperFrames); passed all 7 check gates. Text-led with music and SFX, mixed to −14 LUFS.

**Angle:** be obvious. Who it's for ("Electricians in Ireland, this one's for you."), make them recognise their
problems on an electrician's test-record sheet (each pain stamped FAIL), name the real problem (good at the work,
people can't find you; their slot in the homeowner's feed is empty), then say plainly what Southline sells: Facebook +
Instagram ads for your business, homeowners near you send the job, straight to your phone. CTA: Comment WORK.

**Palette (new for this ad):** Aubergine #22152F, Lilac #EFECF5, Ink #16101D, Graphite #5E566B, Fog #CFC9DA,
Mint accent #34E0A1 (on dark) / #0E8C63 (on light). All other Southline Edit Style v2 rules apply.

Re-render:
```bash
python3 ../../.claude/skills/videoad/scripts/build_audio.py cues.json -o composition/assets/audio.wav
cd composition && npx hyperframes render --quality high --output ../southline_business_check.mp4
```
