---
title: "Knowledge-base authority and maintenance - Innioasis Updater"
description: "Knowledge-base authority and maintenance <!-- knowledge-base-scope: maintained; baseline02-sync 2026-10-03 -- Current authority map — Baseline02, 2026-10-03 The Baseline0"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge_base.html"
---

# Knowledge-base authority and maintenance - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Knowledge-base authority and maintenance

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Knowledge-base authority and maintenance

## Current authority map — Baseline02, 2026-10-03

The [Baseline02 seal](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md) identifies compiled Linux `8584ccd85f052f351fe51650b2348c83ca894ed4` and Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`. Later documentation HEADs and published `main` are separate identities. The [UART01 physical receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) proves bounded C1/C2/C3 behavior on Linux `e9e8d63f9c94232c2b6627881e0967583e202dac`; it does not qualify Baseline02's new automatic cold boot. Baseline02 is sealed, software-tested and PHYSICAL_NOT_RUN. Current summaries, feature JSON, release plan, contracts and navigation follow that distinction; historical receipts and raw captures retain their original claims.

This synchronization uses retained evidence only. Private `out/` paths are literal local references, not public hyperlinks. Source delivery now includes paired source tar archives and locked upstream archives; reconstruction and legal collection do not establish byte-identical rebuild or distribution permission. See [source delivery](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-COMMUNITY-SOURCE-DELIVERY.md).

This repository and adjacent Y2Reborn describe one product. Start with [platform state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md) and [application state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2FCURRENT_REBORN_STATE.md). The complete [Linux catalog](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FDOCUMENTATION_CATALOG.md) and [Reborn catalog](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2FDOCUMENTATION_CATALOG.md) cover retained pages.

## Authority order
  - Exact-image physical receipts for what actually happened on that device.
  - Current state/capability summaries derived from those receipts.
  - Current production source/configuration for implemented/enabled behavior.
  - Exact-pair build/software checks for their stated validation tier.
  - Historical source research, candidate records and proposals within their dates.

PASS applies to the stated bounded behavior. FAIL, PARTIAL and NOT_TESTED remain distinct. No source test, enabled configuration, new boot or merge to main certifies full same-boot restoration or production readiness. Report measured, configured, estimated and unavailable values separately. Never turn invalid SRAM record fields into real register readings or USB presence into active charging.

## Update procedure

After a new implementation or physical result, update both current-state pages, affected maintained contracts/knowledge summaries, capability ledger and roadmap. Link exact commits/kernel/root/boot/evidence and state the scope that supersedes an earlier result. Keep earlier observations, failures and identities intact. Before a milestone/hardware/memory/production boundary follow the [standing audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23standing-milestone-boundary-rule&anchor=standing-milestone-boundary-rule). Documentation maintenance itself performs no build, flash or new hardware test.

Use the catalogs to find every document. Maintained contracts describe source ownership, historical notices bound old task/permission statements, and raw hardware/build evidence is preserved without textual edits. Asset references remain design material, not running-screen or hardware proof. Keep existing paths stable; replace missing private-artifact hyperlinks with literal paths and explain their local-only availability. Do not delete history to hide defects.

## Repository boundaries

Publish reviewed summaries and source. Keep `out/`, caches, generated candidates, raw private captures, owner radio firmware, keys, bonds, calibration and NVRAM local. Do not clean these as if they were disposable documentation clutter. Preserve fallback images/checksums and reserved memory/loader/storage boundaries. Do not prune other worktrees or change Git identity during knowledge cleanup.

`main` names published/integrated source; owner-local candidate branches may be newer. Baseline02 compiled Linux `8584ccd8` / Reborn `b71b4688` identify its images; later documentation revisions do not change those bytes. Documentation HEADs can advance without changing an installed candidate. Static catalogs should be refreshed when adding/retiring a page. Check local links and heading anchors with `python3 tools/development/check-docs.py` from Y2Linux, and run `git diff --check` for documentation changes; do not rebuild unchanged platform binaries.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
