---
title: "M4 power platform - Innioasis Updater"
description: "M4 power platform <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m4-power-platform.html"
---

# M4 power platform - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M4 power platform

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M4 power platform > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Historical checkpoint. The owner’s later charging authorization and the reconstructed stock protection architecture are recorded in [M4 charging](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm4-charging.md). The sensor results below remain valid; the former unconditional BATON gate is superseded.

M4 is ACTIVE by the owner's explicit 2026-09-13 implementation/build request. Entry revision: `ae5819f`. This is an integrated candidate workstream, not a physical qualification result. The owner alone deploys BOOTIMG; no assistant flash, loader, partition-table, calibration or protected-partition write.

## Reconciled entry state

Authenticated read-only SSH finds Linux `6.18.0-y2linux-storage06`, CPU0–3, MemTotal 954376 KiB, internal ext4 `/dev/mmcblk0p5` at `/` and p7 at `/data`, and no SD block device. The owner explicitly confirmed preserving Storage06's boot layout. The current prompt's SD-root description is superseded by that observation and clarification. Storage06's permanent eMMC range protection, stock address translation, rescue and BOOTIMG-owned module contract remain.

Local `main` starts ten commits ahead of `origin/main`. GitHub #33 still describes Storage03, and #29–32 contain older SD-root checkpoints. Local retained Storage06 boot/hash/SSH evidence is newer; it is not replaced by those issue bodies. The fresh read-only capture is retained under `out/m4-live-baseline/`; reviewed identity, power and device excerpts accompany the M4 baseline evidence. `/proc/config.gz` is unavailable; the canonical and packaged Storage06 config provide the config evidence, not a fabricated live config dump.

The ALSA period-notification correction `137b3f2` remains in canonical `kernel/audio/mt6582-afe.c`: only negative constraint results return early, then the substream is attached. Retained AUDIO-02 evidence establishes clean 44.1 kHz playback. 48 kHz, channel separation and repeated-playback residuals remain recorded under #29; no audio reverse-engineering or replay is required to activate the explicitly authorized M4 implementation.``

| Interface | Physical entry state | M4 work |
| --- | --- | --- |
| PWRAP/MFD/regulators | One serialized regmap; MT6323 CID 0x2023; regulators and Power input bound | Retain exclusive transport, propagate errors, extend only reviewed child permissions |
| Power supply | y2-usb-presence/online=1; no battery class | Standard ADC and battery/charger children with documented units and calibration |
| Charging | CHR_EN/CSDAC_EN clear; configured current 70 mA, CV 4.175 V; watchdog enable set | Separate telemetry from policy; no guessed enable or increased limits |
| Thermal | No thermal class; own PMIC thermal calibration enable set | Calibrated thermal framework reporting; unresolved sensors must return no data |
| CPU clocks | ARMPLL reports 1.04 GHz; VPROC reports 1.15 V | Evidence-backed shared CPU OPP/CCF/cpufreq control, no overclock |
| Idle/suspend | No cpuidle class; empty power state | Architectural WFI and system suspend-to-idle; no deep SPM/DRAM changes |
| Display | DSI connected; backlight brightness/actual/max 32 | DRM/panel/backlight PM sequencing and visible restore qualification |
| Audio | Y2Audio; regulator-owned VGP2 at 1.8 V; AFE runtime PM exists | Preserve period fix, qualify stop/restart and playback after resume |
| RTC/poweroff | MFD child devices exist but drivers are disabled; RTC register bank lies beyond current regmap maximum | Upstream RTC/poweroff with checked transport and read-first RTC validation |
| Reset | Early AP watchdog stopped; standard watchdog driver disabled | Upstream MT6582 restart owner, distinct from charger watchdog |

The live log ring contains 11011 empty removable-slot command diagnostics out of 11014 retained lines. These are from 11240000.mmc, not evidence of internal root corruption. Preserve full compressed capture; do not mistake the overwritten boot log for a complete boot trace. The existing empty-slot polling/logging needs bounded PM-compatible handling, without broadening storage write access.

## Architecture and acceptance boundary

Use Linux 6.18 frameworks: PWRAP → regmap → MT6323 MFD → regulator, keys, RTC, poweroff, ADC/thermal and power_supply children. CPU OPPs use the same clock and regulator ownership. PM orders DRM, audio, I2C, MMC, input and PMIC dependencies. The first system sleep mode is `s2idle`, exposed through `mem`/`freeze`; Power and RTC are the intended explicit wake sources. Deep vendor SPM states are not justified by the donor's normal-running SPM code.

The pinned vendor reference is MediaTek `d53dd75c3ff77cac3f5be58fddfe660e94f94d64`. Its charger current/CV tables and ADC conversion are reference semantics, not a license to apply Sprout battery profiles to Y2. Its PMIC temperature conversion uses the device's 0x63a/0x63c efuses, with E2/E3-specific slope decoding. Private donor calibration fixtures and NVRAM writes are excluded. Register-by-register build/flash iterations are excluded; prepare one integrated candidate and one coherent owner-deployed qualification session.

M4 stays OPEN until real boot, battery/charger observations, calibrated thermal readings, bounded frequency transitions, WFI, suspend/wake/session continuity, display/audio/storage regression, RTC, reboot and actual hardware-off evidence. Charging policy may remain explicitly bounded if pack/input/temperature evidence does not support autonomous enablement. No percentage, measured current, full state or temperature is invented. USB reconnect #27 remains deferred except if it directly blocks suspend observation. Wi-Fi/Bluetooth/FM/Y2PlayerNative remain outside this workstream. M0 backup/calibration/recovery residuals, #29 audio residuals and #33 broader storage qualification are not silently closed.

## Implemented candidate contract

`Y2LINUX-M4-01` uses the production configuration/DT/build/package pipeline. It retains the current root and data, and replaces only the offline BOOTIMG payload. Installed Buildroot already supplies `hwclock`, `/usr/sbin/rtcwake`, `evtest`, ALSA tools, `timeout`, `sync`, `reboot` and `poweroff`; no rootfs or Buildroot rebuild is needed. No desktop or application power manager is added.

The PWRAP transport is still the sole WACS2 owner. Regmap now uses its spinlock mode because this MMIO transport only performs bounded `readl/writel/udelay`, including the final atomic poweroff callback. Normal ADC settling sleeps occur outside the regmap lock. PMIC children, probe errors and wake masks use the upstream MFD. The accessible RTC bank is 0x8000–0x803e, not 0x0800. Clear-on-read RTC IRQ status is marked precious and excluded from regmap debugfs dumps. Write masks admit ADC requests/buffer enable, existing regulator/backlight/key ownership, RTC time/alarm/trigger and the exact upstream BBPU poweroff key. VPROC voltage/enable, charger limits/watchdog, trim, efuses, RTC spare/boot words and all unreviewed writes remain blocked.``````````````````````````

| Standard interface | Source and conversion | Calibration / interpretation |
| --- | --- | --- |
| BAT0/voltage_now | AUXADC request CON22 0x76e bit7; ADC0 0x714 bit15 ready, bits14:0 data; raw * 7200000 / 32768 µV | BSP 1.8 V reference, PMIC internal 4:1 BATSNS divider; inherited factory hardware trimming; no software gain/offset or private fixture correction. Absolute accuracy awaits comparison with an external meter. |
| BAT0/present | CHR_CON7 0x00e BATON_EN bit0 and TDET_EN bit2 must be enabled; inverted BATON_UNDET bit12 | Detection disabled returns no data; no forced battery-detection policy writes. |
| BAT0/status | CHR_CON0 0x000 CHRDET bit5 and CHR_EN/CSDAC_EN bits4:3 | Inhibited engine + external power → Not charging; absent external power → Discharging. Unexpected enabled engine → Unknown, never inferred current/full state. |
| BAT0/health | CHR_CON6 0x00c VBAT_OV_DET bit6 | Overvoltage if asserted, otherwise Unknown; pack temperature/health are not invented. |
| BAT0/constant_charge_current | CHR_CON4 0x008 selector3:0, BSP 16-entry table | Configured setpoint in µA, not measured current. Entry live value: 70000. Read-only. |
| BAT0/constant_charge_voltage | CHR_CON3 0x006 selector4:0, BSP 32-entry table | Configured setpoint in µV. Entry live value: 4175000. Read-only. |
| y2-usb-presence/online | CHR_CON0 CHRDET bit5 | The existing userspace name is retained; ownership moves under the charger MFD child. It does not identify USB negotiated input current. |
| IIO mt6323-auxadc | BATSNS voltage7 raw/scale; THR_SENSE1 temp3 raw/processed | Serialized conversion, 1 ms settling, bounded ready poll, no stale result on errors/timeouts. |
| pmic-thermal/temp | ADC4 0x71c via CON22 bit 3; 1.8 V / 32768; factory efuses 0x63a/0x63c and CID-specific BSP conversion | Own E2 calibration is enabled: VTS3910, calibration point 27°C, slope0. This point is not a live temperature. Without the calibration-enable fuse (efuse 0x63a bit 1 clear; seen on one reporter's player, report 09888d70) the vendor nominal of pmic_cali_prepare() applies (VTS 3698 at 25 °C, slope 0), read 10 °C high because nominal is about 8 °C off on our own fuses; the boot log prints die calibration=2 and the efuse words. An unknown CID or invalid ADC returns no data. PMIC die temperature is not battery temperature. |
| cpu-thermal/temp | Thermal1100b000 samples AUXADC11001000 channel11, analog TS_CON0/1 at10209600/4; two CPU sensors, maximum reported | Own read-only efuse words10206100/104 via NVMEM. BSP gain, offset, VTS1/2, slope and half-degree calibration. No default coefficients. Uncalibrated sensors do not register meaningful Celsius reporting. |

There is deliberately no CAPACITY, CURRENT_NOW, battery TEMP, guessed VBUS voltage, charge-complete heuristic or estimated watts. Die sensors use Linux thermal zones; BSP CPU passive110°C/critical120°C and PMIC critical150°C are retained as software trips. CPU cooling acts through the shared cpufreq policy. Existing autonomous thermal interrupt/protection settings are never rewritten; if present but not recognized, the sensor driver refuses takeover. This is software protection plus retained hardware protection, not a newly qualified SPM thermal reset path. Qualification load is bounded and uses a much lower 60°C abort threshold as a test stop condition, not an invented hardware limit.

### Charging limitation and the two watchdogs

The owner's retained stock binary has both `force_get_tbat` at 0xc039a8a0 and `battery_meter_get_battery_temperature` at 0xc039cf24 returning literal25. Their ARM instruction `e3a00019` is `mov r0, #25`. This does not prove the pack lacks a thermistor; it proves those stock functions are not calibrated pack thermometry. The Sprout NTC table/profile is not Y2 battery evidence. Pack identity, board thermistor topology, validated temperature conversion and USB input negotiation are unresolved. Therefore this candidate inhibits charging by clearing only CHR_EN/CSDAC_EN, with checked readback, before ADC dependency deferral and at suspend/resume/shutdown. CHRDET IRQ and a freezable 10-second work item verify inhibit and notify power_supply; they never enable charging. No current, CV, OVP or thermal/emergency protection limit is raised or disabled.

PMIC CHR_CON13 0x01a has watchdog enable bit 4 and timeout selection3:0; the live selection 0 is the BSP 4-second charger watchdog. CHR_CON15 flag/interrupt and watchdog control are retained. BSP actively charging policy must pet/rearm this watchdog; M4's inhibited engine requires no charger re-enable or servicing. The independent AP RGU10007000 uses the upstream MediaTek watchdog, with the exact upstream MT6582/MT6589 compatible pair. The proven early watchdog stop remains; no userspace watchdog daemon starts it. Reboot uses RGU software reset. Poweroff uses the upstream MT6323 BBPU key at 0x8000 and WRTGR at 0x803c, with checked writes and atomic polling. It never uses watchdog reset as poweroff.

### CPU and device PM

Three shared OPPs are enabled: 598000, 747500 and 1040000 kHz, all 1150000 µV. They are the BSP normal F4/F3/F2 table without MT6333 low voltage support; 1.04 GHz and1.15 V are also observed on this Y2. No VPROC write is allowed. Each transition verifies the active VPROC selector, ARMPLL ownership/mux, divider and MAINPLL 1092 MHz, switches temporarily through MAINPLL/2, programs the evidenced ARMPLL word, waits at least 30 µs and verifies readback. Failure restores the old PLL or leaves the verified lower fallback. Unknown FHCTL, voltage or mux state rejects the transition. All four CPUs share one `cpufreq-dt` policy/OPP table. Default governor is powersave; userspace and schedutil are available. The 100 µs clock-latency entry is a conservative software budget, not a measured physical latency.

CPU idle exposes only the standard ARM WFI state, with tickless idle enabled. `mem` selects `s2idle`; `freeze` is also available. All four CPUs retain context, DRAM stays powered, and there is no CPU hotplug, vendor SPM deep idle or DRAM self-refresh transition. No external current reduction is claimed. Linux's PM_SLEEP_SMP selects HOTPLUG_CPU at compile time, but the Y2 SMP operations have no cpu_die callback: ARM marks the CPUs non-hotpluggable. The s2idle path returns before the secondary-CPU offline phase.

Power key and RTC are the only selected wake sources. PMIC wake masks are applied in the MFD's late suspend callback after child drivers arm their IRQs; errors abort suspend and restore runtime masks. EINT applies its wake mask at noirq and restores it before normal resume. Wheel IRQ drains before I2C sleeps; volume scanning stops and reconciles state on resume. Navigation polling uses the standard input driver's PM. No player or power-key application policy is placed in the kernel; a brief Power press remains KEY_POWER, and long-press emergency policy is retained unchanged.

DRM's existing atomic prepare/complete path quiesces/resumes the panel and framebuffer. Backlight uses BL_CORE_SUSPENDRESUME; DCS failures are logged, with reset as the panel's quiescent fallback and full initialization on resume. The first LK handoff path is preserved. ASoC card PM and component device links order stream/DAPM shutdown before AFE/codec sleep. The codec uses standard runtime/system PM; GPIO rail dependencies retain20→18→15 enable order and reverse disable. VGP2 stays regulator-owned at1.8 V for reliability. The M3 period-notification fix is unchanged.

For internal eMMC, normal block queues drain and cache-flush/status checks run, then s2idle retains controller/card state. Active DMA/request state aborts host suspend. No CMD5, new EXT_CSD permission, rail power cut or root reinitialization is introduced. The existing range/address firewall is unchanged. SD remains optional and uses normal card PM with retained host clocks. Expected empty-slot CMD8/55 timeouts no longer fill the boot log; real card/data errors stay visible. MUSB polling is freezable and drained during prepare; the MUSB child has its proper parent and preserves session while the upstream core saves/restores context. USB is not a wake source. Cable reconnect remains separately deferred.

RTC is enabled with no HCTOSYS/SYSTOHC or automatic time write. Initial tests read time and existing alarm. Setting time/alarm later uses standard RTC APIs, preserves unrelated register bits, and never writes RTC spare/boot words. Reboot persistence, alarm wake, actual poweroff and subsequent normal power-on still require the single physical qualification session.

## Primary implementation sources

The locked Linux 6.18 tree supplies the MFD/regulator/key/RTC/poweroff, NVMEM, thermal, cpufreq-dt, cpuidle, ASoC and PM frameworks. Pinned BSP paths and SHA256 are in [m4-power-sources.json](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/m4-power-sources.json). Key primary references:
  - [MT6582 cpufreq, normal OPPs and switch sequence](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/arch/arm/mach-mt6582/mt_cpufreq.c)
  - [MT6582 CPU thermal calibration and sampling](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/thermal/mt6582/mtk_ts_cpu.c)
  - [MT6323 die thermal conversion](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/thermal/mt6582/mtk_ts_pmic.c)
  - [Charger register semantics and configuration tables](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/power/mt6582/charging_hw_pmic.c)

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
