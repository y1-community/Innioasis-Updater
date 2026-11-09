---
title: "M2-USBGUARD-01 — expose the refused USB handoff - Innioasis Updater"
description: "M2-USBGUARD-01 — expose the refused USB handoff <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m2-usb-guard-diagnostic.html"
---

# M2-USBGUARD-01 — expose the refused USB handoff - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-USBGUARD-01 — expose the refused USB handoff

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-USBGUARD-01 — expose the refused USB handoff > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Current next test: [M2-USBACM-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-enumeration.md), a combined guarded enumeration/logging attempt requested by the owner. USBGUARD remains untested and retained as an optional fallback; no additional guard-only test is required.

2026-09-09, localized #23/#27 prerequisite, baseline `de1a6d0`. [Returned CHRDET photos](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-chrdet-hardware-result.md) establish detection but show a connected-start wake refusal with PHY6a=BE instead of the guarded 04. The old presentation hides the other original register values behind unread wake fields. Those missing values prevent an evidence-backed recovery decision.

## Exact change

Keep the existing cached kernel snapshot and every hardware access unchanged. When no extra wake read succeeded and no write occurred, preserve four original USB rows instead of replacing them with zero-filled wake fields:
  - `PRE P:xx D:xx HW:xxxx W:<result>/<written>`: initial POWER/DEVCTL/HWVERS

plus wake result and whether the guarded write happened.
  - `PHY68:xx xx xx xx xx xx xx`: initial PHY68,69,6a,6b,6c,6d,6e, in order.
  - `DMA:` followed by eight four-digit controls, channels 1 through 8.
  - `IRQE TX:xxxx RX:xxxx USB:xx`: original interrupt enables, not status reads.

Each original value uses the USB validity bit; missing fields render as dashes. When extra wake data exists, retain the established before/after layout, but render each control, trim, post-MAC and post-PHY field only when its individual validity bit is set. Preserve wake result, written flag and validity masks. This also handles partial read failures after a write without displaying a fabricated successful readback. The snapshot remains 260 bytes and once/boot.

No new register, retry, refresh, MMIO write, relaxed guard, DMA ownership, IRQ handler, VBUS force, calibration or charger policy. The existing one-byte suspend release remains possible only in the already-reviewed passive state. Screen/build M2-USBGUARD-01; kernel LOCALVERSION changes for identification. No memory or packaging policy change and no major milestone boundary is crossed.

## Targeted validation / owner boundary

Exercise actual ARM PID1 through the existing syscall fixture: preserve distinct raw sentinels on early refusal/first-read failure, show dashes on partial USB, pre-wake and post-write reads, retain errors and reach BEAT 50 without another snapshot read. Sentinel values are synthetic, not additional physical evidence. Add PHY6a=BE to the production guard fixture and assert no extra reads or write. Run affected PID1/text/wake tests plus normal artifact, BOOTIMG, D08, time32 and framebuffer/watchdog validation in one clean build. Compare resolved config, hardware-access sources and linked probe against the retained candidate. Do not repeat unchanged full-source, ROM, recovery or duplicate-build audits.

Stop at the [candidate](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbguard-01-result.md) for a BOOTIMG-only owner test, USB data cable connected to the Linux PC before power-on and left connected. Capture two readable full-screen photos from that same boot, near BEAT 10 and near 50/STOP within the existing maximum 60 seconds from power-on. An unchanged -19/W0 is useful: the four raw rows identify the guard inputs. If wake instead succeeds, retain the success rows and report the exact cable timing; do not manufacture a failure. No enumeration/ttyACM is expected. No physical device action is performed by the agent.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
