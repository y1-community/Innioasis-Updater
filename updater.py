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
        platform_info = CrossPlatformHelper.get_platform_info()
        
        if platform_info['is_windows']:
            # On Windows, try python.exe first, then python3.exe
            python_candidates = ['python.exe', 'python3.exe', 'python']
        else:
            # On macOS/Linux, try python3 first, then python
            python_candidates = ['python3', 'python']
        
        # First try sys.executable
        if sys.executable:
            return sys.executable
        
        # Then try the candidates
        for candidate in python_candidates:
            try:
                result = subprocess.run([candidate, '--version'],
                                        capture_output=True, text=True, timeout=5)
                if result.returncode == 0:
                    return candidate
            except (subprocess.TimeoutExpired, FileNotFoundError):
                continue
        
        # Fallback to sys.executable
        return sys.executable

    @staticmethod
    def get_pip_command():
        """Get the appropriate pip command for the platform"""
        python_exe = CrossPlatformHelper.get_python_executable()
        
        if platform.system().lower() == 'windows':
            # On Windows, use python -m pip
            return [python_exe, '-m', 'pip']
        else:
            # On macOS/Linux, try pip3 first, then pip
            pip_candidates = ['pip3', 'pip']
            for candidate in pip_candidates:
                try:
                    result = subprocess.run([candidate, '--version'],
                                            capture_output=True, text=True, timeout=5)
                    if result.returncode == 0:
                        return [candidate]
                except (subprocess.TimeoutExpired, FileNotFoundError):
                    continue
            
            # Fallback to python -m pip
            return [python_exe, '-m', 'pip']

    @staticmethod
    def get_launch_command(script_path):
        """Get the appropriate launch command for the platform"""
        python_exe = CrossPlatformHelper.get_python_executable()
        platform_info = CrossPlatformHelper.get_platform_info()
        
        if platform_info['is_windows']:
            # On Windows, use python.exe with the script
            return [python_exe, str(script_path)]
        else:
            # On macOS/Linux, try to make the script executable first
            try:
                os.chmod(script_path, 0o755)
            except Exception:
                pass
            
            # Try to run the script directly first
            try:
                result = subprocess.run([str(script_path), '--help'],
                                        capture_output=True, text=True, timeout=5)
                if result.returncode == 0 or result.returncode == 2:  # Help or usage shown
                    return [str(script_path)]
            except (subprocess.TimeoutExpired, FileNotFoundError, PermissionError):
                pass
            
            # Fallback to python with the script
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
            
            self.status_updated.emit("Preparing update...")
            self.progress_updated.emit(10)
            
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
            
            # Find the extracted directory
            extracted_dir = None
            for item in current_dir.iterdir():
                if item.is_dir() and item.name.startswith("Innioasis-Updater-main"):
                    extracted_dir = item
                    break
            
            if not extracted_dir:
                self.update_completed.emit(False, "Could not find extracted directory")
                return
            
            # Install dependencies
            self.install_requirements()
            
            # Copy new files to current directory
            self.status_updated.emit("Installing new files...")
            self.progress_updated.emit(90)
            
            try:
                # Copy all files from extracted directory to current directory
                for item in extracted_dir.iterdir():
                    if item.name not in [".git", "__pycache__", ".DS_Store", "firmware_downloads"]:
                        if item.is_file():
                            shutil.copy2(item, current_dir / item.name)
                        elif item.is_dir():
                            if (current_dir / item.name).exists():
                                shutil.rmtree(current_dir / item.name)
                            shutil.copytree(item, current_dir / item.name)
                
                self.status_updated.emit("Files installed!")
                self.progress_updated.emit(95)
            except Exception as e:
                self.update_completed.emit(False, f"Error installing files: {e}")
                return
            
            # Clean up
            self.status_updated.emit("Cleaning up...")
            self.progress_updated.emit(98)
            
            try:
                if zip_file.exists():
                    zip_file.unlink()
                if extracted_dir.exists():
                    shutil.rmtree(extracted_dir)
                # Write timestamp after successful update
                timestamp_file.write_text(str(time.time()))
            except Exception as e:
                self.status_updated.emit(f"Warning: Could not clean up temporary files: {e}")
            
            self.progress_updated.emit(100)
            self.status_updated.emit("Update completed successfully!")
            self.update_completed.emit(True, "Update successful! Launching firmware_downloader.py...")
            
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
                if chunk:
                    f.write(chunk)
                    downloaded_size += len(chunk)
                    if total_size > 0:
                        progress = int(15 + (downloaded_size / total_size) * 35)  # Progress from 15% to 50%
                        self.progress_updated.emit(progress)
                        self.status_updated.emit(f"Downloading... {int((downloaded_size / total_size) * 100)}%")

    def install_requirements(self):
        """Install requirements.txt if it exists with cross-platform support"""
        requirements_file = Path("requirements.txt")
        if requirements_file.exists():
            self.status_updated.emit("Installing Python dependencies...")
            self.progress_updated.emit(75)
            
            try:
                pip_cmd = CrossPlatformHelper.get_pip_command()
                install_cmd = pip_cmd + ["install", "-r", "requirements.txt"]
                
                self.status_updated.emit(f"Running: {' '.join(install_cmd)}")
                
                # Run pip install with platform-specific handling
                result = subprocess.run(install_cmd,
                                        capture_output=True,
                                        text=True,
                                        timeout=300)  # 5 minute timeout
                
                if result.returncode == 0:
                    self.status_updated.emit("Dependencies installed successfully!")
                else:
                    # Try with --user flag if regular install fails
                    self.status_updated.emit("Retrying with --user flag...")
                    install_cmd_user = pip_cmd + ["install", "--user", "-r", "requirements.txt"]
                    result_user = subprocess.run(install_cmd_user,
                                                 capture_output=True,
                                                 text=True,
                                                 timeout=300)
                    
                    if result_user.returncode == 0:
                        self.status_updated.emit("Dependencies installed successfully (user mode)!")
                    else:
                        self.status_updated.emit(f"Warning: Could not install dependencies: {result_user.stderr}")
                
                self.progress_updated.emit(80)
                
            except subprocess.TimeoutExpired:
                self.status_updated.emit("Warning: Dependency installation timed out")
                self.progress_updated.emit(80)
            except Exception as e:
                self.status_updated.emit(f"Warning: Could not install dependencies: {e}")
                self.progress_updated.emit(80)
        else:
            self.status_updated.emit("No requirements.txt found, skipping dependency installation")
            self.progress_updated.emit(80)


class UpdateProgressDialog(QDialog):
    """Progress dialog for the update process"""
    
    def __init__(self, perform_update=True, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Innioasis Updater")
        self.setModal(True)
        
        # Set up UI
        layout = QVBoxLayout(self)
        
        title_label = QLabel("Innioasis Updater")
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        platform_info = CrossPlatformHelper.get_platform_info()
        platform_label = QLabel(f"Platform: {platform_info['system'].title()} {platform_info['machine']}")
        platform_label.setAlignment(Qt.AlignCenter)
        platform_label.setStyleSheet("color: #666; font-size: 10px;")
        layout.addWidget(platform_label)
        
        self.status_label = QLabel("Initializing...")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setWordWrap(True)
        layout.addWidget(self.status_label)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)
        
        self.log_text = QTextEdit()
        self.log_text.setMaximumHeight(150)
        self.log_text.setReadOnly(True)
        layout.addWidget(self.log_text)
        
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.cancel_update)
        layout.addWidget(self.cancel_button)

        if perform_update:
            self.setFixedSize(500, 300)
            # Set up and start the update worker thread
            self.update_worker = UpdateWorker()
            self.update_worker.progress_updated.connect(self.progress_bar.setValue)
            self.update_worker.status_updated.connect(self.update_status)
            self.update_worker.update_completed.connect(self.on_update_completed)
            self.update_worker.start()
        else:
            # If no update is needed, just show a launch message
            self.setFixedSize(500, 180) # Use a smaller window
            self.update_status("Update not required. Launching application...")
            self.progress_bar.hide()
            self.log_text.hide()
            self.cancel_button.hide()
            # Launch after a short delay so the user sees the message
            QTimer.singleShot(1500, self._launch_and_close)

    def _launch_main_script(self):
        """Finds and launches the main firmware_downloader.py script."""
        firmware_script = Path.cwd() / "firmware_downloader.py"
        if firmware_script.exists():
            try:
                launch_cmd = CrossPlatformHelper.get_launch_command(firmware_script)
                self.update_status(f"Launching: {' '.join(launch_cmd)}")
                subprocess.Popen(launch_cmd)
            except Exception as e:
                self.update_status(f"Error: Could not auto-launch firmware_downloader.py: {e}")
                QMessageBox.critical(self, "Launch Failed", f"Could not launch the main application:\n{e}")
        else:
            self.update_status("Error: firmware_downloader.py not found.")
            QMessageBox.critical(self, "Launch Failed", "Could not find 'firmware_downloader.py'.\nPlease try running the update again using the --force flag.")
            
    def _launch_and_close(self):
        """Helper method to launch the main script and then accept the dialog."""
        self._launch_main_script()
        self.accept()

    def update_status(self, message):
        """Update status message and log"""
        self.status_label.setText(message)
        self.log_text.append(f"[{time.strftime('%H:%M:%S')}] {message}")
        self.log_text.verticalScrollBar().setValue(self.log_text.verticalScrollBar().maximum())
    
    def cancel_update(self):
        """Cancel the update process"""
        reply = QMessageBox.question(
            self,
            "Cancel Update",
            "Are you sure you want to cancel the update? This may leave the application in an inconsistent state.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            if hasattr(self, 'update_worker'):
                self.update_worker.should_stop = True
                self.update_worker.terminate()
                self.update_worker.wait()
            self.reject()
    
    def on_update_completed(self, success, message):
        """Handle update completion"""
        if success:
            self.update_status(message)
            self._launch_main_script()
            # Give a moment for the user to read the final message before closing
            QTimer.singleShot(2000, self.accept)
        else:
            self.update_status(f"Update failed: {message}")
            QMessageBox.critical(self, "Update Failed", 
                                 f"Update failed: {message}\n\nPlease check the error messages above.")
            self.reject()


def main():
    """Main function to check for updates and launch the GUI."""
    parser = argparse.ArgumentParser(description="Innioasis Updater Script")
    parser.add_argument("-f", "--force", action="store_true", help="Force the update, ignoring the 24-hour check.")
    args = parser.parse_args()

    current_dir = Path.cwd()
    timestamp_file = current_dir / ".last_update_check"
    needs_update = False

    if args.force:
        needs_update = True
    else:
        twenty_four_hours_in_seconds = 24 * 60 * 60
        if timestamp_file.exists():
            try:
                last_check_time = float(timestamp_file.read_text())
                if time.time() - last_check_time >= twenty_four_hours_in_seconds:
                    needs_update = True
                # If it's false, we do nothing and proceed to launch with needs_update=False
            except (ValueError, IOError):
                # Corrupted file, treat as needing an update.
                needs_update = True
        else:
            # No timestamp file means this is the first run or it was deleted.
            needs_update = True

    # Always start the GUI application.
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    # Pass the 'needs_update' flag to the dialog to control its behavior.
    dialog = UpdateProgressDialog(perform_update=needs_update)
    result = dialog.exec_()
    
    sys.exit(0 if result == QDialog.Accepted else 1)


if __name__ == "__main__":
    main()
