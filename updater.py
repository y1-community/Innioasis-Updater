#!/usr/bin/env python3
"""
Innioasis Updater Script
Downloads and installs the latest version of the Innioasis Updater
Cross-platform support for Windows, macOS, and Linux
"""

import os
import sys
import zipfile
import subprocess
import requests
from pathlib import Path
import shutil
import time
import threading
import platform
import argparse
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
                               QWidget, QLabel, QProgressBar, QPushButton, QTextEdit,
                               QMessageBox, QDialog)
from PySide6.QtCore import QThread, Signal, Qt, QTimer
from PySide6.QtGui import QFont

class CrossPlatformHelper:
    """Helper class for cross-platform operations"""

    @staticmethod
    def get_platform_info():
        """Get platform information"""
        system = platform.system().lower()
        machine = platform.machine().lower()
        return {
            'system': system,
            'machine': machine,
            'is_windows': system == 'windows',
            'is_macos': system == 'darwin',
            'is_linux': system == 'linux',
            'is_64bit': machine in ['x86_64', 'amd64', 'arm64']
        }

    @staticmethod
    def get_python_executable():
        """Get the appropriate Python executable for the platform"""
        if sys.executable:
            return sys.executable
        
        python_candidates = ['python3', 'python']
        if CrossPlatformHelper.get_platform_info()['is_windows']:
            python_candidates = ['python.exe', 'python3.exe', 'python']
        
        for candidate in python_candidates:
            try:
                result = subprocess.run([candidate, '--version'],
                                        capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    return candidate
            except (subprocess.TimeoutExpired, FileNotFoundError):
                continue
        
        return "python" # Fallback

    @staticmethod
    def get_pip_command():
        """Get the appropriate pip command for the platform"""
        python_exe = CrossPlatformHelper.get_python_executable()
        return [python_exe, '-m', 'pip']

    @staticmethod
    def get_launch_command(script_path):
        """Get the appropriate launch command for the platform"""
        python_exe = CrossPlatformHelper.get_python_executable()
        return [python_exe, str(script_path)]


class UpdateWorker(QThread):
    """Worker thread for handling the update process"""
    
    progress_updated = Signal(int)
    status_updated = Signal(str)
    update_completed = Signal(bool, str)
    
    def __init__(self):
        super().__init__()
        self.should_stop = False
        self.platform_info = CrossPlatformHelper.get_platform_info()
        
    def run(self):
        try:
            current_dir = Path.cwd()
            timestamp_file = current_dir / ".last_update_check"
            
            self.status_updated.emit(f"Starting update process on {self.platform_info['system'].title()}...")
            self.progress_updated.emit(5)
            
            # Download latest version from GitHub
            github_url = "https://github.com/team-slide/Innioasis-Updater/archive/refs/heads/main.zip"
            zip_file = current_dir / "innioasis_updater_latest.zip"
            
            self.status_updated.emit("Downloading latest version from GitHub...")
            self.progress_updated.emit(15)
            
            try:
                self.download_with_progress(github_url, zip_file)
                self.status_updated.emit("Download completed!")
                self.progress_updated.emit(50)
            except Exception as e:
                self.update_completed.emit(False, f"Error downloading update: {e}")
                return
            
            # Extract the zip file
            self.status_updated.emit("Extracting files...")
            self.progress_updated.emit(55)
            
            try:
                with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                    zip_ref.extractall(current_dir)
                self.status_updated.emit("Files extracted!")
                self.progress_updated.emit(70)
            except Exception as e:
                self.update_completed.emit(False, f"Error extracting files: {e}")
                return
            
            extracted_dir = next(current_dir.glob("Innioasis-Updater-main*"), None)
            if not extracted_dir:
                self.update_completed.emit(False, "Could not find extracted directory")
                return
            
            # Install dependencies
            self.install_requirements(extracted_dir)
            
            # Copy new files to current directory
            self.status_updated.emit("Installing new files...")
            self.progress_updated.emit(90)
            
            try:
                self.copy_files_with_error_handling(extracted_dir, current_dir)
                self.status_updated.emit("Files installed!")
                self.progress_updated.emit(95)
            except Exception as e:
                self.update_completed.emit(False, f"Error installing files: {e}")
                return
            
            # Clean up
            self.status_updated.emit("Cleaning up...")
            self.progress_updated.emit(98)
            
            try:
                zip_file.unlink(missing_ok=True)
                shutil.rmtree(extracted_dir)
                timestamp_file.write_text(str(time.time()))
            except Exception as e:
                self.status_updated.emit(f"Warning: Could not clean up temporary files: {e}")
            
            self.progress_updated.emit(100)
            self.status_updated.emit("Update completed successfully!")
            self.update_completed.emit(True, "Update successful!")
            
        except Exception as e:
            self.update_completed.emit(False, f"Unexpected error: {e}")

    def download_with_progress(self, url, filepath):
        """Download file with progress display"""
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded_size = 0
        
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if self.should_stop: return
                if chunk:
                    f.write(chunk)
                    downloaded_size += len(chunk)
                    if total_size > 0:
                        progress = int(15 + (downloaded_size / total_size) * 35)
                        self.progress_updated.emit(progress)
                        self.status_updated.emit(f"Downloading... {int((downloaded_size / total_size) * 100)}%")

    def copy_files_with_error_handling(self, source_dir, dest_dir):
        """Copy files with error handling for write blocking errors - attempts all files including DLL/EXE"""
        error_files = []
        
        for item in source_dir.iterdir():
            if item.name in [".git", "__pycache__", ".DS_Store", "firmware_downloads"]:
                continue
                
            dest_item = dest_dir / item.name
            
            try:
                if item.is_file():
                    shutil.copy2(item, dest_item)
                elif item.is_dir():
                    if dest_item.exists():
                        shutil.rmtree(dest_item)
                    shutil.copytree(item, dest_item)
            except PermissionError as e:
                # Handle write blocking errors (files in use) - common with DLL/EXE files
                if "being used by another process" in str(e) or "access is denied" in str(e):
                    error_files.append(f"{item.name} (in use)")
                    # Don't show individual warnings - just log silently
                    continue
                else:
                    raise e
            except OSError as e:
                # Handle other OS errors (like read-only files)
                if "read-only" in str(e).lower() or "access denied" in str(e).lower():
                    error_files.append(f"{item.name} (access denied)")
                    # Don't show individual warnings - just log silently
                    continue
                else:
                    raise e
        
        # Only show summary if there were significant errors, don't bother user with individual file issues
        if error_files:
            self.status_updated.emit(f"Note: {len(error_files)} files couldn't be updated (likely in use) - will update on next run")
            self.status_updated.emit("Update proceeding successfully - blocked files will be updated later")

    def install_requirements(self, source_dir):
        """Install requirements.txt from the source directory."""
        requirements_file = source_dir / "requirements.txt"
        if requirements_file.exists():
            self.status_updated.emit("Installing Python dependencies...")
            self.progress_updated.emit(75)
            
            try:
                pip_cmd = CrossPlatformHelper.get_pip_command()
                install_cmd = pip_cmd + ["install", "-r", str(requirements_file)]
                
                self.status_updated.emit(f"Running: {' '.join(install_cmd)}")
                
                result = subprocess.run(install_cmd, capture_output=True, text=True, timeout=300)
                
                if result.returncode == 0:
                    self.status_updated.emit("Dependencies installed successfully!")
                else:
                    self.status_updated.emit(f"Warning: Could not install dependencies: {result.stderr}")
                
                self.progress_updated.emit(80)
                
            except Exception as e:
                self.status_updated.emit(f"Warning: Could not install dependencies: {e}")
                self.progress_updated.emit(80)
        else:
            self.status_updated.emit("No requirements.txt found, skipping.")
            self.progress_updated.emit(80)


class UpdateProgressDialog(QDialog):
    """Progress dialog for the update process"""
    
    def __init__(self, perform_update=True, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Innioasis Updater")
        self.setModal(True)
        
        layout = QVBoxLayout(self)
        
        title_label = QLabel("Innioasis Updater")
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        self.status_label = QLabel("Initializing...")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setWordWrap(True)
        layout.addWidget(self.status_label)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        layout.addWidget(self.progress_bar)
        
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        layout.addWidget(self.log_text)
        
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.cancel_update)
        layout.addWidget(self.cancel_button)

        if perform_update:
            self.setFixedSize(500, 300)
            self.update_worker = UpdateWorker()
            self.update_worker.progress_updated.connect(self.progress_bar.setValue)
            self.update_worker.status_updated.connect(self.update_status)
            self.update_worker.update_completed.connect(self.on_update_completed)
            self.update_worker.start()
        else:
            self.setFixedSize(500, 180)
            self.update_status("Update not required. Launching application...")
            self.progress_bar.hide()
            self.log_text.hide()
            self.cancel_button.hide()
            QTimer.singleShot(1500, self.accept)

    def update_status(self, message):
        """Update status message and log"""
        self.status_label.setText(message)
        self.log_text.append(f"[{time.strftime('%H:%M:%S')}] {message}")
        self.log_text.verticalScrollBar().setValue(self.log_text.verticalScrollBar().maximum())
    
    def cancel_update(self):
        """Cancel the update process"""
        if QMessageBox.question(self, "Cancel Update", "Are you sure you want to cancel?",
                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No) == QMessageBox.Yes:
            if hasattr(self, 'update_worker'):
                self.update_worker.should_stop = True
                self.update_worker.terminate()
                self.update_worker.wait()
            self.reject()
    
    def on_update_completed(self, success, message):
        """Handle update completion"""
        self.update_status(message)
        if success:
            QTimer.singleShot(2000, self.accept)
        else:
            QMessageBox.critical(self, "Update Failed", f"Update failed: {message}")
            self.reject()


def launch_firmware_downloader():
    """Finds and launches the main firmware_downloader.py script."""
    firmware_script = Path.cwd() / "firmware_downloader.py"
    if firmware_script.exists():
        try:
            launch_cmd = CrossPlatformHelper.get_launch_command(firmware_script)
            print(f"Launching: {' '.join(launch_cmd)}")
            subprocess.Popen(launch_cmd)
            return True
        except Exception as e:
            QMessageBox.critical(None, "Launch Failed", f"Could not launch the main application:\n{e}")
    else:
        QMessageBox.critical(None, "Launch Failed", "Could not find 'firmware_downloader.py'.")
    return False


def main():
    """Main function to check for updates and launch the GUI."""
    parser = argparse.ArgumentParser(description="Innioasis Updater Script")
    parser.add_argument("-f", "--force", action="store_true", help="Force the update.")
    args = parser.parse_args()

    timestamp_file = Path.cwd() / ".last_update_check"
    needs_update = False

    if args.force:
        needs_update = True
    else:
        if not timestamp_file.exists() or (time.time() - float(timestamp_file.read_text()) >= 24 * 3600):
            needs_update = True

    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    dialog = UpdateProgressDialog(perform_update=needs_update)
    result = dialog.exec()
    
    # **REFACTORED LOGIC:** Only launch after the dialog has successfully closed.
    if result == QDialog.Accepted:
        launch_firmware_downloader()
        sys.exit(0)
    else:
        # User cancelled or an error occurred.
        sys.exit(1)


if __name__ == "__main__":
    main()
