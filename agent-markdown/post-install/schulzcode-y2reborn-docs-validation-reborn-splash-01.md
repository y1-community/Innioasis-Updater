---
title: "REBORN-SPLASH-01 - Innioasis Updater"
description: "REBORN-SPLASH-01 <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-validation-reborn-splash-01.html"
---

# REBORN-SPLASH-01 - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# REBORN-SPLASH-01

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# REBORN-SPLASH-01 > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

The owner installed the startup update and reports that it works. SSH confirms the expected source, hardware renderer and explicit splash handoff. See the [physical inspection](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fvalidation%2F2026-09-18-radio-inspection.md) for evidence and limits.

Built Reborn source: `6209f48402a00a077759df042916f0ae2c89783a`. Built Y2Linux integration: `1e0888795008cc57de92c47a3a241e45cb91e420`. Kernel source retained: `7e318afbffe640c6bf9da458f61ac2108f7d5bde`.

Reborn prepares its first real EGL/GLES frame before asking the early KMS splash to release DRM master. It presents that buffer, acknowledges presentation, and logs `startup.ready`. The splash retains the previous scanout until presentation; neither participant switches the console back to text during handoff. The native boundary is limited to `crates/reborn-graphics/native/splash-handoff.h` and the existing renderer. The previous no-splash startup path remains supported.

The platform helper, exact package/fallback hashes, validation receipts, failure behavior and manual installation procedure are documented in `/home/luca/Dokumente/Code/Y2Linux/docs/build/reborn-splash-01-deployment.md`. The package is `/home/luca/Dokumente/Code/Y2Linux/out/REBORN-SPLASH-01`. It is a matched BOOTIMG + Y2ROOT update: do not combine the new early splash with an older Reborn lacking the handoff. There is no Reborn 02 feature expansion.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
