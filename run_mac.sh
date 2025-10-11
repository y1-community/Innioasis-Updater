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

# Check if running under Rosetta and provide appropriate warnings
check_rosetta() {
    if [[ "$(uname -m)" == "arm64" ]] && [[ "$(arch)" == "i386" ]]; then
        warn_echo "Running under Rosetta 2 (x86_64 emulation on Apple Silicon)"
        log_message "   This may cause compatibility issues with some packages."
        log_message "   Consider running this script natively on Apple Silicon if possible."
        return 0
    fi
    return 1
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

    # Check for Rosetta and provide appropriate warnings
    check_rosetta

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
    ARCH=$(uname -m)
    log_message "   Detected architecture: $ARCH"
    
    BREW_PREFIX=""
    if [[ "$ARCH" == "arm64" ]]; then # Apple Silicon
        BREW_PREFIX="/opt/homebrew"
        log_message "   Using Apple Silicon Homebrew path: $BREW_PREFIX"
    elif [[ "$ARCH" == "x86_64" ]]; then # Intel
        BREW_PREFIX="/usr/local"
        log_message "   Using Intel Homebrew path: $BREW_PREFIX"
    else
        warn_echo "Unknown architecture: $ARCH. Defaulting to Intel path."
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
        log_message "   Detected shell: $CURRENT_SHELL"
        
        # Determine the appropriate shell profile file
        if [ "$CURRENT_SHELL" = "zsh" ]; then
            # Try .zprofile first, then .zshrc as fallback
            if [ -f "$HOME/.zprofile" ]; then
                SHELL_PROFILE="$HOME/.zprofile"
            else
                SHELL_PROFILE="$HOME/.zshrc"
            fi
        elif [ "$CURRENT_SHELL" = "bash" ]; then
            # Try .bash_profile first, then .bashrc as fallback
            if [ -f "$HOME/.bash_profile" ]; then
                SHELL_PROFILE="$HOME/.bash_profile"
            else
                SHELL_PROFILE="$HOME/.bashrc"
            fi
        else
            SHELL_PROFILE="$HOME/.profile" # Fallback
        fi
        log_message "   Using shell profile: $SHELL_PROFILE"
        
        SHELLENV_CMD="eval \"\$($BREW_CMD_PATH shellenv)\""
        if ! grep -qF -- "$SHELLENV_CMD" "$SHELL_PROFILE" 2>/dev/null; then
            log_message "   Adding Homebrew to your shell profile for future sessions..."
            echo -e "\n# Added by Innioasis Updater Setup" >> "$SHELL_PROFILE"
            echo "$SHELLENV_CMD" >> "$SHELL_PROFILE"
        else
            log_message "   Homebrew is already configured in your shell profile."
        fi
    }

    # Check for Homebrew in multiple possible locations
    BREW_FOUND=false
    BREW_CMD_PATH=""
    
    # Check standard locations first
    if [ -x "$BREW_PREFIX/bin/brew" ]; then
        BREW_CMD_PATH="$BREW_PREFIX/bin/brew"
        BREW_FOUND=true
        log_message "   Found Homebrew at standard location: $BREW_CMD_PATH"
    # Check if brew command is available in PATH (might be installed elsewhere)
    elif command -v brew &>/dev/null; then
        BREW_CMD_PATH=$(command -v brew)
        BREW_FOUND=true
        log_message "   Found Homebrew in PATH: $BREW_CMD_PATH"
    # Check alternative locations for edge cases
    elif [ -x "/usr/local/bin/brew" ] && [[ "$ARCH" == "x86_64" ]]; then
        BREW_CMD_PATH="/usr/local/bin/brew"
        BREW_FOUND=true
        log_message "   Found Homebrew at alternative Intel location: $BREW_CMD_PATH"
    elif [ -x "/opt/homebrew/bin/brew" ] && [[ "$ARCH" == "arm64" ]]; then
        BREW_CMD_PATH="/opt/homebrew/bin/brew"
        BREW_FOUND=true
        log_message "   Found Homebrew at alternative Apple Silicon location: $BREW_CMD_PATH"
    fi
    
    if ! $BREW_FOUND; then
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
    
    # Essential packages (required for basic functionality)
    # Install latest Python version to ensure compatibility with modern packages
    ESSENTIAL_PACKAGES="python@3.13 libusb openssl libffi"
    # Optional packages (nice to have but not critical)
    OPTIONAL_PACKAGES="rust cmake pkg-config android-platform-tools"
    
    # Install essential packages with failure tolerance
    for pkg in $ESSENTIAL_PACKAGES; do
        if brew list --formula | grep -q "^${pkg}\$"; then
            success_echo "${pkg} is already installed."
        else
            log_message "   Installing essential package: ${pkg}..."
            if brew install ${pkg} >> "$LOG_FILE" 2>&1; then
                success_echo "Installed ${pkg}."
                
                # Special handling for Python installations
                if [[ "$pkg" == python@* ]]; then
                    log_message "   Python package installed - verifying installation..."
                    PYTHON_VERSION_INSTALLED=$(brew --prefix "$pkg")/bin/python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>/dev/null || echo "unknown"
                    log_message "   Installed Python version: $PYTHON_VERSION_INSTALLED"
                    
                    # Check Tkinter support for the newly installed Python
                    if "$(brew --prefix "$pkg")/bin/python3" -c "import tkinter" 2>/dev/null; then
                        log_message "   ✓ Tkinter support confirmed for installed Python"
                    else
                        warn_echo "   ⚠ Tkinter not available in installed Python - GUI may not work"
                    fi
                fi
            else
                error_echo "Failed to install essential package ${pkg}. This may cause issues."
                warn_echo "Continuing setup - you may need to install ${pkg} manually later."
            fi
        fi
    done
    
    # Install optional packages with failure tolerance
    for pkg in $OPTIONAL_PACKAGES; do
        if brew list --formula | grep -q "^${pkg}\$"; then
            success_echo "${pkg} is already installed."
        else
            log_message "   Installing optional package: ${pkg}..."
            if brew install ${pkg} >> "$LOG_FILE" 2>&1; then
                success_echo "Installed ${pkg}."
            else
                warn_echo "Failed to install optional package ${pkg}. Continuing without it."
                log_message "   Note: ${pkg} is optional and the application should still work without it."
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
    
    # Create .no_updates file for new users to decide on automatic updates
    echo "Automatic utility updates disabled by default for new users" > "$APP_DIR/.no_updates"
    log_message "Created .no_updates file - new users can enable automatic updates in the app settings"

    # --- 5. Setup Python Virtual Environment ---
    step_echo "Setting up Python environment..."
    
    # Try to find the best Python 3 installation
    PYTHON_EXEC=""
    
    # First, check if we installed Python@3.13 via Homebrew (latest version with best compatibility)
    if command -v brew &>/dev/null; then
        # Check for Python 3.13 specifically (latest version with best package compatibility)
        PYTHON_313_PATHS=(
            "$(brew --prefix python@3.13)/bin/python3"
            "$(brew --prefix python@3.13)/bin/python3.13"
        )
        
        for python_path in "${PYTHON_313_PATHS[@]}"; do
            if [ -x "$python_path" ]; then
                PYTHON_EXEC="$python_path"
                log_message "   Using Homebrew Python 3.13: $PYTHON_EXEC"
                break
            fi
        done
        
        # If Python 3.13 not found, try other Homebrew Python versions
        if [ -z "$PYTHON_EXEC" ]; then
            for version in "3.12" "3.11" "3.10"; do
                PYTHON_PATH="$(brew --prefix python@${version})/bin/python3"
                if [ -x "$PYTHON_PATH" ]; then
                    PYTHON_EXEC="$PYTHON_PATH"
                    log_message "   Using Homebrew Python ${version}: $PYTHON_EXEC"
                    break
                fi
            done
        fi
        
        # Fallback to generic Homebrew Python
        if [ -z "$PYTHON_EXEC" ]; then
            BREW_PYTHON_PATH="$(brew --prefix)/bin/python3"
            if [ -x "$BREW_PYTHON_PATH" ]; then
                PYTHON_EXEC="$BREW_PYTHON_PATH"
                log_message "   Using Homebrew Python: $PYTHON_EXEC"
            fi
        fi
    fi
    
    # If Homebrew Python not found, try system Python
    if [ -z "$PYTHON_EXEC" ]; then
        if command -v python3 &>/dev/null; then
            PYTHON_EXEC="python3"
            log_message "   Using system Python: $PYTHON_EXEC"
        fi
    fi
    
    # If still no Python found, try specific paths
    if [ -z "$PYTHON_EXEC" ]; then
        for python_path in "/usr/bin/python3" "/usr/local/bin/python3" "/opt/homebrew/bin/python3"; do
            if [ -x "$python_path" ]; then
                PYTHON_EXEC="$python_path"
                log_message "   Using Python from: $PYTHON_EXEC"
                break
            fi
        done
    fi
    
    if [ -z "$PYTHON_EXEC" ]; then
        error_echo "No Python 3 installation found. Please install Python 3."
        exit 1
    fi
    
    # Log Python version and architecture info
    PYTHON_VERSION=$("$PYTHON_EXEC" -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
    PYTHON_ARCH=$("$PYTHON_EXEC" -c "import platform; print(platform.machine())")
    log_message "   Python version: $PYTHON_VERSION"
    log_message "   Python architecture: $PYTHON_ARCH"
    
    # Check Tkinter compatibility
    if "$PYTHON_EXEC" -c "import tkinter" 2>/dev/null; then
        log_message "   ✓ Tkinter support confirmed"
    else
        warn_echo "   ⚠ Tkinter not available - GUI components may not work"
        log_message "   This may be due to missing tkinter support in the Python installation"
    fi
    
    if ! "$PYTHON_EXEC" -m venv "$VENV_DIR"; then
        error_echo "Failed to create Python virtual environment. Check log."
        exit 1
    fi
    success_echo "Virtual environment created."
    
    source "$VENV_DIR/bin/activate"
    
    # Ensure we're using the correct Python in the virtual environment
    VENV_PYTHON="$VENV_DIR/bin/python"
    if [ -x "$VENV_PYTHON" ]; then
        log_message "   Using virtual environment Python: $VENV_PYTHON"
        python3 -m pip install --upgrade pip wheel setuptools >> "$LOG_FILE" 2>&1
    else
        error_echo "Virtual environment Python not found. Setup failed."
        exit 1
    fi
    
    # Create a temporary requirements file without problematic packages for older Python versions
    TEMP_REQUIREMENTS="/tmp/innioasis_requirements_temp.txt"
    cp requirements.txt "$TEMP_REQUIREMENTS"
    
    # Check Python version compatibility for packages
    PYTHON_MAJOR_MINOR=$("$PYTHON_EXEC" -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
    log_message "   Current Python version: $PYTHON_MAJOR_MINOR"
    
    # Check if we have Python 3.10+ (required for shiboken6 and pyside6)
    PYTHON_VERSION_OK=false
    if python3 -c "import sys; exit(0 if sys.version_info >= (3, 10) else 1)"; then
        PYTHON_VERSION_OK=true
        log_message "   ✓ Python 3.10+ detected - all dependencies should be compatible"
    else
        log_message "   ⚠ Python < 3.10 detected - some packages may not be available"
    fi
    
    # Only remove problematic packages if we don't have Python 3.10+
    if ! $PYTHON_VERSION_OK; then
        log_message "   Removing packages that require Python 3.10+..."
        PROBLEMATIC_PACKAGES=("shiboken6" "pyside6")
        for pkg in "${PROBLEMATIC_PACKAGES[@]}"; do
            if grep -q "^${pkg}$" "$TEMP_REQUIREMENTS"; then
                log_message "   Removing ${pkg} due to Python version incompatibility"
                sed -i '' "/^${pkg}$/d" "$TEMP_REQUIREMENTS"
            fi
        done
    else
        log_message "   All packages should be compatible with Python $PYTHON_MAJOR_MINOR"
    fi
    
    log_message "   Installing Python dependencies from requirements.txt..."
    export LDFLAGS="-L$(brew --prefix openssl)/lib"
    export CPPFLAGS="-I$(brew --prefix openssl)/include"
    
    # Try to install dependencies with fallback handling
    DEPENDENCY_SUCCESS=true
    if ! python3 -m pip install --no-cache-dir -r "$TEMP_REQUIREMENTS" >> "$LOG_FILE" 2>&1; then
        warn_echo "Some Python dependencies failed to install. Trying individual packages..."
        
        # Try installing packages individually to identify problematic ones
        while IFS= read -r package; do
            if [[ "$package" =~ ^[[:space:]]*$ ]] || [[ "$package" =~ ^[[:space:]]*# ]]; then
                continue  # Skip empty lines and comments
            fi
            
            log_message "   Attempting to install: $package"
            
            # Special handling for known problematic packages
            if [[ "$package" == "shiboken6" ]]; then
                log_message "   Note: shiboken6 requires Python 3.10+ and may take longer to install"
            elif [[ "$package" == "pyside6" ]]; then
                log_message "   Note: pyside6 requires Python 3.10+ and may take longer to install"
            fi
            
            if python3 -m pip install --no-cache-dir "$package" >> "$LOG_FILE" 2>&1; then
                log_message "   ✓ Successfully installed: $package"
            else
                # Provide specific guidance for known problematic packages
                if [[ "$package" == "shiboken6" ]] || [[ "$package" == "pyside6" ]]; then
                    warn_echo "   ⚠ Failed to install: $package"
                    log_message "   This may be due to Python version requirements or build dependencies"
                    log_message "   The application should still work without GUI components"
                else
                    warn_echo "   ⚠ Failed to install: $package (continuing without it)"
                fi
                DEPENDENCY_SUCCESS=false
            fi
        done < "$TEMP_REQUIREMENTS"
    fi
    
    # Clean up temp file
    rm -f "$TEMP_REQUIREMENTS"
    
    unset LDFLAGS CPPFLAGS
    
    if $DEPENDENCY_SUCCESS; then
        success_echo "All Python dependencies installed successfully."
    else
        warn_echo "Some Python dependencies failed to install, but core functionality should still work."
        log_message "   Check the log file for details about which packages failed: $LOG_FILE"
    fi
    
    deactivate

    # --- 6. Finalize ---
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
    nohup python3 "$APP_DIR/firmware_downloader.py" >/dev/null 2>&1 &
    exit 0
else
    # --- FIRST RUN: Setup is needed ---
    run_full_setup
    
    # After setup, launch the app for the first time.
    log_message "Launching firmware_downloader.py..."
    cd "$APP_DIR"
    source "$VENV_DIR/bin/activate"
    nohup python3 "$APP_DIR/firmware_downloader.py" >/dev/null 2>&1 &
    exit 0
fi
