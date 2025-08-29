#!/bin/bash

# Innioasis Updater Setup Script for macOS
# This script will guide you through installing all necessary dependencies.
# It will pause and wait for you to complete GUI-based installations.

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

# Ensure the script exits if any command fails
set -e

# --- Main Script ---
clear
echo "=========================================="
echo "  Welcome to the Innioasis Updater Setup"
echo "=========================================="
echo "This script will prepare your Mac to run the application."
echo "It will check for and install the following:"
echo "  - Xcode Command Line Tools"
echo "  - Homebrew Package Manager"
echo "  - Required libraries (libusb, openssl, etc.)"
echo "  - Android Platform Tools (for adb)"
echo "  - Python dependencies"
echo ""

# --- 1. Check macOS Version ---
step_echo "Checking macOS Version..."
if [[ $(sw_vers -productVersion | cut -d . -f 1) -lt 13 ]]; then
    warn_echo "Your macOS version is older than 13.5 (Ventura)."
    warn_echo "This script is tested on macOS 13.5+ but will attempt to continue."
    prompt_for_enter
else
    success_echo "macOS version is compatible."
fi

# --- 2. Install Xcode Command Line Tools ---
step_echo "Checking for Xcode Command Line Tools..."
if ! xcode-select -p &>/dev/null; then
    warn_echo "Xcode Command Line Tools are not installed."
    echo "  A software update popup will now appear."
    echo "  Please click 'Install' and wait for the installation to complete before proceeding."
    
    # This command triggers the GUI installer
    xcode-select --install
    
    echo "  Please complete the installation now."
    prompt_for_enter

    # Loop until the tools are actually installed
    while ! xcode-select -p &>/dev/null; do
        error_echo "Xcode Tools still not found. Please ensure the installation is complete."
        prompt_for_enter
    done
    success_echo "Xcode Command Line Tools installed."
else
    success_echo "Xcode Command Line Tools already installed."
fi

# --- 3. Install Homebrew ---
step_echo "Checking for Homebrew..."
if ! command -v brew &>/dev/null; then
    warn_echo "Homebrew is not installed."
    echo "  The official Homebrew installer will now run."
    echo "  It will ask for your password and explain the changes it will make."
    prompt_for_enter
    
    # This is the official, recommended, non-interactive command
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

    # Add Homebrew to PATH for the current script session
    # This handles both Apple Silicon and Intel Macs
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
step_echo "Installing dependencies with Homebrew..."
BREW_PACKAGES="libusb openssl cmake pkg-config android-platform-tools"
for pkg in $BREW_PACKAGES; do
    if brew list --formula | grep -q "^${pkg}\$"; then
        success_echo "${pkg} is already installed."
    else
        echo "  Installing ${pkg}..."
        brew install ${pkg}
        success_echo "Installed ${pkg}."
    fi
done

# --- 5. Clone or Update the Repository ---
APP_DIR="$HOME/Library/Application Support/Innioasis Updater"
step_echo "Setting up application files in '$APP_DIR'..."
if [ -d "$APP_DIR" ]; then
    success_echo "Application directory already exists. Updating..."
    cd "$APP_DIR"
    # Stash local changes to prevent pull errors, then pull, then apply stash
    git stash push -m "setup-script-stash" > /dev/null
    git pull
    git stash pop > /dev/null 2>&1 || true # Ignore error if there's no stash
    success_echo "Application updated."
else
    echo "  Cloning repository..."
    git clone https://github.com/team-slide/Innioasis-Updater.git "$APP_DIR"
    success_echo "Repository cloned."
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
# We install from requirements.txt as it's the standard
pip install -r requirements.txt
success_echo "All Python dependencies are installed."

deactivate

# --- 7. Final Steps ---
echo ""
echo "=========================================="
success_echo "  Setup Complete!"
echo "=========================================="
echo ""
echo "You can now run the application from the Terminal at any time with these commands:"
echo -e "  1. ${YELLOW}cd \"$APP_DIR\"${NC}"
echo -e "  2. ${YELLOW}source venv/bin/activate${NC}"
echo -e "  3. ${YELLOW}python3 updater.py${NC}"
echo ""

step_echo "Starting the application now..."
prompt_for_enter

cd "$APP_DIR"
source venv/bin/activate
python3 updater.py

exit 0
