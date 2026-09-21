# RELIER — Landing Page

A single-file VSL funnel landing page. No build step, no dependencies.

**Page order:** VSL video → Book a Call → What we do → How it works → Calendar → FAQ → Final CTA.

Blue-and-white theme with motion throughout: animated gradient background, word-by-word
headline entrance, scroll-progress bar, scroll-reveal sections, count-up stats, a looping
logo marquee, shimmer on the primary button and hover lifts on every card. All of it is
disabled automatically for visitors with `prefers-reduced-motion`.

## What's already connected

The GoHighLevel calendar is live — `CONFIG.booking.url` points at
`https://api.leadconnectorhq.com/widget/booking/Jyy3OGmnlXllDOv1VZz6` and renders
inline in the **Book a Call** section. Every "Book a Call" button scrolls to it.

Set `mode: 'redirect'` instead if you'd rather the buttons open the booking page in a
new tab — the inline section is then removed automatically.

## What you still need to add

### 1. Your VSL video

In the `CONFIG` object at the bottom of `index.html`:

```js
video: {
  type:   'youtube',   // 'youtube' | 'vimeo' | 'wistia' | 'mp4' | 'embed'
  id:     'dQw4w9WgXcQ',
  src:    '',          // full URL — only for 'mp4' or 'embed'
  poster: ''           // optional thumbnail image shown before play
}
```

The player shows a click-to-play poster first, then loads the video with autoplay —
standard VSL behaviour, and it keeps the page fast.

### 2. Real numbers in the stats row

The four stats under "What we do" (`312%`, `14 days`, `5 min`, `94%`) are
**placeholders**. Replace them with your own figures — or delete the `.stats` block —
before the page goes live.

## Editing the copy

All headlines, service cards, steps and FAQ answers are plain HTML in `index.html` —
edit them directly. The placeholder copy is written for a generic acquisition/agency
offer; swap it for your own.

## Deploying

The workflows in `.github/workflows/` publish GitHub Pages from the **`gh-pages`**
branch. To publish this page, merge/copy `index.html` onto `gh-pages`, or point
Pages at whichever branch you prefer in **Settings → Pages**.

## Local preview

```bash
python3 -m http.server 8000
# open http://localhost:8000
```
