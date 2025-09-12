import tkinter as tk
from tkinter import ttk, filedialog, messagebox, Menu, simpledialog
import subprocess
import threading
import time
import os
import struct
from PIL import Image, ImageTk
import json
import numpy as np
import platform
import ctypes
import sys
import webbrowser

if platform.system() == "Windows":
    from ctypes import wintypes
import tempfile
import shutil
import re
import datetime

# Add this near the top, after imports
base_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(base_dir, 'assets')

def debug_print(message):
    """Print debug messages to help troubleshoot button issues."""
    print(f"DEBUG: {message}")

def get_platform_font(family="default", size=9, weight="normal"):
    """Get platform-appropriate font family."""
    if family == "default":
        if platform.system() == "Windows":
            return "Segoe UI"
        elif platform.system() == "Darwin":  # macOS
            return "SF Pro Display"
        else:  # Linux
            return "DejaVu Sans"
    return family

class Y1HelperApp(tk.Tk):
    def __init__(self):
        super().__init__()
        debug_print("Initializing Y1HelperApp")
        
        # Set the custom icon for the application window
        # The .ico file must be in the same directory as the script
        try:
            icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'y1_helper.ico')
            if os.path.exists(icon_path):
                self.iconbitmap(icon_path)
            else:
                debug_print("y1_helper.ico not found, using default icon.")
        except tk.TclError as e:
            debug_print(f"Failed to set icon: {e}")
        
        # Base directory (for config file access)
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Assets directory (for PNG files)
        self.assets_dir = os.path.join(self.base_dir, 'assets')
        
        # Configuration file path
        self.config_file = os.path.join(self.base_dir, 'y1_helper_config.json')
        
        # Version information
        self.version = "1.5.0"
        
        # Write version.txt file
        self.write_version_file()
        
        # Load configuration
        self.app_config = self.load_config()

        self.title(f"Y1 Remote Control v{self.version} - created by Ryan Specter - u/respectyarn")
        self.geometry("452x661")
        self.resizable(False, False)
        
        # Ensure window gets focus and appears in front
        self.lift()
        self.attributes('-topmost', True)
        self.after(100, lambda: self.attributes('-topmost', False))
        self.focus_force()
        
        # Center window on screen
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (452 // 2)
        y = (self.winfo_screenheight() // 2) - (661 // 2)
        self.geometry(f"452x661+{x}+{y}")
        
        # Detect Windows 11 theme
        self.setup_windows_11_theme()
        self.apply_theme_colors()
        
        # Device configuration
        self.device_width = 480
        self.device_height = 360
        self.framebuffer_size = self.device_width * self.device_height * 4  # RGBA8888
        
        # Display scaling (75% of original size)
        self.display_scale = 0.75
        self.display_width = int(self.device_width * self.display_scale)  # 360
        self.display_height = int(self.device_height * self.display_scale)  # 270
        
        # State variables
        self.is_capturing = True  # Always capturing
        self.capture_thread = None
        self.current_app = None
        self.control_launcher = False
        self.last_screen_image = None
        self.device_connected = False
        
        # Essential UI variables
        self.status_var = tk.StringVar(value="Ready")
        self.scroll_wheel_mode_var = tk.BooleanVar()
        self.disable_dpad_swap_var = tk.BooleanVar()
        self.rgb_profile_var = tk.StringVar(value="BGRA8888")
        
        # Add input pacing: minimum delay between input events (in seconds)
        self.input_pacing_interval = 0.1  # 100ms
        self.last_input_time = 0
        
        # Scroll cursor variables
        self.scroll_cursor_active = False
        self.scroll_cursor_timer = None
        self.scroll_cursor_duration = 25
        
        # Performance optimization variables
        self.framebuffer_refresh_interval = 4.0
        self.last_framebuffer_refresh = 0
        self.unified_check_interval = 10
        self.last_unified_check = 0
        self.app_detection_interval = 10
        self.last_app_detection = 0
        self.force_refresh_requested = False
        
        # Activity detection variables
        self.last_user_activity = time.time()
        self.inactivity_threshold = 10.0
        self.slow_refresh_interval = 20.0
        self.last_app_change = time.time()
        self.current_app_package = None
        
        # Device state tracking
        self.device_stay_awake_set = False
        self.last_blank_screen_detection = 0
        self.blank_screen_threshold = 0.01
        
        # Input mode persistence
        self.manual_mode_override = False
        self.last_manual_mode_change = time.time()
        
        debug_print("Setting up UI components")
        # Initialize UI
        self.setup_ui()
        self.setup_menu()
        self.setup_bindings()
        
        debug_print("Checking ADB connection")
        # Check ADB connection
        self.unified_device_check()
        
        # Show placeholder if no device connected
        if not hasattr(self, 'device_connected') or not self.device_connected:
            debug_print("No device connected, showing ready placeholder")
            self.show_ready_placeholder()
            self.hide_controls_frame()
            self.disable_input_bindings()
        else:
            self.show_controls_frame()
            self.enable_input_bindings()
        
        # Set device to stay awake while charging
        self.set_device_stay_awake()
        
        if self.device_connected:
            self.detect_current_app()
        
        # Start screen capture immediately
        self.start_screen_capture()
        debug_print("Y1HelperApp initialization complete")

    def load_config(self):
        """Load configuration from JSON file."""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            debug_print(f"Failed to load config: {e}")
        return {}
    
    def save_config(self, config):
        """Save configuration to JSON file."""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            debug_print(f"Config saved: {self.config_file}")
        except Exception as e:
            debug_print(f"Failed to save config: {e}")
    
    def write_version_file(self):
        try:
            version_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "version.txt")
            with open(version_file_path, 'w', encoding='utf-8') as f:
                f.write(f"{self.version}\n")
            debug_print(f"Version file written: {version_file_path}")
        except Exception as e:
            debug_print(f"Failed to write version file: {e}")

    def setup_windows_11_theme(self):
        debug_print("Setting up Windows 11 theme")
        try:
            if platform.system() == "Windows":
                self.is_dark_mode = self.detect_system_theme()
                debug_print(f"System theme detected: {'Dark' if self.is_dark_mode else 'Light'}")
                self.apply_theme_colors()
                self.setup_theme_change_detection()
                debug_print("Windows 11 theme setup complete")
            else:
                debug_print("Not on Windows, using default theme")
                self.is_dark_mode = False
                self.apply_theme_colors()
        except Exception as e:
            debug_print(f"Theme setup failed: {e}")
            self.is_dark_mode = False
            self.apply_theme_colors()

    def detect_system_theme(self):
        if platform.system() != "Windows":
            return False
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
            value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
            winreg.CloseKey(key)
            return value == 0
        except Exception as e:
            debug_print(f"Could not detect system theme: {e}")
            return False

    def apply_theme_colors(self):
        debug_print(f"Applying {'dark' if self.is_dark_mode else 'light'} theme colors")
        if self.is_dark_mode:
            self.bg_color, self.fg_color, self.accent_color, self.secondary_bg, self.border_color = "#202020", "#ffffff", "#0078d4", "#2b2b2b", "#404040"
            self.menu_bg, self.menu_fg, self.menu_select_bg, self.menu_select_fg = "#202020", "#ffffff", "#0078d4", "#ffffff"
            self.button_bg, self.button_fg, self.button_active_bg, self.button_active_fg = "#2b2b2b", "#ffffff", "#0078d4", "#ffffff"
        else:
            self.bg_color, self.fg_color, self.accent_color, self.secondary_bg, self.border_color = "#ffffff", "#000000", "#0078d4", "#f3f3f3", "#e0e0e0"
            self.menu_bg, self.menu_fg, self.menu_select_bg, self.menu_select_fg = "#ffffff", "#000000", "#0078d4", "#ffffff"
            self.button_bg, self.button_fg, self.button_active_bg, self.button_active_fg = "#f3f3f3", "#000000", "#0078d4", "#ffffff"
        
        self.configure(bg=self.bg_color)
        
        if platform.system() == "Windows":
            try:
                hwnd = self.winfo_id()
                if hwnd:
                    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
                    ctypes.windll.dwmapi.DwmSetWindowAttribute(hwnd, DWMWA_USE_IMMERSIVE_DARK_MODE, ctypes.byref(ctypes.c_bool(self.is_dark_mode)), ctypes.sizeof(ctypes.c_bool))
                    debug_print(f"Applied Windows 11 {'dark' if self.is_dark_mode else 'light'} title bar to hwnd: {hwnd}")
            except Exception as e:
                debug_print(f"Could not apply Windows 11 title bar theme: {e}")
        
        style = ttk.Style()
        try:
            style.theme_use('clam')
        except:
            pass
        
        style.configure(".", background=self.bg_color, foreground=self.fg_color, fieldbackground=self.secondary_bg, troughcolor=self.secondary_bg, selectbackground=self.accent_color, selectforeground=self.fg_color, bordercolor=self.border_color, lightcolor=self.border_color, darkcolor=self.border_color, focuscolor=self.accent_color)
        style.configure("TFrame", background=self.bg_color, relief="flat", borderwidth=0)
        style.configure("TLabel", background=self.bg_color, foreground=self.fg_color, font=(get_platform_font(), 9))
        style.configure("TButton", background=self.button_bg, foreground=self.button_fg, bordercolor=self.border_color, focuscolor=self.accent_color, font=(get_platform_font(), 9))
        style.map("TButton", background=[("active", self.button_active_bg), ("pressed", self.button_active_bg)], foreground=[("active", self.button_active_fg), ("pressed", self.button_active_fg)])
        style.configure("TCheckbutton", background=self.bg_color, foreground=self.fg_color, font=(get_platform_font(), 9))
        style.map("TCheckbutton", background=[("active", self.bg_color)], foreground=[("active", self.fg_color)])
        style.configure("TLabelframe", background=self.bg_color, foreground=self.fg_color, bordercolor=self.border_color, font=(get_platform_font(), 9))
        style.configure("TLabelframe.Label", background=self.bg_color, foreground=self.fg_color, font=(get_platform_font(), 9, "bold"))
        style.configure("TMenubar", background=self.menu_bg, foreground=self.menu_fg)
        style.configure("TMenu", background=self.menu_bg, foreground=self.menu_fg)
        
        self.apply_menu_colors()
        self.update_widget_colors()
        debug_print("Theme colors applied with modern styling")

    def update_widget_colors(self):
        debug_print("Updating widget colors")
        try:
            self.configure(bg=self.bg_color)
            self._update_widget_tree(self)
            debug_print("Widget colors updated")
        except Exception as e:
            debug_print(f"Failed to update widget colors: {e}")

    def _update_widget_tree(self, widget):
        try:
            if hasattr(widget, 'configure'):
                widget.configure(bg=self.bg_color, fg=self.fg_color)
            if isinstance(widget, tk.Label):
                widget.configure(bg=self.bg_color, fg=self.fg_color, font=(get_platform_font(), 9))
            elif isinstance(widget, tk.Button):
                widget.configure(bg=self.button_bg, fg=self.button_fg, activebackground=self.button_active_bg, activeforeground=self.button_active_fg, font=(get_platform_font(), 9), relief="flat", bd=1)
            elif isinstance(widget, tk.Checkbutton):
                widget.configure(bg=self.bg_color, fg=self.fg_color, selectcolor=self.bg_color, font=(get_platform_font(), 9))
            elif isinstance(widget, tk.Frame):
                widget.configure(bg=self.bg_color, relief="flat", bd=0)
            elif isinstance(widget, tk.LabelFrame):
                widget.configure(bg=self.bg_color, fg=self.fg_color, font=(get_platform_font(), 9, "bold"), relief="flat", bd=1)
            for child in widget.winfo_children():
                self._update_widget_tree(child)
        except Exception as e:
            debug_print(f"Failed to update widget {widget}: {e}")

    def apply_menu_colors(self):
        debug_print("Applying menu colors")
        try:
            menu_config = {'bg': self.menu_bg, 'fg': self.menu_fg, 'activebackground': self.menu_select_bg, 'activeforeground': self.menu_select_fg, 'selectcolor': self.menu_bg, 'relief': 'flat', 'bd': 0}
            if hasattr(self, 'device_menu'): self.device_menu.configure(**menu_config)
            if hasattr(self, 'apps_menu'): self.apps_menu.configure(**menu_config)
            if hasattr(self, 'context_menu'): self.context_menu.configure(**menu_config)
            debug_print("Menu colors applied")
        except Exception as e:
            debug_print(f"Failed to apply menu colors: {e}")

    def setup_theme_change_detection(self):
        def check_theme_change():
            try:
                new_dark_mode = self.detect_system_theme()
                if new_dark_mode != self.is_dark_mode:
                    debug_print(f"System theme changed to {'dark' if new_dark_mode else 'light'}")
                    self.is_dark_mode = new_dark_mode
                    self.apply_theme_colors()
                    self.update_controls_display()
            except Exception as e:
                debug_print(f"Theme change detection error: {e}")
            self.after(5000, check_theme_change)
        self.after(5000, check_theme_change)

    def get_adb_path(self):
        """Get ADB path based on platform. For Windows, use assets directory. For macOS/Linux, try system paths first."""
        if platform.system() == "Windows":
            # Windows: use adb.exe from assets directory
            adb_path = os.path.join(assets_dir, "adb.exe")
            if os.path.exists(adb_path):
                return adb_path
            else:
                # Fallback to system PATH
                return "adb"
        else:
            # macOS and Linux: try common installation paths
            common_paths = [
                "adb",  # System PATH
                "/usr/local/bin/adb",  # Homebrew (macOS)
                "/opt/homebrew/bin/adb",  # Apple Silicon Homebrew
                "/usr/bin/adb",  # System-wide installation
                "/opt/android-sdk/platform-tools/adb",  # Android SDK
                os.path.expanduser("~/Library/Android/sdk/platform-tools/adb"),  # macOS Android Studio
                os.path.expanduser("~/Android/Sdk/platform-tools/adb"),  # Linux Android Studio
                os.path.expanduser("~/android-sdk/platform-tools/adb"),  # User Android SDK
            ]
            
            for path in common_paths:
                if path == "adb":
                    # Check if adb is in PATH
                    try:
                        if platform.system() == "Windows":
                            # Windows: use where command
                            result = subprocess.run(["where", "adb"], capture_output=True, text=True, timeout=5)
                        else:
                            # macOS/Linux: use which command
                            result = subprocess.run(["which", "adb"], capture_output=True, text=True, timeout=5)
                        if result.returncode == 0:
                            return path
                    except:
                        continue
                elif os.path.exists(path) and os.access(path, os.X_OK):
                    return path
            
            # If no ADB found, return None to trigger installation dialog
            return None

    def setup_ui(self):
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        screen_frame = ttk.LabelFrame(main_frame, text="Mouse Input Panel (480x360)", padding=5)
        screen_frame.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        
        # Use appropriate cursor for each platform
        if platform.system() == "Windows":
            default_cursor = "hand2"
        else:
            # macOS and Linux don't have hand2 cursor, use default
            default_cursor = ""
        
        self.screen_canvas = tk.Canvas(screen_frame, width=self.display_width, height=self.display_height, bg='black', cursor=default_cursor, highlightthickness=0, bd=0, relief="flat")
        self.screen_canvas.pack()
        self.screen_canvas.config(width=self.display_width, height=self.display_height)
        
        self.controls_frame = ttk.LabelFrame(screen_frame, text="Controls", padding=3)
        self.controls_frame.pack(fill=tk.X, pady=(5, 0))
        
        self.controls_label = ttk.Label(self.controls_frame, text="", justify=tk.LEFT, font=(get_platform_font(), 8))
        self.controls_label.pack(anchor="w")
        
        mode_frame = ttk.Frame(self.controls_frame)
        mode_frame.pack(fill=tk.X, pady=(3, 0))
        
        # Create buttons with proper error handling and fallback to tk.Button if ttk fails
        debug_print("Creating input_mode_btn...")
        try:
            self.input_mode_btn = ttk.Button(mode_frame, text="Touch Screen Mode", command=self.toggle_scroll_wheel_mode, style="TButton")
            debug_print("input_mode_btn created successfully with ttk")
        except Exception as e:
            debug_print(f"ttk.Button failed, using tk.Button: {e}")
            self.input_mode_btn = tk.Button(mode_frame, text="Touch Screen Mode", command=self.toggle_scroll_wheel_mode,
                                            bg=self.button_bg, fg=self.button_fg, activebackground=self.button_active_bg,
                                            activeforeground=self.button_active_fg, font=(get_platform_font(), 9), relief="flat", bd=1)
            debug_print("input_mode_btn created successfully with tk.Button")
        self.input_mode_btn.pack(side=tk.LEFT, anchor="w")
        
        try:
            self.screenshot_btn = ttk.Button(mode_frame, text="📸 Screenshot", command=self.take_screenshot, style="TButton")
        except Exception as e:
            debug_print(f"ttk.Button failed, using tk.Button: {e}")
            self.screenshot_btn = tk.Button(mode_frame, text="📸 Screenshot", command=self.take_screenshot,
                                         bg=self.button_bg, fg=self.button_fg, activebackground=self.button_active_bg,
                                         activeforeground=self.button_active_fg, font=(get_platform_font(), 9), relief="flat", bd=1)
        self.screenshot_btn.pack(side=tk.LEFT, padx=(10, 0), anchor="w")
        
        try:
            self.disable_swap_checkbox = ttk.Checkbutton(mode_frame, text="Disable D-pad Swap", variable=self.disable_dpad_swap_var, command=self.update_controls_display, style="TCheckbutton")
        except Exception as e:
            debug_print(f"ttk.Checkbutton failed, using tk.Checkbutton: {e}")
            self.disable_swap_checkbox = tk.Checkbutton(mode_frame, text="Disable D-pad Swap", variable=self.disable_dpad_swap_var, command=self.update_controls_display,
                                                        bg=self.bg_color, fg=self.fg_color, font=(get_platform_font(), 9))
        self.disable_swap_checkbox.pack(side=tk.LEFT, padx=(10, 0), anchor="w")
        self.disable_swap_checkbox.pack_forget()
        
        self._add_tooltip(self.input_mode_btn, "Input Mode: Click to switch between Touch Screen Mode and Scroll Wheel Mode.")
        self._add_tooltip(self.screenshot_btn, "Screenshot: Capture the current device screen and save it to a file.")
        self._add_tooltip(self.disable_swap_checkbox, "When checked, disables the D-pad swap in Scroll Wheel Mode.")
        
        status_frame = ttk.Frame(main_frame)
        status_frame.pack(fill=tk.X, pady=(10, 0))
        
        status_label = ttk.Label(status_frame, textvariable=self.status_var, relief="flat", borderwidth=1, padding=(8, 4), font=(get_platform_font(), 9))
        status_label.pack(fill=tk.X, side=tk.LEFT, expand=True)
        
        self.after(100, lambda: self.screen_canvas.focus_set())
        
        self.screen_canvas.bind("<Button-1>", self.on_screen_click)
        self.screen_canvas.bind("<Button-3>", self.on_screen_right_click)
        self.screen_canvas.bind("<Button-2>", self.on_mouse_wheel_click)
        self.screen_canvas.bind("<MouseWheel>", self.on_mouse_wheel)
        self.screen_canvas.bind("<Button-4>", self.on_mouse_wheel)
        self.screen_canvas.bind("<Button-5>", self.on_mouse_wheel)
        
        self.update_controls_display()
        
        self.context_menu = Menu(self, tearoff=0, bg=self.menu_bg, fg=self.menu_fg, activebackground=self.menu_select_bg, activeforeground=self.menu_select_fg, relief="flat", bd=0)
        self.context_menu.add_command(label="Go Home", command=self.go_home)
        self.context_menu.add_command(label="Open Settings", command=self.launch_settings)
        self.context_menu.add_command(label="Recent Apps", command=self.show_recent_apps)
        
        if hasattr(self, 'apply_menu_colors'):
            self.apply_menu_colors()
        
        self.hide_controls_frame()
        self.input_disabled = True
    
    def launch_rockbox_utility(self):
        """Shows Rockbox theme installation instructions and launches Rockbox Utility."""
        # Load configuration to check if dialog should be shown
        config = self.load_config()
        show_dialog = config.get('show_rockbox_dialog', True)
        
        if show_dialog:
            # Create custom dialog with instructions and checkbox
            dialog = tk.Toplevel(self)
            dialog.title("Rockbox Theme Installation Instructions")
            dialog.geometry("600x500")
            dialog.resizable(False, False)
            dialog.transient(self)
            dialog.grab_set()
            
            # Center dialog on screen
            dialog.update_idletasks()
            x = (self.winfo_screenwidth() // 2) - (600 // 2)
            y = (self.winfo_screenheight() // 2) - (500 // 2)
            dialog.geometry(f"600x500+{x}+{y}")
            
            # Apply theme colors
            dialog.configure(bg=self.bg_color)
            
            # Instructions text
            instructions_text = """To install themes with Rockbox:

1. Turn on USB storage mode on your Y1 device
2. Connect it to your computer via USB cable
3. In Rockbox Utility, configure your device as:
   • iPod Video, OR
   • iPod Classic 6G
4. Make sure to check ONLY:
   • Themes
   • Fonts
5. Click "Customize" then "Install" in Rockbox Utility

This will install your themes and fonts to the device."""
            
            # Create text widget with instructions
            text_frame = tk.Frame(dialog, bg=self.bg_color)
            text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(20, 10))
            
            text_widget = tk.Text(text_frame, wrap=tk.WORD, bg=self.secondary_bg, fg=self.fg_color, 
                                 font=(get_platform_font(), 10), relief="flat", bd=0, padx=15, pady=15)
            text_widget.pack(fill=tk.BOTH, expand=True)
            text_widget.insert(tk.END, instructions_text)
            text_widget.config(state=tk.DISABLED)
            
            # Checkbox for "do not show again"
            checkbox_var = tk.BooleanVar()
            checkbox_frame = tk.Frame(dialog, bg=self.bg_color)
            checkbox_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
            
            checkbox = tk.Checkbutton(checkbox_frame, text="Do not show this dialog again", 
                                     variable=checkbox_var, bg=self.bg_color, fg=self.fg_color,
                                     selectcolor=self.bg_color, font=(get_platform_font(), 9))
            checkbox.pack(anchor="w")
            
            # Buttons
            button_frame = tk.Frame(dialog, bg=self.bg_color)
            button_frame.pack(fill=tk.X, padx=20, pady=(0, 20))
            
            ok_button = tk.Button(button_frame, text="OK", command=lambda: self.handle_rockbox_dialog_ok(dialog, checkbox_var.get()), 
                                 bg=self.button_bg, fg=self.button_fg, activebackground=self.button_active_bg, 
                                 activeforeground=self.button_active_fg, font=(get_platform_font(), 9), relief="flat", bd=1)
            ok_button.pack(side=tk.RIGHT, padx=(10, 0))
            
            cancel_button = tk.Button(button_frame, text="Cancel", command=dialog.destroy,
                                     bg=self.button_bg, fg=self.button_fg, activebackground=self.button_active_bg, 
                                     activeforeground=self.button_active_fg, font=(get_platform_font(), 9), relief="flat", bd=1)
            cancel_button.pack(side=tk.RIGHT)
            
            # Focus on OK button
            ok_button.focus_set()
            
            # Bind Enter key to OK button
            dialog.bind("<Return>", lambda e: self.handle_rockbox_dialog_ok(dialog, checkbox_var.get()))
            dialog.bind("<Escape>", lambda e: dialog.destroy())
            
        else:
            # Skip dialog and launch directly
            self.launch_rockbox_utility_direct()
    
    def handle_rockbox_dialog_ok(self, dialog, do_not_show_again):
        """Handle OK button click from Rockbox dialog."""
        # Save configuration if checkbox is checked
        if do_not_show_again:
            config = self.load_config()
            config['show_rockbox_dialog'] = False
            self.save_config(config)
        
        # Close dialog
        dialog.destroy()
        
        # Launch Rockbox Utility and close Y1 Helper
        self.launch_rockbox_utility_direct()
        self.terminate_process()
    
    def launch_rockbox_utility_direct(self):
        """Directly launches Rockbox Utility from start menu or assets."""
        try:
            if platform.system() == "Windows":
                # Windows: try to launch from start menu
                start_menu_path = os.path.join(os.environ.get('APPDATA', ''), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Rockbox Utility.lnk')
                
                if os.path.exists(start_menu_path):
                    subprocess.Popen(['cmd', '/c', 'start', '', start_menu_path])
                    self.status_var.set("Rockbox Utility launched")
                else:
                    # Fallback: try to run from assets directory
                    rockbox_path = os.path.join(self.assets_dir, "RockboxUtility.exe")
                    if os.path.exists(rockbox_path):
                        subprocess.Popen([rockbox_path])
                        self.status_var.set("Rockbox Utility launched")
                    else:
                        messagebox.showerror("Error", "Rockbox Utility not found in start menu or assets directory.")
            else:
                # macOS and Linux: open Rockbox download page
                webbrowser.open_new_tab("https://www.rockbox.org/download")
                self.status_var.set("Opened Rockbox download page")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch Rockbox Utility: {e}")
    
    # Removed the run_updater_and_exit and launch_updater_and_exit functions
    # as they are no longer needed for the "Install Firmware" button.
    
    def on_close(self):
        """Handle application close event."""
        debug_print("on_close called")
        self.is_capturing = False
        self.stop_threads()
        if self.device_connected:
            self.set_device_stay_awake(False)
        self.destroy()
    
    def stop_threads(self):
        debug_print("Stopping threads...")
        self.is_capturing = False
        if self.capture_thread and self.capture_thread.is_alive():
            self.capture_thread.join(timeout=2)
            if self.capture_thread.is_alive():
                debug_print("Capture thread did not stop gracefully.")
        debug_print("Threads stopped.")
    
    def terminate_process(self):
        debug_print("Terminating process.")
        sys.exit(0)
    
    def show_ready_placeholder(self):
        debug_print("Showing ready placeholder")
        try:
            placeholder_path = os.path.join(self.assets_dir, "ready.png")
            if os.path.exists(placeholder_path):
                img = Image.open(placeholder_path)
                photo_img = ImageTk.PhotoImage(img)
                self.screen_canvas.create_image(0, 0, anchor=tk.NW, image=photo_img)
                self.screen_canvas.image = photo_img
                self.screen_canvas.config(width=img.width, height=img.height)
            else:
                debug_print("Placeholder image not found.")
                self.screen_canvas.create_text(self.display_width / 2, self.display_height / 2,
                                              text="Waiting for device...", fill="white",
                                              font=(get_platform_font(), 16))
        except Exception as e:
            debug_print(f"Failed to show placeholder: {e}")
            self.screen_canvas.create_text(self.display_width / 2, self.display_height / 2,
                                          text="Waiting for device...", fill="white",
                                          font=(get_platform_font(), 16))
    
    def hide_controls_frame(self):
        self.controls_frame.pack_forget()
        self.update_controls_display()

    def show_controls_frame(self):
        self.controls_frame.pack(fill=tk.X, pady=(5, 0))
        self.update_controls_display()

    def unified_device_check(self):
        # ... (rest of the code) ...
        self.after(5000, self.unified_device_check)
    
    def start_screen_capture(self):
        # ... (rest of the code) ...
        self.capture_thread = threading.Thread(target=self.capture_screen, daemon=True)
        self.capture_thread.start()
        
    def capture_screen(self):
        # ... (rest of the code) ...
    
    def update_screen(self, img):
        # ... (rest of the code) ...
    
    def get_framebuffer(self):
        # ... (rest of the code) ...
    
    def get_current_app(self):
        # ... (rest of the code) ...
    
    def detect_current_app(self):
        # ... (rest of the code) ...
    
    def set_device_stay_awake(self, awake=True):
        # ... (rest of the code) ...
    
    def toggle_scroll_wheel_mode(self):
        # ... (rest of the code) ...
    
    def _add_tooltip(self, widget, text):
        # ... (rest of the code) ...
    
    def _show_tooltip(self, event, widget, text):
        # ... (rest of the code) ...
    
    def _hide_tooltip(self, event):
        # ... (rest of the code) ...
    
    def on_screen_click(self, event):
        # ... (rest of the code) ...
    
    def on_screen_right_click(self, event):
        # ... (rest of the code) ...
    
    def on_mouse_wheel(self, event):
        # ... (rest of the code) ...
    
    def on_mouse_wheel_click(self, event):
        # ... (rest of the code) ...
    
    def on_key_press(self, event):
        # ... (rest of the code) ...
    
    def on_key_release(self, event):
        # ... (rest of the code) ...
    
    def send_input_event(self, event_type, value):
        # ... (rest of the code) ...
    
    def update_controls_display(self):
        # ... (rest of the code) ...
    
    def handle_launcher_mode(self):
        # ... (rest of the code) ...
    
    def is_launcher_running(self, package_name):
        # ... (rest of the code) ...
    
    def disable_input_bindings(self):
        # ... (rest of the code) ...
    
    def enable_input_bindings(self):
        # ... (rest of the code) ...
    
    def go_home(self):
        # ... (rest of the code) ...
    
    def launch_settings(self):
        # ... (rest of the code) ...
    
    def take_screenshot(self):
        # ... (rest of the code) ...
    
    def show_recent_apps(self):
        # ... (rest of the code) ...
    
    def setup_bindings(self):
        self.bind("<Alt_L>", self.toggle_launcher_control)
        self.bind("<Alt_R>", self.toggle_launcher_control)
        self.bind_all("<Key>", self.on_key_press)
        self.bind_all("<KeyRelease>", self.on_key_release)

if __name__ == "__main__":
    print("You can minimise this window and use remote control and app install features")
    app = Y1HelperApp()
    app.protocol("WM_DELETE_WINDOW", app.on_close)
    app.mainloop()
