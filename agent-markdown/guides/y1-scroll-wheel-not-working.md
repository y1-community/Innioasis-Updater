---
title: "Innioasis Y1 Scroll Wheel Not Working After Update | Innioasis Firmware Archive - Innioasis Firmware Downloads"
description: "Innioasis Y1 scroll wheel or click wheel not working after an update? Reinstall Y1 Original Software, check the ring, and separate firmware from hardware faults."
language: "en"
source: "https://innioasis.app/guides/y1-scroll-wheel-not-working.html"
---

# Innioasis Y1 Scroll Wheel Not Working After Update | Innioasis Firmware Archive - Innioasis Firmware Downloads

Player recovery · Innioasis Y1

# Innioasis Y1 scroll wheel not working after an update

The wheel turns but nothing moves, or the click wheel stopped responding right after a flash. Here is how to separate a firmware fault from a hardware one, and what to do first.[Get Updater CE](../guide.html#platform)[Y1 software downloads](../firmware.html?model=Y1&software=original-y1)[Recovery guide](recovery.html)

## Work out whether the wheel or the firmware is at fault

On a Y1 the wheel is a physical input, but the firmware decides what each turn and click does. If the wheel stopped the moment you updated or installed an update on the player, the likely cause is software, not a broken part. If it ignores every software you try — stock, Rockbox, or a recovery screen — treat it as hardware.
  - Works in one software, dead in another: firmware fault.
  - Dead on every screen, including recovery: wheel, ribbon, or board.
  - Only one direction misses: usually debris under the ring or wear.
  - Wheel turns but nothing highlights: the player may be frozen — force a restart first.

## Quick checks before reinstalling firmware
  - Hold the power button for about 15 seconds to force the player off, then start it normally.
  - Test the wheel on the home screen, in Settings, and in the music player.
  - Press the physical buttons. If power and back respond but the wheel does not, the fault is the wheel itself.
  - Charge the player for 30 minutes with a known data cable — a low battery can make inputs behave erratically.
  - If you installed Rockbox or another custom build, return to Original Software and test again.

## Reinstall the Y1 firmware that matches your player

Because the wheel is driven by the firmware, an update-related failure is fixed by putting the correct Y1 Original Software back on the player. Do not use a Y2 package, and do not pick a release that is "close enough" — Y1 packages are built for Y1 hardware, and a Y2 build on a Y1 can leave the controls mapped wrong.
  - Open [Updater CE](../guide.html#platform) on your computer.
  - Set Device Model to Y1.
  - Choose Original Software in Software and pick a stable Y1 release — the manual package is `rom.zip`.
  - Click Install / Restore and let the package extract.
  - Power the Y1 fully off, connect the USB data cable only when Updater asks, and leave it until the success message.
Match the model and the release. If the release list looks like Y2 software, stop and re-select Y1. Full steps are in the [Y1 restore guide](restore-original-y1.html).

## Check the wheel ring for debris or damage

If the wheel is stiff, sticks, or only fails in one direction, pocket lint and grit can sit between the ring and the case. Power the player off and wipe around the ring with a dry microfiber cloth. Do not drip cleaners or alcohol into the gap, and do not prise the ring up.

If the ring is loose, cracked, or no longer clicks, the player needs service. Reinstalling firmware will not repair a damaged wheel, a disconnected ribbon, or liquid damage.

## If the player also will not start

A failed update can leave the Y1 unable to boot, which looks like a wheel problem because nothing responds. Work through the [Y1 won't turn on guide](y1-wont-turn-on.html) for charging, force-restart and manual recovery steps.

## Innioasis Y1 scroll wheel FAQ

### Why did my Innioasis Y1 scroll wheel stop working after an update?

An update can leave the wheel driver out of step with the rest of the firmware, especially if the installation was interrupted or a Y2 package was used. Reinstall the Y1 Original Software release for your model and test the wheel on the stock home screen.

### How can I tell whether the Y1 click wheel is broken or the firmware is faulty?

Test the wheel in more than one software. If it works in stock software but not in Rockbox, it is a firmware mapping problem. If it does nothing on any screen, including a recovery menu, suspect the wheel, its ribbon, or the board.

### Will restoring Original Software fix the Y1 scroll wheel?

It fixes failures caused by an update or a mismatched package, and it is the first thing to try. It will not repair a physically damaged wheel, a loose ribbon, or liquid damage.

### Can I use a Y2 firmware package to fix a Y1 wheel problem?

No. Y1 and Y2 packages are not interchangeable, and installing firmware for the wrong model can make the controls worse. Match the model and release before running Install / Restore.

## Related fixes
  - [Y2 scroll wheel not working](y2-scroll-wheel-not-working.html) — the same checks for the Y2
  - [Y1 won't turn on](y1-wont-turn-on.html) — power and boot recovery
  - [Innioasis recovery guide](recovery.html) — all symptom guides in one place
  - [Troubleshooting an install](../troubleshooting.html) — what a failed flash looks like
  - [Restore Y1 Original Software](restore-original-y1.html) — the full restore walkthrough

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
