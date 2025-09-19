#!/usr/bin/env python3
"""
Mac Cleanup Utility for Y1
Removes .DS_Store and .Trashes files from selected drive/directory
"""

import sys
import os
import subprocess
import threading
from pathlib import Path
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
                               QWidget, QPushButton, QLabel, QProgressBar, QMessageBox, 
                               QFileDialog, QGroupBox, QTextEdit)
from PySide6.QtCore import QThread, Signal, Qt, QTimer
from PySide6.QtGui import QFont
import platform

class CleanupWorker(QThread):
    """Worker thread for cleaning up Mac files"""
    progress = Signal(int)
    status = Signal(str)
    finished = Signal(int, int)  # files_deleted, folders_cleaned
    error = Signal(str)
    
    def __init__(self, target_path):
        super().__init__()
        self.target_path = target_path
        
    def run(self):
        try:
            files_deleted = 0
            folders_cleaned = 0
            
            self.status.emit("Scanning for Mac system files...")
            
            # Walk through directory tree
            for root, dirs, files in os.walk(self.target_path):
                # Count total items for progress
                total_items = len(files) + len(dirs)
                current_item = 0
                
                # Check files
                for file in files:
                    if file == '.DS_Store':
                        try:
                            file_path = os.path.join(root, file)
                            os.remove(file_path)
                            files_deleted += 1
                            self.status.emit(f"Deleted: {file_path}")
                        except Exception as e:
                            self.status.emit(f"Could not delete {file_path}: {str(e)}")
                    
                    current_item += 1
                    progress = int((current_item / total_items) * 100) if total_items > 0 else 0
                    self.progress.emit(progress)
                
                # Check directories for .Trashes
                for dir_name in dirs:
                    if dir_name == '.Trashes':
                        try:
                            trash_path = os.path.join(root, dir_name)
                            # Remove the entire .Trashes directory
                            import shutil
                            shutil.rmtree(trash_path)
                            folders_cleaned += 1
                            self.status.emit(f"Removed: {trash_path}")
                        except Exception as e:
                            self.status.emit(f"Could not remove {trash_path}: {str(e)}")
                    
                    current_item += 1
                    progress = int((current_item / total_items) * 100) if total_items > 0 else 0
                    self.progress.emit(progress)
            
            self.status.emit("Cleanup completed")
            self.finished.emit(files_deleted, folders_cleaned)
            
        except Exception as e:
            self.error.emit(f"Cleanup error: {str(e)}")

class MacCleanupUtility(QMainWindow):
    """Main GUI window for the Mac cleanup utility"""
    
    def __init__(self):
        super().__init__()
        self.cleanup_worker = None
        self.target_path = None
        
        self.init_ui()
        
    def init_ui(self):
        """Initialize the user interface"""
        self.setWindowTitle("Mac Cleanup Utility for Y1")
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
        title_label = QLabel("Mac Cleanup Utility for Y1")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Description
        desc_label = QLabel("Remove .DS_Store and .Trashes files from your Y1 device")
        desc_label.setAlignment(Qt.AlignCenter)
        desc_label.setWordWrap(True)
        main_layout.addWidget(desc_label)
        
        # Target selection
        target_group = QGroupBox("Target Location")
        target_layout = QVBoxLayout(target_group)
        
        self.target_label = QLabel("No location selected")
        self.target_label.setAlignment(Qt.AlignCenter)
        target_layout.addWidget(self.target_label)
        
        self.select_target_btn = QPushButton("Select Drive or Directory")
        self.select_target_btn.clicked.connect(self.select_target)
        target_layout.addWidget(self.select_target_btn)
        
        main_layout.addWidget(target_group)
        
        # Cleanup section
        cleanup_group = QGroupBox("Cleanup")
        cleanup_layout = QVBoxLayout(cleanup_group)
        
        self.cleanup_btn = QPushButton("Start Cleanup")
        self.cleanup_btn.clicked.connect(self.start_cleanup)
        cleanup_layout.addWidget(self.cleanup_btn)
        
        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        cleanup_layout.addWidget(self.progress_bar)
        
        # Status label
        self.status_label = QLabel("Ready to clean up Mac system files")
        self.status_label.setAlignment(Qt.AlignCenter)
        cleanup_layout.addWidget(self.status_label)
        
        main_layout.addWidget(cleanup_group)
        
        # Results
        results_group = QGroupBox("Results")
        results_layout = QVBoxLayout(results_group)
        
        self.results_text = QTextEdit()
        self.results_text.setMaximumHeight(100)
        self.results_text.setReadOnly(True)
        results_layout.addWidget(self.results_text)
        
        main_layout.addWidget(results_group)
        
        # Set initial state
        self.update_ui_state()
        
    def select_target(self):
        """Select the target drive or directory"""
        target = QFileDialog.getExistingDirectory(
            self, 
            "Select Drive or Directory to Clean",
            "",
            QFileDialog.ShowDirsOnly
        )
        
        if target:
            self.target_path = Path(target)
            self.target_label.setText(str(self.target_path))
            self.update_ui_state()
    
    def update_ui_state(self):
        """Update UI state based on current conditions"""
        has_target = self.target_path is not None
        is_cleaning = self.cleanup_worker is not None and self.cleanup_worker.isRunning()
        
        self.cleanup_btn.setEnabled(has_target and not is_cleaning)
        
        if not has_target:
            self.status_label.setText("Please select a drive or directory first")
        elif is_cleaning:
            self.status_label.setText("Cleaning up Mac system files...")
        else:
            self.status_label.setText("Ready to clean up Mac system files")
    
    def start_cleanup(self):
        """Start the cleanup process"""
        if not self.target_path:
            QMessageBox.warning(self, "No Target Selected", "Please select a drive or directory first.")
            return
        
        # Clear previous results
        self.results_text.clear()
        
        # Start cleanup worker
        self.cleanup_worker = CleanupWorker(self.target_path)
        self.cleanup_worker.progress.connect(self.progress_bar.setValue)
        self.cleanup_worker.status.connect(self.update_status)
        self.cleanup_worker.finished.connect(self.on_cleanup_finished)
        self.cleanup_worker.error.connect(self.on_cleanup_error)
        
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.cleanup_worker.start()
        self.update_ui_state()
    
    def update_status(self, message):
        """Update status message and results"""
        self.status_label.setText(message)
        self.results_text.append(message)
        # Auto-scroll to bottom
        self.results_text.verticalScrollBar().setValue(
            self.results_text.verticalScrollBar().maximum()
        )
    
    def on_cleanup_finished(self, files_deleted, folders_cleaned):
        """Handle cleanup completion"""
        self.progress_bar.setVisible(False)
        self.update_ui_state()
        
        message = f"Cleanup completed!\n\nFiles deleted: {files_deleted}\nFolders cleaned: {folders_cleaned}"
        self.results_text.append(f"\n{message}")
        
        QMessageBox.information(
            self,
            "Cleanup Complete",
            f"Mac cleanup completed!\n\nFiles deleted: {files_deleted}\nFolders cleaned: {folders_cleaned}"
        )
    
    def on_cleanup_error(self, error_msg):
        """Handle cleanup error"""
        self.progress_bar.setVisible(False)
        self.update_ui_state()
        
        self.results_text.append(f"\nError: {error_msg}")
        
        QMessageBox.critical(
            self,
            "Cleanup Error",
            f"An error occurred during cleanup:\n{error_msg}"
        )

def main():
    """Main function"""
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("Mac Cleanup Utility")
    app.setApplicationVersion("1.0")
    
    # Create and show main window
    window = MacCleanupUtility()
    window.show()
    
    # Run application
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
