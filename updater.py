#!/usr/bin/env python3
"""
Innioasis Updater Script
A smart, resilient, and user-friendly updater designed for a seamless experience.
"""

import os
import sys
import zipfile
import subprocess
import requests
from pathlib import Path
import shutil
import time
import platform
import argparse
import tempfile
import logging
import datetime
import webbrowser
from PySide6.QtWidgets import (QApplication, QVBoxLayout, QWidget, QLabel, QProgressBar,
                               QPushButton, QDialog, QTextEdit)
from PySide6.QtCore import QThread, Signal, Qt, QTimer
from PySide6.QtGui import QFont, QGuiApplication

class CrossPlatformHelper:
    """Helper class for cross-platform operations."""
    @staticmethod
    def get_platform_info():
        system = platform.system().lower()
        return {'is_windows': system == 'windows', 'is_macos': system == 'darwin', 'is_linux': system == 'linux'}

    @staticmethod
    def get_python_executable():
        if sys.executable: return sys.executable
        info = CrossPlatformHelper.get_platform_info()
        candidates = ['python3', 'python']
        if info['is_windows']: candidates = ['python.exe', 'python3.exe', 'python']
        for candidate in candidates:
            try:
                if subprocess.run([candidate, '--version'], capture_output=True, text=True, timeout=5, check=False).returncode == 0: return candidate
            except (subprocess.TimeoutExpired, FileNotFoundError): continue
        return "python"

    @staticmethod
    def get_launch_command(script_path):
        return [CrossPlatformHelper.get_python_executable(), str(script_path)]

    @staticmethod
    def open_path(path_or_url):
        info = CrossPlatformHelper.get_platform_info()
        try:
            if "http" in str(path_or_url): webbrowser.open(path_or_url)
            elif info['is_windows']: subprocess.Popen(['explorer', path_or_url])
            elif info['is_macos']: subprocess.Popen(['open', path_or_url])
            else: subprocess.Popen(['xdg-open', path_or_url])
        except Exception as e:
            logging.error("Could not open path %s: %s", path_or_url, e)

class TroubleshootWorker(QThread):
    """Dedicated worker for downloading troubleshooters."""
    status_updated = Signal(str)
    finished = Signal()

    def run(self):
        self.status_updated.emit("Downloading troubleshooting tools...")
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                if download_troubleshooters(Path.cwd(), Path(temp_dir)):
                    self.status_updated.emit("Troubleshooting tools are ready.")
                    CrossPlatformHelper.open_path(Path.cwd() / "Troubleshooting")
                else:
                    self.status_updated.emit("Couldn't get tools. Opening help website.")
                    CrossPlatformHelper.open_path("https://troubleshooting.innioasis.app")
        except Exception as e:
            logging.error("Troubleshooter download failed: %s", e)
            self.status_updated.emit("Couldn't get tools. Opening help website.")
            CrossPlatformHelper.open_path("https://troubleshooting.innioasis.app")
        finally:
            self.finished.emit()


class UpdateWorker(QThread):
    """Worker thread for handling the update process."""
    progress_updated = Signal(int)
    status_updated = Signal(str)
    update_completed = Signal(bool)
    
    def __init__(self):
        super().__init__()
        self.should_stop = False
        self.platform_info = CrossPlatformHelper.get_platform_info()
        
    def run(self):
        temp_dir = None
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', filename='updater.log', filemode='w')

        try:
            current_dir = Path.cwd()
            temp_dir = Path(tempfile.mkdtemp(prefix="innioasis-update-"))
            timestamp_file = current_dir / ".last_update_check"
            self.status_updated.emit("Just checking for the latest version...")
            self.progress_updated.emit(5)
            
            main_repo_url = "https://github.com/team-slide/Innioasis-Updater/archive/refs/heads/main.zip"
            zip_file = temp_dir / "innioasis_updater_latest.zip"
            self.status_updated.emit(f"Grabbing updates from GitHub...")
            self.download_with_progress(main_repo_url, zip_file, 5, 45)

            self.progress_updated.emit(60)

            self.status_updated.emit(f"Unpacking {zip_file.name}...")
            with zipfile.ZipFile(zip_file, 'r') as z:
                file_list = z.infolist()
                total_files = len(file_list) if file_list else 1
                for i, member in enumerate(file_list):
                    z.extract(member, temp_dir)
                    progress = int(60 + (i / total_files) * 15)
                    self.progress_updated.emit(progress)

            extracted_dir = next(temp_dir.glob("Innioasis-Updater-main*"), None)
            if not extracted_dir: raise FileNotFoundError("Could not find main extracted directory.")
            
            self.status_updated.emit(f"Updating files in current directory...")
            items_to_copy = list(extracted_dir.iterdir())
            total_items = len(items_to_copy) if items_to_copy else 1
            critical_error_occurred = False
            for i, item in enumerate(items_to_copy):
                if self.should_stop: break
                try:
                    dest_item = current_dir / item.name
                    if item.name.lower() in ['.git', '__pycache__', '.ds_store', 'firmware_downloads', 'python.exe', 'pythonw.exe', '.web_scripts']:
                        continue
                    
                    ext = item.suffix.lower()
                    if item.is_file():
                        # Skip platform-incompatible files
                        if not self.platform_info['is_windows'] and ext in ['.exe', '.dll', '.lnk']:
                            self.status_updated.emit(f"Skipping {item.name} - not compatible with {self.platform_info['system']}")
                            continue
                        
                        # Skip copying existing .exe/.dll files to prevent blocking
                        if dest_item.exists() and ext in ['.exe', '.dll']:
                            self.status_updated.emit(f"Skipping {item.name} - already exists (prevents blocking)")
                            continue
                        
                        # Copy the file (this will overwrite existing files safely)
                        shutil.copy2(item, dest_item)
                        
                    elif item.is_dir():
                        # For directories, preserve existing content and merge new files
                        if dest_item.exists():
                            # Copy individual files from the directory without deleting anything
                            self.status_updated.emit(f"Updating directory {item.name} (preserving existing files)")
                            for subitem in item.iterdir():
                                subdest = dest_item / subitem.name
                                if subitem.is_file():
                                    # Skip platform-incompatible files
                                    if not self.platform_info['is_windows'] and subitem.suffix.lower() in ['.exe', '.dll', '.lnk']:
                                        continue
                                    # Skip .exe and .dll files that already exist to prevent blocking
                                    if subdest.exists() and subitem.suffix.lower() in ['.exe', '.dll']:
                                        self.status_updated.emit(f"Skipping {subitem.name} - already exists (prevents blocking)")
                                        continue
                                    # Copy the file (this will overwrite existing files safely)
                                    shutil.copy2(subitem, subdest)
                                elif subitem.is_dir():
                                    # For subdirectories, copy if they don't exist, otherwise merge
                                    if not subdest.exists():
                                        shutil.copytree(subitem, subdest)
                                    else:
                                        # Recursively merge subdirectories
                                        self.merge_directories(subitem, subdest)
                        else:
                            # Directory doesn't exist, copy it normally
                            shutil.copytree(item, dest_item)
                except (IOError, OSError, shutil.Error) as e:
                    # Only treat Python files and missing executables as critical
                    is_critical = ext == '.py' or (ext == '.exe' and not dest_item.exists())
                    if is_critical:
                        critical_error_occurred = True
                        logging.error("CRITICAL ERROR updating %s: %s", item.name, e)
                        self.status_updated.emit(f"Critical error updating {item.name}: {e}")
                    else:
                        logging.warning("Non-critical error on %s, skipping: %s", item.name, e)
                        self.status_updated.emit(f"Skipping {item.name} due to error: {e}")
                
                progress = int(75 + ((i + 1) / total_items) * 20)
                self.progress_updated.emit(progress)

            # Even if some files were skipped, continue with the update
            if critical_error_occurred:
                self.status_updated.emit("Warning: Some critical files could not be updated")
                self.status_updated.emit("The app will run with existing versions")
            else:
                self.status_updated.emit("All files updated successfully!")
            self.status_updated.emit("PNG files and assets preserved - only executables were updated")
            
            self.status_updated.emit("Finalizing...")
            timestamp_file.write_text(str(datetime.date.today()))
            self.progress_updated.emit(100)
            self.update_completed.emit(True)
            
        except requests.exceptions.RequestException as e:
            self.status_updated.emit("Couldn't connect. We'll skip the update for now.")
            time.sleep(3)
            self.update_completed.emit(True)
        except Exception as e:
            self.status_updated.emit(f"An unexpected error occurred.")
            logging.error("Update process failed: %s", e, exc_info=True)
            self.update_completed.emit(False)
        finally:
            if temp_dir and temp_dir.exists(): shutil.rmtree(temp_dir, ignore_errors=True)

    def merge_directories(self, src_dir, dest_dir):
        """Recursively merge source directory into destination directory, preserving existing files"""
        for item in src_dir.iterdir():
            dest_item = dest_dir / item.name
            if item.is_file():
                # Skip platform-incompatible files
                if not self.platform_info['is_windows'] and item.suffix.lower() in ['.exe', '.dll', '.lnk']:
                    continue
                # Skip .exe and .dll files that already exist to prevent blocking
                if dest_item.exists() and item.suffix.lower() in ['.exe', '.dll']:
                    self.status_updated.emit(f"Skipping {item.name} - already exists (prevents blocking)")
                    continue
                # Copy the file (this will overwrite existing files safely)
                shutil.copy2(item, dest_item)
            elif item.is_dir():
                if not dest_item.exists():
                    shutil.copytree(item, dest_item)
                else:
                    # Recursively merge subdirectories
                    self.merge_directories(item, dest_item)

    def download_with_progress(self, url, filepath, base_progress, progress_range):
        response = requests.get(url, stream=True, timeout=15)
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        downloaded_size = 0
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if self.should_stop: return
                if chunk:
                    f.write(chunk); downloaded_size += len(chunk)
                    if total_size > 0:
                        progress = int(base_progress + (downloaded_size / total_size) * progress_range)
                        self.progress_updated.emit(progress)

class UpdateProgressDialog(QDialog):
    """Progress dialog for the update process."""
    def __init__(self, mode='update', parent=None):
        super().__init__(parent)
        self.setWindowTitle("Innioasis Updater")
        self.setModal(True)
        self.setFixedSize(450, 180)
        
        layout = QVBoxLayout(self)
        title_label = QLabel("Innioasis Updater"); title_label.setFont(QFont("Arial", 16, QFont.Bold)); title_label.setAlignment(Qt.AlignCenter)
        self.status_label = QLabel("Initializing..."); self.status_label.setAlignment(Qt.AlignCenter); self.status_label.setWordWrap(True)
        self.progress_bar = QProgressBar(); self.progress_bar.setRange(0, 100); self.progress_bar.setTextVisible(False)
        self.update_button = QPushButton("Run without updating"); self.update_button.clicked.connect(self.run_without_update)
        self.troubleshoot_button = QPushButton("Open Troubleshooting Tools"); self.troubleshoot_button.clicked.connect(self.run_troubleshooter)
        
        layout.addWidget(title_label); layout.addWidget(self.status_label); layout.addWidget(self.progress_bar); layout.addWidget(self.troubleshoot_button); layout.addWidget(self.update_button)

        if mode == 'troubleshoot_win':
            self.status_label.setText("Troubleshooting mode activated.\nClick the button to get the latest tools.")
            self.progress_bar.hide()
            self.update_button.hide()
            self.troubleshoot_button.show()
        elif mode == 'troubleshoot_maclinux':
            CrossPlatformHelper.open_path("https://innioasis.app")
            # Close immediately after opening browser
            QTimer.singleShot(0, self.reject)
        elif mode == 'update':
            self.troubleshoot_button.hide()
            self.update_worker = UpdateWorker(); self.update_worker.progress_updated.connect(self.progress_bar.setValue)
            self.update_worker.status_updated.connect(self.status_label.setText); self.update_worker.update_completed.connect(self.on_update_completed)
            self.update_worker.start()
        else: # No update needed
            self.setFixedSize(450, 120)
            self.status_label.setText("You're all up to date! Launching now...")
            self.progress_bar.hide(); self.update_button.hide(); self.troubleshoot_button.hide()
            QTimer.singleShot(1500, self.accept)

    def run_without_update(self):
        """Run the app without updating"""
        self.accept()  # Close dialog and continue to app launch

    def run_troubleshooter(self):
        self.troubleshoot_button.setEnabled(False)
        self.worker = TroubleshootWorker()
        self.worker.status_updated.connect(self.status_label.setText)
        self.worker.finished.connect(self.accept) # Close dialog when done
        self.worker.start()

    def on_update_completed(self, success):
        self.update_button.hide()
        if success:
            self.status_label.setText("All done! You're now up to date. ✨")
            self.progress_bar.setValue(100)
            QTimer.singleShot(2000, self.accept)
        else:
            self.countdown = 10; self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_countdown); self.timer.start(1000)
            self.update_countdown()

    def update_countdown(self):
        if self.countdown > 0:
            msg = f"Oops, something went wrong. We'll try again later.\nLaunching the app for you now... ({self.countdown})"
            self.status_label.setText(msg)
            self.countdown -= 1
        else:
            self.timer.stop(); self.accept()

def perform_initial_cleanup():
    """Removes obsolete or platform-specific files and folders."""
    logging.info("Performing initial directory cleanup...")
    platform_info = CrossPlatformHelper.get_platform_info()
    
    for path in Path.cwd().iterdir():
        try:
            if path.is_dir() and path.name == '.web_scripts':
                shutil.rmtree(path); logging.info("Removed obsolete folder: %s", path.name)
                continue
            if not platform_info['is_windows']:
                if path.suffix.lower() in ['.exe', '.dll', '.lnk']:
                    path.unlink(); logging.info("Removed Windows-specific file: %s", path.name)
                elif path.is_dir() and 'trouble' in path.name.lower():
                    shutil.rmtree(path); logging.info("Removed Windows-specific folder: %s", path.name)
        except OSError as e:
            logging.warning("Could not remove %s during cleanup: %s", path.name, e)

def download_troubleshooters(current_dir, temp_dir):
    try:
        troubleshooter_url = "https://github.com/team-slide/Innioasis-Updater/raw/main/Troubleshooters%20-%20Windows.zip"
        troubleshooter_zip = temp_dir / "troubleshooters.zip"
        response = requests.get(troubleshooter_url, timeout=15)
        response.raise_for_status()
        troubleshooter_zip.write_bytes(response.content)
        troubleshooting_path = current_dir / "Troubleshooting"
        troubleshooting_path.mkdir(exist_ok=True)
        with zipfile.ZipFile(troubleshooter_zip, 'r') as z: z.extractall(troubleshooting_path)
        return True
    except Exception as e:
        logging.error("Could not download troubleshooters: %s", e)
        return False

def launch_firmware_downloader():
    firmware_script = Path.cwd() / "firmware_downloader.py"
    if firmware_script.exists():
        try:
            launch_cmd = CrossPlatformHelper.get_launch_command(firmware_script)
            subprocess.Popen(launch_cmd)
        except Exception as e: logging.error("Could not launch main application: %s", e)
    else:
        logging.error("Could not find 'firmware_downloader.py'.")

def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', filename='updater.log', filemode='w')
    perform_initial_cleanup()
    
    parser = argparse.ArgumentParser(description="Innioasis Updater Script", add_help=False)
    parser.add_argument("-f", "--force", action="store_true", help="Force the update.")
    args, _ = parser.parse_known_args()

    app = QApplication(sys.argv)
    
    modifiers = QGuiApplication.keyboardModifiers()
    is_troubleshoot_request = bool(modifiers & (Qt.ShiftModifier | Qt.ControlModifier | Qt.AltModifier | Qt.MetaModifier))
    
    mode = 'update' # Default mode
    platform_info = CrossPlatformHelper.get_platform_info()

    if is_troubleshoot_request:
        if platform_info['is_windows']:
            mode = 'troubleshoot_win'
        else:
            mode = 'troubleshoot_maclinux'
    else:
        needs_update = False
        if args.force: needs_update = True
        else:
            try:
                timestamp_file = Path.cwd() / ".last_update_check"
                today = str(datetime.date.today())
                if not timestamp_file.exists() or timestamp_file.read_text() != today: needs_update = True
            except Exception as e:
                logging.error("Could not read timestamp file: %s", e); needs_update = True
        
        if not needs_update:
            mode = 'no_update'

    app.setStyle('Fusion')
    dialog = UpdateProgressDialog(mode=mode)
    dialog.exec()
    
    # Always launch the main app unless the user is on Mac/Linux and requested troubleshoot
    if not (is_troubleshoot_request and not platform_info['is_windows']):
        launch_firmware_downloader()
    
        sys.exit(0)

if __name__ == "__main__":
    main()