---
title: "Innioasis Updater troubleshooting | Innioasis and Timmkoo install problems - Innioasis Updater"
description: "Fix Innioasis Updater installs on any Innioasis or Timmkoo player. Check the model, cable, driver, power-off timing, and where the install stopped — then get it flashing again."
language: "bn"
source: "https://innioasis.app/troubleshooting_bn.html"
---

# Innioasis Updater troubleshooting | Innioasis and Timmkoo install problems - Innioasis Updater

সমস্যা সমাধান

# Find the point where the install stopped.

Where did it stop? That tells you what to fix.[Return to the normal guide](guide_bn.html)[Check firmware](firmware_bn.html)

## It stopped before the USB prompt

This is a computer problem, not a cable problem. Check your model. Unpack the file again. Then try ইনস্টল / পুনরুদ্ধার. If the release list is empty, open the [firmware directory](firmware_bn.html).

## It cannot connect to the player
  - Fully power off the correct Y1 or Y2.
  - Unplug the cable, close other flash or Android tools, and start the install again.
  - Connect only when Updater says it is ready.
  - Use a short USB data cable directly in the computer, not a hub if possible.
  - On Windows, reinstall the MediaTek driver and restart. On Linux, check USB/serial permissions.
Updater connection promptThe live Updater prompt is authoritative for the current model and platform.

## It detected the player but the flash failed

Stop here. Do not try a different model. Close other tools, check you picked the right Y1 or Y2, and use the matching Original Software if the player will not start. [SP Flash Tool](sp-flash-tool_bn.html) and MTKClient are included if you need them, and the files are on the [firmware page](firmware_bn.html).

## Windows driver notes

Some Windows installations block the MediaTek driver because of Core isolation. Follow the current Windows security guidance before changing Memory integrity, and turn it back on when you are finished if your system allows it.[Open driver guide](drivers_bn.html)[Clean install guide](Troubleshooting/clean_install.html)

## Wheel not working, or the player will not start

Input and power faults need different steps from a failed flash. These guides cover the common Y1 and Y2 cases.[Y1 scroll wheel](guides/y1-scroll-wheel-not-working.html)[Y2 scroll wheel](guides/y2-scroll-wheel-not-working.html)[Y1 চালু হবে না](guides/y1-wont-turn-on.html)[Y2 চালু হবে না](guides/y2-wont-turn-on.html)[পুনরুদ্ধারের নির্দেশিকা](guides/recovery.html)

## Still stuck?

When asking for help, include the model, operating system, exact Updater message, whether the player was detected, and the package/project you selected. Do not post private tokens or unrelated system files.[Ask for help](https://discord.gg/zHrT2zrcek)[Support maintenance](support_devs_bn.html#donations)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
