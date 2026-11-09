---
title: "M2-BASELINE-02 — correct live display PHY handoff - Innioasis Updater"
description: "M2-BASELINE-02 — correct live display PHY handoff <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-m2-baseline-02-result.html"
---

# M2-BASELINE-02 — correct live display PHY handoff - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-BASELINE-02 — correct live display PHY handoff

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-BASELINE-02 — correct live display PHY handoff > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Owner tested: black/grey screen and no responding log relay. The [hardware result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-baseline-hardware-result.md) supersedes the original offline handoff below. M1 COMPLETE, M2 ACTIVE. Build starts from `7c34d35` plus this source iteration. [BASELINE-01 captures](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-baseline-hardware-result.md) confirm four CPUs, the five navigation channels, volume/Power, shared PMIC ownership and card identity, but show DSI failing before native display takeover.

Image:`/home/luca/Dokumente/Code/Y2Linux/out/m2-baseline-02/BOOTIMG.img`
Size: 2,015,232 bytes
SHA-256:`13754b8f5ac49d173bce85f854b9683d23a2f3dc798b23309a1aa7197a4a8a34`
Identity: Linux `6.18.0-y2-m2-baseline2`, LOG1 `M2-BASELINE-02`.

## Change and validation

BASELINE-01 incorrectly required LK's live PLL divider/PCW to equal the planned Linux cold configuration. BASELINE-02 gives only the MT6582 PHY its own power callbacks: validate/log live power and lane LDO state, adopt it **without writes or a rate claim**, park DSI, then release inherited PHY power without decrementing unowned CCF references. Normal modeset acquires balanced CCF references and programs the existing cold sequence. Incomplete live power still refuses probe; there is no PLL_TOP read or live PLL retune. Safe CON0/CON1/CON2/PWR/CON/lane words are logged for subsequent diagnosis. Other SoCs retain their original PHY ops.

All core subsystems from [BASELINE-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-baseline-01-result.md%23what-actually-changed&anchor=what-actually-changed) remain integrated, including USB/reconnect, input, PMIC, clocks, DRM, read-only MMC discovery and SMP. No input-driver change is inferred from the absence of wheel activity: capture-02 confirms buttons but not rotation. The host tool now defaults to 180 seconds for baseline builds; old builds retain 45 seconds.

One clean kernel build, no compiler/DT warnings or errors; resolved config/DT, actual linked artifacts, D08 layout and final BOOTIMG pass validation. **26 test methods pass**, including real PHY callbacks under traced MMIO/CCF for unchanged live adoption, cold sequencing, missing-power refusal and CCF errors; plus provider write filters, ARM evdev/relay, USB lifecycle and host capture defaults. ARM PID1 selftest passes. No duplicate reproducibility/provenance/recovery audit. [Layout](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-baseline-02-layout.json), [test/package manifest](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-baseline-02-iteration.json), ELFs/config/logs and 113 snapshotted source inputs are retained with SHA256SUMS under `out/m2-baseline-02/`.

D08 remains 24MiB + 512KiB, with the original low16KiB reservation; image/BSS span 5,191,568 bytes. Expanded RAM still needs LK-heap/live-DMA ownership evidence. PMIC rail/current/charger writes, MMC writes/mounts/rootfs installation, audio/radios/FM, GPU/apps and suspend/DVFS remain excluded. Production thermal, charging and shutdown policy is not implemented. No full input/clock/DRM/USB qualification is claimed; panel identity/init/timings, native framebuffer DMA, wheel response and reconnection still need this physical test. If native display fails, retain USB logs and classify the actual next error.

## Owner flash and one-boot test
  - In the existing SPFT v5.2032, use

`/home/luca/Dokumente/Code/Y2Player/y2_v3.2.0_FM-20260813/MT6582_Android_scatter.txt`. Download Only, all rows unchecked except BOOTIMG, selecting the image above. Check the hash; use the already proven manual flash/power sequence. Never select preloader/LK, format/upgrade or other partitions.
  - Stop SPFT, unplug and start capture below before normal power-on. Keep the

test microSD inserted. Start a 300-second timer at power-on, boot unplugged, attach USB after 10 seconds. No display prompt is required. If logs do not arrive within 30 seconds of attachment, end through the known recovery route.
  - During capture, observe whether readable Linux console replaces LK's logo;

record geometry, flicker, backlight and warmth. Press/release each navigation button, Volume−/+, then briefly Power; **slide a finger around the capacitive wheel clockwise and counterclockwise**. No long Power hold as an input test, CPU stress or charging experiment. Report the physical action order.
  - Optional single reconnect after capture: only if at least 80 seconds remain,

unplug, start the second command below and reconnect after five seconds. Preserve both captures. Do not restart the device timer.
  - Stop on abnormal warmth/faults/lost observation; end by 300 seconds using

the established owner power/recovery sequence. USB intentionally disconnects near 295 seconds and does not power the unit off. Restore BOOTIMG only with the known `/home/luca/Dokumente/Code/Y2Player/out/boot-adb/boot.img` through the same Download Only procedure. Report restoration; do not restore full ROM.

Real-host commands (new output directories; no need to guess ttyACM numbering):`cd /home/luca/Dokumente/Code/Y2Linux sudo python3 tools/observation/usb_log_capture.py --build M2-BASELINE-02 \ --seconds 180 --output out/m2-baseline-02/capture-01`

Optional reconnect capture, started while unplugged:`sudo python3 tools/observation/usb_log_capture.py --build M2-BASELINE-02 \ --wait-seconds 30 --seconds 60 --output out/m2-baseline-02/capture-02`

Capture `timeout`/exit0 normally means the requested recording duration ended; check raw logs for actual kernel errors. Both prior captures were separate boots, so they did not qualify reconnect. The five-minute ceiling and USB cutoff remain unchanged for this same-scope iteration. **No further device action by the agent; await this manual flash and its complete logs.**

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
