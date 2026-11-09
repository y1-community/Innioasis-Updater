---
title: "Y2 Hardware Final implementation candidate - Innioasis Updater"
description: "Y2 Hardware Final implementation candidate <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-hardware-final.html"
---

# Y2 Hardware Final implementation candidate - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 Hardware Final implementation candidate

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 Hardware Final implementation candidate > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Implementation-first continuation of Astra's `022e6ee` handoff, 2026-09-27. Software implementation, runtime enablement and physical qualification are independent. This pass does not contact, reboot or flash the Y2. The device remains on restored original Hardware02. Existing volume, pairing, checksum, timer and DMA fixes are retained. No repeated campaign audit was performed.

One consolidated candidate is software validated at `out/y2linux-hardware-final-candidate/`. Exact built source identities and final validation results belong to its manifest and `validation/summary.json`. Current source implementation is complete up to the documented technical and electrical boundaries; this is not a claim that every desired native hardware mode is implemented. See [capabilities](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-HARDWARE-FINAL-CAPABILITIES.md).

## Implemented in this continuation
  - Automatic standard SDR storage negotiation up to 50 MHz with asynchronous

50 -> 25 -> 13 MHz transport-fault containment; no implicit replay of writes. UUID-less SD uses CID, partition geometry and filesystem identity while keeping mount generation/inode replacement protection. FAT, exFAT and ext4 remain.
  - Dual-role MUSB host core, USB audio/storage/HID classes and NCM modules compile.

The role interface refuses host activation before session/VBUS writes. ECM remains the built-in recovery gadget; NCM is packaged but cannot replace that built-in gadget at runtime. DMA and `y2.usb_dma=off` PIO fallback are retained.
  - schedutil, existing source-backed DVFS and stock-bin high OPP gates; failed

voltage decrease now checks actual readback and attempts restoration, then contains unknown/unsafe readback at the lowest known clock. Reborn publishes bounded per-client workload and 250 ms interaction leases, never per-core MHz.
  - Stock SLIDLE bus DCM/WFI wrapper with shared clock ownership, eligible single

CPU and peripheral gate preflight, readback/rollback, abort/failure counters and WFI fallback. It is compiled and disabled by default. Runtime CPU power-down idle is a separate unresolved context/CIRQ/deadline integration.
  - Configurable source-backed charging ceiling (70/450/650 mA supported selectors;

per-source limits still apply), stock precharge/CV/termination/recharge/watchdog protections retained. Voltage is not raised beyond the 4.175 V source default.
  - Battery SOC chooses hardware capacity, calibrated hybrid or filtered voltage

estimation. An estimated, provisional profile is separate from code. Filtering, rest/sag handling, charge/discharge hysteresis, bounded monotonic smoothing, full/empty corrections and missing-sensor fallback are implemented. Real BAT0 current/counter/temperature are consumed only if exposed; no fake pack sensors.
  - Reborn battery percentage and source/confidence diagnostics. Schema-2 low

battery warning/critical/shutdown support preserves schema-1 owner policies. Provisional SOC warns; only measured/calibrated SOC can independently shut down. Conservative voltage floor remains independent, with bounded countdown.
  - Standard Wi-Fi off/standard/automatic power save with actual readback; automatic

defaults off. Coexistence traffic/CPU/link observations expose future policy hooks without guessing final bitrate rules. Existing DHCP/DNS/reconnect and single-owner Bluetooth reconnect/AVRCP remain.
  - Pinned optional AAC, aptX, aptX HD and LDAC encoder builds are integrated into

the full root. Explicit owner Experimental policy enables optional endpoints; production Auto still consumes qualification/distribution flags. Peer support, request, negotiation and active PCM remain distinct. SBC/XQ, LDAC standard/ mobile/high and ABR policy are implemented; SBC is the fallback. This is an owner-private package, not certification or public distribution approval.
  - Native S16 44.1/48 admission and application rate switches, 88.2 -> 44.1 and

96 -> 48 family conversion, then S16/44.1 fallback if opening fails. Inspected exact MT6582 sources do not define native wide DL1 fetch or >48 kHz clocks; no guessed register layout or false S32/native-high-rate claim was added.
  - Source-backed NTP -> RTC synchronization with durable trusted-time floor and

owner disable precedence; bounded alarm replacement/cancel/readback API.
  - Versioned capability, battery/power/audio/codec configuration receipts tied to

update compatibility and checked against both root tar and ext4 image. Runtime per-CPU highres/NO_HZ and storage error/fallback telemetry are added.

Existing Linux suspend/pm_test, Power/RTC wake routing, USB/radio restoration, GPU/runtime display PM, codec controls, memory diagnostics, signed root OTA, recovery and endurance tooling are retained. Deep suspend remains gated because Astra did not obtain a successful same-boot resume or a discriminating first failure snapshot. This pass does not invent a fix for that unresolved failure.

## Validation and package boundary

Kernel/config/DT, platform host tests, Buildroot and Reborn ARM, Reborn host tests, fmt/strict Clippy, QEMU/installed ARM, FFmpeg/ALSA, package/ELF/dependency, source/license, preserving-data and exact Hardware02 fallback checks are required before the candidate handoff. Results are recorded as they complete; physical qualification is not a prerequisite for producing the package.

No Y2DATA image, partition migration, firmware download on-device, reserved RAM reclaim, NVRAM/calibration write, automatic BOOTIMG OTA or flash is included. Both repositories retain local `hardware-final` commits and configured identity. User documentation/assets remain outside the candidate source checkout.

The next activity is one [physical qualification campaign](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-HARDWARE-FINAL-QUALIFICATION.md) on this assembled platform. Failed or absent evidence never promotes a flag.

## Completed software validation, 2026-09-27

Built pair: Linux `067003f8988042a832181e935128ea93e26070a7` / Reborn `5b5d23b89952d88faf3155cf680ccce918f1b099`. Kernel/config/DT and BOOTIMG memory/partition limits pass without extending any reservation. Buildroot ARM and Reborn ARM, 202 production tests, 189 Reborn workspace tests, fmt/strict Clippy, QEMU application/FFmpeg/ABI checks, installed ARM platform/SQLite/ALSA checks, and 382 ELF files / 1396 dependency edges pass. Signed update/preserving package and exact Hardware02 BOOTIMG/Y2ROOT fallback validation pass. Source inventory covers 105 selected packages and their pinned hashes.

Package includes source bundles, locked kernel/Buildroot archives, Buildroot source/license collection and qualification tools. Legal collection warnings for external-toolchain/local-package recipe metadata are retained, with local source and GPL text supplied separately. Optional codec certification/public distribution remains unapproved; this is a local owner package. Byte-identical rebuilds are not claimed. No device access, flash, push or physical/endurance qualification occurred.

The source pair above is the actual built pair. A later documentation-only commit records these results and is archived separately; it does not change firmware provenance. The engineering campaign remains open for the structured later phase.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
