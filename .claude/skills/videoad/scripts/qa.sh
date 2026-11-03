#!/usr/bin/env bash
# QA a rendered ad: stream info, loudness, and a frame strip at the given times.
#   bash qa.sh out.mp4 0.5 3.9 8.2 12.5 ...      -> prints probe + LUFS, writes out_qa.png (Read it)
set -euo pipefail
[ $# -ge 2 ] || { echo "usage: $0 <video> <t1> [t2 ...]"; exit 1; }
V="$1"; shift
ffprobe -v error -show_entries format=duration,size:stream=codec_name,width,height,r_frame_rate -of compact "$V"
ffmpeg -i "$V" -af ebur128 -f null - 2>&1 | grep -E "^\s+(I:|Peak:)" | head -2 || true
TMP="$(mktemp -d)"; i=0; ins=()
for t in "$@"; do ffmpeg -loglevel error -y -ss "$t" -i "$V" -frames:v 1 -vf "scale=216:-1" "$TMP/f$i.png"; ins+=(-i "$TMP/f$i.png"); i=$((i+1)); done
OUT="${V%.*}_qa.png"
if [ $i -gt 1 ]; then ffmpeg -loglevel error -y "${ins[@]}" -filter_complex "hstack=$i" "$OUT"; else cp "$TMP/f0.png" "$OUT"; fi
echo "frame strip: $OUT"
