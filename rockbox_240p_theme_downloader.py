#!/usr/bin/env python3
"""
Rockbox 240p Theme Downloader for Y1
Downloads 240p themes zip from team-slide/rockbox-240p-iPod-themes and installs to .rockbox folder
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
    """Worker thread for downloading the 240p themes zip"""
    progress = Signal(int)
    status = Signal(str)
    finished = Signal(str)
    error = Signal(str)
    
    def __init__(self, download_dir):
        super().__init__()
        self.download_dir = download_dir
        
    def run(self):
        try:
            self.status.emit("Fetching latest release information...")
            
            # Get latest release information from GitHub API
            api_url = "https://api.github.com/repos/team-slide/rockbox-240p-iPod-themes/releases/latest"
            
            response = requests.get(api_url, timeout=30)
            response.raise_for_status()
            release_data = response.json()
            
            # Find the 240pthemes.zip file in the release assets
            zip_assets = [asset for asset in release_data.get('assets', []) 
                         if asset['name'] == '240pthemes.zip']
            
            if not zip_assets:
                self.error.emit("240pthemes.zip not found in latest release")
                return
                
            asset = zip_assets[0]
            self.status.emit(f"Found 240pthemes.zip ({asset['size']} bytes)")
            
            # Download the zip file
            self.status.emit("Downloading 240pthemes.zip...")
            
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
            
            self.status.emit("Download completed")
            self.finished.emit(str(local_path))
            
        except Exception as e:
            self.error.emit(f"Download error: {str(e)}")

class ThemeInstallWorker(QThread):
    """Worker thread for installing themes"""
    progress = Signal(int)
    status = Signal(str)
    finished = Signal()
    error = Signal(str)
    
    def __init__(self, zip_path, rockbox_folder):
        super().__init__()
        self.zip_path = zip_path
        self.rockbox_folder = rockbox_folder
        
    def run(self):
        try:
            self.status.emit("Extracting themes from 240pthemes.zip...")
            
            # Extract the zip file
            with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
                # Get list of files in the zip
                file_list = zip_ref.namelist()
                
                # Check if zip contains .rockbox folder or files directly
                rockbox_files = [f for f in file_list if f.startswith('.rockbox/')]
                
                if rockbox_files:
                    # Zip contains .rockbox folder - extract its contents
                    self.status.emit("Found .rockbox folder in zip, extracting contents...")
                    total_files = len([f for f in rockbox_files if not f.endswith('/') and not f.startswith('._')])
                    self.status.emit(f"Found {total_files} files to extract")
                    
                    extracted_count = 0
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
                                extracted_count += 1
                            except PermissionError as e:
                                # Skip files we can't write due to permissions
                                self.status.emit(f"Skipped {relative_path} (permission denied)")
                                continue
                            except Exception as e:
                                # Skip files that cause other errors
                                self.status.emit(f"Skipped {relative_path} ({str(e)})")
                                continue
                            
                            # Update progress
                            progress = int((extracted_count / total_files) * 100) if total_files > 0 else 0
                            self.progress.emit(progress)
                            self.status.emit(f"Extracted {relative_path}")
                else:
                    # Zip contains files directly - extract them to .rockbox folder
                    self.status.emit("Extracting files directly to .rockbox folder...")
                    total_files = len([f for f in file_list if not f.endswith('/') and not f.startswith('._')])
                    self.status.emit(f"Found {total_files} files to extract")
                    
                    extracted_count = 0
                    for file_path in file_list:
                        # Skip directories and system files
                        if file_path.endswith('/') or file_path.startswith('._'):
                            continue
                            
                        # Place file directly in the .rockbox folder
                        target_path = self.rockbox_folder / file_path
                        target_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        try:
                            # Extract file
                            with zip_ref.open(file_path) as source_file:
                                with open(target_path, 'wb') as target_file:
                                    target_file.write(source_file.read())
                            extracted_count += 1
                        except PermissionError as e:
                            # Skip files we can't write due to permissions
                            self.status.emit(f"Skipped {file_path} (permission denied)")
                            continue
                        except Exception as e:
                            # Skip files that cause other errors
                            self.status.emit(f"Skipped {file_path} ({str(e)})")
                            continue
                        
                        # Update progress
                        progress = int((extracted_count / total_files) * 100) if total_files > 0 else 0
                        self.progress.emit(progress)
                        self.status.emit(f"Extracted {file_path}")
            
            # Clean up downloaded zip file
            try:
                Path(self.zip_path).unlink()
            except:
                pass
            
            self.status.emit("Installation completed")
            self.finished.emit()
            
        except Exception as e:
            self.error.emit(f"Installation error: {str(e)}")

class Rockbox240pThemeDownloader(QMainWindow):
    """Main GUI window for the 240p theme downloader"""
    
    def __init__(self):
        super().__init__()
        self.download_worker = None
        self.install_worker = None
        self.rockbox_folder = None
        self.zip_path = None
        
        self.init_ui()
        self.setup_theme_detection()
        
    def setup_theme_detection(self):
        """Setup theme change detection for adaptive UI"""
        # No custom styling - let the OS handle it
        pass
        
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("240p Themes for Y1")
        self.setGeometry(100, 100, 500, 400)
        self.setFixedSize(500, 400)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # Header
        title_label = QLabel("240p Themes for Y1")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Instructions
        instructions_label = QLabel("Power on your Y1, connect Via USB and enable USB Storage Mode, then select the device to install all themes")
        instructions_label.setAlignment(Qt.AlignCenter)
        instructions_label.setWordWrap(True)
        instructions_label.setStyleSheet("color: #666; font-style: italic;")
        main_layout.addWidget(instructions_label)
        
        # Folder selection
        folder_group = QGroupBox("Device Selection")
        folder_layout = QVBoxLayout(folder_group)
        
        self.folder_label = QLabel("No device selected")
        self.folder_label.setAlignment(Qt.AlignCenter)
        folder_layout.addWidget(self.folder_label)
        
        self.select_folder_btn = QPushButton("Select Device or .rockbox Folder")
        self.select_folder_btn.clicked.connect(self.select_rockbox_folder)
        folder_layout.addWidget(self.select_folder_btn)
        
        main_layout.addWidget(folder_group)
        
        # Download section
        download_group = QGroupBox("Download & Install")
        download_layout = QVBoxLayout(download_group)
        
        self.download_btn = QPushButton("Download & Install Themes")
        self.download_btn.clicked.connect(self.download_and_install)
        download_layout.addWidget(self.download_btn)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        download_layout.addWidget(self.progress_bar)
        
        # Status label
        self.status_label = QLabel("Ready to download and install themes")
        self.status_label.setAlignment(Qt.AlignCenter)
        download_layout.addWidget(self.status_label)
        
        main_layout.addWidget(download_group)
        
        # Credits
        credits_label = QLabel("Special thanks to @BolfGall for collecting all the Y1 240p themes")
        credits_label.setAlignment(Qt.AlignCenter)
        credits_label.setWordWrap(True)
        main_layout.addWidget(credits_label)
        
        # Set initial state
        self.update_ui_state()
        
    def select_rockbox_folder(self):
        """Select the .rockbox folder"""
        folder = QFileDialog.getExistingDirectory(
            self, 
            "Select your Y1 device or .rockbox folder",
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
        is_downloading = self.download_worker is not None and self.download_worker.isRunning()
        is_installing = self.install_worker is not None and self.install_worker.isRunning()
        
        self.download_btn.setEnabled(has_folder and not is_downloading and not is_installing)
        
        if not has_folder:
            self.status_label.setText("Please select a device first")
        elif is_downloading:
            self.status_label.setText("Downloading themes...")
        elif is_installing:
            self.status_label.setText("Installing themes...")
        else:
            self.status_label.setText("Ready to download and install themes")
    
    def download_and_install(self):
        """Start downloading and installing themes"""
        if not self.rockbox_folder:
            QMessageBox.warning(self, "Choose your device", "Please select your Y1 device or .rockbox folder first.")
            return
        
        # Create download directory
        download_dir = Path.cwd() / "temp_themes"
        download_dir.mkdir(exist_ok=True)
        
        # Start download worker
        self.download_worker = ThemeDownloadWorker(download_dir)
        self.download_worker.progress.connect(self.progress_bar.setValue)
        self.download_worker.status.connect(self.status_label.setText)
        self.download_worker.finished.connect(self.on_download_finished)
        self.download_worker.error.connect(self.on_download_error)
        
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.download_worker.start()
        self.update_ui_state()
    
    def on_download_finished(self, zip_path):
        """Handle download completion"""
        self.zip_path = zip_path
        
        # Start installation immediately
        self.install_worker = ThemeInstallWorker(zip_path, self.rockbox_folder)
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
        
        # Use a timer to ensure any previous dialogs are closed
        QTimer.singleShot(100, lambda: QMessageBox.critical(
            self,
            "Download failed",
            f"We couldn't get your themes:\n{error_msg}\n\nPlease check your internet connection and try again."
        ))
    
    def on_install_finished(self):
        """Handle installation completion"""
        self.progress_bar.setVisible(False)
        self.update_ui_state()
        
        # Use a timer to ensure any previous dialogs are closed
        QTimer.singleShot(100, lambda: QMessageBox.information(
            self,
            "All done! 🎉",
            "Your themes are now installed and ready to use on your Y1!"
        ))
    
    def on_install_error(self, error_msg):
        """Handle installation error"""
        self.progress_bar.setVisible(False)
        self.update_ui_state()
        
        # Use a timer to ensure any previous dialogs are closed
        QTimer.singleShot(100, lambda: QMessageBox.critical(
            self,
            "Oops, something went wrong",
            f"We couldn't install your themes:\n{error_msg}\n\nPlease try again or check your device connection."
        ))

def main():
    """Main function"""
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("Rockbox 240p Theme Downloader")
    app.setApplicationVersion("1.0")
    
    # Create and show main window
    window = Rockbox240pThemeDownloader()
    window.show()
    
    # Run application
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
