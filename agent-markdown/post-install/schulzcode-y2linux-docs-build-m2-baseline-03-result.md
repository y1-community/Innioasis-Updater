---
title: "M2-BASELINE-03 — keep the log reader ahead of display probing - Innioasis Updater"
description: "M2-BASELINE-03 — keep the log reader ahead of display probing <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate id"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-m2-baseline-03-result.html"
---

# M2-BASELINE-03 — keep the log reader ahead of display probing - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-BASELINE-03 — keep the log reader ahead of display probing

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-BASELINE-03 — keep the log reader ahead of display probing > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

**Owner-tested: logging responds through display initialization; screen remains black.** M1 COMPLETE, M2 ACTIVE. The 180-second capture-02 contains all kernel records0–605 and PID1 through heartbeat184. DRM/fb0/module initialization returns success; wheel I2C reads time out. See the [physical result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-baseline-hardware-result.md%23latest-baseline-03-logs-the-display-handoff-screen-remains-black&anchor=latest-baseline-03-logs-the-display-handoff-screen-remains-black). The artifact and original handoff procedure below are retained unchanged.

BASELINE-02 enumerated over USB but its 180-second capture contained zero bytes. The owner saw black/grey after LK. [Evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-baseline-hardware-result.md) does not identify the failed instruction or establish PID1 responsiveness.

Image:`/home/luca/Dokumente/Code/Y2Linux/out/m2-baseline-03/BOOTIMG.img`
Size: 2,129,920 bytes
SHA-256:`dae729341fd52d3abe16899ec332b2fdacd2a0fcbde15e796d496a0c443fa543`
Identity: Linux `6.18.0-y2-m2-baseline3`; LOG1 `M2-BASELINE-03`.

## What changed and why

MediaTek DRM is the sole loadable module, packaged as `/display.ko` in the RAM-only initramfs. Its dependencies and all other baseline core drivers remain built in. PID1 starts first, completes its initial provider snapshots and accepts LOG1. After heartbeat12 and successful relay output, it starts one separate child through ordinary clone/finit_module calls. PID1 stays on CPU0; the child loads on previously observed CPU1. Parent checks child completion with wait4(WNOHANG), logs pending status every 15 seconds and never waits synchronously for module initialization. No retry, unload, shell or external module discovery. A session starting at heartbeat240 or later skips display loading to respect the test window.

This isolates synchronous driver-probe waits from the existing logging process; it cannot guarantee survival of a global bus fault or shared-kernel lockup. The child log records module start/result, and DSI records PHY acquisition, parking, release, host registration and command-engine initialization. LOG1 and kernel/PID1 relay use the original single USB writer and transport. No new USB console or endpoint changes. Module loading starts automatically within this one baseline test; it does not require a separate controller/register flash.

Also fixed a source-level safety gap: MT6582 panel transfers now return `-EHOSTDOWN` before touching DSI MMIO if pre-enable/power-on failed. The existing 6.18 host-before-panel bridge ordering is already correct and was not re-ported. Panel initialization values, live/cold PHY sequence and timing remain as in BASELINE-02; this candidate does not claim to have diagnosed/fixed the actual black-screen cause without a kernel log.

The [packaging/startup review](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23baseline-03-observation-and-packaging-review--2026-09-10&anchor=baseline-03-observation-and-packaging-review--2026-09-10) retains D08, SMP/GPT/watchdog policy, CCF/pinctrl/EINT/PWRAP/PMIC, input, MMC identity/read-only enforcement and USB reconnect/deadline. Disk writes/mounts, charger/rail/current policy, audio, radios/FM, GPU/apps and production PM remain excluded. No original loader, partition layout, calibration or donor source changed.

## Validation and retained artifacts

One clean kernel build tree; hidden DRM dependency selections and a diagnostic placement compiler error were corrected there. Final kernel/module have no compiler warnings/errors or unresolved modpost symbols. Exactly one modules.order entry; ARM32 relocatable ABI, build vermagic and empty external module dependencies checked. The exact module bytes must match the initramfs; foreign/extra module entries and changed payloads fail validation. All loader syscall table entries are real linked implementations, including clone, wait4, affinity and finit_module.

28 applicable test methods pass: shared provider/PHY guards, host and ARM input/relay/loader faults, USB lifecycle/capture, exact module archive/caps and mutated real artifacts. The final loader-order refinement prevents clock/regulator snapshots from racing a stuck display clock operation; only PID1/initramfs/DT and BOOTIMG were repackaged, with affected loader/artifact tests rerun. The kernel was not rebuilt for that refinement. ARM PID1 selftest passes. Intermediate package is retained under `out/m2-baseline-03/intermediate/`, not the flash candidate.

D08 map unchanged. Kernel Image 5,017,024B; BSS310,856B; resident span5,327,880B. PID1 817,800B plus module154,460B = 972,260B regular-file payload, within the existing 2MiB cap; compressed initramfs62,733B fits its 512KiB bank. Full emitted layout/relocation/package validation passes. Runtime module allocation/COW and working-set headroom still require observation; no arbitrary RAM expansion. [Layout](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-baseline-03-layout.json), [test/package manifest](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-baseline-03-iteration.json), ELFs/config/module/logs and source snapshots with SHA256SUMS are retained under `out/m2-baseline-03/`. No repeated ROM/source-tree/recovery audit or reproducibility build.

## Owner flash and one-boot test
  - Existing SPFT v5.2032, original

`/home/luca/Dokumente/Code/Y2Player/y2_v3.2.0_FM-20260813/MT6582_Android_scatter.txt`: Download Only, every row unchecked except BOOTIMG, image/hash above. Use the established owner flash/power sequence; no format, upgrade or other row.
  - Stop SPFT and unplug. Start capture below before normal power-on. Keep the

test microSD inserted. Start an independent 300-second timer at power-on; boot unplugged and attach after 10 seconds. LK logo initially remaining is now expected: display probing starts only after the log reader is active.
  - Capture for 180 seconds. Observe the screen transition after USB starts,

test navigation and volume, briefly press Power, and slide a finger around the capacitive wheel both directions. Record physical action order. A later black/grey screen is not display success; keep recording if logging is healthy. If no response arrives within 30 seconds after attachment, or logging stops unexpectedly, end via the known recovery route rather than waiting blindly.
  - Optional single reconnect only with at least 80 seconds left: unplug, start

the second command, reconnect after five unplugged seconds. The display module must not be loaded a second time. No timer restart or second detach experiment.
  - End on abnormal warmth/faults or by 300 seconds from power-on. USB cutoff

around295s does not power off the unit. Use established owner power/recovery steps and restore BOOTIMG only from `/home/luca/Dokumente/Code/Y2Player/out/boot-adb/boot.img`. Report restoration.
`cd /home/luca/Dokumente/Code/Y2Linux sudo python3 tools/observation/usb_log_capture.py --build M2-BASELINE-03 \ --seconds 180 --output out/m2-baseline-03/capture-01`

Optional reconnect, command started while unplugged:`sudo python3 tools/observation/usb_log_capture.py --build M2-BASELINE-03 \ --wait-seconds 30 --seconds 60 --output out/m2-baseline-03/capture-02`

No automatic hardware qualification from exit0; retain complete capture directories. A zero-byte/exit2 result is failed observation even when enumeration succeeds. Stop for the owner's manual flash; no physical device was written by the agent.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
