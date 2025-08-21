#!/usr/bin/env python3
"""
Driver Setup GUI for Y1 Helper
Provides a modern interface for installing WinFSP, UsbDk, Git, and MTK drivers
"""

import sys
import os
import shutil
import platform
import subprocess
import requests
import json
import re
from pathlib import Path
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, 
                                QWidget, QPushButton, QTextEdit, QLabel, QProgressBar, 
                                QMessageBox, QGroupBox, QFrame)
from PySide6.QtCore import QThread, Signal, Qt, QTimer
from PySide6.QtGui import QFont, QIcon, QPixmap


class DriverSetupGUI(QMainWindow):
    """Main GUI window for driver setup"""
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Y1 Helper - Driver Setup")
        self.setFixedSize(700, 650)
        self.setup_ui()
        self.installer_thread = None
        
        # Dictionary of paths and URLs needed
        self.path_dict = {
            "winfsp": "https://api.github.com/repos/winfsp/winfsp/releases/latest",
            "usbdk": "https://api.github.com/repos/daynix/UsbDk/releases/latest",
            "git": "https://api.github.com/repos/git-for-windows/git/releases/latest",
            "mtk_preloader_driver": "https://androiddatahost.com/wp-content/uploads/Mediatek_Driver_Auto_Installer_v1.1352.zip"
        }
        self.arch = platform.architecture()[0]
        self.app_path = os.path.dirname(__file__)
        
    def setup_ui(self):
        """Setup the user interface"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Header
        header_label = QLabel("Y1 Helper Driver Setup")
        header_label.setFont(QFont("Segoe UI", 18, QFont.Bold))
        header_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(header_label)
        
        # Description
        desc_label = QLabel("This tool will install the necessary drivers and tools for Y1 Helper to function properly.")
        desc_label.setFont(QFont("Segoe UI", 10))
        desc_label.setAlignment(Qt.AlignCenter)
        desc_label.setWordWrap(True)
        main_layout.addWidget(desc_label)
        
        # Installation steps group
        steps_group = QGroupBox("Installation Steps")
        steps_group.setFont(QFont("Segoe UI", 11, QFont.Bold))
        steps_layout = QVBoxLayout(steps_group)
        steps_layout.setSpacing(15)
        
        # Step buttons
        self.mtk_btn = self.create_step_button("Install MTK USB Driver", "MediaTek preloader USB driver for device communication")
        self.usbdk_btn = self.create_step_button("Install USB Development Kit", "USB device development kit for Windows")
        self.winfsp_btn = self.create_step_button("Install WinFSP", "File system driver for Windows compatibility")
        self.reboot_btn = self.create_step_button("Reboot System", "Restart system to complete driver installation")
        
        steps_layout.addWidget(self.mtk_btn)
        steps_layout.addWidget(self.usbdk_btn)
        steps_layout.addWidget(self.winfsp_btn)
        steps_layout.addWidget(self.reboot_btn)
        
        main_layout.addWidget(steps_group)
        
        # Progress section
        progress_group = QGroupBox("Progress")
        progress_group.setFont(QFont("Segoe UI", 11, QFont.Bold))
        progress_layout = QVBoxLayout(progress_group)
        
        # Download progress bar
        self.download_progress = QProgressBar()
        self.download_progress.setVisible(False)
        progress_layout.addWidget(self.download_progress)
        
        # Status label
        self.status_label = QLabel("Ready to install drivers")
        self.status_label.setFont(QFont("Segoe UI", 10))
        progress_layout.addWidget(self.status_label)
        
        main_layout.addWidget(progress_group)
        
        # Connect step buttons
        self.mtk_btn.clicked.connect(lambda: self.install_single_step("MTK USB Driver", self.install_mtk_drivers))
        self.usbdk_btn.clicked.connect(lambda: self.install_single_step("USB Development Kit", self.install_usbdk))
        self.winfsp_btn.clicked.connect(lambda: self.install_single_step("WinFSP", self.install_winfsp))
        self.reboot_btn.clicked.connect(self.reboot_system)
        
    def create_step_button(self, text, description):
        """Create a standard step button"""
        button = QPushButton(text)
        button.setFont(QFont("Segoe UI", 11))
        button.setMinimumHeight(50)
        
        # Add description as tooltip
        button.setToolTip(description)
        
        return button
        
    def install_single_step(self, step_name, step_func):
        """Install a single step"""
        try:
            self.status_label.setText(f"Downloading {step_name}...")
            
            success = step_func()
            
            if success:
                self.status_label.setText(f"{step_name} - Installer launched")
                # Disable the button
                sender = self.sender()
                sender.setEnabled(False)
                sender.setText(f"✅ {sender.text()}")
            else:
                self.status_label.setText(f"{step_name} - Ready to try again")
                
        except Exception as e:
            self.status_label.setText(f"{step_name} - Ready to try again")
            
    def reboot_system(self):
        """Reboot the system"""
        reply = QMessageBox.question(self, "Confirm Reboot", 
                                   "Are you sure you want to reboot your system now?",
                                   QMessageBox.Yes | QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            self.status_label.setText("Rebooting in 10 seconds...")
            
            # Countdown timer
            self.countdown_timer = QTimer()
            self.countdown_timer.timeout.connect(self.reboot_countdown)
            self.countdown_counter = 10
            self.reboot_timer = QTimer()
            self.reboot_timer.timeout.connect(self.execute_reboot)
            self.reboot_timer.setSingleShot(True)
            self.reboot_timer.start(10000)  # 10 seconds
            self.countdown_timer.start(1000)  # Every second
            
    def reboot_countdown(self):
        """Update countdown display"""
        self.countdown_counter -= 1
        if self.countdown_counter > 0:
            self.status_label.setText(f"Rebooting in {self.countdown_counter} seconds...")
        else:
            self.countdown_timer.stop()
            
    def execute_reboot(self):
        """Execute the actual reboot"""
        try:
            os.system("shutdown /r /t 0")
        except Exception as e:
            self.status_label.setText("Reboot initiated")
            
    # Installation functions
    def find_python_latest(self):
        """Finds latest python version in development"""
        try:
            url = "https://www.python.org/doc/versions/"
            response = requests.get(url, timeout=10)
    matches = re.findall(r'<a class="reference external" href="(https://docs.python.org/release/[\d.]+/)">Python ([\d.]+)</a>, documentation released on [\d\s\w]+', response.text)

    if matches:
        latest_version_url, latest_version_number = matches[0]
    return latest_version_number
        else:
                return "3.11.0"  # Fallback version
        except:
            return "3.11.0"  # Fallback version
            
    def pull_latest_release(self, url, filename, arch_select=""):
        """Pulls the latest release from github"""
        try:
            response = requests.get(url, timeout=10)
        data = json.loads(response.text)

        if arch_select == "":
                asset_url = data["assets"][0]["browser_download_url"]
        else:
            if arch_select == "64bit":
                    filter_suffix = "-64-bit.exe"
            elif arch_select == "32bit":
                    filter_suffix = "-32-bit.exe"
                else:
                    filter_suffix = ".exe"
                
                # Find asset with matching suffix
                asset_url = None
                for asset in data["assets"]:
                    if asset["name"].endswith(filter_suffix):
                    asset_url = asset["browser_download_url"]
                    break
                
                if not asset_url:
                    asset_url = data["assets"][0]["browser_download_url"]  # Fallback
            
            # Download the file with progress
            self.download_progress.setVisible(True)
            self.download_progress.setValue(0)
            
            response = requests.get(asset_url, timeout=30, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            
            file_path = os.path.join(self.app_path, filename)
            downloaded = 0
            
            with open(file_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_size > 0:
                            progress = int((downloaded / total_size) * 100)
                            self.download_progress.setValue(progress)
            
            self.download_progress.setVisible(False)
            return file_path
            
        except Exception as e:
            self.download_progress.setVisible(False)
            print(f"Failed to download {filename}: {e}")
            return None
            
    def install_winfsp(self):
        """Install WinFSP"""
        try:
            file_path = self.pull_latest_release(self.path_dict["winfsp"], "winfsp.msi")
            if file_path and os.path.exists(file_path):
                # Launch MSI installer and let it handle itself
                subprocess.Popen(["msiexec", "/i", file_path])
        return True
            return False
    except Exception as e:
            print(f"WinFSP installation failed: {e}")
            return False
            
    def install_usbdk(self):
        """Install UsbDk"""
        try:
            file_path = self.pull_latest_release(self.path_dict["usbdk"], "usbdk.msi")
            if file_path and os.path.exists(file_path):
                # Launch MSI installer and let it handle itself
                subprocess.Popen(["msiexec", "/i", file_path])
                return True
            return False
        except Exception as e:
            print(f"UsbDk installation failed: {e}")
            return False
            
    def install_git(self):
        """Install Git"""
        try:
            file_path = self.pull_latest_release(self.path_dict["git"], "git_inst.exe", self.arch)
            if file_path and os.path.exists(file_path):
                # Launch Git installer and let it handle itself
                subprocess.Popen([file_path])
        return True
            return False
    except Exception as e:
            print(f"Git installation failed: {e}")
        return False

    def install_mtk_drivers(self):
        """Install MTK Preloader Driver"""
        try:
            filename = "mtk_preloader_driver.zip"
            driver_folder = "mtk_preloader_driver"
            
            # Download drivers with progress
            self.download_progress.setVisible(True)
            self.download_progress.setValue(0)
            
            response = requests.get(self.path_dict["mtk_preloader_driver"], timeout=30, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            
            file_path = os.path.join(self.app_path, filename)
            downloaded = 0
            
            with open(file_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_size > 0:
                            progress = int((downloaded / total_size) * 100)
                            self.download_progress.setValue(progress)
            
            self.download_progress.setVisible(False)
            
            # Unzip and launch installer
            shutil.unpack_archive(file_path, driver_folder)
            abs_path = os.path.join(self.app_path, driver_folder, 
                                  "Mediatek Driver Auto Installer v1.1352")
            
            # Launch the installer and let it handle itself
            if os.path.exists(os.path.join(abs_path, "Install Drivers.bat")):
                subprocess.Popen(["cmd", "/c", "Install Drivers.bat"], cwd=abs_path)
                return True
        return False
    
        except Exception as e:
            self.download_progress.setVisible(False)
            print(f"MTK driver installation failed: {e}")
            return False
    

def main():
    """Main entry point"""
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Use Fusion style for consistent look
    
    # Set application icon if available
    icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(icon_path))
    
    window = DriverSetupGUI()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
