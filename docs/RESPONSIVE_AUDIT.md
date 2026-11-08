# Responsive and viewport audit

Updated 8 November 2026 by Buffy. Antigravity: read "Open items" first.

## Harness

`tools/responsive/audit.py` (Updater repo) drives headless Chromium over CDP.
It loads each surface at 24 viewports and records horizontal overflow, dock
height and viewport share, running-costs line visibility, reserved clearance
below the footer, dock tap targets under 40px, CLS at top-of-page, and the
presence of Donate, Privacy and Language. Exit status is 1 on any finding.

Run against a local checkout (two servers, one per repo):

    cd InnioasisY1Themes && python3 -m http.server 8099 --bind 127.0.0.1 &
    cd Innioasis-Updater && python3 -m http.server 8098 --bind 127.0.0.1 &
    .verify/venv/bin/python tools/responsive/audit.py \
        --base http://127.0.0.1:8099 --pages themes --out .responsive/themes
    .verify/venv/bin/python tools/responsive/audit.py \
        --base http://127.0.0.1:8098 --pages firmware --out .responsive/firmware
    .verify/venv/bin/python tools/responsive/audit.py \
        --base http://127.0.0.1:8098 --pages updater --out .responsive/updater

Chrome needs `--remote-allow-origins=*`; the harness passes it. Without it the
DevTools WebSocket handshake fails with 403. `trace_overflow.py` prints the
matched CSS rules for one selector, which is how the header overflow was found.

Baseline runs are in `.responsive/` (gitignored) with screenshots per device.

## What was broken and what fixed it

Overflow, up to 251px at 344px wide. `gallery-chrome.js` injects the top bar as
`display:flex` with no wrap, and gave `.gallery-social-links` an inline
`flex-shrink:0`, so stylesheet rules could not win. Fixed in `gallery-chrome.js`
(injected topbar rule now wraps, narrow `@media` block orders the bar, inline
styles no longer refuse to shrink) and in `site-theme.css` (matching flex
rules). The old grid rules were dead code and are gone.

Footer trapped under the dock. The dock published `--y1-dock-space` from
`#support-toolbar-container`, a fixed wrapper whose only child is fixed, so it
measured 0. `support_toolbar.html` now measures `.y1-site-dock-wrap` and
reserves its footprint plus 12px. `site-toolbar.css` starts at 104px so the
first paint is stable.

Sub-40px targets. Donate close (36px) and privacy save (34px) raised to 44px in
`support_toolbar.html`.

Tablet-landscape hero spill. `.lumen-hero-art` bounded in `site-theme.css`.

## Measured after the fixes

- themes: 24/24 devices, overflow 0, footer clearance 0, no small targets;
  findings are CLS only (below).
- firmware: 24/24, exit 0, zero findings. CLS 0.011 at 1440p.
- updater: 23/24 clean, CLS 0.018; one accepted exception (below).

Goal line: hidden on every compact and minimal tier (<=900px wide, <=700px
tall, square screens), visible on full tier (MacBook, iPad landscape, 32-inch
1440p/4K, ultrawide). Donate, Privacy and Language were present at all 24
viewports on all three surfaces.

## Accepted exceptions

- Themes gallery CLS 0.13-0.21 on desktop (0 on phones; the content is below
  the fold there). Cause: the gallery renders skeleton cards, then streams real
  cards, so `.wrap` grows from 2593px to 4469px at ~600-700ms. Fixing it means
  rendering the first card batch server-side or pinning the grid to a fixed
  height until hydration finishes. Owner: Antigravity; measure with the harness,
  target under 0.1.
- Updater landing page, iPad mini landscape (1133x744): 7px of horizontal
  layout overflow from `.lumen-hero-art`. Visually clipped by `overflow-x: clip`
  so there is no scrollbar, but the element box still exceeds the viewport.
  Owner: Antigravity; trace with `trace_overflow.py --selector .lumen-hero-art`.

## Notes for Antigravity

- The dock lives in `support_toolbar.html` in both repos. Change both together.
- Density tiers come from viewport size only, never from the bar height.
- `--y1-dock-space` is the contract between the dock and page padding.
- The harness installs the CLS observer once per tab; adding it per navigation
  multiplies the score (that bug produced the earlier 3.3 readings).
