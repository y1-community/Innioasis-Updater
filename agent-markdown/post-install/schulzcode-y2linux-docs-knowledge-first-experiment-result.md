---
title: "Y2B-240 result — Linux PID1 evidence and Android recovery - Innioasis Updater"
description: "Y2B-240 result — Linux PID1 evidence and Android recovery <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identi"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-first-experiment-result.html"
---

# Y2B-240 result — Linux PID1 evidence and Android recovery - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2B-240 result — Linux PID1 evidence and Android recovery

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2B-240 result — Linux PID1 evidence and Android recovery > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-08. The single diagnostic candidate transfer completed and the owner observed a solid green Y2 display. Android was restored through a second BOOTIMG-only transfer and the owner reports normal operation. **Linux 6.18 boot to initramfs PID1 is established by the reported solid-green diagnostic stage; timed heartbeat success is not established.** This concludes this experiment and achieves M1's Linux-plus-PID1 boot objective, while further diagnostic/timing validation remains. No further boot is implied.

## Actual operation and evidence

Times below are SPFT host timestamps, Europe/Berlin, not device power-on times.``````

| Event | Recorded result |
| --- | --- |
| Candidate operation | Download Only started 22:46:10; USB 5-2, VID:PID 0e8d:2000, ttyACM0 detected 22:46:14; S_DONE(0) at 22:46:17 |
| Candidate transfer | BOOTIMG alone, 1,089,536 bytes; authorized diagnostic path; SHA-256 db7d8a5cf082b37f77c8732bd8e1ab742e4205f9383e421b051917f17364ab7e |
| Observation | Owner: “y2 screen is green”; no photograph/UART log or timed sequence supplied |
| Interrupted host wait | Download Only USB wait started 22:50:39, stopped by user 22:50:48; no target connection/image transfer in that wait |
| Restore operation | Download Only started 22:51:28; same USB port detected 22:51:43; S_DONE(0) at 22:51:46 |
| Actual restore image | /home/luca/Dokumente/Code/Y2Player/out/boot-adb/boot.img, 5,875,712 bytes; SHA-256 275870974bbecc74233761753187ee478bfe79ca9d2f2818facd6e0c039c6b43 |
| Android result | Owner reports device works as expected; fresh ADB sees Y2 on USB 5-2, sys.boot_completed=1, stock Linux 3.4.67 and Android 4.4.2 fingerprint |

Actual tool: SPFT 5.2032.00, executable SHA-256 `d618e7d08ba5a4020038921a95336a3805a4b2cf17a374fd308cc5299ea7d9d8`. Actual DA: original bundled `MTK_AllInOne_DA.bin`, SHA-256 `46cd175d7556e6e80b13f6a70827c6931a5dfa25a09c3cc50e75ba7ff9327618`. Original FM scatter SHA-256 `e5fe03e9f3219cc9b5ead27892f2ddb722acc16adce3306d27feb87893cd977e`. GUI and logs retain Download Only, empty auth file and BOOTIMG alone selected. DA checksum level 0 was the existing setting. Transfer checksums are logged; there is no independent post-write SHA-256 readback. Both actual transmitted images are BOOTIMG; no other ROM image transfer is logged. Preloader/LK and the other normal partition entries were disabled; BMTPOOL is reserved/non-download.

The physical BOOTIMG partition remains EMMC_USER [0x01d80000,0x02d80000). SPFT's logged 0x03180000 is its logical address, not a new raw addressing rule. The owner operated the physical device and download controls; the assistant performed host verification/log inspection and read-only Android checks.

## Interpretation and limits

The reviewed diagnostic paints full green only when its proc endpoint receives `I` from task PID1. That endpoint exists after the built-in kernel initcall, and each paint rechecks the watchdog-disabled and inherited-display guards. Taken with the exact candidate transfer and owner observation, this is evidence of installed LK accepting this image, Linux decompression/startup, usable static-DT RAM, initramfs execution, PID1 and the guarded framebuffer path. This is functional evidence for this image/device state, not a complete audit of loader security, all RAM, DMA safety or watchdog behavior over time.

Preceding stripes, white-half changes, terminal checkerboard, reset/freeze behavior and power-on/power-off times were not reported. Do not infer they failed merely because only green was reported. Do not claim the required three timed heartbeat changes or verify the 60-second cutoff from flash timestamps. The two-second sleep result is logged but is not checked before PID1 paints green; green therefore does not independently validate timer accuracy.

Recovery differs from the planned runbook: the owner restored `out/boot-adb/boot.img`, not original FM boot.img (SHA-256 `5ef1bdf28481ee0bf5f3528c1ddd91cf3f4d2d5f39e4d0ea049a8137a30f6af6`). Record the actual successful Android recovery; do not call it an exact FM restore or exact current-image backup. No additional corrective flash is needed just to make history match the plan. Per-feature audio/storage tests were not independently captured; normal operation is owner-reported, supplemented by ADB.

## Smallest next engineering step — proposal only

Make the existing guarded RGB565 output readable with a tiny fixed-font text renderer and bounded status pages. Keep CPU0, D08 memory, watchdog entry and the same framebuffer aperture. Do not initialize another display path or add eMMC/network/USB drivers for this step.

First display a build identifier, PID, boot-stage/error code and heartbeat counter. Then show kernel version, detected memory, CPU online set, uptime, timer interrupt counts and a bounded selection of kernel log records. Linux 6.18 supplies userspace kernel-log access via [/dev/kmsg](https://raw.githubusercontent.com/torvalds/linux/v6.18/Documentation/ABI/testing/dev-kmsg); use nonblocking reads with explicit record/byte limits and truncation/error indicators, not a reader that waits forever after the last record.

Place progress markers before/after each collection operation. Current PID1 turns green, writes several proc/sysfs reports to UART, and only then enters the heartbeat loop. Consequently a delay/block/error in that path is one possible explanation for a persistent green screen, not a diagnosed cause. Screen progress must not depend on draining UART; retain UART as additional output. Define page timings and bounded writes before implementing, then rebuild and repeat offline D08/artifact checks. A later hardware trial requires separate authorization. No M2 or new implementation started here.

Private final logs/hashes/Android capture: `evidence-private/20260908-y2b240-result/`, indexed in `capture-index.tsv`. Earlier captures remain as historical checkpoints and are superseded by this result where they describe restoration or authorization as pending.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
