---
title: "Y2Linux 1.0 Beta 7.3 (Baseline 64) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 7.3 Baseline 64 Status: PUBLISHED as GitHub release baseline-64 2026-10-16. Release 1.0.0-beta.7.3 , Reborn 1.0.0-beta.7.3 , kernel 6.18.56-y2linux-1.0.0"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-7.3.html"
---

# Y2Linux 1.0 Beta 7.3 (Baseline 64) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 7.3 (Baseline 64)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 7.3 (Baseline 64)

Status: PUBLISHED as GitHub release `baseline-64` (2026-10-16). Release `1.0.0-beta.7.3`, Reborn `1.0.0-beta.7.3`, kernel `6.18.56-y2linux-1.0.0-beta.7.3`, update sequence 5950, Linux `cbab171`, Reborn `7175c76`, git tag `baseline-64` in both repositories. Built with `tools/production/release.py` in 120 s: container suite 743 OK, all seal checks PASS, no MediaTek firmware in any image. Milestone audit: BETA-7.3 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | d234b6129b68c2011c02c630fa82f0ad26a4c8c29793c8f039a9d1e28cb16682 |
| Y2ROOT | 91e2a236148e830393b3c31ffa6f527d9d6b8b3365ffa8884a7810cf07e91b61 |
| RECOVERY | 68c7432b0e7e07a13720662dfe8417506c6125024bda8f7e32b0aa358918d3f1 |
| Y2DATA (no SSH key) | 3cf68b246452ac2b0812cd194a31f722734db61cecd7704d5dcfcfadb8f2a90b |

## Since Beta 7.2 (Reborn `07316bb`)

Owner, on Beta 7.2 with the cable in for the frame-rate measurement: the computer screen (locked since 7.1) could not be left, and "Use While Connected" was not on in the saved settings (`usb_developer: false` on the device) and could not be reached while connected; the 7.2 sampler showed the expected ≈2 frames/s under that still screen. Decision: no covering screen at all — "a little notification that says connected like the library scan and a USB symbol in the BT/Wi-Fi area".``

| Part | Change |
| --- | --- |
| Messages | Connecting: "Connected to a computer"; copying starting: "Copying files from the computer…" (the same message style as the library scan). |
| Status bar | The USB symbol while a computer has the drives (Ready or Copying), in the accent while copying. |
| Removed | The computer screen over the player, its input lock and dismiss state, Settings::usb_developer and the service page's "Use While Connected". Kept: the screen lights when a computer opens the drives; Storage → From a Computer while a cable is in. |

Host evidence: 487 Reborn tests (rewritten: a computer connecting shows the message and the symbol, navigation keeps working, copying shows its message), strict Clippy, fmt; previews 40/41.

## Device checks owed
  - Plug in on any screen: "Connected to a computer" and the USB symbol; the player stays usable; copying turns the symbol

blue with its message.
  - The Beta 7.2 frame-rate sample (now possible with the cable in), then the 7.1 and 7 checks.

## Known gaps

As Beta 7.2: FM radio (Beta 8); no 12/24-hour switch; sleep ≈7.8–9.4 mA vs stock ≈1.3 mA; Bluetooth range hardware-limited; no headphone-jack detection.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
