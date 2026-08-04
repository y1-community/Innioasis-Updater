const puppeteer = require('puppeteer');
const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = process.cwd();
const MIME = { '.html': 'text/html', '.js': 'text/javascript', '.css': 'text/css', '.png': 'image/png', '.ini': 'text/plain', '.xml': 'text/xml' };
const server = http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]);
  if (p === '/') p = '/index.html';
  const f = path.join(ROOT, p);
  if (!f.startsWith(ROOT)) { res.writeHead(403); res.end(); return; }
  fs.readFile(f, (err, d) => {
    if (err) { res.writeHead(404); res.end(); return; }
    res.writeHead(200, { 'Content-Type': MIME[path.extname(f)] || 'application/octet-stream', 'Cache-Control': 'no-store' });
    res.end(d);
  });
});

(async () => {
  await new Promise(r => server.listen(8899, r));
  const browser = await puppeteer.launch({ executablePath: process.env.CHROME_PATH || '/usr/bin/chromium', args: ['--no-sandbox'] });
  async function probe(width, height, label) {
    const page = await browser.newPage();
    await page.setViewport({ width, height });
    await page.goto('http://localhost:8899/index.html', { waitUntil: 'networkidle0' });
    const out = await page.evaluate(() => {
      const hero = document.querySelector('.lumen-hero');
      const textCol = hero.querySelector('div');
      const art = document.querySelector('.lumen-hero-art');
      const actions = document.querySelector('.lumen-hero .lumen-actions');
      const buttons = Array.from(actions.querySelectorAll('a, button'));
      const hr = hero.getBoundingClientRect();
      const tr = textCol.getBoundingClientRect();
      const ar = art.getBoundingClientRect();
      return {
        heroW: Math.round(hr.width),
        textW: Math.round(tr.width),
        artW: Math.round(ar.width),
        artH: Math.round(ar.height),
        artAspect: (ar.width / ar.height).toFixed(2),
        actionsW: Math.round(actions.getBoundingClientRect().width),
        buttonsW: buttons.map(b => Math.round(b.getBoundingClientRect().width)),
        buttonsOnOneLine: (() => {
          const tops = buttons.map(b => Math.round(b.getBoundingClientRect().top));
          return new Set(tops).size === 1;
        })(),
        buttonsRows: new Set(buttons.map(b => Math.round(b.getBoundingClientRect().top))).size
      };
    });
    console.log(label, JSON.stringify(out));
    await page.close();
  }
  await probe(1440, 900, 'desktop-1440');
  await probe(1280, 720, 'landscape-720p');
  await probe(1080, 1920, 'portrait-1080');
  await probe(830, 1920, 'portrait-sidebar');
  await probe(760, 1280, 'tablet-760');
  await browser.close();
  server.close();
})().catch(e => { console.error('FAIL', e.message); server.close(); process.exit(1); });
