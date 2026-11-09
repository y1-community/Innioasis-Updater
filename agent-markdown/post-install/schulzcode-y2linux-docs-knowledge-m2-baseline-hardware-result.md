---
title: "M2 integrated baseline — physical results, 2026-09-10 - Innioasis Updater"
description: "M2 integrated baseline — physical results, 2026-09-10 <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m2-baseline-hardware-result.html"
---

# M2 integrated baseline — physical results, 2026-09-10 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2 integrated baseline — physical results, 2026-09-10

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2 integrated baseline — physical results, 2026-09-10 > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

## Latest: BASELINE-03 logs the display handoff; screen remains black

Owner reports LK logo followed by black in BASELINE-03 capture-02, starting 2026-09-10 15:52:10 UTC. This is a fresh boot log, not proof of a reconnect merely because the directory ends in `02`. The 180-second capture contains **102,314 bytes**, SHA-256 `8fb89a7ee79f17a6496aaa24184ebb7596786b33b5e1357cb3ed6145bb966bf6`. USB identity confirms `6.18.0-y2-m2-baseline3`; LOG1 responds, exit0. All kernel records 0–605 are present in order, and PID1 reaches heartbeat184 with USB stage6/result0. `timeout` means the host recording duration elapsed. Original bytes and chunk index are retained in ignored evidence storage; the [capture record](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-baseline-03-capture.json) records integrity, event counts and limitations. Exact flashed hash/restoration remain owner-unreported.````

| Path | Evidence on this unit | Remaining gap / action |
| --- | --- | --- |
| Display startup | Module starts at 13.815s; live LK PHY is adopted, DSI parks and releases inherited power. Linux powers its PHY at reported338MHz, binds OVL/RDMA/COLOR/DSI, registers fb0 and a 60×45-character framebuffer console. Module returns0 at14.309s, without a logged panel-transfer/probe error. | Visible output fails. This narrows the failure beyond the original live-PLL refusal; it does not identify a bad instruction, validate panel identity, or prove pixel delivery. |
| Display IRQs | OVL334, DSI38, RDMA0 in snapshots at heartbeat60 and120. | OVL IRQ activity establishes some frame-completion signaling. Its stationary count can be normal vblank IRQ disabling after an idle console; it is not proof that scanout stopped. No post-modeset KMS state or backlight hardware readback was captured. |
| Wheel | EINT55 fires eight times; eight APT32F register-frame transfers return -110 between11.364s and38.884s. I2C0 completion IRQ count stays0. No scroll events. | EINT activity is now confirmed; successful I2C transport is not. Diagnose controller/pads/clock/DMA/IRQ completion before changing wheel decoding. I2C1 remains untested. |
| Other input | 55 balanced press/release pairs: navigation46, volume6, power3. PMIC EINT25/nested-key IRQs6; keypad IRQs12. | These paths work in this boot. Physical action order/label mapping and repeat/hold behavior are not separately qualified. |
| Core and observation | Four CPUs online, timer/IPIs advance, IRQ errors0. MemTotal19,548kB; post-display MemAvailable12,080kB. USB/PID1 continue through the recording without captured panic/OOM/relay loss. | Confirms usable logging during and after display loading. Reconnect, five-minute cutoff and stress/PM qualification remain open. |

The inherited PHY words are now actual unit evidence: CON0=`0x11`, CON1=`0x3`, CON2=`0x3c000000`, PWR=`0x101`, CON=`0x403`, lane LDO intersection=`0x1`. Inherited rate is still unknown; do not interpret the Linux338MHz report as the LK rate or retune from these words without the complete divider contract.

Independent observation defect: `initramfs/init.c:log_file()` services the relay between arbitrary 2048-byte snapshot chunks. Seven kernel record headers follow partial snapshot lines. A line-start-only parser falsely reports gaps at128, 240,256,272,288,304,336. They are present in the raw bytes; preserve those bytes and fix snapshot framing in the next source iteration. `PID1 LAST ERR: NONE` is not an all-driver health verdict: the wheel timeouts are kernel messages.

Next combined iteration should collect standard post-modeset DRM state and backlight status, expose the existing I2C driver's bounded failure diagnostics, and repair log framing alongside any source-supported controller fixes. Compare display routing/reset/format and actual unit panel/clock evidence; the capture does not justify guessing a new panel table, rate, rail or DMA range. Source review confirms upstream6.18 already limits OVL PITCH_MSB accesses to supporting variants, and the retained BSP computes I2C source as bus frequency/16; neither an obsolete OVL fix nor the donor's dummy66MHz clock is a justified remedy here.

M1 COMPLETE, M2 ACTIVE. This evidence review changes no candidate bytes, memory, PMIC/storage policy or five-minute limit. No new flash or build was performed.

## BASELINE-02 history: loses the responding log relay

The owner reports LK logo followed by black/grey. The 180-second capture at 2026-09-10 15:30:15 UTC identifies `6.18.0-y2-m2-baseline2` / 0525:a4a7 / 480Mbps, sends LOG1, but receives zero bytes, no protocol header, exit2. Empty raw data and chunk index match the retained hash. [Capture record](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-baseline-02-capture.json). USB enumeration is alive; PID1/relay startup or responsiveness is unknown. Neither the failing instruction nor a completed DSI park/modeset is established. The changed screen does not prove that the display driver successfully probed.

The inferred risk is synchronous display initialization preventing observation. BASELINE-03 moves the exact MediaTek controller module into the initramfs and loads it in a separate child after LOG1 starts, retaining the original kernel/ PID1 relay. This is a normal module-lifecycle change, not a guessed panel fix. Also refuse unpowered DSI host transfers after pre-enable errors. The driver remains part of the one combined candidate. [Packaging/startup audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23baseline-03-observation-and-packaging-review--2026-09-10&anchor=baseline-03-observation-and-packaging-review--2026-09-10).

## BASELINE-01 history

M1 COMPLETE; M2 ACTIVE. Owner-tested M2-BASELINE-01, source checkpoint `7c34d35`, reports LK logo only and host USB disconnect after about five minutes. The compiled identity is confirmed in both captures; the owner did not separately report the flashed file hash or Android restoration. No flash was performed by the development agent.

## Capture integrity and limits

[Machine-readable evidence](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-baseline-01-captures.json) records hashes, contiguous byte chunks and key counts. Original directories remain under `out/m2-baseline-01/`; copies are retained in ignored `evidence-private/20260910-baseline-hardware/`.````

| Capture | Bytes / SHA-256 | Kernel sequence / PID1 |
| --- | --- | --- |
| capture-01 | 78,903 / 502006206f4dd109d99fc7a2293f45b44be961f54cb3a858f475009e7264626c | All 0–574; heartbeat 71 |
| capture-02 | 79,568 / 4bfb2e04a121513f9886e2d2468063166825d3d7e05965464907b0ee41b3b7ad | All 0–575; heartbeat 68 |

Both commands used the old 45-second default, not the documented 180 seconds. `status: timeout`, exit0 means the capture duration elapsed with the expected LOG1 header, not a kernel timeout. No relay GAP/ERR/input-error markers or kernel sequence gaps occur. These retain the complete initial kernel records plus the captured runtime, not five minutes of runtime evidence. Different early kernel timestamps and fresh USB lifecycles show separate boots, not a reconnect test.

## What this establishes on this unit````

| Subsystem | Observation / interpretation |
| --- | --- |
| SMP/GPT | All four CPUs online; timer broadcasts and cross-CPU IPIs advance, IRQ error count zero. Release and basic scheduling work; stress/coherency/PM qualification remains open. |
| RAM | D08 retained; MemTotal 19,708kB with the larger kernel. No captured OOM/oops/panic. No expanded-RAM or sustained working-set claim. |
| CCF/pinctrl/PWRAP | Providers probe; inherited AXI reports 273MHz. PWRAP CID2023, upstream MFD/regulators and backlight probe. No full clock-rate/rail-policy qualification. |
| Navigation | capture-02 has three press/release pairs each for codes 105,158,106,164,28. Five navigation channels work through GPIO/pinctrl/evdev. Exact physical label order was not separately recorded. |
| Volume and Power | Volume−114: six pairs; Volume+115: four pairs; Power116: four pairs. Keypad has 20 IRQs; PMIC EINT25 and nested key IRQ each have eight. This confirms the canonical PWRAP/MFD/EINT25 power-key path. |
| Wheel/I2C | Wheel device registers, but no scroll events, EINT55 IRQs or I2C0 transfers occur. Rotation attempt not explicitly reported. Registration alone proves neither controller response nor scroll function. I2C1 has no clients. |
| Display | Permanent DSI probe failure -EBUSY: unrecognized live DSI PLL (record505). BASELINE-01 wrongly assumed LK used the planned Linux PCW/dividers. It refuses before parking the running stream, consistent with the unchanged LK logo. Actual inherited PLL words were not logged; panel identity/timings remain untested. |
| Backlight | Inherited four-channel ISINK PWM, duty32/32 and current step5 accepted. Illumination persists; brightness transitions and Linux panel operation untested. |
| microSD | Native MSDC identifies an SDXC card; CID/CSD recorded, <=400kHz/one-bit policy. No MMC block driver or disk mount/write path. No throughput/filesystem qualification. |
| eMMC | CMD2/CMD9 identity responses obtained. CMD6 intentionally rejected by write policy; -EROFS/-30 and final initialization failure are expected, not evidence of bad pins/clock. |
| USB | Two high-speed ACM boots retain complete initial kernel logs under shared providers. No captured runtime USB errors. One-detach/reconnect and end-of-window behavior remain unqualified. |
| Power status | Regulator selectors are readable; early unplugged power_supply ONLINE=0 agrees with boot sequencing. No charging, battery voltage, thermal or runtime USB-presence transition qualification. |

58 key events in capture-02 are 29 balanced press/release pairs; none come from the scroll device. Remaining low-priority messages: absent disabled RTC/LED/PWRC DT children, unimplemented cache hierarchy description, deliberately disabled kernel memory protection, unsupported VCAMA/VRTC `get_mode` during the read-only regulator summary. No rail write failure is inferred from those mode warnings.

## Next combined iteration

BASELINE-02 separates inherited PHY power adoption from the Linux cold PLL configuration. It reads/logs the safe PHY status words and validates power/LDOs, leaves a live PLL untouched while DSI parks, then retires inherited power without inventing CCF references. Normal modesetting subsequently owns the cold 338MHz configuration. No PLL_TOP read, guessed live frequency or live PLL retune. Incomplete power still fails safely. Add fault tests for the actual PHY callbacks.

Host capture defaults to 180 seconds for either baseline identifier, preserving 45 seconds and the earlier 60-second ceiling for older experiments. The USB 295-second disconnect and owner 300-second maximum from power-on stay intact. The reported five-minute disconnect matches that programmed cutoff, but neither 45-second capture observes the cutoff itself. USB detach does not power off the Y2; end the run using the established owner power/recovery procedure. No automatic shutdown, charging experiment, memory expansion or milestone boundary change.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
