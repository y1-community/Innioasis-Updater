---
title: "Innioasis Y2 Won&#x27;t Turn On | Innioasis Firmware Archive - Innioasis Firmware Downloads"
description: "Innioasis Y2 won't turn on or charge? Force a restart, check whether a computer sees it, then restore Y2 firmware or use manual SP Flash Tool recovery."
language: "en"
source: "https://innioasis.app/guides/y2-wont-turn-on.html"
---

# Innioasis Y2 Won&#x27;t Turn On | Innioasis Firmware Archive - Innioasis Firmware Downloads

Player recovery · Innioasis Y2

# Innioasis Y2 won't turn on

A black screen does not always mean a dead player. Work through charging, a force restart, and detection on a computer before you try manual recovery.[Get Updater CE](../guide.html#platform)[Firmware Downloads](../firmware.html)[Recovery guide](recovery.html)

## Charge the Y2 properly before anything else

Most "Y2 won't turn on" reports are a flat battery, a charge-only cable, or a charger that cannot supply enough current. A deeply drained Y2 can take 20 to 30 minutes on power before the screen shows anything.
  - Use a known USB data cable, not a charge-only cable.
  - Try a wall charger, then a computer USB port directly — not a hub.
  - Leave it connected for 30 to 60 minutes and watch for a charging icon or backlight.
  - Try a second cable and charger before moving on.

## Force a restart

Hold the power button for about 15 seconds, release it, wait five seconds, then press power once. This clears a hung boot and is safe to repeat.

If the screen shows the logo and then goes black, the player is starting and failing — skip to the firmware restore below. If nothing happens at all, keep it on charge and try again after half an hour.

## Check whether a computer can see the player

Connect the powered-off Y2 with a data cable and open Device Manager on Windows, `lsusb` on Linux, or MTKClient on macOS. A working player appears as a MediaTek device with vendor ID `0e8d`. If it appears, the hardware is alive enough to reinstall even when the screen stays dark.

If nothing appears, install the MediaTek driver on Windows first — the [driver guide](../drivers.html) covers Windows and Linux permissions.

## Restore the Y2 stock firmware

If the player is detected but will not boot, reinstall Y2 Original Software. Use a Y2 package only; a Y1 build will not start on Y2 hardware.
  - Open [Updater CE](../guide.html#platform) on your computer.
  - Set Device Model to Y2.
  - Choose Original Software in Software and pick a stable Y2 release — the manual package is `rom_y2.zip`.
  - Click Install / Restore and let the package extract.
  - Power the Y2 fully off, connect the USB data cable only when Updater asks, and leave it until the success message.
Keep power stable. An installation that loses power can leave the player unusable. Charge it first and connect it directly to the computer.

## Manual recovery when Updater cannot see the player

Updater CE includes manual recovery tools for the cases the guided install cannot finish. [SP Flash Tool](../sp-flash-tool.html) is bundled on Windows and Linux x86, and the MTKClient route covers macOS. Both need a model-matched firmware package from the [Firmware Downloads](../firmware.html) page.

Follow the tool guide for your platform rather than improvising scatter files or offsets. If the player is not detected by any tool, the fault is likely the battery, charge port, or board.

## If it still will not start

Stop flashing and treat it as hardware. Do not open the case or press on the battery. Ask the community with the model, what the screen does, whether a computer detects it, and which packages you tried — the [Discord community](https://discord.gg/zHrT2zrcek) can help identify a service route.

A stock restore replaces the system, so back up anything stored in the player's internal memory before flashing. Music on a MicroSD card is not touched by the restore.

## Innioasis Y2 power FAQ

### Why won't my Innioasis Y2 turn on?

The usual causes are a fully drained battery, a charge-only cable or weak charger, a firmware crash that stops the boot, or a hardware fault. Charge it for 30 minutes with a known data cable before assuming the player is dead.

### How do I force restart an Innioasis Y2?

Hold the power button for about 15 seconds, release it, wait five seconds, then press power once. If nothing appears, leave it charging and try again after 30 minutes.

### Can I recover a Y2 that won't power on?

Often yes. If a computer still detects the MediaTek device, reinstall the Y2 Original Software package with Updater CE. If it is not detected, use the SP Flash Tool or MTKClient recovery included with Updater CE and a model-matched Y2 firmware file.

### Does a Y2 need to be charged before installing?

Yes. An installation that loses power can leave the player unusable. Charge it first and connect it directly to the computer rather than through a hub.

## Related fixes
  - [Y1 won't turn on](y1-wont-turn-on.html) — the same checks for the Y1
  - [Y2 scroll wheel not working](y2-scroll-wheel-not-working.html) — if it boots but the wheel does not
  - [Innioasis recovery guide](recovery.html) — all symptom guides in one place
  - [SP Flash Tool guide](../sp-flash-tool.html) — manual flashing on Windows and Linux
  - [Troubleshooting an install](../troubleshooting.html) — what a failed flash looks like

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
