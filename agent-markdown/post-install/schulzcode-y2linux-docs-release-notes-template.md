---
title: "Release notes format - Innioasis Updater"
description: "Release notes format The text of a GitHub release release.py publish --notes has two kinds of readers. People on the GitHub release page, and people inside an updater, su"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-release-notes-template.html"
---

# Release notes format - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Release notes format

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Release notes format

The text of a GitHub release (`release.py publish --notes`) has two kinds of readers. People on the GitHub release page, and people inside an updater, such as the community [Innioasis Updater](https://github.com/y1-community/Innioasis-Updater), which shows the same text but downloads and flashes the player itself. Write it for someone who uses the player, not for a developer: what they get, where to find it, what was fixed, what to watch out for. Technical detail belongs in the release report under `docs/validation/`.

Everything that only makes sense on the GitHub page goes between `<!-- github-only -->` and `<!-- /github-only -->`. That covers the update hint for players already on Y2Linux (they offer the update themselves, and an updater user is installing fresh), both ways to install from stock (the Innioasis Updater and SP Flash Tool), how it was tested, the file list and the disclaimer. The updater shows only the title line, What's new, Fixed, Known issues and the report link. Each marker sits on a line of its own with a blank line before and after. GitHub hides the comments, and an updater that knows the markers leaves out what is between them. `release.py publish` refuses notes without balanced markers and wraps the "Sources unchanged" section it adds itself.

## Rules
  - First line: the version in bold and one short phrase of what it brings.
  - What's new and Fixed: one bullet each, the name of the feature in bold, then where to find it on the

player (the real menu path) and what it does for the listener. No internal names, file names or ledger numbers. An issue number only where it helps the person who asked.
  - Known issues: short, with what to do about it. End with error reports and Restore Previous System.
  - Link the plain-words release report.
  - The part updaters show stays under 3800 characters (the Innioasis Updater app cuts at 4000), and no line in it

starts with the word "Changes" (that app hides everything up to such a line). `publish` checks both.
  - GitHub-only part, in this order: Already running Y2Linux (the update path), Install with the Innioasis Updater

(Windows, macOS and Linux; the easiest way from stock), Install with SP Flash Tool, How it was tested, Files, then the beta disclaimer and licences.

## Template`**Y2Linux 1.0 Beta X.Y**: one short phrase. ## What's new - **Feature**: where to find it, and what it does for you. ## Fixed - **What was broken**: what you noticed, and that it works now. ## Known issues - Issue, and what to do about it. - Something wrong? Send an error report (Settings → System → Error Reports). **Restore Previous System** (Settings → System → About, tap Version seven times, then Diagnostics) takes you back to the version you had, with your data kept. More details in plain words: **[Beta X.Y report](https://github.com/SchulzCode/Y2Linux/blob/main/docs/validation/Y2-LINUX-1.0-BETA-X.Y.md)**. `

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
