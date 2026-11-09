---
title: "Y2 Hardware Final physical qualification - Innioasis Updater"
description: "Y2 Hardware Final physical qualification <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-hardware-final-qualification.html"
---

# Y2 Hardware Final physical qualification - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 Hardware Final physical qualification

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 Hardware Final physical qualification > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

One structured campaign for the assembled, software-validated candidate (Linux `067003f` / Reborn `5b5d23b`). No test in this document has been executed by this implementation pass. Device remains on original Hardware02; this checklist does not flash it. Candidate and fallback identities are bound by package manifest.

Before any later installation use the existing preserving BOOTIMG/Y2ROOT procedure and exact Hardware02 fallback. Keep Y2DATA, authorization, firmware provenance and calibration unchanged. Record boot/source IDs, requested versus actual mode/clock, workload/load, duration, before/after errors, counters and observed result. Preserve the first failure snapshot. No full audit or repeated unchanged ROM/recovery extraction is part of this campaign plan.

| Area | Structured cases | Promotion criteria / retained fallback |
| --- | --- | --- |
| Storage | Isolated 13/25/50 MHz eMMC/SD readback, sequential/random and durable filesystem/SQLite; 1k/10k/20k library; multiple SD cards including UUID-less FAT, exFAT/ext4; remove/reinsert/source replacement. | Error-free actual negotiated mode and durable contents; verify automatic lower cap/error counters. Restore 25/13 on faults. Never replay uncertain writes. |
| USB device | Matched PIO/DMA TCP both directions, RAM/eMMC/SD SFTP, reserves/ENOSPC, detach/reconnect, service restart and suspend. | Compare delivered bytes to directional programmed counters, bus faults/retransmits/CPU/thermals. PIO/ECM recovery always available. |
| USB host / NCM | First establish exact VBUS circuitry and supported role activation. Then externally safe host audio/storage/HID cases. NCM only after gadget-selection/FIFO integration. | No unknown VBUS energizing; unsupported host role stays refused. NCM compilation is not an active-path pass. |
| CPU | schedutil all baseline OPPs; each workload lease and crash/expiry; interactive latency; heavy DSP/crossfade, scan, transfer; four-core online/offline. Only source/bin-admitted high OPPs in a separate controlled voltage-readback case. | No fixed-MHz application control; QoS release and thermal authority hold. Errors contain clock/voltage and retain known-good table. No overclock/undervolt experiments. |
| Timers | Per-CPU clockevents, highres and actual NO_HZ; long counter rollover, deadline/sub-tick sleeps, hotplug/migration, broadcast and resume. Repeat legacy boot option. | Correct deadlines/continuity on all online cores, truthful runtime telemetry and boot fallback. |
| Cpuidle | WFI baseline, source-gated SLIDLE with one CPU and valid peripheral/clock state; measure entry/residency/wake and abort/failure counters. | No changed clock owner after abort/exit; failures latch WFI. Runtime CPU power-down remains a technical gap until context/CIRQ/deadline integration exists. |
| Suspend/wake | Persistent one-stage pm_test, first USB-overflow/SPM/radio failure snapshot; CPU/device/timer/USB/CONSYS/Wi-Fi/BT/DRM/ALSA restoration; then Power and RTC wake. | Same-boot successful resume and restored subsystems; failed preparation refuses suspend. Existing failure must be resolved before qualification. |
| Charging | SDP/CDP/DCP/legitimate vendor class, enumeration budget, real external current, precharge/CV/termination/recharge/watchdog and unplug/fault. | Limits remain within source/pack ceiling; meter tunes/qualifies limits rather than gating driver implementation. |
| Battery | Voltage/no-load/load/charging filter response; real FG/current/thermistor only if available; calibrated profile across charge/rest/discharge. | Quantify SOC accuracy/confidence, sag/hysteresis/monotonic behavior; publish calibration separately. Estimated source stays provisional until measured. |
| Low battery | Warn/critical/recovery/countdown under load, source changes and charging; hard floor independently; preserve data/audio shutdown. | Adequate reserve and no sag-triggered false shutdown; provisional SOC must not become independent shutdown authority. |
| Wi-Fi | Association/auth failures, DHCP/routes/DNS/NTP, AP loss/reconnect, service/reboot restore; isolated throughput; off/standard/automatic PS and readback. | Stable recovery, truthful Online state, error and power/latency evidence. Off/conservative settings retained on failure. |
| Bluetooth | SBC then XQ/AAC/aptX/aptX HD/LDAC with compatible peers; request vs negotiation vs active PCM; Auto qualified and explicit Experimental; LDAC mobile/standard/high/ABR; AVRCP/pair/bond/reconnect/window. | Audible correctness, no XRUN/growth/reconnect regressions; codec flag only for actually tested peer/mode/source. AirPods cannot qualify aptX/LDAC. |
| Coexistence | Every eligible codec with Wi-Fi off/idle/heavy transfer, library scan and UI; link/CPU/pressure/traffic instrumentation. | Tune later priorities/bitrates using measured stability; no inferred 990 kbps requirement or fabricated ABR bitrate. |
| Wired/codec | 44.1/48 rate changes, source 88.2/96 conversion, 24-bit fixtures at decoder/DSP/conversion boundary, volume/mute/filters/power and screen-off. Native S32/high-rate physical proof only after exact controller implementation. | No claim of preserved low bits across S16 conversion; active ALSA format/rate truthful, safe resampling fallback and no high-gain surprise. |
| RTC | Trusted-time boot sanity, NTP -> RTC, reboot/off retention, alarm replace/cancel/interrupt and same-boot wake. | Clock never treated trusted from build floor alone; failed alarm readback cancels. |
| GPU/memory | Renderer wake/blank/runtime PM, 480x360 navigation/artwork, screen-off power, PSS/LOWMEM/HIGHMEM/cache/slab growth and PID reuse. | Smooth user operation, no unbounded growth or reserved-memory reclamation. |
| OTA/recovery | Signed root update compatibility/configuration, interruption/restore, health timeout/rollback and exact fallback. | Existing data remains intact and BOOTIMG rescue cannot be silently replaced by root OTA. |
| Endurance | One combined long campaign: at least 8 h each representative wired/Bluetooth playback, network/USB/storage overlap, repeated reconnect/rate/power/suspend cycles. | Errors, XRUNs, memory growth, battery/thermal/residency and recovery bounded; all failed/unperformed cases retained. |

Use existing `y2-platform status`, `capabilities`, `health`, `collect`, storage/ library/network/USB/audio qualification tools and `y2-suspend` pm_test staging. Diagnostic artifacts are evidence, never implicit activation authorization for unknown electrical paths. Promote defaults and qualification flags only for measured final-candidate behavior. The implementation candidate remains useful with unqualified capabilities and conservative/default-disabled activation.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
