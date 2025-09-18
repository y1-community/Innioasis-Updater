#!/usr/bin/env python3
"""
Rockbox 360p Theme Downloader for Y1
Downloads all theme zips from rockbox-y1/rockbox releases and installs them to .rockbox folder
"""

import sys
import os
import zipfile
import subprocess
import threading
import requests
import json
import shutil
from pathlib import Path
from urllib.parse import urlparse
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
                               QWidget, QListWidget, QListWidgetItem, QPushButton, QTextEdit,
                               QLabel, QProgressBar, QMessageBox, QFileDialog, QGroupBox,
                               QFrame, QSpacerItem, QSizePolicy)
from PySide6.QtCore import QThread, Signal, Qt, QSize, QTimer, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QFont, QPixmap, QPalette, QColor
import platform
import time

# Global silent mode flag
SILENT_MODE = True

def silent_print(*args, **kwargs):
    """Print only if not in silent mode"""
    if not SILENT_MODE:
        print(*args, **kwargs)

class ThemeDownloadWorker(QThread):
    """Worker thread for downloading themes"""
    progress = Signal(int)
    status = Signal(str)
    finished = Signal(list)
    error = Signal(str)
    
    def __init__(self, release_url, download_dir):
        super().__init__()
        self.release_url = release_url
        self.download_dir = download_dir
        self.themes = []
        
    def run(self):
        try:
            self.status.emit("Fetching release information...")
            
            # Get release information from GitHub API
            api_url = self.release_url.replace("https://github.com/", "https://api.github.com/repos/")
            api_url = api_url.replace("/releases/tag/", "/releases/tags/")
            
            response = requests.get(api_url, timeout=30)
            response.raise_for_status()
            release_data = response.json()
            
            # Find all zip files in the release assets
            zip_assets = [asset for asset in release_data.get('assets', []) 
                         if asset['name'].endswith('.zip')]
            
            if not zip_assets:
                self.error.emit("No zip files found in release")
                return
                
            self.status.emit(f"Found {len(zip_assets)} theme files")
            self.themes = []
            
            # Download each zip file
            for i, asset in enumerate(zip_assets):
                self.status.emit(f"Downloading {asset['name']}...")
                
                # Download the file
                download_url = asset['browser_download_url']
                local_path = self.download_dir / asset['name']
                
                response = requests.get(download_url, stream=True, timeout=60)
                response.raise_for_status()
                
                total_size = int(response.headers.get('content-length', 0))
                downloaded = 0
                
                with open(local_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                            downloaded += len(chunk)
                            if total_size > 0:
                                progress = int((downloaded / total_size) * 100)
                                self.progress.emit(progress)
                
                self.themes.append({
                    'name': asset['name'],
                    'path': local_path,
                    'size': asset['size']
                })
                
                self.status.emit(f"Downloaded {asset['name']}")
            
            self.finished.emit(self.themes)
            
        except Exception as e:
            self.error.emit(f"Download error: {str(e)}")

class ThemeInstallWorker(QThread):
    """Worker thread for installing themes"""
    progress = Signal(int)
    status = Signal(str)
    finished = Signal()
    error = Signal(str)
    
    def __init__(self, themes, rockbox_folder):
        super().__init__()
        self.themes = themes
        self.rockbox_folder = rockbox_folder
        
    def run(self):
        try:
            total_themes = len(self.themes)
            
            for i, theme in enumerate(self.themes):
                self.status.emit(f"Installing {theme['name']}...")
                
                # Extract the zip file
                with zipfile.ZipFile(theme['path'], 'r') as zip_ref:
                    # Get list of files in the zip
                    file_list = zip_ref.namelist()
                    
                    # Find .rockbox folder in the zip
                    rockbox_files = [f for f in file_list if f.startswith('.rockbox/')]
                    
                    if not rockbox_files:
                        self.status.emit(f"No .rockbox folder found in {theme['name']}, skipping...")
                        continue
                    
                    # Extract .rockbox contents to the target folder
                    for file_path in rockbox_files:
                        # Skip directories and system files
                        if file_path.endswith('/') or file_path.startswith('._'):
                            continue
                            
                        # Remove .rockbox/ prefix and extract to target folder
                        relative_path = file_path[len('.rockbox/'):]
                        if relative_path:  # Skip if it's just the folder itself
                            target_path = self.rockbox_folder / relative_path
                            target_path.parent.mkdir(parents=True, exist_ok=True)
                            
                            try:
                                # Extract file
                                with zip_ref.open(file_path) as source_file:
                                    with open(target_path, 'wb') as target_file:
                                        target_file.write(source_file.read())
                            except PermissionError as e:
                                # Skip files we can't write due to permissions
                                self.status.emit(f"Skipped {relative_path} (permission denied)")
                                continue
                            except Exception as e:
                                # Skip files that cause other errors
                                self.status.emit(f"Skipped {relative_path} ({str(e)})")
                                continue
                
                progress = int(((i + 1) / total_themes) * 100)
                self.progress.emit(progress)
                self.status.emit(f"Installed {theme['name']}")
            
            # Clean up downloaded files
            for theme in self.themes:
                try:
                    theme['path'].unlink()
                except:
                    pass
            
            self.finished.emit()
            
        except Exception as e:
            self.error.emit(f"Installation error: {str(e)}")

class InnioasisThemeWorker(QThread):
    """Worker thread for downloading and installing Innioasis Y1 themes"""
    progress = Signal(int)
    status = Signal(str)
    finished = Signal()
    error = Signal(str)
    
    def __init__(self, device_folder):
        super().__init__()
        self.device_folder = device_folder
        self.themes_folder = None
    
    def run(self):
        """Download and install Innioasis Y1 themes"""
        try:
            # Determine the themes folder path
            if self.device_folder.name == '.rockbox':
                # If .rockbox folder is selected, go up one level for Themes
                self.themes_folder = self.device_folder.parent / 'Themes'
            else:
                # If device root is selected, create Themes folder there
                self.themes_folder = self.device_folder / 'Themes'
            
            # Create themes folder
            self.themes_folder.mkdir(exist_ok=True)
            
            self.status.emit("Downloading Innioasis Y1 themes...")
            
            # Download the main repository zip
            zip_url = "https://codeload.github.com/team-slide/InnoasisY1Themes/zip/refs/heads/main"
            response = requests.get(zip_url, stream=True)
            response.raise_for_status()
            
            # Save zip file
            zip_path = Path.cwd() / "innioasis_themes.zip"
            with open(zip_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            self.status.emit("Extracting theme folders...")
            
            # Extract all theme folders
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                file_list = zip_ref.namelist()
                
                # Find all theme folders (skip root files)
                theme_folders = set()
                for file_path in file_list:
                    parts = file_path.split('/')
                    if len(parts) > 2 and parts[1]:  # Skip root files and empty folders
                        theme_folders.add(parts[1])
                
                theme_folders = list(theme_folders)
                total_themes = len(theme_folders)
                
                for i, theme_folder in enumerate(theme_folders):
                    self.status.emit(f"Installing {theme_folder}...")
                    
                    # Extract all files for this theme
                    theme_files = [f for f in file_list if f.startswith(f"InnoasisY1Themes-main/{theme_folder}/")]
                    
                    for file_path in theme_files:
                        # Skip directories and system files
                        if file_path.endswith('/') or file_path.startswith('._'):
                            continue
                        
                        # Remove the InnoasisY1Themes-main/ prefix
                        relative_path = file_path[len('InnoasisY1Themes-main/'):]
                        target_path = self.themes_folder / relative_path
                        target_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        try:
                            # Extract file
                            with zip_ref.open(file_path) as source_file:
                                with open(target_path, 'wb') as target_file:
                                    target_file.write(source_file.read())
                        except PermissionError as e:
                            self.status.emit(f"Skipped {relative_path} (permission denied)")
                            continue
                        except Exception as e:
                            self.status.emit(f"Skipped {relative_path} ({str(e)})")
                            continue
                    
                    progress = int(((i + 1) / total_themes) * 100)
                    self.progress.emit(progress)
                    self.status.emit(f"Installed {theme_folder}")
            
            # Clean up zip file
            try:
                zip_path.unlink()
            except:
                pass
            
            self.finished.emit()
            
        except Exception as e:
            self.error.emit(f"Innioasis theme installation error: {str(e)}")

class Rockbox360pThemeDownloader(QMainWindow):
    """Main GUI window for the 360p theme downloader"""
    
    def __init__(self):
        super().__init__()
        self.themes = []
        self.download_worker = None
        self.install_worker = None
        self.rockbox_folder = None
        
        self.init_ui()
        self.setup_theme_detection()
        
    def setup_theme_detection(self):
        """Setup theme change detection for adaptive UI"""
        # No custom styling - let the OS handle it
        pass
        
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("360p Theme Installer")
        self.setGeometry(100, 100, 500, 400)
        self.setFixedSize(500, 400)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        title_label = QLabel("360p Theme Installer")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Instructions
        instructions_label = QLabel("Power on your Y1, connect Via USB and enable USB Storage Mode, then select the device to install all themes")
        instructions_label.setAlignment(Qt.AlignCenter)
        instructions_label.setWordWrap(True)
        instructions_label.setStyleSheet("color: #666; font-style: italic;")
        main_layout.addWidget(instructions_label)
        
        folder_group = QGroupBox("Device Selection")
        folder_layout = QVBoxLayout(folder_group)
        
        self.folder_label = QLabel("No device selected")
        self.folder_label.setAlignment(Qt.AlignCenter)
        folder_layout.addWidget(self.folder_label)
        
        self.select_folder_btn = QPushButton("Select Device")
        self.select_folder_btn.clicked.connect(self.select_rockbox_folder)
        folder_layout.addWidget(self.select_folder_btn)
        
        main_layout.addWidget(folder_group)
        
        install_group = QGroupBox("Theme Installation")
        install_layout = QVBoxLayout(install_group)
        
        # Rockbox themes button
        self.rockbox_btn = QPushButton("Install Rockbox 360p Themes")
        self.rockbox_btn.clicked.connect(self.install_rockbox_themes)
        install_layout.addWidget(self.rockbox_btn)
        
        # Innioasis themes button
        self.innioasis_btn = QPushButton("Install Innioasis Y1 Themes")
        self.innioasis_btn.clicked.connect(self.install_innioasis_themes)
        install_layout.addWidget(self.innioasis_btn)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        install_layout.addWidget(self.progress_bar)
        
        self.status_label = QLabel("Ready to install themes")
        self.status_label.setAlignment(Qt.AlignCenter)
        install_layout.addWidget(self.status_label)
        
        main_layout.addWidget(install_group)
        
        # Credits
        credits_label = QLabel("Special thanks to the Rockbox Y1 community for the 360p themes")
        credits_label.setAlignment(Qt.AlignCenter)
        credits_label.setWordWrap(True)
        main_layout.addWidget(credits_label)
        
        self.update_ui_state()
        
    def select_rockbox_folder(self):
        """Select the .rockbox folder"""
        folder = QFileDialog.getExistingDirectory(
            self, 
            "Select Device",
            "",
            QFileDialog.ShowDirsOnly
        )
        
        if folder:
            folder_path = Path(folder)
            
            # Find the appropriate .rockbox folder
            if folder_path.name == '.rockbox':
                # User selected .rockbox folder directly
                self.rockbox_folder = folder_path
            elif (folder_path / '.rockbox').exists():
                # User selected device root, .rockbox exists
                self.rockbox_folder = folder_path / '.rockbox'
            else:
                # Look for .rockbox in parent directories (in case user selected a subfolder)
                current_path = folder_path
                while current_path != current_path.parent:
                    if (current_path / '.rockbox').exists():
                        self.rockbox_folder = current_path / '.rockbox'
                        break
                    current_path = current_path.parent
                
                if not self.rockbox_folder:
                    # No .rockbox found, ask if user wants to create one
                    reply = QMessageBox.question(
                        self,
                        "Create .rockbox Folder",
                        f"No .rockbox folder found in {folder_path.name} or parent directories.\n\n"
                        "Would you like to create a .rockbox folder here?",
                        QMessageBox.Yes | QMessageBox.No
                    )
                    
                    if reply == QMessageBox.Yes:
                        try:
                            self.rockbox_folder = folder_path / '.rockbox'
                            self.rockbox_folder.mkdir(exist_ok=True)
                        except PermissionError:
                            QMessageBox.warning(
                                self,
                                "Permission Denied",
                                "Cannot create .rockbox folder in this location.\n"
                                "Please select a different folder or run as administrator."
                            )
                            return
                    else:
                        return
            
            # Test write permissions
            try:
                test_file = self.rockbox_folder / '.test_write'
                test_file.write_text('test')
                test_file.unlink()
            except PermissionError:
                QMessageBox.warning(
                    self,
                    "Permission Denied",
                    "Cannot write to this folder.\n"
                    "Please select a folder you have write access to."
                )
                return
            
            self.folder_label.setText(str(self.rockbox_folder))
            self.update_ui_state()
    
    def update_ui_state(self):
        """Update UI state based on current conditions"""
        has_folder = self.rockbox_folder is not None
        is_working = (self.download_worker is not None and self.download_worker.isRunning()) or \
                    (self.install_worker is not None and self.install_worker.isRunning())
        
        self.rockbox_btn.setEnabled(has_folder and not is_working)
        self.innioasis_btn.setEnabled(has_folder and not is_working)
        
        if not has_folder:
            self.status_label.setText("Please select a device first")
        elif is_working:
            self.status_label.setText("Working...")
        else:
            self.status_label.setText("Ready to install themes")
    
    def install_rockbox_themes(self):
        """Install Rockbox 360p themes"""
        if not self.rockbox_folder:
            QMessageBox.warning(self, "No Folder Selected", "Please select a device first.")
            return
        
        # Create download directory
        download_dir = Path.cwd() / "temp_themes"
        download_dir.mkdir(exist_ok=True)
        
        # Start download worker
        self.download_worker = ThemeDownloadWorker(
            "https://github.com/rockbox-y1/rockbox/releases/tag/360p-theme-pack",
            download_dir
        )
        self.download_worker.progress.connect(self.progress_bar.setValue)
        self.download_worker.status.connect(self.status_label.setText)
        self.download_worker.finished.connect(self.on_download_finished)
        self.download_worker.error.connect(self.on_download_error)
        
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.download_worker.start()
        self.update_ui_state()
    
    def install_innioasis_themes(self):
        """Install Innioasis Y1 themes"""
        if not self.rockbox_folder:
            QMessageBox.warning(self, "No Folder Selected", "Please select a device first.")
            return
        
        # Start Innioasis theme worker
        self.install_worker = InnioasisThemeWorker(self.rockbox_folder)
        self.install_worker.progress.connect(self.progress_bar.setValue)
        self.install_worker.status.connect(self.status_label.setText)
        self.install_worker.finished.connect(self.on_innioasis_finished)
        self.install_worker.error.connect(self.on_install_error)
        
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.install_worker.start()
        self.update_ui_state()
    
    def on_download_finished(self, themes):
        """Handle download completion and start installation"""
        self.themes = themes
        
        # Start install worker immediately after download
        self.install_worker = ThemeInstallWorker(self.themes, self.rockbox_folder)
        self.install_worker.progress.connect(self.progress_bar.setValue)
        self.install_worker.status.connect(self.status_label.setText)
        self.install_worker.finished.connect(self.on_install_finished)
        self.install_worker.error.connect(self.on_install_error)
        
        self.install_worker.start()
        self.update_ui_state()
    
    def on_download_error(self, error_msg):
        """Handle download error"""
        self.progress_bar.setVisible(False)
        self.update_ui_state()
        
        QMessageBox.critical(
            self,
            "Download Error",
            f"Failed to download themes:\n{error_msg}"
        )
    
    def on_install_finished(self):
        """Handle installation completion"""
        self.progress_bar.setVisible(False)
        self.themes = []  # Clear themes after installation
        self.update_ui_state()
        
        QTimer.singleShot(100, lambda: QMessageBox.information(
            self,
            "Installation Complete",
            "All themes have been installed to your .rockbox folder!"
        ))
    
    def on_innioasis_finished(self):
        """Handle Innioasis theme installation completion"""
        self.progress_bar.setVisible(False)
        self.update_ui_state()
        
        QTimer.singleShot(100, lambda: QMessageBox.information(
            self,
            "Installation Complete",
            "All Innioasis Y1 themes have been installed to the Themes folder!"
        ))
    
    def on_install_error(self, error_msg):
        """Handle installation error"""
        self.progress_bar.setVisible(False)
        self.update_ui_state()
        
        QTimer.singleShot(100, lambda: QMessageBox.critical(
            self,
            "Installation Error",
            f"Failed to install themes:\n{error_msg}"
        ))

def main():
    """Main function"""
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("Rockbox 360p Theme Downloader")
    app.setApplicationVersion("1.0")
    
    # Create and show main window
    window = Rockbox360pThemeDownloader()
    window.show()
    
    # Run application
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
