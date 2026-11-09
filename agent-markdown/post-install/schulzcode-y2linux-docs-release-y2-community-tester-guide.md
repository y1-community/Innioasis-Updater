---
title: "Community tester installation, use and recovery - Innioasis Updater"
description: "Community tester installation, use and recovery Baseline02 is the newest sealed owner-local engineering candidate. Its fresh software checks pass; new-image and automatic"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-release-y2-community-tester-guide.html"
---

# Community tester installation, use and recovery - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Community tester installation, use and recovery

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Community tester installation, use and recovery

Baseline02 is the newest sealed owner-local engineering candidate. Its fresh software checks pass; new-image and automatic cold-boot hardware remain PHYSICAL_NOT_RUN. The preceding exact UART01 pair proves bounded C1/C2/C3 and affected I/O behavior. This candidate is not publicly cleared. The firmware and optional-codec redistribution questions remain independent of working source/build support.

## Current package and automatic idle

Use [Baseline02 versions/hashes](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md) and the [qualified paired fallback](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fcandidate-index.md). Only the owner installs BOOTIMG and ANDROID/Y2ROOT. An existing device update preserves Y2DATA; the first-initialization seed below is only for an intended first installation.

Qualified CPU0 C3 policy activates once after static boot checks; every entry still obeys topology, workload, OPP, clocks, timer and UART ACK guards. Check `y2-platform status cpu` for the boot-policy result. `y2-platform cpu-idle-policy stop`disables C3 for this boot; recovery boot options`y2.deep_idle=off` or `y2.cpu_safe=1` retain safe fallback. Runtime deep idle is separate from full system suspend and does not prove battery-life savings. After owner installation, the packaged guarded SSH harness checks exact identity/automatic startup before bounded C3 trials and wake/storage regressions.

## Before installing

Use the exact supported Innioasis Y2 board/layout named in `manifest.json` (`eastaeon82_wet_kk`, MT6582). Other board, display, battery or eMMC revisions need identification before installation. Keep your own original recovery material and the supplied paired fallback. Device-local NVRAM, PROTECT and calibration stay on that same device. Never copy another person's calibration or radio identity. Owner firmware provisioning accepts only the seven hash-checked stock firmware/default files described by `tools/connectivity/provision.py`; no private calibration tree is an input.

The normal package contains `BOOTIMG.img` and `Y2ROOT.img`. The preserving scatter selects only BOOTIMG and ANDROID (Y2ROOT). USRDATA/Y2DATA stays untouched. Never select Format All, Firmware Upgrade, preloader, LK, NVRAM, PROTECT, MBR/EBR, factory or calibration partitions. Flashing is an explicit physical owner action; none of the tools below invokes a flasher. Validate the package and compare its SHA256SUMS before using the separately documented owner flash procedure.

## First installation on your own device
  - Obtain the correctly provisioned, validated system package and a recovery plan

for your exact device. Preserve the stock protected partitions in place.
  - Generate an SSH key on your own computer if you do not already have one:

`ssh-keygen -t ed25519 -f ~/.ssh/y2linux_ed25519`. Keep the private key there. A maintainer never needs it. Only the `.pub` file is used below.
  - On the Linux build/packaging host, generate your separate, empty data seed:
` python3 tools/production/first_owner.py \ --system out/y2linux-baseline-02-candidate \ --public-key ~/.ssh/y2linux_ed25519.pub \ --output out/my-y2-first-initialization`

 This creates a fresh filesystem, without a maintainer data template or user database. Its separate scatter selects USRDATA only. It destroys any existing user data if you choose to flash it. Use it only for an explicitly intended first initialization, never a preserving update.
  - The owner installs the paired system images and, only when needed, their

separate first-initialization image. On first boot, device host keys and mutable settings are created locally. Confirm the new host-key fingerprint through a trusted local observation; never disable host-key checking to resolve a changed key.
  - Check Reborn, Settings → System → Storage/Battery and Settings → Bluetooth,

then export diagnostics. There is no claim of a Windows/macOS installer here; image generation and validation currently require Linux/e2fsprogs. The normal player and music workflow do not require knowledge of its internal USB networking protocol.

## Add music

Use a microSD card or Settings → PC Transfer. Copy music into the card's music folders, safely eject the card from the computer, then insert it in the player and choose Settings → Library → Scan for New Music. Do not remove a card while it is being written.

For internal storage, connect USB and use the transfer tool on your computer:`python3 tools/host/transfer.py song.flac \ --private-key ~/.ssh/y2linux_ed25519 --known-hosts ~/.ssh/known_hosts`

The tool uploads into a temporary file, verifies the hash and publishes the track without replacing an existing file. The destination can include a folder using `--name 'Artist/Album/song.flac'`. If interrupted, the existing music remains intact and the receipt identifies the incomplete transfer. Then rescan in Reborn. Advanced connection details are in the platform transfer documentation.

## Send a useful diagnostic report

Choose Settings → System → Diagnostics → Export Diagnostic Report. It is different from Export Player Data, which is a private backup. Retrieve an export from a computer with the already verified owner connection:`python3 tools/host/diagnostics.py --host root@10.42.0.1 \ --private-key ~/.ssh/y2linux_ed25519 --known-hosts ~/.ssh/known_hosts \ --output ./y2-diagnostics.tar.gz`

This command creates and downloads a fresh redacted export and checks its hash. It includes versions, boot ID, numerical platform/CPU/storage/radio/power health, codec state and classified kernel/Reborn/system log events. It contains no raw log text, music names, database, passwords, SSH private keys, bonds, NVRAM or calibration. Keep your symptom description separate: what you did, what happened, which headphones/card/host you chose to disclose, and roughly when it occurred. The tool keeps private file permissions on the computer. Do not attach a private state backup or the private physical-harness receipts to a public bug report. Eight retained diagnostic exports are allowed before retrieving/removing old ones; low-space reserve is respected.

## Preserving beta1 → beta2 update

Back up irreplaceable music and your private state first. Check the target package manifest, supported layout, SHA256SUMS and paired fallback. With the player powered down, the owner uses only `MT6582_preserve_data_scatter.txt`; only BOOTIMG and ANDROID are selected. No Y2DATA initialization image is used. Settings, library, credentials and Bluetooth bonds remain on Y2DATA. After reboot, check the reported new source pair and verify playback, library and network/bond retention. The integrated qualification tool captures the before/after evidence. A successful host package test is not a physical update rehearsal.

Signed root-only update support is a separate advanced workflow. The manual BOOTIMG/Y2ROOT pair is not A/B OTA, and a checksum is not an update signature.

## Recovery by symptom

| Symptom | Recovery action |
| --- | --- |
| Reborn fails but the platform boots | Export diagnostics; restart through the existing service recovery workflow. Restore the paired fallback if persistent. Preserve Y2DATA. |
| Bad settings | Use Settings → System → Reset & Maintenance → Reset Reborn Settings; it preserves music and the library. Avoid full-user reset unless you intend that loss. |
| Corrupt library database | Use Settings → Library → Rebuild Library if Reborn starts. Existing corrupt DB evidence is retained according to recovery policy; music files are the source of truth. Storage/I/O errors must be resolved first. |
| Bad root or failed root update | Use the documented rescue/rollback workflow or owner-install the supplied paired fallback. Do not initialize data. |
| Bad BOOTIMG or no Linux boot | The owner installs the known matched BOOTIMG/Y2ROOT fallback through the established recovery procedure. There is no automatic A/B boot fallback. |
| Changed/missing SSH identity | Verify the host key through a trusted observation. Restore your own public-key authorization; never borrow maintainer credentials. |
| Missing radio calibration | Stop radio activation and preserve evidence. Restore only that device's own original calibration through the documented owner recovery process. |

## One integrated physical run

Review the offline plan first:`python3 tools/development/qualify-feature-completion.py`

After the owner installs the integration candidate, use existing pinned SSH aliases for USB and the independently authorized Wi-Fi observer:`python3 tools/development/qualify-feature-completion.py \ --package out/y2linux-baseline-02-candidate \ --host y2 --wifi-host y2-wifi --run --exercise --sleep`

The owner, not this implementation pass, runs this command. It checks exact identity before mutation, keeps independent lanes moving after an ordinary test failure, and refuses deep-sleep exercises unless awake/SRAM gates pass. A reset, identity mismatch, taint or lost recovery stops further mutation. Charger removal and the deliberate Power wake require owner interaction. Native bit-depth proof requires I2S capture; codec proof needs a peer supporting that codec; audible and wheel/boot/shutdown observations still need a person. These remain named pending cases rather than inferred passes. `--run` alone is read-only observation; `--observe-seconds` captures an explicitly chosen listening/coexistence workload.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
