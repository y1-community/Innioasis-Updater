---
title: "How to Recover a Non-Booting MediaTek Player After MTKclient Failure · Innioasis Community"
description: "Step-by-step guide to unbrick and recover non-booting Innioasis Y1, Y2, G1, Timmkoo, and MediaTek players after MTKclient interrupted flashes on Linux or macOS."
language: "bn"
source: "https://innioasis.app/recover-non-booting-device_bn.html"
---

# How to Recover a Non-Booting MediaTek Player After MTKclient Failure · Innioasis Community

Troubleshooting & Device Recovery

# Recovering a Non-Booting Device After MTKclient Flashing

If your Innioasis Y1, Y2, or MediaTek device fails to power on or shows a black screen after flashing with MTKclient on macOS or Linux, do not panic. The hardware BootROM (BROM) is permanent and cannot be destroyed.

## Why MTKclient May Stall or Leave a Black Screen

MTKclient relies on software exploit payloads (kamakiri / amonet) to bypass DA authentication and raw USB communication via libusb. On macOS and Linux ARM64 systems:
  - USB handshake latency or port timeouts on macOS can stall DA payload injection mid-transfer.
  - Missing or incomplete partition headers leave the bootloader (preloader / lk) in a non-responsive state.
  - The player appears completely dead—no LED, no charging icon, no screen backlight.

Even in this state, the MediaTek chipset drops back into BROM Mode (USB VID 0e8d, PID 0003), ready for official low-level recovery.

## The Definitive Recovery Method: SP Flash Tool Engine in Updater CE

The safest, most reliable way to recover your bricked player is using আপডেটার CE configured with the official SP Flash Tool backend.

### Exact Steps in Updater CE:
  - খোলা আপডেটার CE.
  - ক্লিক করুন সেটিংস in the left navigation sidebar.
  - Scroll down to the Advanced section and enable Show Advanced Settings.
  - Under Install Method (or Flashing Engine for MediaTek installer), locate the Flash Method dropdown.
  - Change the selection from Auto (recommended) বা MTKClient থেকে SP Flash Tool.
  - Confirm the prompt and return to the main install flow.

## Platform Architecture & OS Requirements for SP Flash Tool

MediaTek's official `SP Flash Tool` binary is compiled natively as an x86_64 ELF binary for Linux and a PE32+ executable for Windows x64.Important Hardware Note for macOS and ARM64 Linux Users:
 Because MediaTek does not compile SP Flash Tool for macOS (Darwin) or Linux ARM64 (aarch64), macOS users and ARM64 Linux users (such as Raspberry Pi or Apple Silicon running Asahi Linux) experiencing a brick must connect their player to: 
  - An x64 Windows PC (Windows 10 / 11 64-bit), or
  - An x86_64 Linux PC (Ubuntu, Debian, Fedora, Arch 64-bit).

## Step-by-Step Hardware Unbricking Process
  - Disconnect the Player: Unplug the USB cable from the player and PC completely.
  - Hard Power Off: Hold the Power button (or Power + Volume Down) for 15 seconds to ensure the chipset is fully powered down and not stuck in a low-power USB loop.
  - Launch Updater CE with SP Flash Tool Mode: Select your device model (e.g. Innioasis Y1 বা Innioasis Y2) and choose মূল সফটওয়্যার to restore stock partitions.
  - Initiate Install / Restore: ক্লিক করুন ইনস্টল / পুনরুদ্ধার in Updater CE. Wait until the status prompt says Waiting for player...
  - Insert USB Cable to Trigger BROM: While the device is OFF, plug in the USB cable directly to a high-speed motherboard USB port (avoid unpowered USB hubs).
  - The system will detect the MediaTek VCOM port, push the Download Agent (DA), rewrite partition tables, and restore all firmware images cleanly.

## Permutations by Model and Operating System

| Model | Failed Platform | Recommended Recovery Setup | Engine & Mode |
| --- | --- | --- | --- |
| Innioasis Y1 | macOS (Apple Silicon / Intel) | Windows x64 / Linux x86_64 PC | SP Flash Tool + Y1 Stock ROM |
| Innioasis Y1 | Linux ARM64 / x86_64 | Linux x86_64 or Windows x64 PC | SP Flash Tool + Community DA |
| Innioasis Y2 | macOS (MTKclient stalled) | Windows x64 / Linux x86_64 PC | SP Flash Tool + Y2 Scatter Recovery |
| Innioasis G1 / G3 / G5 | macOS / Linux MTKclient | Windows x64 PC with VCOM Drivers | SP Flash Tool + Factory Firmware |
| Mechen H1 / Timmkoo A5 | Any platform | Windows x64 or Linux x86_64 PC | SP Flash Tool + Scatter file |

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
