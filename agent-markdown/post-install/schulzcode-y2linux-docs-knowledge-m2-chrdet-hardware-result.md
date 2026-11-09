---
title: "M2-CHRDET-01 physical result - Innioasis Updater"
description: "M2-CHRDET-01 physical result <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m2-chrdet-hardware-result.html"
---

# M2-CHRDET-01 physical result - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-CHRDET-01 physical result

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-CHRDET-01 physical result > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-09, implementation `de1a6d0`. The owner supplied three photographs in `out/m2-chrdet-01/` and reports no error when starting without USB, but error `-19` when starting with USB connected. All show M2-CHRDET-01 and Linux 6.18.0-y2-m2-chrdet1. Filenames describe startup cable state; they do not certify same-boot chronology or BEAT 50.

| Field | USB connected at startup, “10” | No USB at startup, “10” | No USB at startup, “50” |
| --- | --- | --- | --- |
| Actual BEAT / FRAME | 10 / 68 | 11 / 74 | 46 / 284 |
| Uptime / idle seconds | 11.32 / 10.16 | 12.43 / 11.17 | 51.28 / 46.52 |
| Timer IRQ CPU0 | 1134 | 1245 | 5130 |
| PW result / validity | 0 / 7 | 0 / 7 | 0 / 7 |
| CLK result / validity | 0 / 15 | 0 / 15 | 0 / 15 |
| CHR_CON0 / bit5 | 007B / 1 | 0001 / 0 | 0001 / 0 |
| USB result / validity | 0 / 001FFFFF | 0 / 001FFFFF | 0 / 001FFFFF |
| WAKE / written / pre-post validity | -19 / 0 / 00-000 | 0 / 1 / 7F-FFF | 0 / 1 / 7F-FFF |
| PHY 6a before / after | BE / unread | 04 / 00 | 04 / 00 |
| Post POWER / DEVCTL | unread | 20 / 80 | 20 / 80 |
| Post PHY68..6e | unread | 00 00 00 02 12 00 00 | same |
| Pre PHY1a / 1d / 22 / 63 | unread | 10 / 00 / 00 / 00 | same |
| PHY00 / 05 / 15 before-after | unread | 6E/6E / 44/44 / 10/10 | same |
| Last error | PHY WAKE -19 | NONE | NONE |
| MemTotal / CPUs online | 22208 kB / 0 | same | same |
| Sleep / proc / sysfs results | 0 / 0 / 0 | same | same |
| Watchdog / framebuffer / frame write | STOPPED / GUARD OK / 804 | same | same |

CONFIRMED: the cached PMIC status read succeeds in both reported startup conditions; CHRDET tracks the supplied cable-state reports. This is charger presence, not proof of host identity, data-wire integrity, electrical voltage or a usable MUSB session. The connected boot is visibly running at BEAT 10. The no-USB photographs show successful guarded wake and progress as late as BEAT 46; the owner has not explicitly confirmed that those two images share a boot. No connected-boot BEAT 50/STOP or continuous stability is claimed.

## Why -19 appears

`y2_usb_wake_probe()` starts with result -19 and refuses its initial guard unless the complete snapshot matches the reviewed passive state. In particular, PHY6a must be 04. The connected photograph shows BE, with `written=0` and both wake validity masks zero. This establishes refusal before the seven extra mode reads and before any PHY write. It is not a failed CHRDET/PWRAP transaction, a kernel boot failure, or a failed write of zero to 6a.

The old PID1 screen replaces the valid original USB rows whenever all USB reads succeeded, even when the subsequent wake guard refused. Consequently its `BE>00`, zero post-PHY, zero mode/trim and `P:00 D:00` fields contain unread zero-initialized storage. Those zeros are not hardware evidence. Other initial guard failures may coexist with 6a=BE; the original MAC, remaining PHY, DMA and IRQ-enable values were collected but hidden.

The earlier successful attached-cable PHY-wake report remains valid within its reported conditions. Exact cable attachment timing relative to startup is not established there. Do not equate “attached during observation” with “attached at power-on,” erase that success, or infer the loader's complete mode from BE.

## Next evidence boundary

[M2-USBGUARD-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-guard-diagnostic.md) changes diagnostic presentation only: retain the captured initial state on an early refusal and mark unread values with dashes. All register transactions, guards, snapshot ABI, memory/DMA and boot packaging policies remain unchanged. Obtain the connected-start raw state before selecting a stock-derived PHY recovery/session operation. CHRDET=1 alone does not authorize bypassing the passive-state guard or forcing VBUS.

Private originals and manifest: `evidence-private/20260909-m2-chrdet-result/`.``````

| Original filename | Bytes | SHA-256 |
| --- | --- | --- |
| 10 usb connected at startup.jpg | 229798 | 410156d1d9e9ea85976afaabe6d59a83c054db34faaa56e09b2b2f2eef01be58 |
| 10 no usb connected at startup.jpg | 242813 | 4ffe34fdb744461dce47c9f8ce2c51b6adf02c6d6121119f3a11041ca8757aea |
| 50 no usb connected at startup.jpg | 227000 | dbcac6f3ba3ce1e03b08280eaaf63af3f4766b5bfd3bb4708c2a9f459368b0d2 |

Retained candidate rechecked at 1,097,728 bytes, SHA-256 `e511fb89e45326673183f426a4bdd3b6ca708c25bf3e6ceecfc4a67478aa9660`. Association uses the owner report, directory and displayed build; no independent flash readback, host timing or restoration result is supplied. #23/#27/#28 stay open, M1 stays complete, M2 exit remains blocked and M3/application work deferred.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
