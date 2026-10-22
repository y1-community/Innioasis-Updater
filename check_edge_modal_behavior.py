#!/usr/bin/env python3
"""Validate the screenshot-based Edge modal wiring after the next edit round.

Checks:
- Both guide pages still have the renamed Windows button.
- Both pages have a screenshot link below the Windows button that opens the
  screenshot-based Edge modal.
- Both pages contain the new modal markup and the screenshot asset reference.
- lumen-site.js wires the new modal IDs/classes.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
GUIDE = "guide.html"
GUIDE_FIRMWARE = "firmware-guide.html"
JS = "lumen-site.js"
SCREENSHOT = "Screenshot_20261022_190846-1.png"

WINDOWS_BUTTON = (
    '<a class="lumen-button lumen-button--primary" href="https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe" download data-download-confirm="Download started">Download App and Drivers</a>'
)
SCREENSHOT_ANCHOR = (
    '<a class="lumen-edge-help-link" href="#"'
)
MODAL_START = (
    '<div id="edge-keep-screenshot-modal" class="edge-keep-modal" hidden'
)


def text(path: str) -> str:
    return Path(path).read_text("utf-8", "ignore")


def main() -> None:
    guide = text(GUIDE)
    firmware = text(GUIDE_FIRMWARE)
    js = text(JS)

    for label, body in ((GUIDE, guide), (GUIDE_FIRMWARE, firmware)):
        assert WINDOWS_BUTTON in body, f"{label} missing renamed Windows button"
        assert SCREENSHOT_ANCHOR in body, f"{label} missing screenshot help link"
        assert MODAL_START in body, f"{label} missing screenshot modal block"
        assert 'src="Screenshot_20261022_190846-1.png"' in body, (
            f"{label} missing screenshot asset reference"
        )
        assert "Keep the installer after Edge blocks it" in body, (
            f"{label} missing screenshot modal heading"
        )

    assert "function openEdgeKeepScreenshotModal()" in js, (
        "lumen-site.js missing screenshot modal opener"
    )
    assert "function closeEdgeKeepScreenshotModal()" in js, (
        "lumen-site.js missing screenshot modal closer"
    )
    assert "function initEdgeKeepScreenshotHelp()" in js, (
        "lumen-site.js missing screenshot modal wiring"
    )
    assert 'data-edge-keep-screenshot-hint' in js, (
        "lumen-site.js missing screenshot hint binding"
    )
    assert 'openEdgeKeepScreenshotModal();' in js, (
        "lumen-site.js missing screenshot modal open call path"
    )
    assert 'data-edge-keep-screenshot-close' in js, (
        "lumen-site.js missing screenshot modal close binding"
    )

    assert Path(SCREENSHOT).exists(), "Screenshot asset file is missing after copy"

    print("OK: screenshot-based Edge modal wiring checks passed.")


if __name__ == "__main__":
    main()
