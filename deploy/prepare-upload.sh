#!/usr/bin/env bash
# Build an upload-ready copy of the site for shared hosting (Register365,
# cPanel, or any plain web host).
#
#   ./deploy/prepare-upload.sh yourdomain.ie          # Linux/Apache (default)
#   ./deploy/prepare-upload.sh yourdomain.ie windows  # Windows/IIS
#
# Produces  dist/  and  dublin-trades-upload.zip
# Upload the CONTENTS of the zip into the web root (public_html), not the
# folder itself - the site uses root-relative paths like /assets/... and will
# break in a subfolder.

set -euo pipefail
cd "$(dirname "$0")/.."

DOMAIN="${1:-}"
PLATFORM="${2:-linux}"
OUT="dist"
ZIP="dublin-trades-upload.zip"

if [ -z "$DOMAIN" ]; then
  echo "Usage: $0 <your-domain.ie> [linux|windows]" >&2
  exit 1
fi
DOMAIN="${DOMAIN#http://}"; DOMAIN="${DOMAIN#https://}"; DOMAIN="${DOMAIN%/}"

rm -rf "$OUT" "$ZIP"
mkdir -p "$OUT"

# Only the files that belong on a web server. Host-specific configs for other
# platforms, the README and the git plumbing stay behind.
cp -r index.html assets robots.txt sitemap.xml site.webmanifest \
      favicon.svg favicon.ico .well-known "$OUT"/

case "$PLATFORM" in
  linux)   cp .htaccess "$OUT"/ ;;
  windows) cp deploy/web.config "$OUT"/ ;;
  *) echo "Unknown platform: $PLATFORM (use linux or windows)" >&2; exit 1 ;;
esac

# Swap the placeholder domain everywhere it appears.
find "$OUT" -type f \( -name '*.html' -o -name '*.xml' -o -name '*.txt' \
     -o -name '*.webmanifest' -o -name '*.js' -o -name '*.css' \) \
     -exec sed -i "s|www\.dublintrades\.ie|${DOMAIN}|g" {} +

# Only the full placeholder counts as unreplaced - a real domain may legitimately
# contain part of it.
if grep -rq "www\.dublintrades\.ie" "$OUT" 2>/dev/null; then
  echo "WARNING: placeholder domain still present in:" >&2
  grep -rl "www\.dublintrades\.ie" "$OUT" >&2
  exit 1
fi

( cd "$OUT" && zip -q -r -X "../$ZIP" . )

echo "Built $OUT/ and $ZIP for https://${DOMAIN}/ (${PLATFORM})"
echo "Files: $(find "$OUT" -type f | wc -l)   Size: $(du -sh "$OUT" | cut -f1)"
echo
echo "Upload the CONTENTS of $ZIP into public_html (not the folder itself)."
