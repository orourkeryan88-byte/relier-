#!/usr/bin/env bash
# Build an upload-ready copy of the site for shared hosting (Register365,
# cPanel, or any plain web host).
#
#   ./deploy/prepare-upload.sh yourdomain.ie          # Linux/Apache (default)
#   ./deploy/prepare-upload.sh yourdomain.ie windows  # Windows/IIS
#   ./deploy/prepare-upload.sh yourdomain.ie static   # Netlify / Cloudflare Pages
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
  echo "Usage: $0 <your-domain.ie> [linux|windows|static]" >&2
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
  # Netlify and Cloudflare Pages both read _headers; netlify.toml is Netlify's
  # own format and is ignored by Cloudflare, so shipping both is safe.
  static)  cp _headers netlify.toml "$OUT"/ ;;
  *) echo "Unknown platform: $PLATFORM (use linux, windows or static)" >&2; exit 1 ;;
esac

# Swap the placeholder domain everywhere it appears. The config files hold it
# as a regex (www\.dublintrades\.ie), so both spellings are handled.
DOMAIN="$DOMAIN" python3 - "$OUT" <<'PYEOF'
import os, re, sys
placeholder = "www.dublintrades.ie"
domain = os.environ["DOMAIN"]
root = sys.argv[1]
exts = (".html", ".xml", ".txt", ".webmanifest", ".js", ".css", ".config", ".htaccess")
changed = 0
for dirpath, _, names in os.walk(root):
    for n in names:
        if not (n.endswith(exts) or n == ".htaccess"):
            continue
        f = os.path.join(dirpath, n)
        try:
            src = open(f, encoding="utf-8").read()
        except UnicodeDecodeError:
            continue
        out = src.replace(placeholder.replace(".", r"\."), domain.replace(".", r"\."))
        out = out.replace(placeholder, domain)
        if out != src:
            open(f, "w", encoding="utf-8").write(out)
            changed += 1
print(f"  rewrote {changed} file(s) to {domain}")

if domain != placeholder:
    stale = []
    for dirpath, _, names in os.walk(root):
        for n in names:
            f = os.path.join(dirpath, n)
            try:
                if placeholder in open(f, encoding="utf-8").read():
                    stale.append(f)
            except (UnicodeDecodeError, OSError):
                pass
    if stale:
        print("ERROR: placeholder domain still present in:", *stale, sep="\n  ", file=sys.stderr)
        sys.exit(1)
PYEOF

( cd "$OUT" && zip -q -r -X "../$ZIP" . )

echo "Built $OUT/ and $ZIP for https://${DOMAIN}/ (${PLATFORM})"
echo "Files: $(find "$OUT" -type f | wc -l)   Size: $(du -sh "$OUT" | cut -f1)"
echo
echo "Upload the CONTENTS of $ZIP into public_html (not the folder itself)."
