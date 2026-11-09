---
title: "Y2Linux 1.0 Beta 8.4 (Baseline 90) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.4 Baseline 90 Status: PUBLISHED as GitHub release baseline-90 2026-10-18. Release 1.0.0-beta.8.4 , Reborn 1.0.0-beta.8.4 identity only, kernel 6.18.56-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.4.html"
---

# Y2Linux 1.0 Beta 8.4 (Baseline 90) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.4 (Baseline 90)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.4 (Baseline 90)

Status: PUBLISHED as GitHub release `baseline-90` (2026-10-18). Release `1.0.0-beta.8.4`, Reborn `1.0.0-beta.8.4` (identity only), kernel `6.18.56-y2linux-1.0.0-beta.8.4`, update sequence 6700, Linux `c339919`, Reborn `000876f`. Built with `tools/production/release.py`: container suite 775 OK, host suite 802 OK; all seal checks PASS, no MediaTek firmware in any image. Not yet run on a player: the owner installs it over the air. Milestone audit BETA-8.4 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 71ad38769b9aeb91b25936c0e3708625f94fd71f3fb5c54d2598737581ad298e |
| Y2ROOT | d2436b2ce9e1cbfcffdf124060395ff14d7701edd46e61d5ee9fa25b131b5606 |
| RECOVERY | b59d0acda12604e5751e45de21dca0a840cc1b6ec614b6f7f855e3c999c5c6fd |
| Y2DATA (no SSH key) | fec46f0f919ea3bd53df2f9072b0c73405ed6fb48ad08bee6d4e8dc0b1fcfb7f |

## The dark display after a restart

The owner's over-the-air update to Beta 8.3 restarted from the recovery into a dark display; Reborn never drew a frame and the health check rolled the update back ([Beta 8.3 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.3.md)). Four restarts from the recovery that day, logs in `out/dsi-lag-2026-10-18/` (local):````````

| Boot | holding SMI common/larb0 at mm-clocks probe (0.36 s) | Handover snapshot | Display |
| --- | --- | --- | --- |
| 6500 install, 6501 install, rollback (8.2) | yes | larb0 stat=0 greq=0 | lit |
| 6600 install (8.3) | no | SMI gates 1 left closed by a restart, larb0 stat=1 greq=1 after 10 ms | dark |
| rollback to 6500 (8.3's recovery) | yes | larb0 idle | lit |

On the dark boot the SMI common clock gate was closed before Linux touched anything (before Lima's probe at 0.39 s), and LK's display request was stuck in larb0. The DSI register reads lagging one register from the first modeset, which three DSI power cycles did not clear, are the consequence. This is the case found in [POWER-FINAL-40](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-40.md): a watchdog restart keeps `MMSYS_CG_CON0`, so a gate Linux closed at shutdown (DRM disables the display and drops its SMI references) reaches LK, and LK's first fetch through larb0 never completes. [42](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-42.md) reopened the gates as the last step of a restart; [43](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-43.md) removed that because its own test restarts were dark for a second reason (Lima closing the gate during the next boot), which 43's hold fixes. Since then nothing covered the first case.``````````

| Part | Change (Linux 7ed664b) |
| --- | --- |
| Restart handler | Back: priority 255, after every driver has shut down and before the watchdog handler (128); writes MMSYS_CG_CLR0 = 3 (SMI common, larb0) when the DIS domain is powered. A powered-down domain comes back with its gates open anyway. |
| Hold | Unchanged (43): mm-clocks holds SMI common/larb0 from probe until the display mutex owns them. |
| Evidence | When the gate is found closed at probe, the boot logs SMI common gated before Linux touched it: CG_CON0=… larb0 stat=… greq=…. |
| Test | tests.test_display_domain: the handler writes only MMSYS_CG_CLR0 = 3 and only with DIS powered; registered after the hold. |

Not established: why only some restarts leave the gate closed; the handler reopens it on every restart either way.

The first OTA to 8.4: the restart into the recovery is still done by the running 8.2/8.3 kernel, so the install screen can stay dark once more; the restart out of the recovery into 8.4 is done by 8.4's recovery kernel, which has the handler.

## Device result: the owner's OTA 6600 → 6700 (2026-10-18)

The owner first installed 8.3 again (14:13, lit, acknowledged), then 8.4. Every boot after the dark one took the hold, and none logged `SMI gates … left closed` (`/data/logs/system.log*`, logs in `out/ota-90-owner/`, local):``````````````

| Boot | LK | SMI hold at probe | Handover | Display |
| --- | --- | --- | --- | --- |
| 14:05 restart into 6600 (8.3 recovery) | lcm=0 | no | SMI gates 1 left closed, larb0 busy | dark, rolled back |
| 14:11 rollback into 6500 | lcm=0 | yes | idle | lit |
| 14:13 restart into 6600 | lcm=0 | yes | idle | lit, acknowledged |
| recovery for 6700 (entered by 8.3's kernel) | lcm=0 | yes | idle | lit |
| 14:45 restart into 6700 (8.4's recovery kernel, with the handler) | lcm=1 | yes | larb0 stat=0 greq=0 | lit, acknowledged |

Install (kept 6600 package as the rollback copy, `source: package`), journal `timings`: verify 1.50 s (the kept root hashed alongside), backup_root 0.17 s, backup_boot 1.31 s, system 8.33 s, check 4.10 s, boot 0.76 s: 16.2 s. The estimate said 14 s at `verify`, 8 s at `system` (real 12.8 s), 7 s at `check` (4.9), 1 s at `boot` (0.8): the system write took 8.3 s for 103 MB written, against 4.4 s for the same amount in the 6600 install, so the model's 10 ms per MiB was low this time (eMMC write speed varies; one sample).

One lit restart through the handler is not yet proof for an intermittent fault (one dark restart in five that day).

## Known gaps
  - The restart handler has run once on the player (lit). Later restarts: check for `holding SMI common/larb0` and no

`SMI gates … left closed`.
  - Unchanged: the sleep drain with the panel powered down is not measured yet (#42); the GC9503V panel path awaits a

GC9503V owner (#45). One host-suite run failed a timing-sensitive Bluetooth test under load (`test_reconnect_signal_cache_intents_and_bounded_recovery`); it passed alone three times and in the full rerun.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
