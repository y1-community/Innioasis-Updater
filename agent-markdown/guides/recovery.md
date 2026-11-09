---
title: "Innioasis Y1 and Y2 Recovery Guide | Innioasis Firmware Archive - Innioasis Firmware Downloads"
description: "Recovery guide for Innioasis Y1 and Y2 players that won't turn on or have a scroll wheel that stopped working after an update. Reset and firmware steps."
language: "en"
source: "https://innioasis.app/guides/recovery.html"
---

# Innioasis Y1 and Y2 Recovery Guide | Innioasis Firmware Archive - Innioasis Firmware Downloads

Player recovery · Y1 and Y2

# Innioasis Y1 and Y2 recovery guide

Won't turn on, wheel not working, or an install that stopped halfway. Start with the symptom, then follow the steps in order instead of jumping straight to manual recovery.[Get Updater CE](../guide.html#platform)[Firmware Downloads](../firmware.html)[Troubleshooting](../troubleshooting.html)

Start with Innioasis Updater

## The guided install fixes most of these

Updater does it in one pass. Pick the software, follow the steps on screen, and you are done. It also tells you when a fix or a new release lands.

## Start with the symptom

These guides cover the two failures people hit most often after an update or an install. Pick the one that matches what you see, then work through it in order.

### Scroll wheel not working

The wheel turns but the player ignores it, or it stopped right after an update.

[Y1 scroll wheel guide](y1-scroll-wheel-not-working.html) · [Y2 scroll wheel guide](y2-scroll-wheel-not-working.html)

### Player won't turn on

A black screen, no charge light, or a logo that appears and disappears.

[Y1 power guide](y1-wont-turn-on.html) · [Y2 power guide](y2-wont-turn-on.html)

### Install stopped part-way

Updater failed before or after the USB prompt, or the release list looks wrong.

[Troubleshooting guide](../troubleshooting.html)

### Need the files

Original Software and custom packages for each model.

[Firmware Downloads](../firmware.html)

## Y1 and Y2 packages are not interchangeableNever cross-install a model. A Y1 `rom.zip` is not a Y2 package, and a Y2 `rom_y2.zip` will not run on a Y1. Installing firmware for the wrong model is one of the most common reasons a player ends up with dead controls or a boot loop.

Check the model printed on the player, then match it in Updater CE before you choose a release.

## Restore the matching Original Software first

Before any manual tool, put the stock firmware for the correct model back on the player. This fixes most update-related wheel and boot failures.

Y1: select Y1, choose Original Software, pick a stable Y1 release, then run Install / Restore. [Full Y1 restore guide](restore-original-y1.html).

Y2: select Y2, choose Original Software, pick a stable Y2 release, then run Install / Restore. [Full Y2 restore guide](restore-original-y2.html).

Power the player off and connect the USB data cable only when Updater asks. Leave it connected until the success message.

## Manual recovery that ships with Updater CE

When Updater cannot finish the job, the same install includes the manual tools. [SP Flash Tool](../sp-flash-tool.html) is bundled on Windows and Linux x86 machines, and the MTKClient route covers macOS. Both need a firmware package that matches the model, available on the [Firmware Downloads](../firmware.html) page.

Use the guide for your platform and keep the player charged. If no tool detects the player at all, the fault is likely hardware rather than firmware.

## What to include when you ask for help
  - The model — Y1 or Y2 — printed on the player.
  - What the screen does: nothing, a logo, a boot loop, or the home screen.
  - Whether a computer detects the player as a MediaTek device.
  - The exact Updater message and the package you selected.
  - What you already tried, including any manual tool.

Do not post private tokens or unrelated system files. The [community Discord](https://discord.gg/zHrT2zrcek) and [r/innioasis](https://reddit.com/r/innioasis) are the fastest places to compare notes.

## Innioasis recovery FAQ

### How do I fix an Innioasis player that won't turn on?

Charge it for 30 minutes with a known data cable, force a restart by holding power for 15 seconds, then check whether a computer detects it. If it does, restore the model-matched Original Software; if not, use the manual recovery tools included with Updater CE.

### Why is my Y1 or Y2 scroll wheel not working?

If the wheel stopped after an update, it is usually a firmware mismatch. Reinstall the model-matched Original Software and test again. If the wheel is dead in every firmware, treat it as a hardware fault.

### Where do I download firmware for recovery?

The Firmware Downloads page at innioasis.app/firmware.html hosts original and custom packages for each model. Always pick the Y1 or Y2 package that matches the player.

### What recovery tools are included with Updater CE?

Updater CE includes SP Flash Tool on Windows and Linux, and the MTKClient route including macOS, for manual recovery when the normal install can't finish.

## Related fixes
  - [Y1 scroll wheel not working](y1-scroll-wheel-not-working.html) — click wheel unresponsive after an update
  - [Y2 scroll wheel not working](y2-scroll-wheel-not-working.html) — the same checks for the Y2
  - [Y1 won't turn on](y1-wont-turn-on.html) — charging, restart and manual recovery
  - [Y2 won't turn on](y2-wont-turn-on.html) — the same checks for the Y2
  - [SP Flash Tool guide](../sp-flash-tool.html) — manual flashing on Windows and Linux

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
