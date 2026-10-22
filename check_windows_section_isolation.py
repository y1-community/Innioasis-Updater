#!/usr/bin/env python3
"""Confirm the edits landed in the Windows download card and did not touch the
macOS, Linux, or “Another platform?” markup."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
GUIDE = "guide.html"
GUIDE_FIRMWARE = "firmware-guide.html"

WINDOWS_CARD_START = "class=\"lumen-download-option\" id=\"windows\""
MACOS_CARD_START = "class=\"lumen-download-option\" id=\"macos\""
LINUX_CARD_START = "class=\"lumen-download-option\" id=\"linux\""
ANOTHER_PLATFORM = "data-another-platform"


def card_text(page: str, start_marker: str, end_marker: str) -> str:
    body = Path(page).read_text("utf-8", "ignore")
    start = body.find(start_marker)
    if start == -1:
        raise SystemExit(f"{page} missing {start_marker!r}")
    end = body.find(end_marker, start)
    if end == -1:
        raise SystemExit(f"{page} missing end marker {end_marker!r} after windows card")
    return body[start:end]


def main() -> None:
    guide_win = card_text(GUIDE, WINDOWS_CARD_START, MACOS_CARD_START)
    firmware_win = card_text(
        GUIDE_FIRMWARE, WINDOWS_CARD_START, MACOS_CARD_START
    )
    guide_mac = card_text(GUIDE, MACOS_CARD_START, LINUX_CARD_START)
    firmware_mac = card_text(
        GUIDE_FIRMWARE, MACOS_CARD_START, LINUX_CARD_START
    )

    for label, win_block in ((GUIDE, guide_win), (GUIDE_FIRMWARE, firmware_win)):
        if "Download App and Drivers" not in win_block:
            raise SystemExit(f"{label} Windows card must contain the renamed button")
        if DRIVER_BUTTON_HTML in win_block:
            raise SystemExit(
                f"{label} Windows card still contains the removed Drivers button"
            )

    for label, mac_block in ((GUIDE, guide_mac), (GUIDE_FIRMWARE, firmware_mac)):
        if "Download Homebrew" not in mac_block:
            raise SystemExit(f"{label} macOS card must still contain Download Homebrew")
        if "Download Updater CE</a>" not in mac_block:
            raise SystemExit(f"{label} macOS card must still contain Download Updater CE")

    for page in (GUIDE, GUIDE_FIRMWARE):
        body = Path(page).read_text("utf-8", "ignore")
        if ANOTHER_PLATFORM not in body:
            raise SystemExit(f"{page} must still contain {ANOTHER_PLATFORM!r}")

    required_mac_urls = (
        "https://github.com/Homebrew/brew/releases/latest/download/Homebrew.pkg",
        "https://github.com/y1-community/Innioasis-Updater/releases/latest/download/Innioasis.Updater.for.Mac.dmg",
    )
    for url in required_mac_urls:
        if url not in Path(GUIDE).read_text("utf-8", "ignore"):
            raise SystemExit(f"guide.html must still include {url!r}")
        if url not in Path(GUIDE_FIRMWARE).read_text("utf-8", "ignore"):
            raise SystemExit(f"firmware-guide.html must still include {url!r}")

    required_linux_strings = (
        "curl -sL https://github.com/y1-community/Innioasis-Updater/releases/latest/download/run_linux.sh | bash",
        "Linux setup notes",
        "data-copy-target=\"linux-install-command\"",
    )
    for s in required_linux_strings:
        if s not in Path(GUIDE).read_text("utf-8", "ignore"):
            raise SystemExit(f"guide.html must still include {s!r}")
        if s not in Path(GUIDE_FIRMWARE).read_text("utf-8", "ignore"):
            raise SystemExit(f"firmware-guide.html must still include {s!r}")

    # These two names are intentionally reused in the check file body; keep the
    # message read-only so the stdout encoding does not explode in cp1252 shells.
    Path("_windows_section_isolation_stdout.txt").write_text(
        "OK: only the Windows download card was changed; macOS, Linux, and the "
        "Another platform toggle are untouched.",
        "utf-8",
    )
    print("OK: only the Windows download card was changed; macOS, Linux, and the "
          "Another platform toggle are untouched.")


DRIVER_BUTTON_HTML = (
    '<a class="lumen-button" href="https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe" download data-download-confirm="Download started">Download &amp; Install Driver</a>'
)


if __name__ == "__main__":
    main()
