# Video editor toolkit

One script installs and tests: **Remotion**, **HyperFrames**, **FFmpeg**, **whisper.cpp**, **yt-dlp**.

```bash
bash tools/video-editor/setup-video-tools.sh
```

- macOS (needs Homebrew) or Ubuntu/Debian. On Windows, run it inside WSL (Ubuntu).
- Needs Node.js 22+ (HyperFrames). The script stops and tells you if Node is older.
- Installs into `~/video-tools` (override with `TOOLS_DIR=...`). Whisper model defaults to `base.en`
  (`WHISPER_MODEL=small.en` for better accuracy).

Each tool gets a real test, and a PASS/FAIL summary prints at the end:

| Tool | Test |
|---|---|
| FFmpeg | generate 16:9 footage, trim, crop to 1080×1920, burn a caption, fade audio, verify size |
| yt-dlp | download a 15s section of Big Buck Bunny (Creative Commons) from YouTube |
| whisper.cpp | build from source, download the model, transcribe the JFK sample ("ask not what your country…") |
| Remotion | install Remotion 4, render a 3s 1080×1920 spring-animated composition |
| HyperFrames | `doctor`, `lint`, then render a 3s 1080×1920 GSAP composition |
