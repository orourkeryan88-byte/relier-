// Render the Theatre.js ad to MP4: bundle -> serve -> scrub sequence per frame in headless Chromium -> ffmpeg.
// usage: node render.mjs                 full render  -> southline_electricians_theatre.mp4
//        node render.mjs --stills 1.7,4.6  only grab stills -> stills/*.png (fast QA)
import { build } from 'esbuild'
import http from 'node:http'
import fs from 'node:fs'
import path from 'node:path'
import { spawn, execFileSync } from 'node:child_process'
import { createRequire } from 'node:module'
const require = createRequire(import.meta.url)
const { chromium } = require('playwright')

const ROOT = path.dirname(new URL(import.meta.url).pathname)
const OUT = path.join(ROOT, 'southline_electricians_theatre.mp4')
const args = process.argv.slice(2)
const stills = args[0] === '--stills' ? args[1].split(',').map(Number) : null

await build({ entryPoints: [path.join(ROOT, 'src/ad.js')], bundle: true, format: 'iife', outfile: path.join(ROOT, 'bundle.js'),
  define: { 'process.env.NODE_ENV': '"production"' }, logLevel: 'warning' })

const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.otf': 'font/otf' }
const server = http.createServer((req, res) => {
  const f = path.join(ROOT, decodeURIComponent(req.url.split('?')[0]) === '/' ? 'index.html' : decodeURIComponent(req.url.split('?')[0]))
  fs.readFile(f, (err, data) => { if (err) { res.writeHead(404); res.end() } else { res.writeHead(200, { 'Content-Type': MIME[path.extname(f)] || 'application/octet-stream' }); res.end(data) } })
}).listen(0)
const url = `http://127.0.0.1:${server.address().port}/`

const browser = await chromium.launch()
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 })
page.on('pageerror', e => { console.error('PAGE ERROR', e.message); process.exitCode = 1 })
page.on('console', m => { if (m.type() === 'error') console.error('console:', m.text()) })
await page.goto(url)
await page.waitForFunction(() => window.AD && window.AD.ready, null, { timeout: 30000 })
const { DURATION, FPS, SFX } = await page.evaluate(() => ({ DURATION: AD.DURATION, FPS: AD.FPS, SFX: AD.SFX }))

if (stills) {
  fs.mkdirSync(path.join(ROOT, 'stills'), { recursive: true })
  for (const t of stills) {
    await page.evaluate(t => AD.seek(t), t)
    await page.screenshot({ path: path.join(ROOT, 'stills', `${t.toFixed(2)}.png`) })
  }
  console.log('stills done')
} else {
  const n = Math.round(DURATION * FPS)
  const silent = path.join(ROOT, '_video.mp4')
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
    '-c:v', 'libx264', '-preset', 'medium', '-crf', '16', '-pix_fmt', 'yuv420p', silent], { stdio: ['pipe', 'inherit', 'inherit'] })
  const t0 = Date.now()
  for (let i = 0; i < n; i++) {
    await page.evaluate(t => AD.seek(t), i / FPS)
    const buf = await page.screenshot({ type: 'jpeg', quality: 95 })
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r))
    if (i % 90 === 0) console.log(`frame ${i}/${n}  ${((Date.now() - t0) / 1000).toFixed(0)}s`)
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r))
  fs.writeFileSync(path.join(ROOT, 'sfx.json'), JSON.stringify({ duration: n / FPS, events: SFX }))
  execFileSync('python3', [path.join(ROOT, 'mix_audio.py'), path.join(ROOT, 'sfx.json'), path.join(ROOT, '_audio.wav')], { stdio: 'inherit' })
  execFileSync('ffmpeg', ['-y', '-loglevel', 'error', '-i', silent, '-i', path.join(ROOT, '_audio.wav'), '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k',
    '-shortest', '-movflags', '+faststart', OUT], { stdio: 'inherit' })
  fs.rmSync(silent); fs.rmSync(path.join(ROOT, '_audio.wav'))
  console.log('wrote', OUT)
}
await browser.close(); server.close()
