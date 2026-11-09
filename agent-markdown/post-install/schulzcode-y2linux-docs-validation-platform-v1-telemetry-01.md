---
title: "Platform v1 telemetry repair — 2026-09-25 - Innioasis Updater"
description: "Platform v1 telemetry repair — 2026-09-25 <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-platform-v1-telemetry-01.html"
---

# Platform v1 telemetry repair — 2026-09-25 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Platform v1 telemetry repair — 2026-09-25

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Platform v1 telemetry repair — 2026-09-25 > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Subsequent owner-installed retest: both repairs now pass their narrow physical checks on boot `3194fa9d-2dee-4105-86f0-4021580bf8d0`. Status/health return; no reader remains after a bounded counter timeout while charging. See the [latest physical report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-PHYSICAL-QUALIFICATION.md) for exact identity, timings and evidence. Remaining kernel warnings stop Session A and Wi-Fi health is failed/degraded. This does not promote Platform v1 or waive any physical gate.

This is the separately owner-authorized corrective pass following the [physical qualification stop](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-PHYSICAL-QUALIFICATION.md). No repair was applied during qualification. The installed image and its Session A FAIL / B–D NOT_TESTED record remain unchanged. No device access or flashing occurs in this pass.

## Changes and software validation

The health CLI's network-check import used the name `check`, making the health function a shadowed local throughout `main`. Give the network function its own name. Quick/full health now return their actual JSON and exit status, including filesystem failures; the repair does not convert a failed check into success.

`/sys/power/wakeup_count` is a suspend handshake, not a nonblocking telemetry counter. Linux `kernel/power/main.c:wakeup_count_show` calls `pm_get_wakeup_count(..., true)`, which waits interruptibly while a wakeup source is active (`drivers/base/power/wakeup.c`). The physical receipt found precisely this wait with the charger source active. Query it using the existing bounded child-command runner with a 100 ms deadline and 64-byte output limit. A timeout returns null plus `command_timeout`, terminating and reaping the interruptible reader; a readable zero remains zero. This adds up to about 100 ms of observation time while a source stays active. The generic runner cannot guarantee reaping a process stuck in an unrelated uninterruptible kernel wait. No charger, wakeup, suspend, governor, voltage or hardware policy is changed.

Host validation: `python3 -m unittest discover -s tests -p 'test_platform*.py' -v` passes 67 tests. Four new regressions exercise quick/full failing health, network dispatch, a real blocked FIFO reader with termination/reaping, and zero/valid/invalid/missing counters. Receipts are under `out/y2linux-platform-v1-telemetry-01-build/`. All 5 packaged ARM/QEMU tests also pass using the actual image's Python, modules and BusyBox reader, including the full system-section CLI with a blocked counter. The initial extra smoke test expected an unfiltered CPU key in section-filtered JSON; that harness assertion was corrected and the initial failure is recorded. No production or image change was needed. Neither host nor emulated checks prove behavior on the charging Y2; the first physical check after a separately authorized install must repeat the mandatory baseline and inspect for leftover readers.

## Warning review

Evidence is the original private boot capture, boot ID `083d4abb-a447-4ac6-a063-e8898c150bca`, installed Linux source `d04b95aaff713edf943042d97a4c6134ca19fc24`, kernel `6.18.0-y2linux-platform-v1-candidate-01`. Review uses the pinned Linux 6.18 source and retained platform source. There are 28 priority 0–4 entries, including repeated rate-limit notices; this is not a count of distinct crashes. No retained Oops/panic/WARN stack or ext4/I/O error was found, and taint is zero.````````````````````````````````

| Message | Source-backed interpretation and remaining gate |
| --- | --- |
| dummy_timer is not functional (four) | kernel/time/tick-oneshot.c:tick_switch_to_oneshot rejects switching the current dummy clockevent to one-shot. The suffix is a pr_cont after pr_info, so its isolated priority is misleading. This is not proof of a dead timer, but effective clockevent/idle behavior and boot ordering remain to be checked (#28/#34). |
| Cache hierarchy not detected | drivers/base/cacheinfo.c fails cache/shared-CPU map setup. Incomplete cache description, not observed memory corruption. Cache topology and kernel description review remain (#28). |
| mt6323-led missing of_node | drivers/mfd/mfd-core.c cannot find the compatible child declared by mt6397-core.c. PMIC LED description mismatch; do not add a speculative hardware node solely to suppress this warning (#28/#30). |
| Memory protection not selected | init/main.c:mark_readonly reports absent strict kernel RWX configuration. This is a real hardening limitation; enabling it requires a separate kernel/memory validation boundary (#28/#32). |
| p8 extends beyond EOD | Retained stock partition-map clipping. Observed p5/p7 geometry, UUIDs, mounts and zero ext4 counters are consistent; no partition rewrite is justified. Durability/recovery remain untested (#33). |
| VCAMA/VRTC get_mode unsupported | drivers/regulator/mt6323-regulator.c:mt6323_ldo_get_mode logs when modeset_mask is zero. These rails expose that unsupported query; debugfs regulator-summary code can call it. This message alone does not prove a failed voltage transition. No rail configuration change; power qualification remains separate (#30). |
| Bluetooth extended features page 2 | kernel/platform/connectivity/hci.c:controller_quirks deliberately sets the existing E2 quirk after the own-device page-2 status 0x30 trace. net/bluetooth/hci_event.c warns when the controller advertises the inconsistent maximum. Preserve this compatibility workaround. Pairing/SBC/reconnect still need physical evidence (#31). |
| MSDC/OVL/printk suppression | Rate limiting means some diagnostic lines were omitted. It does not by itself identify a storage/display failure, and limits conclusions from the log (#28/#33). |
| Wi-Fi Start command | kernel/platform/connectivity/wifi/common/wlan_lib.c:1427 uses an unprefixed printk for the normal start command. Warning priority is not an association result. Full state/DHCP/DNS tests remain (#31). |

Early temperature ENODATA precedes later CPU/PMIC readings; absolute sensor accuracy and loaded thermal behavior remain unqualified. Orphan cleanup was followed by clean filesystem checks and zero error counters. These observations are retained without claiming power-loss durability or charging qualification.

The candidate keeps the same kernel and therefore does not promise to remove these messages. Source classification does not waive the owner's warning stop rule or promote any physical gate. Review the remaining timer/cache/hardening items before restarting later sessions; stop again on the owner's fault rules.

## Candidate handoff

Candidate: `out/y2linux-platform-v1-telemetry-01-candidate/`, status IMAGE_VALIDATED_PHYSICAL_PENDING, never installed during this pass.````````````````````

| Identity | Value |
| --- | --- |
| Corrected platform source | 814c2f3470566021c1a9c43037fd868de8b2df9c |
| Build ID | Y2LINUX-PLATFORM-V1-TELEMETRY-01 |
| Release / rootfs | 1.0.0-candidate.2 / 2025.02.18-platform-v1.2 |
| Retained kernel/base source | d04b95aaff713edf943042d97a4c6134ca19fc24 |
| Retained kernel | 6.18.0-y2linux-platform-v1-candidate-01 |
| Retained Reborn source | 155608393f6acfc6657f2f2e23cd07d0533479c6 |
| New root SHA256, 536870912 bytes | 4a8e520946ad1aaa00df46e9f302463341e4408bba063f43728b8cb8f68bb092 |
| Original UI fallback SHA256, 536870912 bytes | edcecfaae26b8102c071000b5d2e9e5f84626ad08e3ff5818b050174f301a044 |
| Required unchanged BOOTIMG SHA256, 6756352 bytes | f7b4a950a0504a411ad72db0aac9398f04dc1ccabd6a6a0a3a7fdab198ca2622 |

Fresh regular-file/debugfs overlay: exactly `cli.py`, `observe.py`, `/etc/y2linux/versions.json`, `/etc/y2linux/build-id` and `/usr/lib/os-release` changed. Whole-tree comparison covers 2,266 entries, including file hashes, symlink targets and modes. Image-inode comparison covers 2,267 entries including the root, preserving type, mode, flags, UID/GID/project, ACL pointer and link count. Unprivileged extraction reports expected chown failures; image inode checks establish ownership independently. No other extraction errors occurred.

All four Reborn ELF hashes remain exact. Label/UUID and 512 MiB image size pass; `e2fsck -fn` exits 0. The scatter bytes match the original root-only UI scatter, selecting only ANDROID and preserving all stock geometry. The original UI image is included as fallback and its hash rechecked. The unchanged local BOOTIMG requirement is hash-verified; no BOOTIMG or Y2DATA payload is included. Source bundles, reproducible overlay script, test receipts and checksums accompany the candidate. It is a root-only review package, not a signed OTA update.

Next physical boundary: separately authorized installation, verify this exact new identity, repeat the mandatory Session A baseline while charging, and check that status/health return without leftover readers. Health may correctly report real failures. The existing warning rule and unresolved review gates remain; Sessions B–D, endurance and E/F/G have not advanced. No core acceptance follows from this repair.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
