---
title: "Plugins: one kind of package for everything optional - Innioasis Updater"
description: "Plugins: one kind of package for everything optional Status: plan, 2026-10-31. Nothing here is built yet. Applies to Y2Linux platform and Y2Reborn. 1. Why, and the owner'"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-plugins-plan.html"
---

# Plugins: one kind of package for everything optional - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Plugins: one kind of package for everything optional

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Plugins: one kind of package for everything optional

Status: plan, 2026-10-31. Nothing here is built yet. Applies to Y2Linux (platform) and Y2Reborn.

## 1. Why, and the owner's decisions

Users asked for Navidrome sync. It does not belong in Y2Linux, Reborn or the platform, and neither do the next ten requests like it. The answer is plugins: optional packages that users install from a store (or build themselves), so the core stays small, stable and testable.

Decided by the owner (2026-10-31):
  - One unified kind of package. A skin, a set of headphone profiles, internet radio, Last.fm and Navidrome

sync are all the same thing: a signed package that contributes to fixed extension points. One format, one installer, one store, one Add-ons screen, one permission model.
  - Every plugin with code is WebAssembly. No native plugins: not as `.so` files, not as separate native

processes, not even for our own. Plugins are written in Rust (or any language that compiles to WebAssembly) and run in a sandboxed runtime. Plugins without code (skins, profiles, fonts) carry no module at all.
  - Rust everywhere: the host, the contract, the SDK and our plugins.
  - The coding standard ([CODING-STANDARD.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCODING-STANDARD.md)) and its ratchet apply from the first commit.

Still open, with a recommendation: who may publish in the store (§8), whether CJK fonts leave the image (§6).

## 2. The model

A plugin is a package with a manifest, an optional WebAssembly module and optional assets. The manifest declares which extension points it contributes to and which permissions it needs. Reborn and the platform know only the extension points, never a particular plugin.``

| Extension point | What the plugin provides | Code? | Examples |
| --- | --- | --- | --- |
| Look | skin layouts (today's skin format), colours, icons, fonts | no | skins, CJK font |
| Sound | headphone/EQ profiles (today's ParametricEQ format), DSP presets | no | the 47 headphone profiles |
| Source | a browsable catalogue and, per item, something to play or download | yes | internet radio, Navidrome, podcasts |
| Listener | reactions to playback events | yes | Last.fm, ListenBrainz, Navidrome play counts |
| Job | background work under constraints (Wi-Fi, charger, interval) | yes | Navidrome sync, podcast downloads |
| Settings | a settings schema; Reborn draws the form | no (validation optional) | every plugin with options |

A plugin may combine them: Navidrome is Source + Job + Listener + Settings; Last.fm is Listener + Settings; a skin is Look only.

Plugins never draw UI and never touch real-time audio. A Source's catalogue is data (sections, lists, items with artwork and actions); Reborn draws it with its own components, so every plugin looks right in every skin and works with the wheel, search and Customize. Playback is always the core's: a Source hands back a stream URL or a file, never audio samples.

## 3. What the core becomes

Core Reborn keeps exactly what a plugin must never be able to break, plus the machinery for the extension points:
  - Playback engine: decoding (FFmpeg), gapless, crossfade, the EQ/DSP engine, volume, wired and Bluetooth

output, and the stream player (today's radio stream fetcher: curl, ICY stripping, reconnect; FFmpeg has no network protocols). A Source plugin's URL plays through it.
  - Local library: scanner, database, queue, history, session, audiobooks (their chapters and speed are

playback internals). Local music is the one built-in source.
  - UI framework: navigation, components, renderer, input, the skin engine with one default skin, the generic

Source browser, the Add-ons screen, settings forms, the QR code sign-in screen.
  - Device and safety: Wi-Fi, Bluetooth, battery, sleep, storage, updates, diagnostics, error reports (all

platform-backed).
  - The plugin client: the contribution registry and the connection to the plugin host.

Leaving the core:

| Today in the core | Becomes | Size today |
| --- | --- | --- |
| Internet radio: radio-browser.info directory, station search, favourites, logos | Radio plugin (Source) | ≈ 1,700 code lines; the stream player stays |
| Last.fm sign-in, Now Playing, scrobble queue | Last.fm plugin (Listener + Settings) | ≈ 1,300 code lines |
| Automatic time zone (ipapi.co / ipwho.is) | Time zone plugin (Job) | ≈ 150 lines |
| 16 skins | skin plugins (Look); one default stays | 3.5 MB |
| 47 headphone profiles | profile plugins (Sound); a neutral setting stays | 0.2 MB |
| Noto CJK font | font plugin (Look), see §6 | 15.7 MB |

About 7 % of Reborn's code leaves. The bigger gain is that new features never enter the core again, and the core's job becomes a stable, versioned contract instead of an open-ended feature list.

## 4. Architecture` Reborn (UI, playback) ──Unix socket, typed messages──▶ y2-plugin-host (unprivileged user) │ └─ WebAssembly runtime: one instance per plugin │ install / remove / update (platform command) ▼ y2-platform (root): verify signatures, unpack to /data, store client, rollback`
  - `y2-plugin-host`: a separate Rust process (crash isolation from Reborn and the platform), running as its own

user, started by the supervisor. It loads each enabled plugin's module into the runtime, calls its exports and implements the host functions it imports (§5). Event-driven: it sleeps while no plugin has work.
  - Reborn talks to the host over a Unix socket with typed messages (a contract crate, as `y2p-contract` is

for the platform): browse/search/resolve for Sources, playback events for Listeners, settings forms, status. Reborn caches Source pages so browsing never waits on a plugin longer than one request.
  - The platform owns everything privileged: verifying and unpacking packages, the catalog download, updates,

quotas. New commands: `y2-platform plugins list|install|remove|update|enable|disable|catalog`.
  - Where the host lives (decision for P1): in Y2Reborn's workspace (it serves the player; Reborn's supervisor

starts it) with the package/installer side in the platform. The contract crate for Reborn ↔ host follows the `y2p-contract` rules (one copy, synced, checked by the build).

### Files````````

| Path | What | Owner |
| --- | --- | --- |
| /usr/share/y2/plugins/<id>/ | preinstalled plugins (in the image, signed like store plugins) | image |
| /data/plugins/<id>/<version>/ | installed versions (two kept: current and previous) | platform |
| /data/plugin-data/<id>/ | a plugin's private data (settings, secrets, queues), mode 0700 | host user |
| /media/internal/music/<Plugin name>/ | music a Job downloads (the library scans it) | host user |

A store version of a preinstalled plugin overrides it; removing it falls back to the preinstalled one.

## 5. The contract

### Interface

Defined in WIT (WebAssembly Interface Types) as the package `y2:plugin@1.0.0`; the SDK generates the Rust bindings on both sides. Versioning as the platform's contract: additive changes raise the minor version, a host runs every plugin of its major version, a plugin declares the oldest minor it needs.

Exports a plugin may implement (by extension point):
  - Source: `browse(path) -> page` (sections; items with title, subtitle, artwork, kind: container, playable,

station; actions), `search(query) -> page`, `resolve(item) -> playable` (a URL with optional headers, or a file path in its music folder; format hints, duration, metadata).
  - Listener: `on-event(event)` for started, progress, finished, skipped, liked; the host keeps a durable queue

per plugin, so an event survives a restart or a plugin that is busy.
  - Job: `run(trigger) -> outcome`, with progress reported through a host function.
  - Settings: a static schema in the manifest (text, secret, toggle, choice, number, action button, sign-in

with a URL shown as QR code); `validate(values)` optional.

Host functions a plugin may import, each gated by a manifest permission:``````````````````````````

| Import | Permission | Rules |
| --- | --- | --- |
| http.request | network with fixed hosts, or network:user-hosts | HTTPS; plain HTTP only to user-configured LAN hosts (Navidrome at home), with a warning; size, time and rate limits |
| files.* | storage:own-music | only below its music folder, openat without following symlinks (as y2p-core does for the SD card); quota |
| data.*, secrets.get | always (own only) | its own key-value store and secrets |
| library.rescan | library | asks Reborn to scan its music folder |
| status.report | always | progress and messages shown in the Add-ons screen |
| time.now, log | always | — |

### Package

`<id>-<version>.y2plugin`: a tar archive with `manifest.json`, an optional `plugin.wasm`, `assets/`, and `signature` (Ed25519 over the manifest, which lists every file's SHA-256).

Manifest fields: `id` (reverse DNS, e.g. `org.y2linux.radio`), `name`, `version`, `api` (`y2:plugin` version), `author`, `license`, `description`, `contributions`, `permissions`, `limits` (memory, at most the host's cap), `settings`, `min_platform`.

## 6. The core after the move, and the CJK question

Reborn ships one default skin, a neutral sound setting, local music, and the preinstalled plugins Radio and Last.fm (preinstalled so an update from 9.x loses nothing; users can remove them).

CJK font (open): track titles in Chinese, Japanese or Korean need the font in the core UI. Recommendation: make it a plugin, and when the library scan finds a title the default font cannot draw, Reborn offers to install it (with a fallback that shows the title as a code-point box until then). Alternative: keep it in the image.

## 7. Security model

Threats: a malicious plugin, a buggy plugin, a hostile or compromised server a plugin talks to, a compromised store. Layers, inside out:
  - The WebAssembly runtime is the sandbox. A plugin has no system calls, no memory outside its own, no

threads, no files and no network except through host functions. Per instance: a memory cap (default 16 MB), a CPU budget per call (fuel or epoch interruption), a wall-clock timeout.
  - Host functions are the attack surface and are written to the coding standard with tests that include

hostile input (path traversal, symlinks, oversized responses, malformed WIT values) and fuzzing.
  - The host process is a second wall, with what the kernel offers today (checked on the player

2026-10-31: no seccomp, no LSM, no cgroups, only mount namespaces; `no_new_privs`, resource limits and separate users work): its own unprivileged user, `no_new_privs`, `setrlimit` (address space, open files, no child processes), low priority, a private mount namespace showing only its own directories.
  - Kernel hardening later: seccomp for the host, Landlock, cgroup v2 memory/CPU accounting. Kernel

configuration changes, so after a hardware round (memory, sleep); not a precondition.
  - The store signs packages with its own key, never the update key (`platform-v1-release-*` signs only

system updates). Installing shows the permissions; an update that asks for more asks again.

Battery without cgroups: event-driven host, the CPU budget per call, background Jobs only under their declared constraints (Wi-Fi, charger), low priority.

Known separate risk: Reborn and the four platform daemons run as root (checked 2026-10-31). Dropping root where it is not needed is its own hardening project (§10, P6).

## 8. The store
  - Catalog: a signed JSON index (id, versions, sizes, hashes, permissions, screenshots), hosted with the

packages as GitHub release files of a `Y2Plugins` repository. The platform fetches it like the update channel (TLS once the clock is trusted).
  - Review (open, recommendation): only plugins the owner has reviewed are signed and listed. Anyone can

sideload a package from Internal Storage (`Plugins/` folder) after turning on Developer plugins; it runs in the same sandbox, marked unverified.
  - Updates: per plugin, staged and verified, the previous version kept for one rollback. After a system update

a plugin whose `api` major is no longer served is disabled with a message.

## 9. For plugin authors
  - `y2-plugin-sdk` (Rust crate): the generated bindings plus helpers (HTTP, JSON, settings).
  - A template repository and the `y2plugin` CLI: build, package, sign (sideload key), and run on a PC against a

simulated host (the real host code with a fake Reborn), so a plugin can be developed without a player.
  - Documentation: the contract, the permissions, the review checklist.

## 10. Phases

Each phase ends with the gate green, the code-quality ratchet not worse, and the listed checks.``````````

| Phase | Content | Exit |
| --- | --- | --- |
| P0 Spike | choose the runtime on armv7: wasmtime's portable interpreter (Pulley) with the component model, or wasmi (pure Rust, core modules only); prototype host + a plugin doing HTTP and file writes on the player | measured binary size, idle and per-instance RAM, CPU for a sync-like workload, component-model support; decision recorded here |
| P1 Foundation | contract v1 (Look, Sound, Settings), package format and signatures, y2-platform plugins commands, the host process with sandbox layers 1–3, Reborn's Add-ons screen, sideloading | skins and headphone profiles install and remove as plugins; host idle CPU ≈ 0 s/h; application_ready unchanged |
| P2 Sources and Jobs | Source, Job, http, files, library.rescan; Reborn's generic Source browser; Radio rebuilt as a plugin (preinstalled) | radio parity with 9.x (directory, search, favourites, logos, playback, reconnect); then the directory code leaves the core |
| P3 Listeners | Listener with durable queues; Last.fm as a plugin (preinstalled), QR sign-in through Settings | no scrobble lost across restarts and updates; the Last.fm code leaves the core |
| P4 Navidrome | the first plugin outside the core, in its own repository: browse and stream (Source), offline sync (Job), play counts (Listener) | works against a real Navidrome server on Wi-Fi; sync only on Wi-Fi and charger |
| P5 Store and SDK | catalog, store key, review checklist, updates and rollback, SDK, template, CLI, documentation | a plugin goes from template to signed store listing end to end |
| P6 Hardening | kernel features (§7.4) after a hardware round; Reborn and daemons without root where possible | — |

Moving a feature out of the core (P2, P3) keeps its user data: favourites, Last.fm session and queue migrate into the plugin's data directory on first start.

## 11. Measurements every phase reports

Idle CPU (s/h) of the host and Reborn, host and per-plugin RSS, `application_ready`, overnight sleep current with plugins installed, the image size, and the core's code size (`tools/development/code-quality.py`).

## 12. Risks and open questions
  - The runtime on 32-bit ARM (P0): no JIT; interpreter speed and memory decide which runtime, and whether the

component model is available.
  - Memory: one instance per enabled plugin; the cap and the number of active plugins need a budget.
  - The Source browser's expressiveness: radio's On Air card and logos must be expressible as data; the page

model may need a few more item kinds.
  - Support load of third-party plugins: review checklist, clear unverified labelling, crash reports per plugin.
  - Secrets: no secure element; secrets are protected by the host user's file permissions, not encrypted at rest.
  - Last.fm API credentials ship in the plugin as they ship in the image today (extractable either way).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
