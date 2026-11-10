# Terminal mode, TUI and the streamed lite install

These modes are for developers and for machines that cannot open the window.
They are not linked from the public pages.

## Entry points

| Command | What it does |
| --- | --- |
| `UpdaterCE.AppImage` / tarball / zip | Normal window |
| `UpdaterCE.AppImage --tui` | Terminal interface in the same bundle |
| `UpdaterCE.AppImage --cli <command>` | Scriptable commands, no Qt |
| `innioasis-updater-lite` | Installed by `run_linux_lite.sh`, Python only |
| `curl -fsSLO https://innioasis.app/run_linux_lite.sh && sh run_linux_lite.sh` | Streamed install (resumable) |

When Linux has no `DISPLAY`/`WAYLAND_DISPLAY`, or Qt cannot load the xcb plugin,
the launcher starts the TUI instead of aborting. The window remains the default
wherever a display exists, on every platform.

## Commands

```sh
--cli list [--model Y1] [--json]
--cli download <model> [--output DIR] [--extract]
--cli flash <unpacked-folder> [--dry-run]
--cli adb devices
--cli components [list|fetch|prefetch]
--cli doctor [--json]
--cli tui
```

`--json` gives one JSON object per line, which is what an agent or a script
uses: `list` → `download` → `flash --dry-run` → `flash`.

## Components

The window build bundles SP Flash Tool, adb and unrar. A streamed lite session
carries none of them: 200 MB is not a reasonable start-up cost for a Pi Zero.
`src/console/components.py` resolves a tool in this order:

1. inside the session (AppImage payload, extracted tarball/zip, source tree),
2. a previous component download in
   `~/.local/share/innioasis-updater/components`,
3. the published archive (same release URLs the window build uses, plus
   Google's official platform-tools), with progress and cleanup.

Downloads happen between tasks, when a task first needs the tool: adb before an
adb command, SP Flash Tool before the first install that offers it. Nothing is
fetched at menu time. If `components.measure_mbps()` reports more than 60 Mbps,
the TUI prefetches the session's tools; set `INNIOASIS_NO_PREFETCH=1` to keep
even a fast session lazy.

SP Flash Tool has no console mode; MTKClient's `mtk wl` is the console flashing
engine, and SP Flash Tool is fetched for sessions that will hand over to a
desktop.

## Platform support

The console package imports only the standard library, so it runs on Linux,
macOS and Windows, including 32-bit x86 and 32-bit ARM where no PySide6 wheel
exists. Flashing tools themselves remain platform-specific: MTKClient via pip,
adb from platform-tools, SP Flash Tool for x86_64 Linux/Windows.

## Build and release

```sh
python3 scripts/build_lite_payload.py --out dist/linux-lite \
    --site-dir ../Innioasis-Updater
```

`build_appimage.sh` runs it for every release. The payload is architecture
independent (17 KB) and checksummed. `run_linux_lite.sh --check` reports what a
machine has; `--update` and `--uninstall` maintain an install.

## Verification

- `scripts/verify_linux_runtime.py` rejects a bundle that needs glibc newer
  than 2.35, bundles Python newer than 3.12, is missing an xcb client library,
  or contains SSE4.2/POPCNT/AVX instructions (PySide6 6.10+).
- `.github/workflows/linux-distros.yml` starts the published build under
  Ubuntu 22.04, Debian 12, Fedora 40, openSUSE Leap 15.6 and Arch.
