---
title: "CI firmware builds - Innioasis Updater"
description: "CI firmware builds GitHub Actions workflow build-firmware-releases.yml ../.github/workflows/build-firmware-releases.yml produces patched rom.zip releases on ryan-specter/"
language: "en"
source: "https://innioasis.app/post-install/ryan-specter-koensayr-auto-docs-supported-firmware-ci.html"
---

# CI firmware builds - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y1&software=koensayr-y1)

Post-install setup · Koensayr · Y1

# CI firmware builds

A Y1 custom Software maintained by the community.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y1&software=koensayr-y1)[Install guide](../guide.html?model=Y1&software=koensayr-y1)

# CI firmware builds

GitHub Actions workflow [`build-firmware-releases.yml`](https://github.com/ryan-specter/koensayr-auto/blob/HEAD/.github/workflows/build-firmware-releases.yml) produces patched `rom.zip` releases on [ryan-specter/koensayr-auto](https://innioasis.app/firmware.html?model=Y1&software=koensayr-y1).

## Upstream sources (allowlist)

CI only builds these upstream tags (see [`tools/ci/discover-inputs.sh`](https://github.com/ryan-specter/koensayr-auto/blob/HEAD/tools/ci/discover-inputs.sh)):[](https://innioasis.app/firmware.html?model=Y1&software=original-y1)``

| Repository | Upstream tags | Asset |
| --- | --- | --- |
| y1-community/y1-stock-rom | 3.0.2, Latest-3.0.7 | rom.zip |

Koensayr release tags:`{koensayr-version}-koensayr-{stock-firmware}` (e.g. `2.4.0-koensayr-3.0.7`) so Innioasis Updater can read the stock OS version from the suffix. Stock 3.0.7 is built from upstream tag `Latest-3.0.7`. User-facing copy comes from [`.github/workflows/workflow.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2F.github%2Fworkflows%2Fworkflow.md); commits by SeanathanVT append a Detailed notes: section with the latest commit message.

Not built by CI: other stock tags (`2.8.2`, `ADB-2.1.9`, `type-b-1.7.6`, …), `rom_type_b.zip`, `rom_240p.zip`, `update.zip`, voice packs, and other assets.

Rockbox-Y1 `rom.zip` is out of scope: the image has no Innioasis `com.innioasis.y1` music APK, so the stock patch pipeline does not apply. Build Rockbox releases manually if needed.

To add another stock tag, extend `Y1_UPSTREAM_TAGS` in `discover-inputs.sh`.

## Output naming
  - GitHub release tag / title:`{koensayr-version}-koensayr-{firmware-version}` (e.g. `2.4.0-koensayr-3.0.2`, `2.4.0-koensayr-3.0.7`)
  - Internal firmware slug (`--firmware-slug`): `@` replaced with `-` (e.g. `y1-stock-rom-3.0.2`) for `system-*-devel.img` naming

## Patch set

Every green CI build verifies upstream `rom.zip` SHA256 and MD5 against [`KNOWN_FIRMWARES`](https://github.com/ryan-specter/koensayr-auto/blob/HEAD/apply.bash), then runs `./apply.bash --all --no-flash` (strict manifest match — no `--accept-any-firmware`):
  - Music-player UX (`--music-apk`)
  - Bluetooth pairing (`--bluetooth`)
  - ADB + bloat removal (`--adb`, `--remove-apps`)
  - Root (`--root`)
  - AVRCP 1.3 + Y1Bridge (`--avrcp`)

Diagnostic tooling under `tools/` is not embedded in the ROM.

## Expectations by upstream[``](https://github.com/ryan-specter/koensayr-auto/blob/HEAD/apply.bash)``

| Input | CI expectation |
| --- | --- |
| y1-stock-rom 3.0.2 / 3.0.7 | Supported; matches KNOWN_FIRMWARES (3.0.7 accepts both Innioasis and y1-community system.img layouts) |

Failed matrix jobs do not block other releases (`fail-fast: false`).

## Idempotency
  - Push to `main`: always rebuilds and republishes (`--force`), so patched `com.innioasis.y1` APKs and other `--all` changes land in the latest `rom.zip` releases. Each publish deletes the prior GitHub release tag and recreates it (no leftover assets such as older `rom-koensayr.zip` names).
  - Weekly schedule: skips a matrix entry only when `build-manifest.json` on the existing release matches both the upstream `rom.zip` SHA256 and the current koensayr git revision (`koensayr_git_sha`).
  - `workflow_dispatch`: set force to rebuild regardless.

## Scripts[``](https://github.com/ryan-specter/koensayr-auto/blob/HEAD/tools/ci/discover-inputs.sh)``[``](https://github.com/ryan-specter/koensayr-auto/blob/HEAD/tools/ci/build-one.sh)``[``](https://github.com/ryan-specter/koensayr-auto/blob/HEAD/tools/ci/firmware-manifest.sh)````[``](https://github.com/ryan-specter/koensayr-auto/blob/HEAD/tools/ci/patch-revision.sh)``[``](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2F.github%2Fworkflows%2Fworkflow.md)[``](https://github.com/ryan-specter/koensayr-auto/blob/HEAD/tools/ci/extract-rom.sh)``[``](https://github.com/ryan-specter/koensayr-auto/blob/HEAD/tools/ci/repack-rom.sh)````

| Script | Role |
| --- | --- |
| tools/ci/discover-inputs.sh | Emit JSON matrix for allowlisted upstream rom.zip assets |
| tools/ci/build-one.sh | Download → MD5/SHA256 gate → patch → repack → gh release |
| tools/ci/firmware-manifest.sh | Read KNOWN_FIRMWARES rows from apply.bash |
| tools/ci/patch-revision.sh | Current git SHA recorded in build-manifest.json |
| .github/workflows/workflow.md | User-facing intro prepended to each GitHub release (edit for new features) |
| tools/ci/extract-rom.sh | Unzip upstream ROM; record sparse system.img |
| tools/ci/repack-rom.sh | Replace system.img and zip patched rom.zip |

These are Koensayr's own instructions, shown here word for word.

Published by the [ryan-specter/koensayr-auto](https://innioasis.app/firmware.html?model=Y1&software=koensayr-y1) project [[1]](https://innioasis.app/firmware_info.html?repo=ryan-specter%2Fkoensayr-auto&software=koensayr-y1)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aryan-specter)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
