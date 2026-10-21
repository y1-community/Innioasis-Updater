import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage']
  });

  const page = await browser.newPage();
  const consoleMessages = [];
  page.on('console', msg => consoleMessages.push({ type: msg.type(), text: msg.text() }));
  page.on('pageerror', err => consoleMessages.push({ type: 'pageerror', text: err.message }));

  await page.goto('http://localhost:8000/firmware.html', { waitUntil: 'networkidle0' });

  // Click the zip download button on the first row
  await page.waitForSelector('.lumen-zip-download-button');
  await page.evaluate(() => document.querySelector('.lumen-zip-download-button').click());
  console.log('Clicked zip download button');

  // Check progress element visibility
  await new Promise(r => setTimeout(r, 600));
  const progressState = await page.evaluate(() => {
    const wrap = document.getElementById('lumen-download-progress-wrap');
    const label = document.getElementById('lumen-download-progress-label');
    const metrics = document.getElementById('lumen-download-progress-metrics');
    return {
      visible: wrap && !wrap.hidden,
      labelText: label ? label.textContent : null,
      metricsText: metrics ? metrics.textContent : null
    };
  });
  console.log('Progress state:', progressState);
  console.log('Console logs during click:', consoleMessages);

  // Test dismiss button behavior on completion
  console.log('Testing markCompleted and dismiss checkmark button persistence...');
  await page.evaluate(() => {
    const wrap = document.getElementById('lumen-download-progress-wrap');
    const label = document.getElementById('lumen-download-progress-label');
    const dismissBtn = document.getElementById('lumen-download-progress-dismiss');
    label.textContent = "Saved to downloads";
    dismissBtn.hidden = false;
    dismissBtn.onclick = function () {
      wrap.hidden = true;
      dismissBtn.hidden = true;
    };
  });

  // Check state after completion
  let state = await page.evaluate(() => {
    const wrap = document.getElementById('lumen-download-progress-wrap');
    const label = document.getElementById('lumen-download-progress-label');
    const dismissBtn = document.getElementById('lumen-download-progress-dismiss');
    return {
      wrapHidden: wrap.hidden,
      label: label.textContent,
      dismissBtnHidden: dismissBtn.hidden
    };
  });
  console.log('State at completion:', state);
  if (state.wrapHidden || state.dismissBtnHidden || state.label !== 'Saved to downloads') {
    throw new Error('Dismiss button or label not in expected state');
  }

  // Wait 4 seconds to confirm it does not auto-dismiss
  await new Promise(r => setTimeout(r, 4000));
  state = await page.evaluate(() => {
    const wrap = document.getElementById('lumen-download-progress-wrap');
    return { wrapHidden: wrap.hidden };
  });
  console.log('State after 4s (verifying persistence):', state);
  if (state.wrapHidden) {
    throw new Error('Notification should remain on screen until user dismisses it');
  }

  await page.setViewport({ width: 1280, height: 1024 });

  // Click the dismiss button
  await page.evaluate(() => {
    const btn = document.getElementById('lumen-download-progress-dismiss');
    if (btn) btn.scrollIntoView();
  });
  await page.click('#lumen-download-progress-dismiss');
  state = await page.evaluate(() => {
    const wrap = document.getElementById('lumen-download-progress-wrap');
    const dismissBtn = document.getElementById('lumen-download-progress-dismiss');
    return {
      wrapHidden: wrap.hidden,
      dismissBtnHidden: dismissBtn.hidden
    };
  });
  console.log('State after clicking checkmark dismiss button:', state);
  if (!state.wrapHidden || !state.dismissBtnHidden) {
    throw new Error('Dismiss button did not hide notification');
  }
  console.log('All dismiss button checks passed successfully!');
  await browser.close();
})();
