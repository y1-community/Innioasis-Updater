---
title: "Y2Linux working rules - Innioasis Updater"
description: "Y2Linux working rules Before activating, closing or crossing a major milestone boundary, or materially changing hardware/memory/production scope, repeat the roadmap/gap a"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-agents.html"
---

# Y2Linux working rules - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux working rules

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux working rules

Before activating, closing or crossing a major milestone boundary, or materially changing hardware/memory/production scope, repeat the roadmap/gap audit using real hardware evidence and update the roadmap before proceeding. Follow [the standing audit procedure](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23standing-milestone-boundary-rule&anchor=standing-milestone-boundary-rule). Do not treat a planning epic as implementation or hardware authorization.

Use targeted validation for localized changes. Reserve broader qualification for architecture/memory/packaging changes, new hardware subsystems, milestone qualification and release candidates. A documentation-only audit does not build or flash anything and does not repeat unchanged source/ROM/recovery provenance.

Preserve the existing configured Git author/committer identity and authenticated GitHub account. Do not modify identity settings or add model attribution.

Write code to [the coding standard](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCODING-STANDARD.md) (platform and Y2Reborn alike): the platform gate (`tools/development/platform-gate.sh`) must print `GATE OK` before every commit, including its code-quality ratchet (`tools/development/code-quality.py`), which lets nothing get worse.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
