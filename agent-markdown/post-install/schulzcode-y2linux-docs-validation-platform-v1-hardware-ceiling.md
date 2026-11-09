---
title: "Y2 hardware capability ceiling campaign - Innioasis Updater"
description: "Y2 hardware capability ceiling campaign <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-platform-v1-hardware-ceiling.html"
---

# Y2 hardware capability ceiling campaign - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 hardware capability ceiling campaign

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 hardware capability ceiling campaign > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

ACTIVE, started 2026-09-26. This report records the exact unit's measured capabilities, source-backed next steps and unresolved limits. A supported mode, compiled feature or short passing test is not a final qualified ceiling. [Identity and regression](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-PHYSICAL-BRINGUP.md%23physical-01-regression-baseline--2026-09-26&anchor=physical-01-regression-baseline--2026-09-26), [issues](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-PHYSICAL-ISSUES.md), [audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23hardware-capability-ceiling-entry--2026-09-26&anchor=hardware-capability-ceiling-entry--2026-09-26).

## Current measured baseline

Initial measurements use Physical 01 boot `4991ba2c-0571-4649-9f7c-9e0318abb952`. A normal reboot after temporary diagnostics restored original binaries and taint 0 on boot `b3d92d70-521e-41d7-bca7-69b4badf00c1`; SFTP and staged suspend use that boot. [Sanitized numeric evidence](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/platform-v1-hardware-ceiling-physical01.json) retains matched benchmarks and private receipt digests. MB/s uses decimal bytes; Mb/s uses decimal bits. Private commands, raw results, exit codes and host UTC are retained under `out/platform-v1-hardware-ceiling/20260926T184237Z-physical01/`.

| Subsystem | Measured state | Remaining ceiling / acceptance work |
| --- | --- | --- |
| eMMC | 8-bit, 13 MHz, legacy, 3.3 V; large direct sequential read/write 10.64/10.65 MB/s; verified random reads/writes | fsync p50/p99 4.36/14.74 ms; durable metadata 44.31/64.48 ms; faster SDR modes remain unmeasured |
| SD | Known-good replacement SD128; 4-bit, 13 MHz, legacy; three large sequential read runs 5.87–5.89 MB/s, writes 5.52–5.81 MB/s | Higher modes only after host/card/voltage evidence; lifecycle, representative cards, scan and playback |
| USB device | USB 2 high-speed ECM, PIO; TCP into unit 39.56–39.65 Mb/s, out 46.56–46.66 Mb/s | RAM SFTP up 3.58–3.72/down 4.39–5.45 MB/s; eMMC up 2.70–2.74/down 4.88–5.42; DMA, retransmissions, reconnect/PM and NCM remain open |
| USB host | No electrical acceptance | Role/connector/VBUS switch/current limit unknown; do not energize VBUS. HID/storage/UAC depend on that proof |
| CPU | Four cores online; 598/747.5/1040 MHz at existing 1.15 V policy | Exact bin selects stock table 0: 1196 MHz/1.20 V, 1300 MHz/1.25 V; regulator/SPM transition and per-OPP qualification required |
| Core/idle | WFI; GPT 100 Hz with broadcast to dummy local clockevents | Manual 1–4-core cycles pass. GPT6 13 MHz/PPI29 physical diagnostic passes; integrated high-resolution/tickless and deeper SPM states remain unqualified |
| Suspend/RTC | RTC UTC write/read/ticking pass; NTP synchronized; deep mode compiled | Recovered log: freezer/devices/platform/processors return; USB IRQ overflow after devices and radio restart failure after processors. Fresh reboot restores health. Core/SPM and Power/RTC wake remain open |
| GPU | 500.5 MHz, matching prior exact stock branch; screen-off runtime suspended | Load/frame-time/temperature/resume/endurance; no unsupported clock expansion |
| Memory | 952288 KiB usable, HIGHMEM retained, process PSS readable | Throughput/latency/pressure and DMA review; preserve reserved regions |
| Charging | SDP allocation 500 mA, configured 450 mA; CC/HOLD/recharge behavior and battery voltage observed | Owner has no external meter presently. Input/pack current and positive energy balance are unmeasured; source/load curves and pack evidence required |
| Battery/SOC | No qualified current, coulomb count, SOC or percentage | Exact MT6323/stock/pack path; calibrated estimate only if fuel gauge unavailable and real curves support it; identify source internally |
| Low battery | Thresholds explicitly disabled | Measured warning/critical/reserve before full notification/checkpoint/audio/SQLite/sync/shutdown proof |
| Wi-Fi | WPA2/DHCP/ordinary DNS/NTP/TCP; 65 Mb/s reported link, measured local TCP 45–47 Mb/s | Reconnect/AP loss/reboot, source-backed aggregation/offload review, coexistence and endurance |
| Bluetooth | Actual SBC, S16_LE stereo at negotiated 48 kHz direct / 44.1 kHz Reborn; clean owner-confirmed audio and Reborn play/pause | Fixed temporary Reborn app plays >3 min with zero errors; trace did not capture incoming control. Fresh pairing, reconnect, endurance/coexistence and codecs remain open |
| Wired audio | Actual S16_LE 44.1/48 kHz, clean direct playback and switches | Longer Reborn/screen-off/load qualification before product 48 kHz promotion; real DL1 24-bit transport before 88.2/96; no inference from 32-bit slots |
| CS43131 | Existing DAC playback; truthful unavailable jack IRQ telemetry | Exact IRQ/load/gain topology; upstream/documented features only, no guessed high gain |
| OTA/recovery | Pinned recovery access and retained candidate fallback | Stable storage/power/core first; signed staging/install/readback/health/rollback; broken app test retains explicit owner approval |
| Endurance | Storage/radio/audio/hotplug baseline passes; devices-stage suspend causes recovery failure | Long runs and repeated lifecycle cycles; no platform freeze yet |

## Matched library results after the wider bus

Receipt `17` supersedes the overlapping first `05` run for attribution. Old Telemetry 01 and new Physical 01 ARM binaries run serially on the **same 8-bit, 13 MHz system** with unchanged 1k/10k/20k workloads. All count/integrity checks pass. Cache is uncontrolled; these are synthetic short-WAV metadata workloads, not a compressed-audio decode or cold-media benchmark.

| Tracks | Binary | Population ms | Page p50 / p99 ms | Commit-64 p99 ms | Initial / incremental scan s |
| --- | --- | --- | --- | --- | --- |
| 1k | old | 92.299 | 6.895 / 7.427 | 5.866 | 3.900 / 0.154 |
| 1k | new | 109.545 | 2.384 / 2.860 | 6.984 | 4.154 / 0.192 |
| 10k | old | 2035.236 | 45.233 / 49.378 | 566.759 | 46.380 / 3.752 |
| 10k | new | 3434.218 | 2.067 / 2.428 | 578.580 | 52.553 / 7.666 |
| 20k | old | 4639.869 | 93.435 / 97.478 | 579.307 | 98.253 / 12.789 |
| 20k | new | 7387.706 | 2.080 / 2.448 | 562.513 | 114.573 / 18.251 |

Historical one-bit commit p99 at 10k/20k was 3384.874/3363.743 ms; the old binary now reaches 566.759/579.307 ms. This strongly supports a bus-width contribution, while the historical/current comparison still has uncontrolled cache/run differences. On the same current bus, query/index changes take pages from 45.233/93.435 ms to 2.067/2.080 ms. Conversely, new indexes increase population and scan time; do not present them as a universal speedup. Existing exact-query/index A/B receipts separately isolate SQL behavior.

20k completes without count/integrity failure. Full track-list construction remains about 45 ms p50, and the new 20k workload consumes about 79.7 s user CPU plus 22.4 s system CPU over 161.1 s. Faster storage alone will not remove the remaining scanner/metadata/SQLite/UI cost. No additional library optimization preceded these measurements; the final interactive library envelope remains open until physical UI/load/endurance qualification.

## Recovery and playback findings

The real Reborn player rejected a valid opened sink because native `rb_sink_open` left the returned device name empty. Its contract correctly rejected that mismatch. Repair populates the actual name and validates outputs; checks are retained. The new ALSA null-PCM regression failed before the repair; all seven audio tests passed afterwards. Temporary fixed ARM app SHA-256 `8072c34e2daf0534a62e1affd755e4bb37a20bd12a504ba55be7daa400960a6a` played SBC for 182.955 seconds with zero XRUN/recovery/decode/playback failures. The owner reports clean audio and working play/pause; the captured trace did not include an incoming AVRCP command. The direct fixture's control failure is therefore not a product AVRCP failure. Original binary, exact saved session and library were restored; only the qualification fixture was deleted.

Normal reboot after diagnostics passed in about 14.5 seconds to recovered SSH, with taint 0, unchanged versions, clean root/data/SD error counters, 8/4-bit 13 MHz legacy buses and ordinary checked DNS. The host stream then lost USB while `pm_test devices` was running. **Receipt 49 retrieves the persistent log and supersedes the initial incomplete interpretation**: freezer, devices, platform and processors all returned on the same boot with taint 0. The processors stage records CPU3/2/1 power-off result 0 and all three coming back. No core-stage or actual SPM-entry receipt exists.

Return from `pm_test` did not restore the platform. At uptime 822.388990 s, after devices, `Y2USB stopped stage=6 result=-75 IRQ=477827 events=05` records the driver's interrupt-burst guard terminating USB. After processors, WMT opcode 08 parameter 02 times out with -110 and Wi-Fi enable fails. These are specific failure locations, not established root causes. The old suspend helper swallows radio restore errors, so its rc=0 is insufficient. The SSH-bound staged harness also advanced without checking USB health; future qualification must run one stage at a time with a persistent local result and host recovery check.

Power/cable attempts did not recover access. The owner's first reported restart was not confirmed by boot identity. Reborn's Power Menu → Reboot then produced a fresh splash and restored pinned USB SSH: boot `fffb5ac5-fba4-4729-967f-858e6d4aaf17`, unchanged exact Physical 01 versions, taint 0, pm_test none, all four CPUs online, root/data/SD error counters 0, unchanged 8/4-bit 13 MHz IOS and quick health OK. Further suspend requires observability and correction/qualification of the restore path, not a guessed SPM register change. Hardware 02 adds a first-overflow register snapshot and makes radio-restore errors fail the helper; neither change claims to repair the underlying interrupt/radio failure.

## Hardware Batch 2 implementation boundary

[Full admission audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23hardware-batch-2-build-admission--2026-09-26&anchor=hardware-batch-2-build-admission--2026-09-26) admits a grouped host build. [Hardware 02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-HARDWARE-02.md) now passes release validation and is ready for one owner flash. None of its new modes is physically qualified:
  - Storage: 8/4-bit SDR high speed at existing 3.3 V, inherited stock source,

initial 25 MHz cap; root-only `y2_clock_limit_hz` on the host accepts only 13/25/50 MHz caps while owning the idle host. Negotiated card speed stays an upper bound; actual IOS frequency must be measured. Clock stability waits are bounded at 20 ms; failed changes restore the preceding clock and cap. Failed restoration rejects subsequent requests before command/DMA preparation and requires reboot into the safe profile. `y2.mmc_safe=1` preserves the 26 MHz crystal / 13 MHz legacy fallback. No DDR/UHS/HS200/voltage change; no automatic CRC downshift claim.
  - USB: upstream Inventra DMA via the source-backed shared interrupt, 32-bit

DMA addressing and explicit bus-fault teardown. `y2.usb_dma=off` retains PIO; controller allocation failure also uses PIO. A DMA fault terminates the session; a live request is never silently replayed through PIO. Host power stays electrically blocked.
  - Timer: existing GPT owner starts stock GPT6, checks counter progress against

GPT2, then permits the physical architectural timer on PPI29. Failed setup or `y2.local_timer=off` retains GPT/dummy fallback. No always-on declaration across power-down/suspend. Long counter continuity, NO_HZ/high-resolution, core hotplug and PM still require physical qualification.
  - Reborn: include the physically tested sink metadata repair in the paired

root image. No audio precision, codec or product-rate promotion is implied.

## Source findings that constrain the next batches
  - The existing MSDC driver already uses DMA. Request queue policy and protected

stock-partition translation must remain intact. Exact stock board data says eight/four pins and advertises high-speed modes; that alone does not validate a different signal voltage or timing edge. Exact LK writes selector 1 for both MSDC hosts; stock hclks[0]=200 MHz and the inherited MSDCPLL is ~400 MHz. This supports the source-1 / PLL-div2 inference used for bounded SDR testing, without PLL retuning. The actual eMMC reports EXT_CSD revision 8 / card type `0x57`; card capability is not board qualification.
  - Exact stock local-timer setup requests per-CPU interrupt 29 and calibrates

the physical CP15 timer against jiffies. Userspace reads of CNTFRQ/CNTPCT/ CNTVCT trap on every current core (`12`); this proves only that EL0 access is unavailable. Privileged reads then found the counter stopped; stock GPT6 initialization was absent. Receipt `34` starts only GPT6, measures 12 rates from 12,999,956 to 13,000,027 Hz and 12 successful PPI29 deliveries across four cores (10.001377–10.003376 ms for 10 ms requests), then restores original controls and unloads. Effective NO_HZ/high-resolution acceptance still needs the integrated kernel and long-run tests.
  - Exact stock MUSB uses its integrated DMA with a sampled W1C status byte at

offset `0x200` and aggregate interrupt bit 3. Current glue masks that bit. Linux's existing MediaTek MUSB implementation provides the corresponding no-separate-IRQ DMA integration; MT6582 layout, ownership, DMA mask and reconnect/error fallback must be reconciled before activation.
  - Exact stock CPU tables include higher bins and voltages, unlike the current

three fixed-voltage entries. The active unit's bin was read and matched; a generic MT6582 maximum is insufficient. Actual devinfo bits select stock table 0: 1300/1196 MHz require 1.25/1.20 V. Existing 1040 MHz at 1.15 V stays until the regulator/SPM voltage-transition contract is implemented.
  - External current measurement is unavailable. Voltage trends, configured

current and PMIC/CPU die temperatures must remain distinguishable from measured battery current, pack temperature, SOC or useful charge energy.

Ordinary test failures stay recorded while independent investigation continues. Data corruption, unsafe thermal/electrical behavior or loss of recovery stops the affected experiment. No higher clock, voltage, unknown VBUS path or memory reclamation is justified by the campaign name alone.

## USB networking compatibility decision

ECM remains the recoverable installed profile while Inventra DMA is qualified. NCM can aggregate frames, but a class name alone does not prove better Y2 throughput or host compatibility. The pinned Linux source contains both the `f_ncm` gadget and `cdc_ncm` host driver. Microsoft's current USB class-driver matrix lists `UsbNcm.sys` for Windows 11 and Windows Server 2022; it does not establish Windows 10 support. [Microsoft USB class drivers](https://learn.microsoft.com/en-us/windows-hardware/drivers/usbcon/supported-usb-classes). Apple's 2026-09-21 accessory guide, section 38, specifies NCM 1.0 for Ethernet over USB; that is source support for investigation, not a tested macOS version matrix on this gadget. [Apple Accessory Design Guidelines](https://developer.apple.com/accessories/Accessory-Design-Guidelines.pdf).

NCM remains a deliberate later profile with ECM fallback, subject to actual Windows/Linux/macOS enumeration, raw TCP/CPU measurements, transfers and reconnect/PM tests. It is not enabled in Hardware 02 without those results.

## Recovered network and RTC follow-up

Receipts 50–52 retain exact Physical 01 identity on boot `fffb5ac5`. Ordinary DNS succeeds in 16–35 ms and shared radio status has both functions active, error/transport_errors/recoveries 0. The observer nevertheless reports one `supplicant_unavailable` sample and DEGRADED health. This preserves PHY-020; it does not erase receipt 49's earlier OK or equate the observer timeout with failed DNS/association.

The RTC still carried 2022 while the system clock was NTP-synchronized. Source inspection explains the missing automatic update: `ntp_event` requires an explicit RTC write qualification policy, which is not enabled. A standard `hwclock -w -u` now succeeds and reads back 2026-09-26 21:15:09 UTC. Three later samples advance by two seconds each, about 1.18 seconds behind the system clock; the short sample and integer RTC resolution do not establish drift. No RTC register workaround is needed from this observation. Reboot/full-power retention and alarm wake remain pending, and the earlier date is not evidence of a failed retention test because no prior qualified write was established.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
