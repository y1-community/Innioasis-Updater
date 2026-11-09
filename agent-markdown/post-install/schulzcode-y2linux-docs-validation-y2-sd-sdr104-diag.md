---
title: "Y2 SD SDR104 stability — research and diagnostic candidate 3 - Innioasis Updater"
description: "Y2 SD SDR104 stability — research and diagnostic candidate 3 <!-- knowledge-base-scope: scoped-validation-record -- Superseding physical evidence, 2026-10-04: Baseline02"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-sd-sdr104-diag.html"
---

# Y2 SD SDR104 stability — research and diagnostic candidate 3 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 SD SDR104 stability — research and diagnostic candidate 3

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 SD SDR104 stability — research and diagnostic candidate 3 > **Superseding physical evidence, 2026-10-04:** Baseline02 includes the later > stock-pad/card-driver policy and passes 4 GiB of SDR104 direct reads at four > offsets, scratch hashes, all four SD modes and physical remove/reinsert. > See [the Platform 1.0 storage pass](Y2-PLATFORM-V1-STORAGE.md). Candidate 3's > failures and the original candidate 4 software-only receipt remain historical > evidence; they do not describe the current installed configuration. 

Source and software record, 2026-10-02. Candidate 2 negotiated SDR104 on a real Y2 and fell back to DDR50 under sustained reads. This page records why the old tuning could not have found a stable operating point, what the MT6582 controller actually implements, and what diagnostic candidate 3 adds. Candidate 3 was flashed on 2026-10-02 and characterized over SSH; the measurements are in "Physical characterization of candidate 3". Candidate 4 follows from them and has not been flashed.

## Evidence from the installed candidate 2``````````````

| Test | Result |
| --- | --- |
| 128 MiB direct read right after boot, SDR104 | 1.67 s (~77 MB/s), no errors |
| First 1 GiB direct read | 2 CRC events, 0 timeouts, then SDR104 -> DDR50 (crc) |
| Status after the fallback | tuning_runs=4, fallbacks=1, resets=1, tune_pad changed from 0x9951500 to 0xa951500 |

The interface works at 200 MHz, but not for a sustained load. It is not proof that SDR104 is impossible. A clean 128 MiB read is not a qualification.

## What the old SD tuning really did

Decoding `tune_pad` with the MT6582 `MSDC_PAD_TUNE` layout (below):````````````

| Field | 0x9951500 | After the retune 0xa951500 |
| --- | --- | --- |
| DATRRDLY | 21 | 21 |
| CMDRDLY | 21 | 21 |
| CMDRRDLY | 6 | 10 |
| CLKTXDLY | 1 | 1 |

Two defects explain these numbers.
  - A 64-step sweep on a 32-tap delay line. Mainline `mtk-sd.c` chooses

`tuning_step` from `MMC_CAP2_NO_MMC`: 64 for a host that cannot do MMC. The Y2 SD host declares `no-mmc`, so it swept 64 steps. MT6582 delay fields are 5 bits wide. Steps 32 to 63 re-tested tap 31, and the "second half" registers mainline writes at `PAD_TUNE + 4` are `MSDC_DAT_RDDLY0` on this controller (offset `0xf0`), not a second tuning register.
  - No failing tap.`get_best_delay()` returns `len / 3` for a window that

starts at tap 0. For an all-pass 64-step map that is 64 / 3 = 21, which is exactly what both command and data picked, in two independent tunings. Neither sweep saw a failing tap, so "21" was arbitrary and said nothing about the timing eye.

The `CMDRRDLY` / `CLKTXDLY` values come from the same bug. `sdr_set_field()` does not mask its value, so the internal-delay sweep at step 38 wrote `38 << 22`: the low five bits landed in `CMDRRDLY` (6) and bit 5 set bit 27, `CLKTXDLY` (1). The retune picked 42 and produced 10 and 1. The card clock output delay was therefore shifted by one tap as a side effect.

This is a hypothesis about timing margin, not a measured eye. The decoded registers and the arithmetic fit it. The pass maps added by candidate 3 settle it.

## MT6582 MSDC register facts

Sources: the MediaTek MT6582 BSP `mt6582/sd.c` (register dump and the `msdc_tune_*` functions), and the stock Y2 kernel functions `msdc_set_sr`, `msdc_set_smt`, `msdc_set_rdtdsel`, `msdc_set_driving`, `msdc_pin_pud`, disassembled from the retained stock kernel.``````````````````````````````````````````````````````````````````

| Item | Fact |
| --- | --- |
| MSDC_PAD_TUNE (0xec) | DATWRDLY[4:0], DATRRDLY[12:8], CMDRDLY[20:16], CMDRRDLY[26:22], CLKTXDLY[31:27]. Five bits each: 32 taps, linear |
| MSDC_DAT_RDDLY0/1 (0xf0/0xf4) | Per-lane read delay. Used only when IOCON.DDLSEL = 1; mainline runs DDLSEL = 0 |
| SDC_DATCRC_STS (0x60) | Failing data lanes: bits 7:0 rising edge, 15:8 falling edge. Per-lane CRC identification is available |
| MAIN_VER / ECO_VER (0x100/0x104) | Controller version registers |
| Stock UHS tuning (above 100 MHz) | Sweeps IOCON.RSPL, PAD_TUNE.CMDRDLY, PATCH_BIT1.CMD_RSP, PATCH_BIT0.INT_DAT_LATCH_CK_SEL, IOCON.DSPL, per-lane DAT_RDDLY, PATCH_BIT0.CKGEN_MSDC_DLY_SEL; error-driven, not a single sweep |
| MSDC1 pad cells (GPIO 0x10005000) | CLK 0xc40, CMD 0xc50, DAT 0xc60, PAD 0xc70 |
| Pad cell bits | Drive [10:8], slew [12], Schmitt [13]; PAD cell: RDSEL[9:4], TDSEL[3:0]. Stock uses RDSEL = TDSEL = 0 at both voltages |
| RXDLYSEL | The vendor driver never touches PAD_TUNE bits 13, 15 or 21 and its saved_para.pad_tune is built from the three delay fields only. Mainline sets bit 15 for compatibles without data_tune; the status read it back as 0 on both hosts. Candidate 3 settles this on the hardware (see below) |
| SDR104 clock | The MSDC source is MSDCPLL / 2 = 200 MHz. Dividers give 100 and 50 MHz; there is no reachable clock between 100 and 200 MHz without retuning a PLL, so there is no "slightly lower SDR104" |

The stock autok code (`msdc_autok_*`) is the SDIO 3.0 calibration of the WiFi host (it scans over core voltage). It is not a model for the SD slot.

## What candidate 3 changes

No electrical setting changes: voltage, pad drive and the clock source are exactly candidate 2's.``````````````````

| Area | Change |
| --- | --- |
| Tuning geometry | The Y2 hosts use exactly 32 taps. SD tuning writes only its own field per sweep (no DAT_RDDLY0 write, no overflow into CLKTXDLY) |
| SD tuning | Scans both sampling edges for command and data, and requires every one of 3 tries of a tap to pass. Selection: widest eye over both edges, then the better margin, then the rising edge; the centre of that window. Eyes below 4 taps fail the level and the ladder steps down. An all-pass sweep is flagged open (no information). The command-internal delay (CMDRRDLY) is swept and recorded but applied only when it shows a real eye |
| Failed tuning | The registers it disturbed are restored before the lower level negotiates |
| Diagnostics | New y2_storage_diag and y2_tune_diag. y2_storage keeps its one-line contract |
| Characterization | Root-only y2_lab on the SD host, compiled in only while Y2_MSDC_LAB is 1 |
| eMMC | Functionally unchanged. It keeps the mainline tuning; only passive records are added |

Windows are linear: `Y2_TUNE_CIRCULAR` is 0 because tap 31 is not adjacent to tap 0 on this delay line. The helper supports a circular line and is tested for it.

## Diagnostics reference

Both attributes live under `/sys/bus/platform/devices/11240000.mmc/` (SD) and `11230000.mmc` (eMMC, `y2_storage_diag` only). Every line is `key=value` or `key: field=value ...`.

`y2_storage_diag`:``````````````````````````````````````````````````````````````````````````````````````

| Line | Content |
| --- | --- |
| host= mode= timing= level= ceiling= width= clock_hz= actual_hz= cap_hz= | Negotiated state |
| signal: | Signalling voltage from ios, from the driver state and the regulator (vqmmc_mv, enabled, vmmc_mv) |
| card: | Name, manufacturer, revisions, sd3_bus_mode, driver types, uhs_max_dtr |
| fallback: | Previous mode, current mode, reason, counts, resets, retunes, tuning runs at the fallback |
| regs: / regs.tune: | IOCON, PAD_TUNE, DAT_RDDLY0/1, PATCH_BIT0/1/2, MSDC_CFG, SDC_CFG, PS, decoded delays and edges |
| probe: / rxdlysel: | Which PAD_TUNE / DAT_RDDLY bits stick when written (write ones, read, clear), controller versions, and supported / requested / actual for RXDLYSEL |
| pad: / pad.clk,cmd,dat,pad: | Raw pad cells read back from the GPIO block, with drive, slew, Schmitt, pull byte, requested drive, RDSEL, TDSEL |
| pad.drive: | Drive values before programming and the error code |
| fault.total= ... | Counters: cmd_crc, cmd_timeout, data_crc, data_timeout, stop, other, timeouts |
| fault.lanes: | Failing data lanes (rising and falling edge) |
| fault.first: / fault.last: | Sequence, time, kind, command, direction, block size and count, argument, controller error bits, DATCRC_STS, level, timing, PAD_TUNE, IOCON, PATCH_BIT0 |

`y2_tune_diag`: for the first and the latest tuning, the registers at the end of the sweep, then per phase (`cmd`, `cmd_int`, `data`) the pick (edge, delay, window, eye width, margins, `open`, clipping, window counts, what the old `get_best_delay` would have chosen) and, per scanned edge, the `all` map (every try passed), the `any` map (at least one try passed) and the passing windows. Bit `n` of a map is tap `n`.

Only the first failure of a boot is logged (`Y2 storage first fault:`). Later failures are counted without logging.

## Characterization interface (`y2_lab`)

Root-only (0600) on the SD host. Unmount the card first: a marginal operating point can fail reads.````````````````````````````````````````

| Command | Effect |
| --- | --- |
| set name=value ... | Writes one field: cmdrdly cmdrrdly datrrdly datwrdly clktxdly rspl dspl wdspl ddlsel latchck ckgen wrcrcs cmdta rddly0 rddly1; a pad field drv_* (0 to 7), sr_*, smt_* (0 or 1), pull_* (byte), rdsel (0 to 63), tdsel (0 to 15) with * = clk, cmd, dat; or drvtype (0 B, 1 A, 2 C, 3 D) for the next level (candidate 4) |
| scan [tries=N] [latchck=L] [ckgen=C] | Sweeps every tap, both edges, command and data at the given PATCH_BIT0 fields; restores the registers; reading y2_lab returns the maps and windows |
| retune | Runs the production SD tuning again |
| level NAME | Renegotiates at a ladder level (e.g. back to SDR104 after a fallback) |

## Physical characterization of candidate 3

Flashed 2026-10-02 (`6.18.0-y2linux-sd-sdr104-diag-03`), SD128 119 GiB UHS-I card, SDR104 at 199 999 771 Hz, 1.8 V (`vqmmc_mv=1800`, `vmmc_mv=3300`). Read-only raw reads of `/dev/mmcblk1`, `iflag=direct`.

What the new diagnostics showed``````````````````````

| Item | Result |
| --- | --- |
| RXDLYSEL | Does not exist on MT6582.pad_tune_writable=0xffdf1f1f: bits 13, 15 and 21 never stick; only the five delay fields do. supported=no requested=1 actual=0. Controller MAIN_VER=0x20120911, ECO_VER=1 |
| Pad drive readback | The 4/4/4 write does take effect (pad.clk/cmd/dat drive=4). Candidate 2 only recorded the values before it |
| Other pad cells | LK state: SMT=0 on CLK/CMD/DAT, RDSEL=12, TDSEL=5, slew 0. The stock kernel sets SMT=1 and RDSEL=TDSEL=0 for MSDC1 |
| Tuning maps | Command rising edge: all 32 taps pass. Command falling edge: fails taps 9 to 15. Data rising edge: taps 0 to 30 pass. Data falling edge: fails taps 5 to 19 and passes 0 to 4 and 20 to 31. The command-internal delay passes taps 0 to 23. The rising-edge sweeps are (almost) open eyes, so "the pick is centred" says little |
| Faults | Every failure is a data CRC on CMD18 reads. Zero command CRCs and zero timeouts. Lanes DAT0 to DAT3 all fail on the rising edge (DAT0 most often); in the DDR50 stage the falling-edge lanes fail too |

What does not fix SDR104. Each point renegotiates SDR104 through `y2_lab` (`level SDR104`), applies the setting, then reads raw 16 MiB chunks and stops at the first CRC:

| Dimension swept | Values | Result |
| --- | --- | --- |
| Data read delay, rising edge | 0, 6, 12, 18, 24, 31 | all fail within 16 to 32 MiB |
| Data read delay, falling edge | 0, 3, 22, 26, 31 | all fail within 16 MiB |
| Clock TX delay | 1, 2, 4, 8, 16 | all fail within 16 MiB |
| Clock-generator delay | 0, 3, 6, 10, 16, 24, 31 | all fail within 16 MiB (16 was worse: 11 faults) |
| Internal latch clock | 1 to 7 | all fail within 16 MiB |
| Pad drive strength, all lines | 1, 2, 3, 5, 6, 7 | all fail (7: 48 MiB) |
| Drive on data or clock only | 1, 7 | all fail |
| Slew rate | all lines, data only | all fail |
| Host clock capped at 100 MHz, SDR104 timing |  | 2 GiB, 0 faults, 42 MB/s |
| Host clock 200 MHz |  | 64 MiB, 2 faults |

So the failure is a 200 MHz signal-margin problem that no sampling-phase setting recovers: all four data lanes fail, on both edges, at any delay. SDR50 (100 MHz) and SDR104 timing capped at 100 MHz are clean and run at about 42 MB/s, the same as DDR50. The clock tree offers nothing between 100 and 200 MHz (the shared MSDCPLL is the only source).

## Candidate 4

Two untested dimensions remain, both backed by evidence rather than guesses:
  - Host input pads. The stock `msdc_set_smt` / `msdc_set_rdtdsel` (bic-only,

so they write zero) leave MSDC1 with Schmitt inputs on CLK/CMD/DAT and `RDSEL = TDSEL = 0` at both voltages. Linux leaves LK's `SMT=0, RDSEL=12, TDSEL=5`. Candidate 4 programs the stock values for the SD host together with the drive, at the same two places (probe and the 1.8 V switch). The eMMC pads are unchanged.
  - Card output driver type. The host had no `select_drive_strength` hook, so

the core always used type B. Candidate 4 adds the hook and advertises types A, C and D for the SD host. The default is still B; `y2_lab` can request A, C or D for the next negotiation (`set drvtype=1|2|3`, then `level SDR104`).

`y2_lab` also gains `smt_clk|cmd|dat`, `pull_clk|cmd|dat`, `rdsel` and `tdsel`, so the LK values can be restored for an A/B comparison on the same boot.

## Characterization plan
  - For each setting, `level SDR104`, set the field, read raw chunks to the first

CRC (the harness above), and record the registers before reading.
  - If a setting reaches multi-GiB with zero faults, repeat on other offsets and

for much longer, with hashes, then run the full qualification list: repeated multi-GiB reads, runtime suspend and resume, idle and wake, repeated mode setup and reboot negotiation, zero CRC, timeouts, resets and unexpected fallbacks.
  - If nothing reaches 200 MHz, the production ceiling is the 100 MHz modes

(SDR50, or SDR104 timing capped at 100 MHz), with DDR50 behind them.

## Candidate 4 receipt``````````````````````````````

| Field | Value |
| --- | --- |
| Linux built source | dcbd7d1 (code 3920a54) |
| Reborn built source | b92d312cc2dc4b74f57a1a9a7b1407e34707137a, unchanged |
| Kernel / root / release / build | 6.18.0-y2linux-sd-sdr104-diag-04 / 2025.02.18-platform-v1.14 / 1.0.0-sd-sdr104-diag-candidate.4 / Y2LINUX-SD-SDR104-DIAG-04 |
| Validation | Production/platform suite 304 tests PASS; Reborn ARM QEMU, installed ARM, ELF closure, release inventory, legal-info PASS; mtk-sd.c and pinctrl.c build with W=1 without warnings, lab interface on and off |
| Package | out/y2linux-sd-sdr104-diag04-candidate/: only BOOTIMG and ANDROID/Y2ROOT; no Y2DATA, USRDATA, preloader, LK, NVRAM, PROTECT, calibration or factory image; fallback is the exact Hardware02 pair |
| BOOTIMG.img | 139e1d05fb7d5bdada4a499eb2fbfebf21467317fd01a2ee1189763284aecd19 |
| Y2ROOT.img | a88aa8395dc9dcd53e2700a4cc60bcb4ac81940d95d4fc7871c218222e629384 |

Not flashed, not pushed, no physical result.

## Tests

`tests/test_sd_tuning.py` (23 tests): window detection, wrap-around on a circular line only, midpoint and margins, the open eye, multiple windows, narrow-eye rejection, edge selection, command and data CRC classification, fault log first/last and lane histogram, pad cell decoding, pad readback and set through the real `pinctrl.c` code, RXDLYSEL, a simulated controller that runs the real tuning code (separate command and data picks, flaky taps, failure with register restore, open eye), the diagnostic output and its one-page budget, and fallback cause. `tests/test_storage_ceiling.py` keeps its contracts. Both run in `tools/production/tests.sh`.

## Candidate receipt````````````````````````````````````````````

| Field | Value |
| --- | --- |
| Linux built source | c5f0eec (code 04b41b0, identity c5f0eec) |
| Reborn built source | b92d312cc2dc4b74f57a1a9a7b1407e34707137a, unchanged since storage ceiling candidate 2 |
| Kernel / root / release / build | 6.18.0-y2linux-sd-sdr104-diag-03 / 2025.02.18-platform-v1.13 / 1.0.0-sd-sdr104-diag-candidate.3 / Y2LINUX-SD-SDR104-DIAG-03 |
| Validation | Production/platform suite 301 tests PASS (3 native-dependency skips); Reborn ARM QEMU check, installed ARM, ELF closure, release inventory, legal-info PASS; mtk-sd.c and pinctrl.c build with W=1 without warnings, with the lab interface on and off. Reborn cargo checks were not repeated: its source is unchanged |
| Preserving package | out/y2linux-sd-sdr104-diag03-candidate/: MT6582_preserve_data_scatter.txt selects only BOOTIMG and ANDROID/Y2ROOT; no Y2DATA, USRDATA, preloader, LK, NVRAM, PROTECT, calibration or factory image |
| BOOTIMG.img | 94b9976dd3fed82122197acd1f8de1fa116b346f0f1a1db0330b529261798689 |
| Y2ROOT.img | b163d0d1f9301c6067c1e46577942ca5dd3f88bac6c93b1a581425879310f1a7 |
| Fallback | Exact Hardware02 pair: fallback/BOOTIMG.imgb2a2c3bc…, fallback/Y2ROOT.img63dbd0a1… |

Not flashed, not pushed, no physical result. Owner action: flash this package's BOOTIMG and Y2ROOT with the preserve-data scatter.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
