---
title: "USB device and owner file transfer v1 - Innioasis Updater"
description: "USB device and owner file transfer v1 <!-- knowledge-base-scope: source-contract; baseline02-sync 2026-10-03 -- Current bounded evidence: UART01 passes three 1 MiB bidire"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-architecture-platform-usb-v1.html"
---

# USB device and owner file transfer v1 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# USB device and owner file transfer v1

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# USB device and owner file transfer v1

Current bounded evidence: UART01 passes three 1 MiB bidirectional USB checksum rounds with an independent Wi-Fi observer after CPU idle qualification, same boot and no filesystem errors. The repaired device/transfer path is retained in Baseline02. New-image acceptance and large-transfer/cable/host-sleep endurance remain pending; USB host/VBUS and full-suspend restoration remain separate. Normal Dropbear is USB-bound. The temporary owner-authorized Wi-Fi observer is a qualification fallback, not a new persistent listener. See [UART01 hardware](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) and [Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md).

Historical SFTP implementation: DONE_SOFTWARE / HOST_VALIDATED. ACM + ECM used the existing peripheral-only MUSB/PHY path. The session runtime-PM reference correction already exists; this pass does not duplicate it. USB host/OTG and USB Audio host remain PHYSICAL_GATE: MT6582 MAC host capability is not board ID/role wiring, VBUS sourcing, current limit or connector proof. No host/VBUS path is enabled. Retained evidence is M2 passive B-device state and POWER-02's two workaround reconnects; neither establishes PC sleep/wake/large-transfer endurance; the newer bounded UART01 checksum proof is scoped above.

## Protocol and access

Use authenticated SFTP over the existing USB ECM link, 10.42.0.1:22, with the provisioned owner public key. Linux/macOS OpenSSH and Windows OpenSSH/WinSCP are client options; platform-specific ECM enumeration/address setup still needs qualification. The candidate retains ECM and does not claim universal Windows plug-and-play or add an unqualified RNDIS gadget. The new desktop-transfer candidate supersedes SFTP as the normal product path: MTP + ECM by default, ACM + ECM as an advanced disconnected-session choice. [USB Platform 1.0 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-USB.md) records architecture, file confinement and qualification limits. No writable Linux filesystem is exported as USB mass storage. The following authenticated SFTP contract remains.

Dropbear 2026.94 is restricted to both that address and usb0 using SO_BINDTODEVICE. Its existing warning-and-continue failure is patched to close the socket instead. Password authentication and forwarding remain disabled. The supervised listener waits for owner authorization, exact USB address and successful nonblocking getrandom before host-key generation or network crypto. Missing entropy keeps it Starting; no weak RNG fallback is selected. Kernel listening state, service heartbeat and boot identity determine readiness. It does not listen on Wi-Fi.

Only OpenSSH 9.9p2's SFTP subsystem is installed, using pinned Buildroot 2025.02.18 source/hash and all its LTS security patches. No second sshd, client suite or universal key is installed. The SFTP wrapper disables link/copy-data operations; a small patch checks 96 MiB and 128-inode reserve before each data write. [SFTP subsystem options](https://man.openbsd.org/sftp-server) are standard OpenSSH. This is trusted-owner administration, with the existing root SSH account. It is not an untrusted media sandbox: root keys already authorize maintenance. A separate unprivileged/chroot upload account is DEFERRED until product onboarding and its storage permission requirements are settled. No private keys enter images.

## Verified upload

On an owner computer with a verified host-key entry:`python3 tools/host/transfer.py song.flac --name 'Artist/Album/song.flac' \ --private-key /owner/path/y2_key --known-hosts /owner/path/y2_known_hosts`

The helper calculates SHA-256, requests a private staging token, uploads over SFTP, then asks the platform to verify/publish. Filename input never becomes shell syntax; OpenSSH receives quoted fixed commands. The destination is under the stable /data/music contract, with no symlink/submount traversal or overwrite. Mount generation and free space are checked again on commit. A fresh sealed inode prevents an old SFTP file descriptor from changing already verified music. File and directory fsync precede success. This requires space for upload plus sealed copy plus the 96-MiB reserve; it intentionally rejects oversized transfers.

An interrupted session leaves only its private stage. The printed token supports `y2-platform transfer status --id TOKEN` and explicit `y2-platform transfer discard --id TOKEN`. A successful helper discards its stage after printing the commit receipt. At most eight stages are admitted. If power fails after atomic publication but before the receipt, existing music is still never overwritten; inspect its hash and discard the retained stage before retry. The helper does not automatically resume an unknown transaction. Ordinary SFTP clients may use /data/music directly but do not gain the helper's verified atomic publish contract. They still receive reserve-write failures.

## Qualification

For a future exact candidate, capture y2-status USB, SFTP/SSH readiness and hashes before/after: unplug/reconnect on one boot, PC sleep/wake, upload interrupt, one large file and many small files, concurrent playback, near-full data refusal, and unauthorized/incorrect host-key rejection. Confirm a Wi-Fi-side attempt cannot reach the USB-bound listener (including a route to 10.42.0.1). Use externally verified host keys; never disable host-key checking. Record client OS/driver, negotiated USB speed, elapsed bytes/time, boot ID, kernel warnings, data-space state and Reborn XRUNs. Owner controls cable and power actions. No throughput figure or electrical durability is claimed.

## Historical physical note — 2026-09-28

2026-09-28 physical update: The [Fix01 run](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01-PHYSICAL-QUALIFICATION.md) passed one 256-KiB bidirectional SHA roundtrip, then lost USB connection during the next transfer while the Y2 UI stayed usable. The owner restarted. The failed-interval observer did not survive, so controller/IRQ/DMA cause is unknown. The protocol and access contract below remains implemented, but loaded transfer reliability, independent recovery and full-suspend restoration are not qualified. Normal Dropbear remains USB-bound; the run's temporary key-only Wi-Fi SSH recovery listener was removed afterward.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
