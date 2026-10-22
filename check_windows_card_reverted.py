#!/usr/bin/env python3
"""Validate the reverted Windows download card.

Checks:
- the DriverInstall link is back in both guide pages,
- the “Blocked by Edge?” text link is present in both pages,
- the renamed primary button is still present,
- the screenshot asset reference and screenshot modal are gone,
- the old text-only Edge modal is also gone.
"""
from __future__ import annotations

from pathlib import Path

GUIDE = "guide.html"
GUIDE_FIRMWARE = "firmware-guide.html"

DRIVER_LINK = (
    '<a class="lumen-button" href="https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe" download data-download-confirm="Download started">Download &amp; Install Driver</a>'
)
EDGE_TEXT_HELP = (
    '<a class="lumen-edge-help-text" href="#"'
)
PRIMARY_BUTTON = (
    '<a class="lumen-button lumen-button--primary" href="https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe" download data-download-confirm="Download started">Download App and Drivers</a>'
)
SCREENSHOT_REF = 'src="Screenshot_20261022_190846-1.png"'
OLD_MODAL = 'id="edge-keep-modal"'
SCREENSHOT_MODAL = 'id="edge-keep-screenshot-modal"'
OLD_HINT_TEXT = "Need the file after Edge blocked it?"


def main() -> None:
    problems: list[str] = []
    for page in (GUIDE, GUIDE_FIRMWARE):
        body = Path(page).read_text("utf-8", "ignore")
        if DRIVER_LINK not in body:
            problems.append(f"{page} missing restored DriverInstall button")
        if PRIMARY_BUTTON not in body:
            problems.append(f"{page} missing Download App and Drivers button")
        if EDGE_TEXT_HELP not in body:
            problems.append(f"{page} missing Blocked by Edge? text link")
        if SCREENSHOT_REF in body:
            problems.append(f"{page} still references the screenshot asset")
        if SCREENSHOT_MODAL in body:
            problems.append(f"{page} still has the screenshot modal")
        if OLD_MODAL in body:
            problems.append(f"{page} still has the old text-only modal")
        if OLD_HINT_TEXT in body:
            problems.append(f"{page} still has the old Edge hint text")

    if problems:
        for p in problems:
            print("FAIL:", p)
        raise SystemExit(1)

    print("OK: Windows card reverted to driver button + Blocked by Edge? text link, and screenshot assets are gone from both guide pages.")


if __name__ == "__main__":
    main()
