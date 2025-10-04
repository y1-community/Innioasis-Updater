#!/bin/bash

# ==============================================================================
# Innioasis Updater - Robust, Context-Aware Setup & Launcher v6.5
#
# This script provides a one-time, highly automated setup process. It allows
# the official Homebrew installer to run interactively to handle its own
# password prompts, ensuring a reliable installation.
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

    show_dialog_if_needed "Welcome to Innioasis Updater! The setup process is starting. Some steps, like the Homebrew installation, will require your interaction."

    # --- 1. Install Xcode Command Line Tools ---
    step_echo "Checking for Xcode Command Line Tools..."
    if ! xcode-select -p &>/dev/null; then
        warn_echo "Xcode Command Line Tools are required."
        log_message "A software update popup will appear. Please click 'Install' and wait."
        
        xcode-select --install

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

    # --- 2. Install, Configure, or Update Homebrew ---
    step_echo "Checking for Homebrew package manager..."
    
    # Define Homebrew paths based on CPU architecture
    BREW_PREFIX=""
    if [[ "$(uname -m)" == "arm64" ]]; then # Apple Silicon
        BREW_PREFIX="/opt/homebrew"
    else # Intel
        BREW_PREFIX="/usr/local"
    fi
    BREW_CMD_PATH="$BREW_PREFIX/bin/brew"

    # --- AUTOMATED PATH CONFIGURATION FUNCTION ---
    configure_brew_paths() {
        # 1. Configure for the CURRENT script session
        eval "$($BREW_CMD_PATH shellenv)"
        
        # 2. Configure for FUTURE terminal sessions
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
    }

    # First, check if the Homebrew executable exists at its standard location
    if ! [ -x "$BREW_CMD_PATH" ]; then
        # --- SCENARIO 1: HOMEBREW NOT INSTALLED (INTERACTIVE) ---
        warn_echo "Homebrew not found. Starting interactive installation..."
        log_message "The official Homebrew installer will now run. Please follow its instructions."
        log_message "You will be prompted to enter your password by the installer itself."
        show_dialog_if_needed "The Homebrew installer will now run in the terminal. Please follow its instructions and enter your password when prompted."
        
        # Run the official installer INTERACTIVELY, allowing it to ask for sudo.
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

        # After the user completes the interactive install, we configure the paths.
        step_echo "Configuring new Homebrew installation..."
        configure_brew_paths
    else
        # --- SCENARIO 2: HOMEBREW IS INSTALLED ---
        success_echo "Homebrew installation detected."
        # Check if it's configured in the current shell. If not, fix it.
        if ! command -v brew &>/dev/null; then
            warn_echo "Homebrew is installed but not configured in your shell. Fixing..."
            configure_brew_paths
        fi
        
        success_echo "Homebrew is configured. Skipping update."
    fi

    # Verify that brew is now available before proceeding
    if ! command -v brew &>/dev/null; then
        error_echo "Failed to find the 'brew' command after installation. Please run the script again in a new terminal window."
        exit 1
    fi

    # --- 3. Install Brew Dependencies ---
    step_echo "Installing required tools with Homebrew..."
    BREW_PACKAGES="python python-tk libusb openssl libffi rust cmake pkg-config android-platform-tools"
    for pkg in $BREW_PACKAGES; do
        if brew list --formula | grep -q "^${pkg}\$"; then
            success_echo "${pkg} is already installed."
        else
            log_message "   Downloading resources we need for Innioasis Updater and ${pkg} (This may take 5-60 minutes depending on download speeds."
            if brew install ${pkg} >> "$LOG_FILE" 2>&1; then
                success_echo "Installed ${pkg}."
            else
                error_echo "Failed to install ${pkg}. Check log for details: $LOG_FILE"
                exit 1
            fi
        fi
    done

    # --- 4. Setup Application Files ---
    step_echo "Setting up application files from Git..."
    rm -rf "$APP_DIR" # Always start clean
    if ! git clone "$REPO_URL" "$APP_DIR" >> "$LOG_FILE" 2>&1; then
        error_echo "Git clone failed. Check log for details: $LOG_FILE"
        exit 1
    fi
    success_echo "Application files cloned to '$APP_DIR'."
    cd "$APP_DIR"
    
    # Create version file to prevent first-time dialog
    echo "1.6.1" > "$APP_DIR/.version"

    # --- 5. Setup Python Virtual Environment ---
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

    # --- 6. Finalize ---
    step_echo "Finalizing setup..."
    touch "$COMPLETION_MARKER"
    
    # Create .no_updates file for new users to decide on automatic updates
    echo "Automatic utility updates disabled by default for new users" > "$APP_DIR/.no_updates"
    log_message "Created .no_updates file - new users can enable automatic updates in the app settings"
    
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
