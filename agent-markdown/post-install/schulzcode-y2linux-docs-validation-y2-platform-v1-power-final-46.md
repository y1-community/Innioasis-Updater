---
title: "POWER-FINAL-46 — space for every update, restart by default; first public release - Innioasis Updater"
description: "POWER-FINAL-46 — space for every update, restart by default; first public release Status: PUBLISHED and INSTALLED over Wi-Fi as GitHub release baseline-46 2026-10-16, arc"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-46.html"
---

# POWER-FINAL-46 — space for every update, restart by default; first public release - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-46 — space for every update, restart by default; first public release

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-46 — space for every update, restart by default; first public release

Status: PUBLISHED and INSTALLED over Wi-Fi as GitHub release `baseline-46` (2026-10-16, archive `20261016/150`), the first release on the update channel; its recovery screen stayed dark (fix: 47). Package `out/y2linux-platform-v1-power-final-candidate-46/` (fallback = 45, which the player runs), receipts `out/deep-sleep-final/build46-receipts/`. BOOTIMG `d5bacc9ee66b52c3894070e8f9c2846acb95e4fefa668262576856415bb5583f`, Y2ROOT `e8dde2d1b958a21cbc862fd7eaef5b147cda82ef08c306a7343c5c241842d87a`, RECOVERY `476567c538c7f1dbcea6b5f5cd1577595c4b862f9a9521c374b86ae4b35fe1e2`. Kernel `6.18.56-y2linux-platform-v1-power-final-46`, update sequence 4600, Linux `d03ab29`, Reborn `850687d`. Container suite 718 OK, host update/handover tests 31 OK, Reborn fmt/clippy/tests OK, all seal checks PASS. Signed with the release key; the release assets are `…-46-ota-release/` (manifest, signature, three payloads).

## Why

Owner after 45: "does the update process also have a cleanup, so that we can guarantee there is always enough space for users to update?" Staging 45 had failed `update_data_space_reserve` because a cancelled package stayed in `pending`, and nothing removed disposable data (the owner's player held 330 MiB of test logs).``````````````````

| Change | Detail |
| --- | --- |
| Stale package | Deleted before every download and on Cancel Update. |
| Rollback copies | The recovery deletes the previous copies right before writing new ones; the space check counts them as free. |
| Cleanup | If the download does not fit, disposable data goes one entry at a time until it does: /data/logs except system.log, recovery-last.log, recovery-display.txt; rotated *.previous.jsonl platform journals; finished qualification runs. First for the manifest (a check works on a nearly full volume), then for the payloads. Never music, settings, library or the rollback copies. |
| Refusal | download.jsonneeded_bytes; Reborn: "the update needs N MB of system space. Your music is not affected." |
| Restart | Default: restart into the recovery and back. Override restart.json{"mode": "poweroff"}. Low battery in the recovery always turns off. Outcome screens say Restarting. Reborn: Restart and Install. |

## Owner steps
  - Player on Wi-Fi: Settings → About & Updates → Check for Updates, Download Update, Restart and Install.
  - The agent checks the install log, the display, `Acknowledged` and the cleaned-up package afterwards.

## Device results
  - Over-the-air install from the GitHub release over Wi-Fi PASSED (owner: "it worked"): check found 46 (58.7 MB,

release key), download, Restart and Install, restart into 46 (boot `5b0b3a40`, reason 4), `Acknowledged`, taint 0.
  - The recovery screen stayed dark. Hand-over read-back correct (`vact=00000168` at 0.52 s), then at the first

modeset (0.56 s) the read lag; 44's three power cycles did not clear it (`still lag after 3 power cycles`), vblank 1. Analysis and fix: [47](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-47.md).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
