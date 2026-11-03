#!/usr/bin/env bash
# Scaffold a new ad workspace: <project-dir>/hyperframes/{index.html, assets/} + an empty cues.json.
#   bash new_project.sh <OpenMontage>/projects/<slug>
set -euo pipefail
[ $# -eq 1 ] || { echo "usage: $0 <project-dir>"; exit 1; }
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="$1/hyperframes"
[ -e "$DEST/index.html" ] && { echo "refusing to overwrite $DEST/index.html"; exit 1; }
mkdir -p "$DEST"
cp -r "$HERE/assets/template/." "$DEST/"
cat > "$1/cues.json" <<'EOF'
{"duration": 25.0, "bpm": 124, "dropouts": [], "events": []}
EOF
echo "scaffolded $DEST (edit index.html; fill $1/cues.json; then build_audio.py -> $DEST/assets/audio.wav)"
