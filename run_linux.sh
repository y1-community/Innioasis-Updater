#!/usr/bin/env bash
# Innioasis Updater CE - Linux launcher
#
# Installs the rewritten Innioasis Updater from the latest release, or runs it
# without installing. No sudo, no system packages, no Python.
#
#   bash run_linux.sh              choose from the menu
#   bash run_linux.sh install      install the app
#   bash run_linux.sh run          run once, in a window
#   bash run_linux.sh tui          run once, in the terminal interface
#
# A session started here stays in the foreground and keeps the terminal, which
# is what the --tui interface needs. Starting it in the background with nohup
# and the output sent to /dev/null left the interface attached to nothing: it
# printed the firmware list and the main screen, then exited.
#
# The AppImage comes from y1-community/innioasis-updater first, so first
# downloads and upgrades stay separately countable. The portable .tar.gz and
# .zip come from y1-community/updater-ce-neo, which owns the portable packages.

set -u

PRIMARY_REPO="y1-community/innioasis-updater"
PORTABLE_REPO="y1-community/updater-ce-neo"
SITE="https://innioasis.app/guide.html"
APP_NAME="Innioasis Updater"

say() { printf '%s\n' "$*"; }
fail() { printf '\n%s\n\nOpen %s to download the app.\n' "$*" "$SITE"; }

pause() {
    [ -t 0 ] && { printf '\nPress Enter to close.'; read -r _; }
}

# Reconnect to the terminal when this script is piped from curl.
if [ ! -t 0 ] && [ -r /dev/tty ]; then
    exec </dev/tty
fi

MODE="${1:-}"
case "$MODE" in
    "" | install | run | tui) ;;
    -h | --help | help)
        say "$APP_NAME"
        say ""
        say "  bash run_linux.sh            choose from the menu"
        say "  bash run_linux.sh install    install it on this computer"
        say "  bash run_linux.sh run        run once, in a window"
        say "  bash run_linux.sh tui        run once, in the terminal interface"
        exit 0
        ;;
    *)
        say "Unknown option: $MODE"
        say "Use install, run, tui, or no option at all."
        pause
        exit 2
        ;;
esac

case "$(uname -m 2>/dev/null)" in
    x86_64 | amd64) ARCH="x64" ;;
    aarch64 | arm64) ARCH="arm64" ;;
    *)
        fail "This computer's processor is not supported by the ready-made builds."
        pause
        exit 1
        ;;
esac

download() {
    # download URL DESTINATION
    if command -v curl >/dev/null 2>&1; then
        curl -fL --retry 2 --connect-timeout 15 --progress-bar -o "$2" "$1"
    elif command -v wget >/dev/null 2>&1; then
        wget -q --show-progress -O "$2" "$1"
    else
        return 1
    fi
}

url_ok() {
    if command -v curl >/dev/null 2>&1; then
        curl -fsIL --connect-timeout 12 -o /dev/null "$1" >/dev/null 2>&1
    else
        wget --spider -q -T 12 "$1" >/dev/null 2>&1
    fi
}

asset_url() {
    # asset_url REPO NAME... -> first asset that exists
    local repo="$1"
    shift
    local name url
    for name in "$@"; do
        url="https://github.com/${repo}/releases/latest/download/${name}"
        if url_ok "$url"; then
            printf '%s\n' "$url"
            return 0
        fi
    done
    return 1
}

resolve_appimage() {
    local names
    if [ "$ARCH" = "arm64" ]; then
        names="UpdaterCE-arm64.appimage UpdaterCE-arm64.AppImage"
    else
        names="UpdaterCE.appimage UpdaterCE.AppImage"
    fi
    # shellcheck disable=SC2086
    asset_url "$PRIMARY_REPO" $names || asset_url "$PORTABLE_REPO" $names
}

resolve_zip() {
    local names
    if [ "$ARCH" = "arm64" ]; then
        names="UpdaterCE-Linux-Portable-arm64.zip Updater-CE-Linux-Portable-arm64.zip"
    else
        names="UpdaterCE-Linux-Portable.zip Updater-CE-Linux-Portable.zip"
    fi
    # shellcheck disable=SC2086
    asset_url "$PORTABLE_REPO" $names || asset_url "$PRIMARY_REPO" $names
}

resolve_targz() {
    local names
    if [ "$ARCH" = "arm64" ]; then
        names="UpdaterCE-Linux-Portable-arm64.tar.gz Updater-CE-Linux-Portable-arm64.tar.gz"
    else
        names="UpdaterCE-Linux-Portable.tar.gz Updater-CE-Linux-Portable.tar.gz"
    fi
    # shellcheck disable=SC2086
    asset_url "$PORTABLE_REPO" $names || asset_url "$PRIMARY_REPO" $names
}

write_desktop_entry() {
    local exec_path="$1"
    local desktop_dir="$HOME/.local/share/applications"
    mkdir -p "$desktop_dir" 2>/dev/null || return 0
    cat >"$desktop_dir/innioasis-updater-ce.desktop" <<EOF
[Desktop Entry]
Type=Application
Name=$APP_NAME
Comment=Firmware updates for Innioasis players
Exec="$exec_path"
Terminal=false
Categories=Utility;
Icon=system-software-update
EOF
    if command -v update-desktop-database >/dev/null 2>&1; then
        update-desktop-database "$desktop_dir" >/dev/null 2>&1 || true
    fi
}

fuse_ok() {
    [ -e /dev/fuse ] && { command -v fusermount3 >/dev/null 2>&1 || command -v fusermount >/dev/null 2>&1; }
}

install_appimage() {
    local url dest launcher flag
    url=$(resolve_appimage) || return 1
    dest="$HOME/.local/bin/Innioasis-Updater.AppImage"
    launcher="$HOME/.local/bin/innioasis-updater"
    mkdir -p "$HOME/.local/bin" 2>/dev/null || return 1
    say "Downloading $APP_NAME…"
    download "$url" "$dest.part" || { rm -f "$dest.part"; return 1; }
    mv -f "$dest.part" "$dest" || return 1
    chmod +x "$dest" 2>/dev/null || true
    if fuse_ok; then
        flag=""
    else
        flag=" --appimage-extract-and-run"
    fi
    cat >"$launcher" <<EOF
#!/bin/sh
exec "$dest"$flag "\$@"
EOF
    chmod +x "$launcher" 2>/dev/null || true
    write_desktop_entry "$launcher"
    say "Installed. Open $APP_NAME from your app menu."
    return 0
}

# Find the application inside an unpacked folder and print its path.
find_app_exe() {
    find "$1" -maxdepth 3 -type f \
        \( -name "Innioasis Updater" -o -name "Innioasis-Updater" -o -name "UpdaterCE" -o -name "innioasis-updater" -o -name "innioasis-updater-ce" \) \
        -print -quit 2>/dev/null
}

unpack_archive() {
    # unpack_archive ARCHIVE DESTINATION
    local archive="$1" destination="$2"
    case "$archive" in
        *.tar.gz | *.tgz)
            if command -v tar >/dev/null 2>&1; then
                tar -xzf "$archive" -C "$destination" >/dev/null 2>&1 || true
            elif command -v python3 >/dev/null 2>&1; then
                python3 -m tarfile -e "$archive" "$destination" >/dev/null 2>&1 || true
            fi
            ;;
        *)
            if command -v unzip >/dev/null 2>&1; then
                unzip -q "$archive" -d "$destination" >/dev/null 2>&1 || true
            elif command -v python3 >/dev/null 2>&1; then
                python3 -m zipfile -e "$archive" "$destination" >/dev/null 2>&1 || true
            fi
            ;;
    esac
}

# Collapse a single top-level folder so the application is easy to find.
flatten_single_folder() {
    local staging="$1" only
    if [ "$(find "$staging" -mindepth 1 -maxdepth 1 | wc -l)" = "1" ]; then
        only=$(find "$staging" -mindepth 1 -maxdepth 1)
        if [ -d "$only" ]; then
            mv "$only"/* "$staging"/ 2>/dev/null || true
            rmdir "$only" 2>/dev/null || true
        fi
    fi
}

install_portable_folder() {
    # The tarball first, then the zip: both are the same folder in a different wrapper.
    local url work target staging exe
    work=$(mktemp -d 2>/dev/null) || return 1
    target="$HOME/.local/share/innioasis-updater-ce"
    staging="$target.part"

    if url=$(resolve_targz); then
        say "Downloading $APP_NAME…"
        if download "$url" "$work/app.tar.gz"; then
            rm -rf "$staging" 2>/dev/null
            mkdir -p "$staging" 2>/dev/null || { rm -rf "$work"; return 1; }
            unpack_archive "$work/app.tar.gz" "$staging"
        fi
    fi

    if [ ! -e "$staging" ] || [ -z "$(find "$staging" -mindepth 1 -maxdepth 1 2>/dev/null)" ]; then
        url=$(resolve_zip) || { rm -rf "$work" "$staging"; return 1; }
        say "Downloading $APP_NAME…"
        if ! download "$url" "$work/app.zip"; then
            rm -rf "$work" "$staging"
            return 1
        fi
        rm -rf "$staging" 2>/dev/null
        mkdir -p "$staging" 2>/dev/null || { rm -rf "$work"; return 1; }
        unpack_archive "$work/app.zip" "$staging"
    fi
    rm -rf "$work"

    flatten_single_folder "$staging"
    exe=$(find_app_exe "$staging")
    if [ -z "$exe" ]; then
        rm -rf "$staging"
        return 1
    fi
    chmod +x "$exe" 2>/dev/null || true
    rm -rf "$target" 2>/dev/null
    mv "$staging" "$target" 2>/dev/null || { rm -rf "$staging"; return 1; }
    exe="$target/${exe#"$staging"/}"
    mkdir -p "$HOME/.local/bin" 2>/dev/null || true
    cat >"$HOME/.local/bin/innioasis-updater" <<EOF
#!/bin/sh
exec "$exe" "\$@"
EOF
    chmod +x "$HOME/.local/bin/innioasis-updater" 2>/dev/null || true
    write_desktop_entry "$HOME/.local/bin/innioasis-updater"
    say "Installed. Open $APP_NAME from your app menu."
    return 0
}

install_app() {
    if install_appimage; then
        return 0
    fi
    say "The AppImage is unavailable. Using the portable package instead."
    if install_portable_folder; then
        return 0
    fi
    fail "The download could not be completed."
    return 1
}

# Download the matching build into a temporary folder and print its path.
fetch_run_copy() {
    # fetch_run_copy KIND -> prints the unpacked application path
    local kind="$1" url work dest exe
    work=$(mktemp -d 2>/dev/null) || return 1
    if [ "$kind" = "appimage" ]; then
        if url=$(resolve_appimage); then
            dest="$work/Innioasis-Updater.AppImage"
            say "Downloading $APP_NAME…"
            if download "$url" "$dest"; then
                chmod +x "$dest" 2>/dev/null || true
                printf '%s\n' "$dest"
                return 0
            fi
        fi
        rm -rf "$work"
        return 1
    fi

    if url=$(resolve_targz); then
        say "Downloading $APP_NAME…"
        if download "$url" "$work/app.tar.gz"; then
            mkdir -p "$work/app"
            unpack_archive "$work/app.tar.gz" "$work/app"
        fi
    fi
    if [ -z "$(find "$work/app" -mindepth 1 -maxdepth 1 2>/dev/null)" ] && url=$(resolve_zip); then
        say "Downloading $APP_NAME…"
        if download "$url" "$work/app.zip"; then
            mkdir -p "$work/app"
            unpack_archive "$work/app.zip" "$work/app"
        fi
    fi
    flatten_single_folder "$work/app"
    exe=$(find_app_exe "$work/app")
    if [ -z "$exe" ]; then
        rm -rf "$work"
        return 1
    fi
    chmod +x "$exe" 2>/dev/null || true
    printf '%s\n' "$exe"
}

# The terminal interface. exec keeps this shell's terminal, which is what
# launcher.py --tui reads from and writes to. The temporary folder is left for
# the session to use and cleaned by the system.
run_tui() {
    local app
    app=$(fetch_run_copy appimage) || app=$(fetch_run_copy folder) || {
        fail "The download could not be completed."
        return 1
    }
    say "$APP_NAME is starting. Press q in the interface to come back here."
    case "$app" in
        *.AppImage | *.appimage)
            if fuse_ok; then
                exec "$app" --tui
            else
                exec "$app" --appimage-extract-and-run --tui
            fi
            ;;
        *)
            exec "$app" --tui
            ;;
    esac
}

# The window. A GUI has no use for this terminal, so it is started detached.
run_window() {
    local app
    app=$(fetch_run_copy appimage) || app=$(fetch_run_copy folder) || {
        fail "The download could not be completed."
        return 1
    }
    if [ -n "${DISPLAY:-}" ] || [ -n "${WAYLAND_DISPLAY:-}" ]; then
        (nohup "$app" >/dev/null 2>&1 &) 2>/dev/null
        say "$APP_NAME is starting."
        return 0
    fi
    say "No desktop session was found. Starting the terminal interface instead."
    case "$app" in
        *.AppImage | *.appimage)
            if fuse_ok; then
                exec "$app" --tui
            else
                exec "$app" --appimage-extract-and-run --tui
            fi
            ;;
        *)
            exec "$app" --tui
            ;;
    esac
}

choose_from_menu() {
    printf '\n%s\n\n' "$APP_NAME"
    printf '  1) Install it on this computer\n'
    printf '  2) Run it once in the terminal\n'
    printf '  3) Run it once in a window\n'
    printf '  4) Quit\n\n'
    printf 'Choose 1-4: '
    read -r choice
    case "$choice" in
        1) install_app ;;
        2) run_tui ;;
        3) run_window ;;
        *) say "Nothing changed." ;;
    esac
}

case "$MODE" in
    install) install_app ;;
    run) run_window ;;
    tui) run_tui ;;
    *) choose_from_menu ;;
esac

pause
