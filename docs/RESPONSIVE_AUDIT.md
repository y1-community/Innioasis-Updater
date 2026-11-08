# Responsive and viewport audit

Updated 8 November 2026 by Buffy. Antigravity: read "Open items" first.

## Harness

`tools/responsive/audit.py` (Updater repo) drives headless Chromium over CDP.
It loads each surface at 24 viewports and records horizontal overflow, dock
height and viewport share, running-costs line visibility, reserved clearance
below the footer, dock tap targets under 40px, CLS at top-of-page, and the
presence of Donate, Privacy and Language. Exit status is 1 on any finding;
the CLS band is 0.05.

    cd InnioasisY1Themes && python3 -m http.server 8099 --bind 127.0.0.1 &
    cd Innioasis-Updater && python3 -m http.server 8098 --bind 127.0.0.1 &
    .verify/venv/bin/python tools/responsive/audit.py \
        --base http://127.0.0.1:8099 --pages themes --out .responsive/themes
    .verify/venv/bin/python tools/responsive/audit.py \
        --base http://127.0.0.1:8098 --pages firmware --out .responsive/firmware
    .verify/venv/bin/python tools/responsive/audit.py \
        --base http://127.0.0.1:8098 --pages updater --out .responsive/updater

Chrome needs `--remote-allow-origins=*`; the harness passes it. Without it the
DevTools handshake fails with 403. `trace_overflow.py --selector X` prints the
matched rules for one element, which is how the header and hero overflows were
found. Reports and screenshots land in `.responsive/` (gitignored).

## Current results (8 Nov 2026, local servers, 24 devices each)

| surface | exit | overflow | footer clearance | small targets | CLS |
| --- | --- | --- | --- | --- | --- |
| updater | 0 | 0 | 0 | 0 | <=0.05 on all 24 |
| firmware | 1 | 0 | 0 | 0 | 0.0601 at 1440x1440 only |
| themes | 1 | 0 | 0 | 0 | 0.13-0.21 on desktop |

## Fixed in this pass

- Gallery header overflow (up to 251px). `gallery-chrome.js` injects the top
  bar as `display:flex` with no wrap and gave `.gallery-social-links` an inline
  `flex-shrink:0`; stylesheet rules could never win. The bar now wraps, has a
  narrow-screen order block, and the inline styles permit shrinking. Matching
  flex rules live at the end of `site-theme.css`.
- Updater hero spill (7px at 1133x744). `.lumen-hero` is a two-track grid with a
  fixed 340px art column; the tracks could not shrink. `site-theme.css` now uses
  `minmax(0, 1fr) minmax(0, auto)` with `min-width:0` children and caps the art
  at `min(340px, 100%)`. The element box now ends inside the viewport.
- Dock reserve. `--y1-dock-space` was published from a fixed wrapper that
  measures 0; `support_toolbar.html` measures `.y1-site-dock-wrap` instead, and
  `site-toolbar.css` starts at 104px.
- Tap targets: donate close 36px and privacy save 34px raised to 44px.
- Gallery skeleton ships in `index.html` markup (24 cards) instead of being
  injected after paint, and the grid rows are pinned at 392px (360px narrow).

## Open items

- Themes gallery CLS stays 0.13-0.21 on desktop, measured at top-of-page.
  Shift entries show `.theme-grid` moving down 87px when the filter bar is
  inserted, then `.wrap` and the banner moving up 8px, plus skeleton-card row
  heights changing on swap. Static skeleton cards, pinned grid rows and 87px /
  41px reservations for `.gallery-controls` and `.site-compat-banner` did not
  reduce the score, so the dominant moving region is still unidentified.
  Next step: capture `entry.sources` with full rects on every entry and diff the
  first 1500ms; do not add more min-heights until that is done.
  Owner: Antigravity.
- Firmware archive at 1440x1440: CLS 0.0601, 0.01 over the band. Same method.
  Owner: Antigravity.
- `viewport-fit=cover` is appended at runtime by the dock; it belongs in the
  static viewport meta of generated pages.

## Behaviours re-verified after the fixes

Goal line hidden on every compact and minimal tier (<=900px wide, <=700px tall,
square screens) and shown on the full tier (MacBook, iPad landscape, 32-inch
1440p/4K, ultrawide). Donate, Privacy and Language present at all 24 viewports
on all three surfaces. No dock target under 40px. Footer clearance measured 0
(dock footprint fully covered by reserved space) everywhere.

## Handoff for Antigravity

- The dock lives in `support_toolbar.html` in both repos. Change both together.
- Density tiers come from viewport size only, never from the bar height.
- `--y1-dock-space` is the contract between dock and page padding.
- The harness installs the CLS observer once per tab. Installing it per
  navigation multiplies the score; that bug produced the earlier 3.3 readings.
