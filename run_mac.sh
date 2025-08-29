#!/bin/bash

# Innioasis Updater Setup Script for macOS v3.2
#
# Changelog:
# - Automates Xcode Command Line Tools check by polling for completion,
#   preventing user confusion and unnecessary prompts.
# - Implements a completion marker (`.mac_setup_complete`) to bypass setup
#   on subsequent runs, enabling one-click execution.
# - Refines user-facing instructions for clarity and a smoother experience.
# - Retains robust features: git clone with ZIP fallback, Homebrew for a
#   modern Python, and linker flags for reliable dependency installation.

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
export LDFLAGS="-L$(brew --prefix openssl)/lib -L$(brew --prefix libusb)/lib"
export CPPFLAGS="-I$(brew --prefix openssl)/include -I$(brew --prefix libusb)/include"
pip install -r requirements.txt
# Unset the variables so they don't linger in the user's shell
unset LDFLAGS CPPFLAGS
success_echo "All Python dependencies are installed."

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
