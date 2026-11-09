---
title: "Source delivery and distribution gate - Innioasis Updater"
description: "Source delivery and distribution gate <!-- knowledge-base-scope: maintained; baseline02-sync 2026-10-03 -- Current Baseline02 delivery — 2026-10-03 Sealed package: out/y2"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-release-y2-community-source-delivery.html"
---

# Source delivery and distribution gate - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Source delivery and distribution gate

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Source delivery and distribution gate

## Current Baseline02 delivery — 2026-10-03

Sealed package: `out/y2linux-baseline-02-candidate/` (local-only). Compiled pair: Linux `8584ccd85f052f351fe51650b2348c83ca894ed4` / Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`. Current exact inputs are recorded in `metadata/versions.json`, `manifest.json` and `sources/manifest.json`.````````````````

| Delivered material | Package-relative path |
| --- | --- |
| Exact project source snapshots | sources/Y2Linux.tar.gz, sources/Y2Reborn.tar.gz |
| Locked upstream sources | sources/linux-6.18.tar.xz, sources/buildroot-2025.02.18.tar.xz |
| Collector sources/manifests/licenses and warnings | sources/Buildroot-legal-info/ |
| Source pair and material hashes | sources/manifest.json |
| Actual selected package/build inventory | validation/release-inventory.json |
| Validation exit codes | validation/validation-exit-codes.json |

The current package supplies source tar archives, not the historical Git bundles. They retain source content; they do not carry Git history or prove possession of the original commit objects. Use the exact recorded commits in available local repositories, or identify unpacked source snapshots honestly when reconstructing. The fallback is the exact qualified UART01 BOOTIMG/Y2ROOT pair. Collector PASS retains explicit Bootlin/local-package/Buildroot limitations; legal review is incomplete and distribution remains owner-local. No byte-identical rebuild is claimed. See [Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md) and [current reconstruction](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fplatform-v1-reconstruction.md).

This pass distinguishes technical codec support, local engineering packaging and permission to publish. No public-distribution approval is inferred from successful compilation, an OSS library license, a disabled endpoint or a legal-info archive.

The preserving package records exact Linux/Reborn commits, kernel/Buildroot inputs, root/release versions, BOOTIMG/Y2ROOT hashes, fallback identities, firmware file expectations, platform API and delivered capabilities. The capability record lists selected build symbols and installed configuration separately from enabled, experimental, hardware-conditional and physically qualified state. A fresh build never manufactures a physical qualification record.

`tools/production/privacy.py` scans the actual ext4 image, through read-only host extraction, for protected/private filenames and credential/key material. `system_update.py` refuses packaging when the scan fails. The existing partition allowlist checks remain independent. The public-distribution check fails separately for unapproved firmware and compiled optional codecs, even when their endpoint is disabled. This engineering candidate remains owner-local.

For a later public release, retain and supply the exact corresponding sources, patches, configuration and build/install scripts, not just a commit URL or a binary SDK. Preserve copyright/license notices and include the selected packages' license texts. Record the chosen source-delivery method and review obligations for the actual GPL/LGPL versions and linking arrangements. Reborn's native media membrane uses shared FFmpeg libraries; actual ELF dependencies, configuration and source archives belong in its receipt. This is an engineering checklist, not a legal clearance determination. The [GNU licensing FAQ](https://www.gnu.org/licenses/gpl-faq.en.html) provides primary guidance; applicability and codec/patent/certification decisions remain for the owner/legal review.

Run Buildroot `legal-info` and preserve its README warnings, manifests, source archives and licenses. Its collection has limits: external toolchain and local packages may require additional source material. Include the pinned Buildroot archive itself, Linux source archive and overlays, both source snapshots/bundles, Cargo lock/vendor checksums, exact Bootlin toolchain source expectations, codec source ledger and local source SPDX/licenses. The [Buildroot manual](https://buildroot.org/downloads/manual/manual.html#legal-info) explicitly describes the collection and its limitations.

Reconstruction uses the pinned dependency archives and adjacent clean source checkouts described in `docs/build/platform-v1-reconstruction.md`. Current-source kernel/Buildroot/Reborn builds and dependency closure must pass before sealing. Source identity is reconstructable; byte-identical filesystem and complete clean rebuild equivalence have not been demonstrated. No such claim is made.

Unresolved public decisions remain: matched MediaTek firmware/defaults rights; AAC/aptX/aptX-HD/LDAC redistribution/certification questions from the existing codec ledger; complete external-toolchain source delivery; release signing/channel ownership. The owner-local candidate does not remove these features to hide the questions.

The integration collector completed with explicit warnings for the external Bootlin toolchain and local `y2-connectivity`/`y2-update` package license fields, and for Buildroot itself. The package separately supplies the pinned Buildroot archive and both exact project source archives; the collector warning README is retained. Complete external-toolchain delivery and final local-package notice review remain open public-release obligations.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
