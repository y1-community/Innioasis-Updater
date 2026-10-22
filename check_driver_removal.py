#!/usr/bin/env python3
"""Extra check that no Windows download section still surfaces a separate
“Download & Install Driver” action as a first-class button.

The requested change is specifically: remove the Drivers button from the
Innioasis Updater CE Windows download section, and rename the existing
“Download Updater CE for Windows” button to “Download App and Drivers”.
So the driver link should only remain where this site already documents the
driver as its own step (the drivers.html setup page and the “need to reboot”
notes), not as a sibling button to the Updater CE download.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent

DRIVER_BUTTON_HTML = (
    '<a class="lumen-button" href="https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe" download data-download-confirm="Download started">Download &amp; Install Driver</a>'
)


def main() -> None:
    problems: list[str] = []

    for page in ["guide.html", "firmware-guide.html"]:
        body = Path(page).read_text("utf-8", "ignore")
        if DRIVER_BUTTON_HTML in body:
            problems.append(
                f"{page} still contains the standalone Drivers download button"
            )

    if problems:
        for p in problems:
            print("FAIL:", p)
        raise SystemExit(1)

    print("OK: no Windows download section still shows the standalone Drivers button.")


if __name__ == "__main__":
    main()
