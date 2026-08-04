import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch({ headless: true, args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  
  // Test desktop width
  await page.setViewport({ width: 1280, height: 800 });
  await page.goto('http://localhost:8080/firmware.html', { waitUntil: 'networkidle0' });
  
  const results = {};
  
  // 1. Check no release dropdown
  results.noReleaseDropdown = await page.$('#release-dropdown') === null && await page.$('select') === null;
  
  // 2. Check two filters
  const filters = await page.$$('.filter, select, input[type="search"], input[type="text"], .filter-input, .filter-select');
  results.filterCount = await page.evaluate(() => {
    // Let's check specific filter elements or inputs/selects in filter container
    const filterContainer = document.querySelector('.filters, .filter-bar, [class*="filter"]');
    return document.querySelectorAll('input, select').length;
  });

  // Let's inspect the page content
  const html = await page.content();
  console.log("HTML length:", html.length);
  
  // Check console messages
  const consoleMessages = [];
  page.on('console', msg => consoleMessages.push({ type: msg.type(), text: msg.text() }));

  // Test mobile width
  await page.setViewport({ width: 375, height: 667 });
  await page.reload({ waitUntil: 'networkidle0' });

  await browser.close();
  console.log(JSON.stringify(results, null, 2));
})();
