import http from 'http';
import fs from 'fs';
import path from 'path';

// Let's inspect firmware.html using node to verify requirements:
// 1. Verify no release dropdown (check if '#release-dropdown' or any select other than model and software exists)
// 2. Verify two filters (model and software)
// 3. Verify table scroller (lumen-table-wrap)
// 4. Verify guide CTA and expandable download details in lumen-site.js / HTML
const html = fs.readFileSync('firmware.html', 'utf8');

console.log("--- HTML Checks ---");
console.log("Has release-dropdown:", html.includes("release-dropdown"));
console.log("Select count:", (html.match(/<select/g) || []).length);
console.log("Table wrap:", html.includes("lumen-table-wrap"));

// Let's check firmware-catalog.js and lumen-site.js
const catalog = fs.readFileSync('firmware-catalog.js', 'utf8');
const script = fs.readFileSync('lumen-site.js', 'utf8');

console.log("\n--- Script Checks ---");
console.log("First row prominent updater CTA check:", script.includes("primary"));
console.log("Compact guide link removed:", !script.includes("lumen-compact-guide-link"));
console.log("Manual ZIP link removed:", !script.includes("lumen-manual-download") && !script.includes("Manual ZIP"));
console.log("Release details <details> check:", script.includes("lumen-release-details"));
console.log("Release details summary renamed:", script.includes("<summary>Release details and zip</summary>"));
console.log("Model zip options present:", script.includes('label: "Y1 · Type A"') && script.includes('label: "Y1 · Type B"') && script.includes('label: "Y2"'));

