# Southline Agency — Landing Page

A single-file VSL funnel landing page. No build step, no dependencies.

**Page order:** VSL video → Book a Call (calendar) → What we do → How it works → FAQ → Final CTA.

The audience is **tradesmen / trade businesses** — copy, the industry marquee and the
FAQ all speak to that.

Blue-and-white theme with motion throughout: animated gradient background, word-by-word
headline entrance, scroll-progress bar, scroll-reveal sections, a looping industry
marquee, shimmer on the primary button and hover lifts on every card. All of it is
disabled automatically for visitors with `prefers-reduced-motion`.

## What's already connected

The GoHighLevel calendar is live — `CONFIG.booking.url` points at
`https://api.leadconnectorhq.com/widget/booking/Jyy3OGmnlXllDOv1VZz6` and renders
inline in the **Book a Call** section. Every "Book a Call" button scrolls to it.

Set `mode: 'redirect'` instead if you'd rather the buttons open the booking page in a
new tab — the inline section is then removed automatically.

## No invented claims

The page deliberately contains **no statistics, client counts, testimonials, logos,
timelines, prices or guarantees**, because none were supplied. Nothing on it asserts a
result Southline hasn't verified.

What remains is positioning and process copy. Two things are still worth checking
against how you actually operate before launch:

- **The industry marquee** ("Who we work with") lists Electricians, Plumbing & Heating,
  HVAC, Roofing, Builders & Renovations, Joinery & Carpentry, Landscaping & Groundwork
  and Painting & Decorating. Edit it to the trades you actually serve.
- **The three service cards** describe a standard acquisition scope (paid media,
  funnel/booking systems, follow-up). Confirm each line is something you deliver.

If you later want proof elements — real numbers, named clients, testimonials — add them
only once you can back them up.

## Pre-launch checklist

- [x] ~~Add the VSL video~~ — done, see below
- [ ] Confirm the trades listed in the "Who we work with" marquee
- [ ] Confirm the three service cards describe what you actually deliver
- [ ] Once the site has a domain, change `og:image` / `twitter:image` in the
      `<head>` from `og-image.png` to the absolute URL
- [ ] Check the calendar on the live URL (it can't render in a local file
      preview or a sandboxed viewer — third-party iframes are blocked there)

All internal links were tested: every "Book a Call" button (nav, hero, above the
video, final CTA, footer, sticky mobile bar) scrolls to the calendar, and the
nav/footer links reach their sections clear of the sticky header.

## What you still need to add

### The VSL video

`assets/vsl.mp4` is the supplied office clip with the first and last 2 seconds
trimmed off (55.33s → 51.33s), re-encoded for web with `faststart` so it begins
playing before the whole file downloads. `assets/vsl.webm` is a VP9 copy and
`assets/vsl-poster.jpg` is the still shown before play.

The player emits both sources and lets the browser choose — H.264 plays
everywhere, VP9 covers Chromium builds without proprietary codecs.

To swap the video later, change `CONFIG.video` at the bottom of `index.html`.
It also accepts `type: 'youtube' | 'vimeo' | 'wistia'` with an `id`, if you'd
rather host it externally.

## Editing the copy

All headlines, service cards, steps and FAQ answers are plain HTML in `index.html` —
edit them directly.

## Calendar styling

The **Book a Call** section sits on a deep navy-to-blue gradient (`.booking` in the
stylesheet), with the calendar itself on a white card. The white area *inside* the
calendar is rendered by GoHighLevel in a cross-origin iframe — this page can't restyle
it. Change that in GHL under the calendar's own appearance settings.

## Deploying

The workflows in `.github/workflows/` publish GitHub Pages from the **`gh-pages`**
branch. To publish this page, merge/copy `index.html` onto `gh-pages`, or point
Pages at whichever branch you prefer in **Settings → Pages**.

## Putting the page inside GoHighLevel

`ghl-embed.html` is a build of the same page for a GHL **Custom JS/HTML**
element. It differs from `index.html` in three ways:

- no `<!DOCTYPE>`, `<html>`, `<head>` or `<body>` — GHL pages already have them
- every selector is scoped to `#southline-page`, and a reset neutralises the
  host template's bare element styles (`h1`, `p`, `section`...), which would
  otherwise beat anything the embed merely inherits
- the video paths are placeholders, since the files must be served from GHL's
  Media Library rather than a relative `assets/` folder
- **it needs no JavaScript.** Page builders routinely strip `script` tags from
  custom-code blocks, or run them only on the published page and not in the
  editor. So the video element, the booking iframe and the marquee are all
  plain markup, scroll-reveal is opt-in rather than opt-out, and the script
  that remains only adds polish. Verified by rendering the block with every
  script removed.

Regenerate it after editing `index.html`:

```bash
python3 tools/build-ghl-embed.py
```

## Packaging for a host

To make an upload bundle for Netlify / Vercel / Cloudflare Pages or a cPanel
file manager:

```bash
zip -r southline-site.zip index.html assets og-image.png
```

`index.html` references `assets/` by relative path, so keep that folder beside
it — the HTML alone will load without the video. The zip is gitignored; the
files inside it are tracked individually.

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000
```
