#!/bin/bash

# Innioasis Updater Setup Script for macOS v3.3
#
# Changelog:
# - Enhanced Python dependency installation with more robust environment variables
#   (LDFLAGS, CPPFLAGS, CFLAGS, PKG_CONFIG_PATH) to prevent wheel build failures for
#   packages like 'scrypt'.
# - Added 'rust' and 'libffi' to Homebrew dependencies as a preventative measure
#   for a wider range of modern Python packages that use Rust or C extensions.
# - Refined macOS version check to officially support 13.5+ while allowing attempts
#   on 12.0+ with a warning.
# - Added --no-cache-dir to pip install to avoid using potentially corrupt cached builds.
# - Improved error handling during pip install to provide clearer user guidance on failure.

# --- Style and Formatting ---
BLUE='\033[0;34m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# --- Helper Functions ---
step_echo() {
    echo -e "\n${BLUE}▶ $1${NC}"
}

success_echo() {
    echo -e "${GREEN}✓ $1${NC}"
}

warn_echo() {
    echo -e "${YELLOW}⚠️ $1${NC}"
}

error_echo() {
    echo -e "${RED}✗ $1${NC}"
}

prompt_for_enter() {
    read -p "  Press [Enter] to continue..."
}

# --- Configuration ---
APP_DIR="$HOME/Library/Application Support/Innioasis Updater"
REPO_URL="https://github.com/team-slide/Innioasis-Updater.git"
VENV_DIR="$APP_DIR/venv"
COMPLETION_MARKER="$VENV_DIR/.mac_setup_complete"

# --- Pre-flight Check: Has setup already been completed? ---
# If the completion marker exists, skip the entire setup and just run the app.
if [ -f "$COMPLETION_MARKER" ]; then
    echo -e "${GREEN}Setup has already been completed. Launching the application directly.${NC}"
    cd "$APP_DIR"
    source "$VENV_DIR/bin/activate"
    # Use nohup to detach the process, allowing the terminal to close.
    nohup python3 updater.py > /dev/null 2>&1 &
    echo "Application is running. You can close this terminal window."
    exit 0
fi

# --- Main Script ---
clear
echo "=========================================="
echo "  Welcome to the Innioasis Updater Setup"
echo "=========================================="
echo "This script will perform a one-time setup to prepare your Mac."
echo "Future runs of this script will launch the application instantly."
echo ""
echo "Your involvement may be needed to approve installations or enter your password."
echo ""
prompt_for_enter

# --- 1. Check macOS Version ---
step_echo "Checking macOS Version..."
macos_version=$(sw_vers -productVersion)
if [[ $(echo "$macos_version" | cut -d . -f 1) -lt 12 ]]; then
    error_echo "Your macOS version ($macos_version) is older than 12 (Monterey)."
    error_echo "This script is not compatible with your OS. Please upgrade macOS."
    exit 1
elif [[ "$macos_version" < "13.5" ]]; then
    warn_echo "Your macOS version is $macos_version."
    warn_echo "This script is officially supported on macOS 13.5 (Ventura) and newer."
    warn_echo "It will attempt to run, but you may encounter issues."
    prompt_for_enter
else
    success_echo "macOS version $macos_version is fully supported."
fi

# --- 2. Install Xcode Command Line Tools ---
step_echo "Checking for Xcode Command Line Tools..."
if ! xcode-select -p &>/dev/null; then
    warn_echo "Xcode Command Line Tools are required."
    echo "  A software update popup will appear on your screen."
    echo "  Please click 'Install' and agree to the terms."
    echo -e "  ${YELLOW}This script will automatically detect when the installation is complete and continue. This may take several minutes.${NC}"
    
    # Trigger the installer GUI
    xcode-select --install
    
    # Poll until the installation is complete
    echo -n "  Waiting for you to complete the installation..."
    while ! xcode-select -p &>/dev/null; do
        echo -n "."
        sleep 5
    done
    echo "" # Newline after the dots
    success_echo "Xcode Command Line Tools installed."
else
    success_echo "Xcode Command Line Tools already installed."
fi

# --- 3. Install Homebrew ---
step_echo "Checking for Homebrew package manager..."
if ! command -v brew &>/dev/null; then
    warn_echo "Homebrew is not installed. It will be installed now."
    echo "  The official Homebrew installer will explain the changes it will make and require your password to proceed."
    prompt_for_enter
    
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    # Add Homebrew to PATH for the current shell session
    if [[ "$(uname -m)" == "arm64" ]]; then
      eval "$(/opt/homebrew/bin/brew shellenv)"
    else
      eval "$(/usr/local/bin/brew shellenv)"
    fi
    success_echo "Homebrew installed and configured for this session."
else
    success_echo "Homebrew already installed."
    step_echo "Updating Homebrew..."
    brew update
    success_echo "Homebrew updated."
fi

# --- 4. Install Brew Dependencies ---
step_echo "Installing required tools with Homebrew..."
# Added rust and libffi to prevent common build failures with Python packages.
BREW_PACKAGES="python libusb openssl libffi rust cmake pkg-config android-platform-tools"
for pkg in $BREW_PACKAGES; do
    if brew list --formula | grep -q "^${pkg}\$"; then
        success_echo "${pkg} is already installed."
    else
        echo "  Installing ${pkg}..."
        brew install ${pkg}
        success_echo "Installed ${pkg}."
    fi
done

# --- 5. Setup Application Files ---
setup_with_git() {
    echo "  Attempting a clean clone with git (Primary Method)..."
    if [ -d "$APP_DIR" ]; then
        warn_echo "Existing directory found. It will be removed to ensure a clean installation."
        rm -rf "$APP_DIR"
    fi
    
    if git clone "$REPO_URL" "$APP_DIR"; then
        success_echo "Application files cloned successfully using git."
        return 0
    else
        error_echo "Git clone failed."
        return 1
    fi
}

setup_with_zip() {
    warn_echo "Falling back to ZIP download method..."
    local zip_url="https://github.com/team-slide/Innioasis-Updater/archive/refs/heads/main.zip"
    local tmp_zip="/tmp/innioasis_updater.zip"
    
    if ! curl -L --fail "$zip_url" -o "$tmp_zip"; then
        error_echo "Failed to download ZIP file. Cannot continue."
        return 1
    fi
    
    rm -rf "$APP_DIR"
    mkdir -p "$APP_DIR"
    
    unzip -q "$tmp_zip" -d "/tmp"
    local unzipped_dir="/tmp/Innioasis-Updater-main"
    mv "$unzipped_dir"/* "$APP_DIR"/
    mv "$unzipped_dir"/.* "$APP_DIR"/ 2>/dev/null || true # Move hidden files
    
    rm "$tmp_zip"
    rm -rf "$unzipped_dir"
    
    success_echo "Application files set up successfully using ZIP."
    return 0
}

step_echo "Setting up application files in '$APP_DIR'..."
if ! setup_with_git; then
    if ! setup_with_zip; then
        error_echo "Both git and ZIP methods failed. Please check your internet connection and try again."
        exit 1
    fi
fi

cd "$APP_DIR"

# --- 6. Setup Python Virtual Environment and Dependencies ---
step_echo "Setting up Python environment..."

# It's crucial to use the Python installed by Homebrew, not the system one.
HOMEBREW_PREFIX=$(brew --prefix)
PYTHON_EXEC="$HOMEBREW_PREFIX/bin/python3"

if [ ! -f "$PYTHON_EXEC" ]; then
    error_echo "Could not find Homebrew's Python 3 at '$PYTHON_EXEC'."
    error_echo "This should have been installed. Please check your Homebrew setup."
    exit 1
fi

if [ ! -d "$VENV_DIR" ]; then
    echo "  Creating Python virtual environment using Homebrew's Python..."
    "$PYTHON_EXEC" -m venv "$VENV_DIR"
    success_echo "Virtual environment created."
else
    success_echo "Virtual environment already exists."
fi

echo "  Activating virtual environment..."
source "$VENV_DIR/bin/activate"

echo "  Upgrading pip, wheel, and setuptools..."
python3 -m pip install --upgrade pip wheel setuptools
success_echo "Pip, wheel, and setuptools upgraded."

echo "  Installing Python dependencies from requirements.txt..."
# Set comprehensive environment variables to help pip find Homebrew libraries.
# This is critical for compiling packages with C extensions (like 'scrypt') on macOS.
export LDFLAGS="-L$(brew --prefix openssl)/lib -L$(brew --prefix libusb)/lib -L$(brew --prefix libffi)/lib"
export CPPFLAGS="-I$(brew --prefix openssl)/include -I$(brew --prefix libusb)/include -I$(brew --prefix libffi)/include"
export CFLAGS="$CPPFLAGS"
export PKG_CONFIG_PATH="$(brew --prefix openssl)/lib/pkgconfig:$(brew --prefix libusb)/lib/pkgconfig:$(brew --prefix libffi)/lib/pkgconfig"

# Attempt installation with flags set and without using cached wheels.
if ! python3 -m pip install --no-cache-dir -r requirements.txt; then
    error_echo "Failed to install Python dependencies."
    warn_echo "This usually happens when a package with C-extensions fails to compile."
    echo ""
    echo "  Please review the error messages above this one for specific details."
    echo "  Common troubleshooting steps:"
    echo "  1. Run 'brew doctor' and fix any reported issues."
    echo "  2. Ensure Xcode Command Line Tools are fully updated."
    echo "  3. If the issue persists, please report the full error log on the project's GitHub page."

    unset LDFLAGS CPPFLAGS CFLAGS PKG_CONFIG_PATH
    deactivate
    exit 1
fi

# Unset the variables so they don't linger in the user's shell.
unset LDFLAGS CPPFLAGS CFLAGS PKG_CONFIG_PATH
success_echo "All Python dependencies installed successfully."

deactivate

# --- 7. Create Completion Marker ---
step_echo "Finalizing setup..."
touch "$COMPLETION_MARKER"
success_echo "Completion marker created. Future runs of this script will launch the app immediately."

# --- 8. Final Steps ---
echo ""
echo "=========================================="
success_echo "  Setup Complete!"
echo "=========================================="
echo ""
echo "The application is ready. For reference, to run it manually:"
echo -e "  1. ${YELLOW}cd \"$APP_DIR\"${NC}"
echo -e "  2. ${YELLOW}source venv/bin/activate${NC}"
echo -e "  3. ${YELLOW}python3 updater.py${NC}"
echo ""

step_echo "Starting the application now..."
prompt_for_enter

cd "$APP_DIR"
source venv/bin/activate
# Use nohup to detach the process, allowing the terminal to close.
nohup python3 updater.py > /dev/null 2>&1 &

echo "Application is running. You can close this terminal window."
exit 0
