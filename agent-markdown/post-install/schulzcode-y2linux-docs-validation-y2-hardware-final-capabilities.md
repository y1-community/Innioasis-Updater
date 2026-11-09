---
title: "Current platform capability evidence - Innioasis Updater"
description: "Current platform capability evidence <!-- knowledge-base-scope: maintained-capability-summary; baseline02-sync 2026-10-03 -- Baseline02 source and UART01 hardware — 2026-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-hardware-final-capabilities.html"
---

# Current platform capability evidence - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Current platform capability evidence

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Current platform capability evidence

## Baseline02 source and UART01 hardware — 2026-10-03

Baseline02 is sealed/software-tested and enables qualified CPU0 C3 automatically through guarded boot policy. Its new-image/cold-boot hardware state remains PHYSICAL_NOT_RUN. Latest physically verified pair is UART01, Linux `e9e8d63f9c94232c2b6627881e0967583e202dac` and Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`, same boot `fd955840-35d9-47db-83e0-ff47d6bb2d2b`, taint 0.

| Capability | Exact bounded UART01 evidence | Limit |
| --- | --- | --- |
| C1 WFI | Four cores, advancing entries/residency, rejected 0, 400 bounded wakes | Baseline02 regression pending |
| C2 SLIDLE | +6,971 entries / 84.3473% residency; clock restore failures 0 | Endurance/SD-absent variant separate |
| C3 DORMANT | 21 guarded reset-and-return trials; +3,624 normal entries / 65.2450%; final 3,647 checked returns | New automatic cold boot, injected CIRQ edge coverage and endurance separate |
| Timers / hotplug / parking | GPT6/GPT4/PPI29/CNTFRQ/highres/NO_HZ; 18 hotplug transitions; natural CPU0/owner 0xe | No new timer architecture |
| Guarded active DVFS | All five 598 / 747.5 / 1040 / 1196 / 1300 MHz OPP readbacks before/after C3 | Mixed charging/endurance/natural thermal trips not established |
| Storage idle/wake | eMMC and inserted SD: eight fsynced checksum rounds each after C2 and after C3; errors 0 | Not every high-speed mode/fault/endurance |
| Demand wake / playback / USB | Screen/workload restore, real FFmpeg/ALSA fixture, three USB 1 MiB bidirectional hash rounds with independent Wi-Fi observer | Not perceptual fidelity/optional BT/host/reconnect endurance |
| Full system suspend / Power+RTC wake | No new acceptance | Remains a separate open gate |
| Battery SOC / savings | Provisional policy; no new electrical measurement | No battery-life improvement claim |

This documentation ledger does not set runtime capability qualification flags. [Baseline02 receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md), [UART01 physical record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md), [feature inventory](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-COMMUNITY-BETA-FEATURE-AUDIT.md) and [current state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md) govern current summaries. Earlier Fix01/Fix02 FAIL/NOT_TESTED rows below remain valid for their own images.

## Historical exact-image capability ledgers

The following text retains earlier dated decisions and results. Its “current”, “next” and candidate labels belong to those sessions; the Baseline02 summary above takes precedence. Historical failures and seal-time NOT_RUN receipts remain evidence for their exact images.

# CPU Final Fix02 physical observations — 2026-09-29

The [Fix02 physical report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX02-PHYSICAL-QUALIFICATION.md) is the current CPU evidence for installed Linux `1a1a6693` / Reborn `77cf83e0`, kernel `6.18.0-y2linux-cpu-final-fix02`, root `2025.02.18-platform-v1.8`. It supersedes matching Fix01 rows below. Overall Fix02 acceptance is FAIL, not production qualification. No runtime capability flags or implementation source were changed.``````

| Capability / observed scope | Physical state | Evidence limit |
| --- | --- | --- |
| Timers, highres/NO_HZ, hotplug, schedutil, eight QoS classes, thermal override, C1 | PASS | regression gate; no natural thermal trip induced |
| MSDC0/MSDC1 runtime clock gating | PASS | gated at rest, CCF 0, 16/16 hash rounds with caches dropped, no errors |
| C2 SLIDLE | FAIL | zero entries; clock mask 0 radios-off, refused by TOPCKGEN+4 0x0 ≠ 0x0f |
| System-idle coordinator | PASS | parks 3→2→1 and restores on display wake; wake counted as pressure restore |
| High-bin admission / voltage DVFS | PASS | 1196 @ 1.20 V, 1300 @ 1.25 V readback; sampled ordering; bounded integrity |
| C3 DORMANT | NOT_TESTED | preflight unmet: topology, frequency, domains, clocks, bus |
| SRAM journal self-test / warm retention | PASS | one ordinary warm reboot |
| Charger refusal / staged PM levels | PASS | active charging -EBUSY; all five pm_test levels same boot |
| Full RTC suspend | FAIL | SPM return proven; backstop reset after device resume, before PM exit |
| Power wake / RTC cycles / resume restoration | NOT_TESTED | no same-boot full resume |
| USB loaded transfer | FAIL | 0/10 1-MiB rounds; EP1 RX DMA IRQ storm, reproducible, attributed |
| SD media lifecycle | FAIL | kernfs-keyed inventory remounts after inode reclaim (non-CPU) |

# CPU Final Fix01 physical observations — 2026-09-27

The [Fix01 physical report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01-PHYSICAL-QUALIFICATION.md) is the current CPU evidence for installed Linux `0de6e951` / Reborn `36db1869`, kernel `6.18.0-y2linux-cpu-final-fix01`, root `2025.02.18-platform-v1.7`. It supersedes only matching older CPU observations below; the immutable Hardware Final inventory is preserved as history. Overall Fix01 acceptance is FAIL, not production qualification. No runtime capability flags or implementation source were changed.

| Capability / observed scope | Physical state | Evidence limit |
| --- | --- | --- |
| GPT6/GPT4/PPI29, local timer | PASS | all CPUs, CNTFRQ 13 MHz, hotplug continuity, sole GPT4 broadcast ownership |
| High-resolution timers / NO_HZ | PASS | actual timer_list state, stopped ticks, ~1.09-ms requested 1-ms sleeps |
| Conservative cpufreq / schedutil | PASS | 598/747.5/1040 MHz exercised; bounded CPU/memory integrity |
| Thermal authority over QoS | PASS | cooling cap overrides real heavy lease; not an induced heat trip |
| Workload QoS / Reborn producers | PASS | all eight real classes, renew/expiry, screen-off interaction release |
| CPU1–3 hotplug / C1 WFI | PASS | repeated transitions, advancing local IRQs and WFI residency |
| C2 SLIDLE | FAIL | zero entries; MSDC0/MSDC1 clock ownership remains after runtime suspend |
| System-idle coordinator | PARTIAL | no automatic parking in 120/160-s observations; sustained eligibility unproven |
| High-bin admission / voltage DVFS | PARTIAL | software VOSEL recognized at 1.15 V; PWRAP readiness rejects high OPPs; voltage changes NOT_TESTED |
| C3 DORMANT / CIRQ deadline handoff | NOT_TESTED | disabled; clock/domain prerequisites and recovery gates unmet |
| Suspend devices-stage attempt | FAIL | no same-boot recovery; owner Power ineffective, restart required |
| Charger clean refusal / other staged levels | NOT_TESTED | attached USB was not active charging; no further PM entry after failure |
| Full RTC/Power wake / full restoration | NOT_TESTED | no successful staged basis; new boots are not resumes |
| Persistent suspend diagnostics | PARTIAL | durable kernel_suspend survives; SRAM records invalid, exact kernel boundary unavailable |
| Awake RTC alarm/PMIC IRQ | PASS | bounded alarm while awake; not deep wake qualification |
| Native fixture playback | PASS | bounded 44.1 and 24/96->48, zero XRUN/decode/filter errors; no perceptual fidelity claim |
| Wi-Fi data | PASS | four small SHA-verified roundtrips; final health has supplicant telemetry discrepancy |
| CONSYS bounded isolation/retry | PASS | independent radio restart reproduces exactly one timeout/retry then WLAN/HCI/calibration success |
| USB data / sustained recovery | PARTIAL | first hash roundtrip passes; next transfer loses connection while UI remains usable; owner restart |
| Filesystem safety / recovered runtime health | PASS | rw root/data/SD, ext4 counters 0, taint 0; not failed-interval panic proof |

Timers and performance leases are now narrow physical successes. M4 power, M2/M5 transport recovery and M6 production gates remain open. The coherent Fix02 plan in the report covers PM diagnostic safety, PWRAP readiness, MMC runtime ownership/coordinator reachability and loaded USB recovery. No Fix02 was built.

# CPU Final continuation — 2026-09-27

The following CPU Final and Hardware Final inventory is a **historical software scope**. The physical Fix01 table above takes precedence for current observed behavior. See [current platform state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md) for overall acceptance and remaining gates.

The CPU rows below now describe [CPU Final](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL.md) source implementation. The Hardware Final package remains immutable; CPU Final has its own candidate. CPU Final software checks and its single preserving package now pass at runtime source Linux `ff586df` / Reborn `afcf9ff`; exact receipts are in the CPU Final report. This changes implementation/default reporting, not physical qualification. Physical qualification remains false. Other capability rows retain Hardware Final semantics. Runtime telemetry reports actual admission and fallback state.

# Y2 Hardware Final capability ledger

Built implementation/default inventory, Linux `067003f` / Reborn `5b5d23b`, 2026-09-27. Every flag describes this candidate, not historical Hardware02 evidence. `implemented`, `enabled`, `qualified` and `experimental` are independent. Runtime `y2-platform capabilities` resolves radio and codec enablement from the installed inventory and explicit owner policy; active codec/PCM is observed separately. Actual timer and storage state is in `y2-platform status`.``````````````````````````````````````````````````````````````````````````````````````````````````````

| Capability | Implemented | Default enabled | Qualified | Experimental | Reason / limit |
| --- | --- | --- | --- | --- | --- |
| telemetry | true | true | false | false | physical qualification of this exact candidate pending |
| health | true | true | false | false | physical qualification of this exact candidate pending |
| storage | true | true | false | false | physical qualification of this exact candidate pending |
| wifi | true | false | false | false | physical qualification of this exact candidate pending |
| bluetooth | true | false | false | false | physical qualification of this exact candidate pending |
| usb_device | true | true | false | false | physical qualification of this exact candidate pending |
| usb_host | true | false | false | true | VBUS physical validation pending; host role refused before session or VBUS write |
| audio | true | true | false | false | S16 44.1/48 enabled independently of qualification; high source rates convert with explicit fallback |
| power_observation | true | true | false | false | SOC estimate available; pack current/temperature remain unavailable unless real BAT0 properties exist |
| low_battery_shutdown | true | true | false | false | conservative stock-boundary voltage floor; provisional SOC only warns |
| deep_suspend | true | false | false | false | same_boot_resume_unqualified |
| cpuidle | true | true | false | false | physical qualification of this exact candidate pending |
| system_watchdog | true | false | false | false | AP_watchdog_driver_available_recovery_policy_unqualified |
| ota | true | true | false | false | physical qualification of this exact candidate pending |
| automatic_bootimg_update | false | false | false | false | single_slot_rescue_can_be_lost |
| shutdown | true | true | false | false | physical qualification of this exact candidate pending |
| emmc | true | true | false | false | physical qualification pending |
| sd | true | true | false | false | physical qualification pending |
| usb_dma | true | true | false | false | physical qualification pending |
| usb_ncm | true | false | false | true | module compiled; ECM remains recovery default; NCM activation and FIFO integration pending |
| local_timer | true | true | false | false | physical qualification pending |
| high_resolution_timers | true | true | false | false | physical qualification pending |
| no_hz_idle | true | true | false | false | physical qualification pending |
| cpufreq | true | true | false | false | physical qualification pending |
| dvfs | true | true | false | true | stock-bin voltage control implemented; high stock OPPs default gated |
| workload_qos | true | true | false | false | physical qualification pending |
| cpu_hotplug | true | true | false | false | physical qualification pending |
| slow_idle | true | true | false | true | automatic stock single-CPU/clock preflight, readback and WFI fallback; residency unqualified |
| cpu_power_down_idle | true | false | false | true | CPU Final adds stock runtime PCM, Linux context, CIRQ replay and GPT4 broadcast; conservative single-CPU/media-domain preflight |
| charging | true | true | false | false | physical qualification pending |
| battery_soc | true | true | false | false | physical qualification pending |
| rtc_time | true | true | false | false | physical qualification pending |
| rtc_alarm | true | false | false | true | alarm software implemented; same-boot suspend wake pending |
| wifi_power_save | true | false | false | true | off/standard/automatic implemented; automatic defaults conservatively off |
| radio_coexistence | true | true | false | false | instrumentation and policy hooks implemented; no final bitrate overrides |
| bluetooth_sbc | true | true | false | false | runtime enablement uses compiled inventory and explicit Experimental gate; physical qualification pending |
| bluetooth_sbc_xq | true | false | false | true | runtime enablement uses compiled inventory and explicit Experimental gate; physical qualification pending |
| bluetooth_aac | true | false | false | true | runtime enablement uses compiled inventory and explicit Experimental gate; physical qualification pending |
| bluetooth_aptx | true | false | false | true | runtime enablement uses compiled inventory and explicit Experimental gate; physical qualification pending |
| bluetooth_aptx_hd | true | false | false | true | runtime enablement uses compiled inventory and explicit Experimental gate; physical qualification pending |
| bluetooth_ldac | true | false | false | true | runtime enablement uses compiled inventory and explicit Experimental gate; physical qualification pending |
| wired_48 | true | true | false | false | source-backed native S16 path enabled; full candidate qualification pending |
| audio_rate_conversion | true | true | false | false | physical qualification pending |
| wired_s32 | false | false | false | true | exact MT6582 DL1 wide-fetch/high-rate register path not defined in inspected pinned sources; source-backed conversion fallback implemented |
| wired_native_88200 | false | false | false | true | exact MT6582 DL1 wide-fetch/high-rate register path not defined in inspected pinned sources; source-backed conversion fallback implemented |
| wired_native_96000 | false | false | false | true | exact MT6582 DL1 wide-fetch/high-rate register path not defined in inspected pinned sources; source-backed conversion fallback implemented |
| cs43131_controls | true | true | false | false | physical qualification pending |
| gpu_runtime_pm | true | true | false | false | physical qualification pending |
| display_off | true | true | false | false | physical qualification pending |
| memory_telemetry | true | true | false | false | physical qualification pending |
| diagnostics | true | true | false | false | physical qualification pending |

## Defaults, fallbacks and tuning``````

| Group | Default and fallback | Physical qualification / tuning |
| --- | --- | --- |
| eMMC / SD | Standard SDR automatic maximum 50 MHz; faults lower to 25/13; 8/4-bit. No DDR/UHS/HS200. CID/geometry identity accepts missing UUID. | Matched scratch readback/durable tests, multi-card/removal, maximum stable clock, fault counters, endurance. |
| USB | Inventra DMA; y2.usb_dma=off PIO. ECM/ACM USB-only key-auth SFTP; reserves and durable publication retained. | DMA delivered throughput versus programmed counters, RX/TX, reconnect/suspend, retransmits and ENOSPC publication. |
| Host / NCM | Host stack/classes compiled, role refused before VBUS. NCM/dependency and host audio/dependencies carried by BOOTIMG within unchanged size limits; default built-in ECM remains. | Exact VBUS topology before host activation. NCM needs a reviewed gadget-selection/FIFO integration; compilation alone is not active NCM. |
| CPU / timer | schedutil, 598/747.5/1040 MHz table; bin-checked 1196/1300 automatically admitted after voltage handshake; voltage floor 1.15 V. Per-open expiring QoS, interaction 250 ms. GPT6/PPI29 with legacy fallback. | OPP transitions/readback, scheduler/QoS, thermal limits, all-core hotplug and timer continuity/broadcast/highres/tickless residency. Floors/durations provisional. |
| Idle / suspend | WFI/automatic preflight SLIDLE; experimental DORMANT adds distinct PCM/CIRQ/GPT4/context. Deep suspend explicit existing owner qualification path and pm_test. | SLIDLE entry/abort counters/residency/wake. Suspend staged failure snapshot, CPU/USB/radio/DRM/ALSA restoration, Power and RTC same-boot wake. |
| Charging | Source-aware BC1.1, stock protections, 4.175 V; supported 70/450/650 mA configurable ceiling. No arbitrary charger voltage/current. | Real external current, source class/USB enumeration, pack ceiling, thermal behavior, termination/recharge/watchdog. |
| Battery | Estimated table in /etc/y2linux/battery-profile.json; private owner override in /data/system/platform. Hardware/hybrid takes precedence when real. Sensors absent -> null/state-only. | Rest/charge/load/discharge calibration replaces provisional curve, qualified current/resistor/NTC only if actual hardware path exists. |
| Low battery | Provisional SOC warns; independent 3.4 V floor after five samples, ten-second grace; schema-1 owner policy retained. | Reserve, load-sag immunity, warning/countdown/recovery, SOC trust and final thresholds. No synthetic shutdown demonstration here. |
| Wi-Fi / coexistence | Retained checksum repair. Standard power-save callback, automatic conservatively off, off fallback. Traffic and CPU/link hooks, no bitrate override. | Association/DHCP/DNS/NTP/reboot/AP-loss, PS readback/power/latency, isolated throughput and all-codec heavy coexistence. |
| Bluetooth | SBC default. Experimental policy enables compiled private optional codecs and XQ; qualified production Auto separate. LDAC standard/ABR, 990 not mandatory. | Peer/negotiated/active PCM agreement, every codec, AVRCP, reconnect/screen-off/endurance and CPU/radio pressure. Source/license inventory retained. |
| Wired / CS43131 | Native S16 44.1/48; high source rates convert by family then 44.1 fallback. Existing hardware volume/filters/DAPM; no automatic high gain/load work. | Rate switching, low bits, I2S clocks, clicks/volume/screen-off; load sensing needs verified board measurement path. |
| RTC | UTC read/write/persistent floor; NTP sync source-backed, owner override; bounded alarm API doesn't enter suspend. | Retention across reboot/off, alarm interrupt and same-boot wake, bad-time recovery. |
| GPU / memory | Existing renderer/display/runtime PM and PSS/LOWMEM/HIGHMEM/cache/slab/growth observation. Reserved regions unchanged. | 480x360 smoothness, screen-off/wake power and repeated memory-growth tests. |
| OTA / recovery | Platform v1 root-only signed OTA/exact kernel; configuration contract v2 and battery/power schemas included. BOOTIMG remains preserving manual update. | Interrupted update/recovery/health/rollback later. This package includes only BOOTIMG/Y2ROOT and exact Hardware02 fallback, no data image. |

## Technical gaps, separate from qualification

Native S32/24-bit preservation and native 88.2/96 lack an exact MT6582 DL1 fetch, interconnect and clock programming path in the inspected pinned source. The conversion architecture is implemented; native modes are honestly false. CPU Final implements runtime dormant context, CIRQ replay and Linux GPT4 broadcast with the distinct stock runtime PCM; experimental entry remains conservatively gated. NCM is compiled/packaged with activation integration pending. CPU Final adds MUSB quiesce/stale-status ordering and isolated bounded CONSYS boot retry for captured restoration faults; new same-boot restoration is unqualified. Actual net battery current/charge counter and pack temperature remain absent when no hardware property exists. These are substantive limits, not merely `qualified=false` labels for nonexistent implementations.

Astra's physical evidence and exact source/provenance index remain in [the handoff](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-HARDWARE-FINAL-HANDOFF.md). Optional codec provenance/licensing and native-audio register analysis remain in [the source review](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-HARDWARE-FINAL-RADIO-AUDIO.md).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
