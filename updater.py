#!/usr/bin/env python3
"""
Innioasis Updater Script
Downloads and installs the latest version from team-slide/y1-helper repository
Cross-platform support for Windows, macOS, and Linux

Features:
- Automatic process management (kills ADB, flash_tool.exe, libusb, etc.)
- Conservative file handling (never removes existing files, only merges/updates)
- Preserves user data directories (firmware_downloads, assets, Lib, DLLs, etc.)
- Process cleanup on exit and failure
- Enhanced error reporting for locked files
- Graceful handling of blocking processes
- Daily update check with timestamp-based logic
- Automatic launch of firmware_downloader.py after successful update

Safety Features:
- NEVER removes existing files unless explicitly requested
- Preserves all user data and runtime directories
- Verifies downloaded files before extraction
- Checks for expected files after update
- Graceful fallback if update is incomplete
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
import psutil
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
                               QWidget, QLabel, QProgressBar, QPushButton, QTextEdit,
                               QMessageBox, QDialog)
from PySide6.QtCore import QThread, Signal, Qt, QTimer
from PySide6.QtGui import QFont

class ProcessManager:
    """Manages processes that might block file updates"""
    
    # Processes that commonly block file updates
    BLOCKING_PROCESSES = [
        'adb.exe', 'adb', 'flash_tool.exe', 'flash_tool', 'libusb-win32-devel-filter.exe',
        'libusb-win32-devel-filter', 'mtkclient', 'mtk.py', 'firmware_downloader.py',
        'y1_helper.py', 'updater.py', 'python.exe', 'python3', 'python'
    ]
    
    @staticmethod
    def kill_blocking_processes():
        """Kill processes that might block file updates"""
        killed_processes = []
        failed_kills = []
        
        try:
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                try:
                    proc_name = proc.info['name'].lower()
                    cmdline = proc.info['cmdline']
                    
                    # Check if this is a blocking process
                    is_blocking = False
                    for blocking_name in ProcessManager.BLOCKING_PROCESSES:
                        if blocking_name.lower() in proc_name:
                            is_blocking = True
                            break
                    
                    # Also check command line for Python scripts
                    if cmdline and any('firmware_downloader.py' in str(arg) or 'y1_helper.py' in str(arg) or 'updater.py' in str(arg) for arg in cmdline):
                        is_blocking = True
                    
                    # Don't kill the current process
                    if proc.pid == os.getpid():
                        continue
                    
                    if is_blocking:
                        try:
                            proc.terminate()
                            proc.wait(timeout=3)  # Wait up to 3 seconds for graceful termination
                            killed_processes.append(f"{proc_name} (PID: {proc.pid})")
                        except (psutil.NoSuchProcess, psutil.TimeoutExpired):
                            try:
                                proc.kill()  # Force kill if graceful termination fails
                                killed_processes.append(f"{proc_name} (PID: {proc.pid}) - force killed")
                            except psutil.NoSuchProcess:
                                failed_kills.append(f"{proc_name} (PID: {proc.pid}) - already terminated")
                        except Exception as e:
                            failed_kills.append(f"{proc_name} (PID: {proc.pid}) - error: {e}")
                            
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    continue
                    
        except Exception as e:
            return [], [f"Error scanning processes: {e}"]
        
        return killed_processes, failed_kills
    
    @staticmethod
    def kill_adb_server():
        """Kill ADB server specifically"""
        try:
            # Try to kill ADB server using adb kill-server command
            if platform.system().lower() == "windows":
                subprocess.run(['adb', 'kill-server'], 
                             capture_output=True, timeout=10, 
                             creationflags=subprocess.CREATE_NO_WINDOW)
            else:
                subprocess.run(['adb', 'kill-server'], 
                             capture_output=True, timeout=10)
            return True
        except Exception as e:
            # If adb command fails, try to kill adb processes directly
            try:
                for proc in psutil.process_iter(['pid', 'name']):
                    if proc.info['name'] and 'adb' in proc.info['name'].lower():
                        proc.terminate()
                        proc.wait(timeout=3)
                return True
            except Exception:
                return False
    
    @staticmethod
    def wait_for_process_cleanup(timeout=10):
        """Wait for processes to be fully cleaned up"""
        start_time = time.time()
        while time.time() - start_time < timeout:
            # Check if any blocking processes are still running
            blocking_running = False
            try:
                for proc in psutil.process_iter(['name']):
                    proc_name = proc.info['name'].lower()
                    for blocking_name in ProcessManager.BLOCKING_PROCESSES:
                        if blocking_name.lower() in proc_name:
                            blocking_running = True
                            break
                    if blocking_running:
                        break
                
                if not blocking_running:
                    return True
                    
                time.sleep(0.5)  # Wait 500ms before checking again
            except Exception:
                break
        
        return False


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
            
            # Kill blocking processes before starting update
            self.status_updated.emit("Stopping processes that might block updates...")
            self.progress_updated.emit(8)
            
            try:
                killed_processes, failed_kills = ProcessManager.kill_blocking_processes()
                
                if killed_processes:
                    self.status_updated.emit(f"Stopped {len(killed_processes)} blocking processes")
                    for proc in killed_processes[:3]:  # Show first 3 processes
                        self.status_updated.emit(f"  - {proc}")
                    if len(killed_processes) > 3:
                        self.status_updated.emit(f"  ... and {len(killed_processes) - 3} more")
                
                if failed_kills:
                    self.status_updated.emit(f"Warning: {len(failed_kills)} processes couldn't be stopped")
                
                # Kill ADB server specifically
                if ProcessManager.kill_adb_server():
                    self.status_updated.emit("ADB server stopped")
                else:
                    self.status_updated.emit("Warning: Could not stop ADB server")
                
                # Wait for processes to be fully cleaned up
                if ProcessManager.wait_for_process_cleanup():
                    self.status_updated.emit("Process cleanup completed")
                else:
                    self.status_updated.emit("Warning: Some processes may still be running")
                
            except Exception as e:
                self.status_updated.emit(f"Warning: Error stopping processes: {e}")
                self.status_updated.emit("Continuing with update...")
            
            self.progress_updated.emit(10)
            
            # Download latest version from GitHub - use the correct repository
            github_url = "https://github.com/team-slide/y1-helper/archive/refs/heads/main.zip"
            zip_file = current_dir / "innioasis_updater_latest.zip"
            
            self.status_updated.emit("Downloading latest version from GitHub...")
            self.progress_updated.emit(15)
            
            try:
                self.download_with_progress(github_url, zip_file)
                self.status_updated.emit("Download completed!")
                self.progress_updated.emit(50)
                
                # Verify the downloaded file
                if not zip_file.exists() or zip_file.stat().st_size < 10000:  # Less than 10KB
                    self.update_completed.emit(False, "Downloaded file is too small or missing - download may have failed")
                    return
                    
                # Verify it's a valid zip file
                try:
                    with zipfile.ZipFile(zip_file, 'r') as test_zip:
                        file_list = test_zip.namelist()
                        if not file_list:
                            self.update_completed.emit(False, "Downloaded file is not a valid zip archive")
                            return
                        self.status_updated.emit(f"Zip file verified: {len(file_list)} files found")
                except Exception as e:
                    self.update_completed.emit(False, f"Downloaded file is not a valid zip archive: {e}")
                    return
                    
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
            
            extracted_dir = next(current_dir.glob("y1-helper-main*"), None)
            if not extracted_dir:
                self.update_completed.emit(False, "Could not find extracted directory")
                return
            
            # Verify the extracted directory contains expected files
            expected_files = ["firmware_downloader.py", "y1_helper.py", "updater.py"]
            missing_files = []
            for expected_file in expected_files:
                if not (extracted_dir / expected_file).exists():
                    missing_files.append(expected_file)
            
            if missing_files:
                self.status_updated.emit(f"Warning: Missing expected files: {', '.join(missing_files)}")
                self.status_updated.emit("Update may be incomplete")
            else:
                self.status_updated.emit("All expected files found in update")
            
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
            
            # Extract troubleshooting shortcuts if present
            self.status_updated.emit("Setting up troubleshooting shortcuts...")
            self.progress_updated.emit(96)
            
            try:
                self.extract_troubleshooting_shortcuts(current_dir)
                self.status_updated.emit("Troubleshooting shortcuts ready!")
                self.progress_updated.emit(97)
            except Exception as e:
                self.status_updated.emit(f"Warning: Could not set up troubleshooting shortcuts: {e}")
                self.progress_updated.emit(97)
            
            # Verify that firmware_downloader.py exists after update
            self.status_updated.emit("Verifying update...")
            self.progress_updated.emit(98)
            
            firmware_script = current_dir / "firmware_downloader.py"
            if not firmware_script.exists():
                self.status_updated.emit("Warning: firmware_downloader.py not found after update")
                self.status_updated.emit("This may indicate an incomplete update")
                
                # Try to find any Python scripts that might be the main application
                python_scripts = list(current_dir.glob("*.py"))
                if python_scripts:
                    self.status_updated.emit(f"Found Python scripts: {', '.join([s.name for s in python_scripts])}")
                    self.status_updated.emit("Update may have been partially successful")
                else:
                    self.status_updated.emit("No Python scripts found - update may have failed")
            else:
                self.status_updated.emit("firmware_downloader.py verified successfully")
                
                # Check file size to ensure it's not empty
                if firmware_script.stat().st_size < 1000:  # Less than 1KB
                    self.status_updated.emit("Warning: firmware_downloader.py appears to be very small")
                    self.status_updated.emit("This may indicate a corrupted download")
            
            # Clean up
            self.status_updated.emit("Cleaning up...")
            self.progress_updated.emit(99)
            
            try:
                zip_file.unlink(missing_ok=True)
                shutil.rmtree(extracted_dir)
                timestamp_file.write_text(str(time.time()))
                
                # Log successful update
                self.status_updated.emit("Update timestamp recorded")
                
            except Exception as e:
                self.status_updated.emit(f"Warning: Could not clean up temporary files: {e}")
            
            self.progress_updated.emit(100)
            self.status_updated.emit("Update completed successfully!")
            self.status_updated.emit("The application will now launch...")
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
        skipped_files = []
        
        # Check if any blocking processes are still running before starting file operations
        self.status_updated.emit("Checking for blocking processes before file operations...")
        try:
            blocking_running = False
            for proc in psutil.process_iter(['name']):
                proc_name = proc.info['name'].lower()
                for blocking_name in ProcessManager.BLOCKING_PROCESSES:
                    if blocking_name.lower() in proc_name and proc.pid != os.getpid():
                        blocking_running = True
                        self.status_updated.emit(f"Warning: {proc_name} (PID: {proc.pid}) is still running")
                        break
                if blocking_running:
                    break
            
            if blocking_running:
                self.status_updated.emit("Some blocking processes are still running - file operations may fail")
                self.status_updated.emit("Attempting to continue with update...")
        except Exception as e:
            self.status_updated.emit(f"Warning: Could not check for blocking processes: {e}")
        
        for item in source_dir.iterdir():
            # Skip Git and cache directories
            if item.name in [".git", "__pycache__", ".DS_Store"]:
                continue
            
            # NEVER touch firmware_downloads directory - it contains user data
            if item.name == "firmware_downloads":
                self.status_updated.emit("Skipping firmware_downloads directory (preserving user data)")
                continue
            
            # Skip any other directories that might contain user data or runtime files
            if item.name in ["assets", "Lib", "DLLs", "Scripts", "Tools"]:
                self.status_updated.emit(f"Skipping {item.name} directory (preserving existing files)")
                continue
            
            # CRITICAL: Never skip .exe files on Windows - they are essential system files
            # Only skip .lnk files on Windows if they're old shortcuts
            if item.name.endswith('.exe'):
                # Always copy .exe files - they are essential
                pass
            elif item.name.endswith('.lnk'):
                # Handle .lnk files based on platform
                if not self.platform_info['is_windows']:
                    # Skip .lnk files on non-Windows systems
                    skipped_files.append(f"{item.name} (Windows-specific)")
                    continue
                elif item.name not in ['Innioasis Updater.lnk']:
                    # On Windows, skip old .lnk files but keep essential ones
                    skipped_files.append(f"{item.name} (old shortcut)")
                    continue
                
            dest_item = dest_dir / item.name
            
            try:
                if item.is_file():
                    # For files, always copy (overwrite if exists)
                    shutil.copy2(item, dest_item)
                elif item.is_dir():
                    # For directories, merge contents instead of replacing
                    if dest_item.exists():
                        # Copy contents of source directory into existing destination
                        for subitem in item.iterdir():
                            subdest = dest_item / subitem.name
                            if subitem.is_file():
                                shutil.copy2(subitem, subdest)
                            elif subitem.is_dir():
                                if subdest.exists():
                                    # Recursively merge subdirectories
                                    self.merge_directories(subitem, subdest)
                                else:
                                    shutil.copytree(subitem, subdest)
                    else:
                        # Destination doesn't exist, copy the entire directory
                        shutil.copytree(item, dest_item)
            except PermissionError as e:
                # Handle write blocking errors (files in use) - common with DLL/EXE files
                if "being used by another process" in str(e) or "access is denied" in str(e):
                    error_files.append(f"{item.name} (in use)")
                    # Try to identify which process is using the file
                    try:
                        for proc in psutil.process_iter(['pid', 'name', 'open_files']):
                            try:
                                for file_info in proc.open_files():
                                    if str(dest_item) in str(file_info.path):
                                        error_files[-1] = f"{item.name} (in use by {proc.info['name']} PID: {proc.pid})"
                                        break
                            except (psutil.NoSuchProcess, psutil.AccessDenied):
                                continue
                    except Exception:
                        pass
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
        
        # Show summary of skipped and error files
        if skipped_files:
            self.status_updated.emit(f"Skipped {len(skipped_files)} Windows-specific files on {self.platform_info['system'].title()}")
        
        if error_files:
            self.status_updated.emit(f"Note: {len(error_files)} files couldn't be updated (likely in use) - will update on next run")
            
            # Show which processes are blocking files
            blocking_processes = set()
            for error_file in error_files:
                if "in use by" in error_file:
                    process_info = error_file.split("in use by ")[1].split(" PID:")[0]
                    blocking_processes.add(process_info)
            
            if blocking_processes:
                self.status_updated.emit(f"Files are being used by: {', '.join(blocking_processes)}")
                self.status_updated.emit("These processes will be automatically stopped on the next update")
            
            self.status_updated.emit("Update proceeding successfully - blocked files will be updated later")

    def merge_directories(self, source_dir, dest_dir):
        """Recursively merge source directory into destination directory"""
        for item in source_dir.iterdir():
            subdest = dest_dir / item.name
            if item.is_file():
                # Always copy files (overwrite if exists)
                shutil.copy2(item, subdest)
            elif item.is_dir():
                if subdest.exists():
                    # Recursively merge subdirectories
                    self.merge_directories(item, subdest)
                else:
                    # Copy the entire subdirectory if it doesn't exist
                    shutil.copytree(item, subdest)

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

    def extract_troubleshooting_shortcuts(self, current_dir):
        """Extract troubleshooting shortcuts from Troubleshooters - Windows.zip if present"""
        troubleshooters_zip = current_dir / "Troubleshooters - Windows.zip"
        
        if troubleshooters_zip.exists():
            self.status_updated.emit("Found troubleshooting shortcuts, extracting...")
            
            try:
                with zipfile.ZipFile(troubleshooters_zip, 'r') as zip_ref:
                    zip_ref.extractall(current_dir)
                
                # Remove the zip file after extraction
                troubleshooters_zip.unlink()
                self.status_updated.emit("Troubleshooting shortcuts extracted successfully")
                
            except Exception as e:
                self.status_updated.emit(f"Error extracting troubleshooting shortcuts: {e}")
                raise e
        else:
            self.status_updated.emit("No troubleshooting shortcuts found, skipping...")


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
            
            # Clean up any processes that were started during the update
            self.update_status("Cleaning up processes...")
            try:
                ProcessManager.kill_blocking_processes()
                ProcessManager.kill_adb_server()
                self.update_status("Process cleanup completed")
            except Exception as e:
                self.update_status(f"Warning: Error during process cleanup: {e}")
            
            self.reject()
    
    def on_update_completed(self, success, message):
        """Handle update completion"""
        self.update_status(message)
        if success:
            QTimer.singleShot(2000, self.accept)
        else:
            # Clean up processes if update failed
            self.update_status("Cleaning up processes after failed update...")
            try:
                ProcessManager.kill_blocking_processes()
                ProcessManager.kill_adb_server()
                self.update_status("Process cleanup completed")
            except Exception as e:
                self.update_status(f"Warning: Error during process cleanup: {e}")
            
            QMessageBox.critical(self, "Update Failed", f"Update failed: {message}")
            self.reject()


def launch_firmware_downloader():
    """Finds and launches the main firmware_downloader.py script."""
    firmware_script = Path.cwd() / "firmware_downloader.py"
    if firmware_script.exists():
        try:
            launch_cmd = CrossPlatformHelper.get_launch_command(firmware_script)
            print(f"Launching: {' '.join(launch_cmd)}")
            
            # Use windowless subprocess on Windows to avoid command prompt flash
            if CrossPlatformHelper.get_platform_info()['is_windows']:
                subprocess.Popen(launch_cmd, creationflags=subprocess.CREATE_NO_WINDOW)
            else:
                subprocess.Popen(launch_cmd)
            
            return True
        except Exception as e:
            QMessageBox.critical(None, "Launch Failed", f"Could not launch the main application:\n{e}")
    else:
        QMessageBox.critical(None, "Launch Failed", "Could not find 'firmware_downloader.py'.")
    return False


def check_for_blocking_processes():
    """Check if any blocking processes are running before starting the updater"""
    try:
        blocking_found = []
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                proc_name = proc.info['name'].lower()
                cmdline = proc.info['cmdline']
                
                # Check if this is a blocking process
                for blocking_name in ProcessManager.BLOCKING_PROCESSES:
                    if blocking_name.lower() in proc_name and proc.pid != os.getpid():
                        blocking_found.append(f"{proc_name} (PID: {proc.pid})")
                        break
                
                # Also check command line for Python scripts
                if cmdline and any('firmware_downloader.py' in str(arg) or 'y1_helper.py' in str(arg) for arg in cmdline):
                    blocking_found.append(f"Python script (PID: {proc.pid})")
                    
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        
        return blocking_found
    except Exception:
        return []

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

    # Check for blocking processes before starting
    if needs_update:
        blocking_processes = check_for_blocking_processes()
        if blocking_processes:
            print("Warning: The following processes may block updates:")
            for proc in blocking_processes:
                print(f"  - {proc}")
            print("The updater will attempt to stop these processes automatically.")
            print()

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


def cleanup_on_exit():
    """Cleanup function to be called on exit"""
    try:
        # Kill any remaining blocking processes
        ProcessManager.kill_blocking_processes()
        ProcessManager.kill_adb_server()
    except Exception:
        pass

if __name__ == "__main__":
    # Register cleanup function
    import atexit
    atexit.register(cleanup_on_exit)
    
    try:
        main()
    except KeyboardInterrupt:
        print("\nUpdate interrupted by user")
        cleanup_on_exit()
        sys.exit(1)
    except Exception as e:
        print(f"Fatal error: {e}")
        cleanup_on_exit()
        sys.exit(1)
