---
title: "M1 — Linux 6.18 First Boot - Innioasis Updater"
description: "M1 — Linux 6.18 First Boot <!-- knowledge-base-scope: decision-log-/-historical-roadmap -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-m1-first-boot.html"
---

# M1 — Linux 6.18 First Boot - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M1 — Linux 6.18 First Boot

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M1 — Linux 6.18 First Boot > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Historical milestone record. For current platform status and work ordering, use [CURRENT_PLATFORM_STATE.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md) and the [Platform v1 roadmap](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Fplatform-v1-roadmap.md).

Canonical [milestone 2](https://github.com/SchulzCode/Y2Linux/milestone/2). Core objective achieved on the physical Y2: Linux 6.18 + initramfs + native PID1. The M1 milestone is closed for this core objective. Physical UART research #16 remains open outside the milestone; remaining diagnostic uncertainties are recorded separately rather than treated as failures of the core boot objective.

The latest owner report confirms `6.18.0-y2-m1`, increasing BEAT and uptime, working sleep, proc/sysfs mounts, framebuffer diagnostics, watchdog stopped, CPU0 online and static D08 RAM visible. [Hardware result and remaining diagnostic uncertainties](../knowledge/m1-runtime-hardware-result.md). This supersedes the historical sleep -38 and hardware-pending status below. It does not certify unreported counters, run duration, expanded RAM or unrelated peripherals.

[The historical foundation queue](#historical-foundation-research-queue) was planning only. No new code/build/flash or M2 execution occurred in this session. M1 core success does not require another build or retrospective full-suite run: today's change records hardware evidence, not a new release-candidate certification. The sections below preserve the earlier implementation/research chronology.

The owner explicitly changed execution for M1: the lead researches and implements directly, without delegation. Tiny sequential issues preserve reviewable checkpoints; none is state:luna-ready. All commits use the owner's configured identity and issues use the authenticated owner account. Platform work remains solely in Y2Linux.[](https://github.com/SchulzCode/Y2Linux/issues/8)``[](https://github.com/SchulzCode/Y2Linux/issues/9)``[](https://github.com/SchulzCode/Y2Linux/issues/10)``[](https://github.com/SchulzCode/Y2Linux/issues/11)``[](https://github.com/SchulzCode/Y2Linux/issues/12)``[](https://github.com/SchulzCode/Y2Linux/issues/13)``[](https://github.com/SchulzCode/Y2Linux/issues/14)``[](https://github.com/SchulzCode/Y2Linux/issues/15)

| Checkpoint | Dependency | Completed change | Commit |
| --- | --- | --- | --- |
| Y2B-201 / #8 | Y2E-125/130 | Locked source/tool environment and ARMv7 smoke test | fc53655 |
| Y2B-205 / #9 | #8 | D08 arithmetic validator and rejection cases | fccf52d |
| Y2B-210 / #10 | #9 | Minimal CPU0 config; D09 makes no-hyp selection enforceable | 9de3428 |
| Y2B-215 / #11 | #10 | D08 DT memory and researched CPU/GIC/GPT/UART foundation | 1e6a2b5 |
| Y2B-220 / #12 | #11 | Tiny deterministic diagnostic initramfs and QEMU user self-test | 927e457 |
| Y2B-225 / #13 | #12 | Actual ELF/DT/gzip layout checks, fixed physical base, appended payload | 950af2e |
| Y2B-230 / #14 | #13 | Strict legacy MTK package and explicit LK read padding | 84d1bf2 |
| Y2B-235 / #15 | #14 | Clean reproducibility, actual corruption tests, retained result and launch-gate review | Final result commit containing this document |

[Result, exact versions/hashes/map](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Ffirst-boot-result.md) and [reproduction commands](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Ffirst-boot.md) are authoritative for this artifact. D08 limits are unchanged. Configuration resolution exposed a hidden upstream option; bounded research produced one Kconfig prompt-visibility patch (D09) rather than accepting a policy violation.

The [hardware launch-gate review](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Ffirst-boot-launch-gates.md) identifies the next smallest missing proofs. No speculative peripheral/rootfs/SMP backlog or next implementation wave is created. The current output is an unsigned offline candidate. Closing the eight implementation checkpoints does not close M1, pass M0, authorize a DA, raw acquisition, flash, boot or restore, or prove the physical console. The next wave must start from launch-gate evidence and a concrete separately authorized experiment.

## Observation gate follow-up

[Y2E-140 / #16](https://github.com/SchulzCode/Y2Linux/issues/16) is open: installed ttyMT0/UART0 evidence prompted D10 and two fully validated reproducible builds, plus receive-only host tooling. The first-artifact hashes above now resolve to the current UART0 result; historical UART3 reports/bundle remain retained. Physical TX/GND/level and actual stock LK/kernel serial capture are still missing. No further kernel feature or device experiment was added.

[Y2E-145 / #17](https://github.com/SchulzCode/Y2Linux/issues/17) records the subsequent NO-GO decision for the unchanged candidate, hardware-dependent authentication, denied current raw acquisition and adverse normal-path watchdog evidence. [Decision](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Flaunch-readiness.md). M1 remains open; no first-boot operation issue exists.

Y2E-150 / #18 now supplies D11–D13 and the [risk-accepted diagnostic result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Frisk-diagnostic-result.md). Research `3aeeb03`; implementation `1234f85`; two final builds match and all 11 tests pass. The previous NO-GO hard gates are superseded by owner-accepted risk; watchdog and guarded visual diagnostics are implemented. Y2B-240 prepares one BOOTIMG-only experiment requiring separate hardware authorization. M1 remains open until actual boot evidence is reviewed.

Execution checkpoint: [Y2B-240 / #19](https://github.com/SchulzCode/Y2Linux/issues/19), awaiting separate owner hardware authorization.

Y2B-245 offline implementation is complete at source `d83fccf`. Two release builds match across 12 outputs and all 14 tests pass. [Final artifact and validation](../build/y2b245-result.md). New text-candidate hardware validation remains pending separate authorization; Linux-plus-PID1 boot is already achieved by Y2B-240 solid green.

## Current hardware boundary: Y2B-250

The owner reports the real Y2B-245 renderer, PID1 and successful proc/sysfs mounts, followed by `BEAT: 0 / STOP: SLEEP ERROR / -38`. [Evidence and root cause](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2b245-hardware-result.md). [Y2B-250 #21](https://github.com/SchulzCode/Y2Linux/issues/21) enables the missing ARM time32 ABI. No increasing heartbeat has been established; no new flash or M2 is authorized.

Localized iterations now use one clean build, directly affected tests, D08/layout/BOOTIMG safety validation and final image size/hash. Trust the unchanged audited source and locked toolchain; do not repeat full provenance/recovery audits or two reproducibility builds. Reserve exhaustive verification for architecture/memory/packaging changes, new subsystems, milestone completion and release candidates.

Y2B-250 is built and validated offline: [candidate and focused results](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2b250-result.md). The real timer/heartbeat trial remains pending; no milestone-completion claim is added.

## Post-core roadmap audit, 2026-09-09

[Full coverage and remaining phase gates](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md). M1 core remains achieved. Broader exact-artifact boot repeatability, timing accuracy and long-run qualification remain under Y2H-300 #28 rather than being silently inferred from the successful screen. Five later-phase epics are deferred; no new implementation or hardware test was performed.

## Historical foundation research queue

The September 8–10 queue followed the initial M1 runtime result. Its order and bounded research goals are retained here after removing the superseded rolling "next five" task list. These are historical scopes; the current implementation, qualification gaps and next work are in the [Platform v1 roadmap](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Fplatform-v1-roadmap.md). The original detailed specifications remain in `issues/`.[](https://github.com/SchulzCode/Y2Linux/issues/22)[](https://github.com/SchulzCode/Y2Linux/issues/23)[](https://github.com/SchulzCode/Y2Linux/issues/24)[](https://github.com/SchulzCode/Y2Linux/issues/25)[](https://github.com/SchulzCode/Y2Linux/issues/26)

| Order | Stable issue | One deliverable | Dependency interpretation |
| --- | --- | --- | --- |
| 1 | Y2E-155 / #22 — Specify one safe static RAM expansion step | One exact additional-RAM policy or a precise NO-GO | Uses Y2E-130, Y2B-250 and current hardware evidence; D08 unchanged until a reviewed successor. |
| 2 | Y2E-160 / #23 — Establish the MT6323 power and supply prerequisite map | Minimal PMIC transport/supply ownership contract | Follows the RAM decision; does not require actual expansion. |
| 3 | Y2E-165 / #24 — Resolve the wheel and select-button event path | CW/CCW/select evdev implementation contract or bounded blocker | Uses supply/transport findings; full input and power drivers are not prerequisites for research. |
| 4 | Y2E-170 / #25 — Specify a safe display handoff and backlight ownership boundary | One standard-interface takeover decision preserving observation | Uses power ownership and proven D13/D14; follows input research without requiring its driver. |
| 5 | Y2E-175 / #26 — Specify a read-only removable-SD controller proof | One slot/controller read-only test contract or first missing prerequisite | Uses RAM, power and inherited display-DMA exclusions; keeps eMMC disabled. |

The ordering put RAM headroom before shared power, local controls, display and removable storage. Removable SD was the smaller initial storage surface than internal eMMC; inherited pixels did not establish a display-driver contract. The later [DEV-02 qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-dev02-live-qualification.md) records the narrow achieved scope. Source availability and external hardware success did not authorize RAM expansion or substitute for this unit's evidence.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
