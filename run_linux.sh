#!/bin/bash
# Innioasis Updater Linux Launcher
# Supports Ubuntu, Linux Mint, ChromeOS/FydeOS Linux, Arch, SteamOS, and other distributions
# Based on MTKclient requirements and Linux distribution best practices

# Don't exit on errors - handle them gracefully
set +e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# User-facing verbosity: concise by default.
# Set INSTALL_VERBOSE=1 for detailed diagnostics.
INSTALL_VERBOSE="${INSTALL_VERBOSE:-0}"

# Logging function
log() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1" >&2
}

warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

step() {
    echo
    echo -e "${BLUE}==>${NC} $1"
}

vlog() {
    if [ "$INSTALL_VERBOSE" = "1" ]; then
        log "$1"
    fi
}

run_cmd() {
    # Usage: run_cmd "description" "command"
    local description="$1"
    local command_str="$2"
    if [ "$INSTALL_VERBOSE" = "1" ]; then
        log "$description"
        eval "$command_str"
    else
        log "$description"
        eval "$command_str" >/dev/null 2>&1
    fi
}

elapsed_seconds() {
    local start_ts="$1"
    local end_ts
    end_ts=$(date +%s)
    echo $((end_ts - start_ts))
}

TOTAL_PHASES=10
CURRENT_PHASE=0
phase() {
    CURRENT_PHASE=$((CURRENT_PHASE + 1))
    step "[$CURRENT_PHASE/$TOTAL_PHASES] $1"
}

# Keep crypto dependency troubleshooting quiet by default.
# Set PYCRYPTO_VERBOSE=1 to override, otherwise it follows INSTALL_VERBOSE.
PYCRYPTO_VERBOSE="${PYCRYPTO_VERBOSE:-$INSTALL_VERBOSE}"
# Optional crypto package install. Keep disabled by default now that crypto is lazy-loaded.
INSTALL_PYCRYPTO="${INSTALL_PYCRYPTO:-0}"
pycrypto_log() {
    if [ "$PYCRYPTO_VERBOSE" = "1" ]; then
        log "$1"
    fi
}

# Use first available command from a candidate list
resolve_cmd() {
    for candidate in "$@"; do
        if command -v "$candidate" >/dev/null 2>&1; then
            echo "$candidate"
            return 0
        fi
    done
    return 1
}

# Return 0 for immutable/ostree style systems where package managers may be read-only
is_immutable_system() {
    [ -e /run/ostree-booted ] || [ -f /usr/lib/os-release ] && grep -qi "ostree" /usr/lib/os-release 2>/dev/null
}

# Ensure pip tooling exists for the provided Python executable
ensure_pip_tools() {
    local py_bin="${1:-python3}"

    if ! command -v "$py_bin" >/dev/null 2>&1; then
        warning "Python executable not found: $py_bin"
        return 1
    fi

    if "$py_bin" -m pip --version >/dev/null 2>&1; then
        return 0
    fi

    log "pip not available for $py_bin, attempting bootstrap..."
    if "$py_bin" -m ensurepip --upgrade >/dev/null 2>&1; then
        success "Bootstrapped pip using ensurepip"
    else
        warning "ensurepip failed for $py_bin"
    fi

    if "$py_bin" -m pip --version >/dev/null 2>&1; then
        return 0
    fi

    case "$DISTRO_ID" in
        ubuntu|linuxmint|pop|elementary|zorin|debian|raspbian)
            sudo apt-get update >/dev/null 2>&1 || true
            sudo apt-get install -y python3-pip python3-setuptools python3-venv >/dev/null 2>&1 || true
            ;;
        arch|manjaro|endeavouros|cachyos|garuda|artix)
            sudo pacman -Sy --noconfirm >/dev/null 2>&1 || true
            sudo pacman -S --noconfirm python-pip python-setuptools >/dev/null 2>&1 || true
            ;;
        fedora|rhel|centos|almalinux|rocky|bazzite|ublue-os)
            local dnf_cmd
            dnf_cmd=$(resolve_cmd dnf yum)
            if [ -n "$dnf_cmd" ]; then
                sudo "$dnf_cmd" install -y python3-pip python3-setuptools >/dev/null 2>&1 || true
            fi
            ;;
        opensuse*|sles)
            sudo zypper install -y python3-pip python3-setuptools >/dev/null 2>&1 || true
            ;;
    esac

    if "$py_bin" -m pip --version >/dev/null 2>&1; then
        success "pip is now available for $py_bin"
        return 0
    fi

    warning "pip is still unavailable for $py_bin"
    return 1
}

# Install python packages with graceful fallback and package isolation flags when needed
install_python_packages() {
    local py_bin="$1"
    shift
    local packages=("$@")

    if ! ensure_pip_tools "$py_bin"; then
        warning "Skipping Python package installation: pip unavailable for $py_bin"
        return 1
    fi

    local base_args=("-m" "pip" "install")
    local user_args=()
    if [ "$py_bin" = "python3" ]; then
        user_args+=("--user")
    fi

    if "$py_bin" "${base_args[@]}" "${user_args[@]}" --break-system-packages "${packages[@]}" >/dev/null 2>&1; then
        return 0
    fi
    if "$py_bin" "${base_args[@]}" "${user_args[@]}" "${packages[@]}" >/dev/null 2>&1; then
        return 0
    fi

    return 1
}

# Detect system architecture
detect_architecture() {
    ARCH=$(uname -m)
    case "$ARCH" in
        x86_64)
            ARCH_TYPE="amd64"
            ARCH_BITS="64"
            ;;
        aarch64|arm64)
            ARCH_TYPE="arm64"
            ARCH_BITS="64"
            ;;
        armv7l|armv6l)
            ARCH_TYPE="armhf"
            ARCH_BITS="32"
            ;;
        i386|i686)
            ARCH_TYPE="i386"
            ARCH_BITS="32"
            ;;
        armv5l)
            ARCH_TYPE="armel"
            ARCH_BITS="32"
            ;;
        *)
            ARCH_TYPE="unknown"
            ARCH_BITS="unknown"
            warning "Unknown architecture: $ARCH"
            ;;
    esac
    
    log "Detected architecture: $ARCH ($ARCH_TYPE, $ARCH_BITS-bit)"
}

# Detect Linux distribution
detect_distro() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        DISTRO_ID="$ID"
        DISTRO_VERSION="$VERSION_ID"
        DISTRO_NAME="$NAME"
        DISTRO_ID_LIKE="${ID_LIKE:-}"

        # Special handling for Raspberry Pi OS and known derivatives
        if [ "$ID" = "debian" ] && [ -f /etc/rpi-issue ]; then
            DISTRO_ID="raspbian"
            DISTRO_NAME="Raspberry Pi OS"
        elif [ "$ID" = "cachyos" ]; then
            DISTRO_ID="cachyos"
        elif [ "$ID" = "bazzite" ]; then
            DISTRO_ID="bazzite"
        fi
    elif [ -f /etc/redhat-release ]; then
        DISTRO_ID="rhel"
        DISTRO_NAME="Red Hat Enterprise Linux"
    elif [ -f /etc/debian_version ]; then
        DISTRO_ID="debian"
        DISTRO_NAME="Debian"
    else
        DISTRO_ID="unknown"
        DISTRO_NAME="Unknown Linux Distribution"
    fi
    
    log "Detected distribution: $DISTRO_NAME ($DISTRO_ID)"
}

# Pause before exit to allow user to see error messages
pause_before_exit() {
    echo
    read -p "Press Enter to continue..." -r
}

# Ensure the installer is running from a valid directory.
# If current working directory was removed (or is inside a path we are about to delete),
# switch to a safe location to avoid getcwd-related Python/pip failures.
ensure_safe_working_directory() {
    local install_target="${1:-}"
    local current_dir
    current_dir=$(pwd 2>/dev/null || true)

    if [ -z "$current_dir" ]; then
        warning "Current directory is no longer available; switching to a safe directory."
        cd "$HOME" 2>/dev/null || cd /tmp || return 1
        return 0
    fi

    if [ -n "$install_target" ] && [[ "$current_dir" == "$install_target"* ]]; then
        warning "Installer is running from inside $install_target; switching to home directory."
        cd "$HOME" 2>/dev/null || cd /tmp || return 1
    fi
}

# Check if running as root
check_root() {
    if [ "$EUID" -eq 0 ]; then
        error "This script should not be run as root for security reasons."
        error "Please run as a regular user. The script will use sudo when needed."
        return 1
    fi
    return 0
}

# Detect existing running GUI instance to avoid partial-overwrite races.
check_existing_updater_instance() {
    local pids
    pids=$(pgrep -f "firmware_downloader.py" 2>/dev/null || true)
    if [ -n "$pids" ]; then
        warning "Innioasis Updater is already running (PID(s): $(echo "$pids" | tr '\n' ' '))."
        warning "Please close Innioasis Updater, then run this installer again."
        return 1
    fi
    return 0
}

# Check for partial installations and clean them up
check_and_cleanup_partial_installation() {
    log "Checking for previous partial installations..."
    
    # Get installation directory
    get_install_dir
    ensure_safe_working_directory "$INSTALL_DIR"
    
    local cleanup_needed=false
    
    # Check for incomplete installation directory
    if [ -d "$INSTALL_DIR" ]; then
        # Check if installation is incomplete
        if [ ! -f "$INSTALL_DIR/firmware_downloader.py" ] || [ ! -f "$INSTALL_DIR/README.md" ]; then
            warning "Found incomplete installation directory: $INSTALL_DIR"
            cleanup_needed=true
        else
            log "Found existing complete installation at: $INSTALL_DIR"
            
            # Crypto backends are optional during install because they are lazy-loaded at runtime.
            # Keep existing install even if crypto verification is degraded.
            if [ -d "$INSTALL_DIR/venv" ] && ! verify_pycryptodome_installation "$INSTALL_DIR/venv" 1; then
                warning "Existing install found; crypto backend could not be verified"
                warning "Continuing without forced cleanup (crypto features may be limited)"
            fi
            
            return 0
        fi
    fi
    
    # Check for temporary download directories
    local temp_dirs=("$HOME/innioasis-updater-temp" "/tmp/innioasis-updater-*" "$HOME/.cache/innioasis-updater")
    for temp_dir in "${temp_dirs[@]}"; do
        if ls $temp_dir >/dev/null 2>&1; then
            warning "Found temporary installation files: $temp_dir"
            cleanup_needed=true
        fi
    done
    
    # Check for incomplete launcher scripts
    if [ -f "$HOME/.local/bin/innioasis-updater" ] && [ ! -f "$INSTALL_DIR/firmware_downloader.py" ]; then
        warning "Found launcher script but missing main application files"
        cleanup_needed=true
    fi
    
    if [ "$cleanup_needed" = true ]; then
        log "Partial installation detected. Cleaning up..."

        # Avoid deleting the directory we are currently running from.
        ensure_safe_working_directory "$INSTALL_DIR"
        
        # Remove incomplete installation directory
        if [ -d "$INSTALL_DIR" ]; then
            rm -rf "$INSTALL_DIR"
            success "Removed incomplete installation directory"
        fi
        
        # Remove temporary directories
        for temp_dir in "${temp_dirs[@]}"; do
            if ls $temp_dir >/dev/null 2>&1; then
                rm -rf $temp_dir
                success "Removed temporary directory: $temp_dir"
            fi
        done
        
        # Remove incomplete launcher
        if [ -f "$HOME/.local/bin/innioasis-updater" ] && [ ! -d "$INSTALL_DIR" ]; then
            rm -f "$HOME/.local/bin/innioasis-updater"
            success "Removed incomplete launcher script"
        fi
        
        log "Cleanup completed. Ready for fresh installation."
    else
        log "No partial installation detected."
    fi
    
    return 0
}

# Check if sudo is available
check_sudo() {
    if ! command -v sudo >/dev/null 2>&1; then
        error "sudo is not available. Please install sudo or run as root (not recommended)."
        return 1
    fi
    
    # Request sudo permissions early
    log "Requesting sudo permissions..."
    vlog "Needed for system packages and USB access rules"
    
    if ! sudo -v; then
        error "Failed to obtain sudo permissions. Please ensure you have sudo access and try again."
        return 1
    fi
    
    # Keep sudo session alive in background
    while true; do
        sudo -n true 2>/dev/null && sleep 60 || break
    done &
    
    success "Sudo permissions obtained successfully"
    return 0
}

# Setup virtual environment
setup_virtual_environment() {
    log "Setting up Python virtual environment..."
    
    # Get installation directory
    get_install_dir
    
    # Create virtual environment in installation directory
    VENV_DIR="$INSTALL_DIR/venv"
    
    if [ -d "$VENV_DIR" ]; then
        log "Virtual environment already exists, removing old one..."
        rm -rf "$VENV_DIR"
    fi
    
    # Create new virtual environment
    if python3 -m venv "$VENV_DIR"; then
        success "Virtual environment created at $VENV_DIR"
    else
        warning "Standard venv creation failed, retrying with ensurepip..."
        if python3 -m venv --without-pip "$VENV_DIR" && python3 -m ensurepip --upgrade >/dev/null 2>&1; then
            if ! "$VENV_DIR/bin/python" -m ensurepip --upgrade >/dev/null 2>&1; then
                warning "Could not bootstrap pip inside venv via ensurepip"
            fi
        else
            error "Failed to create virtual environment"
            return 1
        fi
    fi
    
    # Define Python packages for virtual environment (crypto backend is optional)
    PYTHON_PACKAGES="PySide6 requests lxml configparser colorama capstone keystone-engine usb pyusb libusb1 pyserial adbutils pillow numpy"
    
    # Activate virtual environment and install packages
    log "Installing Python packages in virtual environment..."
    "$VENV_DIR/bin/python" -m ensurepip --upgrade >/dev/null 2>&1 || true
    if "$VENV_DIR/bin/python" -m pip install --upgrade pip setuptools wheel; then
        success "pip upgraded in virtual environment"
    else
        warning "Failed to upgrade pip in virtual environment; continuing with existing pip"
    fi

    # Install all required packages
    if install_python_packages "$VENV_DIR/bin/python" $PYTHON_PACKAGES; then
        success "Python packages installed in virtual environment"
    else
        warning "Failed to install one or more Python packages in virtual environment"
        warning "Application may still run if missing packages are optional"
    fi
    
    # Check and fix pycryptodome installation if needed
    if [ "$INSTALL_PYCRYPTO" = "1" ]; then
        check_pycryptodome_status "$VENV_DIR"
        local pycrypto_status=$?
        
        case $pycrypto_status in
            0)
                log "pycryptodome is already working correctly"
                ;;
            1|2|3)
                warning "Attempting optional crypto package setup..."
                if ! install_pycryptodome_fallback "$VENV_DIR"; then
                    warning "Optional crypto setup failed; continuing installation"
                fi
                ;;
        esac
    else
        vlog "Skipping optional pycryptodome setup in virtual environment"
    fi
    
    # Create activation script
    cat > "$INSTALL_DIR/activate_venv.sh" << EOF
#!/bin/bash
# Activate Innioasis Updater virtual environment
source "$VENV_DIR/bin/activate"
echo "Virtual environment activated for Innioasis Updater"
EOF
    chmod +x "$INSTALL_DIR/activate_venv.sh"
    
    success "Virtual environment setup completed"
    return 0
}

# Verify pycryptodome installation (supports both pycryptodome and pycryptodomex)
verify_pycryptodome_installation() {
    local venv_dir="$1"
    local quiet="${2:-0}"

    if [ "$quiet" != "1" ]; then
        log "Verifying pycryptodome/pycryptodomex installation..."
    fi

    local verify_script='import sys
try:
    from Crypto.Cipher import AES
    from Crypto.Util.number import bytes_to_long
    _ = bytes_to_long(b"\x01")
    sys.exit(0)
except ImportError:
    try:
        from Cryptodome.Cipher import AES
        from Cryptodome.Util.number import bytes_to_long
        _ = bytes_to_long(b"\x01")
        sys.exit(0)
    except ImportError:
        sys.exit(1)'

    if [ -n "$venv_dir" ] && [ -d "$venv_dir" ]; then
        if source "$venv_dir/bin/activate" && python -c "$verify_script" >/dev/null 2>&1; then
            if [ "$quiet" != "1" ]; then
                success "Crypto backend verified in virtual environment"
            fi
            return 0
        fi
    else
        if python3 -c "$verify_script" >/dev/null 2>&1; then
            if [ "$quiet" != "1" ]; then
                success "Crypto backend verified in system Python"
            fi
            return 0
        fi
    fi

    if [ "$quiet" != "1" ]; then
        warning "Crypto backend verification failed"
    fi
    return 1
}

# Check if pycryptodome is already properly installed
check_pycryptodome_status() {
    local venv_dir="$1"
    
    vlog "Checking optional crypto backend status..."
    
    # Check if pycryptodome is already working
    if verify_pycryptodome_installation "$venv_dir" 1; then
        vlog "Crypto backend is already available"
        return 0
    fi
    
    # Check if package metadata exists even when imports fail (Python 3.12+/3.14 friendly).
    local check_cmd="python -c \"import importlib.metadata as md; print([d.metadata.get('Name','') for d in md.distributions() if d.metadata.get('Name','').lower() in ['pycryptodome','pycryptodomex','pycrypto']])\" 2>/dev/null || true"
    
    if [ -n "$venv_dir" ] && [ -d "$venv_dir" ]; then
        local installed_packages=$(source "$venv_dir/bin/activate" && eval $check_cmd)
    else
        local installed_packages=$(eval $check_cmd)
    fi
    
    if [ -n "$installed_packages" ] && [ "$installed_packages" != "[]" ]; then
        vlog "Found installed crypto packages: $installed_packages"
        vlog "Package exists but import failed; treating as degraded state"
        return 3
    fi
    
    vlog "Crypto package not currently installed"
    return 2
}

# Install pycryptodome with fallback methods
install_pycryptodome_fallback() {
    local venv_dir="$1"
    local cache_scope="system"
    if [ -n "$venv_dir" ] && [ -d "$venv_dir" ]; then
        cache_scope="venv"
    fi

    # Avoid repeatedly running the same expensive fallback sequence in one installer run.
    if [ "$cache_scope" = "venv" ] && [ "${PYCRYPTODOME_FALLBACK_VENV_STATUS:-}" = "failed" ]; then
        pycrypto_log "Skipping repeated pycryptodome fallback attempts for virtual environment"
        return 1
    elif [ "$cache_scope" = "system" ] && [ "${PYCRYPTODOME_FALLBACK_SYSTEM_STATUS:-}" = "failed" ]; then
        pycrypto_log "Skipping repeated pycryptodome fallback attempts for system python"
        return 1
    fi
    
    pycrypto_log "Attempting fallback pycryptodome installation..."
    pycrypto_log "Architecture: $ARCH_TYPE ($ARCH_BITS-bit)"
    
    # Architecture-specific considerations
    local extra_flags=""
    case "$ARCH_TYPE" in
        armhf|armel|arm64)
            pycrypto_log "ARM architecture detected - using optimized build flags"
            extra_flags="--no-binary=pycryptodome"
            # Ensure we have necessary build tools for ARM
            if ! command -v gcc >/dev/null 2>&1; then
                warning "GCC not found - pycryptodome may fail to compile on ARM"
                log "Consider installing build-essential package"
            fi
            ;;
        amd64|i386)
            pycrypto_log "x86 architecture detected - using standard installation"
            ;;
        *)
            warning "Unknown architecture - attempting standard installation"
            ;;
    esac
    
    # Try different installation methods - prioritize pycryptodome for Crypto imports
    local install_methods=(
        "pip install pycryptodome --upgrade $extra_flags"
        "pip install pycryptodome --no-cache-dir $extra_flags"
        "pip install pycryptodome --force-reinstall $extra_flags"
        "pip install pycryptodomex --upgrade $extra_flags"
        "pip install pycryptodomex --force-reinstall $extra_flags"
    )
    
    for method in "${install_methods[@]}"; do
        pycrypto_log "Trying: $method"
        
        if [ -n "$venv_dir" ] && [ -d "$venv_dir" ]; then
            if source "$venv_dir/bin/activate" && eval $method 2>/dev/null; then
                if verify_pycryptodome_installation "$venv_dir" 1; then
                    success "pycryptodome installed successfully with method: $method"
                    if [ "$cache_scope" = "venv" ]; then
                        PYCRYPTODOME_FALLBACK_VENV_STATUS="ok"
                    else
                        PYCRYPTODOME_FALLBACK_SYSTEM_STATUS="ok"
                    fi
                    return 0
                fi
            fi
        else
            if eval $method 2>/dev/null; then
                if verify_pycryptodome_installation "" 1; then
                    success "pycryptodome installed successfully with method: $method"
                    if [ "$cache_scope" = "venv" ]; then
                        PYCRYPTODOME_FALLBACK_VENV_STATUS="ok"
                    else
                        PYCRYPTODOME_FALLBACK_SYSTEM_STATUS="ok"
                    fi
                    return 0
                fi
            fi
        fi
    done
    
    # Source builds are slow/brittle on many distros; disabled by default.
    # Set ENABLE_PYCRYPTODOME_SOURCE_BUILD=1 to re-enable for debugging.
    if [ "${ENABLE_PYCRYPTODOME_SOURCE_BUILD:-0}" = "1" ] && command -v git >/dev/null 2>&1 && command -v gcc >/dev/null 2>&1; then
        pycrypto_log "Attempting to install pycryptodome from source..."
        local temp_dir
        local original_cwd
        temp_dir=$(mktemp -d)
        original_cwd=$(pwd)
        cd "$temp_dir" || return 1
        
        if git clone https://github.com/Legrandin/pycryptodome.git 2>/dev/null; then
            cd pycryptodome
            
            # Set up build environment for source compilation
            export CFLAGS="-O2"
            export CXXFLAGS="-O2"
            
            # Architecture-specific compiler flags
            case "$ARCH_TYPE" in
                armhf|armel)
                    export CFLAGS="$CFLAGS -march=armv7-a -mfpu=neon"
                    ;;
                arm64)
                    export CFLAGS="$CFLAGS -march=armv8-a"
                    ;;
            esac
            
            if [ -n "$venv_dir" ] && [ -d "$venv_dir" ]; then
                if source "$venv_dir/bin/activate" && python setup.py build_ext --inplace && pip install . 2>/dev/null; then
                    if verify_pycryptodome_installation "$venv_dir" 1; then
                        success "pycryptodome installed from source successfully"
                        if [ "$cache_scope" = "venv" ]; then
                            PYCRYPTODOME_FALLBACK_VENV_STATUS="ok"
                        else
                            PYCRYPTODOME_FALLBACK_SYSTEM_STATUS="ok"
                        fi
                        cd "$original_cwd" || true
                        rm -rf "$temp_dir"
                        return 0
                    fi
                fi
            else
                if python3 setup.py build_ext --inplace && pip3 install . 2>/dev/null; then
                    if verify_pycryptodome_installation "" 1; then
                        success "pycryptodome installed from source successfully"
                        if [ "$cache_scope" = "venv" ]; then
                            PYCRYPTODOME_FALLBACK_VENV_STATUS="ok"
                        else
                            PYCRYPTODOME_FALLBACK_SYSTEM_STATUS="ok"
                        fi
                        cd "$original_cwd" || true
                        rm -rf "$temp_dir"
                        return 0
                    fi
                fi
            fi
        fi
        
        cd "$original_cwd" || true
        rm -rf "$temp_dir"
    else
        pycrypto_log "Skipping pycryptodome source build fallback (disabled by default)"
    fi
    
    # Final attempt with system package manager if available
    pycrypto_log "Attempting to install pycryptodome via system package manager..."
    
    case "$DISTRO_ID" in
        ubuntu|linuxmint|pop|elementary|zorin|debian|raspbian)
            if command -v apt >/dev/null 2>&1; then
                if sudo apt install -y python3-pycryptodome 2>/dev/null || sudo apt install -y python3-pycryptodomex 2>/dev/null; then
                    if verify_pycryptodome_installation "" 1; then
                        success "Installed pycryptodome package via apt"
                        if [ "$cache_scope" = "venv" ]; then
                            PYCRYPTODOME_FALLBACK_VENV_STATUS="ok"
                        else
                            PYCRYPTODOME_FALLBACK_SYSTEM_STATUS="ok"
                        fi
                        return 0
                    fi
                fi
            fi
            ;;
        arch|manjaro|endeavouros|cachyos|garuda|artix)
            if command -v pacman >/dev/null 2>&1; then
                if sudo pacman -S --noconfirm --needed python-pycryptodome 2>/dev/null || sudo pacman -S --noconfirm --needed python-pycryptodomex 2>/dev/null; then
                    if verify_pycryptodome_installation "" 1; then
                        success "Installed pycryptodome package via pacman"
                        if [ "$cache_scope" = "venv" ]; then
                            PYCRYPTODOME_FALLBACK_VENV_STATUS="ok"
                        else
                            PYCRYPTODOME_FALLBACK_SYSTEM_STATUS="ok"
                        fi
                        return 0
                    fi
                fi
            fi
            ;;
        fedora|rhel|centos|almalinux|rocky|bazzite|ublue-os)
            local dnf_cmd
            dnf_cmd=$(resolve_cmd dnf yum)
            if [ -n "$dnf_cmd" ]; then
                if sudo "$dnf_cmd" install -y python3-pycryptodome 2>/dev/null || sudo "$dnf_cmd" install -y python3-pycryptodomex 2>/dev/null; then
                    if verify_pycryptodome_installation "" 1; then
                        success "Installed pycryptodome package via $dnf_cmd"
                        if [ "$cache_scope" = "venv" ]; then
                            PYCRYPTODOME_FALLBACK_VENV_STATUS="ok"
                        else
                            PYCRYPTODOME_FALLBACK_SYSTEM_STATUS="ok"
                        fi
                        return 0
                    fi
                fi
            fi
            ;;
    esac
    
    if [ "$cache_scope" = "venv" ]; then
        PYCRYPTODOME_FALLBACK_VENV_STATUS="failed"
    else
        PYCRYPTODOME_FALLBACK_SYSTEM_STATUS="failed"
    fi
    warning "Optional crypto package could not be validated automatically"
    warning "Installation will continue. Most core features still work."
    return 1
}

# Fix Cryptodome import statements in Innioasis Updater code
fix_cryptodome_imports() {
    vlog "Skipping Cryptodome import fixes; codebase already handles imports"
    return 0
}

# Install Python packages via pip as fallback
install_python_packages_via_pip() {
    log "Installing Python packages via pip..."
    
    if ! ensure_pip_tools python3; then
        warning "pip tooling unavailable for system python, skipping global user package install"
        return 1
    fi
    
    # Install packages via pip
    # Try with --break-system-packages for Ubuntu 25.04+ which has externally-managed-environment
    # Use pycryptodomex to support "Cryptodome" imports
    PYTHON_PACKAGES="PySide6 requests lxml configparser colorama capstone keystone-engine usb pyusb libusb1 pyserial adbutils pillow numpy"
    
    if install_python_packages python3 $PYTHON_PACKAGES; then
        success "Python packages installed via pip successfully"
    else
        warning "Failed to install some Python packages via pip"
        warning "You may need to install them manually later with: python3 -m pip install --user --break-system-packages $PYTHON_PACKAGES"
    fi
    
    if [ "$INSTALL_PYCRYPTO" = "1" ] && ! verify_pycryptodome_installation "" 1; then
        warning "Optional crypto backend setup requested, attempting install..."
        install_pycryptodome_fallback
    fi
}

# Install dependencies based on distribution
install_dependencies() {
    log "Installing required dependencies for $DISTRO_NAME..."
    
    case "$DISTRO_ID" in
        ubuntu|linuxmint|pop|elementary|zorin)
            install_ubuntu_deps
            ;;
        debian)
            install_debian_deps
            ;;
        raspbian)
            install_raspbian_deps
            ;;
        arch|manjaro|endeavouros|cachyos|garuda|artix)
            install_arch_deps
            ;;
        fedora|rhel|centos|almalinux|rocky|bazzite|ublue-os)
            install_fedora_deps
            ;;
        opensuse*|sles)
            install_opensuse_deps
            ;;
        steamos|holoiso)
            install_steamos_deps
            ;;
        chromeos|fydeos)
            install_chromeos_deps
            ;;
        *)
            install_generic_deps
            ;;
    esac
    
    # Always try to install Python packages via pip as a fallback
    install_python_packages_via_pip
    
    # Try to install Android tools as fallback if not available
    if ! command -v adb >/dev/null 2>&1 || ! command -v fastboot >/dev/null 2>&1; then
        install_android_tools_fallback
    fi
}

# Ubuntu/Debian-based distributions
install_ubuntu_deps() {
    log "Installing dependencies for Ubuntu/Debian-based distribution..."
    
    # Update package list
    log "Updating package list..."
    if ! sudo apt-get update; then
        error "Failed to update package list. Please check your internet connection and try again."
        return 1
    fi
    
    # Install essential packages
    log "Installing essential packages..."
    
    # Base packages for all architectures
    # MTKClient requirements: libfuse2, libfuse3, fuse3, libusb-1.0-0-dev, openssl
    BASE_PACKAGES="python3 python3-pip python3-venv python3-dev python3-setuptools pkg-config git curl wget unzip udev usbutils android-tools-adb android-tools-fastboot cmake build-essential gcc g++ make libffi-dev libssl-dev openssl zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libncurses5-dev libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev libfuse2 libfuse3 fuse3 libusb-1.0-0-dev libusb-1.0-0 libxcb-cursor0"
    
    # Architecture-specific packages
    case "$ARCH_TYPE" in
        amd64|i386)
            ARCH_PACKAGES="libusb-1.0-0-dev libusb-1.0-0 build-essential"
            ;;
        arm64|armhf|armel)
            ARCH_PACKAGES="libusb-1.0-0-dev libusb-1.0-0 build-essential"
            # For ARM systems, also install cross-compilation tools if needed
            if [ "$ARCH_BITS" = "32" ]; then
                ARCH_PACKAGES="$ARCH_PACKAGES gcc-arm-linux-gnueabihf"
            fi
            ;;
        *)
            ARCH_PACKAGES="libusb-1.0-0-dev libusb-1.0-0 build-essential"
            ;;
    esac
    
    if ! sudo apt-get install -y $BASE_PACKAGES $ARCH_PACKAGES; then
        error "Failed to install essential packages. Some packages may not be available."
        warning "Continuing with available packages..."
    fi
    
    # Install Python packages (try PySide6 first, fallback to PySide2)
    log "Installing Python packages..."
    if sudo apt-get install -y \
        python3-pyside6.qtcore \
        python3-pyside6.qtgui \
        python3-pyside6.qtwidgets \
        python3-requests \
        python3-configparser \
        python3-lxml 2>/dev/null; then
        success "PySide6 packages installed successfully"
    else
        warning "PySide6 not available, trying PySide2..."
        if sudo apt-get install -y \
            python3-pyside2.qtcore \
            python3-pyside2.qtgui \
            python3-pyside2.qtwidgets \
            python3-requests \
            python3-configparser \
            python3-lxml; then
            success "PySide2 packages installed successfully"
        else
            warning "System PySide packages not available, will install via pip"
        fi
    fi
    
    # Install Python packages via pip if system packages failed
    install_python_packages_via_pip
    
    success "Ubuntu/Debian dependencies installation completed"
}

# Debian
install_debian_deps() {
    log "Installing dependencies for Debian..."
    
    # Update package list
    sudo apt-get update
    
    # Base packages for all architectures
    BASE_PACKAGES="python3 python3-pip python3-venv python3-dev python3-setuptools pkg-config git curl wget unzip udev usbutils libxcb-cursor0"
    
    # Architecture-specific packages
    case "$ARCH_TYPE" in
        amd64|i386)
            ARCH_PACKAGES="libusb-1.0-0-dev libusb-1.0-0 build-essential"
            ;;
        arm64|armhf|armel)
            ARCH_PACKAGES="libusb-1.0-0-dev libusb-1.0-0 build-essential"
            ;;
        *)
            ARCH_PACKAGES="libusb-1.0-0-dev libusb-1.0-0 build-essential"
            ;;
    esac
    
    sudo apt-get install -y $BASE_PACKAGES $ARCH_PACKAGES
    
    # Install Python packages (try PySide6 first, fallback to PySide2)
    if sudo apt-get install -y \
        python3-pyside6.qtcore \
        python3-pyside6.qtgui \
        python3-pyside6.qtwidgets \
        python3-requests \
        python3-configparser \
        python3-lxml 2>/dev/null; then
        success "PySide6 packages installed successfully"
    else
        warning "PySide6 not available, trying PySide2..."
        sudo apt-get install -y \
            python3-pyside2.qtcore \
            python3-pyside2.qtgui \
            python3-pyside2.qtwidgets \
            python3-requests \
            python3-configparser \
            python3-lxml
    fi
    
    success "Debian dependencies installed successfully"
}

# Raspberry Pi OS (Raspbian)
install_raspbian_deps() {
    log "Installing dependencies for Raspberry Pi OS..."
    
    # Update package list
    sudo apt-get update
    
    # Base packages for Raspberry Pi
    BASE_PACKAGES="python3 python3-pip python3-venv python3-dev python3-setuptools pkg-config git curl wget unzip udev usbutils"
    
    # Architecture-specific packages for ARM
    case "$ARCH_TYPE" in
        armhf)
            ARCH_PACKAGES="libusb-1.0-0-dev libusb-1.0-0 build-essential"
            ;;
        arm64)
            ARCH_PACKAGES="libusb-1.0-0-dev libusb-1.0-0 build-essential"
            ;;
        *)
            ARCH_PACKAGES="libusb-1.0-0-dev libusb-1.0-0 build-essential"
            ;;
    esac
    
    sudo apt-get install -y $BASE_PACKAGES $ARCH_PACKAGES
    
    # Install Python packages (Raspbian may not have PySide6, so try PySide2 first)
    if sudo apt-get install -y \
        python3-pyside2.qtcore \
        python3-pyside2.qtgui \
        python3-pyside2.qtwidgets \
        python3-requests \
        python3-configparser \
        python3-lxml 2>/dev/null; then
        success "PySide2 packages installed successfully"
    else
        warning "PySide2 not available, will install via pip"
    fi
    
    success "Raspberry Pi OS dependencies installed successfully"
}

# Arch-based distributions
install_arch_deps() {
    log "Installing dependencies for Arch-based distribution..."

    if is_immutable_system; then
        warning "Immutable/ostree system detected; skipping pacman system package install"
        install_python_packages_via_pip
        return 0
    fi

    # Update package database
    if ! run_cmd "Refreshing package database..." "sudo pacman -Sy"; then
        warning "Could not refresh package database"
    fi
    
    # Base packages for all architectures
    # MTKClient requirements: fuse2, fuse3, libusb
    BASE_PACKAGES="python python-pip python-virtualenv python-setuptools pkgconf base-devel git curl wget unzip udev usbutils cmake gcc gcc-libs make libffi openssl bzip2 readline sqlite tk libxml2 xz ncurses android-tools fuse2 fuse3 libusb"
    
    # Architecture-specific packages
    case "$ARCH_TYPE" in
        amd64|i386)
            ARCH_PACKAGES="libusb"
            ;;
        arm64|armhf|armel)
            ARCH_PACKAGES="libusb"
            ;;
        *)
            ARCH_PACKAGES="libusb"
            ;;
    esac
    
    if ! run_cmd "Installing system packages..." "sudo pacman -S --noconfirm --needed $BASE_PACKAGES $ARCH_PACKAGES"; then
        warning "Some Arch dependencies failed to install"
    fi
    
    # Install Python packages (try PySide6 first, fallback to PySide2)
    if run_cmd "Installing optional GUI packages..." "sudo pacman -S --noconfirm --needed python-pyside6 python-requests python-lxml"; then
        success "PySide6 packages installed successfully"
    else
        warning "PySide6 not available, trying PySide2..."
        run_cmd "Installing PySide2 fallback packages..." "sudo pacman -S --noconfirm --needed python-pyside2 python-requests python-lxml" || warning "PySide2 fallback package installation failed"
    fi
    
    install_python_packages_via_pip
    success "Arch dependencies installed successfully"
}

# Fedora/RHEL-based distributions
install_fedora_deps() {
    log "Installing dependencies for Fedora/RHEL-based distribution..."

    if is_immutable_system; then
        warning "Immutable/ostree system detected; skipping system package install"
        install_python_packages_via_pip
        return 0
    fi

    local dnf_cmd
    dnf_cmd=$(resolve_cmd dnf yum)
    if [ -z "$dnf_cmd" ]; then
        warning "dnf/yum not available; using generic dependency flow"
        install_generic_deps
        return 0
    fi

    # Update package database
    sudo "$dnf_cmd" update -y
    
    # Base packages for all architectures
    # MTKClient requirements: fuse, fuse-devel, libusb1-devel
    BASE_PACKAGES="python3 python3-pip python3-venv python3-devel python3-setuptools pkgconfig gcc gcc-c++ make git curl wget unzip systemd-udev usbutils cmake libffi-devel openssl-devel zlib-devel bzip2-devel readline-devel sqlite-devel tk-devel libxml2-devel xz-devel ncurses-devel android-tools fuse fuse-devel libusb1-devel libusb1"
    
    # Architecture-specific packages
    case "$ARCH_TYPE" in
        amd64|i386)
            ARCH_PACKAGES="libusb1-devel libusb1"
            ;;
        arm64|armhf|armel)
            ARCH_PACKAGES="libusb1-devel libusb1"
            ;;
        *)
            ARCH_PACKAGES="libusb1-devel libusb1"
            ;;
    esac
    
    sudo "$dnf_cmd" install -y $BASE_PACKAGES $ARCH_PACKAGES || warning "Some Fedora/RHEL dependencies failed to install"
    
    # Install Python packages (try PySide6 first, fallback to PySide2)
    if sudo "$dnf_cmd" install -y \
        python3-PySide6 \
        python3-requests \
        python3-lxml 2>/dev/null; then
        success "PySide6 packages installed successfully"
    else
        warning "PySide6 not available, trying PySide2..."
        sudo "$dnf_cmd" install -y \
            python3-PySide2 \
            python3-requests \
            python3-lxml || warning "PySide2 fallback package installation failed"
    fi
    
    install_python_packages_via_pip
    success "Fedora/RHEL dependencies installed successfully"
}

# openSUSE
install_opensuse_deps() {
    log "Installing dependencies for openSUSE..."
    
    # Update package database
    sudo zypper refresh
    
    # Base packages for all architectures
    # MTKClient requirements: fuse, fuse-devel, libusb-1_0-devel
    BASE_PACKAGES="python3 python3-pip python3-venv python3-devel python3-setuptools pkg-config gcc gcc-c++ make git curl wget unzip udev usbutils cmake libffi-devel openssl-devel zlib-devel bzip2-devel readline-devel sqlite3-devel tk-devel libxml2-devel xz-devel ncurses-devel android-tools fuse fuse-devel libusb-1_0-devel libusb-1_0-0"
    
    # Architecture-specific packages
    case "$ARCH_TYPE" in
        amd64|i386)
            ARCH_PACKAGES="libusb-1_0-devel libusb-1_0-0"
            ;;
        arm64|armhf|armel)
            ARCH_PACKAGES="libusb-1_0-devel libusb-1_0-0"
            ;;
        *)
            ARCH_PACKAGES="libusb-1_0-devel libusb-1_0-0"
            ;;
    esac
    
    sudo zypper install -y $BASE_PACKAGES $ARCH_PACKAGES
    
    # Install Python packages (try PySide6 first, fallback to PySide2)
    if sudo zypper install -y \
        python3-PySide6 \
        python3-requests \
        python3-lxml 2>/dev/null; then
        success "PySide6 packages installed successfully"
    else
        warning "PySide6 not available, trying PySide2..."
        sudo zypper install -y \
            python3-PySide2 \
            python3-requests \
            python3-lxml
    fi
    
    success "openSUSE dependencies installed successfully"
}

# SteamOS/HoloISO
install_steamos_deps() {
    log "Installing dependencies for SteamOS/HoloISO..."
    
    # SteamOS uses pacman but may need special handling
    if command -v pacman >/dev/null 2>&1; then
        # Update package database
        sudo pacman -Sy
        
        # Install essential packages
        sudo pacman -S --noconfirm \
            python \
            python-pip \
            python-virtualenv \
            python-setuptools \
            libusb \
            pkgconf \
            base-devel \
            git \
            curl \
            wget \
            unzip \
            udev \
            usbutils
        
        # Install Python packages via pip (SteamOS may not have PySide6 in repos)
        pip3 install --user PySide6 requests lxml
    else
        warning "SteamOS detected but pacman not available. Using generic installation."
        install_generic_deps
    fi
    
    success "SteamOS dependencies installed successfully"
}

# ChromeOS/FydeOS Linux
install_chromeos_deps() {
    log "Installing dependencies for ChromeOS/FydeOS Linux..."
    
    # ChromeOS Linux uses apt but may have limited packages
    if command -v apt >/dev/null 2>&1; then
        # Update package list
        sudo apt update
        
        # Install essential packages (ChromeOS may have limited packages)
        sudo apt install -y \
            python3 \
            python3-pip \
            python3-venv \
            python3-dev \
            python3-setuptools \
            libusb-1.0-0-dev \
            libusb-1.0-0 \
            pkg-config \
            build-essential \
            git \
            curl \
            wget \
            unzip \
            udev \
            usbutils \
            cmake \
            gcc \
            g++ \
            make \
            libffi-dev \
            libssl-dev \
            zlib1g-dev \
            libbz2-dev \
            libreadline-dev \
            libsqlite3-dev \
            libncurses5-dev \
            libncursesw5-dev \
            xz-utils \
            tk-dev \
            libxml2-dev \
            libxmlsec1-dev \
            liblzma-dev
        
        # Try to install android-tools, but don't fail if not available
        sudo apt install -y android-tools-adb android-tools-fastboot 2>/dev/null || warning "Android tools not available in ChromeOS repos"
        
        # Install Python packages via pip (ChromeOS may not have PySide6 in repos)
        python3 -m pip install --user --break-system-packages PySide6 requests lxml configparser colorama capstone usb pyusb libusb1 pyserial adbutils
        
        if [ "$INSTALL_PYCRYPTO" = "1" ] && ! verify_pycryptodome_installation "" 1; then
            warning "Optional crypto backend setup requested, attempting install..."
            install_pycryptodome_fallback
        fi
    else
        warning "ChromeOS/FydeOS detected but apt not available. Using generic installation."
        install_generic_deps
    fi
    
    success "ChromeOS/FydeOS dependencies installed successfully"
}

# Generic installation for unknown distributions
install_generic_deps() {
    log "Installing dependencies using generic method..."
    
    # Try to install Python and pip
    if command -v python3 >/dev/null 2>&1; then
        log "Python3 is already installed"
    else
        error "Python3 is not installed. Please install Python3 manually."
        exit 1
    fi
    
    # Try to install build tools if available
    log "Attempting to install build tools..."
    
    # Try different package managers
    if command -v apt >/dev/null 2>&1; then
        sudo apt update 2>/dev/null || true
        sudo apt install -y build-essential cmake pkg-config libusb-1.0-0-dev 2>/dev/null || warning "Could not install build tools via apt"
    elif command -v pacman >/dev/null 2>&1; then
        if is_immutable_system; then
            warning "Immutable/ostree system detected; skipping pacman build tool install"
        else
            sudo pacman -Sy 2>/dev/null || true
            sudo pacman -S --noconfirm base-devel cmake pkgconf libusb 2>/dev/null || warning "Could not install build tools via pacman"
        fi
    elif command -v dnf >/dev/null 2>&1 || command -v yum >/dev/null 2>&1; then
        local dnf_cmd
        dnf_cmd=$(resolve_cmd dnf yum)
        sudo "$dnf_cmd" update -y 2>/dev/null || true
        sudo "$dnf_cmd" install -y gcc gcc-c++ make cmake pkgconfig libusb1-devel 2>/dev/null || warning "Could not install build tools via $dnf_cmd"
    elif command -v zypper >/dev/null 2>&1; then
        sudo zypper refresh 2>/dev/null || true
        sudo zypper install -y gcc gcc-c++ make cmake pkg-config libusb-1_0-devel 2>/dev/null || warning "Could not install build tools via zypper"
    fi
    
    # Install Python packages via pip
    # Try with --break-system-packages for Ubuntu 25.04+ which has externally-managed-environment
    # Crypto backend is optional and lazy-loaded at runtime.
    PYTHON_PACKAGES="PySide6 requests lxml configparser colorama capstone usb pyusb libusb1 pyserial adbutils pillow numpy"
    
    log "Installing Python packages..."
    if ! install_python_packages python3 $PYTHON_PACKAGES; then
        warning "Some Python packages failed to install. Trying individual packages..."
        for package in $PYTHON_PACKAGES; do
            if ! install_python_packages python3 "$package"; then
                warning "Failed to install $package"
            fi
        done
    fi
    
    # Try to install keystone-engine separately (it often needs build tools)
    log "Attempting to install keystone-engine..."
    if ! install_python_packages python3 keystone-engine; then
        warning "keystone-engine failed to install (requires cmake and build tools)"
    fi
    
    if [ "$INSTALL_PYCRYPTO" = "1" ]; then
        log "Verifying optional crypto backend installation..."
        if ! verify_pycryptodome_installation "" 1; then
            warning "Optional crypto backend setup requested, attempting install..."
            install_pycryptodome_fallback
        fi
    fi
    
    # Try to install libusb
    if command -v pkg-config >/dev/null 2>&1 && pkg-config --exists libusb-1.0; then
        log "libusb is already installed"
    else
        warning "libusb not found. Please install libusb-1.0 development package manually."
        warning "On most distributions: sudo apt install libusb-1.0-0-dev (Debian/Ubuntu)"
        warning "Or: sudo pacman -S libusb (Arch) or sudo dnf install libusb1-devel (Fedora)"
    fi
    
    success "Generic dependencies installation completed"
}

# Install Android Platform Tools as fallback
install_android_tools_fallback() {
    log "Installing Android Platform Tools as fallback..."
    
    # Check if adb and fastboot are already available
    if command -v adb >/dev/null 2>&1 && command -v fastboot >/dev/null 2>&1; then
        log "Android tools already available"
        return 0
    fi
    
    # Create temporary directory
    TEMP_DIR=$(mktemp -d)
    local original_cwd
    original_cwd=$(pwd)
    cd "$TEMP_DIR" || return 1
    
    # Download Android Platform Tools
    log "Downloading Android Platform Tools..."
    if command -v wget >/dev/null 2>&1; then
        if wget -O platform-tools.zip https://dl.google.com/android/repository/platform-tools-latest-linux.zip 2>/dev/null; then
            success "Downloaded Android Platform Tools"
        else
            warning "Failed to download Android Platform Tools with wget"
            cd "$original_cwd" || true
            rm -rf "$TEMP_DIR"
            return 1
        fi
    elif command -v curl >/dev/null 2>&1; then
        if curl -L -o platform-tools.zip https://dl.google.com/android/repository/platform-tools-latest-linux.zip 2>/dev/null; then
            success "Downloaded Android Platform Tools"
        else
            warning "Failed to download Android Platform Tools with curl"
            cd "$original_cwd" || true
            rm -rf "$TEMP_DIR"
            return 1
        fi
    else
        warning "Neither wget nor curl available for downloading Android Platform Tools"
        cd "$original_cwd" || true
        rm -rf "$TEMP_DIR"
        return 1
    fi
    
    # Extract the archive
    if command -v unzip >/dev/null 2>&1; then
        if unzip -q platform-tools.zip 2>/dev/null; then
            success "Extracted Android Platform Tools"
        else
            warning "Failed to extract Android Platform Tools"
            cd "$original_cwd" || true
            rm -rf "$TEMP_DIR"
            return 1
        fi
    else
        warning "unzip not available for extracting Android Platform Tools"
        cd "$original_cwd" || true
        rm -rf "$TEMP_DIR"
        return 1
    fi
    
    # Install to user directory
    USER_BIN_DIR="$HOME/.local/bin"
    mkdir -p "$USER_BIN_DIR"
    
    # Copy tools
    if cp platform-tools/adb "$USER_BIN_DIR/" && cp platform-tools/fastboot "$USER_BIN_DIR/"; then
        chmod +x "$USER_BIN_DIR/adb" "$USER_BIN_DIR/fastboot"
        success "Android Platform Tools installed to $USER_BIN_DIR"
        log "Note: You may need to add $USER_BIN_DIR to your PATH"
    else
        warning "Failed to install Android Platform Tools"
        cd "$original_cwd" || true
        rm -rf "$TEMP_DIR"
        return 1
    fi
    
    # Clean up
    cd "$original_cwd" || true
    rm -rf "$TEMP_DIR"
    return 0
}

# Setup MTKClient specific requirements
setup_mtkclient_requirements() {
    log "Setting up MTKClient specific requirements..."
    
    # Add user to required groups
    log "Adding user to required groups for MTKClient..."
    
    # Ensure commonly-used USB/serial groups exist and add current user.
    # Arch/CachyOS often use uucp/lock and may not ship plugdev by default.
    if ! getent group plugdev >/dev/null 2>&1; then
        sudo groupadd -f plugdev >/dev/null 2>&1 || true
    fi
    local mtk_groups=("plugdev" "dialout" "uucp" "lock")
    for grp in "${mtk_groups[@]}"; do
        if getent group "$grp" >/dev/null 2>&1; then
            if sudo usermod -a -G "$grp" "$USER"; then
                log "Added user $USER to $grp group"
            else
                warning "Failed to add user to $grp group"
            fi
        fi
    done
    
    # Check for vendor interface 0xFF (like LG devices)
    log "Checking for vendor interface 0xFF devices..."
    if [ -f "/etc/modprobe.d/blacklist.conf" ]; then
        if ! grep -q "blacklist qcaux" "/etc/modprobe.d/blacklist.conf" 2>/dev/null; then
            if echo "blacklist qcaux" | sudo tee -a "/etc/modprobe.d/blacklist.conf" >/dev/null; then
                log "Added qcaux blacklist for LG devices"
            else
                warning "Failed to add qcaux blacklist"
            fi
        else
            log "qcaux blacklist already exists"
        fi
    else
        warning "blacklist.conf not found - vendor interface 0xFF devices may have issues"
    fi
    
    # Verify OpenSSL installation
    log "Verifying OpenSSL installation..."
    if command -v openssl >/dev/null 2>&1; then
        local openssl_version=$(openssl version 2>/dev/null)
        success "OpenSSL found: $openssl_version"
        
        # Check if OpenSSL version is compatible (1.1.1 or higher)
        local openssl_numeric
        openssl_numeric=$(echo "$openssl_version" | awk '{print $2}')
        local openssl_major=0
        local openssl_minor=0
        local openssl_patch=0

        IFS='.' read -r openssl_major openssl_minor openssl_patch _ <<< "$openssl_numeric"
        openssl_major=${openssl_major//[^0-9]/}
        openssl_minor=${openssl_minor//[^0-9]/}
        openssl_patch=${openssl_patch//[^0-9]/}

        [ -z "$openssl_major" ] && openssl_major=0
        [ -z "$openssl_minor" ] && openssl_minor=0
        [ -z "$openssl_patch" ] && openssl_patch=0

        if [ "$openssl_major" -gt 1 ] || { [ "$openssl_major" -eq 1 ] && [ "$openssl_minor" -gt 1 ]; } || { [ "$openssl_major" -eq 1 ] && [ "$openssl_minor" -eq 1 ] && [ "$openssl_patch" -ge 1 ]; }; then
            success "OpenSSL version is compatible for MTKClient"
        else
            warning "OpenSSL version may be too old for MTKClient (need 1.1.1+)"
            warning "Current version: $openssl_version"
        fi
    else
        error "OpenSSL not found - MTKClient requires OpenSSL for cryptographic operations"
        return 1
    fi
    
    # Verify libfuse installation
    log "Verifying libfuse installation..."
    local fuse_available=false
    
    if pkg-config --exists fuse3 2>/dev/null; then
        local fuse_version=$(pkg-config --modversion fuse3 2>/dev/null)
        success "libfuse3 found: version $fuse_version"
        fuse_available=true
    elif pkg-config --exists fuse 2>/dev/null; then
        local fuse_version=$(pkg-config --modversion fuse 2>/dev/null)
        success "libfuse found: version $fuse_version"
        fuse_available=true
    fi
    
    if [ "$fuse_available" = false ]; then
        warning "libfuse not found - filesystem mounting may not work"
        warning "MTKClient uses fuse for mounting flash partitions as filesystems"
    fi
    
    # Verify libusb installation
    log "Verifying libusb installation..."
    if pkg-config --exists libusb-1.0 2>/dev/null; then
        local libusb_version=$(pkg-config --modversion libusb-1.0 2>/dev/null)
        success "libusb-1.0 found: version $libusb_version"
    else
        error "libusb-1.0 not found - USB communication will not work"
        error "MTKClient requires libusb-1.0 for USB device communication"
        return 1
    fi
    
    # Check for required Python packages for MTKClient
    log "Checking MTKClient Python dependencies..."
    local required_packages=("Crypto" "Cryptodome" "pyusb" "usb" "serial" "lxml")
    
    for package in "${required_packages[@]}"; do
        if python3 -c "import ${package}" 2>/dev/null; then
            success "Python package $package is available"
        else
            warning "Python package $package is missing - will be installed later"
        fi
    done
    
    success "MTKClient requirements setup completed"
    log "Note: You may need to reboot or log out/in for group changes to take effect"
    log "Note: For full MTKClient functionality, ensure your device is in BROM mode when connecting"
    return 0
}

# Resolve the shared SP Flash Tool system-prep script (identical to firmware_downloader.py).
# Prefer the copy next to this installer; after install, prefer INSTALL_DIR.
find_spflash_system_prep_script() {
    local candidates=()
    local here
    here="$(cd "$(dirname "${BASH_SOURCE[0]}")" 2>/dev/null && pwd)" || here=""
    [ -n "$here" ] && candidates+=("$here/linux_spflash_system_prep.sh")
    [ -n "${INSTALL_DIR:-}" ] && candidates+=("$INSTALL_DIR/linux_spflash_system_prep.sh")
    candidates+=("$HOME/.local/share/innioasis-updater/linux_spflash_system_prep.sh")
    local c
    for c in "${candidates[@]}"; do
        if [ -f "$c" ]; then
            echo "$c"
            return 0
        fi
    done
    return 1
}

# SP Flash Tool + MediaTek system prep — soft-fail; never aborts the installer.
# Uses the same linux_spflash_system_prep.sh as firmware_downloader.py.
setup_spflash_system_prep() {
    log "Preparing SP Flash Tool / MediaTek USB+serial access (best-effort)..."

    local prep_script=""
    if prep_script="$(find_spflash_system_prep_script)"; then
        log "Using shared prep script: $prep_script"
        chmod +x "$prep_script" 2>/dev/null || true
        if sudo bash "$prep_script" "$USER"; then
            success "SP Flash Tool system prep finished"
            return 0
        fi
        warning "SP Flash Tool system prep reported issues — continuing install"
        return 0
    fi

    warning "linux_spflash_system_prep.sh not found next to installer"
    warning "Skipping full SP Flash Tool prep for now; the app will re-run it on first launch"
    return 0
}

# Create udev rules for USB access (MTKClient broad rules + shared SPFT prep).
# Soft-fail: missing pieces are skipped; install continues.
setup_udev_rules() {
    log "Setting up udev rules for USB device access..."

    if ! sudo mkdir -p /etc/udev/rules.d; then
        warning "Failed to create udev rules directory — skipping USB rules (install continues)"
        return 0
    fi

    # Broad MediaTek/vendor USB rules for MTKClient (best-effort; soft-fail)
    if ! sudo tee /etc/udev/rules.d/99-mediatek.rules > /dev/null << 'EOF'
# MediaTek USB devices for MTKClient (installer; soft-fail safe)
SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev", TAG+="uaccess", ENV{ID_MM_DEVICE_IGNORE}="1"
SUBSYSTEM=="usb", ATTR{idVendor}=="0bb4", MODE="0666", GROUP="plugdev", TAG+="uaccess"
SUBSYSTEM=="usb", ATTR{idVendor}=="18d1", MODE="0666", GROUP="plugdev", TAG+="uaccess"
SUBSYSTEM=="usb", ATTR{idVendor}=="22d9", MODE="0666", GROUP="plugdev", TAG+="uaccess"
EOF
    then
        warning "Failed to write 99-mediatek.rules — continuing"
    fi

    # Canonical SP Flash Tool prep (identical to firmware_downloader.py)
    setup_spflash_system_prep

    # Best-effort udev reload
    if command -v udevadm >/dev/null 2>&1; then
        sudo udevadm control --reload-rules >/dev/null 2>&1 || true
        sudo udevadm trigger >/dev/null 2>&1 || true
    fi

    success "USB access setup finished (any failures were skipped)"
    return 0
}

# Determine appropriate installation directory
get_install_dir() {
    # Default to user directory for better compatibility and no sudo requirements
    case "$DISTRO_ID" in
        ubuntu|linuxmint|pop|elementary|zorin|debian)
            INSTALL_DIR="/home/$USER/.local/share/innioasis-updater"
            ;;
        arch|manjaro|endeavouros|cachyos|garuda|artix)
            INSTALL_DIR="/home/$USER/.local/share/innioasis-updater"
            ;;
        fedora|rhel|centos|almalinux|rocky|bazzite|ublue-os)
            INSTALL_DIR="/home/$USER/.local/share/innioasis-updater"
            ;;
        opensuse*|sles)
            INSTALL_DIR="/home/$USER/.local/share/innioasis-updater"
            ;;
        steamos|holoiso)
            INSTALL_DIR="/home/$USER/.local/share/innioasis-updater"
            ;;
        chromeos|fydeos)
            INSTALL_DIR="/home/$USER/.local/share/innioasis-updater"
            ;;
        *)
            INSTALL_DIR="/home/$USER/.local/share/innioasis-updater"
            ;;
    esac
    
    log "Installation directory: $INSTALL_DIR"
}

# Global variable to store download directory
DOWNLOAD_DIR=""

# Download Innioasis Updater from GitHub
download_innioasis() {
    step "Fetching app files from GitHub (usually under 1 minute)"
    
    # Create temporary directory for download
    TEMP_DIR=$(mktemp -d)
    if [ ! -d "$TEMP_DIR" ]; then
        error "Failed to create temporary directory"
        return 1
    fi
    
    # Try to clone the repository
    local clone_start
    clone_start=$(date +%s)
    log "Downloading repository..."
    if git clone https://github.com/y1-community/Innioasis-Updater.git "$TEMP_DIR/innioasis-updater" 2>/dev/null; then
        success "Repository download complete ($(elapsed_seconds "$clone_start")s)"
        DOWNLOAD_DIR="$TEMP_DIR/innioasis-updater"
    else
        warning "Direct clone failed; switching to ZIP download."
        
        # Download as ZIP if git is not available
        ZIP_FILE="$TEMP_DIR/innioasis-updater.zip"
        local zip_start
        zip_start=$(date +%s)
        if command -v wget >/dev/null 2>&1; then
            if wget -O "$ZIP_FILE" https://github.com/y1-community/Innioasis-Updater/archive/refs/heads/main.zip 2>/dev/null; then
                success "ZIP download complete ($(elapsed_seconds "$zip_start")s)"
            else
                error "Failed to download ZIP archive with wget"
                rm -rf "$TEMP_DIR"
                return 1
            fi
        elif command -v curl >/dev/null 2>&1; then
            if curl -L -o "$ZIP_FILE" https://github.com/y1-community/Innioasis-Updater/archive/refs/heads/main.zip 2>/dev/null; then
                success "ZIP download complete ($(elapsed_seconds "$zip_start")s)"
            else
                error "Failed to download ZIP archive with curl"
                rm -rf "$TEMP_DIR"
                return 1
            fi
        else
            error "Neither git, wget, nor curl is available for downloading"
            rm -rf "$TEMP_DIR"
            return 1
        fi
        
        # Extract ZIP file
        local unzip_start
        unzip_start=$(date +%s)
        log "Extracting app files..."
        if command -v unzip >/dev/null 2>&1; then
            if unzip -q "$ZIP_FILE" -d "$TEMP_DIR" 2>/dev/null; then
                success "Extraction complete ($(elapsed_seconds "$unzip_start")s)"
                DOWNLOAD_DIR="$TEMP_DIR/Innioasis-Updater-main"
            else
                error "Failed to extract ZIP archive"
                rm -rf "$TEMP_DIR"
                return 1
            fi
        else
            error "unzip is not available for extracting the archive"
            rm -rf "$TEMP_DIR"
            return 1
        fi
    fi
    
    # Verify that the main Python file exists
    if [ ! -f "$DOWNLOAD_DIR/firmware_downloader.py" ]; then
        error "firmware_downloader.py not found in downloaded files"
        rm -rf "$TEMP_DIR"
        return 1
    fi
    
    success "App files are ready for installation"
    return 0
}

# Install Innioasis Updater
install_innioasis() {
    log "Installing Innioasis Updater to $INSTALL_DIR..."
    
    # Download the application first
    if ! download_innioasis; then
        error "Failed to download Innioasis Updater"
        return 1
    fi
    
    if [ -z "$DOWNLOAD_DIR" ]; then
        error "Download directory not set"
        return 1
    fi
    
    # Create installation directory (user directory - no sudo needed)
    if ! mkdir -p "$INSTALL_DIR"; then
        error "Failed to create installation directory: $INSTALL_DIR"
        rm -rf "$(dirname "$DOWNLOAD_DIR")"
        return 1
    fi
    
    # Copy files to installation directory
    if ! cp -r "$DOWNLOAD_DIR"/* "$INSTALL_DIR/"; then
        error "Failed to copy files to installation directory"
        rm -rf "$(dirname "$DOWNLOAD_DIR")"
        return 1
    fi
    
    # Set proper permissions
    if ! chmod -R 755 "$INSTALL_DIR"; then
        error "Failed to set permissions of installation directory"
        return 1
    fi
    
    # Clean up temporary directory
    rm -rf "$(dirname "$DOWNLOAD_DIR")"
    
    # Make scripts executable
    chmod +x "$INSTALL_DIR"/*.py 2>/dev/null || true
    chmod +x "$INSTALL_DIR"/*.sh 2>/dev/null || true
    
    success "Innioasis Updater installed to $INSTALL_DIR"
    return 0
}

# Create desktop entry
create_desktop_entry() {
    log "Creating desktop entry..."
    
    # Create desktop entry directory
    if ! mkdir -p "$HOME/.local/share/applications"; then
        error "Failed to create applications directory"
        return 1
    fi
    
    # Create desktop entry (user installation)
    LAUNCHER_CMD="$HOME/.local/bin/innioasis-updater"
    ICON_PATH="$INSTALL_DIR/mtkclient/gui/images/icon.png"
    
    if ! cat > "$HOME/.local/share/applications/innioasis-updater.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Innioasis Updater
Comment=Firmware downloader and installer for MediaTek devices
Exec=$LAUNCHER_CMD
Icon=$ICON_PATH
Terminal=false
Categories=System;Settings;
StartupNotify=true
EOF
    then
        error "Failed to create desktop entry file"
        return 1
    fi
    
    # Make desktop entry executable
    chmod +x "$HOME/.local/share/applications/innioasis-updater.desktop"
    
    # Update desktop database
    if command -v update-desktop-database >/dev/null 2>&1; then
        update-desktop-database "$HOME/.local/share/applications"
    fi
    
    success "Desktop entry created successfully"
    return 0
}

# Create launcher script
create_launcher() {
    log "Creating launcher script..."
    
    # User installation - create user launcher
    USER_BIN_DIR="$HOME/.local/bin"
    mkdir -p "$USER_BIN_DIR"
    
    if ! tee "$USER_BIN_DIR/innioasis-updater" > /dev/null << EOF
#!/bin/bash
# Innioasis Updater Launcher
# Generated by run_linux.sh installer

# Change to installation directory
cd "$INSTALL_DIR" || {
    echo "Error: Cannot access installation directory: $INSTALL_DIR" >&2
    exit 1
}

# Check if main application file exists
if [ ! -f "firmware_downloader.py" ]; then
    echo "Error: firmware_downloader.py not found in $INSTALL_DIR" >&2
    exit 1
fi

# Determine Python executable to use
PYTHON_EXEC="python3"

# Activate virtual environment if it exists
if [ -f "venv/bin/activate" ]; then
    # Source the virtual environment
    source venv/bin/activate
    
    # Use the virtual environment's Python if available
    if [ -f "venv/bin/python" ]; then
        PYTHON_EXEC="./venv/bin/python"
    elif [ -f "venv/bin/python3" ]; then
        PYTHON_EXEC="./venv/bin/python3"
    fi
    
    echo "Using virtual environment Python: $PYTHON_EXEC"
else
    echo "Warning: Virtual environment not found, using system Python"
fi

# Launch the application with the determined Python executable
exec \$PYTHON_EXEC firmware_downloader.py "\$@"
EOF
    then
        error "Failed to create launcher script"
        return 1
    fi
    
    # Make launcher executable
    if ! chmod +x "$USER_BIN_DIR/innioasis-updater"; then
        error "Failed to make launcher script executable"
        return 1
    fi
    
    success "Launcher script created at $USER_BIN_DIR/innioasis-updater"
    
    # Check if ~/.local/bin is in PATH
    if ! echo "$PATH" | grep -q "$HOME/.local/bin"; then
        log "Adding $USER_BIN_DIR to PATH..."
        
        # Add to .bashrc
        if [ -f "$HOME/.bashrc" ]; then
            if ! grep -q 'export PATH="$HOME/.local/bin:$PATH"' "$HOME/.bashrc"; then
                echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
                log "Added $USER_BIN_DIR to ~/.bashrc"
            fi
        fi
        
        # Add to .profile
        if [ -f "$HOME/.profile" ]; then
            if ! grep -q 'export PATH="$HOME/.local/bin:$PATH"' "$HOME/.profile"; then
                echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.profile"
                log "Added $USER_BIN_DIR to ~/.profile"
            fi
        fi
        
        # Add to .zshrc if it exists
        if [ -f "$HOME/.zshrc" ]; then
            if ! grep -q 'export PATH="$HOME/.local/bin:$PATH"' "$HOME/.zshrc"; then
                echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.zshrc"
                log "Added $USER_BIN_DIR to ~/.zshrc"
            fi
        fi
        
        # Update current session PATH
        export PATH="$HOME/.local/bin:$PATH"
        
        log "Note: You may need to restart your terminal or run 'source ~/.bashrc' for the command to be available"
    else
        log "Command 'innioasis-updater' is now available (PATH already configured)"
    fi
    
    return 0
}

launch_updater_detached() {
    local launch_cmd=""

    # Prefer launcher command so any future launcher improvements apply automatically.
    if command -v innioasis-updater >/dev/null 2>&1; then
        launch_cmd="innioasis-updater"
    elif [ -f "$HOME/.local/bin/innioasis-updater" ]; then
        launch_cmd="$HOME/.local/bin/innioasis-updater"
    elif [ -f "$INSTALL_DIR/firmware_downloader.py" ]; then
        local py_exec="python3"
        if [ -f "$INSTALL_DIR/venv/bin/python" ]; then
            py_exec="$INSTALL_DIR/venv/bin/python"
        elif [ -f "$INSTALL_DIR/venv/bin/python3" ]; then
            py_exec="$INSTALL_DIR/venv/bin/python3"
        fi
        launch_cmd="cd \"$INSTALL_DIR\" && \"$py_exec\" firmware_downloader.py"
    else
        return 1
    fi

    # Fully detach from terminal so users can close this window safely.
    nohup bash -lc "$launch_cmd" >/dev/null 2>&1 &
    disown 2>/dev/null || true
    return 0
}

# Show completion message and offer to launch
show_completion_message() {
    echo
    success "Installation complete."
    log "Install location: $INSTALL_DIR"
    log "Launch command: innioasis-updater"
    log "Desktop entry: Innioasis Updater"
    echo
    
    # Check if command is available
    if command -v innioasis-updater >/dev/null 2>&1; then
        log "✅ Command 'innioasis-updater' is ready to use!"
    else
        warning "Command 'innioasis-updater' may not be in PATH yet"
        log "Run: source ~/.bashrc (or restart terminal)"
        log "Fallback launch: ~/.local/bin/innioasis-updater"
        echo
    fi
    
    echo "If your phone is not detected:"
    echo "  1) Reboot or log out/in once (group and udev changes)"
    echo "  2) Stop ModemManager and retry"
    echo "  3) Use a short known-good USB data cable"
    echo

    # Ask if user wants to launch the application
    echo "Launch Innioasis Updater now?"
    read -p "Press Enter to launch, or type 'n' to skip: " -r
    echo
    
    if [[ ! $REPLY =~ ^[Nn]$ ]]; then
        log "🚀 Launching Innioasis Updater..."
        echo

        if launch_updater_detached; then
            success "Innioasis Updater started as a separate GUI process."
            log "You can now close this terminal window safely."
        else
            warning "Could not launch automatically. Start it manually with: innioasis-updater"
        fi
    else
        echo
        log "You can launch later with: innioasis-updater"
        log "Or: ~/.local/bin/innioasis-updater"
    fi
    
    echo
}

# Check if running in a supported environment
check_environment() {
    log "Checking environment compatibility..."
    
    # Check if we're in a Linux environment
    if [ "$(uname -s)" != "Linux" ]; then
        error "This script is designed for Linux systems only."
        return 1
    fi
    
    # Check if we have a display (for GUI)
    if [ -z "$DISPLAY" ] && [ -z "$WAYLAND_DISPLAY" ]; then
        warning "No display detected. GUI may not work properly."
        warning "Make sure you're running this in a graphical environment."
    fi
    
    # Check if we're in a container
    if [ -f /.dockerenv ] || [ -n "$container" ]; then
        warning "Running in a container. Some features may not work properly."
    fi
    
    success "Environment check completed"
    return 0
}

# Main installation function
main() {
    local install_start_ts
    install_start_ts=$(date +%s)

    # Prevent getcwd-related failures if launched from a removed directory.
    ensure_safe_working_directory
    echo
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║               Innioasis Updater Linux Installer             ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    log "Starting installation..."
    
    # Check environment
    phase "Checking your system environment"
    if ! check_environment; then
        error "Environment check failed"
        pause_before_exit
        exit 1
    fi
    
    # Check if running as root
    phase "Validating safe install mode"
    if ! check_root; then
        error "Root check failed"
        pause_before_exit
        exit 1
    fi

    if ! check_existing_updater_instance; then
        pause_before_exit
        exit 1
    fi
    
    # Check for partial installations and clean them up
    phase "Cleaning up any previous partial install"
    if ! check_and_cleanup_partial_installation; then
        error "Partial installation cleanup failed"
        pause_before_exit
        exit 1
    fi
    
    # Check if sudo is available
    phase "Preparing required permissions"
    if ! check_sudo; then
        error "Sudo check failed"
        pause_before_exit
        exit 1
    fi
    
    # Detect architecture and distribution
    phase "Detecting your Linux distribution"
    detect_architecture
    detect_distro
    
    # Install dependencies
    phase "Installing dependencies (this can take a few minutes)"
    if ! install_dependencies; then
        error "Dependency installation failed"
        warning "Some dependencies may not be installed correctly"
        warning "You may need to install them manually"
    fi
    
    # Setup virtual environment
    phase "Setting up bundled Python environment"
    if ! setup_virtual_environment; then
        warning "Virtual environment setup failed"
        warning "Continuing installation with system Python fallback"
    fi
    
    # Setup MTKClient specific requirements
    phase "Applying MTK USB access setup"
    if ! setup_mtkclient_requirements; then
        error "MTKClient requirements setup failed"
        warning "MTKClient may not work properly"
    fi
    
    # Get installation directory early (needed for shared prep script lookup)
    get_install_dir

    # Setup udev rules + SP Flash Tool system prep (soft-fail; never aborts install)
    phase "Installing USB access rules (MediaTek / SP Flash Tool)"
    setup_udev_rules || warning "USB access setup had issues — install continues; app can re-prep later"
    
    # Install Innioasis Updater
    phase "Downloading and installing Innioasis Updater"
    if ! install_innioasis; then
        error "Innioasis Updater installation failed"
        pause_before_exit
        exit 1
    fi

    # Re-run SP Flash Tool prep from the installed tree so files on disk match the app.
    # Soft-fail: password denial or missing tools must not undo a successful install.
    phase "Finalizing SP Flash Tool system prep"
    if [ -f "$INSTALL_DIR/linux_spflash_system_prep.sh" ]; then
        setup_spflash_system_prep || warning "Post-install SP Flash Tool prep skipped — app will retry on first launch"
    else
        warning "Installed tree missing linux_spflash_system_prep.sh — app will prep on first launch"
    fi
    
    # Final optional crypto check (non-blocking)
    if [ -d "$INSTALL_DIR/venv" ] && verify_pycryptodome_installation "$INSTALL_DIR/venv" 1; then
        vlog "Optional crypto backend available in virtual environment"
    elif verify_pycryptodome_installation "" 1; then
        vlog "Optional crypto backend available in system Python"
    else
        warning "Optional crypto backend unavailable; secure/auth workflows may be limited"
    fi
    
    # Fix Cryptodome import statements
    if ! fix_cryptodome_imports; then
        warning "Failed to fix Cryptodome imports"
        warning "You may need to fix import statements manually"
    fi
    
    # Create desktop entry
    if ! create_desktop_entry; then
        warning "Failed to create desktop entry"
    fi
    
    # Create launcher script
    if ! create_launcher; then
        warning "Failed to create launcher script"
    fi
    
    success "Install flow finished in $(elapsed_seconds "$install_start_ts")s"

    # Show completion message
    show_completion_message
}

# Show help
show_help() {
    cat << EOF
Innioasis Updater Linux Launcher

This script installs and configures Innioasis Updater on Linux systems.

Supported distributions:
  - Ubuntu, Linux Mint, Pop!_OS, Elementary OS, Zorin OS
  - Debian
  - Raspberry Pi OS (Raspbian)
  - Arch Linux, Manjaro, EndeavourOS
  - Fedora, RHEL, CentOS, AlmaLinux, Rocky Linux
  - openSUSE, SLES
  - SteamOS, HoloISO
  - ChromeOS Linux, FydeOS Linux
  - Other Linux distributions (generic installation)

Supported architectures:
  - x86_64 (AMD64)
  - aarch64 (ARM64)
  - armv7l/armv6l (ARM 32-bit)
  - i386/i686 (Intel 32-bit)
  - armv5l (ARM 32-bit soft-float)

Usage:
  $0 [OPTIONS]

Options:
  -h, --help     Show this help message
  -i, --install  Install Innioasis Updater (default)
  -u, --uninstall, -uninstall  Uninstall Innioasis Updater
  -l, --launch   Launch Innioasis Updater (if already installed)
  --update       Update Innioasis Updater to latest version
  --cleanup      Clean up partial installations and temporary files

Examples:
  $0                    # Install Innioasis Updater
  $0 --install          # Install Innioasis Updater
  $0 --uninstall        # Uninstall Innioasis Updater
  $0 --launch           # Launch Innioasis Updater
  $0 --update           # Update to latest version
  $0 --cleanup          # Clean up partial installations

Requirements:
  - Python 3.6 or higher
  - PySide6 (or PySide2 as fallback)
  - libusb-1.0
  - Internet connection for downloading dependencies

Environment variables:
  INSTALL_VERBOSE=1                      Enable detailed diagnostic logs
  INSTALL_PYCRYPTO=1                     Attempt optional crypto backend install
  ENABLE_PYCRYPTODOME_SOURCE_BUILD=1     Allow source-build crypto fallback (advanced)

For more information, visit: https://github.com/y1-community/Innioasis-Updater
EOF
}

# Uninstall function
uninstall() {
    log "Uninstalling Innioasis Updater..."
    
    # Get installation directory
    get_install_dir
    
    # Remove installation directory (user directory - no sudo needed)
    if [ -d "$INSTALL_DIR" ]; then
        rm -rf "$INSTALL_DIR"
        success "Removed installation directory: $INSTALL_DIR"
    fi
    
    # Remove launcher scripts
    if [ -f "/usr/local/bin/innioasis-updater" ]; then
        if sudo rm -f "/usr/local/bin/innioasis-updater"; then
            success "Removed system launcher script"
        else
            warning "Failed to remove system launcher script"
        fi
    fi
    
    if [ -f "$HOME/.local/bin/innioasis-updater" ]; then
        if rm -f "$HOME/.local/bin/innioasis-updater"; then
            success "Removed user launcher script"
        else
            warning "Failed to remove user launcher script"
        fi
    fi
    
    # Remove desktop entry
    if [ -f "$HOME/.local/share/applications/innioasis-updater.desktop" ]; then
        rm -f "$HOME/.local/share/applications/innioasis-updater.desktop"
        success "Removed desktop entry"
    fi

    # Remove udev rules created by installer / SP Flash Tool prep (best-effort)
    for rule in \
        99-mediatek.rules \
        78-mediatek-access.rules \
        20-innioasis-mm-blacklist-mtk.rules \
        49-innioasis-ttyacm-mode.rules \
        78-innioasis-mediatek-access.rules \
        99-innioasis-mediatek.rules \
        99-ttyacms.rules
    do
        if [ -f "/etc/udev/rules.d/$rule" ]; then
            if sudo rm -f "/etc/udev/rules.d/$rule"; then
                success "Removed udev rules: /etc/udev/rules.d/$rule"
            else
                warning "Failed to remove /etc/udev/rules.d/$rule"
            fi
        fi
    done
    sudo udevadm control --reload-rules >/dev/null 2>&1 || true
    sudo udevadm trigger >/dev/null 2>&1 || true

    # Remove qcaux blacklist line added by installer, if present
    if [ -f "/etc/modprobe.d/blacklist.conf" ] && grep -q '^blacklist qcaux$' "/etc/modprobe.d/blacklist.conf"; then
        if sudo sed -i '/^blacklist qcaux$/d' "/etc/modprobe.d/blacklist.conf"; then
            success "Removed qcaux blacklist entry from /etc/modprobe.d/blacklist.conf"
        else
            warning "Failed to remove qcaux blacklist entry"
        fi
    fi
    
    # Update desktop database
    if command -v update-desktop-database >/dev/null 2>&1; then
        update-desktop-database "$HOME/.local/share/applications"
    fi
    
    success "Innioasis Updater uninstalled successfully"
}

# Update function
update() {
    log "Updating Innioasis Updater..."
    
    # Get installation directory
    get_install_dir
    
    if [ ! -d "$INSTALL_DIR" ]; then
        error "Innioasis Updater not found. Please install it first using: $0 --install"
        exit 1
    fi
    
    # Download the latest version
    if ! download_innioasis; then
        error "Failed to download latest version of Innioasis Updater"
        return 1
    fi
    
    if [ -z "$DOWNLOAD_DIR" ]; then
        error "Download directory not set"
        return 1
    fi
    
    # Backup current installation
    BACKUP_DIR="$INSTALL_DIR.backup.$(date +%Y%m%d_%H%M%S)"
    if sudo mv "$INSTALL_DIR" "$BACKUP_DIR"; then
        log "Backed up current installation to $BACKUP_DIR"
    else
        warning "Failed to backup current installation"
    fi
    
    # Create new installation directory
    if ! sudo mkdir -p "$INSTALL_DIR"; then
        error "Failed to create installation directory: $INSTALL_DIR"
        rm -rf "$(dirname "$DOWNLOAD_DIR")"
        return 1
    fi
    
    # Copy new files
    if ! sudo cp -r "$DOWNLOAD_DIR"/* "$INSTALL_DIR/"; then
        error "Failed to copy new files to installation directory"
        rm -rf "$(dirname "$DOWNLOAD_DIR")"
        return 1
    fi
    
    # Clean up temporary directory
    rm -rf "$(dirname "$DOWNLOAD_DIR")"
    
    # Set proper permissions
    sudo chown -R root:root "$INSTALL_DIR"
    sudo chmod -R 755 "$INSTALL_DIR"
    sudo chmod +x "$INSTALL_DIR"/*.py 2>/dev/null || true
    sudo chmod +x "$INSTALL_DIR"/*.sh 2>/dev/null || true
    
    success "Innioasis Updater updated successfully"
    
    # Ask if user wants to remove backup
    echo
    read -p "Would you like to remove the backup directory ($BACKUP_DIR)? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        sudo rm -rf "$BACKUP_DIR"
        success "Backup directory removed"
    else
        log "Backup directory kept at: $BACKUP_DIR"
    fi
}

# Launch function
launch() {
    log "Launching Innioasis Updater..."
    
    # Get installation directory
    get_install_dir
    
    # Try to use the launcher script first
    if command -v innioasis-updater >/dev/null 2>&1; then
        log "Using launcher script: innioasis-updater"
        innioasis-updater
    elif [ -f "$HOME/.local/bin/innioasis-updater" ]; then
        log "Using user launcher: $HOME/.local/bin/innioasis-updater"
        "$HOME/.local/bin/innioasis-updater"
    elif [ -f "$INSTALL_DIR/firmware_downloader.py" ]; then
        log "Using direct Python execution"
        cd "$INSTALL_DIR"
        
        # Determine Python executable to use
        PYTHON_EXEC="python3"
        
        # Use virtual environment Python if available
        if [ -f "venv/bin/python" ]; then
            PYTHON_EXEC="./venv/bin/python"
            log "Using virtual environment Python: $PYTHON_EXEC"
        elif [ -f "venv/bin/python3" ]; then
            PYTHON_EXEC="./venv/bin/python3"
            log "Using virtual environment Python: $PYTHON_EXEC"
        else
            log "Virtual environment not found, using system Python"
        fi
        
        exec $PYTHON_EXEC firmware_downloader.py
    else
        error "Innioasis Updater not found. Please install it first using: $0 --install"
        error "Expected location: $INSTALL_DIR/firmware_downloader.py"
        exit 1
    fi
}

# Parse command line arguments
case "${1:-}" in
    -h|--help)
        show_help
        exit 0
        ;;
    -u|--uninstall|-uninstall)
        uninstall
        exit 0
        ;;
    -l|--launch)
        launch
        exit 0
        ;;
    --update)
        update
        exit 0
        ;;
    --cleanup)
        check_and_cleanup_partial_installation
        exit 0
        ;;
    -i|--install|"")
        main
        ;;
    *)
        error "Unknown option: $1"
        show_help
        exit 1
        ;;
esac
