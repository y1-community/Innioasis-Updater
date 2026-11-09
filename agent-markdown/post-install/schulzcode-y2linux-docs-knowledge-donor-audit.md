---
title: "Y2 donor audit and Linux 6.18 integration decision - Innioasis Updater"
description: "Y2 donor audit and Linux 6.18 integration decision <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-donor-audit.html"
---

# Y2 donor audit and Linux 6.18 integration decision - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 donor audit and Linux 6.18 integration decision

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 donor audit and Linux 6.18 integration decision > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-10: [additional reverse-engineering audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md) supplies experiment history and selected captures for this exact donor. It resolves the stale 368-line claim, explains cold display/audio failures and identifies two fixes already covered by 6.18. Power-key and Bluetooth conclusions below are corrected accordingly. Their results are not ours.

2026-09-09. Canonical baseline `8ebc800`. M1 complete; M2 active with exit criteria unmet; M3 and application development remain gated.

## Material and review limits

Reference: `artificery-dev/linux`, `tempo/innioasis-y2`, Linux 6.12, base `adc218676eef25575469234709c2d87185ca223a`, head `53fb57bb99c916c24b65db5b7f9723be37f67826`. The immutable local `donorSource/` bundle contains 364 changed source/build files, 8,650,507 bytes, 36 commits. All supplied SHA256SUMS entries match. All 372 files inside the zip match the extracted files, including metadata; the zip adds no hidden implementation. The commit list attributes the series to Chris Hendrickson. Preserve each file's existing SPDX/copyright and record its originating commit when reusing it. The bundle is a changed-file snapshot, not a complete kernel or independent record of donor hardware tests. Referenced donor test notes, configurations, firmware and ROMs are not included. Do not equate comments saying "confirmed" with a result on our older Y2.

[Inventory](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/donor-files.tsv) covers every changed path, hash, size, line count and whether that path exists in our locked upstream v6.18 tree. 314 paths are absent in v6.18; 50 exist with different contents. Those differences include ordinary 6.12→6.18 evolution: they are not all donor changes to import. [Commit metadata](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/donor-commits.tsv) retains the complete supplied history. All source files were inventoried and read for structural/source comparison; M2 controllers, board DT, audio and integration changes received focused review. The 296 connectivity/Bluetooth paths account for 7,496,956 bytes (87% of source bytes); they received architectural triage, not a line-by-line correctness or security certification. No whole radio dump belongs in the M2 build.

Compared with the local Y2PlayerNative blueprint, current GitHub issues #1–32, our v6.18 source/config/DT and retained stock/Linux evidence. USBACM-03 has a real 11,754-byte LOG1 capture, kernel sequences 0–77 and PID1 beats 1–43 without reported relay gaps/errors. USBACM-04 has offline validation only. Host USB inspection through host execution found no attached Y2 during this audit. No new hardware result, build or flash is implied by this document.

## Subsystem matrix

Reuse classes (split when a row combines distinct drivers): A our/upstream 6.18 solution is preferable; B likely small adaptation; C substantial forward-port; D evidence; E correction required; F implementation missing in both projects. Availability is separate from hardware readiness. Paths below are relative to the donor snapshot unless explicitly identified as upstream or canonical.``````````````````````````````````````````

| Subsystem | Class | Useful implementation and decision | Dependencies / remaining proof |
| --- | --- | --- | --- |
| RAM | D | Board DT admits [80000000,be000000), consistent with our stock 992 MiB main bank. Reservation/ownership reconciliation below precedes adoption. | #22; LK lifetime, every active DMA master, lowmem/HIGHMEM, allocator tests. |
| SMP | B | platsmp.c adds MT6582 to the existing MT7623 SRAMROM layout at 10202000; reuse upstream MediaTek SMP with reviewed match data. | SRAM ownership, secondary release/coherency, GIC, clocks/thermal; optional for initial input. |
| Clocks | E | clk-mt6582*.c supplies useful gate/mux register tables, but parent order is explicitly "best-effort", PLL postdiv approximate and VENCPLL a guessed 500 MHz. | Check retained vendor clkmgr; proper CCF providers before clocked consumers. Preserve USB and inherited scanout gates. |
| Reset | A | Upstream mtk_wdt.c already matches MT6582 and supplies reset-controller infrastructure. No reason to import raw radio RGU writes as general reset support. | Keep our early watchdog stop; audit individual reset lines/consumers before enabling. |
| GPIO | B | gpio-mt6582.c: 169 pins, 16-pin/16-byte banks, DIR/DOUT/DIN/SET/CLR. Retained vendor layout corroborates offsets. Adapt resource lifetime and v6.18 callbacks. | First candidate exposes inherited input levels through standard GPIO and evdev; output/pinmux ownership follows. |
| pinctrl | F | No MT6582 pinctrl implementation: donor explicitly inherits muxing. Changing pinctrl Kconfig is not a pin controller. | Build proper mux/bias/range descriptions from vendor tables; do not swallow missing pinctrl in storage. |
| IRQ | A | Our working upstream GIC/sysirq/timer remain preferred. Donor EINT glue is useful, but v6.18 mtk_eint now takes base arrays/nbase and a pin map argument. | EINT translation/mux map and teardown before enable; do not assume every GPIO equals its EINT solely from the comment. |
| PWRAP / MT6323 | E | mtk-pmic-wrap.c adds an MT2701-like variant and optional wrapper IRQ. Source is useful; ignored negative optional IRQ errors include probe defer. Full transport would conflict with our persistent USB PWRAP claim. | One transport owner/lock shared by USB, MFD and consumers; preserve observed sync-idle wait. |
| Regulators | A | Use upstream v6.18 MT6323 MFD/regulators. Donor DT contributes VGP2, VCN and VIBR consumer clues, not a new regulator driver. | PWRAP + PMIC IRQ, real rail mapping/limits and unused-regulator policy; no dummy supplies. |
| Battery / charger | E | mt6323-charger.c has ADC/status/register knowledge, but unchecked writes, heuristic voltage→capacity/full claims, unconditional present, recurring re-enable and optional higher-current recovery. | Start with serialized ADC/status and real units; separate policy, watchdog and calibrated battery/thermal limits from telemetry. |
| I2C | D | No new bus driver. DT claims mt6577-i2c, AP-DMA channels 11000200/280, SPI44/45 and fixed 66 MHz/div16. | Upstream v6.18 i2c-mt65xx; verify IP quirks, real clocks/pins, DMA mask/buffer ownership and inherited channel quiescence. |
| Wheel rotation | B | apt32f-wheel.c: address 0x51, register-zero repeated-start nine-byte frame, class3 and codes1–4, data-ready55. | I2C + EINT; check AA as well as 55, transfer errors/capability; validate direction/acceleration then use standard relative wheel events where appropriate. |
| Navigation buttons | B | Board DT maps active-low GPIO6/7/9/10/54 to left/back/right/playpause/enter. Reuse upstream gpio-keys family. | GPIO; verify mapping on our revision. Polled evdev first needs neither EINT nor I2C DMA. |
| Volume / power key | E / A | Keypad gives MEM1 bits0/1 and SPI116 but needs clock/lifecycle/error correction. PMIC patch guards a missing-home-key pointer in long-press setup; v6.18 already uses static register descriptions and needs no such patch. | Keypad gate/keycode/register/lifetime validation. Use upstream PMIC keys after EINT25/MFD; preserve long-press recovery. |
| Display interface / DRM | C | OVL→RDMA→COLOR→DSI, MMSYS/mutex and old format/FIFO data are high-value inputs. Port variants into current DRM helpers rather than replace files. | CCF, coherent DMA/CMA/IOMMU/SMI choice, quiesced old scanout, panel, atomic state, failure fallback. |
| GC9503V panel | E | panel-gc9503v.c has a valuable LK init/gamma table. Comments claim 368 lines/sync-event; emitted mode is 360/sync-pulse. Board DT omits power/reset/backlight relationships used by driver. | Reconcile with our proven 480×360 scanout and LK, electrical reset polarity, real supply and link timings. |
| Backlight | E | mt6323-backlight.c gangs four ISINKs into one class device, but drops every regmap error; comment ceiling1 conflicts with code5/full-brightness probe. Step/duty arithmetic drops brightness at boundaries (31→32). | MFD/regmap owner, verified current ceiling, monotonic map, error/shutdown handling and panel binding. |
| eMMC | E | Board uses mt8135-mmc, 8-bit/50 MHz and fixed 3.3 V. Optional-pinctrl patch masks all errors, including defer, across the generic driver. | Verify MT6582 quirks, clocks/VMCH/VEMC/pins and DMA. Read-only understanding first; no partition writes or donor root=p8 adoption. |
| microSD | E | Same MSDC source; 4-bit/50 MHz, broken-cd polling, shared fixed supply and inherited pins. Comment explicitly says it may not work. | Real VMC/VMCH topology, pins/card detect, DMA and read-only removable-media test; no automatic mount/write. |
| USB | A | Keep canonical kernel/usb/ PIO MUSB and LOG1 capture. Donor generic PHY rewrites digital/analog session controls with no equivalent observed-state guards and fake clocks. | #27 robustness remains open; generic transport/clock refactor must preserve physical baseline. |
| Watchdog | A | Our reviewed early AP_RGU stop covers pre-probe boot; upstream MT6582 watchdog is preferable for later standard ownership. | Driver handoff, timeout/pet/reboot evidence; donor charger watchdog is a separate device. |
| Thermal | F | No thermal sensor/calibration/trip/cooling driver added by donor. SPM thermal handshake does not measure temperature. | Sensor/ADC/efuse contract, trustworthy units/protection before sustained loads. |
| cpufreq / cpuidle | F | No MT6582 OPP/cpufreq or deep-idle implementation in bundle; normal SPM program is not DVFS/suspend support. | Accurate CPU/bus PLL model, regulators, OPPs, thermal, CPU coordination. |
| Audio AFE / I2S / DMA | C | sound/soc/mediatek/mt6582/ implements DL1→I05/I06→O00/O01→second I2S (I2S_CON3), IRQ and 8–48 kHz rate table. | M3: v6.18 common AFE API/lifetime, DMA/IRQ race review, clocks/PM, real samples/rates. Remove unrelated FM path for this board. |
| CS43131 | A | Upstream v6.18 cs43130 already supports CS43131. Donor machine/DT gives bus1:30, 22.5792 MHz crystal, GPIO20/18/15 and VGP2 clues. | Validate rail identities/voltage/order; nominal GPIO "regulators" do not prove the electrical supply model. |
| AW87559 | B | New codec component with AW87559/OCA72559 IDs and stock register sequences; bus1:58, enable8. | M3: fail-safe mute/drop-enable on table-write failure, shutdown, board population and safe levels. |
| Headphone routing / detection | E | Machine driver routes DAC through amp and changes DAC PCM_PATH_CTL_2 for mono speaker. IRQ16/codec jack detection is only DT/source evidence. | Mutual exclusion, jack API/event policy, pop-safe ordering; DAPM event returns update_bits positive-change value rather than zero success. |
| Haptics | B | DT uses upstream regulator-haptic with MT6323 VIBR. | PMIC regulator, actual motor voltage/current/duration; no 3.3 V assumption from comment alone. |
| Wi-Fi | C | Vendor fullmac cfg80211 port and AHB HIF 180f0000, WMT firmware/power dependencies. | Later #31; firmware/calibration, memory, shared power/locks and 6.18 cfg80211 review. |
| Bluetooth | C | WMT/STP over BTIF plus standard HCI bridge, optional competing vendor char channel. History adds cold modem/calibration prerequisites outside the kernel bundle. | Later #31; transport/firmware/AP-DMA/exclusive ownership. Correction: Basic Rate is a controller-scoped HCI quirk, not a blanket ban; still an unresolved EDR workaround. |
| FM | D | MT6627/STP and AFE ASRC route are reference for other revisions. | Owner confirms this older Y2 lacks usable reception hardware. Exclude from this device's implementation/exit promises. |
| GPU / SPM | E | Lima DT, MFG genpd and normal-mode PCM provide leads; overlapping SPM mappings use devm_ioremap to evade exclusive claims; PCM uses virt_to_phys without DMA API. | Later, or only required core dependency: shared regmap/genpd and DMA ownership/cache visibility. No GPU required for first input. |
| RTC / power-off | B | Board describes existing upstream MT6323 RTC and power controller. | PMIC transport/IRQ and tested shutdown; retain current recovery behavior until qualified. |
| Development rootfs | D | Donor DT mentions eMMC p8 but bundle contains no usable rootfs/config/package recipe. | Keep initramfs for bring-up, progress to removable media once storage and RAM pass; #28/#32 own later image/layout choice. |

## RAM reconciliation

Additional concrete correction targets: the apmixed probe never stores its `clk_data` with `platform_set_drvdata`, but remove retrieves and dereferences that value. The DRM/PHY changes include direct framebuffer `ioremap` writes at `bfb54600` and hardcoded FIFO values in shared component paths. They need to be removed or properly restricted by variant data. The donor's regmap debugfs-write enable and EDR fallback are not M2 platform foundations.

Our [D08 analysis](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Finitial-ram-map.md) is stronger than the donor DT alone: stock reports `[80000000,be000000)`and`[bf800000,bfa00000)` as RAM; `[bfb00000,c0000000)` is framebuffer. The traced default model explains modem `[be000000,bf800000)`, connectivity `[bfa00000,bfb00000)` and LK display scratch starting `bf700000`. The donor instead reserves `[bdf00000,be000000)` for its connectivity driver. That is a new chosen location, not proof that inherited connectivity DMA already uses it. Keep all high exclusions until ownership is established. Its claimed scanout at `bfb54600` also differs from our guarded, physically working `bfb00000` aperture; do not substitute donor addresses.

LK code/BSS begins `81e00000`, BSS ends `81e55434`; heap high-water and final DMA ownership are still missing. The donor does not resolve these by advertising a large bank. Do not invent a heap cap. Next RAM work under #22 should target a useful large static bank toward the evidenced 992 MiB, with explicit loader and DMA exclusions, rather than repeat tiny increments. First input keeps D08.

For a successor policy, use the resolved v6.18 ARM `PAGE_OFFSET`, vmalloc reservation and lowmem limit, not the donor comment's approximate 760 MiB. 992 MiB at the usual 3G split needs HIGHMEM or another reviewed virtual layout; physical DRAM below 4 GiB does not mean it all fits the direct map. Keep kernel, initrd and DMA allocations addressable, use DMA APIs and measure zone/highmem pages. Preserve low tags, BOOTIMG load/copy/decompressor bounds and high display carveouts. Full memory/layout/config regression plus allocator-owned-page allocation/write/verify/release on hardware is required. Source claims alone cannot close the DMA/heap gap or certify maximal RAM.

## New execution order and first slice

The donor removes much of the need to discover controller register maps from scratch. The highest-value ports are GPIO/input, corrected CCF/PWRAP shared providers, APT32F over the upstream I2C controller, then DRM/panel and MSDC. The old serial #27→#22→#23→#24→#25→#26 queue is superseded by dependencies:
  - Preserve USBACM-03 and the pending USBACM-04 robustness candidate. Implement

GPIO navigation→upstream gpio-keys-polled→evdev→existing USB logs on D08. Use five explicit active-low lines and a 20 ms poll interval. A read-only inherited-input provider verifies input direction; no pinmux/rail/clock/IRQ rewrite or DMA is needed for this complete navigation-event path. It is an initial GPIO subset, not completed pinctrl/EINT/wheel support.
  - Reconcile large-bank RAM and shared CCF/PWRAP resource ownership alongside

the returned input evidence. Then combine GPIO/EINT + I2C/AP-DMA + wheel, keypad clock + volume keys, and PMIC MFD + power key/telemetry as coherent consumer/provider slices. Avoid independent raw PWRAP users.
  - Correct and port display/panel/backlight together after supplies and DMA

layout are ready; retain USB during takeover. Bring removable storage and development rootfs forward as soon as clocks/pins/rails/DMA permit. eMMC begins with read-only access, never assumed donor partition usage.
  - Complete basic power/thermal reporting, watchdog ownership and repeated

boot/input/display/storage/rootfs/log qualification before M2 closure. M3 then starts from donor AFE plus upstream codec support; radios stay later.

First input adds a new hardware subsystem: one clean build, complete existing offline suite, meaningful GPIO refusal/bank-boundary and ARM evdev/relay tests, resolved DT/config and current D08/BOOTIMG checks. No duplicate source hashing, ROM provenance or SPFT research. Stop at a reviewable BOOTIMG for the owner's manual flash; real key mapping, event continuity and USB survival remain unproved until capture. No physical flash by the assistant, no loader/calibration or partition changes, no milestone promotion and no speculative issue fan-out.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
