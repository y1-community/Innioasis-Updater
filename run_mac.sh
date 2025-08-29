#!/bin/bash

# Innioasis Updater Setup Script for macOS v3.1
# - Prioritizes a clean git clone to prevent conflicts.
# - Falls back to a ZIP download if git fails.
# - Installs an up-to-date Python via Homebrew for tkinter compatibility.
# - Provides clear prompts for all user interactions.
# - Sets linker flags to prevent "Failed building wheel" errors.

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

# --- Main Script ---
clear
echo "=========================================="
echo "  Welcome to the Innioasis Updater Setup"
echo "=========================================="
echo "This script will prepare your Mac to run the application."
echo "Your involvement will be needed for a few steps."
echo ""
prompt_for_enter

# --- Configuration ---
APP_DIR="$HOME/Library/Application Support/Innioasis Updater"
REPO_URL="https://github.com/team-slide/Innioasis-Updater.git"

# --- 1. Check macOS Version ---
step_echo "Checking macOS Version..."
if [[ $(sw_vers -productVersion | cut -d . -f 1) -lt 13 ]]; then
    warn_echo "Your macOS version is older than 13.5 (Ventura)."
    warn_echo "This script is tested on macOS 13.5+, but will attempt to continue."
    prompt_for_enter
else
    success_echo "macOS version is compatible."
fi

# --- 2. Install Xcode Command Line Tools ---
step_echo "Checking for Xcode Command Line Tools..."
if ! xcode-select -p &>/dev/null; then
    warn_echo "Xcode Command Line Tools are not installed."
    echo "  A software update popup will now appear on your screen."
    echo "  Please click 'Install' and wait for the download and installation to complete."
    echo "  This script will wait for you."
    
    xcode-select --install
    
    echo "  Please complete the GUI installation. Once it disappears, press Enter here."
    prompt_for_enter

    while ! xcode-select -p &>/dev/null; do
        error_echo "Xcode Tools still not found. Please ensure the installation is fully complete."
        warn_echo "If the installation failed, please run 'xcode-select --install' again in a new terminal."
        prompt_for_enter
    done
    success_echo "Xcode Command Line Tools installed."
else
    success_echo "Xcode Command Line Tools already installed."
fi

# --- 3. Install Homebrew ---
step_echo "Checking for Homebrew package manager..."
if ! command -v brew &>/dev/null; then
    warn_echo "Homebrew is not installed."
    echo "  The official Homebrew installer will now run in your terminal."
    echo "  It will explain the changes it will make and may ask for your password to proceed."
    prompt_for_enter
    
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

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
# Add 'python' to ensure a modern version with working tkinter is installed
BREW_PACKAGES="python libusb openssl cmake pkg-config android-platform-tools"
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
    # This is the key change: remove the directory first to prevent conflicts.
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
VENV_DIR="venv"
if [ ! -d "$VENV_DIR" ]; then
    echo "  Creating Python virtual environment..."
    python3 -m venv "$VENV_DIR"
    success_echo "Virtual environment created."
else
    success_echo "Virtual environment already exists."
fi

echo "  Activating virtual environment..."
source "$VENV_DIR/bin/activate"

echo "  Upgrading pip, wheel, and setuptools..."
python3 -m pip install --upgrade pip wheel setuptools
success_echo "Pip upgraded."

echo "  Installing Python dependencies from requirements.txt..."
# Explicitly set flags to help pip find Homebrew's libraries.
# This prevents common "Failed building wheel" errors.
export LDFLAGS="-L$(brew --prefix openssl)/lib -L$(brew --prefix libusb)/lib"
export CPPFLAGS="-I$(brew --prefix openssl)/include -I$(brew --prefix libusb)/include"
pip install -r requirements.txt
# Unset the variables so they don't linger in the user's shell
unset LDFLAGS CPPFLAGS
success_echo "All Python dependencies are installed."

deactivate

# --- 7. Final Steps ---
echo ""
echo "=========================================="
success_echo "  Setup Complete!"
echo "=========================================="
echo ""
echo "The application is ready. To run it manually in the future,"
echo "open Terminal and use these commands:"
echo -e "  1. ${YELLOW}cd \"$APP_DIR\"${NC}"
echo -e "  2. ${YELLOW}source venv/bin/activate${NC}"
echo -e "  3. ${YELLOW}python3 updater.py${NC}"
echo ""

step_echo "Starting the application now..."
prompt_for_enter

cd "$APP_DIR"
source venv/bin/activate
# Use nohup to detach the process, allowing the terminal to close.
# Redirect stdout and stderr to /dev/null to prevent output.
nohup python3 updater.py > /dev/null 2>&1 &

echo "Application is running. You can close this terminal window."
exit 0

