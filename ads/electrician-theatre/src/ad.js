// Southline: Meta ads for electricians. 9:16 motion ad built on Theatre.js (@theatre/core).
// All motion is authored as Theatre keyframes (bezier handles) in code, loaded as project state,
// then the sequence is scrubbed frame by frame by render.mjs. Procedural extras (sparks, grain,
// typing, flicker) are pure functions of time so every frame is deterministic.
import { getProject, createRafDriver } from '@theatre/core'

const W = 1080, H = 1920, FPS = 30
const stage = document.getElementById('stage')

// ---------------------------------------------------------------- keyframe DSL
const EASE = {
  out: [0.16, 1, 0.3, 1],          // expo-ish ease out
  io: [0.65, 0, 0.35, 1],          // ease in-out
  in: [0.7, 0, 0.84, 0],           // ease in
  back: [0.34, 1.56, 0.64, 1],     // overshoot
  soft: [0.25, 0.1, 0.25, 1],
  lin: [0, 0, 1, 1],
}
const TR = {}                                    // objectKey -> prop -> [[t, v, ease]]
const K = key => key.replace(/\//g, '_')            // Theatre treats '/' in object keys as folders, so keep keys flat
const kf = (key, prop, list) => { ((TR[K(key)] ||= {})[prop] ||= []).push(...list) }
const SFX = []                                   // [t, name, gain] -> mixed by mix_audio.py
const sfx = (t, name, gain = 0.6) => SFX.push([+t.toFixed(3), name, gain])

function buildState(length) {
  let id = 0
  const tracksByObject = {}
  for (const [key, props] of Object.entries(TR)) {
    const o = (tracksByObject[key] = { trackIdByPropPath: {}, trackData: {} })
    for (const [prop, raw] of Object.entries(props)) {
      const list = raw.slice().sort((a, b) => a[0] - b[0])
      const kfs = list.map(([t, v, e]) => ({
        id: 'k' + id++, position: +t.toFixed(4), value: v,
        handles: [0.5, 0, 0.5, 1], connectedRight: true, type: e === 'hold' ? 'hold' : 'bezier',
      }))
      list.forEach(([, , e], i) => {
        const c = EASE[e] || EASE.out
        kfs[i].handles[2] = c[0]; kfs[i].handles[3] = c[1]
        if (kfs[i + 1]) { kfs[i + 1].handles[0] = c[2]; kfs[i + 1].handles[1] = c[3] }
      })
      const tid = 't' + id++
      o.trackIdByPropPath[JSON.stringify([prop])] = tid
      o.trackData[tid] = { type: 'BasicKeyframedTrack', __debugName: `${key}:${prop}`, keyframes: kfs }
    }
  }
  return {
    sheetsById: { Ad: { staticOverrides: { byObject: {} },
      sequence: { type: 'PositionalSequence', length, subUnitsPerUnit: FPS, tracksByObject } } },
    definitionVersion: '0.4.0', revisionHistory: [],
  }
}

// ---------------------------------------------------------------- elements
const REG = []          // every animated element -> Theatre sheet object
const PROC = []         // procedural updaters fn(t)
const DEF = { x: 0, y: 0, s: 1, o: 1, r: 0, b: 0, rx: 0, ry: 0, p: 0 }

function E(key, parent, o = {}) {
  const el = document.createElement('div')
  if (o.cls) el.className = o.cls
  if (o.html != null) el.innerHTML = o.html
  if (o.style) Object.assign(el.style, o.style)
  if (o.inline) el.style.display = 'inline-block'
  else { el.classList.add('abs'); el.style.left = (o.cx ?? 540) + 'px'; el.style.top = (o.cy ?? 960) + 'px'; if (!key) el.style.transform = 'translate(-50%,-50%)' }
  parent.appendChild(el)
  const r = { key, el, inline: !!o.inline, fx: o.fx, bob: o.bob, baseFilter: o.filter || '', init: { ...DEF, ...(o.init || {}) } }
  if (key) REG.push(r)
  return r
}

function apply(r, v, t) {
  let y = v.y, x = v.x
  if (r.bob) { y += r.bob[0] * Math.sin(t * r.bob[1] + (r.bob[2] || 0)); x += (r.bob[3] || 0) * Math.cos(t * r.bob[1] * 0.7) }
  const c = r.inline ? '' : 'translate(-50%,-50%) '
  r.el.style.transform = `${c}translate3d(${x.toFixed(2)}px,${y.toFixed(2)}px,0) perspective(1400px) rotateX(${v.rx.toFixed(2)}deg) rotateY(${v.ry.toFixed(2)}deg) rotate(${v.r.toFixed(2)}deg) scale(${v.s.toFixed(4)})`
  const op = Math.max(0, Math.min(1, v.o))
  r.el.style.opacity = op
  r.el.style.visibility = op < 0.002 ? 'hidden' : 'visible'
  const f = (v.b > 0.05 ? `blur(${v.b.toFixed(2)}px) ` : '') + r.baseFilter
  r.el.style.filter = f || 'none'
  if (r.fx) r.fx(r.el, v, t)
}

// a line of text revealed word by word: each word flips up in 3D out of a blur
const GOLDWORDS = []
function line(key, parent, text, o) {
  const { cy, size = 84, weight = 800, cls = '', t0, stagger = 0.06, dur = 0.6, rise = 70, blur = 14, maxw = 960, shineAt } = o
  const ln = E(null, parent, { cls: 'line', cy })
  ln.el.style.fontSize = size + 'px'; ln.el.style.fontWeight = weight
  ln.maxw = maxw; LINES.push(ln)
  const words = text.split(' ')
  words.forEach((w, j) => {
    const k = `${key}/w${j}`
    const r = E(k, ln.el, { inline: true, cls: 'w ' + cls, init: { o: 0 } })
    r.el.textContent = w
    if (j < words.length - 1) ln.el.appendChild(document.createTextNode(' '))
    const s = t0 + j * stagger
    kf(k, 'o', [[s, 0, 'out'], [s + dur * 0.55, 1]])
    kf(k, 'y', [[s, rise, 'out'], [s + dur, 0]])
    kf(k, 'b', [[s, blur, 'out'], [s + dur * 0.75, 0]])
    kf(k, 'rx', [[s, 70, 'out'], [s + dur, 0]])
    kf(k, 's', [[s, 1.06, 'out'], [s + dur, 1]])
    sfx(s + 0.05, 'tick', 0.18)
    if (cls.includes('gold')) GOLDWORDS.push({ el: r.el, t: (shineAt ?? (t0 + words.length * stagger + dur + 0.1)) + j * 0.06 })
  })
  ln.end = t0 + (words.length - 1) * stagger + dur
  return ln
}
const LINES = []
const UNDERLINES = []

// procedural: shine sweep across gold words (a wave, word by word)
PROC.push(t => {
  for (const g of GOLDWORDS) {
    const p = Math.max(0, Math.min(1, (t - g.t) / 0.7))
    g.el.style.backgroundPosition = `${(120 - 140 * p).toFixed(1)}% 0, 0 0`
  }
})

// spark burst: glowing particles fly out, slow, fall, fade
function burst(parent, cx, cy, at, n = 28, reach = 440, seed = 1) {
  let s = seed * 9301
  const rnd = () => ((s = (s * 9301 + 49297) % 233280) / 233280)
  const parts = []
  for (let i = 0; i < n; i++) {
    const d = document.createElement('div'); d.className = 'spark'; const sz = 8 + rnd() * 22
    Object.assign(d.style, { width: sz + 'px', height: sz + 'px', left: '0px', top: '0px', opacity: 0 })
    parent.appendChild(d); parts.push({ d, a: rnd() * Math.PI * 2, v: 0.35 + rnd() * 0.65, sz })
  }
  PROC.push(t => {
    const p = (t - at) / 1.0
    for (const q of parts) {
      if (p <= 0 || p >= 1) { q.d.style.opacity = 0; continue }
      const e = 1 - Math.pow(1 - p, 4), dd = reach * q.v * e
      const x = cx + Math.cos(q.a) * dd - q.sz / 2, y = cy + Math.sin(q.a) * dd * 0.8 + 180 * p * p - q.sz / 2
      q.d.style.transform = `translate(${x}px,${y}px)`; q.d.style.opacity = Math.pow(1 - p, 1.4)
    }
  })
}

// ---------------------------------------------------------------- global background
const BG = E(null, stage, { cx: 540, cy: 960, style: { width: W + 'px', height: H + 'px',
  background: 'radial-gradient(1100px 900px at 78% 18%, rgba(194,117,26,.30), transparent 62%), radial-gradient(1000px 1000px at 12% 88%, rgba(47,166,129,.22), transparent 62%), linear-gradient(180deg,#0e3228,#05120e)' } })
BG.el.style.transform = 'translate(-50%,-50%)'
const ORB = E(null, stage, { cx: 540, cy: 760, style: { width: '900px', height: '900px', borderRadius: '50%',
  background: 'radial-gradient(circle, rgba(229,166,79,.22), rgba(229,166,79,0) 65%)' } })
const GRID = E(null, stage, { cx: 540, cy: 960, style: { width: (W + 108) + 'px', height: (H + 108) + 'px',
  backgroundImage: 'radial-gradient(rgba(255,255,255,.075) 1.7px, transparent 2.2px)', backgroundSize: '54px 54px' } })
const SPARKS = []
{
  let s = 77; const rnd = () => ((s = (s * 9301 + 49297) % 233280) / 233280)
  for (let i = 0; i < 34; i++) {
    const d = document.createElement('div'); d.className = 'spark'; const sz = 6 + rnd() * 16
    Object.assign(d.style, { width: sz + 'px', height: sz + 'px', left: 0, top: 0 }); stage.appendChild(d)
    SPARKS.push({ d, x: rnd() * W, y: rnd() * (H + 120), v: 18 + rnd() * 46, ph: rnd() * 6.28, f: 0.6 + rnd(), sz })
  }
}
const VIGNETTE = E(null, stage, { cx: 540, cy: 960, style: { width: W + 'px', height: H + 'px',
  background: 'radial-gradient(130% 90% at 50% 45%, transparent 55%, rgba(0,0,0,.5) 100%)' } })
PROC.push(t => {
  ORB.el.style.transform = `translate(-50%,-50%) translate(${(300 * Math.sin(t * 0.42)).toFixed(1)}px,${(340 * Math.sin(t * 0.29 + 1)).toFixed(1)}px)`
  GRID.el.style.transform = `translate(-50%,-50%) translate(${(26 * Math.sin(t * 0.31)).toFixed(1)}px,${(-((t * 14) % 54)).toFixed(1)}px)`
  BG.el.style.transform = `translate(-50%,-50%) scale(${1.04 + 0.03 * Math.sin(t * 0.2)})`
  for (const k of SPARKS) {
    const y = ((k.y - k.v * t) % (H + 120) + H + 120) % (H + 120) - 60, x = k.x + 22 * Math.sin(t * k.f + k.ph)
    k.d.style.transform = `translate(${x.toFixed(1)}px,${y.toFixed(1)}px)`
    k.d.style.opacity = (0.2 + 0.5 * (0.5 + 0.5 * Math.sin(t * 3 * k.f + k.ph))).toFixed(3)
  }
})

// ---------------------------------------------------------------- scene layers + transitions
const S = [0, 2.0, 5.0, 9.4, 14.2, 18.2], END = 22.6
const LAYERS = S.map((_, i) => {
  const L = E(`L${i}`, stage, { cls: 'layer', init: { o: i === 0 ? 1 : 0, p: 1 },
    fx: (el, v) => {
      if (v.p < 0.999) { const X = -500 + v.p * 2080; el.style.clipPath = `polygon(0 0, ${X + 300}px 0, ${X - 300}px 1920px, 0 1920px)` }
      else el.style.clipPath = 'none'
    } })
  const C = E(`C${i}`, L.el, { cls: 'cam' })
  const end = i < S.length - 1 ? S[i + 1] + 0.3 : END
  kf(`C${i}`, 's', [[S[i], 1, 'soft'], [end, 1.045]])
  return C.el
})
// gold light-wipe edge
const WIPE = E('WIPE', stage, { cx: 540, cy: 960, init: { o: 0, x: -1040, r: 17.35 }, style: { width: '90px', height: '2400px',
  background: 'linear-gradient(90deg, rgba(255,214,140,0) 0%, rgba(255,214,140,.25) 30%, rgba(255,245,220,1) 50%, rgba(255,214,140,.25) 70%, rgba(255,214,140,0) 100%)',
  boxShadow: '0 0 90px 30px rgba(229,166,79,.45)' } })

function zoomblur(a, b, c) {
  kf(`L${a}`, 'o', [[c - 0.24, 1, 'in'], [c + 0.06, 0]])
  kf(`L${a}`, 's', [[c - 0.24, 1, 'in'], [c + 0.06, 1.16]])
  kf(`L${a}`, 'b', [[c - 0.24, 0, 'in'], [c + 0.06, 26]])
  kf(`L${b}`, 'o', [[c - 0.06, 0, 'out'], [c + 0.24, 1]])
  kf(`L${b}`, 's', [[c - 0.06, 0.88, 'out'], [c + 0.45, 1]])
  kf(`L${b}`, 'b', [[c - 0.06, 20, 'out'], [c + 0.32, 0]])
  sfx(c - 0.25, 'whoosh', 0.55)
}
function lightwipe(a, b, c) {
  const t0 = c - 0.34, t1 = c + 0.12
  kf(`L${b}`, 'o', [[t0 - 0.01, 0, 'lin'], [t0, 1]])
  kf(`L${b}`, 'p', [[t0, 0, 'io'], [t1, 1]])
  kf(`L${a}`, 'o', [[t1, 1, 'lin'], [t1 + 0.01, 0]])
  kf(`L${a}`, 's', [[t0, 1, 'in'], [t1, 1.06]])
  kf(`L${a}`, 'b', [[t0, 0, 'in'], [t1, 6]])
  kf('WIPE', 'o', [[t0 - 0.01, 0, 'lin'], [t0, 1, 'hold'], [t1, 1, 'lin'], [t1 + 0.01, 0]])
  kf('WIPE', 'x', [[t0, -1040, 'io'], [t1, 1040]])
  sfx(t0, 'swish', 0.6); sfx(c - 0.1, 'shimmer', 0.35)
}
zoomblur(0, 1, S[1]); lightwipe(1, 2, S[2]); zoomblur(2, 3, S[3]); lightwipe(3, 4, S[4]); zoomblur(4, 5, S[5])

// ================================================================ 1. HOOK: pattern interrupt
{
  const P = LAYERS[0], T = S[0]
  E(null, P, { cx: 540, cy: 960, style: { width: W + 'px', height: H + 'px', background: 'radial-gradient(120% 70% at 50% 42%, #1a1510, #050505 70%)' } })
  const led = E('h/led', P, { cx: 540, cy: 800, cls: 'led', html: 'STOP BUYING<br>SHARED<br>LEADS.',
    style: { fontSize: '140px', textAlign: 'center', whiteSpace: 'nowrap' }, filter: 'drop-shadow(0 0 16px rgba(255,190,90,.55))',
    fx: (el, v, t) => { if (t < T + 0.34) el.style.opacity = (0.35 + 0.65 * (Math.floor((t - T) * 40) % 2)).toFixed(2) } })
  kf('h/led', 's', [[T, 1.22, 'out'], [T + 0.55, 1]])
  kf('h/led', 'x', [[T, -14, 'lin'], [T + 0.05, 12, 'lin'], [T + 0.1, -6, 'lin'], [T + 0.15, 0]])
  kf('h/led', 'b', [[T, 8, 'out'], [T + 0.2, 0]])
  // chromatic ghost
  const ghost = E('h/ghost', P, { cx: 540, cy: 800, cls: 'led', html: 'STOP BUYING<br>SHARED<br>LEADS.',
    style: { fontSize: '140px', textAlign: 'center', whiteSpace: 'nowrap', backgroundImage: 'radial-gradient(circle, #ff4b6b 0 3.1px, transparent 3.7px)', mixBlendMode: 'screen' }, init: { o: 0 } })
  kf('h/ghost', 'o', [[T, 0.7, 'out'], [T + 0.45, 0]]); kf('h/ghost', 'x', [[T, 16, 'out'], [T + 0.45, 0]])
  E(null, P, { cx: 540, cy: 960, style: { width: W + 'px', height: H + 'px', pointerEvents: 'none',
    background: 'repeating-linear-gradient(0deg, rgba(0,0,0,.18) 0 2px, transparent 2px 5px)' } })
  burst(P, 540, 800, T + 0.04, 30, 520, 3)
  line('h/l1', P, 'Electricians,', { cy: 1300, size: 108, weight: 900, cls: 'gold', t0: T + 0.42, stagger: 0.08 })
  line('h/l2', P, 'watch this first.', { cy: 1425, size: 74, weight: 800, t0: T + 0.6, stagger: 0.07 })
  sfx(T, 'glitch', 0.8); sfx(T + 0.04, 'hit', 1.0); sfx(T + 0.42, 'whoosh', 0.45)
}

// ================================================================ 2. OPEN LOOP
{
  const P = LAYERS[1], T = S[1]
  line('q/l1', P, 'Why does one sparky', { cy: 700, size: 86, weight: 800, t0: T + 0.05 })
  const l2 = line('q/l2', P, 'only quote big jobs…', { cy: 825, size: 108, weight: 900, cls: 'gold', t0: T + 0.42 })
  line('q/l3', P, 'while you price sockets?', { cy: 950, size: 82, weight: 800, cls: 'muted', t0: T + 0.85 })
  const ul = E('q/ul', P, { cx: 540, cy: 900, style: { width: '900px', height: '12px', borderRadius: '6px', transformOrigin: 'left center',
    background: 'linear-gradient(90deg,#e5a64f,#ffd896)', boxShadow: '0 0 24px rgba(229,166,79,.6)' }, init: { o: 0 },
    fx: (el, v) => { el.style.transform += ` scaleX(${v.p.toFixed(4)})` } })
  UNDERLINES.push([ul, l2])
  kf('q/ul', 'o', [[T + 0.95, 0, 'lin'], [T + 0.96, 1]]); kf('q/ul', 'p', [[T + 0.96, 0, 'out'], [T + 1.4, 1]])
  const pill = E('q/pill', P, { cx: 540, cy: 1150, cls: 'pill glass shine', html: 'The answer’s simpler than you think',
    style: { fontSize: '38px', fontWeight: 700 }, init: { o: 0 },
    fx: (el, v, t) => el.style.setProperty('--shp', (130 - 160 * Math.max(0, Math.min(1, (t - T - 2.1) / 0.8))) + '%') })
  kf('q/pill', 'o', [[T + 1.6, 0, 'out'], [T + 1.85, 1]]); kf('q/pill', 's', [[T + 1.6, 0.6, 'back'], [T + 2.1, 1]])
  kf('q/pill', 'y', [[T + 1.6, 40, 'out'], [T + 2.1, 0]])
  sfx(T + 0.05, 'hit', 0.8); sfx(T + 0.42, 'whoosh', 0.4); sfx(T + 0.96, 'swish', 0.4); sfx(T + 1.6, 'pop', 0.8)
}

// ================================================================ 3. RELATE: the late-night quoting thread
{
  const P = LAYERS[2], T = S[2]
  line('r/l1', P, '9:47pm. Still quoting.', { cy: 330, size: 86, weight: 800, t0: T + 0.05 })
  line('r/l2', P, 'Sound familiar?', { cy: 450, size: 112, weight: 900, cls: 'gold', t0: T + 0.3 })
  const msgs = [['How much to move one socket?', false, 0.75], ['€90. Can do Thursday.', true, 1.45],
                ['Ah. Got someone for €60.', false, 2.15], ['Just wanted a ballpark tbh', false, 2.8]]
  msgs.forEach(([m, out, ta], i) => {
    const y = 660 + i * 142, k = `r/b${i}`
    const b = E(k, P, { cls: 'bubble ' + (out ? 'out' : 'in'), html: m, init: { o: 0 } })
    b.el.style.top = y + 'px'
    if (out) { b.el.style.left = 'auto'; b.el.style.right = '70px' } else b.el.style.left = '70px'
    b.inline = true; b.el.style.position = 'absolute'; b.el.style.transform = 'none'; b.el.style.marginTop = '-56px'
    const T0 = T + ta
    kf(k, 'o', [[T0, 0, 'out'], [T0 + 0.15, 1]]); kf(k, 's', [[T0, 0.55, 'back'], [T0 + 0.5, 1]])
    kf(k, 'y', [[T0, 40, 'out'], [T0 + 0.45, 0]]); kf(k, 'r', [[T0, out ? 5 : -5, 'out'], [T0 + 0.5, 0]])
    sfx(T0, out ? 'swish' : 'pop', 0.65)
    if (!out) {
      const tk = `r/t${i}`
      const ty = E(tk, P, { cls: 'bubble in', html: '<span class="dot"></span><span class="dot"></span><span class="dot"></span>', init: { o: 0 },
        style: { padding: '0 34px' },
        fx: (el, v, t) => { [...el.children].forEach((d, j) => { d.style.transform = `translateY(${(-9 * Math.max(0, Math.sin(t * 12 - j * 0.9))).toFixed(1)}px)` }) } })
      ty.inline = true; ty.el.style.position = 'absolute'; ty.el.style.left = '70px'; ty.el.style.top = y + 'px'; ty.el.style.marginTop = '-56px'
      kf(tk, 'o', [[T0 - 0.45, 0, 'out'], [T0 - 0.35, 1, 'hold'], [T0 - 0.02, 1, 'lin'], [T0, 0]])
      kf(tk, 's', [[T0 - 0.45, 0.6, 'back'], [T0 - 0.2, 1]])
    }
  })
  const vt = T + 3.45
  const v = E('r/v', P, { cx: 540, cy: 660 + 4 * 142 + 90, cls: 'pill', html: 'Another unpaid evening.',
    style: { fontSize: '46px', fontWeight: 800, background: '#e84848', color: '#fff', boxShadow: '0 18px 44px -14px rgba(232,72,72,.7)' }, init: { o: 0 } })
  kf('r/v', 'o', [[vt, 0, 'out'], [vt + 0.12, 1]]); kf('r/v', 's', [[vt, 1.5, 'out'], [vt + 0.35, 1]])
  kf('r/v', 'x', [[vt + 0.12, 0, 'lin'], [vt + 0.17, -14, 'lin'], [vt + 0.22, 12, 'lin'], [vt + 0.27, -6, 'lin'], [vt + 0.32, 0]])
  sfx(vt + 0.05, 'hit', 0.9)
}

// ================================================================ 4. BODY: the lead filter (answers the open loop)
{
  const P = LAYERS[3], T = S[3]
  line('f/l1', P, 'The difference?', { cy: 330, size: 86, weight: 800, t0: T + 0.05 })
  line('f/l2', P, 'Their leads get filtered.', { cy: 450, size: 104, weight: 900, cls: 'gold', t0: T + 0.3 })
  // funnel (SVG) that draws itself on
  const fun = E('f/fun', P, { cx: 540, cy: 930, init: { p: 0 }, filter: 'drop-shadow(0 0 18px rgba(229,166,79,.55))',
    html: `<svg width="720" height="400" viewBox="0 0 720 400"><defs><linearGradient id="ff" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#e5a64f" stop-opacity=".22"/><stop offset="1" stop-color="#e5a64f" stop-opacity=".04"/></linearGradient></defs>
      <path id="fp" d="M30 20 H690 L430 300 V380 H290 V300 Z" fill="url(#ff)" stroke="#f0b45a" stroke-width="6" stroke-linejoin="round"/></svg>`,
    fx: (el, v) => { const p = el.querySelector('#fp'); const L = 2200; p.style.strokeDasharray = L; p.style.strokeDashoffset = (L * (1 - v.p)).toFixed(1); p.style.fillOpacity = v.p } })
  kf('f/fun', 'p', [[T + 0.2, 0, 'io'], [T + 0.9, 1]])
  const spout = E('f/glow', P, { cx: 540, cy: 1110, style: { width: '420px', height: '420px', borderRadius: '50%',
    background: 'radial-gradient(circle, rgba(255,214,140,.75), rgba(229,166,79,.25) 35%, rgba(229,166,79,0) 68%)' }, init: { o: 0 } })
  const chips = [['Full rewire', 1], ['Move a socket', 0], ['EV charger', 1], ['Cheapest price?', 0],
                 ['Just a ballpark', 0], ['Solar PV', 1], ['Fuse board', 1], ['40km away', 0]]
  const XO = [-150, 140, -70, 180, -180, 70, 150, -110]
  const slots = [[320, 1250], [760, 1250], [320, 1375], [760, 1375]]
  let gi = 0; const glowK = []
  chips.forEach(([label, good], i) => {
    const k = `f/c${i}`, t0 = T + 0.95 + i * 0.36, x0 = XO[i]
    E(k, P, { cx: 540, cy: 560, cls: 'chip ' + (good ? 'good' : 'bad'), html: label, init: { o: 0 } })
    kf(k, 'o', [[t0, 0, 'out'], [t0 + 0.1, 1]])
    kf(k, 'x', [[t0, x0, 'io']]); kf(k, 'y', [[t0, 0, 'in']])
    if (!good) {
      const dir = x0 >= 0 ? 1 : -1
      kf(k, 'x', [[t0 + 0.36, x0, 'out'], [t0 + 0.95, x0 + dir * 520]])
      kf(k, 'y', [[t0 + 0.36, 240, 'out'], [t0 + 0.55, 150, 'in'], [t0 + 0.95, 520]])
      kf(k, 'r', [[t0 + 0.36, 0, 'out'], [t0 + 0.95, dir * 70]])
      kf(k, 'o', [[t0 + 0.6, 1, 'in'], [t0 + 0.95, 0]])
      sfx(t0 + 0.36, 'click', 0.85)
    } else {
      const [sx, sy] = slots[gi++]
      kf(k, 'x', [[t0 + 0.36, x0, 'io'], [t0 + 0.66, 0, 'out'], [t0 + 1.1, sx - 540]])
      kf(k, 'y', [[t0 + 0.36, 240, 'io'], [t0 + 0.66, 540, 'back'], [t0 + 1.1, sy - 560]])
      kf(k, 's', [[t0 + 0.36, 1, 'io'], [t0 + 0.66, 0.7, 'back'], [t0 + 1.1, 1]])
      glowK.push(t0 + 0.6)
      sfx(t0 + 0.6, 'pop', 0.7); sfx(t0 + 0.95, 'coin', 0.5)
    }
  })
  glowK.forEach(g => kf('f/glow', 'o', [[g - 0.05, 0, 'out'], [g + 0.05, 1, 'out'], [g + 0.45, 0]]))
  glowK.forEach((g, i) => kf('f/glow', 's', [[g - 0.05, 0.6, 'out'], [g + 0.45, 1.25 + 0.0001 * i]]))
  line('f/l3', P, 'Only real jobs reach the phone.', { cy: 1530, size: 70, weight: 800, t0: T + 4.05, stagger: 0.05 })
  sfx(T + 0.2, 'swish', 0.5); sfx(T + 4.05, 'shimmer', 0.7)
}

// ================================================================ 5. SOLUTION: what Southline builds
{
  const P = LAYERS[4], T = S[4]
  line('s/l1', P, 'We build it for you.', { cy: 300, size: 84, weight: 800, t0: T + 0.05 })
  const cards = [['Your Meta ads', 'Big jobs', 'Rewires · EV · solar PV', 'cream', 390, 650, -4],
                 ['Every lead', 'Filtered', 'Job, area, timing checked', 'goldfill', 690, 1040, 3],
                 ['Straight to', 'Your phone', 'Name, number, job', 'cream', 420, 1430, -2]]
  cards.forEach(([lab, big, sm, cls, cx, cy, ang], i) => {
    const k = `s/c${i}`, t0 = T + 0.45 + i * 0.5, from = i % 2 ? 1 : -1
    E(k, P, { cx, cy, cls: 'card ' + cls + (i === 1 ? ' shine' : ''), html: `<div class="lab">${lab}</div><div class="big">${big}</div><div class="sm">${sm}</div>`,
      init: { o: 0, r: ang }, bob: [9, 2.0, i * 1.7, 4],
      fx: i === 1 ? (el, v, t) => el.style.setProperty('--shp', (130 - 160 * Math.max(0, Math.min(1, (t - t0 - 0.9) / 0.9))) + '%') : null })
    kf(k, 'o', [[t0, 0, 'out'], [t0 + 0.2, 1]])
    kf(k, 'x', [[t0, from * 380, 'out'], [t0 + 0.7, 0]])
    kf(k, 'ry', [[t0, from * -55, 'out'], [t0 + 0.8, 0]])
    kf(k, 'rx', [[t0, 25, 'out'], [t0 + 0.8, 0]])
    kf(k, 's', [[t0, 0.75, 'back'], [t0 + 0.7, 1]])
    kf(k, 'r', [[t0, ang * 4, 'out'], [t0 + 0.8, ang]])
    sfx(t0, 'whoosh', 0.4); sfx(t0 + 0.3, 'pop', 0.7)
  })
}

// ================================================================ 6. CTA: comment QUALITY
{
  const P = LAYERS[5], T = S[5]
  line('k/l1', P, 'Want leads worth', { cy: 430, size: 86, weight: 800, t0: T + 0.05 })
  line('k/l2', P, 'the drive?', { cy: 540, size: 104, weight: 900, cls: 'gold', t0: T + 0.25 })
  const row = E('k/row', P, { cx: 540, cy: 760, style: { display: 'flex', alignItems: 'center', gap: '26px', whiteSpace: 'nowrap' }, init: { o: 0 } })
  row.el.innerHTML = '<span style="font-size:94px;font-weight:800">Comment</span>'
  kf('k/row', 'o', [[T + 0.45, 0, 'out'], [T + 0.7, 1]]); kf('k/row', 'y', [[T + 0.45, 40, 'out'], [T + 0.8, 0]])
  const kw = E('k/kw', row.el, { inline: true, cls: 'pill goldfill shine', html: 'QUALITY',
    style: { fontSize: '62px', fontWeight: 900, letterSpacing: '.02em', position: 'relative', display: 'inline-flex' }, init: { o: 0 },
    bob: null,
    fx: (el, v, t) => {
      const pulse = t > T + 1.2 ? 1 + 0.035 * Math.sin((t - T - 1.2) * 6) : 1
      el.style.transform += ` scale(${pulse.toFixed(4)})`
      el.style.setProperty('--shp', (130 - 160 * (((t - T - 1.1) % 1.8 + 1.8) % 1.8 / 0.9)) + '%')
    } })
  kf('k/kw', 'o', [[T + 0.55, 0, 'out'], [T + 0.7, 1]]); kf('k/kw', 's', [[T + 0.55, 0.4, 'back'], [T + 1.05, 1]])
  kf('k/kw', 'r', [[T + 0.55, -8, 'back'], [T + 1.05, 0]])
  burst(P, 760, 760, T + 0.62, 24, 360, 7)
  line('k/l3', P, 'to learn more.', { cy: 890, size: 92, weight: 800, t0: T + 0.75 })
  // comment box with typing
  const TY = T + 1.35, CH = 0.1, KW = 'QUALITY', PT = TY + KW.length * CH + 0.35
  const box = E('k/box', P, { cx: 540, cy: 1160, init: { o: 0 },
    style: { width: '900px', height: '150px', borderRadius: '75px', background: '#fff', boxShadow: '0 24px 60px -24px rgba(0,0,0,.8)',
             display: 'flex', alignItems: 'center', boxSizing: 'border-box', padding: '0 46px 0 24px', color: '#111' },
    html: `<div style="width:100px;height:100px;border-radius:50%;background:#e6e2da;flex:none;position:relative;overflow:hidden">
             <div style="position:absolute;left:32px;top:18px;width:36px;height:36px;border-radius:50%;background:#bdb8ae"></div>
             <div style="position:absolute;left:14px;top:60px;width:72px;height:60px;border-radius:50%;background:#bdb8ae"></div></div>
           <div class="typed" style="flex:1;margin-left:36px;font-size:52px;font-weight:700;display:flex;align-items:center"></div>
           <div class="post" style="font-size:46px;font-weight:800">Post</div>`,
    fx: (el, v, t) => {
      const n = Math.max(0, Math.min(KW.length, Math.floor((t - TY) / CH) + 1)), posted = t >= PT + 0.08
      const typed = el.querySelector('.typed'), caret = !posted && (t < TY + 0.9 || Math.floor(t * 3) % 2 === 0)
      const txt = posted || t < TY ? '' : KW.slice(0, n)
      typed.innerHTML = txt ? `${txt}${caret ? '<span style="display:inline-block;width:5px;height:60px;background:#e5a64f;margin-left:6px"></span>' : ''}`
        : `<span style="color:#a09c94;font-weight:500;font-size:44px">Add a comment…</span>`
      el.querySelector('.post').style.color = txt ? '#d4912f' : '#cbc7c0'
    } })
  kf('k/box', 'o', [[T + 0.95, 0, 'out'], [T + 1.15, 1]]); kf('k/box', 'y', [[T + 0.95, 70, 'out'], [T + 1.4, 0]])
  kf('k/box', 's', [[T + 0.95, 0.94, 'out'], [T + 1.4, 1, 'out'], [PT - 0.02, 1, 'out'], [PT + 0.06, 0.97, 'out'], [PT + 0.25, 1]])
  for (let i = 0; i < KW.length; i++) sfx(TY + i * CH, 'tick', 0.5)
  // finger + ripple
  E('k/tap', P, { cx: 915, cy: 1160, init: { o: 0 }, style: { width: '68px', height: '68px', borderRadius: '50%', background: 'rgba(255,255,255,.9)',
    border: '3px solid rgba(20,20,20,.35)', boxShadow: '0 10px 24px rgba(0,0,0,.4)' } })
  kf('k/tap', 'o', [[PT - 0.55, 0, 'out'], [PT - 0.4, 1, 'hold'], [PT + 0.3, 1, 'out'], [PT + 0.55, 0]])
  kf('k/tap', 'x', [[PT - 0.55, 130, 'out'], [PT - 0.05, 0]]); kf('k/tap', 'y', [[PT - 0.55, 340, 'out'], [PT - 0.05, 0]])
  kf('k/tap', 's', [[PT - 0.05, 1, 'out'], [PT + 0.02, 0.8, 'out'], [PT + 0.2, 1]])
  E('k/rip', P, { cx: 915, cy: 1160, init: { o: 0 }, style: { width: '80px', height: '80px', borderRadius: '50%', border: '5px solid #ffd896' } })
  kf('k/rip', 'o', [[PT, 0.9, 'out'], [PT + 0.6, 0]]); kf('k/rip', 's', [[PT, 0.4, 'out'], [PT + 0.6, 3.2]])
  // toast
  E('k/toast', P, { cx: 540, cy: 1335, cls: 'pill', init: { o: 0 },
    style: { fontSize: '40px', background: '#111', color: '#fff', gap: '18px', boxShadow: '0 18px 40px -16px rgba(0,0,0,.8)' },
    html: '<span style="width:44px;height:44px;border-radius:50%;background:#22aa5c;display:inline-flex;align-items:center;justify-content:center;font-size:28px">✓</span>We’ll DM you the details' })
  kf('k/toast', 'o', [[PT + 0.12, 0, 'out'], [PT + 0.3, 1]]); kf('k/toast', 'y', [[PT + 0.12, 50, 'out'], [PT + 0.55, 0]])
  kf('k/toast', 's', [[PT + 0.12, 0.85, 'back'], [PT + 0.55, 1]])
  sfx(PT, 'click', 1.0); sfx(PT + 0.15, 'ping', 0.6)
  // brand
  E('k/brand', P, { cx: 540, cy: 1560, init: { o: 0 }, html: '<div style="font-size:66px;font-weight:900;letter-spacing:.02em;text-align:center">SOUTHLINE</div><div style="font-size:38px;font-weight:500;color:#a0bcaf;text-align:center;margin-top:4px">Meta ads for electricians</div>' })
  kf('k/brand', 'o', [[T + 1.1, 0, 'out'], [T + 1.5, 1]]); kf('k/brand', 'y', [[T + 1.1, 30, 'out'], [T + 1.6, 0]])
  sfx(T + 0.05, 'whoosh', 0.5); sfx(T + 0.55, 'pop', 0.85); sfx(T + 0.62, 'shimmer', 0.5)
}

// ---------------------------------------------------------------- Theatre project
const project = getProject('Southline Electricians', { state: buildState(END) })
const sheet = project.sheet('Ad')
const driver = createRafDriver({ name: 'frame-stepper' })     // we tick it manually, one tick per rendered frame
for (const r of REG) { r.obj = sheet.object(K(r.key), r.init); r.v = { ...r.init }; r.obj.onValuesChange(v => { r.v = v }, driver) }

function seek(t) {
  sheet.sequence.position = t
  driver.tick(performance.now())
  for (const r of REG) apply(r, r.v, t)
  for (const f of PROC) f(t)
  // grain: jitter the noise tile every frame
  GRAIN.style.backgroundPosition = `${(Math.sin(t * 977) * 400) | 0}px ${(Math.cos(t * 613) * 400) | 0}px`
}

// film grain overlay
const GRAIN = document.createElement('div')
{
  const c = document.createElement('canvas'); c.width = c.height = 256; const g = c.getContext('2d'); const im = g.createImageData(256, 256)
  let s = 5; for (let i = 0; i < im.data.length; i += 4) { s = (s * 16807) % 2147483647; const v = s % 256; im.data[i] = im.data[i + 1] = im.data[i + 2] = v; im.data[i + 3] = 255 }
  g.putImageData(im, 0, 0)
  Object.assign(GRAIN.style, { position: 'absolute', inset: 0, backgroundImage: `url(${c.toDataURL()})`, opacity: 0.06, mixBlendMode: 'overlay', pointerEvents: 'none' })
  stage.appendChild(GRAIN)
}
stage.insertBefore(VIGNETTE.el, LAYERS[0].parentElement)

window.AD = { seek, DURATION: END, FPS, SFX, ready: false }
Promise.all([project.ready, document.fonts.ready]).then(() => {
  for (const ln of LINES) {                       // fit lines to the safe width
    let size = parseFloat(ln.el.style.fontSize)
    while (ln.el.offsetWidth > ln.maxw && size > 30) { size -= 2; ln.el.style.fontSize = size + 'px' }
    ln.el.style.transform = 'translate(-50%,-50%)'
  }
  for (const [ul, ln] of UNDERLINES) {            // size underline to its line, sit it under the text
    ul.el.style.width = ln.el.offsetWidth + 'px'
    ul.el.style.top = (parseFloat(ln.el.style.top) + ln.el.offsetHeight / 2 + 4) + 'px'
  }
  seek(0)
  window.AD.ready = true
})
