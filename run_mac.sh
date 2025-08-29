#!/bin/bash

# ==============================================================================
# Innioasis Updater - Robust, Context-Aware Setup & Launcher v6.2
#
# This script provides a one-time, highly automated setup process. It asks
# for sudo access once upfront, handles all subsequent steps non-interactively,
# and automatically configures the user's shell environment for Homebrew.
# ==============================================================================

# --- Configuration ---
APP_DIR="$HOME/Library/Application Support/Innioasis Updater"
REPO_URL="https://github.com/team-slide/Innioasis-Updater.git"
VENV_DIR="$APP_DIR/venv"
PYTHON_SCRIPT="$APP_DIR/updater.py"
COMPLETION_MARKER="$VENV_DIR/.mac_setup_complete"
LOG_FILE="/tmp/innioasis_setup.log"

# --- Setup UI and Helper Functions ---
INTERACTIVE_MODE=false
if [ -t 0 ]; then
    INTERACTIVE_MODE=true
fi

# Terminal styles
BLUE='\033[0;34m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; NC='\033[0m'

# Unified logging for both terminal and files
log_message() {
    echo -e "$1" | tee -a "$LOG_FILE"
}

step_echo() { log_message "\n${BLUE}▶ $1${NC}"; }
success_echo() { log_message "${GREEN}✓ $1${NC}"; }
warn_echo() { log_message "${YELLOW}⚠️ $1${NC}"; }
error_echo() { log_message "${RED}✗ $1${NC}"; }

# Displays a GUI dialog only if not in an interactive terminal
show_dialog_if_needed() {
    if ! $INTERACTIVE_MODE; then
        osascript -e "display dialog \"$1\" buttons {\"OK\"} default button \"OK\" with icon 1" > /dev/null
    fi
}

# ==============================================================================
# SECTION 1: FULL SETUP LOGIC
# ==============================================================================
run_full_setup() {
    clear
    # Clean up old log
    rm -f "$LOG_FILE"

    echo "=========================================="
    echo "  Welcome to the Innioasis Updater Setup"
    echo "=========================================="
    echo "This script will perform a one-time, automated setup."
    echo "Log file will be saved to: $LOG_FILE"
    echo

    show_dialog_if_needed "Welcome to Innioasis Updater! The setup process is starting. Administrator access is required to install necessary tools."

    # --- 1. Acquire Sudo Privileges Upfront ---
    step_echo "Requesting administrator privileges..."
    echo "Please enter your Mac's password to allow installation of system tools like Homebrew."
    if ! sudo -v; then
        error_echo "Failed to obtain administrator privileges. Cannot continue."
        show_dialog_if_needed "Setup failed: Could not get administrator privileges."
        exit 1
    fi
    # Keep sudo session alive in the background
    while true; do sudo -n true; sleep 60; kill -0 "$$" || exit; done &
    SUDO_KEEPALIVE_PID=$!
    trap 'kill "$SUDO_KEEPALIVE_PID"' EXIT
    success_echo "Administrator privileges acquired."

    # --- 2. Install Xcode Command Line Tools ---
    step_echo "Checking for Xcode Command Line Tools..."
    if ! xcode-select -p &>/dev/null; then
        warn_echo "Xcode Command Line Tools are required."
        log_message "A software update popup will appear. Please click 'Install' and wait."
        
        # This is the only mandatory GUI interaction
        xcode-select --install

        # Poll until the installation is complete
        echo -n "Waiting for Xcode Tools installation to complete (this can take several minutes)..."
        while ! xcode-select -p &>/dev/null; do
            echo -n "."
            sleep 5
        done
        echo ""
        success_echo "Xcode Command Line Tools installed."
    else
        success_echo "Xcode Command Line Tools already installed."
    fi

    # --- 3. Install/Update Homebrew Non-Interactively ---
    step_echo "Checking for Homebrew package manager..."
    if ! command -v brew &>/dev/null; then
        warn_echo "Homebrew not found. Installing now (this may take 5-15 minutes)..."
        show_dialog_if_needed "Now installing Homebrew. This is a one-time process and may take several minutes. Please wait."
        
        # Use the official non-interactive method
        if ! NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" >> "$LOG_FILE" 2>&1; then
            error_echo "Homebrew installation failed. Check the log file for details: $LOG_FILE"
            show_dialog_if_needed "Homebrew installation failed. Please check the log file for details."
            exit 1
        fi
        
        # --- AUTOMATED PATH CONFIGURATION ---
        # The installer finishes by telling the user to add brew to their path.
        # We do this automatically for the current session and all future sessions.
        step_echo "Configuring Homebrew environment..."
        BREW_PREFIX=""
        if [[ "$(uname -m)" == "arm64" ]]; then # Apple Silicon
            BREW_PREFIX="/opt/homebrew"
        else # Intel
            BREW_PREFIX="/usr/local"
        fi
        BREW_CMD_PATH="$BREW_PREFIX/bin/brew"

        # 1. Configure for the CURRENT script session using Homebrew's recommended method
        eval "$($BREW_CMD_PATH shellenv)"
        
        # 2. Configure for FUTURE terminal sessions by adding to the correct shell profile
        SHELL_PROFILE=""
        CURRENT_SHELL=$(basename "$SHELL")
        if [ "$CURRENT_SHELL" = "zsh" ]; then
            SHELL_PROFILE="$HOME/.zprofile"
        elif [ "$CURRENT_SHELL" = "bash" ]; then
            SHELL_PROFILE="$HOME/.bash_profile"
        else
            SHELL_PROFILE="$HOME/.profile" # Fallback
        fi
        log_message "   Detected shell profile: $SHELL_PROFILE"
        
        SHELLENV_CMD="eval \"\$($BREW_CMD_PATH shellenv)\""
        if ! grep -qF -- "$SHELLENV_CMD" "$SHELL_PROFILE" 2>/dev/null; then
            log_message "   Adding Homebrew to your shell profile for future sessions..."
            echo -e "\n# Added by Innioasis Updater Setup" >> "$SHELL_PROFILE"
            echo "$SHELLENV_CMD" >> "$SHELL_PROFILE"
        else
            log_message "   Homebrew is already configured in your shell profile."
        fi

        # 3. Verify that brew is now available
        if ! command -v brew &>/dev/null; then
            error_echo "Homebrew was installed, but 'brew' command is still not available. A new terminal session may be required."
            show_dialog_if_needed "Homebrew installation finished, but the command is not working. Please try running the script again."
            exit 1
        fi

        success_echo "Homebrew installed and configured."
    else
        success_echo "Homebrew already installed. Updating..."
        brew update >> "$LOG_FILE" 2>&1
        success_echo "Homebrew updated."
    fi

    # --- 4. Install Brew Dependencies ---
    step_echo "Installing required tools with Homebrew..."
    BREW_PACKAGES="python python-tk libusb openssl libffi rust cmake pkg-config android-platform-tools"
    for pkg in $BREW_PACKAGES; do
        if brew list --formula | grep -q "^${pkg}\$"; then
            success_echo "${pkg} is already installed."
        else
            log_message "   Installing ${pkg}..."
            if brew install ${pkg} >> "$LOG_FILE" 2>&1; then
                success_echo "Installed ${pkg}."
            else
                error_echo "Failed to install ${pkg}. Check log for details: $LOG_FILE"
                exit 1
            fi
        fi
    done

    # --- 5. Setup Application Files ---
    step_echo "Setting up application files from Git..."
    rm -rf "$APP_DIR" # Always start clean
    if ! git clone "$REPO_URL" "$APP_DIR" >> "$LOG_FILE" 2>&1; then
        error_echo "Git clone failed. Check log for details: $LOG_FILE"
        exit 1
    fi
    success_echo "Application files cloned to '$APP_DIR'."
    cd "$APP_DIR"

    # --- 6. Setup Python Virtual Environment ---
    step_echo "Setting up Python environment..."
    PYTHON_EXEC="$(brew --prefix)/bin/python3"
    
    if ! "$PYTHON_EXEC" -m venv "$VENV_DIR"; then
        error_echo "Failed to create Python virtual environment. Check log."
        exit 1
    fi
    success_echo "Virtual environment created."
    
    source "$VENV_DIR/bin/activate"
    python3 -m pip install --upgrade pip wheel setuptools >> "$LOG_FILE" 2>&1
    
    log_message "   Installing Python dependencies from requirements.txt..."
    export LDFLAGS="-L$(brew --prefix openssl)/lib"
    export CPPFLAGS="-I$(brew --prefix openssl)/include"
    
    if ! python3 -m pip install --no-cache-dir -r requirements.txt >> "$LOG_FILE" 2>&1; then
        error_echo "Failed to install Python dependencies. Check log."
        deactivate
        exit 1
    fi
    
    unset LDFLAGS CPPFLAGS
    success_echo "All Python dependencies installed."
    deactivate

    # --- 7. Finalize ---
    step_echo "Finalizing setup..."
    touch "$COMPLETION_MARKER"
    
    echo
    echo "=========================================="
    success_echo "  Setup Complete!"
    echo "=========================================="
    echo "You can run this script again anytime to launch the application."
    show_dialog_if_needed "Setup Complete! The application will now launch. You can run this script again in the future to open the app directly."
    sleep 2
}

# ==============================================================================
# SCRIPT ENTRY POINT
# ==============================================================================

# Check if setup has been completed.
if [ -f "$COMPLETION_MARKER" ]; then
    # --- FAST PATH: Setup is complete, run the app silently ---
    cd "$APP_DIR"
    source "$VENV_DIR/bin/activate"
    nohup python3 "$PYTHON_SCRIPT" >/dev/null 2>&1 &
    exit 0
else
    # --- FIRST RUN: Setup is needed ---
    run_full_setup
    
    # After setup, launch the app for the first time.
    log_message "Launching the application..."
    cd "$APP_DIR"
    source "$VENV_DIR/bin/activate"
    nohup python3 "$PYTHON_SCRIPT" >/dev/null 2>&1 &
    exit 0
fi

