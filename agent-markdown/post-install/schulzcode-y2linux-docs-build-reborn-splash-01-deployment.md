---
title: "REBORN-SPLASH-01 startup update - Innioasis Updater"
description: "REBORN-SPLASH-01 startup update <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-reborn-splash-01-deployment.html"
---

# REBORN-SPLASH-01 startup update - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# REBORN-SPLASH-01 startup update

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# REBORN-SPLASH-01 startup update > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Owner installed and reports working, 2026-09-18. Subsequent SSH inspection confirms the expected build and splash-to-Reborn handoff. The owner installed before the written handoff was finished; this document retains the exact package and recovery instructions. No assistant flashing or reboot was performed.

Built Reborn source `6209f48402a00a077759df042916f0ae2c89783a`, integration `1e0888795008cc57de92c47a3a241e45cb91e420`, retained GPU-02 kernel source `7e318afbffe640c6bf9da458f61ac2108f7d5bde`. Rust 1.90.0, ARMv7 hard-float glibc, the existing Buildroot GCC 13.3.0 toolchain and vendored offline Cargo sources. Later documentation/test/packaging commits do not change these build identities.

## Implementation and console policy

The original firmware logo is untouched. Early normal boot puts tty0 into `KD_GRAPHICS` before the display module can attach the framebuffer console. Normal root service output goes to `/dev/kmsg`. Kernel command line and log level are unchanged; dmesg and SSH retain diagnostics. BusyBox syslog/klogd retain a bounded `/data/logs/system.log` plus one rotated file, 256 KiB each. Existing Reborn structured logging, metrics, health and control remain intact.

`/sbin/reborn-splash` in initramfs starts after the unchanged offline-charger gate permits normal boot. It is the same 17,724-byte native binary installed as `/usr/libexec/reborn-splash` in Y2ROOT. It discovers the Mediatek KMS connector and preferred mode, uses a CPU-mapped DRM dumb buffer and the Reborn dark/mint palette and 8×8 text style. The small loading bar updates at 20 FPS through a timed poll; there is no busy loop, GPU context, X11, desktop framework or fbdev drawing path. Only the small indicator is redrawn during animation. A singleton lock makes the root service's start attempt idempotent. The early process keeps directory FDs so its state/log/socket survive moving `/run` and switching root.

The console guard bypasses offline charging and the existing low-voltage gate. The charging program, kernel, display module, firmware, storage layout and Y2DATA contents are not changed. Offline-charging runtime regression remains unverified for this candidate; byte preservation and gate ordering are checked.

## Explicit handoff and failure behavior

Reborn allocates graphics resources and prepares its first actual UI framebuffer before it requests ownership. A root-only Unix socket at `/run/reborn-splash/control.sock` (directory 0700/socket 0600, peer UID checked) exchanges `READY 1`, `RELEASED 1`, then `PRESENTED 1`.

The splash drops DRM master but keeps its displayed framebuffer alive. Reborn already has an open DRM FD, acquires master, presents the first real frame, then acknowledges. Only then does the splash retire its buffer and exit. Neither path restores a text console or the retired splash CRTC. This avoids a last-close console restoration between processes. Reborn without a splash service still supports the previous startup path.

After 60 seconds without readiness, the splash becomes a static **Startup needs attention / Diagnostics available over USB** screen. A later ready Reborn can still take over. Malformed/oversized requests do not release the display; request assembly and handoff have a three-second deadline. A disconnected/timed-out handoff attempts to reclaim master and show failure without blindly killing Reborn. The existing bounded Reborn supervisor and SSH services remain active.

Splash events go to kmsg and a bounded 8 KiB JSONL file in `/run/reborn-splash`; Reborn copies startup evidence to `/data/reborn/logs/splash-boot.jsonl` best-effort. State is available at `/run/reborn-splash/state.json`. A normal handoff ends with `state=presented` and centralized `startup.ready` from Reborn.

## Why BOOTIMG changed

Read-only inspection of the preceding installed system showed fbcon appearing at 0.745889 seconds and switch_root at 9.213802 seconds. Y2ROOT cannot suppress that earlier console interval. Therefore BOOTIMG changed, limited to early initramfs policy/helper/libdrm and the DT initrd-end address for the new archive. The kernel, display module and offline-charging executable are byte-identical; 57 original initramfs entries are unchanged. All other DT fields and reservations match. No kernel rebuild, boot-argument change or partition modification.

## Package and exact hashes

Directory: `/home/luca/Dokumente/Code/Y2Linux/out/REBORN-SPLASH-01`.````````````````

| Payload | SHA256 |
| --- | --- |
| Y2ROOT.img | d40e9337e3a1149d12fdd240a59918b0d2c48e4e6a9974ab5b470685250d900c |
| BOOTIMG.img | 8671de2900fd05cc80a9eb7a3541d5bbdab7e5dd96c18f73f44ca1b13beb19a5 |
| fallback/Y2ROOT.img — deployed Reborn Baseline 01 | c353152dea44a554486e024a4d8a8105fbbdfd1310db5749b28d7e5b8e5c8012 |
| fallback/BOOTIMG.img — GPU-02 | 2e5f7e785e80dfc646e57d0ccfadff683d54a2c5303671c819ea4e42863089a9 |

Y2ROOT remains a 512 MiB image, with used ext4 space increasing by 28,672 bytes to 89,882,624 bytes. BOOTIMG is 6,244,352 bytes, an increase of 40,960 bytes. The [manifest](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/evidence/reborn-splash-01/package-manifest.json) records the ten changed root paths. Unrelated libraries and service files match Baseline 01.

## Manual installation and rollback reference

Already performed by the owner; no further installation is needed for inspection.
  - On the host, run:
` cd /home/luca/Dokumente/Code/Y2Linux/out/REBORN-SPLASH-01 sha256sum -c SHA256SUMS`
  - Open the established SP Flash Tool v5.2032 workflow. Load this directory's

`MT6582_preserve_data_scatter.txt` and choose Download Only.
  - Verify BOOTIMG and ANDROID only are checked and point to this directory's

`BOOTIMG.img` and `Y2ROOT.img`. **USRDATA and every other row must be unchecked with no payload.** Do not use Format or Firmware Upgrade.
  - Use the existing owner shutdown/USB entry procedure, select Download, connect

the powered-off Y2 and wait for successful completion before disconnecting. Boot normally. Keep Y2DATA; there is no data image or formatting step.
  - For rollback, load `fallback/MT6582_preserve_data_scatter.txt`, again Download

Only with both BOOTIMG and ANDROID, using both fallback images. Do not mix new early splash with old Reborn: the old app cannot acknowledge its handoff.

## Validation and actual device evidence

[Receipts](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fevidence%2Freborn-splash-01%2FREADME.md): 50 Rust tests, Clippy with warnings denied, 20 host daemon checks, nine native protocol/drawing tests, five BOOTIMG unit checks, eight ARM application/runtime checks, five ARM early-helper/shell checks, offline cross/rootfs build, raw ext4 consistency and image-preservation checks passed. Native drawing previews were inspected on the host; they are not physical panel photographs.

After the owner installed, boot ID `e650130d-34f0-46e8-a9eb-b39a9ca467da` recorded: console hidden 698 ms, splash visible 828 ms, released 49,448 ms, Reborn presented 49,456 ms. Owner reports the visible startup works. SSH confirms Mali400 EGL/GLES, same-session stability and all ten safe Reborn baseline checks pass.

The owner then reported radio unavailability. Targeted SSH tests found Wi-Fi scanning succeeds with 28 networks; Bluetooth adapter/BlueALSA and a ten-second discovery succeed with no discoverable peer. Both radios were initially off and were restored off. A misleading Wi-Fi off/unavailable state and a global stale UI notice are recorded in `/home/luca/Dokumente/Code/Y2Reborn/docs/validation/2026-09-18-radio-inspection.md`. No radio code or preferences were changed during inspection.

Actual Wi-Fi association/DHCP, pairing/A2DP, offline charging, SD hotplug and suspend/resume remain outside this successful startup/scan observation. This is not full Reborn Baseline 01 acceptance or authorization for Reborn 02.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
