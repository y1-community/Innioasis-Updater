#!/usr/bin/env python3
"""Quick parity checks for the Windows download-section change.

Validates that guide.html and firmware-guide.html no longer ship a separate
“Download & Install Driver” button or the old “Download Updater CE for Windows”
label, and that both now carry the renamed “Download App and Drivers” button plus
the Edge “keep the file” modal markup and wiring.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

GUIDE = "guide.html"
GUIDE_FIRMWARE = "firmware-guide.html"
JS = "lumen-site.js"
CSS = "lumen.css"


def text(path: str) -> str:
    return Path(path).read_text("utf-8", "ignore")


def assert_contains(path: str, needle: str, label: str) -> None:
    if needle not in text(path):
        raise AssertionError(f"{path} should contain {label!r}")


def assert_not_contains(path: str, needle: str, label: str) -> None:
    if needle in text(path):
        raise AssertionError(f"{path} should NOT contain {label!r}")


def main() -> None:
    guide = text(GUIDE)
    firmware = text(GUIDE_FIRMWARE)
    js = text(JS)
    css = text(CSS)

    # 1) The old driver-only button and old Windows label are gone from both
    #    download sections.
    for path, body in ((GUIDE, guide), (GUIDE_FIRMWARE, firmware)):
        assert_not_contains(
            path,
            '<a class="lumen-button" href="https://github.com/y1-community/supplemental-apks/releases/latest/download/DriverInstall.exe" download data-download-confirm="Download started">Download &amp; Install Driver</a>',
            "old DriverInstall button",
        )
        assert_not_contains(
            path,
            "Download Updater CE for Windows",
            "old Windows download label",
        )

    # 2) Both Windows download sections now use the renamed primary button.
    for path, body in ((GUIDE, guide), (GUIDE_FIRMWARE, firmware)):
        assert_contains(
            path,
            '<a class="lumen-button lumen-button--primary" href="https://github.com/y1-community/Innioasis-Updater/releases/latest/download/installer.exe" download data-download-confirm="Download started">Download App and Drivers</a>',
            "renamed Download App and Drivers button",
        )
        assert_contains(
            path,
            'data-edge-keep-hint href="#" role="button">Need the file after Edge blocked it?</a>',
            "Edge keep-help button",
        )

    # 3) Both pages now embed the same Edge keep modal block.
    modal_marker = (
        '<div id="edge-keep-modal" class="edge-keep-modal" hidden aria-hidden="true" role="dialog"'
    )
    assert_contains(GUIDE, modal_marker, "Edge keep modal container")
    assert_contains(
        GUIDE,
        "<ol class=\"edge-keep-modal__steps\"><li>Open Edge’s download panel by pressing <strong>Ctrl + J</strong> (or the download icon).</li><li>Hover over the blocked file name, then click the <strong>More options button (…)</strong> that appears.</li><li>Select <strong>Keep</strong> from the menu.</li><li>If Edge now shows a second prompt with a big Delete button and a Cancel button, select <strong>Show more</strong>, press the <strong>▼</strong> next to <strong>Delete</strong>, then choose <strong>Keep</strong>.</li></ol>",
        "Edge keep step list",
    )
    assert_contains(
        GUIDE,
        '<button type="button" class="lumen-button lumen-button--primary edge-keep-modal__close" data-edge-keep-close>Close</button>',
        "Edge keep modal close button",
    )
    assert_contains(GUIDE_FIRMWARE, modal_marker, "Edge keep modal container (firmware guide)")
    assert_contains(
        GUIDE_FIRMWARE,
        "<ol class=\"edge-keep-modal__steps\"><li>Open Edge’s download panel by pressing <strong>Ctrl + J</strong> (or the download icon).</li><li>Hover over the blocked file name, then click the <strong>More options button (…)</strong> that appears.</li><li>Select <strong>Keep</strong> from the menu.</li><li>If Edge now shows a second prompt with a big Delete button and a Cancel button, select <strong>Show more</strong>, press the <strong>▼</strong> next to <strong>Delete</strong>, then choose <strong>Keep</strong>.</li></ol>",
        "Edge keep step list (firmware guide)",
    )
    assert_contains(
        GUIDE_FIRMWARE,
        '<button type="button" class="lumen-button lumen-button--primary edge-keep-modal__close" data-edge-keep-close>Close</button>',
        "Edge keep modal close button (firmware guide)",
    )

    # 4) Both pages still keep the macOS/Linux download buttons and the
    #    “Another platform?” toggle, so we only changed the Windows line.
    assert_contains(
        GUIDE,
        '<a class="lumen-button" href="https://github.com/Homebrew/brew/releases/latest/download/Homebrew.pkg" download data-download-confirm="Download started">Download Homebrew</a>',
        "macOS Homebrew button still present",
    )
    assert_contains(
        GUIDE,
        'Download Updater CE</a>',
        "macOS Updater CE button still present",
    )
    assert_contains(
        GUIDE,
        "curl -sL https://github.com/y1-community/Innioasis-Updater/releases/latest/download/run_linux.sh | bash",
        "Linux install command still present",
    )
    assert_contains(GUIDE, "data-another-platform", "Another platform toggle still present")
    assert_contains(
        GUIDE_FIRMWARE,
        '<a class="lumen-button" href="https://github.com/Homebrew/brew/releases/latest/download/Homebrew.pkg" download data-download-confirm="Download started">Download Homebrew</a>',
        "macOS Homebrew button still present (firmware guide)",
    )
    assert_contains(
        GUIDE_FIRMWARE,
        "curl -sL https://github.com/y1-community/Innioasis-Updater/releases/latest/download/run_linux.sh | bash",
        "Linux install command still present (firmware guide)",
    )
    assert_contains(
        GUIDE_FIRMWARE, "data-another-platform", "Another platform toggle still present (firmware guide)"
    )

    # 5) JavaScript now wires the Edge keep modal open/close paths.
    assert_contains(
        JS,
        "function openEdgeKeepModal() {",
        "openEdgeKeepModal() definition",
    )
    assert_contains(
        JS,
        "function closeEdgeKeepModal() {",
        "closeEdgeKeepModal() definition",
    )
    assert_contains(
        JS,
        "function initEdgeKeepHelp() {",
        "initEdgeKeepHelp() definition",
    )
    assert_contains(
        JS,
        'document.querySelectorAll("[data-edge-keep-hint]").forEach(function (btn) {',
        "Edge keep hint binding",
    )
    assert_contains(
        JS,
        'var closeButton = modal.querySelector("[data-edge-keep-close]")',
        "Edge keep close binding",
    )
    assert_contains(
        JS,
        'initDownloadConfirm();\n        initEdgeKeepHelp();\n        initLumenTips();',
        "initEdgeKeepHelp() is called between initDownloadConfirm() and initLumenTips()",
    )

    # 6) CSS ships the modal and the secondary-button styles we referenced.
    assert_contains(
        CSS,
        ".edge-keep-modal { position: fixed; inset: 0; z-index: 1000;",
        "edge-keep-modal base style",
    )
    assert_contains(
        CSS,
        ".edge-keep-modal[hidden] { display: none; }",
        "edge-keep-modal hidden style",
    )
    assert_contains(
        CSS,
        ".edge-keep-modal__steps { margin: .75rem 0 0; padding: 0; list-style: none; }",
        "edge-keep-modal steps style",
    )
    assert_contains(
        CSS,
        ".lumen-button--secondary { background: var(--lumen-panel); color: var(--lumen-text); border: 1px solid var(--lumen-line-strong); }",
        "lumen-button--secondary style",
    )

    print("OK: Windows download section parity checks passed.")


if __name__ == "__main__":
    main()
