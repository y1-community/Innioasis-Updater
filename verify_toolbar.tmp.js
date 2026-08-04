const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({ executablePath: process.env.CHROME_PATH, args: ['--no-sandbox'] });
  const page = await browser.newPage();
  await page.setViewport({ width: 1280, height: 900 });
  const errors = [];
  page.on('pageerror', e => errors.push(String(e)));
  await page.goto('http://localhost:8899/index.html', { waitUntil: 'networkidle0' });
  await new Promise(r => setTimeout(r, 800));

  const base = await page.evaluate(() => {
    const bar = document.querySelector('.y1-site-dock-bar');
    const links = Array.from(bar.querySelectorAll('.y1-dock-link')).map(l => ({
      text: l.textContent.trim(),
      tag: l.tagName,
      hasIcon: !!l.querySelector('svg.y1-dock-icon')
    }));
    const seps = bar.querySelectorAll('.y1-dock-sep').length;
    const privacyPanel = document.getElementById('y1-privacy-panel');
    return { links, seps, privacyHidden: privacyPanel ? privacyPanel.hidden : 'MISSING', privacyHtml: privacyPanel ? privacyPanel.querySelector('.y1-privacy-body').textContent.trim() : '' };
  });

  // Click Privacy: panel opens, donate closes
  const clickResult = await page.evaluate(() => {
    const open = document.querySelector('[data-privacy-open]');
    open.click();
    const pp = document.getElementById('y1-privacy-panel');
    const dp = document.getElementById('y1-donate-panel');
    return {
      privacyOpen: !pp.hidden && pp.classList.contains('is-open'),
      donateClosed: dp.hidden,
      expanded: open.getAttribute('aria-expanded'),
      focusOnClose: document.activeElement === document.querySelector('[data-privacy-close]')
    };
  });

  // Escape closes
  const escResult = await page.evaluate(() => {
    document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
    return document.getElementById('y1-privacy-panel').hidden;
  });

  // 2077 theme translations
  await page.evaluate(() => { document.documentElement.setAttribute('data-lumen-theme', '2077'); });
  await new Promise(r => setTimeout(r, 400));
  const night = await page.evaluate(() => {
    const open = document.querySelector('[data-privacy-open]');
    open.click();
    return {
      dockText: Array.from(document.querySelectorAll('.y1-dock-link')).map(l => l.textContent.trim()),
      panelTitle: document.getElementById('y1-privacy-title').textContent.trim(),
      panelBody: document.getElementById('y1-privacy-panel').querySelector('.y1-privacy-body').textContent.trim()
    };
  });

  console.log(JSON.stringify({ base, clickResult, escResult, night, errors }, null, 2));
  await browser.close();
})();
