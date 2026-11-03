#!/usr/bin/env bash
# Run OpenMontage's HyperFrames quality gate, then render at high quality.
#   bash check_and_render.sh <OpenMontage dir> <workspace path relative to it, e.g. projects/slug/hyperframes> <out.mp4>
# Exits non-zero (and prints every error) if any gate fails.
set -uo pipefail
[ $# -eq 3 ] || { echo "usage: $0 <OM> <workspace> <out.mp4>"; exit 1; }
OM="$1"; WS="$2"; OUT="$(realpath -m "$3")"
cd "$OM" || exit 1
PY=".venv/bin/python"; [ -x "$PY" ] || PY=python3
"$PY" - "$WS" "$OUT" <<'EOF'
import json, sys
from tools.video.hyperframes_compose import HyperFramesCompose
ws, out = sys.argv[1], sys.argv[2]
H = HyperFramesCompose()
r = H.execute({"operation": "check", "workspace_path": ws})
rep = (r.data or {}).get("report", {})
bad = False
for k, v in rep.items():
    if isinstance(v, dict) and "findings" in v:
        errs = [f for f in v["findings"] if f.get("severity") == "error"]
        print(f"{k:8s} ok={v.get('ok')} errors={len(errs)}")
        for f in errs[:15]:
            bad = True
            print("   ", f.get("code"), "|", (f.get("message") or "")[:160], "| t=", f.get("time"), f.get("selector"))
if not r.success or bad:
    print("CHECK FAILED:", r.error); sys.exit(2)
r = H.execute({"operation": "render_existing", "workspace_path": ws, "output_path": out,
               "quality": "high", "fps": 30, "profile": "tiktok_vertical"})
print("render", "OK" if r.success else "FAILED", r.error or "", out)
sys.exit(0 if r.success else 3)
EOF
