---
title: "Y2Linux platform, build and release audit - Innioasis Updater"
description: "Y2Linux platform, build and release audit <!-- knowledge-base-scope: historical-audit/review -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-audit-current-system-03_y2linux_audit.html"
---

# Y2Linux platform, build and release audit - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Y2Linux platform, build and release audit

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Y2Linux platform, build and release audit > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

## Repository quality and authority

VERIFIED / HIGH: production responsibilities are identifiable: kernel inputs/overlays, DT/config, Buildroot external packages, production initramfs, packaging, and hardware-evidence documentation. This is a better foundation than an opaque prebuilt vendor image. The patch manifest records both base and resulting hashes; the overlay mechanism can reject an unexpected source version. Keep it.

WEAK / HIGH (F14/F30): current-state documentation and manifests lag behind the product. The [README](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) still describes pre-Reborn boundaries. [package.py](https://github.com/SchulzCode/Y2Linux/blob/main/tools/production/package.py) emits `application.name=Y2PlayerNative`, `implemented=false` and `/usr/bin/y2player`, while [reborn.mk](https://github.com/SchulzCode/Y2Linux/blob/main/buildroot/package/reborn/reborn.mk) installs and starts `/usr/bin/reborn`. Worse, [validate.py](https://github.com/SchulzCode/Y2Linux/blob/main/tools/production/validate.py), `validate_manifest`, requires `not application.implemented`. Passing validation therefore preserves a false capability statement. This is an interface-contract defect, not cosmetic documentation debt.

Keep historical first-boot configurations, stock fixtures and recovery records clearly labeled. Do not purge them during a cleanup. The imported Wi-Fi core is live vendor-derived implementation, not dead code. Committed deterministic assets, vendored Rust and small media fixtures have a reproducibility purpose; removing them based on file count would be counterproductive. Only the third-party fixture distribution issue needs immediate release attention.

## Build and reproducibility: F13

CURRENT — IMPLEMENTED, with WEAK clean-machine closure / HIGH.
  - [Buildroot lock](https://github.com/SchulzCode/Y2Linux/blob/main/buildroot/inputs.lock.json): 2025.02.17, archive checksum, Bootlin ARM hard-float toolchain and source-date epoch.
  - [Kernel/build input lock](https://github.com/SchulzCode/Y2Linux/blob/main/tools/build/inputs.lock.json): Linux 6.18 source identity, constrained build environment inputs. [Production configuration](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/config/production.config) is separate from first-boot configuration.
  - [Production build](https://github.com/SchulzCode/Y2Linux/blob/main/tools/production/build.py): rejects dirty source, records both repository HEADs, restricts output to `out/`, explicitly provisions owner firmware, reconstructs BOOTIMG, and validates artifacts. Local packages are dircleaned before a userspace rebuild, addressing Buildroot stamp staleness.
  - [Cross build](https://github.com/SchulzCode/Y2Reborn/blob/main/tools/build/cross.sh): Buildroot SDK owns native dependencies; Cargo uses locked/vendored source and the pinned Rust toolchain. This avoids accidentally linking host ALSA/FFmpeg into the ARM binary.
  - Ext4 image creation specifies labels/UUIDs, deterministic time/hash-seed inputs and disabled lazy initialization. Production defconfig enables reproducibility. Packaging hashes actual payloads and enforces image-size boundaries.

The remaining gaps are substantive:
  - `ffmpeg9.py:apply` requires `.cache/buildroot-dl/ffmpeg/ffmpeg-9.0.1.tar.xz` to exist before Buildroot can fetch the package. It verifies the hash, but the production path does not fetch this new archive. A clean checkout/cache is insufficient without an additional provisioning step.
  - Reborn is the sibling path `../Y2Reborn` and its current HEAD, not an immutable paired release input. Recording that HEAD is good, but it is not a command that obtains the required pair. Rust/Cargo is expected from the owner's toolchain installation (`$(HOME)/.cargo/bin/cargo` by default).
  - Kernel execution has a controlled environment; Buildroot/native host steps also depend on the host's available tools. Host prerequisites and a complete cache acquisition/offline recipe need one tested contract. Offline Cargo is not offline whole-product reproducibility.
  - FFmpeg is upgraded by text/regex editing Buildroot's 6.1.5 package and renaming its old patch files. That is understandable for an experiment but brittle maintenance: upstream package changes can stop matching silently. A maintained versioned package override is the eventual target, not a second media build system.
  - Reuse/resume paths intentionally keep older userspace. `versions.json` can name current Reborn while `userspace-source.json` records retained root/data. A source HEAD must not be mistaken for the embedded application identity. Validate the embedded build ID/dependency manifest per payload, including the lazy `.so`, not only the image checksum.
  - The latest retained `...ui-polish-02-build/buildroot/target` is not a complete rebuilt production rootfs. A missing `usr/bin/reborn` there is a reuse-workspace fact, not proof that the packaged image lacks Reborn. Read-only image inspection confirmed `/usr/lib/reborn/libreborn_media.so` and the qualification JSON. The complete older SDK tree passed `verify-ffmpeg.py`.

TARGET: one documented, paired-source acquisition/build/package procedure with explicit owner-only inputs and verifiable embedded component identity. GAP: no clean-machine/repeated-image comparison was demonstrated here. Reproducible intent is strong; reproducibility of the release images from a clean machine remains UNKNOWN. Do not advertise byte-identical reproducibility until measured. No build was performed in this documentation-only audit.

## Boot, recovery, flashing: G01/G02/F31

The [production init](https://github.com/SchulzCode/Y2Linux/blob/main/initramfs/production/init) and [storage policy](https://github.com/SchulzCode/Y2Linux/blob/main/initramfs/production/storage.sh) are among the strongest parts. Controller/geometry/filesystem identity precedes writes; read-only preflight checks markers and compatibility; unacceptable fsck or mounting results lead to rescue. The code does not format an unknown device or silently select an SD root. BOOTIMG owns its matching modules in RAM, avoiding a kernel/root-module mismatch during preserving updates. Preserve these contracts.

[Layout](https://github.com/SchulzCode/Y2Linux/blob/main/tools/production/layout.py), [package](https://github.com/SchulzCode/Y2Linux/blob/main/tools/production/package.py), [validation](https://github.com/SchulzCode/Y2Linux/blob/main/tools/production/validate.py), and readback profiles carefully distinguish absolute, logical and scatter address spaces. The native eMMC offset correction is Y2-specific; generic partition tooling assumptions are unsafe here. Inspecting the logic does not replace the retained physical addressing evidence.

The normal update target set is BOOTIMG + ANDROID. USRDATA is initialization-only. Preloader, LK, MBR/EBRs, NVRAM, PROTECT and calibration are outside the permitted payload set. The kernel's protected-storage policy is a second barrier. No new accidental protected-partition write path was demonstrated in the inspected production flow.

Remaining public-user risk: the first-install scatter selects USRDATA; the preserve-data scatter does not. A user choosing the wrong otherwise valid profile loses user data. Checksums do not prevent that choice. The package is still owner-personalized, and manual SP Flash Tool interaction cannot be made safe merely by a passed Python validator. Public instructions must distinguish initial install, preserving update, failed update and deliberate factory reset; test them from an independent operator's perspective. No image contains a universal owner private key; do not distribute a personalized data image as a universal product default.

There is no atomic A/B update or automatic rollback. That is not necessarily an alpha blocker if updates are explicitly manual and rescue/restoration is proven. Signed OTA is not a prerequisite for an offline owner alpha; it becomes relevant only if a remotely delivered update workflow is offered. Treat the existing manually packaged system-update path as a real limited capability, not as “no recovery.”

## Kernel/DT: G03/F29

The reviewed drivers use Linux facilities rather than userspace MMIO: devm resources, regmap, DMA APIs, ASoC, clocks, genpd, standard input and network interfaces. For example [AFE](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/audio/mt6582-afe.c) constrains DMA to 32 bits, uses managed buffers, disables/synchronizes IRQs before clock gating, and pairs runtime-PM acquisition/release. The [MFG clock](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/mfg-clock.c) refuses accesses to a powered-off domain; [SPM](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/spm.c) latches ambiguous power failures rather than pretending recovery succeeded. Those are good ownership choices.

Risks concentrate in board-specific evidence, not abstraction count:
  - The fixed GPIO DAC rails have nominal DT voltages with acknowledged measurement limits. Do not extrapolate to a new rail or voltage policy.
  - PWRAP, boot handoff, display timing, SPM PCM and connectivity protocols retain reverse-engineered/vendor assumptions. Timeouts/readback improve containment, not proof that all modes are safe.
  - The memory map intentionally excludes the inherited loader/radio regions. No evidence supports reclaiming them merely to improve a memory number.
  - CPU/MFG policies are split into named owners, but PM ordering crosses them, PMIC, audio, display, eMMC and CONSYS. Only integrated same-boot suspend/resume can prove that composition.
  - Ext4 patches 0032–0034 are a documented upstream 32-bit inode-state backport, not an application-specific filesystem hack. Keep their provenance; do not remove them as unexplained local churn.
  - `/project` includes and overlay compilation are intentional controlled-build conventions, not portable standalone kernel sources. Document that contract before proposing upstreamability work.

No blanket resource-leak-free or suspend-safe claim is justified by this inspection. High-resolution AFE support is specifically absent; see [audio](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fcurrent-system%2F05_AUDIO_AUDIT.md). Current power and deep-suspend limitations are in [power audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fcurrent-system%2F07_POWER_PLATFORM_AUDIT.md).

## Storage and runtime configuration: F26

Internal ext4 data lives separately from the replaceable root image. Root is normally writable; `/run` and runtime state isolate many transient writes, while application/system logs intentionally persist in bounded form. Root/data boot fsck improves recoverability but is not proof of arbitrary power-cut safety.

[y2-media](https://github.com/SchulzCode/Y2Linux/blob/main/buildroot/board/y2/production-overlay/usr/sbin/y2-media) accepts a unique supported SD filesystem and mounts with nosuid/nodev/noexec. Supported paths are ext4/vfat, not exFAT. This is a real limitation for commonly formatted large cards; document it even if adding exFAT is deferred. The application delegates mount policy to this helper rather than constructing arbitrary mount commands.

Reborn detects insertion/removal by polling, marks sources offline and stops invalid generations. However, mount errors are often discarded, unmount can encounter open files, and there is no electrical power-loss/hot-removal qualification here. Full data volume, transient media I/O failure and a corrupt library must be tested together—not merely `is_dir` and mount-string fixtures. See F05/F07/F26.

## Realistic security and privacy: G10/F32

Good current defaults: no normal password login; [Dropbear](https://github.com/SchulzCode/Y2Linux/blob/main/buildroot/board/y2/overlay/etc/default/dropbear) binds USB Ethernet `10.42.0.1:22`, disables password and forwarding features; startup requires owner authorization. SSH keys, Wi-Fi configuration and bonds have private persistent directories. Reborn's control socket is local, parent 0700/socket 0600, bounded, and accepts enumerated commands rather than arbitrary shell execution. Firmware identity checks and root-only calibration handling are strong.

This is nevertheless a root-run media player, not a sandboxed consumer OS. Malformed user media reaches native FFmpeg and graphics/ALSA code with root privileges. The file-only FFmpeg protocol whitelist, allocation/probe limits, no general network decoder input, and no open Wi-Fi SSH listener reduce attack surface. They do not replace maintenance of native dependencies. Root isolation is a later scoped hardening decision; first fix concrete lifetime/error defects.

Diagnostic sanitizer tests cover secrets and protected calibration material, but free-form strings and media names cannot be assumed perfectly anonymous. [y2-collect](https://github.com/SchulzCode/Y2Linux/blob/main/buildroot/board/y2/overlay/usr/sbin/y2-collect) is broader raw platform collection than Reborn's sanitized bundle. Maintain separate private raw captures and public sanitized receipts. Do not publish raw bundles automatically. No credential exposure was observed or reproduced during this audit.

## Redistribution and licensing: F15

MISSING public compliance closure / HIGH; legal permission UNKNOWN. This is a technical inventory, not jurisdiction-specific legal advice. [package.py](https://github.com/SchulzCode/Y2Linux/blob/main/tools/production/package.py) explicitly says the package is owner-local and full third-party source/license collection must accompany a later public release. The production build records firmware redistribution permission as false/unestablished.``````

| Material | Inspected technical position | Public-release requirement/gap |
| --- | --- | --- |
| Linux and local kernel/donor code | GPL notices/SPDX and patch provenance retained | Supply corresponding modified source/build material through a compliant distribution mechanism. |
| Buildroot | Build system plus many independently licensed packages | Export/review legal-info and notices for the actual image; Buildroot's license is not the license of the rootfs. |
| FFmpeg 9.0.1 | Shared libraries; generated config has GPL=0, NONFREE=0, VERSION3=0 | LGPL source/notices/build details and user replacement rights need release packaging, not only a dependency name. |
| Mesa/libdrm | Predominantly permissive upstream notices, with per-file exceptions/third-party material | Collect actual built-source notices; do not replace them with Reborn's MIT notice. |
| BlueZ / BlueALSA / ALSA / SBC library | Inspected BlueZ COPYING is GPLv2; BlueALSA 4.3.1 LICENSE is MIT; other components have their own LGPL/GPL/per-file terms | Collect exact package source/notice obligations; optional-codec rights cannot be inferred from BlueALSA's MIT license. |
| Rust crates | Vendored/locked, metadata inventory exists | Preserve required notices/licenses; dependencies.json alone is not a complete notice archive. |
| DejaVu font bitmaps | Font license files are in Reborn source | reborn.mk installs only the top-level MIT LICENSE and dependency JSON, not those font notices. Read-only rootfs listing confirms that omission in /usr/share/reborn. |
| Icons/UI reference pack | Local SVG/bitmap assets exist | Establish source/permission record rather than assuming a reference pack is covered by the application's MIT declaration. |
| APE/WavPack fixtures | README identifies external Wavecor specimens, explicitly outside generated-fixture CC0 | Package currently copies them into the rootfs. Obtain redistribution permission or substitute/remove from public payload after owner decision. Public accessibility is not permission. |
| CONSYS/modem firmware | Exact owner-supplied blob checksums | Extraction/identity does not grant redistribution permission. Owner-provisioning versus lawful public bundle is a release decision. Never bundle device calibration. |

Upstream guidance supports the distinction between configuration-dependent FFmpeg licensing and the library merely being present: [FFmpeg legal guidance](https://ffmpeg.org/legal.html). Buildroot documents that its legal-info collection still needs review and may be incomplete: [Buildroot legal notice](https://buildroot.org/downloads/manual/manual.html#_legal_notice_and_licensing). Kernel licensing/source requirements are described by [kernel licensing rules](https://www.kernel.org/doc/html/latest/process/license-rules.html). Patent/codec distribution rights depend on the actual distribution and jurisdiction; they were not resolved by this audit. Do not describe AAC/aptX/LDAC as shipped merely to create speculative legal problems—they are not enabled Bluetooth codecs here.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
