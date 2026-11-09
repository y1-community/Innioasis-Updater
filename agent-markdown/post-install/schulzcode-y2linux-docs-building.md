---
title: "Building Y2Linux from source - Innioasis Updater"
description: "Building Y2Linux from source This builds the kernel, the Buildroot root filesystem with the Y2Reborn player, and a first-install package that you flash with SP Flash Tool"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-building.html"
---

# Building Y2Linux from source - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Building Y2Linux from source

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Building Y2Linux from source

This builds the kernel, the Buildroot root filesystem with the Y2Reborn player, and a first-install package that you flash with SP Flash Tool ([INSTALL.md](https://innioasis.app/guides/reborn-y2linux-y2.html)). These are the same commands that produced 1.0 Beta 7.10 (Baseline 73) on the maintainer's machine (an Arch-based Linux, x86_64). They have not yet been run on a second machine. If a step fails, please open an issue with the log.

## 1. Host requirements
  - Linux x86_64 with about 15 GB free disk (download cache about 4 GB, build about 7 GB,

compiler cache up to 5 GB).
  - Python 3.12 or newer.
  - bubblewrap (`bwrap`) and unprivileged user namespaces. The kernel build runs in a

locked, network-isolated Alpine userspace that the tools download and hash-check. You don't need Docker.
  - The standard Buildroot host packages: `gcc`, `g++`, `make`, `binutils`, `patch`,

`perl`, `rsync`, `cpio`, `unzip`, `bzip2`, `gzip`, `tar`, `file`, `bc`, `wget`, `which`, `diffutils`, `findutils`, `gawk`, `git`. The root filesystem is built on the host (not inside bubblewrap), so these must be installed.
  - Rust via rustup, with toolchain 1.99.0 and the ARM target. The Buildroot recipe

calls `~/.cargo/bin/cargo`. Override that with `REBORN_CARGO=/path/to/cargo` if needed.
` rustup toolchain install 1.99.0 --profile minimal \ --target armv7-unknown-linux-gnueabihf -c rustfmt -c clippy`
  - `e2fsprogs` (`debugfs`, `e2fsck`), `util-linux` (`blkid`) and `simg2img`

(Arch: `android-tools`; Debian/Ubuntu: `android-sdk-libsparse-utils`) for the firmware and packaging steps.
  - An ed25519 SSH key for root access over USB. The packaging step writes its

public half into the data partition.
` ssh-keygen -t ed25519 -f ~/.ssh/y2linux_ed25519`

## 2. Get the sources

Y2Linux and Y2Reborn must sit next to each other in the same parent folder. Buildroot builds Reborn from `../Y2Reborn`.`mkdir y2 && cd y2 git clone https://github.com/SchulzCode/Y2Linux.git git clone https://github.com/SchulzCode/Y2Reborn.git git -C Y2Linux checkout baseline-75 git -C Y2Reborn checkout baseline-75 cd Y2Linux`

Use the tag of the release you want to rebuild (the newest is in the readme's table and on the [releases page](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)); both repositories carry the same tag.

Keep both trees clean (no uncommitted changes). The build and packaging tools refuse dirty trees and record both commit IDs in the image. If you change anything, commit it first.

## 3. The stock Innioasis firmware folder

Keep the Innioasis firmware package for the Y2, v3.2.0 FM (2026-08-13), unpacked: the folder you would load into SP Flash Tool to reflash stock. Packaging (step 6) checks it by SHA-256 and takes the partition layout from its scatter file. It is also your only way back to stock.````````````````

| File in the stock folder | SHA-256 |
| --- | --- |
| boot.img | 5ef1bdf28481ee0bf5f3528c1ddd91cf3f4d2d5f39e4d0ea049a8137a30f6af6 |
| system.img | 5a7a92f3a95374f31abe8b3ddbd68c5c2ce5677547db3d1cbc21653d24c76989 |
| userdata.img | 552e325ecf2faffeb9351022147bbfda3b7cebe25df491b2d732e85c5c68f27c |
| MT6582_Android_scatter.txt | e5fe03e9f3219cc9b5ead27892f2ddb722acc16adce3306d27feb87893cd977e |

Radio firmware (since Baseline 49). The Wi-Fi/Bluetooth chip needs proprietary MediaTek firmware that may not be redistributed. It is not in this repository, the build never downloads it, and no image contains it. Each player gets it once from its owner's `system.img` (the Firmware drive, or `y2-platform firmware install /path/to/system.img`), checked file by file against the reviewed SHA-256 values ([inventory](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/evidence/m5-firmware-inventory.json)); a player that ran an older image keeps its copy across the update. See [INSTALL](https://innioasis.app/guides/reborn-y2linux-y2.html). `--owner-firmware` and `tools/connectivity/provision.py` are no longer needed for a build.

## 4. Build`python3 tools/production/build.py --output out/y2-build # your own image (all codecs) python3 tools/production/build.py --output out/y2-build --public # as the public releases`

`--public` leaves out the codecs the public images may not carry (aptX/aptX HD); SBC, AAC (fdk-aac-free) and LDAC stay. Every build installs into an empty target directory.

On the first run this:
  - Downloads and hash-checks the locked inputs (`tools/build/inputs.lock.json`:

Linux 6.18.56 and the Alpine 3.24 build userspace with LLVM 22; `buildroot/inputs.lock.json`: Buildroot 2026.08) into `.cache/`. Buildroot uses the Bootlin GCC 15.3 cross toolchain.
  - Builds the kernel inside bubblewrap with the overlays in `kernel/patches/`.
  - Builds the Buildroot toolchain and root filesystem on the host, including FFmpeg

9.0.2 and Y2Reborn (offline, from its vendored crates).
  - Builds the initramfs and device tree, and validates the artifacts.

A first build takes about 8–10 minutes on a 16-thread machine (kernel ≈2 min, Buildroot ≈6 min with the Bootlin cross toolchain). Buildroot builds packages in parallel (per-package directories) and keeps compiler output in `.cache/ccache`, so a later clean build is faster. Resume a stage of an existing build with `--resume kernel|buildroot|artifacts`: about 1 minute, because only packages whose inputs changed are rebuilt (Reborn, fdk-aac and bluez-alsa are tracked by their inputs; this project's small helpers always rebuild). Logs for each stage are in `out/y2-build/*.log`. Don't copy or move a build folder: it contains absolute paths, symlinks and library search paths of its own location; resume it in place or build afresh. The result is `out/y2-build/BOOTIMG.img` (kernel and rescue initramfs) and `out/y2-build/buildroot/images/` (root filesystem).

### Last.fm app key (optional)

Last.fm needs an API account (last.fm/api/account/create). Put its key and shared secret, never in the source, into `~/.local/share/y2linux/lastfm-api.json` as `{"api_key": "…", "shared_secret": "…"}` with `chmod 600`. The build copies it into the image as `/usr/share/reborn/lastfm-api.json` (mode 0600); without it Settings → Last.fm says the build has no key and only the `.scrobbler.log` file works.

## 5. Test (optional, recommended)`python3 tools/build/run.py --output out/y2-build -- sh /project/tools/production/tests.sh`

This runs the platform test suite inside the locked environment (1.0 Beta 7.10: 766 cases, about 30 s). For a quick check while working, run the same test modules on the host in about 45 s (needs `clang`, `pyelftools` and `qemu-arm`; Arch: `python-pyelftools qemu-user`):`tools/development/host-tests.sh`

`python3 -m unittest discover` also collects retained historical tests that are not part of the release gate ([tests/README](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Ftests%2FREADME.md)).

Y2Reborn's own tests run on the host (see the Y2Reborn README):`cd ../Y2Reborn && cargo test --workspace --locked --offline`

## 6. Make the first-install package`STOCK=/path/to/y2_v3.2.0_FM-20260813 python3 tools/production/package.py \ --build out/y2-build \ --output out/y2-first-install \ --stock "$STOCK" \ --public-key ~/.ssh/y2linux_ed25519.pub python3 tools/production/validate.py out/y2-first-install --build out/y2-build`

`validate.py` should end with `PASS offline Production Storage v1`. `$STOCK` is the folder from step 3. A public package for a release (as on the GitHub releases page) uses `--public` instead of `--public-key`: its data image has no SSH key, its manifest no local paths, and its `MT6582_Android_scatter.txt` also writes the Y2 recovery image (`RECOVERY.img`), so one SP Flash Tool pass sets up everything ([why](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FRECOVERY-AND-UPDATES.md)). The package contains:````````````````````

| File | Purpose |
| --- | --- |
| BOOTIMG.img | Kernel and rescue initramfs (BOOTIMG partition) |
| Y2ROOT.img | Root filesystem (stock ANDROID partition) |
| Y2DATA.img | Empty data partition with your SSH public key (stock USRDATA partition) |
| MT6582_Android_scatter.txt | First install: BOOTIMG + ANDROID + USRDATA |
| MT6582_preserve_data_scatter.txt | Later updates: BOOTIMG + ANDROID only, keeps your data |
| manifest.json, SHA256SUMS, metadata/ | Hashes, partition plan, licences and build inputs |
| install.md, recovery.md | The detailed flashing and recovery runbooks |

The package must be created in `out/` from the exact commit you built, with a clean tree. `Y2DATA.img` carries your SSH public key, so it is personal: don't share it.

Continue with [INSTALL.md](https://innioasis.app/guides/reborn-y2linux-y2.html).

## 7. Releases (maintainer)

`tools/production/release.py` does a release in three commands. Nothing reaches GitHub or a player before `publish`.`python3 tools/production/release.py bump --version 1.0.0-beta.7.10 --sequence 6300 # identity in both repositories # review, run the checks, commit Y2Linux and Y2Reborn python3 tools/production/release.py sync-contract # only after platform/crates/y2p-contract changed; commit Y2Reborn python3 tools/production/release.py build --label 73 # ≈2 min # write the report and docs, commit them (only docs/ and readme.md may change after the build) python3 tools/production/release.py publish --label 73 --title "Y2Linux 1.0 Beta 7.10" \ --notes notes.md --yes`

The release text follows [the release notes format](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FRELEASE-NOTES-TEMPLATE.md): written for listeners, with everything but the changes and known issues between `<!-- github-only -->` markers that updaters such as the Innioasis Updater leave out. `publish` refuses notes without them.

`build` resumes the one build workspace `out/build` (`--clean` rebuilds it from scratch), runs the container suite, the update package with its validation and privacy check, the ELF and installed-ARM checks, the release inventory, the first-install package and legal-info in parallel (≈30 s instead of ≈80 s one after another), signs the update with the release key, checks that no image contains MediaTek firmware and puts everything under `out/release-<label>/` (`summary.json` lists hashes, test count and the time of every step). The third-party package sources go into a reproducible archive named after its hash; `publish` uploads it and the Linux source archive only when no earlier release carries the identical file, and links that file otherwise. The base for the next update package is always the newest published release. `build` refuses to start while Y2Reborn's `crates/y2p-contract` (the record types the platform and Reborn share) is not the same files as Y2Linux's `platform/crates/y2p-contract`; change the crate in Y2Linux only and copy it with `sync-contract`.

After every successful `build`, `out/` keeps only the workspace, the two newest release outputs (always including the newest published one) and the archives (`deep-sleep-final`, `rea`, `screenshots`); unused locked build environments in `.cache` go too. A build folder that the workspace still uses is never deleted. Preview with `release.py prune --dry-run`.

## Reference
  - [Locked build environment](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fenvironment.md) (what `tools/build/prepare.py` pins and isolates)
  - [Source reconstruction](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fplatform-v1-reconstruction.md) (inputs, licences, reproducibility limits)
  - [Kernel policy](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fkernel-policy.md), [overlay manifest](https://github.com/schulzcode/y2linux/blob/HEAD/kernel/patches/manifest.json)
  - Byte-identical rebuilds are not claimed: host tools, paths and timestamps can change

bytes in the Buildroot part. Each package records the exact inputs it used.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
