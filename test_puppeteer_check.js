import puppeteer from 'puppeteer';

(async () => {
  let browser;
  try {
    browser = await puppeteer.launch({ 
      headless: true, 
      executablePath: process.env.CHROME_PATH || '/usr/bin/google-chrome-stable',
      args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage'] 
    });
  } catch (e) {
    console.log("Puppeteer launch failed:", e.message);
    process.exit(0);
  }
  const page = await browser.newPage();
  
  // Test desktop width
  await page.setViewport({ width: 1280, height: 800 });
  await page.goto('http://localhost:8080/firmware.html', { waitUntil: 'networkidle0' });
  
  const results = {};
  
  // 1. Check no release dropdown
  results.noReleaseDropdown = await page.$('#release-dropdown') === null;
  
  // 2. Check two filters
  const filtersCount = await page.evaluate(() => {
    return document.querySelectorAll('.lumen-filterbar select, .lumen-filterbar input').length;
  });
  results.twoFilters = filtersCount === 2;

  // Wait for table to render or load
  await page.waitForSelector('#lumen-firmware-table tr', { timeout: 5000 }).catch(() => {});

  results.hasReleaseRowsOrUnavailable = await page.evaluate(() => {
    const rows = document.querySelectorAll('#lumen-firmware-table tr');
    return rows.length > 0;
  });

  results.firstRowProminentUpdater = await page.evaluate(() => {
    const firstRow = document.querySelector('#lumen-firmware-table tr');
    if (!firstRow) return false;
    return firstRow.querySelector('.lumen-updater-button') !== null;
  });

  results.allRowsFullUpdaterButton = await page.evaluate(() => {
    const rows = document.querySelectorAll('#lumen-firmware-table tr');
    if (rows.length <= 1) return true; // if only 1 row or 0
    // Every row should carry the full Get it on Updater button
    for (let i = 0; i < rows.length; i++) {
      if (rows[i].querySelector('.lumen-updater-button') === null) {
        return false;
      }
    }
    return true;
  });

  results.manualZipLinkRemoved = await page.evaluate(() => {
    return document.querySelectorAll('.lumen-manual-download').length === 0;
  });

  results.releaseDetailsSummary = await page.evaluate(() => {
    const summary = document.querySelector('.lumen-release-details summary');
    return summary ? summary.textContent.trim() : null;
  });

  results.noHorizontalOverflow = await page.evaluate(() => {
    const tableWrap = document.querySelector('.lumen-table-wrap');
    if (!tableWrap) return false;
    return tableWrap.scrollWidth <= tableWrap.clientWidth + 5; // allow small tolerance
  });

  // Test mobile width
  await page.setViewport({ width: 375, height: 667 });
  await new Promise(r => setTimeout(r, 500));

  results.mobileNoHorizontalOverflow = await page.evaluate(() => {
    const tableWrap = document.querySelector('.lumen-table-wrap');
    if (!tableWrap) return false;
    return tableWrap.scrollWidth <= tableWrap.clientWidth + 5;
  });

  // Expand guide CTA or release details
  const detailsExpanded = await page.evaluate(() => {
    const details = document.querySelector('.lumen-release-details details, details.lumen-release-details');
    if (details) {
      details.open = true;
      return true;
    }
    return false;
  });
  results.detailsExpanded = detailsExpanded;

  await browser.close();
  console.log(JSON.stringify(results, null, 2));
})();
