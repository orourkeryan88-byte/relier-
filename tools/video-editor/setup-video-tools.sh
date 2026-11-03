#!/usr/bin/env bash
# Installs and tests the video-editing toolkit: Remotion, HyperFrames, FFmpeg, whisper.cpp, yt-dlp.
# macOS (Homebrew) or Linux (apt). On Windows, run it inside WSL (Ubuntu).
#
#   bash setup-video-tools.sh            # install + test everything
#   TOOLS_DIR=~/somewhere bash setup-video-tools.sh
#   WHISPER_MODEL=small.en bash setup-video-tools.sh   # bigger, more accurate model (default base.en)
#   REMOTION_BROWSER=/path/to/chrome bash setup-video-tools.sh   # optional: use an existing Chrome for Remotion
set -u
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TOOLS_DIR="${TOOLS_DIR:-$HOME/video-tools}"
WHISPER_MODEL="${WHISPER_MODEL:-base.en}"
mkdir -p "$TOOLS_DIR/tests"
say() { printf '\n\033[1m==> %s\033[0m\n' "$*"; }
# results kept in RES_<tool> variables (portable to macOS's bash 3.2, no associative arrays)
pass() { printf -v "RES_$1" '%s' "PASS  $2"; printf '    \033[32mPASS\033[0m %s\n' "$2"; }
fail() { printf -v "RES_$1" '%s' "FAIL  $2"; printf '    \033[31mFAIL\033[0m %s\n' "$2"; }
has() { command -v "$1" >/dev/null 2>&1; }

# ---------------------------------------------------------------- prerequisites
say "Installing prerequisites"
OS="$(uname -s)"
if [ "$OS" = "Darwin" ]; then
  has brew || { echo "Install Homebrew first: https://brew.sh"; exit 1; }
  brew install ffmpeg yt-dlp cmake git node
elif has apt-get; then
  sudo apt-get update -y
  sudo apt-get install -y ffmpeg cmake build-essential git curl python3 python3-pip pipx
  pipx install yt-dlp || python3 -m pip install --user -U yt-dlp
  export PATH="$HOME/.local/bin:$PATH"
else
  echo "Unsupported system: use macOS, Ubuntu/Debian, or WSL on Windows."; exit 1
fi
NODE_MAJOR="$(node -v 2>/dev/null | sed 's/v\([0-9]*\).*/\1/')"
if [ -z "$NODE_MAJOR" ] || [ "$NODE_MAJOR" -lt 22 ]; then
  echo "HyperFrames needs Node.js 22+ (found: $(node -v 2>/dev/null || echo none))."
  echo "Install it (e.g. 'nvm install 22' or https://nodejs.org) and re-run this script."; exit 1
fi

# ---------------------------------------------------------------- 1. FFmpeg
say "FFmpeg: generate, trim, reframe to 9:16, caption, encode"
T="$TOOLS_DIR/tests/ffmpeg"; mkdir -p "$T"
if ffmpeg -loglevel error -y -f lavfi -i testsrc2=size=1920x1080:rate=30:duration=6 -f lavfi -i sine=frequency=440:duration=6 \
     -c:v libx264 -pix_fmt yuv420p -c:a aac "$T/source.mp4" &&
   ffmpeg -loglevel error -y -ss 1 -to 5 -i "$T/source.mp4" \
     -vf "crop=ih*9/16:ih,scale=1080:1920,drawtext=text='FFMPEG OK':fontsize=110:fontcolor=white:box=1:boxcolor=black@0.6:boxborderw=24:x=(w-tw)/2:y=h*0.72" \
     -af "afade=t=in:d=0.5,afade=t=out:st=3.5:d=0.5" -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a aac "$T/edit_9x16.mp4" &&
   [ "$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$T/edit_9x16.mp4")" = "1080,1920" ]; then
  pass ffmpeg "$(ffmpeg -version | head -1 | cut -d' ' -f1-3) -> $T/edit_9x16.mp4"
else fail ffmpeg "edit test failed (drawtext needs ffmpeg built with libfreetype)"; fi

# ---------------------------------------------------------------- 2. yt-dlp
say "yt-dlp: download a 15s section of Big Buck Bunny (Creative Commons)"
T="$TOOLS_DIR/tests/ytdlp"; mkdir -p "$T"
if yt-dlp --no-progress -f "b[height<=480]/bv*[height<=480]+ba/b" --download-sections "*0:10-0:25" --force-keyframes-at-cuts \
     -o "$T/yt_test.%(ext)s" "https://www.youtube.com/watch?v=aqz-KE-bpKQ" && ls "$T"/yt_test.* >/dev/null 2>&1; then
  pass ytdlp "yt-dlp $(yt-dlp --version) -> $(ls "$T"/yt_test.*)"
else fail ytdlp "download failed (try: yt-dlp -U)"; fi

# ---------------------------------------------------------------- 3. whisper.cpp
say "whisper.cpp: build + $WHISPER_MODEL model + transcribe the JFK sample"
W="$TOOLS_DIR/whisper.cpp"
[ -d "$W" ] || git clone --depth 1 https://github.com/ggml-org/whisper.cpp.git "$W"
( cd "$W" && cmake -B build -DCMAKE_BUILD_TYPE=Release >/dev/null && cmake --build build -j --config Release >/dev/null ) &&
( cd "$W" && { [ -f "models/ggml-$WHISPER_MODEL.bin" ] || bash ./models/download-ggml-model.sh "$WHISPER_MODEL"; } )
if "$W/build/bin/whisper-cli" -m "$W/models/ggml-$WHISPER_MODEL.bin" -f "$W/samples/jfk.wav" -otxt -of "$TOOLS_DIR/tests/jfk" >/dev/null 2>&1 &&
   grep -qi "ask not what your country" "$TOOLS_DIR/tests/jfk.txt"; then
  pass whisper "transcribed: $(tr -s ' \n' ' ' < "$TOOLS_DIR/tests/jfk.txt" | cut -c1-80)…"
else fail whisper "transcription test failed"; fi

# ---------------------------------------------------------------- 4. Remotion
say "Remotion: install + render a 3s 1080x1920 test composition"
R="$TOOLS_DIR/tests/remotion"; mkdir -p "$R/src"; cp "$HERE/tests/remotion/src/"* "$R/src/"
( cd "$R" && [ -f package.json ] || npm init -y >/dev/null ) &&
( cd "$R" && npm install --silent remotion@4 @remotion/cli@4 react@18.3.1 react-dom@18.3.1 ) &&
( cd "$R" && npx remotion render src/index.ts Test out/remotion_test.mp4 --log=error ${REMOTION_BROWSER:+--browser-executable="$REMOTION_BROWSER"} )
if [ -s "$R/out/remotion_test.mp4" ]; then pass remotion "remotion $(cd "$R" && node -p "require('remotion/package.json').version") -> $R/out/remotion_test.mp4"
else fail remotion "render failed"; fi

# ---------------------------------------------------------------- 5. HyperFrames
say "HyperFrames: doctor + lint + render a 3s test composition"
H="$TOOLS_DIR/tests/hyperframes"; mkdir -p "$H"; cp "$HERE/tests/hyperframes/index.html" "$H/"
# GSAP is installed in a side folder: a package.json inside $H would be named "hyperframes" and shadow the CLI for npx
D="$TOOLS_DIR/tests/_deps"; mkdir -p "$D"
( cd "$D" && { [ -f package.json ] || npm init -y >/dev/null; } && npm install --silent gsap@3.14.2 ) && cp "$D/node_modules/gsap/dist/gsap.min.js" "$H/"
( cd "$H" && npx --yes hyperframes doctor | tail -25 )
if ( cd "$H" && npx --yes hyperframes lint && npx --yes hyperframes render --quality draft --output hyperframes_test.mp4 ) && [ -s "$H/hyperframes_test.mp4" ]; then
  pass hyperframes "hyperframes $(npx --yes hyperframes --version 2>/dev/null | tail -1) -> $H/hyperframes_test.mp4"
else fail hyperframes "lint/render failed (see 'npx hyperframes doctor')"; fi

# ---------------------------------------------------------------- summary
say "Summary"
for k in ffmpeg ytdlp whisper remotion hyperframes; do v="RES_$k"; printf '  %-12s %s\n' "$k" "${!v:-FAIL  not run}"; done
