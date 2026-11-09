---
title: "Y2P-400 — M4 end-user production power platform - Innioasis Updater"
description: "Y2P-400 — M4 end-user production power platform <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2p-400.html"
---

# Y2P-400 — M4 end-user production power platform - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2P-400 — M4 end-user production power platform

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2P-400 — M4 end-user production power platform > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Historical September 15 issue snapshot. The subsequent POWER-03 owner acceptance and current physical limits are recorded in the [current platform state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md). The pending-deployment language below describes this original checkpoint.

OPEN / ACTIVE / PARTIAL. POWER-03 is built; awaiting owner manual BOOTIMG deployment and physical qualification. Do not start M5.

## Corrected production candidate — 2026-09-15

Source `16875c4acc813b54c781167883227cf289f4dfcd`, Linux `6.18.0-y2linux-m4-power-03`. All 74 production/M4 tests, ARM rescue ABI/shell checks, DT/config/memory/loader checks, package validation and 12 package rejection cases pass. No physical deployment or POWER-03 hardware pass is claimed.
  - BOOTIMG: 5408768 bytes, SHA256 `66b6ecd5ef54da6f3ea07be2c9deda284d0a7636e9c6da4c5d72d84eca5fc010`.
  - Fallback POWER-02: 5378048 bytes, SHA256 `1852dfc995953f86ef5c47349515e8d6f06478daa6c1a89efe0f223501c226c9`. It retains the known charging failures.
  - Only BOOTIMG changes. Preserve installed Y2ROOT, Y2DATA/schema 1, owner SSH, stock loaders/tables and protected calibration. No root/data image is included.

Corrections: stop charging immediately at the 4.175-V target, confirm voltage-limited completion while inhibited, recharge after 60 seconds below 4.110 V. Preserve the 4.2-V fail-closed software guard; use the actual stock 4.3-V battery-OVP selector without disabling its detector. Retain first-fault registers and clear a real fault only after verified removal/engine stop and safe samples. Current source limits remain 450-mA configured SDP, at most 650-mA CDP/DCP/Apple, conservative 70-mA unknown; stock-evidenced low-voltage limits remain.

Fix MT6323's stock 1968 RTC epoch for time and alarm, preserve spare fields, enable RTC boot time and boot ID. Read the thermal efuse words with 32-bit accesses instead of the observed byte truncation; physical temperature accuracy remains to be verified. Give the MUSB session a kernel runtime-PM reference with release on detach/resume before reentry, replacing the POWER-02 userspace pin. Preserve the integrated SPM/offline architecture, s2idle fallback and 598/747.5/1040-MHz OPPs at the stock-proven 1.15 V. No guessed lower voltage or new power platform.

[Manual BOOTIMG deployment and coherent qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fbuild%2Fy2linux-m4-power-03-deployment.md) · [Build receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fbuild%2Fevidence%2Fy2linux-m4-power-03%2FREADME.md) · [Implementation and exact policy](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fknowledge%2Fm4-end-user-power.md) · [Subsequent owner-accepted M5 baseline](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fbuild%2Fy2linux-m5-connectivity-01-deployment.md).

## Actual installed baseline

POWER-02 remains installed until owner deployment. The completed entry audit verified its full image-length hash above and working p5/p7 root/data/SSH. It reached 4.200073 V then latched voltage fault 0x8 and stayed inhibited as voltage fell; the focused follow-up still found that latch around 3.74 V. The separate earlier OVP 0x10 lacks its original detector snapshot and is not yet explained physically. A 12.96-second DCP observation and two reconnects under the userspace runtime pin do not qualify sustained charging or final USB behavior.

Earlier inspected SPM counters were entries=0/resumes=0, RTC reported 2082, and CPU thermal conversion was implausible. The source corrections above are not substitutes for physical acceptance. The owner explicitly directs focused M4 completion using the completed audit; no broad audit, M5, GPU or player work.

[Retained physical failure evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2F67cbe8f1df439a25eb542fc5c6f35fc57b758430%2Fdocs%2Fhardware-evidence%2F2026-09-15-m5-entry%2FREADME.md) · [Roadmap](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).

After the owner reports POWER-03 running, perform one coherent session over SSH/standard interfaces, with owner cable/button/audible observations. Require actual SPM resumes/residency, unchanged boot/process/mount/data identity, separate Power and RTC wake, all resume regressions, sustained PC/wall/bank charging, real termination/recharge and low-battery recovery, offline lifecycle, reboot and actual hardware-off. Make targeted fixes for concrete failures. Close only when mandatory physical gates pass.

Required physical acceptance:
  -  Sustained positive charging gain and useful stock-evidenced current policy, never above the actual Y2 stock ceiling; retain 4.175 V unless a justified stock CV change is established.
  -  PC SDP, detectable CDP, DCP wall charger, power bank and conservative unknown-source behavior; charger detection must work without gadget enumeration and USB descriptors must match bus-power behavior.
  -  Safe low-battery/precharge and empty-battery recovery without Android; establish stock preloader/LK/Linux responsibilities and boot thresholds.
  -  Charger insertion/removal/source changes, watchdog, safety faults, coherent state machine, termination and recharge with real hysteresis and bounded time.
  -  Offline charging in production rescue/initramfs before switch_root: native charging UI, timed screen blank, brief status request, deliberate Power-on while still connected, and low-power watchdog servicing.
  -  Off + wall/PC/power-bank insertion stays offline; completion stays offline; removal powers off; reinsertion returns offline; normal poweroff with charger connected returns offline instead of booting the normal OS.
  -  Truthful battery/external-power telemetry and stock-equivalent protections; no fabricated pack temperature, measured current, SOC or Full state.
  -  Calibrated CPU/PMIC die thermal readings, bounded load/cooling and repeated supported OPP transitions; voltage DVFS only with actual Y2 evidence.
  -  WFI fallback, safe deeper idle where evidenced, real deep suspend with low standby consumption and SAME Linux session restored; s2idle fallback remains available.
  -  Intended Power/RTC/source wake; wheel must not wake accidentally.
  -  Display/backlight, buttons/volume/wheel, ALSA/CS43131 playback, internal root/data, optional SD and USB restore; coherent charging and filesystem integrity.
  -  RTC read/set, reboot persistence, suspend alarm, deep wake and off persistence where supported; no unrelated RTC spare/boot writes.
  -  Clean reboot, actual hardware poweroff, subsequent normal Power-button boot and powered-off charger behavior.

Battery percentage, calibrated battery current and pack Celsius may remain explicitly scoped follow-ups only under the owner's stated conditions. These optional telemetry gaps do not waive charging, recovery, offline charging, deep suspend or any other hard power gate.

M3 residual 48 kHz/channel/repeat tests and wider #33 storage tests stay separate. USB reconnect #27 stays separate unless directly required for this qualification. The latest owner request is focused M4 completion and explicitly stops M5. Do not start radios, GPU or Y2PlayerNative. Close #30 only after the actual physical matrix passes and a final boundary audit records source/evidence commits, exact candidate/fallback paths and hashes, qualified policies, results and remaining limitations.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
