#!/usr/bin/env bash
# Hosted copy of the text-session launcher. The window build stays the one
# people open from the AppImage, the tarball and the zip. This file is what
# https://innioasis.app/run_linux_lite.sh serves.

set -euo pipefail

curl -fsSL https://raw.githubusercontent.com/y1-community/updater-ce-neo/main/run_linux_lite.sh | bash -s -- "$@"
