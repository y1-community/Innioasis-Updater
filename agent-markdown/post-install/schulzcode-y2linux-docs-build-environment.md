---
title: "Locked offline build environment - Innioasis Updater"
description: "Locked offline build environment <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-environment.html"
---

# Locked offline build environment - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Locked offline build environment

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Locked offline build environment > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Y2B-201 pins upstream Linux v6.18 (`7d0a66e4bb9081d75c82ec4957c50034cb0ea449`) and the official kernel.org release archive in `tools/build/inputs.lock.json`. Archive SHA-256 is `9106a4605da9e31ff17659d958782b815f9591ab308d03b0ee21aad6c7dced4b`; the 31 previously audited source files are checked independently. Checksums were obtained through official HTTPS endpoints; no independent OpenPGP verification is claimed.

The isolated x86_64 userspace is Alpine 3.22.1 plus 64 individually hashed official APK archives (79 installed packages including the base). Its ARM compiler/linker are Clang/LLD 20.1.8; host tools include GCC 14.2.0, GNU Make 4.4.1, Python 3.12.14 and pyelftools 0.32. All package revisions and URLs are in the lock. Host requirements: Linux, Python 3.12 or newer, bubblewrap and enabled unprivileged user namespaces. Neither a Docker daemon nor host package installation is needed.

From the repository root:`python3 tools/build/prepare.py # Fetch exact locked inputs, verify, reconstruct python3 tools/build/prepare.py --offline # Same checks; missing cached inputs fail python3 tools/build/run.py --output out/smoke -- sh /project/tools/build/smoke.sh`

Preparation extracts the checked archive, installs APKs with signature checking and network disabled, and checks the exact package inventory. Absolute rootfs symlinks are converted to equivalent relative links before safe extraction. An incomplete environment or changed lock fails closed; reconstruct in a fresh checkout/cache instead of silently updating packages. The build wrapper checks the lock marker. It mounts sources, project and userspace read-only, exposes only its chosen `out/` directory for persistent writes, uses a private minimal `/dev`, and unshares network and other namespaces. It never exposes the Y2 or host block devices. A surrounding application sandbox may require permission to create these namespaces.

Every invocation sees fixed `/src`, `/project` and `/build` paths, an empty inherited environment, UTC/C locale, source-tag epoch, `KBUILD_BUILD_VERSION=1`, and fixed build metadata recorded in the lock. These build strings do not change Git identity. Source and tool archives, caches and products are ignored by Git. Retain the cache for offline reconstruction; upstream mirrors are not guaranteed to retain packages forever. SHA-256 locks detect substitution, not compromise of the initially trusted publisher.

Validation on 2026-09-08: reconstruction completed using cached archives with networking disabled; all audited kernel sources matched. The smoke object is ELF32 little-endian ARM EABI5, ARMv7/Cortex-A7 in ARM instruction mode. No kernel was built for this checkpoint. Later checkpoints must prove clean-build byte reproducibility and validate the actual ELF/artifact layout against D08.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
