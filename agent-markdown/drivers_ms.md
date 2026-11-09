---
title: "Innioasis Y1 and Y2 USB drivers | Windows driver and Linux permissions - Innioasis Updater"
description: "Set up your computer for Innioasis Updater: Windows MediaTek driver and Linux USB permissions — plus cable and timing fixes."
language: "ms"
source: "https://innioasis.app/drivers_ms.html"
---

# Innioasis Y1 and Y2 USB drivers | Windows driver and Linux permissions - Innioasis Updater

Computer setup

# Make the computer ready before the player.

Most connection problems come from the driver, permissions, cable, or timing. Windows needs the MediaTek driver installed. Linux needs the right USB permissions. Find your platform below.[Dapatkan Updater CE](guide_ms.html#platform)[Menyelesaikan masalah](troubleshooting_ms.html)

## Windows
  - Download the MediaTek driver installer below.
  - Run the installer and allow Windows to install the driver.
  - Restart the computer.
  - Open Updater CE and wait for the connect prompt before you plug in the powered-off player.

Some Windows systems block the driver through Core isolation (Memory integrity). If Updater CE still cannot see the player after a restart, turn Memory integrity off in Windows Security, restart, and reinstall the driver. Turn the setting back on when you are finished if your system allows it.

Windows won't launch the app? If Windows Security or Smart App Control stops Updater CE from opening, open tetapan (press Win + I) → Privacy & security → Windows Security → App & browser control → Smart App Control settings and set it to Off. To re-enable later, set `VerifiedAndReputablePolicyState` kepada `1` (On) or `2` (Evaluation Mode) under `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\CI\Policy` in Registry Editor.[Download Windows driver](https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe)

[Back to the main guide](guide_ms.html#windows) · [Muat Turun Perisian](firmware_ms.html)

## Linux USB permissions

Linux needs your user account to be allowed to talk to the MediaTek USB chip inside the player. Updater CE usually sorts this out during install, and the same permission covers SP Flash Tool, so treat this as a fix-it step rather than a normal stage.
  - Run Updater CE as your normal user, not as root. The installer asks for administrator access only when it needs it.
  - Check the player is seen at all. Power the player off, connect the cable, and run the lsusb command in a terminal. A connected player shows up as a MediaTek device with the vendor ID 0e8d.
`lsusb`
  - If it appears in lsusb but Innioasis Updater CE or SP Flash Tool says permission denied or cannot open the port, your user is missing access to the USB device. The same udev rule covers both tools, so add one that lets the users group read it.
`SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"`

Save that line to a new file named /etc/udev/rules.d/51-innioasis.rules, then run:`sudo udevadm control --reload && sudo udevadm trigger`
  - Unplug the player fully, plug it back in, and try the install again.
  - If SP Flash Tool reports a serial permission or port race, unplug fully and reconnect only when prompted.
Do not improvise flash offsets.If you move to a manual recovery tool, use the files and model-specific configuration shipped with the project.

[Back to the main guide](guide_ms.html#linux) · [Muat Turun Perisian](firmware_ms.html) · [SP Flash Tool panduan](sp-flash-tool_ms.html)

## Cable and timing
  - Use a known USB data cable.
  - Avoid hubs while troubleshooting.
  - Power the correct model fully off.
  - Connect only at the prompt.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
