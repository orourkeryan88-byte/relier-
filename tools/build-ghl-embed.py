import re, sys

src = open('index.html', encoding='utf-8').read()
ROOT = '#southline-page'

RESET = """
/* ---------------------------------------------------------------
   Host-theme reset. A GHL template styles bare element selectors
   (h1, p, section...), and those beat anything we merely inherit.
   This neutralises them first; every rule below is equal or higher
   specificity and comes later, so our own styling still wins.
   --------------------------------------------------------------- */
#southline-page h1,#southline-page h2,#southline-page h3,#southline-page h4,
#southline-page h5,#southline-page h6,#southline-page p,#southline-page span,
#southline-page a,#southline-page li,#southline-page ul,#southline-page ol,
#southline-page em,#southline-page strong,#southline-page i,#southline-page b,
#southline-page button,#southline-page summary,#southline-page details,
#southline-page div,#southline-page section,#southline-page article,
#southline-page header,#southline-page footer,#southline-page nav{
  font-family:inherit;
  font-weight:inherit;
  font-style:normal;
  font-size:inherit;
  color:inherit;
  line-height:inherit;
  letter-spacing:inherit;
  text-transform:none;
  text-align:inherit;
  text-decoration:none;
  background:none;
  border:0;
  border-radius:0;
  margin:0;
  padding:0;
  box-shadow:none;
  float:none;
  text-shadow:none;
  max-width:none;
  min-height:0;
}
#southline-page ul,#southline-page ol{list-style:none}
#southline-page img,#southline-page video,#southline-page iframe{border:0;margin:0}
"""

style = re.search(r'<style>(.*?)</style>', src, re.S).group(1)
script = re.search(r'<script>(.*?)</script>', src, re.S).group(1)
body = re.search(r'<body>(.*?)\n<script>', src, re.S).group(1)

def split_selectors(sel):
    """Split a selector list on top-level commas (ignore commas inside parens)."""
    out, depth, cur = [], 0, ''
    for ch in sel:
        if ch == '(': depth += 1
        elif ch == ')': depth -= 1
        if ch == ',' and depth == 0:
            out.append(cur); cur = ''
        else:
            cur += ch
    if cur.strip(): out.append(cur)
    return out

def scope_one(s):
    s = s.strip()
    if not s: return s
    if s.startswith('from') or s.startswith('to') or re.match(r'^\d+%', s):
        return s                                  # keyframe stops
    if s.startswith('html'):
        return ROOT + s[4:]
    if s == 'body':
        return ROOT
    if s.startswith('body'):
        return ROOT + s[4:]
    if s.startswith(':root'):
        rest = s[5:]
        return ROOT + rest if rest else ROOT
    if s.startswith('*'):
        return ROOT + ' ' + s
    return ROOT + ' ' + s

def scope_block(css):
    """Walk the CSS, prefixing selectors but leaving @keyframes stops alone."""
    out, i, n = [], 0, len(css)
    while i < n:
        # at-rule?
        m = re.match(r'\s*@([a-zA-Z-]+)([^{;]*)([{;])', css[i:])
        if m:
            name, params, term = m.group(1), m.group(2), m.group(3)
            out.append(css[i:i + m.end()])
            i += m.end()
            if term == ';':
                continue
            depth, start = 1, i
            while i < n and depth:
                if css[i] == '{': depth += 1
                elif css[i] == '}': depth -= 1
                i += 1
            inner = css[start:i-1]
            if name.endswith('keyframes'):
                out.append(inner)                  # stops must stay untouched
            else:
                out.append(scope_block(inner))     # @media / @supports
            out.append('}')
            continue
        # ordinary rule
        j = css.find('{', i)
        if j == -1:
            out.append(css[i:]); break
        sel_raw = css[i:j]
        lead = sel_raw[:len(sel_raw) - len(sel_raw.lstrip())]
        sel = sel_raw.strip()
        depth, k = 1, j + 1
        while k < n and depth:
            if css[k] == '{': depth += 1
            elif css[k] == '}': depth -= 1
            k += 1
        decls = css[j+1:k-1]
        if sel.startswith('/*') and '*/' in sel:      # keep leading comments
            cpos = sel.rindex('*/') + 2
            comment, sel = sel[:cpos], sel[cpos:].strip()
        else:
            comment = ''
        scoped = ', '.join(scope_one(s) for s in split_selectors(sel))
        nl = chr(10) if comment else ''
        out.append(lead + comment + nl + scoped + '{' + decls + '}')
        i = k
    return ''.join(out)

scoped_css = RESET + scope_block(style)

# point the media assets at placeholders the user fills from the GHL media library
script = script.replace(
  "    src:    'assets/vsl.mp4',            // H.264 — plays in every real browser\n"
  "    srcAlt: 'assets/vsl.webm',           // optional VP9 fallback; '' to skip\n"
  "    poster: 'assets/vsl-poster.jpg'",
  "    src:    'PASTE_MP4_URL_HERE',        // GHL Media Library URL for vsl.mp4\n"
  "    srcAlt: '',                          // optional: URL for vsl.webm\n"
  "    poster: 'PASTE_POSTER_URL_HERE'      // GHL Media Library URL for vsl-poster.jpg")

out = f'''<!--
  ============================================================
  SOUTHLINE AGENCY — GoHighLevel embed
  ============================================================
  Paste this whole block into a GHL "Custom JS/HTML" element on
  a blank funnel/website page (full width, no padding).

  BEFORE IT WILL WORK:
  1. Upload assets/vsl.mp4 and assets/vsl-poster.jpg to the GHL
     Media Library, copy each file's URL, and paste them into
     CONFIG.video at the bottom of this block.
  2. Leave the page's own section padding at 0 so the design runs
     edge to edge.

  Every style below is scoped to {ROOT}, so nothing here can
  leak out and restyle the rest of your GHL page.
-->

<div id="southline-page">
<style>
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700;800&display=swap');

/* smooth anchor scrolling — this one line is intentionally global */
html{{scroll-behavior:smooth}}

{scoped_css}
</style>
{body}
<script>{script}</script>
</div>
'''
open('ghl-embed.html', 'w', encoding='utf-8').write(out)
print('written ghl-embed.html')
print('unscoped top-level selectors remaining:',
      len(re.findall(r'(?m)^(?!\s*[@}/])[a-z*:\[][^{}]*\{', scoped_css)))
