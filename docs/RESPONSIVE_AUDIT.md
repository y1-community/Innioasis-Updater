# Responsive and viewport audit

Last updated 8 November 2026. Maintained by Buffy and Antigravity; edit in
place and keep the "Open items" section current.

## What this covers

The three public surfaces: the firmware archive (`innioasis.app/firmware.html`),
the Updater CE landing page (`innioasis.app`) and the themes gallery
(`themes.innioasis.app`).

`tools/responsive/audit.py` drives the local headless Chromium over the DevTools
protocol. For every page and viewport it records:

- horizontal overflow (document wider than the viewport)
- bottom dock height and its share of the viewport
- whether the running-costs goal line is showing
- footer copy hidden behind the dock
- dock tap targets under 40 CSS px
- cumulative layout shift, with the shifted nodes

Run it against production:

    .verify/venv/bin/python tools/responsive/audit.py --out .responsive/live

Or against a local checkout of the themes or main site (pages then resolve
against the `--base` origin):

    python3 -m http.server 8099 --bind 127.0.0.1
    .verify/venv/bin/python tools/responsive/audit.py --base http://127.0.0.1:8099 \
        --pages themes --out .responsive/local

Exit status is 1 when anything fails, so it can gate CI. `report.md` and
`report.json` land in the output directory next to per-device screenshots.

## Device matrix

Square and small handhelds: IkkoMind One, Unihertz Pocket, Titan 2, Elite,
Elite Pro, BlackBerry Passport. Foldables: Galaxy Z Flip 5 and 6, Z Fold 5 cover
and inner screens, the 420x900 foldable iPhone profile. Phones: iPhone SE, 16,
16 Pro Max. Tablets: iPad mini. Laptops: MacBook Air 13, MacBook Pro 16.
Everything else: smart-fridge portrait, 32-inch 1440p, 32-inch 4K, 34-inch
ultrawide.

Adding a device is one dict in `DEVICES`.

## Dock behaviour

Priority, highest first, and unchanged by density:

1. Donate, Privacy, Language (the language panel is also the accessibility
   entry point)
2. text size, close
3. running-costs goal line and the ticker

`support_toolbar.html` sets `data-dock-density` on the dock container from the
viewport alone, never from the bar's own height, so a tier change cannot
oscillate:

| tier | when | effect |
| --- | --- | --- |
| full | wide and tall | everything, goal line included |
| compact | width under 900, height under 700, or a nearly square viewport | goal line and ticker hidden, A- and A+ folded |
| minimal | width under 420, height under 480, or a small square screen | icon-only controls, 44px targets |

The dock publishes its height as `--y1-dock-space`; the page reserves that space
at the bottom so a footer is never trapped under the bar. Every control keeps a
44x44 CSS px hit area at every density.

Confirmed locally at 600x600 and 344x882 and 393x852: goal line hidden, dock
55px instead of 103px on the compact tier, no dock-height share above 12%.

## Open items

- Narrow gallery widths still overflow. At 344px the document is 251px too
  wide, at 393px 202px, at 600px 33px. The widest node is
  `.gallery-social-links` (603px) inside `.gallery-topbar`. Two overrides
  (single class, then `body.site-themes-app .gallery-topbar .gallery-social-links`)
  did not change the measurement, so the width is coming from somewhere else in
  that strip, most likely an absolutely positioned ancestor or an inline
  `width` on a child. Start there rather than adding more `max-width` rules.
- Desktop CLS on the themes gallery measured 1.03 locally and 3.3 on the live
  site (MacBook Air, 32-inch 1440p). The layout-shift entries carry no source
  nodes, so the cause is not yet attributed. Check hero image decoding and the
  theme card skeleton-to-card swap before touching unrelated layout.
- The iPhone profile is 420x900; confirm the real foldable Safari viewport once
  it ships, then update `DEVICES`.
- `viewport-fit=cover` is appended at runtime by the dock script. It belongs in
  the static viewport meta on generated pages so the first paint already has
  safe-area insets.

## Working notes for Antigravity

- The dock is one self-contained file (`support_toolbar.html`, style block plus
  inline script) and exists in both `InnioasisY1Themes` and `Innioasis-Updater`.
  Change both in the same commit.
- The density tier is derived only from `window.innerWidth` and
  `window.innerHeight`. If you add a rule that changes the bar height, do not
  feed that height back into the tier.
- `site-theme.css` carries the top-bar responsive overrides at the end of the
  file, under the "Responsive hardening" heading. Media queries there use 900px
  and 420px breakpoints.
- Keep prose in the product voice: short sentences, no marketing adjectives, no
  em dashes. The site copy is edited with the humanizer checklist.
