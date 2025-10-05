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
        
        # Special handling for Raspberry Pi OS
        if [ "$ID" = "debian" ] && [ -f /etc/rpi-issue ]; then
            DISTRO_ID="raspbian"
            DISTRO_NAME="Raspberry Pi OS"
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

# Check if running as root
check_root() {
    if [ "$EUID" -eq 0 ]; then
        error "This script should not be run as root for security reasons."
        error "Please run as a regular user. The script will use sudo when needed."
        return 1
    fi
    return 0
}

# Check for partial installations and clean them up
check_and_cleanup_partial_installation() {
    log "Checking for previous partial installations..."
    
    # Get installation directory
    get_install_dir
    
    local cleanup_needed=false
    
    # Check for incomplete installation directory
    if [ -d "$INSTALL_DIR" ]; then
        # Check if installation is incomplete
        if [ ! -f "$INSTALL_DIR/firmware_downloader.py" ] || [ ! -f "$INSTALL_DIR/README.md" ]; then
            warning "Found incomplete installation directory: $INSTALL_DIR"
            cleanup_needed=true
        else
            log "Found existing complete installation at: $INSTALL_DIR"
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
    log "This script requires sudo permissions for:"
    log "  - Installing system packages"
    log "  - Setting up udev rules for USB device access"
    log "  - Creating system directories"
    log ""
    log "Requesting sudo permissions..."
    
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
        error "Failed to create virtual environment"
        return 1
    fi
    
    # Activate virtual environment and install packages
    log "Installing Python packages in virtual environment..."
    if source "$VENV_DIR/bin/activate" && pip install --upgrade pip; then
        success "pip upgraded in virtual environment"
    else
        error "Failed to upgrade pip in virtual environment"
        return 1
    fi
    
    # Install all required packages
    if source "$VENV_DIR/bin/activate" && pip install $PYTHON_PACKAGES; then
        success "Python packages installed in virtual environment"
    else
        error "Failed to install Python packages in virtual environment"
        return 1
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

# Fix Cryptodome import statements in Innioasis Updater code
fix_cryptodome_imports() {
    log "Fixing Cryptodome import statements..."
    
    # Get installation directory
    get_install_dir
    
    # Fix all Python files that have incorrect Cryptodome imports
    if find "$INSTALL_DIR" -name "*.py" -exec grep -l "from Cryptodome" {} \; 2>/dev/null | head -1 | grep -q .; then
        log "Found files with incorrect Cryptodome imports, fixing..."
        find "$INSTALL_DIR" -name "*.py" -exec sed -i 's/from Cryptodome/from Crypto/g' {} \;
        success "Cryptodome import statements fixed"
    else
        log "No incorrect Cryptodome imports found"
    fi
    
    # Fix firmware_downloader.py to use virtual environment Python for mtk.py calls
    log "Updating firmware_downloader.py to use virtual environment..."
    firmware_downloader="$INSTALL_DIR/firmware_downloader.py"
    
    if [ -f "$firmware_downloader" ]; then
        # Create backup
        cp "$firmware_downloader" "$firmware_downloader.backup"
        
        # Create a Python script to fix the firmware_downloader.py
        cat > "$INSTALL_DIR/fix_firmware_downloader.py" << 'EOF'
#!/usr/bin/env python3
import re
import sys

def fix_firmware_downloader(file_path):
    """Fix firmware_downloader.py to use virtual environment Python for mtk.py calls"""
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Fix the main mtk.py call in the run() method
    # Replace sys.executable with python_executable
    content = re.sub(
        r'(\s+)cmd = \[\s*sys\.executable, "mtk\.py"',
        r'\1# Use virtual environment Python if available, otherwise use system Python\n\1python_executable = sys.executable\n\1venv_python = os.path.join(os.getcwd(), "venv", "bin", "python")\n\1if os.path.exists(venv_python):\n\1    python_executable = venv_python\n\1\n\1cmd = [\n\1    python_executable, "mtk.py"',
        content
    )
    
    # Fix the terminal command generation for Linux
    content = re.sub(
        r'python3 mtk\.py w uboot,bootimg,recovery,android,usrdata lk\.bin,boot\.img,recovery\.img,system\.img,userdata\.img',
        r'$(if [ -f "venv/bin/python" ]; then echo "./venv/bin/python"; else echo "python3"; fi) mtk.py w uboot,bootimg,recovery,android,usrdata lk.bin,boot.img,recovery.img,system.img,userdata.img',
        content
    )
    
    # Fix the macOS terminal script
    content = re.sub(
        r'# Run MTK command with python3 \(same as used in regular installation\)\npython3 mtk\.py w uboot,bootimg,recovery,android,usrdata lk\.bin,boot\.img,recovery\.img,system\.img,userdata\.img',
        r'# Run MTK command with virtual environment Python if available, otherwise python3\nif [ -f "venv/bin/python" ]; then\n    ./venv/bin/python mtk.py w uboot,bootimg,recovery,android,usrdata lk.bin,boot.img,recovery.img,system.img,userdata.img\nelse\n    python3 mtk.py w uboot,bootimg,recovery,android,usrdata lk.bin,boot.img,recovery.img,system.img,userdata.img\nfi',
        content
    )
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    print(f"Fixed {file_path} to use virtual environment")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 fix_firmware_downloader.py <firmware_downloader.py>")
        sys.exit(1)
    
    fix_firmware_downloader(sys.argv[1])
EOF
        
        # Run the fix script
        if python3 "$INSTALL_DIR/fix_firmware_downloader.py" "$firmware_downloader"; then
            success "firmware_downloader.py updated to use virtual environment"
            rm -f "$INSTALL_DIR/fix_firmware_downloader.py"
        else
            warning "Failed to update firmware_downloader.py"
            # Restore backup
            mv "$firmware_downloader.backup" "$firmware_downloader"
        fi
    else
        warning "firmware_downloader.py not found, skipping virtual environment fix"
    fi
    
    return 0
}

# Install Python packages via pip as fallback
install_python_packages_via_pip() {
    log "Installing Python packages via pip..."
    
    # Check if pip is available
    if ! command -v pip3 >/dev/null 2>&1; then
        warning "pip3 not available, skipping Python package installation"
        return 1
    fi
    
    # Install packages via pip
    # Try with --break-system-packages for Ubuntu 25.04+ which has externally-managed-environment
    PYTHON_PACKAGES="PySide6 requests lxml configparser colorama capstone keystone-engine pycryptodome usb pyusb libusb1 pyserial adbutils pillow numpy"
    
    if pip3 install --user --break-system-packages $PYTHON_PACKAGES 2>/dev/null; then
        success "Python packages installed via pip successfully"
    elif pip3 install --user $PYTHON_PACKAGES 2>/dev/null; then
        success "Python packages installed via pip successfully"
    else
        warning "Failed to install some Python packages via pip"
        warning "You may need to install them manually later"
        warning "Try: pip3 install --user --break-system-packages $PYTHON_PACKAGES"
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
        arch|manjaro|endeavouros)
            install_arch_deps
            ;;
        fedora|rhel|centos|almalinux|rocky)
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
    BASE_PACKAGES="python3 python3-pip python3-venv python3-dev python3-setuptools pkg-config git curl wget unzip udev usbutils android-tools-adb android-tools-fastboot cmake build-essential gcc g++ make libffi-dev libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libncurses5-dev libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev"
    
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
    BASE_PACKAGES="python3 python3-pip python3-venv python3-dev python3-setuptools pkg-config git curl wget unzip udev usbutils"
    
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
    
    # Update package database
    sudo pacman -Sy
    
    # Base packages for all architectures
    BASE_PACKAGES="python python-pip python-virtualenv python-setuptools pkgconf base-devel git curl wget unzip udev usbutils cmake gcc gcc-libs make libffi openssl zlib bzip2 readline sqlite tk libxml2 xz-utils ncurses android-tools"
    
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
    
    sudo pacman -S --noconfirm $BASE_PACKAGES $ARCH_PACKAGES
    
    # Install Python packages (try PySide6 first, fallback to PySide2)
    if sudo pacman -S --noconfirm \
        python-pyside6 \
        python-requests \
        python-lxml 2>/dev/null; then
        success "PySide6 packages installed successfully"
    else
        warning "PySide6 not available, trying PySide2..."
        sudo pacman -S --noconfirm \
            python-pyside2 \
            python-requests \
            python-lxml
    fi
    
    success "Arch dependencies installed successfully"
}

# Fedora/RHEL-based distributions
install_fedora_deps() {
    log "Installing dependencies for Fedora/RHEL-based distribution..."
    
    # Update package database
    sudo dnf update -y
    
    # Base packages for all architectures
    BASE_PACKAGES="python3 python3-pip python3-venv python3-devel python3-setuptools pkgconfig gcc gcc-c++ make git curl wget unzip systemd-udev usbutils cmake libffi-devel openssl-devel zlib-devel bzip2-devel readline-devel sqlite-devel tk-devel libxml2-devel xz-devel ncurses-devel android-tools"
    
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
    
    sudo dnf install -y $BASE_PACKAGES $ARCH_PACKAGES
    
    # Install Python packages (try PySide6 first, fallback to PySide2)
    if sudo dnf install -y \
        python3-PySide6 \
        python3-requests \
        python3-lxml 2>/dev/null; then
        success "PySide6 packages installed successfully"
    else
        warning "PySide6 not available, trying PySide2..."
        sudo dnf install -y \
            python3-PySide2 \
            python3-requests \
            python3-lxml
    fi
    
    success "Fedora/RHEL dependencies installed successfully"
}

# openSUSE
install_opensuse_deps() {
    log "Installing dependencies for openSUSE..."
    
    # Update package database
    sudo zypper refresh
    
    # Base packages for all architectures
    BASE_PACKAGES="python3 python3-pip python3-venv python3-devel python3-setuptools pkg-config gcc gcc-c++ make git curl wget unzip udev usbutils cmake libffi-devel openssl-devel zlib-devel bzip2-devel readline-devel sqlite3-devel tk-devel libxml2-devel xz-devel ncurses-devel android-tools"
    
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
        pip3 install --user --break-system-packages PySide6 requests lxml configparser colorama capstone pycryptodome usb pyusb libusb1 pyserial adbutils
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
        sudo pacman -Sy 2>/dev/null || true
        sudo pacman -S --noconfirm base-devel cmake pkgconf libusb 2>/dev/null || warning "Could not install build tools via pacman"
    elif command -v dnf >/dev/null 2>&1; then
        sudo dnf update -y 2>/dev/null || true
        sudo dnf install -y gcc gcc-c++ make cmake pkgconfig libusb1-devel 2>/dev/null || warning "Could not install build tools via dnf"
    elif command -v zypper >/dev/null 2>&1; then
        sudo zypper refresh 2>/dev/null || true
        sudo zypper install -y gcc gcc-c++ make cmake pkg-config libusb-1_0-devel 2>/dev/null || warning "Could not install build tools via zypper"
    fi
    
    # Install Python packages via pip
    # Try with --break-system-packages for Ubuntu 25.04+ which has externally-managed-environment
    PYTHON_PACKAGES="PySide6 requests lxml configparser colorama capstone pycryptodome usb pyusb libusb1 pyserial adbutils pillow numpy"
    
    log "Installing Python packages..."
    if ! pip3 install --user --break-system-packages $PYTHON_PACKAGES 2>/dev/null; then
        if ! pip3 install --user $PYTHON_PACKAGES 2>/dev/null; then
            warning "Some Python packages failed to install. Trying individual packages..."
            for package in $PYTHON_PACKAGES; do
                if ! pip3 install --user --break-system-packages $package 2>/dev/null; then
                    pip3 install --user $package 2>/dev/null || warning "Failed to install $package"
                fi
            done
        fi
    fi
    
    # Try to install keystone-engine separately (it often needs build tools)
    log "Attempting to install keystone-engine..."
    if ! pip3 install --user --break-system-packages keystone-engine 2>/dev/null; then
        pip3 install --user keystone-engine 2>/dev/null || warning "keystone-engine failed to install (requires cmake and build tools)"
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
    cd "$TEMP_DIR"
    
    # Download Android Platform Tools
    log "Downloading Android Platform Tools..."
    if command -v wget >/dev/null 2>&1; then
        if wget -O platform-tools.zip https://dl.google.com/android/repository/platform-tools-latest-linux.zip 2>/dev/null; then
            success "Downloaded Android Platform Tools"
        else
            warning "Failed to download Android Platform Tools with wget"
            rm -rf "$TEMP_DIR"
            return 1
        fi
    elif command -v curl >/dev/null 2>&1; then
        if curl -L -o platform-tools.zip https://dl.google.com/android/repository/platform-tools-latest-linux.zip 2>/dev/null; then
            success "Downloaded Android Platform Tools"
        else
            warning "Failed to download Android Platform Tools with curl"
            rm -rf "$TEMP_DIR"
            return 1
        fi
    else
        warning "Neither wget nor curl available for downloading Android Platform Tools"
        rm -rf "$TEMP_DIR"
        return 1
    fi
    
    # Extract the archive
    if command -v unzip >/dev/null 2>&1; then
        if unzip -q platform-tools.zip 2>/dev/null; then
            success "Extracted Android Platform Tools"
        else
            warning "Failed to extract Android Platform Tools"
            rm -rf "$TEMP_DIR"
            return 1
        fi
    else
        warning "unzip not available for extracting Android Platform Tools"
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
        rm -rf "$TEMP_DIR"
        return 1
    fi
    
    # Clean up
    rm -rf "$TEMP_DIR"
    return 0
}

# Create udev rules for USB access
setup_udev_rules() {
    log "Setting up udev rules for USB device access..."
    
    # Create udev rules directory if it doesn't exist
    if ! sudo mkdir -p /etc/udev/rules.d; then
        error "Failed to create udev rules directory"
        return 1
    fi
    
    # Create udev rule for MediaTek devices
    if ! sudo tee /etc/udev/rules.d/99-mediatek.rules > /dev/null << 'EOF'
# MediaTek USB devices
SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="0bb4", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="18d1", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="22d9", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e8a", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e8b", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e8c", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e8d", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e8e", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e8f", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e90", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e91", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e92", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e93", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e94", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e95", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e96", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e97", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e98", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e99", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e9a", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e9b", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e9c", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e9d", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e9e", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2e9f", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ea0", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ea1", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ea2", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ea3", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ea4", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ea5", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ea6", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ea7", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ea8", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ea9", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eaa", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eab", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eac", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ead", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eae", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eaf", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eb0", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eb1", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eb2", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eb3", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eb4", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eb5", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eb6", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eb7", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eb8", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eb9", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eba", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ebb", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ebc", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ebd", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ebe", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ebf", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ec0", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ec1", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ec2", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ec3", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ec4", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ec5", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ec6", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ec7", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ec8", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ec9", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eca", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ecb", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ecc", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ecd", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ece", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ecf", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ed0", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ed1", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ed2", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ed3", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ed4", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ed5", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ed6", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ed7", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ed8", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ed9", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eda", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2edb", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2edc", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2edd", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ede", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2edf", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ee0", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ee1", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ee2", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ee3", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ee4", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ee5", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ee6", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ee7", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ee8", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ee9", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eea", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eeb", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eec", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eed", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eee", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eef", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ef0", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ef1", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ef2", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ef3", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ef4", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ef5", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ef6", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ef7", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ef8", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2ef9", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2efa", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2efb", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2efc", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2efd", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2efe", MODE="0666", GROUP="plugdev"
SUBSYSTEM=="usb", ATTR{idVendor}=="2eff", MODE="0666", GROUP="plugdev"
EOF
    then
        error "Failed to create udev rules file"
        return 1
    fi
    
    # Add user to plugdev group if it exists
    if getent group plugdev >/dev/null 2>&1; then
        if sudo usermod -a -G plugdev "$USER"; then
            log "Added user $USER to plugdev group"
        else
            warning "Failed to add user to plugdev group"
        fi
    else
        warning "plugdev group does not exist on this system"
    fi
    
    # Reload udev rules
    if sudo udevadm control --reload-rules && sudo udevadm trigger; then
        success "udev rules configured successfully"
        return 0
    else
        error "Failed to reload udev rules"
        return 1
    fi
}

# Determine appropriate installation directory
get_install_dir() {
    # Default to user directory for better compatibility and no sudo requirements
    case "$DISTRO_ID" in
        ubuntu|linuxmint|pop|elementary|zorin|debian)
            INSTALL_DIR="/home/$USER/.local/share/innioasis-updater"
            ;;
        arch|manjaro|endeavouros)
            INSTALL_DIR="/home/$USER/.local/share/innioasis-updater"
            ;;
        fedora|rhel|centos|almalinux|rocky)
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
    log "Downloading Innioasis Updater from GitHub..."
    
    # Create temporary directory for download
    TEMP_DIR=$(mktemp -d)
    if [ ! -d "$TEMP_DIR" ]; then
        error "Failed to create temporary directory"
        return 1
    fi
    
    # Try to clone the repository
    log "Cloning repository from https://github.com/team-slide/Innioasis-Updater..."
    if git clone https://github.com/team-slide/Innioasis-Updater.git "$TEMP_DIR/innioasis-updater" 2>/dev/null; then
        success "Repository cloned successfully"
        DOWNLOAD_DIR="$TEMP_DIR/innioasis-updater"
    else
        warning "Git clone failed, trying to download as ZIP archive..."
        
        # Download as ZIP if git is not available
        ZIP_FILE="$TEMP_DIR/innioasis-updater.zip"
        if command -v wget >/dev/null 2>&1; then
            if wget -O "$ZIP_FILE" https://github.com/team-slide/Innioasis-Updater/archive/refs/heads/main.zip 2>/dev/null; then
                success "ZIP archive downloaded successfully"
            else
                error "Failed to download ZIP archive with wget"
                rm -rf "$TEMP_DIR"
                return 1
            fi
        elif command -v curl >/dev/null 2>&1; then
            if curl -L -o "$ZIP_FILE" https://github.com/team-slide/Innioasis-Updater/archive/refs/heads/main.zip 2>/dev/null; then
                success "ZIP archive downloaded successfully"
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
        if command -v unzip >/dev/null 2>&1; then
            if unzip -q "$ZIP_FILE" -d "$TEMP_DIR" 2>/dev/null; then
                success "ZIP archive extracted successfully"
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
    
    success "Innioasis Updater downloaded successfully"
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

# Activate virtual environment if it exists
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
fi

# Launch the application
exec python3 firmware_downloader.py "\$@"
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

# Show completion message and offer to launch
show_completion_message() {
    echo
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║                    🎉 Installation Complete! 🎉              ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo
    success "Innioasis Updater has been successfully installed!"
    echo
    log "📁 Installation directory: $INSTALL_DIR"
    log "🚀 Launcher command: innioasis-updater"
    log "🖥️  Desktop shortcut: Available in your applications menu"
    log "🌐 Website: https://innioasis.app"
    echo
    
    # Check if command is available
    if command -v innioasis-updater >/dev/null 2>&1; then
        log "✅ Command 'innioasis-updater' is ready to use!"
    else
        warning "Command 'innioasis-updater' may not be in PATH yet"
        log "Try running: source ~/.bashrc"
        log "Or restart your terminal"
        log "Or run directly: ~/.local/bin/innioasis-updater"
        echo
    fi
    
    # Ask if user wants to launch the application
    echo "Would you like to launch Innioasis Updater now?"
    read -p "Press Enter to launch, or type 'n' to skip: " -r
    echo
    
    if [[ ! $REPLY =~ ^[Nn]$ ]]; then
        log "🚀 Launching Innioasis Updater..."
        echo
        
        # User installation
        if command -v innioasis-updater >/dev/null 2>&1; then
            innioasis-updater
        elif [ -f "$HOME/.local/bin/innioasis-updater" ]; then
            "$HOME/.local/bin/innioasis-updater"
        else
            cd "$INSTALL_DIR"
            python3 firmware_downloader.py
        fi
    else
        echo
        log "You can launch Innioasis Updater later using:"
        echo "    innioasis-updater"
        echo "    or: ~/.local/bin/innioasis-updater"
        echo "    or find it in your applications menu"
    fi
    
    echo
    echo "Thank you for using Innioasis Updater! 🙏"
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
    log "Starting Innioasis Updater Linux installation..."
    
    # Check environment
    if ! check_environment; then
        error "Environment check failed"
        pause_before_exit
        exit 1
    fi
    
    # Check if running as root
    if ! check_root; then
        error "Root check failed"
        pause_before_exit
        exit 1
    fi
    
    # Check for partial installations and clean them up
    if ! check_and_cleanup_partial_installation; then
        error "Partial installation cleanup failed"
        pause_before_exit
        exit 1
    fi
    
    # Check if sudo is available
    if ! check_sudo; then
        error "Sudo check failed"
        pause_before_exit
        exit 1
    fi
    
    # Detect architecture and distribution
    detect_architecture
    detect_distro
    
    # Install dependencies
    if ! install_dependencies; then
        error "Dependency installation failed"
        warning "Some dependencies may not be installed correctly"
        warning "You may need to install them manually"
    fi
    
    # Setup virtual environment
    if ! setup_virtual_environment; then
        error "Virtual environment setup failed"
        pause_before_exit
        exit 1
    fi
    
    # Setup udev rules
    if ! setup_udev_rules; then
        error "udev rules setup failed"
        warning "USB device access may not work properly"
    fi
    
    # Get installation directory
    get_install_dir
    
    # Install Innioasis Updater
    if ! install_innioasis; then
        error "Innioasis Updater installation failed"
        pause_before_exit
        exit 1
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
  -u, --uninstall Uninstall Innioasis Updater
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

For more information, visit: https://github.com/team-slide/Innioasis-Updater
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
        python3 firmware_downloader.py
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
    -u|--uninstall)
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
