---
title: "Platform 1.0 integrated software qualification - Innioasis Updater"
description: "Platform 1.0 integrated software qualification 2026-10-04. READY FOR PLATFORM V1 PHYSICAL QUALIFICATION . Compiled Linux 4c72466f2f27ddf9f0ca18ba8ddc4d89c52599d2 / Reborn"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-integration.html"
---

# Platform 1.0 integrated software qualification - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Platform 1.0 integrated software qualification

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Platform 1.0 integrated software qualification

2026-10-04. READY_FOR_PLATFORM_V1_PHYSICAL_QUALIFICATION.

Compiled Linux `4c72466f2f27ddf9f0ca18ba8ddc4d89c52599d2` / Reborn `dd73dcc3243045cd33e319dda2f76918ed37ea31`; kernel `6.18.0-y2linux-platform-v1-integration-01`; root `2025.02.18-platform-v1.23`. Candidate `/home/luca/Dokumente/Code/worktrees/platform-v1-integration/Y2Linux/out/y2linux-platform-v1-integration-candidate`. BOOTIMG SHA256 `d2dec1a517a596861adb69b4c9aaab51e68d5caf46712a99dbd8607e9d8fbb06`; Y2ROOT SHA256 `cd3c077fd6c4882c82b7c67c42266f5f0ddc04828ddc2af111434740153bd1dc`.

Fresh kernel/config/DT/modules/ABI/full ARM Buildroot/Reborn and exact FFmpeg9.0.2 PASS.466production cases:456PASS and10minimal-host native-dependency skips, each matched to an actual passing native case. Native groups43scratch/31storage-measurement-owner/15GIO-ALSA PASS.324workspace Rust tests/fmt/strict Clippy PASS. Cortex-A7 QEMU/installed ARM contracts/library,384ELFs/1411edges,106packages,449source/license records, final root/fallback/manifest/checksum/private-state/preserving scatter PASS. All owner source heads/refs/worktrees retained.

Private software receipts `/home/luca/Dokumente/Code/worktrees/platform-v1-integration/Y2Linux/out/platform-v1-integration-qualification`; final-seal.json, software-summary.json and validation-exit-codes.json distinguish initial corrected failures from final checks. Package contains exact source archives, collector limitations, capability/composition receipts and owner handoff. No byte reproducibility/legal clearance claimed.

Integrated physical/endurance NOT_RUN. Retain UART01 bounded C1/C2/C3 and Baseline02 RTC FAIL at their exact scope. Ordinary deep sleep and wider native AFE admission remain guarded; real desktop/AP/headset/codec/listening/controls/endurance/recovery campaign is pending. Firmware/codec permissions and corresponding-source/notices/collector review remain public distribution blockers.

See [master16-item handoff](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-MASTER.md%23final-16-item-master-handoff&anchor=final-16-item-master-handoff), [233-feature matrix](https://github.com/schulzcode/y2linux/blob/HEAD/docs/release/Y2-COMMUNITY-BETA-FEATURES.json) and [one A–J plan](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-PHYSICAL-QUALIFICATION.md). Only owner installs: Download Only, preserving scatter, BOOTIMG+ANDROID only; DATA/every other partition unselected. No main merge/push/master flash.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
