---
title: "Y2 storage hardware ceiling — eMMC and SD bus modes - Innioasis Updater"
description: "Y2 storage hardware ceiling — eMMC and SD bus modes <!-- knowledge-base-scope: scoped-validation-record -- Superseding physical evidence, 2026-10-04: the installed Baseli"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-storage-ceiling.html"
---

# Y2 storage hardware ceiling — eMMC and SD bus modes - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 storage hardware ceiling — eMMC and SD bus modes

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 storage hardware ceiling — eMMC and SD bus modes > **Superseding physical evidence, 2026-10-04:** the installed Baseline02 now > passes bounded HS200 and SDR104 read/write/hash, fsync and runtime-PM checks. > See [the Platform 1.0 storage pass](Y2-PLATFORM-V1-STORAGE.md) for exact modes, > measurements and remaining qualification gaps. The record below preserves > the source-only state at its original date. 

Source and software record, 2026-10-01. The ceilings below come from stock Y2 binaries, the MT6582 BSP source, the installed eMMC's EXT_CSD and the MT6323 regulator tables. The implementation is software-validated. No bus mode above 50 MHz has run on a Y2 under Linux yet. The candidate section records what was built. Physical results belong in a separate report.

Before this pass both hosts ran at 50 MHz SDR. The eMMC used 8-bit HS52 and the SD used 4-bit SD High Speed at 3.3 V. That limit came from our own device tree, not from the hardware.

## Answers````````````

| Question | Answer | Basis |
| --- | --- | --- |
| Can the eMMC go beyond 50 MHz? | Yes | HS200 at 200 MHz: host source 200 MHz, card type 0x57, IO fixed 1.8 V, stock msdc0 flags include MSDC_UHS1 (BSP maps it to the HS200 capability) |
| Is DDR52 possible? | Yes | Card type bit 2 (DDR52 1.8/3 V); stock msdc0 flags include MSDC_DDR; DDR clock = source/4 = 50 MHz |
| Is 100 MHz / HS200 possible? | Yes, HS200 at 200 MHz | Mainline CMD21 tuning on PAD_TUNE/IOCON (MSDC v4, mt8135_compat). An HS200 bus held at 100 MHz (y2_clock_limit_hz) moves as many bytes as DDR52, so the ladder falls from 200 MHz HS200 straight to the untuned DDR52 |
| Is HS400 possible? | No | The card supports it (bit 6), but MT6582 MSDC has no data strobe / EMMC50 block |
| Can SD use 100 MHz? | Yes | SDR50 runs at source/2 = 100 MHz |
| Is SDR50 possible? | Yes | Stock msdc1 flags include MSDC_UHS1 → SDR50/SDR104 |
| Is 1.8 V UHS wired? | Yes | Stock msdc_sd_power_switch (0xc04f2b60) sets MT6323 VMC to 1800 mV and applies dedicated 1.8 V pad drive values; VMC's table is {1.8, 3.3 V} |
| Is SDR104 possible? | Yes, at 200 MHz | The 200 MHz source is undivided. The spec allows up to 208 MHz, so 200 MHz is the host maximum. CMD19 tuning |

These answers depend on the card that is inserted. A card without UHS-I, or one that refuses 1.8 V, negotiates SD High Speed at 3.3 V as before.

## Evidence````````````````````````````````````````

| Item | Finding | Source |
| --- | --- | --- |
| msdc0 board flags | 0x3c0 = SYS_SUSPEND, HIGHSPEED, UHS1, DDR; 8 data pins; drive clk/cmd/dat 4/2/2 | hash-identified stock kernel msdc_hw record, out/platform-v1-physical-bringup/stock-reference/msdc-board-platform-data.json |
| msdc1 board flags | 0x3e3 = CD, WP, REMOVABLE, SYS_SUSPEND, HIGHSPEED, UHS1, DDR; 4 pins; drive 7/7/7 at 3.3 V, sd_18/sdr50/ddr50 drive 4 | same |
| Flag mapping | UHS1 → MMC_CAP_UHS_SDR12/25/50/104 + MMC_CAP2_HS200_1_8V_SDR; DDR → UHS_DDR50, 1_8V_DDR | MT6582 BSP mt6582/sd.c |
| eMMC power | Stock powers only VEMC_3V3 (card VCC, 3.3 V). The VIO18 line is commented out: eMMC IO is the always-on 1.8 V VIO18 rail. msdc_ops_switch_volt returns 0 for eMMC | BSP msdc_emmc_power, stock disassembly |
| eMMC IO range | DVDD18_MSDC0 1.7–1.95 V; MediaTek's own reference board uses vqmmc = vio18 | MT6592 datasheet, mt8173-evb.dts |
| SD power | VMCH 3.3 V card supply, VMC IO supply 3.3 V → 1.8 V on switch; then Schmitt trigger, RDSEL/TDSEL (0 in both modes on MT6582) and the 1.8 V drive table; 10 ms after power-on and power-off | stock msdc_sd_power, msdc_sd_power_switch, msdc_set_driving (0xc04f28c0) |
| EN18IO comparator | Absent from MT6582 (REMOVEED_FOR_MT6582, no stock symbol) | BSP, stock symbols |
| Pad drive cells | GPIO 0x10005000, bits 10:8; MSDC0 0xc00/0xc10/0xc20, MSDC1 0xc40/0xc50/0xc60 | stock msdc_set_driving |
| Source clock | LK selector 1: MSDCPLL 400 MHz / 2 = 200 MHz; undivided 200, /2 = 100, DDR = src/4 = 50 MHz | kernel/platform/clocks.c, LK |
| eMMC card | EXT_CSD[196] = 0x57: HS26, HS52, DDR52, HS200 1.8 V, HS400 1.8 V | identification readback |
| Stock tuning | Error-driven retune (msdc_tune_cmdrsp/read/write, AUTO_K), dropping modes after power-cycle failures. Mainline's CMD19/21 sweep uses the same PAD_TUNE/IOCON fields | stock disassembly, mainline msdc_execute_tuning |

Extracted disassembly is kept privately in `out/storage-ceiling-source/stock/`.

## Implementation````````````````````````````````

| Part | Source | What it does |
| --- | --- | --- |
| Ladders and policy | kernel/platform/storage-modes.h | Ladder levels, card-capability parsers, fallback rule, EXT_CSD identity bytes, stock pad drive table |
| Driver | kernel/patches/0009-y2-msdc-readonly.patch (mtk-sd.c) | Per-level caps (DT caps ∩ level) and clock cap; voltage switch with VMC and pad drive; tuning record; fault classification; fallback worker; post-negotiation readback; y2_storage status |
| Pad drive | kernel/platform/pinctrl.cy2_msdc_pad_drive() | The GPIO block owner writes the stock 3.3 V or 1.8 V drive values under its lock; probe returns -EPROBE_DEFER until pinctrl is up |
| Request firewall | kernel/platform/storage-policy.h | Admits CMD21 (tuning block read, no address) and the CMD6 values HS200 needs: HS_TIMING ≤ 2 with default drive strength, BUS_WIDTH 5/6 (DDR). HS400 and drive-type changes stay denied |
| Device tree | kernel/dts/innioasis-y2-production.dts | mmc0: mmc-ddr-1_8v, mmc-hs200-1_8v, vqmmc = VIO18 (fixed, always-on), no vmmc. mmc1: all UHS-I modes, vmmc = VMCH 3.3 V, vqmmc = VMC 1.8–3.3 V. Rails exist only in the production DT, each with a consumer |
| Status | tools/platform/y2_platform/observe.py | storage.controllers[].mode carries the decoded y2_storage line |
| Reborn | crates/reborn-platform/src/client.rs (Reborn b92d312) | Diagnostics → Storage shows mode, card, tuning and faults per host |

### Negotiation and fallback

The MMC core negotiates the highest mode both the host and the card admit. The current ladder level limits what the host offers.

| Host | Ladder (highest → lowest) |
| --- | --- |
| eMMC | HS200 200 MHz → DDR52 50 MHz DDR → HS52 50 MHz → HS 25 MHz → legacy 13 MHz |
| SD | SDR104 200 MHz → DDR50 50 MHz DDR → SDR50 100 MHz → HS 50 MHz 3.3 V → HS 25 MHz → legacy 13 MHz |

The SD ladder follows the core's own preference, SDR104 > DDR50 > SDR50, so SDR50 comes after DDR50. A 1.8 V switch failure skips every remaining UHS level.``````

| Trigger | Action |
| --- | --- |
| Tuning failure (CMD19/21) | tuning event; the next level is applied to the caps. The core then falls back on this init |
| 1.8 V switch failure (SD) | voltage event; skip to 3.3 V HS |
| CRC / timeout at a tuned timing | The core retunes first; a second strike at the same level downgrades |
| CRC / timeout at an untuned timing, controller data error | Immediate downgrade |
| Readback mismatch | verify event, downgrade with card re-init. 500 ms after any high timing is set, eMMC re-reads EXT_CSD and compares the identity bytes the core itself treats as read-only (plus SEC_COUNT). SD reads SD_STATUS twice; both copies must match and report 4-bit width |

A downgrade lowers the caps first. If the current timing is still admitted, only the clock changes. Otherwise the card is re-initialised with `mmc_hw_reset()`. The core flushes the cache first. On eMMC its "power cycle" changes no rail (no vmmc, VIO18 always-on), so the card sees a CMD0 re-initialisation. SD is power-cycled through VMCH. If re-init fails, the next level is tried. The filesystem never stays on a mode that failed.

### Safety
  - Root/data eMMC is never power-cycled. VEMC_3V3 is not declared, so Linux

cannot switch the card supply off. VIO18 is always-on.
  - No IO voltage is guessed. eMMC IO stays at the fixed 1.8 V rail. SD uses

only VMC's two table values, which are the values stock uses.
  - Partitions, geometry, boot areas and protected regions are untouched. The

request firewall admits only the CMD21 block read and the HS200/DDR switch values.
  - CRC and error handling are unchanged. Retries and fallbacks are added on

top.
  - Runtime PM keeps MSDC_CFG, IOCON, PAD_TUNE and DAT_RDDLY0/1 across clock

gating, so tuning survives. eMMC s2idle re-initialises on resume, which re-negotiates and retunes.
  - SD hotplug: CMD55 timing out with no card resets the SD ladder to its

ceiling, so a replacement card starts from the top. VMC/VMCH power-off is followed by the stock 10 ms wait.

### Boot controls``````````

| Parameter | Effect |
| --- | --- |
| y2.emmc_mode=<level> | eMMC ceiling, e.g. HS52 for the previous behaviour |
| y2.sd_mode=<level> | SD ceiling, e.g. HS for 3.3 V 50 MHz |
| y2.mmc_safe=1 | Existing safe storage mode: 26 MHz source, legacy 13 MHz, no high-speed caps |

`y2_clock_limit_hz` also accepts 13/25/50/100/200 MHz at runtime.

## Diagnostics

`/sys/bus/platform/devices/1123{0,4}0000.mmc/y2_storage` is one line of `key=value`:

`host level ceiling timing width clock_hz actual_hz cap_hz signal_mv vqmmc_mv card_level card_caps hs400_card tuning tuning_runs tuning_failures tune_iocon tune_pad tune_rddly0 voltage_switches verify fallbacks resets reset_error clock_error drive_before crc_events timeout_events controller_events tuning_events voltage_events verify_events`

`y2-platform status` exposes it as `storage.controllers[].mode`, and Reborn Diagnostics shows it as plain text. No register decoding is needed.

## Tests``````

| Test | Covers |
| --- | --- |
| tests/test_storage_ceiling.py (11) | Ladder invariants, card parsing (EXT_CSD type, SD bus modes), pad table, caps never exceed DT, safe mode, fallback with re-init and repeated failure, fault classification, retune strikes, voltage/tuning hooks, SD_STATUS readback, empty-slot reset, runtime-PM retained registers incl. DDR, status parsing, DT rails |
| tests/test_mmc_requests.py | CMD21 is the only new read; CMD6 183/185 admitted values |
| tests/test_mmc_context.py | EXT_CSD identity copy saved at legacy timing only |
| Existing storage and overlay tests | Unchanged contracts still pass |

## Candidate receipt````````````````````````

| Field | Value |
| --- | --- |
| Linux built source | 540ae029b13940d4b2dfe21902bed71b89cb117a (later commit 2c1ab53 changes only tests/test_storage_recovery.py; validation ran there) |
| Reborn built source | b92d312cc2dc4b74f57a1a9a7b1407e34707137a (0.2.0) |
| Kernel | 6.18.0-y2linux-storage-ceiling |
| Root / release / build | 2025.02.18-platform-v1.11 / 1.0.0-storage-ceiling-candidate.1 / Y2LINUX-STORAGE-CEILING |
| Base | Reborn Product UI v2 candidate (Linux 5cfe04cb, Reborn bd8436dd) |
| Fallback | Exact Hardware02 pair (6.18.0-y2linux-hardware-02, 2025.02.18-platform-v1.4) |

The shipped DTB declares mmc0 `mmc-ddr-1_8v`, `mmc-hs200-1_8v` and vqmmc→VIO18 (1.8 V, always-on). It declares mmc1 `sd-uhs-sdr12/25/50/104` and `sd-uhs-ddr50` with vmmc→VMCH (3.3 V) and vqmmc→VMC (1.8–3.3 V). Both hosts allow 200 MHz. No VEMC_3V3 node exists.``````````````````

| Check | Result |
| --- | --- |
| Kernel build (mtk-sd.c, pinctrl.c also W=1) | PASS, no warnings in storage sources |
| DT gate (dev_dtb.py, reviewed storage rails/modes) | PASS on the built DTB; mutation test rejects HS400, unknown modes, changed supply, switchable eMMC IO |
| Production/platform regression (tools/production/tests.sh, container) | PASS, 281 tests, 3 explicit native-dependency skips |
| Native host-dependency tests (test_system_update_fallback) | PASS |
| Reborn cargo fmt --check, clippy --workspace --all-targets --locked -D warnings, cargo test --workspace --locked | PASS, 212 tests |
| Reborn ARM QEMU check, installed ARM modules, ELF closure | PASS |
| Release inventory (at the built commit), legal-info | PASS |
| Preserving package (system_update.py) | PASS: clean ext4, BOOTIMG/Y2ROOT only, no Y2DATA payload, exact Hardware02 fallback |

The first build, from `0e62046`, was stopped by the DT gate. That gate still pinned 50 MHz and admitted no MMC supply. `540ae02` taught the gate the reviewed set. The first container run then failed one stale test, which `2c1ab53` fixed. Logs are kept in `out/storage-ceiling/superseded-*`.

`out/y2linux-storage-ceiling-candidate/`: `MT6582_preserve_data_scatter.txt` selects only BOOTIMG and ANDROID/Y2ROOT. Nothing was flashed or pushed.````````````````

| File | SHA-256 |
| --- | --- |
| BOOTIMG.img | 4332d4f284e9ee76b4d76985480c184ebaacd7c674a3656925ff290ef3cd501c |
| Y2ROOT.img | 72eab34a39255a1b7f2eba0fe0a6abd891a0b089f8fb847cf42ad8eec033ba72 |
| fallback/BOOTIMG.img | b2a2c3bcb7cc7783828882e447e8b867453cb5b65846ce63577076b1ca4afeea |
| fallback/Y2ROOT.img | 63dbd0a198cd86e847c10ed163fd14b2cbe269595fa1988c99ac8393160bb547 |

## First boot checks for the owner
  - `cat /sys/bus/platform/devices/11230000.mmc/y2_storage` should show

`level=HS200 timing=hs200 width=8 actual_hz=200000000 signal_mv=1800 tuning=pass verify=pass`with all`*_events=0`. Reborn shows the same under Diagnostics → Storage.
  - With a UHS-I card inserted, `11240000.mmc/y2_storage` should show

`level=SDR104` (or `DDR50`/`SDR50`, as the card supports) with `signal_mv=1800` and `voltage_switches` ≥ 1. With a non-UHS card it should show `HS` at 3300 mV.
  - Run the existing storage hash rounds on `/data` and `/media/sd`. Then

remove the card and insert another; the SD level should start from the ceiling again.
  - Any `fallbacks` > 0 names the failing level and event in the kernel log

(`Y2 storage fallback <from> -> <to> (<event>)`). If boot itself fails, boot the fallback pair, or add `y2.emmc_mode=HS52 y2.sd_mode=HS` (previous modes) or `y2.mmc_safe=1`.

## First device check and candidate 2

The first candidate booted on 2026-10-01.
  - eMMC: works at HS200. Status showed 8-bit, 199 999 771 Hz, 1.8 V; tuning

passed on the first run and the readback passed. There were no CRC/timeout events and no fallbacks. A read-only 128 MiB direct read took 0.96 s (~133 MB/s).
  - SD: no card initialised. The PWRAP PMIC write gate

(`kernel/platform/policy.h`) refused every VMC/VMCH write with `-EPERM` (`vmch-sd-card: failed to disable: -1`, `could not set regulator OCR (-1)`). The 1.8 V switch failed, and so did the 3.3 V power cycle used for the fallback.

Commit `61a353b` admits only VMC enable (DIGLDO_CON3 bit 12), VMCH enable (CON5 bit 14), the VMC 1.8/3.3 V selector (CON24 bit 4) and the VMCH selector pinned to 3.3 V (CON26 bit 7). VEMC_3V3 stays unwritable. A PWRAP test drives the exact regulator writes through the gate.````````````````````

| Field | Value |
| --- | --- |
| Linux built source | 4db6d6dee8e8b21d85f4f7dfa8e6b7aac82d5e56 |
| Reborn built source | b92d312cc2dc4b74f57a1a9a7b1407e34707137a |
| Kernel / root / release / build | 6.18.0-y2linux-storage-ceiling-02 / 2025.02.18-platform-v1.12 / 1.0.0-storage-ceiling-candidate.2 / Y2LINUX-STORAGE-CEILING-02 |
| Validation | Production/platform 281 tests PASS (3 native skips); Reborn ARM QEMU, installed ARM, ELF, release inventory, legal-info, preserving package PASS |
| BOOTIMG.img | 5c17f744a0569feb16f6954531024ae7dcafee10bf14cbdb2eb18ba5d083fd36 |
| Y2ROOT.img | dc611011ce6f129cf18a61a28f9435e2504ade1d416f0b78d6db26764fd20a59 |

Package: `out/y2linux-storage-ceiling-02-candidate/`. It supersedes the first candidate. Not flashed by this pass.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
