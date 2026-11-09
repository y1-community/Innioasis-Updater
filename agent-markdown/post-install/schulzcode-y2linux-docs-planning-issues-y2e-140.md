---
title: "Y2E-140 — Establish a reliable first-boot observation path - Innioasis Updater"
description: "Y2E-140 — Establish a reliable first-boot observation path <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2e-140.html"
---

# Y2E-140 — Establish a reliable first-boot observation path - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2E-140 — Establish a reliable first-boot observation path

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2E-140 — Establish a reliable first-boot observation path > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Depends on Y2E-125/130 and the completed M1 offline artifact. Research directly; supporting host tooling only. No candidate flash, pin probing, voltage injection, boot-mode change or feature expansion.

Acceptance:
  -  Reconcile package preloader/LK/kernel UART selection with safe installed-stock console evidence; record exact normal/conditional selection and baud/format.
  -  Establish a board-specific physical TX/GND connection and logic voltage from credible evidence, or explicitly retain this blocker and evaluate the smallest alternative.
  -  Define reproducible receive-only host capture with retained raw bytes, timing, adapter/settings and integrity metadata.
  -  Capture identifiable stock LK/kernel output before changing BOOTIMG; distinguish a host tooling test from device proof.
  -  Decide whether the existing artifact needs revision; any justified change must rerun all offline validation.
  -  Update authoritative knowledge and identify the next bounded launch proof. Keep this issue open if physical/capture acceptance remains unsatisfied.

2026-09-08 result: OPEN, physical evidence required. Installed ttyMT0/sysfs/iomem plus remapped FM driver prove the normal installed-kernel controller is UART0 (0x11002000), superseding UART3. Package LK's conditional UART0 branch is consistent with this result, but installed handoff identity/routing and actual baud are not fully proved. The manufacturer native pin-domain table supports expected 1.8 V; no board-specific TX/GND pad or pad measurement is confirmed. No adapter was present.

D10 corrects only DT UART0/IRQ51 and strict validation. Two fresh full offline builds match across 11 outputs; all nine artifact tests pass (22 real-artifact and 25 package mutation/extent cases), source verification covers 91,166 files/links. All D08 addresses/sizes, kernel/config/initramfs bytes stay unchanged. Current BOOTIMG SHA-256: `574061649e10266927267b68afbc95da7fe0761dc9823e88767741bac9363fd9`.

Receive-only host tool/runbook implemented; four PTY tests pass on Python 3.14.7 and locked 3.12.14. These are not hardware proof. Actual ADB `/proc/last_kmsg` yields only a prior late kernel/shutdown log, not LK/serial capture. Next missing evidence is verified UART0 TX/GND/level plus actual stock LK/kernel capture. If native TX is inaccessible, investigate exact preloader UART-over-USB accessory detection/electrical/routing persistence; do not guess cables or switch PHY live. U07b is the next launch gate after observation passes; U07c and backup/recovery/power remain required.

[Authoritative evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fobservation-path.md), [capture runbook](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fstock-console-capture.md), [revised artifact](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Ffirst-boot-result.md). No candidate boot/flash or additional Linux feature occurred.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
