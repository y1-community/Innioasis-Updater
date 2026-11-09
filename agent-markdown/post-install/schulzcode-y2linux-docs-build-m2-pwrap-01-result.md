---
title: "M2-PWRAP-01 — USB power prerequisite ready for device test - Innioasis Updater"
description: "M2-PWRAP-01 — USB power prerequisite ready for device test <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate ident"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-m2-pwrap-01-result.html"
---

# M2-PWRAP-01 — USB power prerequisite ready for device test - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-PWRAP-01 — USB power prerequisite ready for device test

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-PWRAP-01 — USB power prerequisite ready for device test > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Subsequent [physical photographs](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-pwrap-hardware-result.md) confirm PWRAP RC=0, CID=0x2023, VUSB=0xc000 and BEAT 50. Timer IRQ reporting returns -61; source-backed parser diagnosis is recorded. Exact flashed hash and restoration outcome remain unreported. Original handoff below is historical.

2026-09-09. #23 prerequisite for #27, under active M2 #28. Offline validated; not flashed or hardware validated. M1 remains complete. [Contract and source evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-pwrap-probe.md).

## Candidate

`/home/luca/Dokumente/Code/Y2Linux/out/m2-pwrap-01/BOOTIMG.img`

1,093,632 bytes; SHA-256: `c51102c861d65d39f5af2425ed73e9c1ba21d8adaae1b016f450a58630946ac0`.

Kernel release `6.18.0-y2-m2-pwrap1`; title/build `M2-PWRAP-01`. The earlier fallback remains `out/m1-y2b250-time32/BOOTIMG.img`, SHA-256 `074c3e6946e6e8ac61bc1df0da4fa53807071dd50ae3db4def97563c9207afce`. The owner-proven stock/FM BOOTIMG restoration boundary is unchanged.

## Change and validation

One cached probe starts after the first successful heartbeat. It first checks inherited PWRAP state; if usable, it requests PMIC CID and then VUSB status. Only wrapper read-command and completed-response acknowledgement writes occur. No PMIC register, rail/charger, clock/PHY/calibration, loader or storage write is implemented. USB is still disabled; no ttyACM enumeration is expected yet.
  - One clean build, Clang/LLD 20.1.8 and pinned Linux v6.18. The absent extracted

build environment was reconstructed from the existing locked cache; no new dependency version or repeated full source/ROM/recovery audit was selected.
  - The actual production PWRAP state machine passes 20 host fault scenarios;

production PID1 passes 13 QEMU ARM scenarios, including failed/short/invalid probe reads and timeout status while continuing all 50 heartbeats. These prebuild results are retained as a summary, not represented as hardware logs.
  - 16 build validation test methods pass, covering D08, package/formats, overlays,

renderer/guard, emitted watchdog instructions, actual artifact corruptions and linked time32 syscall behavior. Final artifact tests also pass after adding probe source/identity to the report. No compiler warning/error was emitted.
  - Linked ARM review confirms PID1-only 48-byte snapshots, caching before access,

exact resource span, CID read command `0x00800000`, guarded VUSB read command `0x02810000`, and completion acknowledgement `0xa4=1`. Fixed 1000-poll loops, no stale response clearing or reset/retry path. No new syscall is introduced.
  - Resolved configuration differs from the last time32 candidate only in

`LOCALVERSION`. DT source is unchanged; generated initrd-end follows the new 4,663-byte gzip. CPU0, D08, excluded framebuffer and D12 instructions persist.
  - [Layout](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-pwrap-01-layout.json) and

[iteration record](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-pwrap-01-iteration.json) retain exact dimensions. Resident kernel is `[0x80008000,0x8029d4f0)`; initramfs ends `0x84001237`; decompressor workspace ends `0x8038e098`. BOOTIMG wrappers/read tail and the 16 MiB BOOTIMG partition limit pass. No RAM policy or DMA ownership changes.

The ignored output bundle retains the project source snapshot, lock, ELFs, resolved config, test/build logs, focused disassembly, layout and SHA256SUMS. No physical Y2 command, flash or restore was performed in this session.

## Requested owner test and exact evidence

Use the existing proven BOOTIMG-only test procedure when ready. This handoff is a stop for the owner's physical test, not an automatic flash. Stock preloader, LK, partition tables and calibration remain protected. Observe for at most 60 seconds from power-on, with the existing manual recovery boundary.

Expected: logo, guarded diagnostic screen, first heartbeat, briefly `READ PWRAP / NO PMIC WRITES`, then continuing heartbeat/status. Normal terminal stage is `STOP: RESTORE ANDROID` after 50 successful sleeps. Probe denial/error must remain visible while heartbeat continues. An MMIO hang may leave the pre-probe stage frozen; do not retry a different address or image automatically.

Return:
  - Confirm the selected candidate SHA-256 (and flashed/readback identity if the

proven procedure supplies it); a version string alone is not hash evidence.
  - A readable full-screen photo around BEAT 5–10, and another at BEAT 50/STOP

or the exact last visible stage on failure. Include PWRAP RC/VALID, MUX/WRAP/ WACS/INIT, ARB/PRE, CID/VUSB and POST, plus BEAT/FRAME, MemTotal, uptime, timer IRQ, sleep/mount status and LAST ERR. Exact transcription is sufficient if no photo is possible; do not infer fields that were not recorded.
  - Host elapsed time from power-on and between the observations; whether the

USB cable stayed attached, and any freeze, reset or display change.
  - The result of the usual authorized BOOTIMG-only return to the known-good

system, if performed. Do not broaden a failed restore to other partitions.

Interpretation: `RC:0 VALID:3` means both transactions completed and CID low byte matched `0x23`; the full CID/revision is recorded, not predetermined. VUSB bit 14 is software enable and bit 15 the reported enable status. A zero VUSB bit is useful evidence, not permission to turn it on. `VALID:1` means only CID is valid; `VALID:0` means neither value is confirmed. `-19` is an initialization/identity refusal, `-16` busy/stale/resource refusal, `-110` timeout and `-5` lost/invalid state. A syscall/protocol failure is shown separately as `PWRAP READ ERR`.

This trial cannot close #23 or #27 by itself. Next, use the actual result to select the smallest transport/supply fix or continue the remaining USB clock/PHY/VBUS/FIFO/IRQ/DMA contract. M2 exit, media/input/standard display and basic battery/charger information remain unqualified. M3 stays deferred.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
