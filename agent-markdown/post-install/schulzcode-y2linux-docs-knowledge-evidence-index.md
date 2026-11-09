---
title: "Evidence provenance and review - Innioasis Updater"
description: "Evidence provenance and review <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-evidence-index.html"
---

# Evidence provenance and review - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Evidence provenance and review

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Evidence provenance and review > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Date: 2026-09-08. Research task: [Y2E-101](https://github.com/SchulzCode/Y2Linux/issues/1). Capture ID: `20260908-provenance`. Status: bounded historical provenance audit complete. The later [Y2E-125 recovery update](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frecovery.md) accepts owner-observed successful same-device flashing and identifies the FM fallback/tool. Earlier unproven-recovery statements below describe the original evidence boundary.

Reference root: `/home/luca/Dokumente/Code/Y2Player`, Git revision `870f2b33e49129990bc0a98eeb34d58ed42542b6`. The source tree was clean when inspected. Ignored binaries/captures are not authenticated by that revision. All 24 top-level regular files in `OriginalFirmware/` were hashed without modification; see [artifact-manifest.tsv](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/artifact-manifest.tsv). Vendor origin, package download provenance and current-device compatibility remain UNKNOWN. A directory called OriginalFirmware is not proof of authenticity or a per-device backup.

## Verified historical captures

The command `sha256sum -c checksums.txt` was run from each snapshot directory. Both commands returned 0: 93 of 93 entries matched in each, with no missing manifest members. ZIP hashes also match the historical hardware report. Each capture manifest has 89 observation rows: 70 COLLECTED, 12 UNAVAILABLE, 5 DENIED and 2 EMPTY. Checksums establish retained bytes, not that every command successfully observed hardware.``````

| Snapshot | Manifest validation | Extra unmanifested member | Decision |
| --- | --- | --- | --- |
| out/hardware-snapshots/2026-07-29_004316/ | 93/93 match | One patched primary audio library under pulled/ | Reuse only authenticated manifest members as the original snapshot. The added patched binary is separate evidence. |
| out/hardware-snapshots/2026-07-29_004935/ | 93/93 match | One supplemental personal source-media file | Media is not part of the original manifest and is excluded from public evidence. |

The raw verification logs, complete extra-file lists and research helper remain private in `evidence-private/20260908-provenance/`. No source media or firmware is committed.

The later `out/afe-runtime/2026-07-30_135519/manifest-files.csv` contains 116 hashed records. All 116 referenced files were independently rehashed and matched; detailed comparison remains private. This validates retained capture bytes, not the electrical interpretations in the report.

Direct inspection confirms that old ADB host exit 0 accompanied `klogctl: Operation not permitted` for dmesg and permission-denied cmdline. `uname` was unavailable; config.gz and exported DT paths were unavailable; an empty modules list does not prove that the kernel lacks built-in drivers. Preserve statuses independently of exit codes.

## Generated artifacts: restricted reuse

`out/boot-adb/checksums.txt`: exit 1. `boot.img`, `boot-stock.img`, `ramdisk-adb.img` and `verification-report.txt` matched, but the listed standalone `adbd` file was absent. The current manifest identifies build `20260813T163015Z-2697c3590c89-dirty`, output boot SHA-256 `9abda0890c37558820602b1cf4c6bad74852a9a01812787e1b54b626c616797e`, and a CS43131 idle-resume kernel patch. This output is a modified kernel/ramdisk, not merely the stock kernel with ADB enabled. The manifest itself is not among its checksummed members. Do not infer current-device installation or certify complete build reproducibility from this directory.

`out/firmware/checksums.txt`: exit 1. `system.img`, `build-manifest.txt` and `verification-report.txt` matched; `Y2Player.apk` did not. The directory is not a coherent verified distribution as it stands. Do not repair/rebuild/replace files in this research task. A matching system image remains separately identifiable; it is not a stock image or proof of successful restoration.

The decompressed kernel and symbolized ELF match their published hashes (`5f284fade5e9ab4f...` and `b2b5570d2db50cc...`; full values in the manifest). They may support offline analysis, subject to validating derivation from the exact stock kernel. `reverse/system/lib/libaudio.primary.default.so` was absent at the initially referenced path. The alternate authenticated snapshot member `out/hardware-snapshots/2026-07-29_004935/pulled/system__lib__libaudio.primary.default.so` is available and hashes to `5c5162f6a68f7db57febd050ee88cc886779dcce5948937149d6cd211eb0e6de`, matching the historical stock HAL. The unmanifested patched copy in the earlier snapshot hashes to `c155e239c8d13bc83bc4016ebdcbd1724114d728df86beb4d42c112150ffe216`, matching the historical patch report; it remains a separate derivative, not an original capture member.

## Report precedence and unresolved claims````````````

| Source | Reusable scope | Qualification |
| --- | --- | --- |
| docs/Y2_HARDWARE_AND_DAC_ANALYSIS.md | Exact archived stock/capture hashes, DAC binding and initial analysis | Later second-I2S analysis supersedes parts of its route/rate recommendations. |
| Audio phase-2, phase-3 and phase-4 reports | Evolution from static call graph to captured active route | Preserve differences and measured versus inferred distinctions; phase-4 electrical/analog uncertainties remain open. |
| docs/BLUETOOTH_STACK_INVESTIGATION.md | Vendor artifact/service topology | Its early no-runtime-evidence statement is time-scoped, not a repository-wide current conclusion. |
| docs/FM_RADIO_FEASIBILITY.md | Reported runtime chip ID and routing experiments | Successful tune/open does not establish useful reception or physical RF population on every revision. |
| RELEASE_2.5.md | Current search/FM/input behavior and revision claims | Behavioral reference; external hardware-revision claims still need source provenance. |
| docs/ADB_BOOT_IMAGE.md | Earlier secure non-root ADB design | Current generated boot manifest additionally records a kernel patch. Referenced PowerShell collector is absent from the current checkout. |
| README and docs/Y2_INPUT_MAP.md | Historical UI/key mapping | Older no-search/no-acceleration descriptions are superseded by release/source behavior. Android keycodes are not Linux scan codes. |

## Review decision

Y2E-101 is complete as a catalog and integrity assessment, including failed/generated inputs. Failed package checks are quarantined from recovery readiness; they do not prevent independent, passive observation of an already authorized device. Y2E-105 is therefore permitted next, without assuming that the connected device is stock or that any generated image is installed. Raw partition acquisition, firmware execution and restoration remain blocked. No implementation issue is ready.

## Y2E-140 evidence follow-up

Private `20260908-observation/` retains fresh read-only stock console/sysfs/resource evidence and previous kernel RAM-console tail, FM UART remapping, pinned vendor sources and externally sourced board-photo evidence. [Interpretation and limits](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fobservation-path.md); per-file hashes are appended to [capture-index.tsv](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/capture-index.tsv). Definitive remote statuses use Android echo; preliminary printf attempts are explicitly superseded. No UART wire capture or physical pin/voltage proof exists yet.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
