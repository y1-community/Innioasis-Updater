---
title: "M2-BASELINE-01 — integrated Linux 6.18 core development baseline - Innioasis Updater"
description: "M2-BASELINE-01 — integrated Linux 6.18 core development baseline <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-m2-baseline-01-result.html"
---

# M2-BASELINE-01 — integrated Linux 6.18 core development baseline - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-BASELINE-01 — integrated Linux 6.18 core development baseline

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-BASELINE-01 — integrated Linux 6.18 core development baseline > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-10, starting from clean main 4dde305. **Owner tested; partial core success, DSI handoff failed.** See the [physical results](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-baseline-hardware-result.md). The original offline report and flash procedure below are historical. M1 remains COMPLETE, M2 ACTIVE. This [scope audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23m2-baseline-01-integration-authorization--2026-09-10&anchor=m2-baseline-01-integration-authorization--2026-09-10) supersedes separate M2-INPUT-01/USBACM-04 prerequisite flashes. It does not close M2 or change the blueprint, rootfs/application plan, or M3/M4/M5 gates.

Image:`/home/luca/Dokumente/Code/Y2Linux/out/m2-baseline-01/BOOTIMG.img`Size: 2,015,232 bytes SHA-256:`6cba96dbcb529d46f2c5ca51d5e2a7c62ca90aaa005d2173e24558437cbe8598` Linux 6.18.0-y2-m2-baseline1; LOG1 header M2-BASELINE-01.

## What actually changed

At 4dde305 only CPU0/GIC/GPT, stopped AP watchdog, inherited text, guarded USB PIO/ACM/PID1 logs, offline reconnect and polled navigation were implemented. The following are now compiled and connected in the same candidate. “Integrated” is a source/build result, never confirmation on this older physical Y2.``````````

| Subsystem | Integrated design / first-boot interpretation |
| --- | --- |
| CPU/timer/watchdog | Four CPUs using upstream MediaTek release keys at SRAMROM 10202000; no hotplug/SPM power sequence. Proven GPT retained, upstream dummy per-CPU clockevents plus ARM tick broadcast are linked. No invented architected-timer IRQ. Exact early AP watchdog-stop instructions still validated; no production watchdog/reboot driver. |
| USB/logging | Original guarded unplugged PHY wake, MUSB PIO and ACM; USBACM-04 one-reconnect lifecycle retained. Startup snapshot now precedes display/storage device probes. PWRAP and clock reads use their shared owners. USB deadline 295s from its early start; PID1 285 heartbeat iterations; neither replaces the owner's wall-clock cutoff. |
| CCF | Read inherited ARM/MAIN/UNIV/MM/MSDC PLLs and AXI mux; BSP-derived fractional/divider arithmetic, no PLL/CPU retuning. Real AXI parents and /16 I2C contract replace donor's approximate 66MHz placeholder. Reviewed infra/peri/MM gates. Unresolved MM/PWM parents report zero, never a fabricated VENCPLL rate. Shared SMI/mutex gates remain on for this bounded LK handoff. |
| GPIO/pinctrl/EINT | Minimal reviewed navigation, I2C0/1, SD1 and LCM mux/bias groups; gpio-ranges and pinctrl ownership. MT6582 register layout with upstream 6.18 EINT library. Parent SPI113 HIGH; PMIC EINT25 HIGH, wheel55 FALLING. Keypad and eMMC retain LK pad setup. No generic full-pad/drive-strength claim. |
| PWRAP/MT6323 | One serialized WACS2 regmap owner, shared with USB; upstream MT6397-family MFD and MT6323 regulators. No competing raw owner or wrapper exception IRQ. Write firewall allows only PMIC interrupt mask/status, power-key IRQ selection, backlight PWM duty/enables. Rail, charger, current and reset-policy writes fail -EPERM; regulators have no voltage constraints/consumers. |
| I2C/input | Native I2C0 and empty I2C1 with AP-DMA; wheel register-zero + repeated-start nine-byte frames. Navigation, wheel, volume keypad and upstream PMIC power key produce evdev. PID1 discovers all four names, verifies opened names, captures initial held keys and press/release events, including deferred devices. |
| DRM/panel | Separate MT6582 OVL format, RDMA FIFO, COLOR/mutex/MMSYS variants; existing 6.18 OVL pitch fix retained. 480×360 GC9503V candidate with LK command table, RGB888 two-lane sync-pulse link and MMSYS reset routed through GPIO112. Linux allocates the framebuffer in D08; old raw framebuffer/devmem mechanisms are absent. Standard fbcon replaces the diagnostic screen. |
| PHY/DSI/backlight | Actual 338MHz PLL contract for the donor's programmed PCW, evidence-based cold enable order, no PLL_TOP reads or unnecessary access after lane shutdown. Park inherited stream before OVL takeover; balanced probe references; bound a stuck DSI hard IRQ and mask it on timeout. Backlight holds inherited current/clock settings, uses monotonic PWM up to the lowest inherited duty, propagates errors and attempts rollback while dark. Cold/unrecognized ISINK setup fails probe safely. |
| microSD/eMMC | Upstream MSDC variant, inherited-DMA-idle guard and documented 26MHz crystal source; one-bit bus, card rate capped at 400kHz. No MMC_BLOCK, disk mount, filesystem, write/erase/vendor command or eMMC CMD6. CID/CSD responses are logged. eMMC may intentionally fail initialization at its first configuration switch; identity before that is useful. SD identification/SCR is useful, not a throughput/rootfs qualification. |
| Basic power | Standard read-only y2-usb-presence power_supply ONLINE from previously evidenced CHRDET bit5; regulator summary uses upstream selector/voltage tables. No invented battery percentage, ADC voltage, temperature, charge-current or charging-state claim. |

Sources and failure explanations: [pinned donor/history audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md). Adapted GPL source retains MediaTek/Chris Hendrickson/Maxim Kutnij attribution. Donor source and the external repository were not modified. Targeted additional BSP locators/hashes are in [baseline sources](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-baseline-01-sources.json). The [older GPIO/pin definitions](https://android.googlesource.com/kernel/mediatek/+/android-4.4.4_r3/arch/arm/mach-mt6582/sprout/dct/dct/cust_gpio_usage.h) establish SoC mux functions, not automatic proof of this board's wiring.

## RAM reconciliation and DMA boundary

**D08 retained: 24MiB at `80000000–81800000`, plus 512KiB at `84000000–84080000`; low `80000000–80004000` remains reserved.**````````````````````````

| Evidence | Consequence |
| --- | --- |
| Own D08 boot, photographed 22,208kB MemTotal, stock /proc/iomem | D08 works; stock main RAM and donor agree on 80000000–be000000 (992MiB). Stock capacity alone does not transfer LK/runtime ownership to this kernel. |
| LK code/BSS at 81e00000–81e55434, heap upper/live extent unbounded | Cannot exclude only the BSS and assume every higher page is free. Do not invent a small extra interval or declare all 992MiB available. |
| Modem be000000–bf800000, stock extra bank bf800000–bfa00000, inferred connectivity bfa00000–bfb00000, framebuffer bfb00000–c0000000 and diagnostic scratch near bf700000 | Keep all outside managed RAM. Donor consys reservation near bdf00000 is not adopted. Display takeover does not establish that every loader/DMA reservation is reclaimable. |
| Actual 6.18 non-LPAE, PAGE_OFFSET c0000000, HIGHMEM=n | mmu.c defaults to 240MiB vmalloc + 8MiB guard: physical lowmem ceiling b0000000 (768MiB), before reservations. Full donor RAM would additionally require a reviewed HIGHMEM/address-space change; a 992MiB DT is not 992MiB usable lowmem. |

Single ownership blocker for useful expansion: a defensible upper/live boundary for LK heap and inherited DMA outside D08. Address-space/HIGHMEM work is a separate calculable design choice once ownership is known. No capacity claim from their unit supplies that missing ownership evidence on ours.

Current kernel Image 4,878,848 B, BSS 312,720 B, resident span 5,191,568 B; PID1 ELF 816,160 B, gzip initramfs 13,399 B. The retained [layout](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-baseline-01-layout.json) checks the actual relocated compressed copy, tables, stack, inflated image/BSS, DT/initrd, LK read tail and 16MiB BOOTIMG limit. Driver DMA uses Linux allocations within D08; no LK framebuffer pointer is given to Linux's allocator. Runtime memory pressure/fragmentation remains a hardware observation, not an offline guarantee.

## Validation and remaining risks

One clean kernel build tree, with compiler/API errors repaired there; no second reproducibility build. Final compiled units and DT have no outstanding warnings or errors. Configuration dependencies and actual linked subsystems were checked. 24 applicable test methods pass: provider arithmetic/write filters, actual PWRAP callback faults, host/ARM multiple-device evdev and relay/backpressure, USB lifecycle/failure guards and linked syscalls, corrupt real artifacts, and host capture/reconnect fixtures. The ARM PID1 selftest also passes. Superseded single-device/screen fixtures are historical, not claimed as baseline tests.

The review caught and fixed a retained-history/queue capacity mismatch that would lose replay after a long first capture. Replay history is 256KiB and the queue 512KiB; kernel ring 256KiB. `GAP`/`ERR` and snapshot truncation are explicit; any such marker prevents claiming a complete log. Standard snapshots include CPU/online set, memory/zones/buddy/iomem, IRQs, clocks, deferred probes, regulator summary, power-supply uevent and input devices. No ROM/source-tree rehash, SPFT/recovery rediscovery, device access or flashing was performed.

New drivers, SMP and the changed provider/USB integration are **not hardware qualified**. MM/PWM source rates, cold power-domain ownership, inherited keypad/ eMMC pads, panel identity/revision, I2C/EINT wiring, low-speed card compatibility, DRM timing/IRQ behavior and longer-duration stability remain risks. Safe probe failure is useful evidence. Failure before PID1/ACM can still prevent USB logs; no independent early crash channel is claimed.

Intentionally disabled: charging policy/experiments, battery ADC/gauge/thermal without justified units, cpufreq/cpuidle/suspend, production shutdown/watchdog, all disk writes/mounts/rootfs installation, audio/DAC/amplifier activation, Wi-Fi/Bluetooth/FM, Mali/userspace GPU and applications. I2C1 has no M3 clients. This older unit has no usable FM reception hardware.

To reproduce later in a fresh output directory (no duplicate build was run):`python3 tools/build/run.py --output out/m2-baseline-next -- sh /project/tools/build/baseline.sh`

Existing issues #22–#28 now carry this offline integration checkpoint and remain open. Exact sources, resolved config, ELFs, logs and `SHA256SUMS` are retained under `out/m2-baseline-01/`; `source/` and `source-sha256.json` retain the inputs.

## Exact owner flash and single-boot test
  - Use the already working SPFT v5.2032 setup and original

`/home/luca/Dokumente/Code/Y2Player/y2_v3.2.0_FM-20260813/MT6582_Android_scatter.txt`. Select Download Only, deselect every row, then select BOOTIMG only and choose the image above. Check its size/hash. Let the scatter resolve the address; no raw Write Memory, format, upgrade, loader or calibration operation.
  - Flash manually using the same successful power/cable sequence. Close/stop

SPFT's operation, unplug USB and start the host capture command below before normal power-on through stock LK. Start an independent **300-second timer at power-on**. This supersedes 60 seconds only for this candidate: AP watchdog stop and BOOTIMG recovery are proven; it permits idle observation, not stress.
  - Insert an ordinary test microSD before boot if available; no formatting or

rootfs is needed. Boot unplugged, wait 10 seconds, attach the data cable. The old `ATTACH USB` diagnostic screen no longer exists. If no ACM/log appears within 30 seconds after attachment, retain the failure/screen and terminate this trial using the known recovery route; do not leave it running.
  - During the initial 180-second capture, press/release Prev, Menu, Next,

Play and Select separately, then rotate the wheel slowly both directions and press/release Volume−, Volume+, and briefly Power. Use approximately half-second presses with gaps; no long Power hold as an input test. Expected navigation codes 105/158/106/164/28; volume 114/115, power116; wheel may produce up/down/page events. Observe display geometry, colors, readable console, flicker, illumination and ordinary warmth. Do not stress CPU or test charging.
  - Optional, if logging is healthy and at least 80 seconds remain: after the

first command exits, unplug once, start the second capture command, and reconnect after five unplugged seconds. Capture for 60 seconds. Only one reconnect is supported; it must not reset the device deadline or heartbeat.
  - End sooner on abnormal warmth, reset loops or lost observation. End the

hardware run by 300 seconds from power-on, using the owner's known power/ recovery sequence; restore BOOTIMG only through the same Download Only procedure. The last recorded working Android restore is `/home/luca/Dokumente/Code/Y2Player/out/boot-adb/boot.img`, 5,875,712 B, SHA-256 `275870974bbecc74233761753187ee478bfe79ca9d2f2818facd6e0c039c6b43`; see [actual recovery](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Ffirst-experiment-result.md). Keep that established setup ready; do not substitute a full-ROM restore.

Run on the real host from `/home/luca/Dokumente/Code/Y2Linux`:`sudo python3 tools/observation/usb_log_capture.py --build M2-BASELINE-01 \ --seconds 180 --output out/m2-baseline-01/capture-01`

Optional second capture, started while unplugged:`sudo python3 tools/observation/usb_log_capture.py --build M2-BASELINE-01 \ --wait-seconds 30 --seconds 60 --output out/m2-baseline-01/capture-02`

The tool discovers and verifies the actual ACM device, asserts DTR and sends LOG1; it does not assume ttyACM0. Keep both complete directories (`raw.bin`, USB descriptors, hashes, timestamps, exit report), including failures. Exit0 is collection success, not platform qualification. Report power-on/cable timing, physical button order, display behavior and Android restoration. Then review all probe/runtime failures together, fix independent issues in one source iteration, and build one next candidate. Stop here for the owner's manual flash.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
