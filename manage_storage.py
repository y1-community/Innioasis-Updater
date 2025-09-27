#!/usr/bin/env python3
"""
Storage Management Tool for Innioasis Updater
Manages storage usage by analyzing firmware downloads and extracted files
"""

import sys
import os
import platform
from pathlib import Path
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
                               QWidget, QPushButton, QLabel, QProgressBar, QMessageBox, 
                               QGroupBox, QTextEdit, QListWidget, QListWidgetItem, QCheckBox,
                               QSplitter, QHeaderView, QTableWidget, QTableWidgetItem, QAbstractItemView)
from PySide6.QtCore import QThread, Signal, Qt, QTimer
from PySide6.QtGui import QFont, QIcon
import time

class StorageAnalysisWorker(QThread):
    """Worker thread for analyzing storage usage"""
    progress = Signal(int)
    status = Signal(str)
    analysis_completed = Signal(dict)
    error = Signal(str)
    
    def __init__(self, project_dir):
        super().__init__()
        self.project_dir = Path(project_dir)
        
    def run(self):
        try:
            self.status.emit("Starting storage analysis...")
            self.progress.emit(10)
            
            # Analyze firmware downloads
            self.status.emit("Analyzing firmware downloads...")
            firmware_downloads = self.analyze_firmware_downloads()
            self.progress.emit(40)
            
            # Analyze extracted files
            self.status.emit("Analyzing extracted files...")
            extracted_files = self.analyze_extracted_files()
            self.progress.emit(50)
            
            # Analyze extra subfolders
            self.status.emit("Analyzing extra subfolders...")
            extra_subfolders = self.analyze_extra_subfolders()
            self.progress.emit(60)
            
            # Analyze platform-specific files (Windows executables on non-Windows systems)
            self.status.emit("Analyzing platform-specific files...")
            platform_files = self.analyze_platform_specific_files()
            self.progress.emit(70)
            
            # Calculate totals
            self.status.emit("Calculating storage totals...")
            analysis_result = {
                'firmware_downloads': firmware_downloads,
                'extracted_files': extracted_files,
                'extra_subfolders': extra_subfolders,
                'platform_files': platform_files,
                'total_download_size': sum(f['size'] for f in firmware_downloads),
                'total_extracted_size': sum(f['size'] for f in extracted_files),
                'total_extra_size': sum(f['size'] for f in extra_subfolders),
                'total_platform_size': sum(f['size'] for f in platform_files),
                'total_cleanup_size': sum(f['size'] for f in firmware_downloads) + sum(f['size'] for f in extracted_files) + sum(f['size'] for f in extra_subfolders) + sum(f['size'] for f in platform_files)
            }
            
            self.progress.emit(100)
            self.status.emit("Analysis completed")
            self.analysis_completed.emit(analysis_result)
            
        except Exception as e:
            self.error.emit(f"Analysis error: {str(e)}")
    
    def analyze_firmware_downloads(self):
        """Analyze files in firmware_downloads folder"""
        downloads_dir = self.project_dir / "firmware_downloads"
        downloads = []
        
        if downloads_dir.exists():
            for file_path in downloads_dir.iterdir():
                if file_path.is_file():
                    file_info = {
                        'name': file_path.name,
                        'path': str(file_path.relative_to(self.project_dir)),
                        'size': file_path.stat().st_size,
                        'full_path': str(file_path),
                        'type': 'firmware_download'
                    }
                    downloads.append(file_info)
        
        return downloads
    
    def analyze_extracted_files(self):
        """Analyze extracted firmware files in project root"""
        extracted_files = []
        
        # List of files that are extracted from firmware zips
        extracted_file_names = [
            'android-info.txt', 'boot.img', 'cache.img', 'clean_steps.mk', 'EBR1', 'EBR2',
            'factory.ini', 'installed-files.txt', 'kernel', 'kernel_g368_nyx.bin', 'lk.bin',
            'logo.bin', 'MBR', 'MT6572_Android_scatter.txt', 'preloader_g368_nyx.bin',
            'previous_build_config.mk', 'ramdisk-recovery.img', 'ramdisk.img', 'recovery.img',
            'secro.img', 'system.img', 'userdata.img'
        ]
        
        for file_name in extracted_file_names:
            file_path = self.project_dir / file_name
            if file_path.exists() and file_path.is_file():
                file_info = {
                    'name': file_path.name,
                    'path': str(file_path.relative_to(self.project_dir)),
                    'size': file_path.stat().st_size,
                    'full_path': str(file_path),
                    'type': 'extracted_file'
                }
                extracted_files.append(file_info)
        
        return extracted_files
    
    def analyze_extra_subfolders(self):
        """Analyze subfolders that aren't essential directories"""
        extra_subfolders = []
        
        # Essential directories that should be preserved
        essential_dirs = {
            '.cache', '.github', 'assets', 'codecs', 'Contents', 'examples', 
            'firmware_downloads', 'logs', 'More Tools and Troubleshooters', 
            'mtkclient', 'src', 'Toolkit', 'Tools', 'Troubleshooting', 'venv',
            '__pycache__', 'libs', 'DLLs', 'Lib', 'scripts', 'Scripts', 'tcl', 'include'  # Add libs, DLLs, Lib, scripts, Scripts, tcl, include directories
        }
        
        # File extensions that should never be offered for removal by storage manager
        # These are only handled by redundant_files.txt cleanup
        # On Windows, .exe and .dll are protected, but on macOS/Linux they can be removed
        current_platform = platform.system().lower()
        if current_platform == "windows":
            protected_extensions = {'.exe', '.py', '.dll', '.so', '.dylib'}
        else:
            # On macOS/Linux, .exe and .dll files are not needed and can be removed
            protected_extensions = {'.py', '.so', '.dylib'}
        
        for item in self.project_dir.iterdir():
            if item.is_dir() and item.name not in essential_dirs:
                # Check if directory contains only protected file types
                if self.contains_only_protected_files(item, protected_extensions):
                    continue  # Skip directories with only protected files
                
                # Calculate directory size
                dir_size = self.calculate_directory_size(item)
                file_info = {
                    'name': item.name,
                    'path': str(item.relative_to(self.project_dir)),
                    'size': dir_size,
                    'full_path': str(item),
                    'type': 'extra_subfolder'
                }
                extra_subfolders.append(file_info)
        
        return extra_subfolders
    
    def analyze_platform_specific_files(self):
        """Analyze platform-specific files that can be removed on non-Windows systems"""
        platform_files = []
        current_platform = platform.system().lower()
        
        # Only analyze on non-Windows systems
        if current_platform != "windows":
            # Look for .exe and .dll files in the project directory
            for file_path in self.project_dir.rglob('*'):
                if file_path.is_file() and file_path.suffix.lower() in ['.exe', '.dll']:
                    # Skip files in protected directories
                    if any(protected_dir in str(file_path) for protected_dir in ['venv', 'mtkclient', 'assets', 'Tools', 'Troubleshooting']):
                        continue
                    
                    file_info = {
                        'name': file_path.name,
                        'path': str(file_path.relative_to(self.project_dir)),
                        'size': file_path.stat().st_size,
                        'full_path': str(file_path),
                        'type': 'platform_file'
                    }
                    platform_files.append(file_info)
        
        return platform_files
    
    def contains_only_protected_files(self, directory, protected_extensions):
        """Check if directory contains only files with protected extensions"""
        try:
            for file_path in directory.rglob('*'):
                if file_path.is_file():
                    if file_path.suffix.lower() not in protected_extensions:
                        return False  # Found a non-protected file
            return True  # All files are protected
        except (OSError, PermissionError):
            return True  # Assume protected if we can't access
    
    def calculate_directory_size(self, directory):
        """Calculate total size of a directory"""
        total_size = 0
        try:
            for file_path in directory.rglob('*'):
                if file_path.is_file():
                    try:
                        total_size += file_path.stat().st_size
                    except (OSError, PermissionError):
                        # Skip files that can't be accessed
                        continue
        except (OSError, PermissionError):
            # Skip directories that can't be accessed
            pass
        return total_size

class StorageManagementTool(QMainWindow):
    """Main GUI window for storage management"""
    
    def __init__(self):
        super().__init__()
        self.analysis_result = None
        self.analysis_worker = None
        
        self.init_ui()
        self.start_analysis()
        
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("Storage Management Tool - Innioasis Updater")
        self.setGeometry(100, 100, 800, 600)
        
        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # Header
        title_label = QLabel("Storage Management Tool")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 16, QFont.Bold))
        main_layout.addWidget(title_label)
        
        desc_label = QLabel("Manage firmware downloads and extracted files")
        desc_label.setAlignment(Qt.AlignCenter)
        desc_label.setWordWrap(True)
        main_layout.addWidget(desc_label)
        
        # Progress section
        progress_group = QGroupBox("Analysis Progress")
        progress_layout = QVBoxLayout(progress_group)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        progress_layout.addWidget(self.progress_bar)
        
        self.status_label = QLabel("Ready to analyze storage usage")
        self.status_label.setAlignment(Qt.AlignCenter)
        progress_layout.addWidget(self.status_label)
        
        main_layout.addWidget(progress_group)
        
        # Results section
        results_group = QGroupBox("Storage Analysis Results")
        results_layout = QVBoxLayout(results_group)
        
        # Storage summary
        self.summary_label = QLabel("No analysis results available")
        self.summary_label.setAlignment(Qt.AlignCenter)
        self.summary_label.setWordWrap(True)
        results_layout.addWidget(self.summary_label)
        
        # File categories table
        self.files_table = QTableWidget()
        self.files_table.setColumnCount(3)
        self.files_table.setHorizontalHeaderLabels(["File", "Size", "Type"])
        self.files_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.files_table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.files_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.files_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.files_table.setVisible(False)
        self.files_table.selectionModel().selectionChanged.connect(self.on_selection_changed)
        results_layout.addWidget(self.files_table)
        
        main_layout.addWidget(results_group)
        
        # Action buttons
        button_layout = QHBoxLayout()
        
        self.analyze_btn = QPushButton("Re-analyze")
        self.analyze_btn.clicked.connect(self.start_analysis)
        button_layout.addWidget(self.analyze_btn)
        
        self.cleanup_btn = QPushButton("Clean Up Selected Files")
        self.cleanup_btn.clicked.connect(self.cleanup_selected_files)
        self.cleanup_btn.setEnabled(False)
        button_layout.addWidget(self.cleanup_btn)
        
        self.cleanup_all_btn = QPushButton("Clean Up All")
        self.cleanup_all_btn.clicked.connect(self.cleanup_all_files)
        self.cleanup_all_btn.setEnabled(False)
        button_layout.addWidget(self.cleanup_all_btn)
        
        # Add view in file manager button (not on Windows)
        if platform.system() != 'Windows':
            self.view_btn = QPushButton("Go to App Folder")
            self.view_btn.clicked.connect(self.view_in_file_manager)
            button_layout.addWidget(self.view_btn)
        
        self.close_btn = QPushButton("Close")
        self.close_btn.clicked.connect(self.close)
        button_layout.addWidget(self.close_btn)
        
        main_layout.addLayout(button_layout)
        
    def start_analysis(self):
        """Start storage analysis"""
        if self.analysis_worker and self.analysis_worker.isRunning():
            return
        
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.status_label.setText("Starting analysis...")
        self.analyze_btn.setEnabled(False)
        self.cleanup_btn.setEnabled(False)
        self.cleanup_all_btn.setEnabled(False)
        self.files_table.setVisible(False)
        
        # Start analysis worker
        self.analysis_worker = StorageAnalysisWorker(Path.cwd())
        self.analysis_worker.progress.connect(self.progress_bar.setValue)
        self.analysis_worker.status.connect(self.status_label.setText)
        self.analysis_worker.analysis_completed.connect(self.on_analysis_completed)
        self.analysis_worker.error.connect(self.on_analysis_error)
        self.analysis_worker.start()
    
    def on_analysis_completed(self, result):
        """Handle analysis completion"""
        self.analysis_result = result
        self.progress_bar.setVisible(False)
        self.analyze_btn.setEnabled(True)
        self.cleanup_btn.setEnabled(True)
        self.cleanup_all_btn.setEnabled(True)
        
        # Update summary
        total_downloads = len(result['firmware_downloads'])
        total_extracted = len(result['extracted_files'])
        total_extra = len(result['extra_subfolders'])
        total_platform = len(result['platform_files'])
        total_size = result['total_cleanup_size']
        
        summary_text = f"""
        <b>Storage Analysis Complete</b><br><br>
        <b>Firmware Downloads:</b> {total_downloads} files ({self.format_size(result['total_download_size'])})<br>
        <b>Extracted Files:</b> {total_extracted} files ({self.format_size(result['total_extracted_size'])})<br>
        <b>Extra Subfolders:</b> {total_extra} folders ({self.format_size(result['total_extra_size'])})<br>
        <b>Platform Files:</b> {total_platform} files ({self.format_size(result['total_platform_size'])})<br>
        <b>Total Cleanup Available:</b> {self.format_size(total_size)}<br><br>
        <b>Note:</b> Extracted files are automatically cleaned up by firmware_downloader.py and updater.py after installation.
        """
        self.summary_label.setText(summary_text)
        
        # Populate files table
        self.populate_files_table(result)
        self.files_table.setVisible(True)
    
    def on_analysis_error(self, error_msg):
        """Handle analysis error"""
        self.progress_bar.setVisible(False)
        self.analyze_btn.setEnabled(True)
        self.status_label.setText(f"Analysis failed: {error_msg}")
        
        QMessageBox.critical(self, "Analysis Error", f"Failed to analyze storage:\n{error_msg}")
    
    def populate_files_table(self, result):
        """Populate the files table with analysis results"""
        all_files = []
        
        # Add firmware downloads
        for file_info in result['firmware_downloads']:
            all_files.append((file_info, "Firmware Download"))
        
        # Add extracted files
        for file_info in result['extracted_files']:
            all_files.append((file_info, "Extracted File"))
        
        # Add extra subfolders
        for file_info in result['extra_subfolders']:
            all_files.append((file_info, "Extra Subfolder"))
        
        # Add platform files
        for file_info in result['platform_files']:
            all_files.append((file_info, "Platform File"))
        
        # Sort by size (largest first)
        all_files.sort(key=lambda x: x[0]['size'], reverse=True)
        
        # Populate table
        self.files_table.setRowCount(len(all_files))
        
        for row, (file_info, file_type) in enumerate(all_files):
            # File name
            name_item = QTableWidgetItem(file_info['name'])
            name_item.setData(Qt.UserRole, file_info)
            self.files_table.setItem(row, 0, name_item)
            
            # Size
            size_item = QTableWidgetItem(self.format_size(file_info['size']))
            self.files_table.setItem(row, 1, size_item)
            
            # Type
            type_item = QTableWidgetItem(file_type)
            self.files_table.setItem(row, 2, type_item)
            
            # No color coding - clean interface
    
    def format_size(self, size_bytes):
        """Format file size"""
        if size_bytes == 0:
            return "0 B"
        size_names = ["B", "KB", "MB", "GB"]
        i = 0
        while size_bytes >= 1024 and i < len(size_names) - 1:
            size_bytes /= 1024.0
            i += 1
        return f"{size_bytes:.1f} {size_names[i]}"
    
    def cleanup_selected_files(self):
        """Clean up selected files"""
        if not self.analysis_result:
            return
        
        # Get selected rows
        selected_rows = set()
        for item in self.files_table.selectedItems():
            selected_rows.add(item.row())
        
        if not selected_rows:
            QMessageBox.warning(self, "No Selection", "Please select files to clean up.")
            return
        
        # Get files to delete
        files_to_delete = []
        for row in selected_rows:
            file_item = self.files_table.item(row, 0)
            if file_item:
                file_info = file_item.data(Qt.UserRole)
                files_to_delete.append(file_info)
        
        if not files_to_delete:
            QMessageBox.warning(self, "Invalid Selection", "No files selected for cleanup.")
            return
        
        # Confirm deletion
        total_size = sum(f['size'] for f in files_to_delete)
        size_formatted = self.format_size(total_size)
        
        reply = QMessageBox.question(
            self, "Confirm Cleanup",
            f"Are you sure you want to delete {len(files_to_delete)} files ({size_formatted})?\n\n"
            "This action cannot be undone.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.perform_cleanup(files_to_delete)
    
    def cleanup_all_files(self):
        """Clean up all files"""
        if not self.analysis_result:
            return
        
        all_files = (self.analysis_result['firmware_downloads'] + 
                    self.analysis_result['extracted_files'] + 
                    self.analysis_result['extra_subfolders'] +
                    self.analysis_result['platform_files'])
        
        if not all_files:
            QMessageBox.information(self, "No Files", "No files to clean up.")
            return
        
        # Confirm deletion
        total_size = sum(f['size'] for f in all_files)
        size_formatted = self.format_size(total_size)
        
        reply = QMessageBox.question(
            self, "Confirm Cleanup All",
            f"Are you sure you want to delete ALL {len(all_files)} files ({size_formatted})?\n\n"
            "This will remove all firmware downloads and extracted files.\n"
            "This action cannot be undone.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            self.perform_cleanup(all_files)
    
    def perform_cleanup(self, files_to_delete):
        """Perform the actual cleanup"""
        deleted_count = 0
        deleted_size = 0
        errors = []
        
        for file_info in files_to_delete:
            try:
                file_path = Path(file_info['full_path'])
                if file_path.exists():
                    if file_path.is_file():
                        file_path.unlink()
                    elif file_path.is_dir():
                        import shutil
                        shutil.rmtree(file_path)
                    deleted_count += 1
                    deleted_size += file_info['size']
            except Exception as e:
                errors.append(f"{file_info['name']}: {str(e)}")
        
        # Show results
        if errors:
            error_msg = f"Cleanup completed with errors:\n\n"
            error_msg += f"Successfully deleted: {deleted_count} files ({self.format_size(deleted_size)})\n\n"
            error_msg += f"Errors:\n" + "\n".join(errors)
            QMessageBox.warning(self, "Cleanup Results", error_msg)
        else:
            QMessageBox.information(
                self, "Cleanup Complete",
                f"Successfully deleted {deleted_count} files ({self.format_size(deleted_size)})."
            )
        
        # Refresh analysis
        self.start_analysis()
    
    def on_selection_changed(self):
        """Handle table selection changes to update view button text"""
        # Only update button text if the view button exists (not on Windows)
        if not hasattr(self, 'view_btn'):
            return
            
        selected_rows = self.files_table.selectionModel().selectedRows()
        if selected_rows:
            # Get the selected file path from the first column
            row = selected_rows[0].row()
            file_name = self.files_table.item(row, 0).text()
            
            # Use platform-appropriate text
            if platform.system() == 'Darwin':  # macOS
                self.view_btn.setText("View in Finder")
            else:  # Linux
                self.view_btn.setText("View in File Manager")
        else:
            self.view_btn.setText("Go to App Folder")
    
    def view_in_file_manager(self):
        """Open the selected file/folder or app folder in the system file manager"""
        import subprocess
        import os
        from pathlib import Path
        
        # Get the app folder (where the script is located)
        app_folder = Path(__file__).parent.absolute()
        
        # Check if a file is selected
        selected_rows = self.files_table.selectionModel().selectedRows()
        if selected_rows:
            # Get the selected file path from the first column
            row = selected_rows[0].row()
            file_name = self.files_table.item(row, 0).text()
            target_path = app_folder / file_name
        else:
            # No file selected, open app folder
            target_path = app_folder
        
        try:
            # Determine the platform and use appropriate command
            if os.name == 'nt':  # Windows
                # Windows explorer /select, returns non-zero exit code even on success
                # So we don't use check=True for Windows
                result = subprocess.run(['explorer', '/select,', str(target_path)], 
                                      capture_output=True, text=True)
                # Only show error if the command actually failed (not just non-zero exit)
                if result.returncode != 0 and result.stderr:
                    QMessageBox.warning(self, "Error", f"Failed to open file manager: {result.stderr}")
            elif os.name == 'posix':  # macOS and Linux
                if platform.system() == 'Darwin':  # macOS
                    subprocess.run(['open', '-R', str(target_path)], check=True)
                else:  # Linux
                    subprocess.run(['xdg-open', str(target_path)], check=True)
        except subprocess.CalledProcessError as e:
            QMessageBox.warning(self, "Error", f"Failed to open file manager: {e}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Unexpected error: {e}")

def main():
    """Main function"""
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("Storage Management Tool")
    app.setApplicationVersion("1.0")
    
    # Create and show main window
    window = StorageManagementTool()
    window.show()
    
    # Run application
    sys.exit(app.exec())

if __name__ == "__main__":
    main()