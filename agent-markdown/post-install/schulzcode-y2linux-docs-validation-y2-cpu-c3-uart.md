---
title: "Y2 C3 MT6582 UART admission correction - Innioasis Updater"
description: "Y2 C3 MT6582 UART admission correction <!-- knowledge-base-scope: exact-image-validation-receipt; baseline02-sync 2026-10-03 -- Baseline02 scope and current evidence Base"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-cpu-c3-uart.html"
---

# Y2 C3 MT6582 UART admission correction - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 C3 MT6582 UART admission correction

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 C3 MT6582 UART admission correction

## Baseline02 scope and current evidence

[Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md) is now the newest sealed candidate with automatic qualified CPU0 C3 startup. New-image/cold-boot hardware remains PHYSICAL_NOT_RUN. The [UART01 physical receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) proves bounded C1/C2/C3 on its exact installed pair. Default-off, UART blocker, pending-flash and harness preparation statements below retain their recorded image/session scope. They do not describe the new Baseline02 startup policy or reopen the solved UART01 architecture. This report's original exact-image evidence is preserved; full system suspend and battery measurements remain separate.

## UART01 installed hardware result — 2026-10-03

C1 WORKING; C2 WORKING; C3 WORKING_AND_REPEATEDLY_OBSERVED. The owner installed UART01; exact manifest/running identity matches Linux `e9e8d63f9c94232c2b6627881e0967583e202dac`, Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`, kernel `6.18.0-y2linux-cpu-c3-uart-01`, root `2025.02.18-platform-v1.20`, release `1.0.0-cpu-c3-uart-candidate.1`, build `Y2LINUX-CPU-C3-UART-01`. Boot `fd955840-35d9-47db-83e0-ff47d6bb2d2b` and taint0 remain unchanged. Source HEADc8ae170 is a later harness fix; installed kernel/source archives and both sealed payload hashes are unchanged. No new images or flash are needed.
  - C1: all four enabled states enter/reside,400 requested1ms wakes return;

entry deltas+1573/+521/+1343/+271, rejections0.
  - C2: natural owned CPU0 parking, +6971 entries/+50.654676s in60.054881s,

84.35% residency, zero exact clock restore failures.
  - C3: first checked reset return then20 further budget1/RGU/SRAM cycles;

+3624 entries/+39.204662s in60.088344s under normal policy, 65.25% DORMANT residency. Final3647 entries/resumes/successes/UART ACKs, no UART timeout or clock/CIRQ/timer/context restore fault.
  - All five OPPs,18 hotplug transitions, eMMC/inserted-SD checksums, screen/

workload/playback wake and USB/independent Wi-Fi integrity pass; no new filesystem/IRQ fault. GPT6/GPT4/PPI29/CNTFRQ13MHz/highres/NO_HZ remain valid.

UART1 remains clocked: source-backed PIO sleep ownership/global SPM request/ ACK permits real DPIDLE without forcing its PERI gate. Two observer defects were corrected locally: fsynced evidence must precede a read-only stable MMC/ prerequisite window; admission counters also include safe pre/post-entry guard refusals. EXACTLY one real entry/return/ACK per bounded cycle is still required, with stronger SRAM reset marker and all original restore guards. Original raw FAIL receipts are retained alongside independent successful rechecks. 33 targeted harness/CPU/UART tests pass; no kernel rebuild is needed for these host qualification corrections. Fresh candidate build validation remains375 integrated/source109/native host/Reborn238/ARM/QEMU/config/DT/modules/ABI/ELF/ package checks as recorded in the historical handoff below.

C3 is enabled with normal budget-1 for the current boot. Original screen, Wi-Fi/BT, schedutil598–1300MHz and coordinator settings are restored; RGU is unarmed. Fresh boots retain image default-off/budget0. Persistent default-on, full system suspend, endurance, additional wake sources and electrical battery improvement are not qualified by this pass. No flash/push or owner-data wipe.

Authoritative raw/joined evidence: `out/cpu-c3-uart-physical/20261003T183259Z-uart01/`; `final-verdict.json`, `guarded-21-cycles.json`, `final-snapshot.json`, `qualification/result.json`, `final-c3/qualification/result.json` and numbered SSH command/UTC/source/boot/exit/output receipts. Detailed current qualification: [Y2-CPU-C3-UART-PHYSICAL.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md).

The following sealed handoff and candidate02 sections are historical; their NOT_RUN/never-entered/owner-flash statements do not describe the current device.

## UART01 sealed software handoff — 2026-10-03

C3 SOFTWARE_READY_NEEDS_NEW_FLASH. New candidate physical NOT_RUN. Owner flash is the remaining boundary. C3 has never been entered on the connected candidate02; neither hardware failure nor hardware impossibility is established. C1/C2 physical working results are preserved.

Candidate: `out/y2linux-cpu-c3-uart-candidate/`. Build `Y2LINUX-CPU-C3-UART-01`, kernel `6.18.0-y2linux-cpu-c3-uart-01`, root `2025.02.18-platform-v1.20`, release `1.0.0-cpu-c3-uart-candidate.1`. Frozen Linux `e9e8d63f9c94232c2b6627881e0967583e202dac`, Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`. Source commits `7ef608a` and `e9e8d63` implement the contract and required kernel errno include; subsequent docs are receipts, not a different installed/build source.````

| Payload | Bytes | SHA256 |
| --- | --- | --- |
| BOOTIMG.img | 7208960 | a35e7ccb11dfcc642089e422d48a274ab2c700dbba15d00b21cce7b463e4006a |
| Y2ROOT.img | 536870912 | d3a8282a9f5d1b0046283bce1b595eb5797b62c2bff90a62260e80bbfafb5d98 |

Fresh kernel/Buildroot/Reborn ARM and config/DT/modules/ABI checks pass. Production suite375 cases: five minimal-host dependency skips are covered by native filesystem/GIO/ALSA tests and ARM compilation/query. Extended source contracts109, native packaging/filesystem/GIO27, ALSA evidence3 and Reborn238 cases pass; formatting/Clippy, Cortex-A7 QEMU, installed ARM helpers and ELF checks pass. Preserving package, source seal (445 source/license files) and sealed-image validation pass. Collector limitations remain recorded; this is an owner-local package, not public distribution approval.

Receipts: `out/cpu-c3-uart-validation/`; all integrated exit codes0. Manifest SHA256 `a43eb82521df9d94ec26b5b1cd46bd0234ff0807ffdcab7fedaf951deb04d48a`; checksum inventory SHA256 `c3041b0a848b2ce8a0a991238cee3433a43b33bf9e0654cd92e4c0bc9c945c49`. Source archives match the frozen pair. Only BOOTIMG/ANDROID payloads and accepted candidate02 fallback BOOTIMG/ROOT are packaged; no Y2DATA, preloader/LK/NVRAM/PROTECT/calibration/table payload.

Owner action: use `MT6582_preserve_data_scatter.txt`, Download Only, selecting BOOTIMG.img and ANDROID/Y2ROOT.img. Preserve existing Y2DATA. Boot normally, then confirm installation; the prepared SSH harness will verify identity and preserved regressions, attempt one25ms RGU/SRAM/budget1 timer wake, and allow20 further cycles only after real UART ACK and all same-boot restore checks pass. The packaged `CPU-C3-UART-OWNER-HANDOFF.md` gives the exact invocation. C3 stays default disabled/budget0 until the guarded physical test. No flash or push was performed; six preexisting owner doc edits remain unstaged.

Final read-only SSH receipt: `out/cpu-c3-uart-physical/20261003T164546Z/read-only-close.json`. Installed identity remains Linuxdb0234e/Rebornb71b4688, kernelidle-02/rootv1.19, boot `f155196b-64d4-45a4-88b3-27755a1a8926`, C3 disabled/budget0/entries0, expected prior probe taint4096. It contains no new UART handshake or deep wake.

## Scope and observed baseline — 2026-10-03

This pass addresses C3 UART admission only. Candidate02's physical C1/C2, parking, timers, five OPPs, hotplug and media results remain authoritative in [the physical qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION-PHYSICAL.md). C2 produced 6,772 entries and 50.669913 seconds in 60.048084 seconds (84.38%), with zero clock restore failures. C3 has never been entered; no dormant hardware failure or hardware impossibility has been demonstrated.

Fresh read-only SSH admission is under `out/cpu-c3-uart-physical/20261003T164546Z/`. Installed identity remains Linux `db0234e7519c559031da6f427869ab683ffe0f3c`, Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`, kernel `6.18.0-y2linux-cpu-idle-02`, root `2025.02.18-platform-v1.19`, build `Y2LINUX-CPU-IDLE-COMPLETION-02`, boot `f155196b-64d4-45a4-88b3-27755a1a8926`. Checkout admission HEAD `96f8ca3` is a later receipt, not the installed source. Prior removed probes explain taint 4096; no probe or C3 trial was run in this pass. Owner documentation edits are preserved separately. Normal restored radio/OPP policy adds legitimate preflight reasons; the prior settled receipt, rather than that active-policy snapshot, establishes UART1 as the sole remaining static blocker.

## Exact stock contract

All vendor references below are MT6582 at commit `d53dd75c3ff77cac3f5be58fddfe660e94f94d64`; no later SoC layout is used. Retained downloads and SHA256 receipts are in `out/cpu-c3-uart-research/` and `out/cpu-idle-completion-research/manifest.json`.``````

| Question | Source-backed answer |
| --- | --- |
| What does R7 request? | SPM_POWER_ON_VAL1 bit0 requests UART sleep/clock-off through SPM. It is not a PERI gate write. |
| Who ACKs? | Hardware exposes SPM_PCM_REG13_DATA bit20. Software polls it, never synthesizes or writes ACK. Public C source does not establish the electrical RTL aggregation. |
| Global or particular port? | There is one request/ACK pair with no port selector. Per-port participation is configured by the UART driver. Do not call the global ACK a UART1-specific signal. |
| Must UART clocks already be gated? | Default DPIDLE mask includes UART1 bit17, UART2/3 bits18/19 and excludes UART0 bit16. Driver-authorized PIO ports remove their own clock bit from that mask. An active eligible UART clock is therefore permitted before the handshake. |
| What is checked first? | dpidle_can_enter checks voltage/early-suspend policy, hotplug count, clock-manager masks and future timer. Clock manager also rejects live MSDC clocks independently. |
| How do owners interact? | UART startup opts non-DMA TX/RX into DPIDLE, enables UART_SLEEP_EN, then enables interrupts. DMA configurations stay blocked. SPM subsequently requires global ACK before PCM power/run/WFI. |
| Is our rule invented? | The old raw PERI mask is copied from stock, with extra MSDC guards. The defect is omitting stock's conditional driver integration, not the existence of bit17 in the default mask. |
| Is UART1 the Y2 console/boot logger? | Linux and retained stock kernel console are hardware UART0 at 0x11002000. Vendor one-based UART1_BASE means that same UART0. Retained LK selects hardware UART0 or UART3 conditionally; it does not prove hardware UART1 at 0x11003000 is used. Live loader branch/pin routing remain unproved. |

Primary source anchors:
  - [mt_idle.c](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/arch/arm/mach-mt6582/mt_idle.c), lines329–425:

default PERI `0x02fe87fd`, conditional mask helpers and admission.
  - [mt_clkmgr.c](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/arch/arm/mach-mt6582/mt_clkmgr.c), lines3319–3345:

live MSDC guard and group-state intersection with current condition masks.
  - [UART startup](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/uart/uart.c), lines1545–1558:

non-DMA mask admission and sleep enable.
  - [MT6582 UART implementation](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/uart/mt6582/platform_uart.c),

lines1737–1741 and2135–2144: sleep enable and clock-ID policy hooks; [register header](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/uart/mt6582/platform_uart.h) defines UART_SLEEP_EN at +0x48.
  - [mt_spm_sleep.c](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/arch/arm/mach-mt6582/mt_spm_sleep.c),

lines602–622,866 and1176–1312: request, ten10us waits, timeout restores prior POWER_ON_VAL1 and returns UART_BUSY; both DPIDLE variants request after PCM fetch and before register/power/run/WFI; wake clears request.
  - [Y2 retained binary analysis](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fobservation-path.md): FM UART

settings at `0xc04a736c`, console switch at `0xc04a9f3c`, LK selection at `0x81e00de8` / `0x81e00fc8`. Input hashes, offsets and confidence are retained there; no broad new reverse engineering or loader change is needed.

## Implemented admission and ownership

The old path already contained a bounded SPM handshake, but preflight never allowed retained UART1 to reach it. The corrected path is:

`cpuidle -> static prerequisites -> existing clock owner -> CIRQ -> Linux CPU/cluster PM -> watchdog -> PCM reset/fetch -> UART request/ACK -> unchanged 480-word DPIDLE power/run -> cpu_suspend/cpu_resume -> checked unwind`.

`uart-idle-policy.h` permits conditional UART1 deferral only with a normal LCR register bank, IER0, no DMA enable/unknown bits and a known sleep-enable value. It uses no LSR assumption: LSR0 neither proves active transmission nor prevents hardware from answering the sleep request. All other clock blockers remain effective, including MMC/APDMA/I2C/SPI. The existing clock lock remains held throughout entry and unwind. CPU0-only/IRQ-disabled entry excludes the existing process-context unused-clock worker. UART1 has no DT serial consumer.

The clock owner temporarily enables UART1's source-backed UART_SLEEP_EN, verifies readback, and restores its exact previous value on every unwind. LCR/IER/DMA and the PERI gate must remain unchanged. This is bounded sleep adoption, not proof that an inherited divisor or inactive IRQ permits shutting the UART down. No clock gate, reset, FIFO, data, baud or pinmux write is added. The existing stricter late-unused UART gate guard remains unchanged.

Mainline 6.18's 8250 MTK driver lacks this MT6582 sleep-enable operation. Patch0061 supplies it through UART0's normal driver only for exact `mediatek,mt6582-uart` PIO ports. DMA ports and other SoCs do not opt in. Failed sleep-enable readback leaves C3 blocked; console probe remains usable.

`spm-uart-policy.h` records real request/readbacks, polls through100us and restores exact prior POWER_ON_VAL1 on refusal. Existing owned requests reject without another write. No ACK means no DPIDLE PCM run and no cpu_suspend call. A qualified refusal consumes the positive budget once. Restore faults latch the existing broken-path protection. UART request/ACK use existing retained SRAM stage markers; watchdog is active before the handshake, with no journal layout or memory expansion.

SPM state and `y2-platform status cpu` expose request/ACK, attempts/successes/ timeouts/restore failures/result/rejection, POWER_ON_VAL1 before/request/after, R13 before/ACK/live bits, conditional ownership and UART1 gate before/after. Static readiness explicitly defers dynamic ACK to the real entry transaction.

## Validation and next physical boundary

Fresh focused locked-host suite: 100 tests pass. Actual C functions execute under UBSAN with injected ACK boundaries, absent ACK, dropped request/clear/ sleep writes, bank/IRQ/DMA/unknown owners, unchanged gate and all unrelated blocker bits. Tests distinguish480-word DPIDLE from28-word normal cleanup PCM. Existing CPU/context/CIRQ/timer/deadline/hotplug/OPP/fallback tests are retained. Diagnostics and actual device harness failure/quarantine are tested.

Candidate identity: `Y2LINUX-CPU-C3-UART-01`, kernel `6.18.0-y2linux-cpu-c3-uart-01`, root `2025.02.18-platform-v1.20`, release `1.0.0-cpu-c3-uart-candidate.1`. API1, partition/data schemas and Reborn source remain unchanged. Fresh kernel, Buildroot/Reborn ARM and preserving package validation receipts will be attached at handoff; no prior binaries are reused.

The single intended candidate is `out/y2linux-cpu-c3-uart-candidate/`, only BOOTIMG and Y2ROOT, with previous accepted images as optional fallback. Y2DATA and protected partitions are preserved. No flash or push is performed. C3 stays default disabled/budget0. Its handoff state is SOFTWARE_READY_NEEDS_NEW_FLASH, not physically working.

After owner installation, use the packaged SSH harness without probes. It checks exact installed identity, C1/C2/timers/hotplug/storage/five OPPs, then waits for natural screen-off/radios-off/USB-detached CPU0 at <=747.5MHz. The first trial has budget1, retained evidence,10s RGU and25ms timer wake. Require new UART request/ACK, attempts/entries/resumes/successes +1, positive residency, same boot, clean context/timer/CIRQ/gate/storage restores and a responsive system. Only then allow20 additional bounded trials at varied deadlines. A failure disables C3 and stops repetition; the precise stage is captured. No runtime policy promotion or battery-life claim precedes evidence.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
