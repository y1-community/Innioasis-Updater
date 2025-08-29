#!/bin/bash

# ==============================================================================
# Innioasis Updater - Robust Terminal Setup & Launcher v5.0
#
# This script provides a one-time, terminal-driven setup for the application.
#
# How it works:
# 1. On first run, it checks for a completion marker. If not found, it
#    begins the full, interactive setup process within the terminal.
# 2. It guides the user through installing Xcode Tools and Homebrew (using
#    the official .pkg installer), then automates the installation of all
#    other dependencies.
# 3. Upon successful setup, it creates a completion marker.
# 4. On all subsequent runs, it finds the marker and immediately launches the
#    Python application silently in the background.
# ==============================================================================

# --- Configuration ---
APP_DIR="$HOME/Library/Application Support/Innioasis Updater"
REPO_URL="https://github.com/team-slide/Innioasis-Updater.git"
VENV_DIR="$APP_DIR/venv"
PYTHON_SCRIPT="$APP_DIR/updater.py"
COMPLETION_MARKER="$VENV_DIR/.mac_setup_complete"

# ==============================================================================
# SECTION 1: FULL SETUP LOGIC
# ==============================================================================
run_full_setup() {
    # --- Style and Formatting ---
    BLUE='\033[0;34m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; NC='\033[0m'

    # --- Helper Functions ---
    step_echo() { echo -e "\n${BLUE}▶ $1${NC}"; }
    success_echo() { echo -e "${GREEN}✓ $1${NC}"; }
    warn_echo() { echo -e "${YELLOW}⚠️ $1${NC}"; }
    error_echo() { echo -e "${RED}✗ $1${NC}"; }
    prompt_for_enter() { read -p "   Press [Enter] to continue..."; }

    clear
    echo "=========================================="
    echo "  Welcome to the Innioasis Updater Setup"
    echo "=========================================="
    echo "This script will perform a one-time setup to prepare your Mac."
    echo "Your involvement will be needed for the Xcode and Homebrew installers."
    prompt_for_enter

    # --- 1. Check macOS Version ---
    step_echo "Checking macOS Version..."
    macos_version=$(sw_vers -productVersion)
    if [[ $(echo "$macos_version" | cut -d . -f 1) -lt 12 ]]; then
        error_echo "macOS version ($macos_version) is older than 12 (Monterey) and is not compatible."
        exit 1
    else
        success_echo "macOS version $macos_version is supported."
    fi

    # --- 2. Install Xcode Command Line Tools ---
    step_echo "Checking for Xcode Command Line Tools..."
    if ! xcode-select -p &>/dev/null; then
        warn_echo "Xcode Command Line Tools are required."
        echo "A software update popup will appear. Please click 'Install' and wait for it to finish before returning here."
        xcode-select --install
        
        echo "Waiting for you to complete the installation..."
        prompt_for_enter

        # Verify installation
        if ! xcode-select -p &>/dev/null; then
             error_echo "Xcode Tools installation was not detected. Please try running 'xcode-select --install' manually, then run this script again."
             exit 1
        fi
        success_echo "Xcode Command Line Tools installed."
    else
        success_echo "Xcode Command Line Tools already installed."
    fi

    # --- 3. Install/Update Homebrew ---
    step_echo "Checking for Homebrew package manager..."
    if ! command -v brew &>/dev/null; then
        warn_echo "Homebrew is not installed. We will download the official installer package."
        
        # Determine architecture
        if [[ "$(uname -m)" == "arm64" ]]; then
            ARCH="arm64"
        else
            ARCH="x86_64" # Intel
        fi
        echo "   Detected architecture: ${ARCH}"

        # Fetch latest release tag from GitHub API
        echo "   Fetching latest Homebrew version..."
        LATEST_TAG=$(curl -sL "https://api.github.com/repos/Homebrew/brew/releases/latest" | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/')
        if [ -z "$LATEST_TAG" ]; then
            error_echo "Could not determine the latest Homebrew version. Please install it manually from brew.sh"
            exit 1
        fi
        success_echo "Latest version is ${LATEST_TAG}."
        
        PKG_URL="https://github.com/Homebrew/brew/releases/download/${LATEST_TAG}/Homebrew-${LATEST_TAG}.pkg"
        PKG_PATH="/tmp/Homebrew-${LATEST_TAG}.pkg"

        echo "   Downloading Homebrew installer from GitHub..."
        if ! curl -L --fail "$PKG_URL" -o "$PKG_PATH"; then
             error_echo "Failed to download Homebrew installer. Please check your internet connection."
             exit 1
        fi
        success_echo "Download complete."

        echo
        warn_echo "The Homebrew installer will now open."
        echo "   Please complete the installation, then return to this terminal window."
        prompt_for_enter

        sudo open "$PKG_PATH"
        
        echo
        echo "Waiting for you to complete the Homebrew installation..."
        echo "Once it is finished, press Enter here to continue the script."
        prompt_for_enter

        # Configure Homebrew path for this session
        if [[ "$ARCH" == "arm64" ]]; then
            eval "$(/opt/homebrew/bin/brew shellenv)"
        else
            eval "$(/usr/local/bin/brew shellenv)"
        fi

        if ! command -v brew &>/dev/null; then
            error_echo "Homebrew installation failed or is not in the PATH. Please check the installer logs."
            exit 1
        fi
        success_echo "Homebrew is now configured."
        rm "$PKG_PATH"
    else
        success_echo "Homebrew already installed. Updating..."
        brew update
        success_echo "Homebrew updated."
    fi

    HOMEBREW_PREFIX=$(brew --prefix)

    # --- 4. Install Brew Dependencies ---
    step_echo "Installing required tools with Homebrew..."
    BREW_PACKAGES="python python-tk libusb openssl libffi rust cmake pkg-config android-platform-tools"
    for pkg in $BREW_PACKAGES; do
        if brew list --formula | grep -q "^${pkg}\$"; then
            success_echo "${pkg} is already installed."
        else
            echo "   Installing ${pkg}..."
            if brew install ${pkg}; then
                success_echo "Installed ${pkg}."
            else
                error_echo "Failed to install ${pkg}. Please check Homebrew logs and run again."
                exit 1
            fi
        fi
    done

    # --- 5. Setup Application Files ---
    step_echo "Setting up application files from Git..."
    if [ -d "$APP_DIR" ]; then
        warn_echo "Existing directory found. Removing for a clean installation."
        rm -rf "$APP_DIR"
    fi
    if ! git clone "$REPO_URL" "$APP_DIR"; then
        error_echo "Git clone failed. Check your internet connection or if Git is installed correctly."
        exit 1
    fi
    success_echo "Application files cloned to '$APP_DIR'."
    cd "$APP_DIR"

    # --- 6. Setup Python Virtual Environment and Dependencies ---
    step_echo "Setting up Python environment..."
    PYTHON_EXEC="$HOMEBREW_PREFIX/bin/python3"
    
    echo "   Creating Python virtual environment..."
    if ! "$PYTHON_EXEC" -m venv "$VENV_DIR"; then
        error_echo "Failed to create virtual environment. Please check your Homebrew Python installation."
        exit 1
    fi
    success_echo "Virtual environment created."
    
    source "$VENV_DIR/bin/activate"
    python3 -m pip install --upgrade pip wheel setuptools
    
    echo "   Installing Python dependencies from requirements.txt..."
    export LDFLAGS="-L$(brew --prefix openssl)/lib -L$(brew --prefix libusb)/lib -L$(brew --prefix libffi)/lib"
    export CPPFLAGS="-I$(brew --prefix openssl)/include -I$(brew --prefix libusb)/include -I$(brew --prefix libffi)/include"
    export PKG_CONFIG_PATH="$(brew --prefix openssl)/lib/pkgconfig:$(brew --prefix libusb)/lib/pkgconfig:$(brew --prefix libffi)/lib/pkgconfig"
    
    if ! python3 -m pip install --no-cache-dir -r requirements.txt; then
        error_echo "Failed to install Python dependencies. Please review the errors above."
        deactivate
        exit 1
    fi
    
    unset LDFLAGS CPPFLAGS PKG_CONFIG_PATH
    success_echo "All Python dependencies installed."
    deactivate

    # --- 7. Create Completion Marker & Finish ---
    step_echo "Finalizing setup..."
    touch "$COMPLETION_MARKER"
    echo ""
    echo "=========================================="
    success_echo "  Setup Complete!"
    echo "=========================================="
    echo "You can run this script again at any time to start the application."
    sleep 3
}

# ==============================================================================
# SCRIPT ENTRY POINT
# ==============================================================================

# Check if setup has been completed.
if [ -f "$COMPLETION_MARKER" ]; then
    # --- FAST PATH: Setup is complete, run the app silently ---
    echo "Setup complete. Launching Innioasis Updater..."
    cd "$APP_DIR"
    source "$VENV_DIR/bin/activate"
    # Execute the python script in the background. Hide all output.
    nohup python3 "$PYTHON_SCRIPT" > /dev/null 2>&1 &
    exit 0
else
    # --- FIRST RUN: Setup is needed ---
    run_full_setup
    
    # After setup, launch the app for the first time.
    echo "Launching the application for the first time..."
    cd "$APP_DIR"
    source "$VENV_DIR/bin/activate"
    nohup python3 "$PYTHON_SCRIPT" > /dev/null 2>&1 &
    exit 0
fi
