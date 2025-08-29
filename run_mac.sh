#!/bin/bash

# ==============================================================================
# Innioasis Updater - Hybrid App Launcher & Setup Script v4.1
#
# This script combines a user-friendly .app launcher with a robust, one-time
# setup process.
#
# How it works:
# 1. On first launch, it detects that setup is needed, displays a native
#    macOS dialog to the user, and then opens a Terminal window to run a
#    comprehensive setup function (`run_full_setup`).
# 2. The setup function installs all dependencies (Xcode, Homebrew, Python, etc.),
#    creates a virtual environment, and installs packages with self-healing and
#    verification steps.
# 3. Upon successful setup, it creates a completion marker and launches the app.
# 4. On all subsequent launches, the script sees the completion marker and
#    immediately runs the Python application silently.
# ==============================================================================

# --- Configuration ---
APP_NAME="Innioasis Updater.app"
APP_DIR="$HOME/Library/Application Support/Innioasis Updater"
REPO_URL="https://github.com/team-slide/Innioasis-Updater.git"
VENV_DIR="$APP_DIR/venv"
PYTHON_SCRIPT="$APP_DIR/updater.py"
COMPLETION_MARKER="$VENV_DIR/.mac_setup_complete"

# ==============================================================================
# SECTION 1: FULL SETUP LOGIC (to be run in a terminal, only once)
# This is the robust setup script, encapsulated in a function.
# ==============================================================================
run_full_setup() {
    # --- Style and Formatting ---
    BLUE='\033[0;34m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; NC='\033[0m'

    # --- Helper Functions ---
    step_echo() { echo -e "\n${BLUE}▶ $1${NC}"; }
    success_echo() { echo -e "${GREEN}✓ $1${NC}"; }
    warn_echo() { echo -e "${YELLOW}⚠️ $1${NC}"; }
    error_echo() { echo -e "${RED}✗ $1${NC}"; }
    prompt_for_enter() { read -p "  Press [Enter] to continue..."; }

    clear
    echo "=========================================="
    echo "  Welcome to the Innioasis Updater Setup"
    echo "=========================================="
    echo "This script will perform a one-time setup to prepare your Mac."
    echo "Your involvement may be needed to approve installations or enter your password."
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
        echo "A software update popup will appear. Please click 'Install'."
        xcode-select --install
        
        # Wait for installation with a timeout
        echo -n "Waiting for installation to complete (this can take several minutes)..."
        timeout_seconds=900 # 15 minutes
        start_time=$(date +%s)
        while ! xcode-select -p &>/dev/null; do
            current_time=$(date +%s)
            elapsed=$((current_time - start_time))
            if [ $elapsed -ge $timeout_seconds ]; then
                error_echo "\nXcode installation timed out. Please install them manually from the terminal with 'xcode-select --install' and run this script again."
                exit 1
            fi
            echo -n "."
            sleep 5
        done
        echo ""
        success_echo "Xcode Command Line Tools installed."
    else
        success_echo "Xcode Command Line Tools already installed."
    fi

    # --- 3. Install/Update Homebrew ---
    step_echo "Checking for Homebrew package manager..."
    if ! command -v brew &>/dev/null; then
        warn_echo "Homebrew is not installed. Installing now..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        
        # Configure Homebrew path for this session
        if [[ "$(uname -m)" == "arm64" ]]; then # Apple Silicon
            eval "$(/opt/homebrew/bin/brew shellenv)"
        else # Intel
            eval "$(/usr/local/bin/brew shellenv)"
        fi
        
        if ! command -v brew &>/dev/null; then
             error_echo "Homebrew installation failed to configure correctly. Please restart your terminal and run the app again."
             exit 1
        fi
        success_echo "Homebrew installed."
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
            echo "  Installing ${pkg}..."
            if brew install ${pkg}; then
                success_echo "Installed ${pkg}."
            else
                error_echo "Failed to install ${pkg}. Please check Homebrew logs and run again."
                exit 1
            fi
        fi
    done

    # --- 5. Setup Application Files ---
    step_echo "Setting up application files..."
    if [ -d "$APP_DIR" ]; then
        warn_echo "Existing directory found. Removing for a clean installation."
        rm -rf "$APP_DIR"
    fi
    if ! git clone "$REPO_URL" "$APP_DIR"; then
        error_echo "Git clone failed. Falling back to ZIP download."
        zip_url="https://github.com/team-slide/Innioasis-Updater/archive/refs/heads/main.zip"
        tmp_zip="/tmp/innioasis_updater.zip"
        if ! curl -L --fail "$zip_url" -o "$tmp_zip"; then
            error_echo "Failed to download ZIP file. Cannot continue."
            exit 1
        fi
        mkdir -p "$APP_DIR"
        unzip -q "$tmp_zip" -d "/tmp"
        unzipped_dir="/tmp/Innioasis-Updater-main"
        mv "$unzipped_dir"/* "$APP_DIR"/
        rm -rf "$unzipped_dir" "$tmp_zip"
    fi
    success_echo "Application files set up in '$APP_DIR'."
    cd "$APP_DIR"

    # --- 6. Setup Python Virtual Environment and Dependencies ---
    step_echo "Setting up Python environment..."
    PYTHON_EXEC="$HOMEBREW_PREFIX/bin/python3"
    
    echo "  Creating Python virtual environment..."
    if ! "$PYTHON_EXEC" -m venv "$VENV_DIR"; then
        warn_echo "Failed to create virtual environment. Attempting to self-heal by reinstalling Python..."
        brew reinstall python
        if ! "$PYTHON_EXEC" -m venv "$VENV_DIR"; then
            error_echo "Failed to create virtual environment even after reinstalling Python. Please check your Homebrew setup."
            exit 1
        fi
    fi
    success_echo "Virtual environment created."
    
    source "$VENV_DIR/bin/activate"
    python3 -m pip install --upgrade pip wheel setuptools
    
    echo "  Installing Python dependencies from requirements.txt..."
    export LDFLAGS="-L$(brew --prefix openssl)/lib -L$(brew --prefix libusb)/lib -L$(brew --prefix libffi)/lib"
    export CPPFLAGS="-I$(brew --prefix openssl)/include -I$(brew --prefix libusb)/include -I$(brew --prefix libffi)/include"
    export PKG_CONFIG_PATH="$(brew --prefix openssl)/lib/pkgconfig:$(brew --prefix libusb)/lib/pkgconfig:$(brew --prefix libffi)/lib/pkgconfig"
    
    if ! python3 -m pip install --no-cache-dir -r requirements.txt; then
        warn_echo "Initial installation of Python packages failed. This can happen on some systems."
        echo "  Attempting automated troubleshooting..."
        echo "  Running 'brew doctor' to check for common issues..."
        brew doctor
        echo "  Updating Homebrew and all installed packages..."
        brew update && brew upgrade
        
        warn_echo "Retrying Python package installation..."
        if ! python3 -m pip install --no-cache-dir -r requirements.txt; then
            error_echo "Failed to install Python dependencies after retry. Please review the errors above and report them on the project's GitHub page."
            deactivate
            exit 1
        fi
    fi
    
    step_echo "Verifying Python package installation..."
    if ! python3 -c "import tkinter, PIL, scrypt, numpy"; then
         error_echo "Verification failed! One or more key Python packages failed to import correctly. The application may not run."
         deactivate
         exit 1
    fi
    success_echo "Key Python packages verified successfully."
    
    unset LDFLAGS CPPFLAGS PKG_CONFIG_PATH
    success_echo "All Python dependencies installed."
    deactivate

    # --- 7. Create Completion Marker & Finish ---
    step_echo "Finalizing setup..."
    touch "$COMPLETION_MARKER"
    success_echo "Completion marker created."
    echo ""
    echo "=========================================="
    success_echo "  Setup Complete!"
    echo "=========================================="
    echo "The application will now launch. You can close this terminal window once it's running."
    sleep 3
}

# ==============================================================================
# SCRIPT ENTRY POINT & MAIN LAUNCHER LOGIC
# This part runs every time the .app is double-clicked.
# ==============================================================================

# --- Argument Parser ---
# If the script is called with '--run-setup', it means we are in the terminal
# window that the main app logic opened. We just run the setup function.
if [ "$1" == "--run-setup" ]; then
    run_full_setup
    
    # After setup, launch the app.
    cd "$APP_DIR"
    source "$VENV_DIR/bin/activate"
    nohup python3 updater.py > /dev/null 2>&1 &
    exit 0
fi

# --- Main App Logic (runs from the .app bundle) ---

# 1. Handle moving the application to /Applications folder.
CURRENT_APP_PATH=$(cd "$(dirname "$0")/../.." && pwd)
DESTINATION_PATH="/Applications/$APP_NAME"

if [ "$CURRENT_APP_PATH" != "$DESTINATION_PATH" ]; then
    ANSWER=$(osascript -e 'display dialog "Would you like to move Innioasis Updater to your Applications folder? This is recommended." buttons {"No", "Yes"} default button "Yes" with icon 1')
    if [ "$ANSWER" = "button returned:Yes" ]; then
        osascript <<EOF
tell application "System Events"
    try
        do shell script "cp -Rf \\\"$CURRENT_APP_PATH\\\" \\\"/Applications/\\\"" with administrator privileges
        display dialog "Successfully moved to Applications folder. Please run the app from there." buttons {"OK"} default button "OK"
        tell application "Finder" to open folder "Applications" of startup disk
    on error errmsg
        display dialog "Failed to move the application. Error: " & errmsg buttons {"OK"} default button "OK"
    end try
end tell
EOF
        exit 0
    fi
fi

# 2. Check if setup has been completed.
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
    echo "First run detected. Initiating setup process."
    
    # Get the full path to this script itself to pass to the new terminal.
    THIS_SCRIPT_PATH=$(cd "$(dirname "$0")" && pwd)/$(basename "$0")

    # Use AppleScript to inform the user and then open Terminal to run the setup function.
    osascript <<EOF
tell application "System Events"
    display dialog "Welcome to Innioasis Updater!\n\nA one-time setup is required to install necessary components. A Terminal window will now open to complete the installation automatically." buttons {"Begin Setup"} default button "Begin Setup" with icon 1
end tell

tell application "Terminal"
    activate
    -- This command tells the new terminal to run this same script file, but with the
    -- '--run-setup' argument, which will trigger the setup function.
    do script "bash '${THIS_SCRIPT_PATH}' --run-setup"
end tell
EOF
    # The main script's job is done; the new terminal window has taken over.
    exit 0
fi

