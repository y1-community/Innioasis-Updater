---
title: "Innioasis Y2 Scroll Wheel Not Working After Update | Innioasis Firmware Archive - Innioasis Firmware Downloads"
description: "Innioasis Y2 scroll wheel or click wheel not working after an update? Reinstall Y2 Original Software, check the ring, and separate firmware from hardware faults."
language: "en"
source: "https://innioasis.app/guides/y2-scroll-wheel-not-working.html"
---

# Innioasis Y2 Scroll Wheel Not Working After Update | Innioasis Firmware Archive - Innioasis Firmware Downloads

Player recovery · Innioasis Y2

# Innioasis Y2 scroll wheel not working after an update

The wheel turns but the player ignores it, or the click wheel stopped right after an update. Here is how to tell a firmware fault from a hardware one on the Y2.[Get Updater CE](../guide.html#platform)[Y2 software downloads](../firmware.html?model=Y2&software=original-y2)[Recovery guide](recovery.html)

## Work out whether the wheel or the firmware is at fault

On a Y2 the wheel is a physical input, but the firmware decides what each turn and click does. A wheel that stopped as soon as you updated or updated points at software. A wheel that ignores every software — stock, Rockbox, or a recovery screen — points at the part.
  - Works in one software, dead in another: firmware fault.
  - Dead on every screen, including recovery: wheel, ribbon, or board.
  - Only one direction misses: usually debris under the ring or wear.
  - Wheel turns but nothing highlights: the player may be frozen — force a restart first.

## Quick checks before reinstalling firmware
  - Hold the power button for about 15 seconds to force the player off, then start it normally.
  - Test the wheel on the home screen, in Settings, and in the music player.
  - Press the physical buttons. If power and back respond but the wheel does not, the fault is the wheel itself.
  - Charge the player for 30 minutes with a known data cable.
  - If you installed Rockbox for Y2 or another custom build, return to Original Software and test again.

## Reinstall the Y2 firmware that matches your player

The wheel is driven by the firmware, so an update-related failure is fixed by putting the correct Y2 Original Software back on the player. Never use a Y1 package on a Y2, and do not pick a release that is "close enough" — Y2 packages are built for Y2 hardware.
  - Open [Updater CE](../guide.html#platform) on your computer.
  - Set Device Model to Y2.
  - Choose Original Software in Software and pick a stable Y2 release — the manual package is `rom_y2.zip`.
  - Click Install / Restore and let the package extract.
  - Power the Y2 fully off, connect the USB data cable only when Updater asks, and leave it until the success message.
Match the model and the release. If the release list looks like Y1 software, stop and re-select Y2. Full steps are in the [Y2 restore guide](restore-original-y2.html).

## Check the wheel ring for debris or damage

If the wheel is stiff, sticks, or only fails in one direction, pocket lint and grit can sit between the ring and the case. Power the player off and wipe around the ring with a dry microfiber cloth. Do not drip cleaners or alcohol into the gap, and do not prise the ring up.

If the ring is loose, cracked, or no longer clicks, the player needs service. Firmware cannot repair a damaged wheel, a disconnected ribbon, or liquid damage.

## If the player also will not start

A failed update can leave the Y2 unable to boot, which looks like a wheel failure because no input responds. Work through the [Y2 won't turn on guide](y2-wont-turn-on.html) for charging, force-restart and manual recovery.

## Innioasis Y2 scroll wheel FAQ

### Why did my Innioasis Y2 scroll wheel stop working after an update?

An update can leave the wheel driver out of step with the rest of the firmware, especially if the installation was interrupted or a Y1 package was used. Reinstall the Y2 Original Software release for your model and test the wheel on the stock home screen.

### How can I tell whether the Y2 click wheel is broken or the firmware is faulty?

Test the wheel in more than one software. If it works in stock software but not in Rockbox, it is a firmware mapping problem. If it does nothing on any screen, including a recovery menu, suspect the wheel, its ribbon, or the board.

### Will restoring Original Software fix the Y2 scroll wheel?

It fixes failures caused by an update or a mismatched package, and it is the first thing to try. It will not repair a physically damaged wheel, a loose ribbon, or liquid damage.

### Can I use a Y1 firmware package to fix a Y2 wheel problem?

No. Y1 and Y2 packages are not interchangeable, and installing firmware for the wrong model can make the controls worse. Match the model and release before running Install / Restore.

## Related fixes
  - [Y1 scroll wheel not working](y1-scroll-wheel-not-working.html) — the same checks for the Y1
  - [Y2 won't turn on](y2-wont-turn-on.html) — power and boot recovery
  - [Innioasis recovery guide](recovery.html) — all symptom guides in one place
  - [Troubleshooting an install](../troubleshooting.html) — what a failed flash looks like
  - [Restore Y2 Original Software](restore-original-y2.html) — the full restore walkthrough

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
