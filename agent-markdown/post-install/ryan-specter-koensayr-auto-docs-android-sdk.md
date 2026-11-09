---
title: "Android SDK setup - Innioasis Updater"
description: "Android SDK setup The Android SDK is required only for the --avrcp flag, which builds src/Y1Bridge/ via Gradle. Gradle itself is bootstrapped by the in-tree wrapper src/Y"
language: "en"
source: "https://innioasis.app/post-install/ryan-specter-koensayr-auto-docs-android-sdk.html"
---

# Android SDK setup - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y1&software=koensayr-y1)

Post-install setup · Koensayr · Y1

# Android SDK setup

A Y1 custom Software maintained by the community.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y1&software=koensayr-y1)[Install guide](../guide.html?model=Y1&software=koensayr-y1)

# Android SDK setup

The Android SDK is required only for the `--avrcp` flag, which builds `src/Y1Bridge/` via Gradle. Gradle itself is bootstrapped by the in-tree wrapper (`src/Y1Bridge/gradlew`) — no separate Gradle install needed — but the wrapper still needs the SDK to compile against and locate `aapt` / `d8` / etc.

This project (apply.bash flash flow) is Linux-only, so all instructions below target Linux. There is no Linux distribution package for the Android SDK (Google's licensing prevents redistribution, so it's not in DNF / APT / EPEL / RPMFusion). Everything below ends up at the same end state: an SDK directory containing `cmdline-tools/`, `platform-tools/`, `platforms/android-34/`, and `build-tools/34.0.0/`, with `ANDROID_HOME` pointing at it (or `sdk.dir` set in `src/Y1Bridge/local.properties`).

## Easy path: `tools/install-android-sdk.sh`

The repo provides an idempotent installer that downloads and provisions everything:`./tools/install-android-sdk.sh`

It will:
  - Detect an existing SDK at `$ANDROID_HOME` or `tools/android-sdk/` — if either is usable (has `platforms/android-34/`), reuse it without re-downloading.
  - Otherwise: download Google's `commandlinetools-linux-XXXXXXX_latest.zip` (pinned build) into `tools/android-sdk/cmdline-tools/latest/`, accept licenses (`yes | sdkmanager --licenses` — running this script is your acceptance, see the script header), install `platforms;android-34` + `build-tools;34.0.0` + `platform-tools`.
  - Always (re-runnable / heals partial-state from prior runs):
    - Write `sdk.dir=<path>` into `src/Y1Bridge/local.properties` so Gradle finds the SDK without `ANDROID_HOME` in your shell.
    - Write `tools/android-sdk-env.sh` (sourceable). Contains `export ANDROID_HOME=…; export PATH=…:cmdline-tools/latest/bin:platform-tools`. Source it (`source tools/android-sdk-env.sh`) when you want `adb` / `sdkmanager` on PATH for interactive shell use. Gradle doesn't need this — it reads `local.properties` directly.

Disk: ~1.5–2 GB. Network: ~1.7 GB total. JDK 17+ is a prereq (the script bails early with install instructions if it's missing).

The two outputs serve different consumers:````````````

| File | Read by | Required for |
| --- | --- | --- |
| src/Y1Bridge/local.properties | Gradle (build time) | ./gradlew assembleDebug |
| tools/android-sdk-env.sh | Your interactive shell (after source …) | adb shell …, sdkmanager --list_installed, etc. |

If you want `ANDROID_HOME` persisted across shells, append the contents of `tools/android-sdk-env.sh` to your `~/.bashrc` / `~/.zshrc`.

Bumping the pinned cmdline-tools build: edit `CMDLINE_TOOLS_BUILD` at the top of `tools/install-android-sdk.sh`, `rm -rf tools/android-sdk/`, re-run.

Everything below is the manual fallback: how to install the SDK by hand if the script doesn't fit your situation (existing system-wide install you'd rather configure, supply-chain policy that doesn't allow scripted downloads, etc.).

## Components needed for this project``````````````````

| Component | Why |
| --- | --- |
| platforms;android-34 | compileSdk 34 in src/Y1Bridge/app/build.gradle |
| build-tools;34.0.0 | AGP 9.2.0 invokes aapt2, d8, zipalign from this version |
| platform-tools | adb for device interaction. Optional for building, mandatory for the post-flash verification steps. |

Total fresh install (cmdline-tools + the three components above): ~1.5–2 GB before Gradle pulls its own dependency cache (another ~500 MB on first `./gradlew assembleDebug`).

## Already have it?

Skip ahead if these already work:`echo "$ANDROID_HOME" # should print a path ls "$ANDROID_HOME/platforms/android-34" # should list non-empty ls "$ANDROID_HOME/build-tools/34.0.0" # should list non-empty "$ANDROID_HOME/cmdline-tools/latest/bin/sdkmanager" --version # should print a version`

If `ANDROID_HOME` is unset but Android Studio is installed, the SDK is typically at `~/Android/Sdk` — set `ANDROID_HOME` to that path and you're done.

## Manual install (Rocky / Alma / RHEL / Fedora / Debian / Ubuntu / Arch)

Same steps regardless of distro — the cmdline-tools are platform-agnostic Java + scripts, distributed only by Google.`# 1. Download the standalone cmdline-tools (~150 MB). # Browse https://developer.android.com/studio#command-tools and grab the # "Command line tools only" Linux zip. mkdir -p ~/Android/Sdk/cmdline-tools cd ~/Android/Sdk/cmdline-tools unzip ~/Downloads/commandlinetools-linux-*_latest.zip # 2. Move into the canonical layout. sdkmanager expects to live at # cmdline-tools/latest/bin/sdkmanager, NOT cmdline-tools/cmdline-tools/... mv cmdline-tools latest # 3. Install the components. Accept licenses when prompted (or run # `yes | ~/Android/Sdk/cmdline-tools/latest/bin/sdkmanager --licenses`). ~/Android/Sdk/cmdline-tools/latest/bin/sdkmanager \ --install "platforms;android-34" "build-tools;34.0.0" "platform-tools" # 4. Persist ANDROID_HOME (bash; for zsh use ~/.zshrc, fish use ~/.config/fish/config.fish). cat >> ~/.bashrc <<'EOF' export ANDROID_HOME=$HOME/Android/Sdk export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools EOF source ~/.bashrc`

## JDK requirement

Gradle (this doc's setup): JDK 17 minimum. Confirmed working: JDK 17, 21, and 25 with the in-tree AGP 9.2.0 + Gradle 9.5.0.

`patch_y1_apk.py` (invoked under `--music-apk`, and by extension `--all`): JDK 11–21 only. apktool 2.9.3's bundled smali assembler silently drops patches on Java 22+, so the patcher warns on a newer JDK and its DEX-signature check will fail. If you only have JDK 22+ installed, install a 17 or 21 alongside it and point `JAVA_HOME` at the older one before running `--music-apk`.

Install whatever you prefer (within the appropriate range):
  - Rocky / Alma / RHEL / Fedora: `sudo dnf install -y java-17-openjdk-devel` (or `java-21-openjdk-devel`)
  - Debian / Ubuntu: `sudo apt install -y openjdk-17-jdk` (or `openjdk-21-jdk`)
  - Arch: `sudo pacman -S jdk17-openjdk` (or `jdk21-openjdk`)

The `-devel` (Rocky/Fedora) / `-jdk` (Debian) package suffix matters — the plain `java-N-openjdk` / `openjdk-N-jre` packages ship the JRE only, no `javac`. Gradle reports `Toolchain ... does not provide the required capabilities: [JAVA_COMPILER]` if you only have the JRE. Install the dev/JDK variant.`# Adjust path per distro; example for Rocky/Fedora with JDK 25: export JAVA_HOME=/usr/lib/jvm/java-25-openjdk $JAVA_HOME/bin/javac -version # verify: javac 25.x.x # Persist for new shells: echo 'export JAVA_HOME=/usr/lib/jvm/java-25-openjdk' >> ~/.bashrc`

Gotcha — gradle daemon caching: Gradle keeps its build daemon alive across invocations. If you change `JAVA_HOME` (or upgrade the underlying JDK install) after a build has run, the cached daemon keeps the old JVM. You'll get the same `[JAVA_COMPILER]` error even though the new `JAVA_HOME` is fine. Stop the daemon before rebuilding:`( cd src/Y1Bridge && ./gradlew --stop && ./gradlew assembleDebug )`

`./gradlew --version` shows the current daemon JVM under `Daemon JVM:`; if that doesn't match your `JAVA_HOME`, run `--stop`.

## Verify the install

After the steps above, in a fresh shell:`echo $ANDROID_HOME # → your SDK path sdkmanager --list_installed # → lists platforms;android-34, build-tools;34.0.0, platform-tools java -version # → 17 or newer ( cd src/Y1Bridge && ./gradlew --version ) # → Gradle 9.5.0, JVM 17+`

If those four pass, `./apply.bash --avrcp` will resolve the SDK and Gradle correctly (with `rom.zip` staged in `staging/` or pointed at via `--artifacts-dir <path>`).

## License acceptance

`sdkmanager --install …` will prompt to accept Google's licenses on first run. To accept up-front (e.g. in a script), use:`yes | sdkmanager --licenses`

The licenses live at `$ANDROID_HOME/licenses/` after acceptance — back them up if you want to short-circuit license re-acceptance on a fresh machine.

## Bumping the SDK pins

If the project bumps `compileSdk` or AGP:
  - Update the corresponding pin in `src/Y1Bridge/app/build.gradle` (`compileSdk`).
  - Re-run `sdkmanager --install "platforms;android-XX" "build-tools;XX.Y.Z"`.
  - Update the Components needed table at the top of this file.

These are Koensayr's own instructions, shown here word for word.

Published by the [ryan-specter/koensayr-auto](https://innioasis.app/firmware.html?model=Y1&software=koensayr-y1) project [[1]](https://innioasis.app/firmware_info.html?repo=ryan-specter%2Fkoensayr-auto&software=koensayr-y1)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aryan-specter)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
