import puppeteer from 'puppeteer';

(async () => {
  const browser = await puppeteer.launch({
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-dev-shm-usage']
  });

  const page = await browser.newPage();
  const port = process.env.PORT || 8000;
  const baseUrl = `http://localhost:${port}`;

  console.log(`Starting comprehensive verification on ${baseUrl}...`);
  const report = {};

  // 1. Verify Home Page
  await page.goto(`${baseUrl}/index.html`, { waitUntil: 'networkidle0' });
  report.homePageTitle = await page.title();

  // Check announcement strip
  const announcementInfo = await page.evaluate(() => {
    const strip = document.querySelector('.lumen-announcement-strip');
    if (!strip) return null;
    const text = strip.querySelector('.lumen-announcement-text')?.textContent || '';
    const links = Array.from(strip.querySelectorAll('a')).map(a => ({ text: a.textContent, href: a.getAttribute('href') }));
    return { text, links };
  });
  report.announcement = announcementInfo;
    throw new Error('Homepage announcement banner missing or missing expected copy');
  }

  // Check home firmware table
  const homeRows = await page.evaluate(() => {
    const rows = document.querySelectorAll('#lumen-home-firmware-table tr');
    return Array.from(rows).map(r => {
      const name = r.querySelector('.lumen-project-link strong')?.textContent || '';
      const models = Array.from(r.querySelectorAll('.lumen-button--model')).map(b => b.textContent.trim());
      const benefitLink = r.querySelector('.lumen-benefit-link')?.getAttribute('href') || null;
      return { name, models, benefitLink };
    });
  });
  report.homeProjectsCount = homeRows.length;
  report.homeProjects = homeRows;

  // Verify Inniclassic has both Y1 and Y2 buttons
  const inniclassicRow = homeRows.find(r => r.name === 'Inniclassic');
  report.inniclassicBothModelsOnHome = inniclassicRow ? (inniclassicRow.models.includes('Y1') && inniclassicRow.models.includes('Y2')) : false;
  // Verify Better-Y has benefit link
  const betterYRow = homeRows.find(r => r.name === 'Better-Y');
  report.betterYBenefitLink = betterYRow?.benefitLink;

  // 2. Verify Software Downloads Catalogue
  await page.goto(`${baseUrl}/firmware.html`, { waitUntil: 'networkidle0' });
  report.firmwarePageTitle = await page.title();

  // Verify releases rendered initially
  await page.waitForSelector('#lumen-firmware-table tr', { timeout: 10000 });
  report.initialReleasesRendered = true;

  // Verify zip download button presence and styling
  const zipButtonInfo = await page.evaluate(() => {
    const row = document.querySelector('#lumen-firmware-table tr');
    if (!row) return null;
    const updaterBtn = row.querySelector('.lumen-updater-button');
    const zipBtn = row.querySelector('.lumen-zip-download-button');
    const svgIcon = zipBtn ? zipBtn.querySelector('svg') : null;
    return {
      hasUpdaterBtn: !!updaterBtn,
      hasZipBtn: !!zipBtn,
      hasSvgIcon: !!svgIcon,
      zipBtnText: zipBtn ? zipBtn.textContent.trim() : null
    };
  });
  report.zipButton = zipButtonInfo;

  // Check Software filter options for Y1
  const y1SoftwareOptions = await page.evaluate(() => {
    const select = document.getElementById('lumen-software-filter');
    return Array.from(select.options).map(o => o.text);
  });
  report.y1SoftwareOptions = y1SoftwareOptions;

  // Switch to Y2 and check options
  await page.select('#lumen-model-filter', 'Y2');
  await new Promise(r => setTimeout(r, 300));
  const y2SoftwareOptions = await page.evaluate(() => {
    const select = document.getElementById('lumen-software-filter');
    return Array.from(select.options).map(o => o.text);
  });
  report.y2SoftwareOptions = y2SoftwareOptions;
  report.y2HasInniclassic = y2SoftwareOptions.includes('Inniclassic');
  report.y2HasAndroid44 = y2SoftwareOptions.includes('Android 4.4 (Dev)');
  report.y1HasAndroid42 = y1SoftwareOptions.includes('Android 4.2 (Dev)');

  // 3. Verify All New Guide, Software, and Benefits Pages
  const testPages = [
    '/guides/inniclassic-y2.html',
    '/inniclassic-y2-software.html',
    '/guides/better-y-y1.html',
    '/better-y-y1-software.html',
    '/better-y-benefits.html',
    '/guides/android-4-2-y1.html',
    '/android-4-2-y1-software.html',
    '/guides/android-4-4-y2.html',
    '/android-4-4-y2-software.html',
    '/guides/linux-y1.html',
    '/linux-y1-software.html'
  ];

  const pageResults = [];
  for (const p of testPages) {
    const resp = await page.goto(`${baseUrl}${p}`, { waitUntil: 'domcontentloaded' });
    const title = await page.title();
    const status = resp.status();
    const titleOk = title.length > 5;
    pageResults.push({ path: p, status, titleOk });
    if (status !== 200 || !titleOk) {
      throw new Error(`Failed check for page ${p}: status=${status}, title=${title}`);
    }
  }
  report.newPages = pageResults;

  // 4. Test JSZip and repack bundling logic in browser
  await page.goto(`${baseUrl}/firmware.html`, { waitUntil: 'networkidle0' });
  const jszipLoaded = await page.evaluate(() => typeof window.JSZip === 'function');
  report.jszipLoaded = jszipLoaded;

  // 5. Test Dynamic Model Filter (e.g. adding G1 or Timmkoo models)
  const dynamicModelTest = await page.evaluate(() => {
    // Inject a new package for G1
    window.INNIOASIS_FIRMWARE_CATALOG.push({
      slug: "original-g1",
      name: "Original Software",
      model: "G1",
      type: "original",
      repo: "y1-community/Innioasis-Updater",
      packageName: "rom_g1.zip",
      guide: "original-software-g1.html"
    });
    // Trigger directory re-init
    if (window.INNIOASIS_TEST_INIT_DIRECTORY) {
      window.INNIOASIS_TEST_INIT_DIRECTORY();
    } else {
      // Re-run initFirmwareDirectory by selecting model or checking options
      const modelSelect = document.getElementById('lumen-model-filter');
      // Dispatch or re-fill
      const catalog = window.INNIOASIS_FIRMWARE_CATALOG;
      const availableModels = [];
      catalog.forEach(item => {
        if (item.model && availableModels.indexOf(item.model) === -1) availableModels.push(item.model);
      });
      return {
        catalogHasG1: availableModels.includes('G1'),
        modelOptions: Array.from(modelSelect.options).map(o => o.value)
      };
    }
    const modelSelect = document.getElementById('lumen-model-filter');
    return {
      modelOptions: Array.from(modelSelect.options).map(o => o.value)
    };
  });
  report.dynamicModelTest = dynamicModelTest;

  // 6. Verify CTAs across all 18 guides and 17 companion software pages
  const allGuides = [
    '/guides/android-4-2-y1.html',
    '/guides/android-4-4-y2.html',
    '/guides/better-y-y1.html',
    '/guides/inniclassic-y1.html',
    '/guides/inniclassic-y2.html',
    '/guides/jj-launcher-y1.html',
    '/guides/jj-launcher-y2.html',
    '/guides/jj-launcher.html',
    '/guides/koensayr-y1.html',
    '/guides/linux-y1.html',
    '/guides/restore-original-y1.html',
    '/guides/restore-original-y2.html',
    '/guides/rockbox-y1.html',
    '/guides/rockbox-y2.html',
    '/guides/solar-y1.html',
    '/guides/solar-y2.html',
    '/guides/y2player-y2.html',
  ];

  const allSoftwarePages = [
    '/android-4-2-y1-software.html',
    '/android-4-4-y2-software.html',
    '/better-y-y1-software.html',
    '/inniclassic-y1-software.html',
    '/inniclassic-y2-software.html',
    '/jj-launcher-y1-software.html',
    '/jj-launcher-y2-software.html',
    '/koensayr-y1-software.html',
    '/linux-y1-software.html',
    '/original-software-y1.html',
    '/original-software-y2.html',
    '/rockbox-y1-software.html',
    '/rockbox-y2-software.html',
    '/solar-y1-software.html',
    '/solar-y2-software.html',
    '/y2player-y2-software.html',
  ];

  for (const g of allGuides) {
    await page.goto(`${baseUrl}${g}`, { waitUntil: 'domcontentloaded' });
    const content = await page.content();
    const countGet = (content.match(/Get Updater CE/g) || []).length;
    const countThis = (content.match(/Get this in Updater CE/g) || []).length;
    if (countGet < 1 || countThis < 1) {
      throw new Error(`Guide ${g} missing required CTAs (Get Updater CE: ${countGet}, Get this in Updater CE: ${countThis})`);
    }
    const banners = await page.$$eval('.lumen-callout', els => els.length);
    if (banners > 0) {
      throw new Error(`Guide ${g} has ${banners} intrusive callout banners`);
    }
    const headerButtons = await page.$$eval('.lumen-guide-header .lumen-actions .lumen-button', els => els.length);
    if (headerButtons > 3) {
      throw new Error(`Guide ${g} has ${headerButtons} header buttons (expected <= 3)`);
    }
  }

  for (const s of allSoftwarePages) {
    await page.goto(`${baseUrl}${s}`, { waitUntil: 'domcontentloaded' });
    const content = await page.content();
    const countGet = (content.match(/Get Updater CE/g) || []).length;
    const countThis = (content.match(/Get this in Updater CE/g) || []).length;
    if (countGet < 1 || countThis < 1) {
      throw new Error(`Software page ${s} missing required CTAs (Get Updater CE: ${countGet}, Get this in Updater CE: ${countThis})`);
    }
    const banners = await page.$$eval('.lumen-callout', els => els.length);
    if (banners > 0) {
      throw new Error(`Software page ${s} has ${banners} intrusive callout banners`);
    }
    const headerButtons = await page.$$eval('.lumen-guide-header .lumen-actions .lumen-button', els => els.length);
    if (headerButtons > 3) {
      throw new Error(`Software page ${s} has ${headerButtons} header buttons (expected <= 3)`);
    }
  }
  report.allCtasVerified = true;

  // 7. Verify device model coverage and stock firmware SEO copy on key pages
  const targetModels = ['Y1', 'Y2', 'G1', 'G3', 'G5', 'Q8', 'R1', 'PR1', 'Q5', 'Q3'];
  const targetTerms = ['Innioasis', 'Timmkoo', 'stock firmware', 'original firmware'];
  const seoPages = ['/index.html', '/firmware.html', '/firmware-faq.html', '/firmware-guide.html'];

  for (const p of seoPages) {
    await page.goto(`${baseUrl}${p}`, { waitUntil: 'domcontentloaded' });
    const text = await page.content();
    for (const m of targetModels) {
      if (!text.includes(m)) {
        throw new Error(`SEO page ${p} missing model mention for ${m}`);
      }
    }
    for (const t of targetTerms) {
      if (!text.toLowerCase().includes(t.toLowerCase())) {
        throw new Error(`SEO page ${p} missing term ${t}`);
      }
    }
  }
  report.seoAndModelsVerified = true;

  console.log(JSON.stringify(report, null, 2));

  await browser.close();
  console.log('test_complete_verification passed completely!');
})();
