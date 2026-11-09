---
title: "Baseline02 integrated preserving candidate - Innioasis Updater"
description: "Baseline02 integrated preserving candidate Sealed build receipt — 2026-10-03 PASS for fresh build and software/package validation. The compiled source and artifact identi"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-baseline-02.html"
---

# Baseline02 integrated preserving candidate - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Baseline02 integrated preserving candidate

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Baseline02 integrated preserving candidate

## Sealed build receipt — 2026-10-03

PASS for fresh build and software/package validation. The compiled source and artifact identities below are the current sealed Baseline02 record. Exact new-image hardware and automatic cold-boot qualification remain NOT_RUN. Prior UART01 C1/C2/C3 architecture remains physically qualified; it is the unchanged paired rollback.````````````

| Field | Recorded identity |
| --- | --- |
| Build | Y2LINUX-BASELINE-02 |
| Kernel | 6.18.0-y2linux-baseline-02 |
| Root | 2025.02.18-platform-v1.21 |
| Release | 1.0.0-baseline-candidate.2 |
| Compiled Linux | 8584ccd85f052f351fe51650b2348c83ca894ed4 |
| Compiled Reborn | b71b468860233faa0a42b8448ec5777fa952b8e3 |
| BOOTIMG SHA256 | 5d8a2999368a04b23b898d2106b465eb6b028c2314da1a39c66c6b26dc8c41a3 |
| Y2ROOT SHA256 | 3148bea2b6d78be34afcbb9cd933502f14416e81c8053324ff6c9ea151ee3892 |
| Manifest SHA256 | 122d6f5d73f3416a2608f770b1d05af5b0ba81db27c315639f56458833cc5654 |
| SHA256SUMS SHA256 | e50c83d37712649466e10188e1eded6b6ccec5f830f86881b028ea86d5d3a654 |

Package: `out/y2linux-baseline-02-candidate/`. Exact owner handoff (`out/y2linux-baseline-02-candidate/BASELINE-02-OWNER-HANDOFF.md`, local-only), seal and check exits (`out/baseline-02-validation/final-seal.json`, local-only), installed boot-policy bytes (`out/baseline-02-validation/boot-policy-installed.json`, local-only), live ARM control proof (`out/baseline-02-validation/live-policy-control.json`, local-only), closing installed-device read (`out/baseline-02-validation/closing-hardware.json`, local-only).

Fresh kernel/config/DT/modules/ABI and ARM Buildroot/Reborn pass. The integrated suite has 391 cases: 386 passed and 5 minimal-environment dependency skips, covered separately by 27 native filesystem/GIO, 3 ALSA and installed ARM checks. All 125 focused source tests and 238 Reborn tests/fmt/lint pass, as do Cortex-A7 QEMU, installed ARM platform/application/codecs, ELF/dependencies, source/license collection, filesystem/privacy, preservation and final sealed-package checks. Collector limitations and owner-local distribution status remain explicit in the package.

New production behavior: S05y2-cpu-idle verifies static foundations, then reads back qualified budget-1/CPU0 enable once each boot. The kernel starts quarantined. No CPU1–3 C3 enable, forced parking/OPP/radio change, UART gate or weakening of entry/fault guards. Boot-policy JSON in status CPU records exact rejection; write/readback/receipt failure closes admission. Manual stop is respected by subsequent starts. Recovery: `y2.deep_idle=off` / `y2.cpu_safe=1`, or `y2-platform cpu-idle-policy stop` for this boot. The guarded harness checks real automatic activation before it quarantines C3 for its foundation/trial phases.

Closing SSH verifies the old installed UART01 source, same boot/taint0 and3647 C3 returns with zero UART timeout/restore failure. No new image was installed. Only the owner flashes: load MT6582_preserve_data_scatter.txt, Download Only, select BOOTIMG and ANDROID/Y2ROOT only, preserve USRDATA/Y2DATA and every protected partition. Then boot and confirm installation for the included automatic SSH qualification. No push or flash was performed. Full system suspend, additional wake sources/endurance and electrical battery measurement remain unqualified.

Local source commits:5fec95e (baseline identity/preparation),8584ccd (automatic qualified boot policy and harness/fault tests). The later documentation receipt commit is not the compiled kernel/root source. Historical preparation below and source-era package documentation are superseded by this sealed receipt and the packaged manifest/owner handoff. The interrupted default-off draft made no package; its logs remain under validation/draft-default-off/. Initial native test-path probe history is preserved under pre-freeze-probes/; final fresh checks pass.

## Repository documentation synchronization — 2026-10-03

Entry pages, current state/candidate/capability summaries, roadmap, power/API contracts, maintained knowledge, release guides and the 233-feature Markdown/JSON inventory now follow this sealed baseline and the exact UART01 hardware proof. The catalog indexes all 289 Linux Markdown pages; 4,329 local links have zero problems. The adjacent Reborn check also passes (58 pages / 563 links).

All 27 documentation/structure/preservation checks pass, including matrix/JSON parity, feature enums/references, 49 overlays against the active manifest, historical census retention, all-page scope, preexisting owner edits and raw capture preservation. `git diff --check` passes. Baseline02 manifest/checksum inventory hashes remain identical to the seal. Private check receipt: `out/docs-baseline02-sync/validation.json` (local-only).

This update changes no implementation, package bytes, runtime flags or physical acceptance. No build, device test, flash, push or repeat of unchanged stock/recovery provenance occurs. Historical reports remain at their original paths and retain their exact-image PASS/FAIL/NOT_RUN results.

## Historical preparation snapshot — superseded by the sealed receipt

The following preparation text records the pre-seal plan. “Pending”, “will” and harness-order statements below are historical; the sealed receipt above and packaged harness govern current behavior.

Owner requested a new latest-source baseline on2026-10-03 after UART01 hardware qualification. Candidate preparation is authorized; flashing and pushing are excluded. All current Linux changes and Rebornb71b4688 are included; the only new production behavior is the owner-selected automatic C3 boot policy. There is no new CPU architecture, memory/layout or data-schema change.

Build `Y2LINUX-BASELINE-02`; kernel `6.18.0-y2linux-baseline-02`; root `2025.02.18-platform-v1.21`; release `1.0.0-baseline-candidate.2`. Only BOOTIMG and ANDROID/Y2ROOT are payloads; preserve Y2DATA and all protected partitions. Fallback retains the exact physically qualified UART01 pair.

C1, C2 and C3 architecture is physically qualified on the preceding UART01 image: four-core WFI, C2+6971entries/84.35%,21 bounded reset-and-return C3 trials and+3624 normal-policy entries/65.25%, all checked context/timer/CIRQ/ clock/storage restores clean. See [authoritative hardware record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md). Read-only admission reconfirms same boot/taint0/3647 C3 returns. This evidence is inherited architecture evidence, not physical acceptance of new images. The new package remains PHYSICAL_NOT_RUN until owner installation and checks.

Owner selects automatic qualified C3 after boot. Kernel registration still starts quarantined/default-off/budget0. `S05y2-cpu-idle` applies the qualified policy once after static identity/SPM/CIRQ/context/timer foundations pass: budget-1, then CPU0 state2 enable, both read back. A failed write rolls back. All dynamic topology/OPP/screen/workload/radio/USB/clock/deadline/UART ACK and restore-failure guards remain unchanged. No active device or clock is forced. Repeated startup respects a later manual disable. Recovery boot options remain `y2.deep_idle=off` and `y2.cpu_safe=1`; `y2-platform cpu-idle-policy stop` closes C3 for this boot. Status CPU exposes the boot-policy result/rejection.

The packaged harness first disables C3 before foundation qualification and uses21 bounded checked reset-and-return trials before runtime observation. New persistent cold-boot behavior is NOT_RUN until owner installation. This does not qualify full system suspend, battery life or wider endurance.

Fresh build/validation and seal receipts will be recorded under `out/baseline-02-validation/`. Final package: `out/y2linux-baseline-02-candidate/`. Existing historical candidate directories are immutable. No source or userspace build outputs are reused.

Automatic policy source tests and live ARM control/readback transaction pass. Live test uses the same qualified UART01 boot and restores original budget-1/ CPU0 enable; it is not a new-image cold-boot test. `/run` evidence is transient; no boot-time polling, persistent data record or radio/OPP/hotplug change is added. Failed activation rolls back, failed foundations stay quarantined and subsequent start cannot replace an owner's runtime control. Foundation and runtime behavior remain distinct: normal activity can legitimately reject individual C3 attempts.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
