# Dublin Trades — website

A single-page site for Dublin Trades (24 hour tradesmen, Dublin & Fingal).
Static HTML/CSS/JS with **no build step, no framework, no third-party code**.

Rebuilt from a 3.1 MB single-file HTML export into a deployable site:
white + yellow theme, SEO metadata and structured data, a GDPR cookie
consent layer, and a hardened security posture.

---

## ⚠️ Before you go live — 3 things you must do

1. **Set your real domain.** The site uses `https://www.dublintrades.ie/` as a
   placeholder. Replace it everywhere:

   ```bash
   grep -rl "www.dublintrades.ie" . | xargs sed -i 's|www\.dublintrades\.ie|YOUR-DOMAIN.ie|g'
   ```

   It appears in `index.html` (canonical, Open Graph, JSON-LD), `sitemap.xml`,
   `robots.txt`, `.well-known/security.txt` and `deploy/nginx.conf.sample`.
   A wrong canonical URL will actively hurt your search ranking.

2. **Serve the security headers.** See [Security](#security) — the response
   headers are the real protection, and on GitHub Pages they do not apply.

3. **Claim your Google Business Profile.** For a local trades business this
   moves the needle more than anything on the page. Once claimed, add the
   profile URL to the `sameAs` field of the JSON-LD block in `index.html`, and
   add your full registered address to `address`.

---

## Colour

Primary palette is **white and yellow**.

| Token | Value | Used for |
|---|---|---|
| `--bg` | `#ffffff` | Page background |
| `--yellow` | `#ffd400` | Buttons, highlights, icon tiles, checkmarks |
| `--ink` | `#141414` | Body text, and text on yellow |
| `--accent-ink` | `#7a5e00` | Small "yellow" text on white |

Yellow is used for **fills, never for body text** — yellow text on white is
about 1.6:1 and is unreadable. Where something needs to read as yellow in
small text, `--accent-ink` is used instead (6.1:1 on white).

Every text/background pair on the page was measured from rendered pixels and
passes WCAG AA in both light and dark mode (lowest measured: 5.62:1).

The WhatsApp buttons stay green on purpose — that green is how people
recognise WhatsApp at a glance. Change `--green` in
`assets/css/styles.css` if you would rather they were yellow too.

Dark mode is supported and follows the visitor's system setting.

---

## SEO

| Area | What was done |
|---|---|
| Document | The original file had no `<!DOCTYPE>`, `<html>`, `<head>` or `<body>` — search engines were parsing a fragment. Now a valid document with `lang="en-IE"`. |
| Title & description | Keyword-led title and a 157-character meta description. |
| Canonical & robots | `rel=canonical` plus `max-image-preview:large`. |
| Social | Open Graph + Twitter card with a generated 1200×630 share image. |
| Structured data | JSON-LD `@graph`: `HomeAndConstructionBusiness` (phone, email, area served, 24/7 opening hours, 11-service offer catalog), `WebSite`, and `FAQPage`. |
| Content | New FAQ section (6 questions) and a 24-area local coverage list — both real ranking content for "tradesman near me" style searches. |
| Headings | Exactly one `<h1>`; sections use `<section aria-labelledby>` with real `<h2>`s. |
| Images | 3.1 MB of inline base64 replaced with responsive `<picture>` elements: WebP with JPEG fallback, `srcset`/`sizes`, lazy loading below the fold, and `width`/`height` on every image to stop layout shift. |
| Speed | Full page including every image: **424 KB over 24 requests**, down from a 3.1 MB single file. Fonts self-hosted and preloaded; hero image preloaded. |
| Crawling | `robots.txt` and `sitemap.xml` (with image entries). |

**Deliberately not added:** `AggregateRating` / `Review` structured data.
Google treats self-serving review markup on your own business as a
manual-action risk, and the star ratings would be unverifiable. The reviews
still display on the page as normal content. Collect reviews on your Google
Business Profile instead — those show in search results legitimately.

---

## Security

### Is it safe? Yes — here is the audit

The uploaded file was checked before anything was reused:

- **18 embedded images decoded and inspected.** All are plain baseline JPEGs
  (JFIF/quantisation/Huffman/scan markers only). **Zero bytes after the
  end-of-image marker**, and no EXIF or comment segments — the two places a
  payload hides in a JPEG. Nothing executable, no polyglot files.
- An automated byte scan flagged `MZ` (the DOS executable signature) in two
  images. **False positive** — both occurrences sit inside compressed scan
  data, not at offset 0, and a random 2-byte sequence turns up about once
  every 65 KB. Both files parse as clean JPEGs.
- **No third-party scripts, no trackers, no analytics, no ad tags.**
- **No external requests at all.** Verified in a real browser: loading the
  page makes **zero** requests off your own domain.
- The original loaded fonts from Google's CDN, which sent every visitor's IP
  to Google. Fonts are now self-hosted (OFL-licensed, redistribution allowed).

There was never malware in this file. The risk in the original was
different: no security headers, so it could be framed and clickjacked.

### Anti-clickjacking ("can't get jacked")

Three layers:

1. `frame-ancestors 'none'` in the Content-Security-Policy response header.
2. `X-Frame-Options: DENY`.
3. `assets/js/guard.js` — a render-blocking frame-buster that hides the page
   and tries to break out. Tested: framing the site from another origin
   renders a blank frame.

> **`frame-ancestors`, `X-Frame-Options` and HSTS are ignored inside a
> `<meta>` tag.** They only work as real HTTP response headers. The `<meta>`
> CSP in `index.html` is a fallback for everything else.

### Other hardening

- **Strict CSP** — `default-src 'self'`, `object-src 'none'`, `base-uri 'self'`,
  `form-action 'self'`. Script and style sources need **no `unsafe-inline`**,
  because the page contains zero inline scripts, inline styles and `on*`
  handlers. That is what makes XSS hard here.
- `X-Content-Type-Options: nosniff`, `Referrer-Policy`, `Permissions-Policy`
  (camera/mic/geolocation/payment all denied), HSTS, COOP, CORP.
- Every `target="_blank"` carries `rel="noopener noreferrer"`.
- The quote form validates input, has a honeypot field and a timing check for
  bots, and renders status text with `textContent` — never `innerHTML`.
- `.well-known/security.txt` so anyone can report a problem.

### Where to deploy (this matters)

| Host | Custom headers? | Verdict |
|---|---|---|
| Cloudflare Pages | Yes — uses `_headers` | ✅ Recommended, free |
| Netlify | Yes — `_headers` / `netlify.toml` | ✅ Recommended, free |
| Apache / cPanel | Yes — `.htaccess` | ✅ Fine |
| nginx / VPS | Yes — `deploy/nginx.conf.sample` | ✅ Fine |
| **GitHub Pages** | **No** | ⚠️ See below |

This repo currently has GitHub Pages workflows. **GitHub Pages cannot send
custom response headers**, so on Pages you lose `frame-ancestors`,
`X-Frame-Options` and HSTS. The `<meta>` CSP and `guard.js` still work, so you
are not defenceless — but for the full set, put Cloudflare Pages in front (it
is free, and also gives you HTTPS and caching).

Config files are already written for every option; they only need the
domain updated.

---

## Uploading to Register365 (reg365)

Register365 is normal Apache shared hosting, so `.htaccess` works — you get the
**full** set of security headers there, unlike GitHub Pages.

### 1. Build the upload bundle

```bash
./deploy/prepare-upload.sh yourdomain.ie          # Linux hosting (normal)
./deploy/prepare-upload.sh yourdomain.ie windows  # Windows/IIS plans only
```

This swaps the placeholder domain everywhere, copies only the files that belong
on a web server, and writes `dublin-trades-upload.zip`.

Not sure which plan you have? If your control panel is cPanel, or you see a
`public_html` folder, it is Linux.

### 2. Upload

Control panel → **File Manager** (or FTP with the details on your hosting
dashboard) → open the **web root**. That is the folder that already contains
the default holding page — usually `public_html`, sometimes `httpdocs` or `web`.

Upload the zip there and use **Extract**.

> Upload the **contents** of the zip, not the folder itself. The site uses
> root-relative paths (`/assets/...`), so it must sit directly in the web root.
> In a subfolder every image and stylesheet 404s.

### 3. Three things that catch people out

- **Delete the default holding page.** Any existing `index.html` or
  `index.php` left in the web root can take priority over yours.
- **Show hidden files.** `.htaccess` and `.well-known` start with a dot and
  most File Managers hide them by default. Turn on "show hidden files" and
  confirm both arrived — without `.htaccess` you lose every security header.
- **Turn on SSL before anything else.** Find Let's Encrypt / AutoSSL / free SSL
  in the panel and enable it for the domain. The `.htaccess` only sends HSTS
  when the request is already HTTPS, so you cannot lock yourself out — but the
  forced-HTTPS redirect needs a working certificate.

### 4. Check it worked

```bash
curl -sI https://yourdomain.ie | grep -i -E "content-security|x-frame|strict-transport"
```

You should see `content-security-policy`, `x-frame-options: DENY` and
`strict-transport-security`. Or paste the domain into
[securityheaders.com](https://securityheaders.com) — it should grade A.

If **no** custom headers come back, Register365 has `mod_headers` disabled on
your plan. Ask their support to enable it. The `<meta>` CSP and `guard.js`
still protect the page in the meantime; the gap is `X-Frame-Options` and HSTS.
Putting Cloudflare (free) in front of the domain also adds headers regardless
of the host.

### 5. Then

Submit `https://yourdomain.ie/sitemap.xml` in
[Google Search Console](https://search.google.com/search-console) so the pages
get indexed.

---

## Cookies

Built to GDPR / ePrivacy rules, which apply in Ireland:

- **Nothing is stored before a choice is made.** Verified: zero cookies on
  first load until a button is pressed.
- Banner offers **Reject all / Customise / Accept all** — rejecting is exactly
  as easy as accepting, which the law requires.
- Analytics and marketing default to **off**.
- Consent is stored in one first-party cookie, `dt_consent`
  (`SameSite=Lax`, `Secure` over HTTPS, 180 days).
- **Cookie settings** links in the footer and in the privacy section let a
  visitor change or withdraw consent at any time.
- Withdrawing consent deletes the optional cookies.
- On-page cookie & privacy notice with a table of exactly what is stored.

Right now `dt_consent` is the **only** cookie the site sets, because there is
no analytics installed.

### Adding analytics later

Put it inside `applyConsent()` in `assets/js/main.js`, in the marked
`if (c.analytics)` block — that is the only place it will respect consent.
Then add the vendor's domain to `script-src` and `connect-src` in **all four**
header files plus the `<meta>` CSP, or the browser will block it. Add the new
cookies to the table in the `#cookies` section.

---

## Structure

```
index.html                  the page
assets/css/styles.css       theme + layout
assets/js/guard.js          frame-buster (render-blocking, loads first)
assets/js/main.js           carousel, cookie consent, quote form
assets/fonts/               self-hosted variable fonts (62 KB total)
assets/img/                 responsive WebP + JPEG, 60 files
_headers                    Netlify / Cloudflare Pages
netlify.toml                Netlify
.htaccess                   Apache / cPanel
deploy/nginx.conf.sample    nginx
robots.txt  sitemap.xml  site.webmanifest  favicon.svg  favicon.ico
.well-known/security.txt
```

Preview locally:

```bash
python3 -m http.server 8099
# http://127.0.0.1:8099/
```

---

## Known limitations

- **The quote form has no backend.** A static site cannot receive form posts.
  It validates locally then opens WhatsApp (or the visitor's mail app) with
  the message pre-filled, so nothing is sent to a third party. To collect
  submissions properly, use Netlify Forms, Formspree or your own endpoint —
  and add that endpoint to `form-action` and `connect-src` in the CSP.
- **Reviews are page content, not verified ratings** — see the SEO note above.
- Images come from the original file. Four slots reused the same photo; that
  was reduced to two by redistributing the 11 unique images, but more
  distinct job photos would improve both the look and image SEO.
- The business address in the structured data is city-level only. Add the
  full address once you are happy to publish it.
