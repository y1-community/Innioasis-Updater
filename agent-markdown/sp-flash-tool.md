---
title: "SP Flash Tool on Windows, Mac and Linux for Innioasis, Timmkoo and other MediaTek players"
description: "Flash Innioasis and Timmkoo players with Updater CE. For other SP Flash Tool v5.2032 devices, including Mechen, Louran, Globluum, Android MP3 players and Android head units, load the manufacturer's package with Install from file on Windows, Mac or Linux."
language: "en"
source: "https://innioasis.app/sp-flash-tool.html"
---

# SP Flash Tool on Windows, Mac and Linux for Innioasis, Timmkoo and other MediaTek players

Manual flashing

# Flash Tool for Innioasis and Timmkoo Players

SP Flash Tool comes inside Innioasis Updater on [Windows](drivers.html#windows) and [Linux](drivers.html#linux). You already have it. This guide shows the safe way to use it on an Innioasis Y1 or Y2, and the Updater route for Timmkoo players.[Return to the Updater guide](guide.html)[Firmware Downloads](firmware.html)[Troubleshooting](troubleshooting.html)

Start with Innioasis Updater

## Updater does the whole job in one pass

Updater does most installs in one pass. Pick the software, follow the steps, and you are done. It also tells you when a fix or a new release lands. SP Flash Tool is inside Updater's Toolkit for the rare cases Updater cannot finish. The steps below are the exception.

## What this tool is for

Updater flashes the player for you. SP Flash Tool is the same engine, without the guard rails. Use it when Updater will not start, when the player will not connect, or when you know your way around a scatter file.Try Updater first. For most installs and most recoveries, the guided [Updater route](guide.html) is the safer choice. Use SP Flash Tool when you know why you need it, and keep a charged battery plus a USB data cable ready.

## Flash tool for Innioasis players

Innioasis Updater is the flash tool for Innioasis players. It installs official software, updates and restore packages through the model-matched flow, and it keeps your music and settings.

### Innioasis Y1 flash tool

Choose the Y1 release in Updater, then connect the powered-off player when the app asks. The same Y1 packages work with SP Flash Tool when you need the manual route.

### Innioasis Y2 flash tool

Choose a release listed for Y2. Y2 packages are not interchangeable with Y1 packages, so check the model before you start.

## Flash tool for Timmkoo players

Timmkoo players use the same Updater install flow. It reads Timmkoo's ZIP and RAR packages directly, so you do not need a separate flash tool or scatter file.

### Timmkoo Q5 flash tool

Select the Q5 model in Updater, choose the Timmkoo package, then run Install / Restore and connect the player at the prompt.

### Timmkoo Q3 and Q3E flash tool

The Q3 entry covers the Q3 and Q3E alike. Updater picks the matching files from the package the project publishes.

## Other SP Flash Tool players, on Windows, Mac and Linux

Innioasis and Timmkoo packages are already in Updater CE. Choose those from the list. Install from file is for a device that is not in that list.

Updater CE installs firmware on Windows, Mac and Linux. SP Flash Tool v5.2032 and earlier is a Windows tool, with a Linux build and no Mac build. Updater CE covers that gap, including devices MTKclient can flash. The [Mac guide](sp-flash-tool-mac.html) explains why the official tool does not run on macOS.

That is the route for other scatter-based Android MP3 players and Android head units, including players sold as Mechen, Louran and Globluum:
  - Download the firmware archive from the manufacturer. It is usually a zip or a rar.
  - In Updater CE, use Install from file and select that archive, or the scatter file inside it.
  - Power the device off and connect it when the app asks.

Do not use Install from file for an Innioasis or Timmkoo package that Updater CE already offers. The catalogue copy is the one that matches the player.

Questions about a community project or a stock package go to [ko-fi.com/teamslide](https://ko-fi.com/teamslide) and the [Innioasis Community Discord](https://discord.gg/zHrT2zrcek).

## Where Updater puts it

SP Flash Tool ships with the Updater install folder, not as a separate download. Open it from there when you need it.

### Windows

Open the Updater install folder and run `flash_tool.exe`. The folder is usually under `%LOCALAPPDATA%\Innioasis Updater`. A Toolkit folder with an SP Flash Tool shortcut is included on some setups.

### Linux

Run the bundled `flash_tool` binary inside the Updater app folder on x86 / x86_64. The project installer prepares USB permissions with udev rules, so the player should appear when connected.

### macOS

SP Flash Tool is not bundled on macOS. Updater uses the MTKClient route there instead. Use the [guided install](guide.html) on a Mac and keep SP Flash Tool for a Windows or Linux machine.

The tool ships with the MediaTek download agent and model-specific configuration, so you do not need to collect DA or scatter files from elsewhere.

## Prepare the firmware
  - Grab the release you want from [Firmware Downloads](firmware.html). Choose `rom.zip` for a Y1 or `rom_y2.zip` for a Y2.
  - Extract the ZIP into its own folder. Windows can use Extract All. On Linux, use your archive manager or `unzip` in a terminal.
  - Check that the scatter file is in the extracted folder. It is usually named `MT6572_Android_scatter.txt` for Y1 packages and `MT6582_Android_scatter_def.txt` for Y2 packages, though a release may name it after its project.
Keep the models separate. The Y1 scatter describes an MT6572 device and the Y2 scatter describes an MT6582 device. Flashing with the wrong one is how players get bricked. If the scatter inside the ZIP does not match your model, stop and use a package listed for your model instead.

## Load the scatter and flash
  - Open SP Flash Tool from the Updater install folder.
  - In the Download tab, click Choose next to Scatter-loading File and select the scatter file from the extracted folder. The partition list will fill in.
  - Leave the flash mode on Download Only unless you are deliberately doing a full recovery, which needs Firmware Upgrade.
  - Click Download. The tool will wait for the player.
  - Power the player fully off, then connect the USB data cable. Put the player down and do not move it.
  - Wait for the green check mark. Only then disconnect the cable and start the player.

Keep the same USB cable and timing rules as the guided route: a data cable, no hub, and connect only when the tool is ready.

## If it does not flash
  - Check that the scatter and ZIP match the model printed on the player.
  - Confirm the player is fully powered off before connecting.
  - On Windows, confirm the MediaTek driver installed with the Updater setup; on Linux, confirm the udev rules from the project installer.
  - Reconnect the cable only when the tool is waiting. A port race can need a full unplug and a fresh Download click.

For anything beyond that, open [troubleshooting](troubleshooting.html). And remember: Updater is still the normal route, and [Y1](guides/restore-original-y1.html) and [Y2](guides/restore-original-y2.html) restore guides use it too.

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
