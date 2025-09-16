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
        
        # Install Firmware button removed
        
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
    
    # launch_rockbox_utility method removed
    
    # handle_rockbox_dialog_ok method removed
    
    # launch_rockbox_utility_direct method removed
    
    # run_updater_and_exit method removed

    def launch_updater_and_exit(self):
        """Launches updater.py with --force flag and closes Y1 Helper GUI."""
        try:
            updater_path = os.path.join(self.base_dir, "updater.py")
            if os.path.exists(updater_path):
                # Launch updater.py with --force flag
                if platform.system() == "Windows":
                    # Windows: use pythonw.exe if available
                    pythonw_path = os.path.join(self.base_dir, "pythonw.exe")
                    if os.path.exists(pythonw_path):
                        subprocess.Popen([pythonw_path, updater_path, "--force"])
                    else:
                        # Fallback to regular python
                        subprocess.Popen([sys.executable, updater_path, "--force"])
                else:
                    # macOS/Linux: use sys.executable
                    subprocess.Popen([sys.executable, updater_path, "--force"])
                
                self.status_var.set("Launching Innioasis Updater...")
                self.update_idletasks()
                
                # Close the GUI after a short delay
                self.after(1000, self.terminate_process)
            else:
                messagebox.showerror("Error", "updater.py not found. Please ensure it is properly installed.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to launch updater.py: {e}")
    
    def terminate_process(self):
        """Terminates the Y1 Helper process completely."""
        try:
            # Close the GUI
            self.destroy()
            # Force terminate the process
            os._exit(0)
        except:
            # If destroy fails, force exit
            os._exit(0)

    def hide_controls_frame(self):
        if hasattr(self, 'controls_frame'):
            self.controls_frame.pack_forget()

    def show_controls_frame(self):
        if hasattr(self, 'controls_frame'):
            self.controls_frame.pack(fill=tk.X, pady=(5, 0))

    def disable_input_bindings(self):
        if hasattr(self, 'screen_canvas'):
            self.screen_canvas.unbind("<Button-1>")
            self.screen_canvas.unbind("<Button-3>")
            self.screen_canvas.unbind("<MouseWheel>")
            self.screen_canvas.unbind("<Button-2>")
            self.unbind_all("<Key>")
            self.unbind_all("<KeyRelease>")
            self.bind("<Alt_L>", self.toggle_launcher_control)
            self.bind("<Alt_R>", self.toggle_launcher_control)
            self.input_disabled = True

    def enable_input_bindings(self):
        if hasattr(self, 'screen_canvas'):
            self.screen_canvas.bind("<Button-1>", self.on_screen_click)
            self.screen_canvas.bind("<Button-3>", self.on_screen_right_click)
            self.screen_canvas.bind("<MouseWheel>", self.on_mouse_wheel)
            self.screen_canvas.bind("<Button-2>", self.on_mouse_wheel_click)
            self.bind_all("<Key>", self.on_key_press)
            self.bind_all("<KeyRelease>", self.on_key_release)
            self.input_disabled = False
            self.ready_placeholder_shown = False
            
            # Set appropriate cursor based on current mode and platform
            if not self.scroll_wheel_mode_var.get():
                if platform.system() == "Windows":
                    self.screen_canvas.config(cursor="hand2")
                else:
                    # macOS and Linux don't have hand2 cursor, use default
                    self.screen_canvas.config(cursor="")

    def update_controls_display(self):
        if self.scroll_wheel_mode_var.get():
            if self.disable_dpad_swap_var.get():
                controls_text = "Scroll Wheel Mode (D-pad Swap Disabled):\nTouch: Left Click | Back: Right Click\nD-pad: W/A/S/D or Arrow Keys\nEnter: Wheel Click, Enter, E"
            else:
                controls_text = "Scroll Wheel Mode:\nTouch: Left Click | Back: Right Click\nScroll: W/S or Up/Down -> DPAD_LEFT/RIGHT\nD-pad: A/D or Left/Right -> DPAD_UP/DOWN\nEnter: Wheel Click, Enter, E -> ENTER"
        else:
            controls_text = "Touch Screen Mode:\nTouch: Left Click | Back: Right Click\nD-pad: W/A/S/D or Arrow Keys\nEnter: Wheel Click, Enter, E -> DPAD_CENTER"
        self.controls_label.config(text=controls_text)

    def toggle_scroll_wheel_mode(self):
        debug_print("toggle_scroll_wheel_mode called")
        try:
            is_scroll_wheel_mode = not self.scroll_wheel_mode_var.get()
            self.scroll_wheel_mode_var.set(is_scroll_wheel_mode)
            self.control_launcher = is_scroll_wheel_mode
            self.manual_mode_override = True
            self.last_manual_mode_change = time.time()
            
            if is_scroll_wheel_mode:
                self.input_mode_btn.config(text="Scroll Wheel Mode")
                self.disable_swap_checkbox.pack(side=tk.LEFT, padx=(10, 0), anchor="w")
                self.status_var.set("Scroll Wheel Mode enabled")
                if not self.ready_placeholder_shown:
                    self.screen_canvas.config(cursor="")
            else:
                self.input_mode_btn.config(text="Touch Screen Mode")
                self.disable_swap_checkbox.pack_forget()
                self.status_var.set("Touch Screen Mode enabled")
                if not self.ready_placeholder_shown:
                    # Use appropriate cursor for each platform
                    if platform.system() == "Windows":
                        self.screen_canvas.config(cursor="hand2")
                    else:
                        # macOS and Linux don't have hand2 cursor, use default
                        self.screen_canvas.config(cursor="")
            
            self.update_controls_display()
        except Exception as e:
            debug_print(f"Error in toggle_scroll_wheel_mode: {e}")
            messagebox.showerror("Error", f"Failed to toggle mode: {e}")

    def toggle_launcher_control(self, event=None):
        self.scroll_wheel_mode_var.set(not self.scroll_wheel_mode_var.get())
        self.toggle_scroll_wheel_mode()

    def setup_menu(self):
        menubar = Menu(self)
        self.config(menu=menubar)
        
        device_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Device", menu=device_menu)
        self.device_menu = device_menu
        
        device_menu.add_command(label="Device Info", command=self.show_device_info)
        device_menu.add_command(label="ADB Shell", command=self.open_adb_shell)
        device_menu.add_command(label="Take Screenshot", command=self.take_screenshot)
        device_menu.add_command(label="Recent Apps", command=self.show_recent_apps)
        device_menu.add_command(label="Change Device Language", command=self.change_device_language)
        
        self.apps_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Apps", menu=self.apps_menu)
        self.apps_menu.add_command(label="Browse APKs...", command=self.browse_apks)
        self.apps_menu.add_separator()
        self.refresh_apps()
        
        help_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        self.help_menu = help_menu
        
        help_menu.add_command(label="Getting Started", command=lambda: webbrowser.open_new_tab("https://troubleshooting.innioasis.app"))
        help_menu.add_separator()
        help_menu.add_command(label="r/innioasis", command=lambda: webbrowser.open_new_tab("https://www.reddit.com/r/innioasis"))
        help_menu.add_command(label="Buy Us Coffee", command=lambda: webbrowser.open_new_tab("https://ko-fi.com/teamslide"))
        
        self.apply_menu_colors()

    def refresh_apps(self):
        # Check if apps_menu is properly initialized
        if not hasattr(self, 'apps_menu') or not self.apps_menu:
            return
            
        # Preserve the static menu items
        try:
            while self.apps_menu.index('end') is not None and self.apps_menu.index('end') > 0:
                if self.apps_menu.type(self.apps_menu.index('end')) == 'separator':
                    break
                self.apps_menu.delete(self.apps_menu.index('end'))
        except Exception as e:
            debug_print(f"Error clearing apps menu: {e}")
            return

        success, stdout, stderr = self.run_adb_command("shell pm list packages -3 -f")
        apps = []
        if success:
            for line in stdout.strip().split('\n'):
                if line.startswith('package:'):
                    package_name = line.split('=')[-1]
                    apps.append(package_name)
        
        if not apps:
            self.apps_menu.add_command(label="No user apps installed", state="disabled")
        else:
            for app in sorted(apps):
                app_menu = Menu(self.apps_menu, tearoff=0)
                app_menu.add_command(label="Launch", command=lambda a=app: self.launch_app(a))
                app_menu.add_command(label="Uninstall", command=lambda a=app: self.uninstall_app(a))
                self.apps_menu.add_cascade(label=app, menu=app_menu)
                if hasattr(self, 'menu_bg'):
                    app_menu.configure(bg=self.menu_bg, fg=self.menu_fg, activebackground=self.menu_select_bg, activeforeground=self.menu_select_fg, relief='flat', bd=0)

    def check_adb_availability(self):
        """Check if ADB is available and show installation dialog if needed."""
        adb_path = self.get_adb_path()
        if adb_path is None:
            # ADB not found - show installation dialog for non-Windows users
            if platform.system() != "Windows":
                self.show_adb_installation_dialog()
            return False
        return True
    
    def show_adb_installation_dialog(self):
        """Show dialog explaining how to install ADB on macOS/Linux."""
        dialog = tk.Toplevel(self)
        dialog.title("ADB Installation Required")
        dialog.geometry("700x600")
        dialog.resizable(False, False)
        dialog.transient(self)
        dialog.grab_set()
        
        # Center dialog on screen
        dialog.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (700 // 2)
        y = (self.winfo_screenheight() // 2) - (600 // 2)
        dialog.geometry(f"700x600+{x}+{y}")
        
        # Apply theme colors
        dialog.configure(bg=self.bg_color)
        
        # Title
        title_label = tk.Label(dialog, text="Android Debug Bridge (ADB) Required", 
                              font=(get_platform_font(), 14, "bold"), bg=self.bg_color, fg=self.fg_color)
        title_label.pack(pady=(20, 10))
        
        # Instructions text
        instructions_text = """Y1 Remote Control requires ADB (Android Debug Bridge) to communicate with your device.

To install ADB on your system:"""
        
        instructions_label = tk.Label(dialog, text=instructions_text, 
                                    font=(get_platform_font(), 10), bg=self.bg_color, fg=self.fg_color,
                                    justify=tk.LEFT, wraplength=650)
        instructions_label.pack(pady=(0, 20), padx=20)
        
        # Platform-specific instructions
        if platform.system() == "Darwin":  # macOS
            platform_text = """macOS Installation:
• Using Homebrew (recommended):
  brew install android-platform-tools

• Using Android Studio:
  Download from developer.android.com and install Android SDK

• Manual installation:
  Download platform-tools from developer.android.com
  Extract to /usr/local/bin/ or ~/bin/"""
        else:  # Linux
            platform_text = """Linux Installation:
• Ubuntu/Debian:
  sudo apt update && sudo apt install android-tools-adb

• Fedora:
  sudo dnf install android-tools

• Arch Linux:
  sudo pacman -S android-tools

• Using Android Studio:
  Download from developer.android.com and install Android SDK

• Manual installation:
  Download platform-tools from developer.android.com
  Extract to /usr/local/bin/ or ~/bin/"""
        
        platform_label = tk.Label(dialog, text=platform_text, 
                                font=(get_platform_font(), 10), bg=self.bg_color, fg=self.fg_color,
                                justify=tk.LEFT, wraplength=650)
        platform_label.pack(pady=(0, 20), padx=20)
        
        # Additional info
        info_text = """After installation:
1. Restart Y1 Remote Control
2. Connect your Y1 device via USB
3. Enable USB debugging on your device
4. Accept the USB debugging prompt on your device"""
        
        info_label = tk.Label(dialog, text=info_text, 
                             font=(get_platform_font(), 10), bg=self.bg_color, fg=self.fg_color,
                             justify=tk.LEFT, wraplength=650)
        info_label.pack(pady=(0, 20), padx=20)
        
        # Buttons
        button_frame = tk.Frame(dialog, bg=self.bg_color)
        button_frame.pack(pady=(0, 20))
        
        # Open download page button
        download_button = tk.Button(button_frame, text="Open Android SDK Download Page", 
                                   command=lambda: webbrowser.open_new_tab("https://developer.android.com/studio#command-tools"),
                                   bg=self.button_bg, fg=self.button_fg, 
                                   activebackground=self.button_active_bg, 
                                   activeforeground=self.button_active_fg, 
                                   font=(get_platform_font(), 9), relief="flat", bd=1)
        download_button.pack(side=tk.LEFT, padx=(0, 10))
        
        # OK button
        ok_button = tk.Button(button_frame, text="OK", command=dialog.destroy,
                             bg=self.button_bg, fg=self.button_fg, 
                             activebackground=self.button_active_bg, 
                             activeforeground=self.button_active_fg, 
                             font=(get_platform_font(), 9), relief="flat", bd=1)
        ok_button.pack(side=tk.LEFT)
        
        # Focus on OK button
        ok_button.focus_set()
        
        # Bind Enter key to OK button
        dialog.bind("<Return>", lambda e: dialog.destroy())
        dialog.bind("<Escape>", lambda e: dialog.destroy())

    def unified_device_check(self):
        try:
            # First check if ADB is available
            if not self.check_adb_availability():
                self.status_var.set("ADB not available - Please install ADB")
                self.device_connected = False
                return
            
            adb_path = self.get_adb_path()
            result = subprocess.run([adb_path, "devices"], capture_output=True, text=True, timeout=5)
            
            if "device" in result.stdout and "List of devices" in result.stdout:
                if not self.device_connected:
                    self.device_connected = True
                    self.status_var.set("Device connected")
                    self.show_controls_frame()
                    self.enable_input_bindings()
                    self.set_device_stay_awake()
                self.refresh_apps()
            else:
                if self.device_connected:
                    self.device_connected = False
                    self.status_var.set("Device disconnected - Please reconnect")
                    self.hide_controls_frame()
                    self.disable_input_bindings()
                else:
                    self.status_var.set("No ADB device found")
                    self.device_connected = False
        except Exception as e:
            if self.device_connected:
                self.device_connected = False
                self.status_var.set("Device disconnected - Please reconnect")
                self.hide_controls_frame()
                self.disable_input_bindings()
            else:
                self.status_var.set(f"ADB Error: {str(e)}")
                self.device_connected = False

    def detect_current_app(self):
        if not self.device_connected: return
        try:
            success, stdout, stderr = self.run_adb_command("shell dumpsys activity activities | grep mResumedActivity")
            detected_package = None
            if success and stdout:
                match = re.search(r' ([a-zA-Z0-9_.]+)/(\S+)', stdout)
                if match:
                    detected_package = match.group(1)

            if detected_package:
                if self.current_app != detected_package:
                    self.current_app = detected_package
                    self.manual_mode_override = False
                # Logic to auto-switch modes based on app
                # (You can expand this list)
                if "rockbox" in detected_package or ".y1" in detected_package:
                    if not self.manual_mode_override:
                        self.scroll_wheel_mode_var.set(True)
                        self.toggle_scroll_wheel_mode() # Update UI
                else:
                     if not self.manual_mode_override:
                        self.scroll_wheel_mode_var.set(False)
                        self.toggle_scroll_wheel_mode() # Update UI

        except Exception as e:
            debug_print(f"Error detecting app: {e}")

    def run_adb_command(self, command, timeout=10):
        try:
            adb_path = self.get_adb_path()
            if adb_path is None:
                return False, "", "ADB not available - Please install ADB"
            
            startupinfo = None
            if platform.system() == "Windows":
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                startupinfo.wShowWindow = subprocess.SW_HIDE

            if '"' in command:
                if platform.system() == "Windows":
                    full_command = f'"{adb_path}" {command}'
                    result = subprocess.run(full_command, shell=True, capture_output=True, text=True, timeout=timeout, startupinfo=startupinfo)
                else:
                    import shlex
                    full_command = [adb_path] + shlex.split(command)
                    result = subprocess.run(full_command, capture_output=True, text=True, timeout=timeout)
            else:
                full_command = [adb_path] + command.split()
                if platform.system() == "Windows":
                    result = subprocess.run(full_command, capture_output=True, text=True, timeout=timeout, startupinfo=startupinfo)
                else:
                    result = subprocess.run(full_command, capture_output=True, text=True, timeout=timeout)
            
            return result.returncode == 0, result.stdout, result.stderr
        except Exception as e:
            return False, "", str(e)

    def start_screen_capture(self):
        if not self.capture_thread or not self.capture_thread.is_alive():
            self.is_capturing = True
            self.capture_thread = threading.Thread(target=self.capture_screen_loop, daemon=True)
            self.capture_thread.start()

    def capture_screen_loop(self):
        temp_dir = tempfile.gettempdir()
        fb_temp_path = os.path.join(temp_dir, "y1_fb0.tmp")
        placeholder_shown = False
        
        while self.is_capturing:
            try:
                current_time = time.time()
                
                if current_time - self.last_unified_check > self.unified_check_interval:
                    self.unified_device_check()
                    self.last_unified_check = current_time
                
                if not self.device_connected:
                    if not placeholder_shown:
                        self.show_ready_placeholder()
                        placeholder_shown = True
                        self.status_var.set("Device disconnected - Please reconnect")
                        self.disable_input_bindings()
                    time.sleep(2)
                    continue
                
                if placeholder_shown:
                    placeholder_shown = False
                    self.status_var.set("Device connected")
                    self.enable_input_bindings()
                
                if current_time - self.last_framebuffer_refresh > self.framebuffer_refresh_interval or self.force_refresh_requested:
                    success, _, _ = self.run_adb_command(f"pull /dev/graphics/fb0 \"{fb_temp_path}\"")
                    if success and os.path.exists(fb_temp_path):
                        self.process_framebuffer(fb_temp_path)
                    else:
                        self.device_connected = False # Assume disconnected
                    self.last_framebuffer_refresh = current_time
                    self.force_refresh_requested = False
                else:
                    time.sleep(0.5)
            except Exception as e:
                self.device_connected = False
                self.show_ready_placeholder()
                placeholder_shown = True
                self.status_var.set("Device disconnected - Please reconnect")
                time.sleep(1)

    def process_framebuffer(self, fb_path):
        try:
            file_size = os.path.getsize(fb_path)
            if file_size < 100:
                self.show_sleeping_placeholder()
                return

            with open(fb_path, 'rb') as f:
                data = f.read()
            
            # Simplified processing logic assuming BGRA8888
            expected_size = self.device_width * self.device_height * 4
            if len(data) >= expected_size:
                arr = np.frombuffer(data[:expected_size], dtype=np.uint8).reshape((self.device_height, self.device_width, 4))
                arr = arr[..., [2, 1, 0, 3]] # BGRA to RGBA for PIL
                img = Image.fromarray(arr).convert('RGB')

                if self.is_screen_blank(img):
                    self.show_sleeping_placeholder()
                    return

                resized_img = img.resize((self.display_width, self.display_height), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(resized_img)
                self.after_idle(lambda: self.update_screen_display(photo))
                self.last_screen_image = img
            else:
                self.show_sleeping_placeholder()

        except Exception as e:
            self.show_sleeping_placeholder()
            
    def force_framebuffer_refresh(self):
        self.force_refresh_requested = True

    def update_screen_display(self, photo):
        self.ready_placeholder_shown = False
        try:
            self.current_photo = photo
            self.screen_canvas.delete("all")
            self.screen_canvas.create_image(0, 0, anchor=tk.NW, image=self.current_photo)
        except Exception:
            pass # Ignore errors during UI update

    def show_sleeping_placeholder(self):
        try:
            # Try to load sleeping.png from assets directory first, then current directory
            img_path = None
            if os.path.exists(os.path.join(self.assets_dir, 'sleeping.png')):
                img_path = os.path.join(self.assets_dir, 'sleeping.png')
            elif os.path.exists('sleeping.png'):
                img_path = 'sleeping.png'
            
            if img_path:
                img = Image.open(img_path)
                img = img.resize((self.display_width, self.display_height), Image.Resampling.LANCZOS)
            else:
                # Fallback to solid color if PNG not found
                img = Image.new('RGB', (self.display_width, self.display_height), (20, 20, 20))
            
            photo = ImageTk.PhotoImage(img)
            self.update_screen_display(photo)
        except Exception as e:
            debug_print(f"Sleeping placeholder error: {e}")
            # Fallback to solid color on error
            try:
                img = Image.new('RGB', (self.display_width, self.display_height), (20, 20, 20))
                photo = ImageTk.PhotoImage(img)
                self.update_screen_display(photo)
            except:
                pass
            
    def show_ready_placeholder(self):
        self.ready_placeholder_shown = True
        try:
            # Try to load ready.png from assets directory first, then current directory
            img_path = None
            if os.path.exists(os.path.join(self.assets_dir, 'ready.png')):
                img_path = os.path.join(self.assets_dir, 'ready.png')
            elif os.path.exists('ready.png'):
                img_path = 'ready.png'
            
            if img_path:
                img = Image.open(img_path)
                img = img.resize((self.display_width, self.display_height), Image.Resampling.LANCZOS)
            else:
                # Fallback to solid color if PNG not found
                img = Image.new('RGB', (self.display_width, self.display_height), (30, 30, 30))
            
            photo = ImageTk.PhotoImage(img)
            self.update_screen_display(photo)
        except Exception as e:
            debug_print(f"Ready placeholder error: {e}")
            # Fallback to solid color on error
            try:
                img = Image.new('RGB', (self.display_width, self.display_height), (30, 30, 30))
                photo = ImageTk.PhotoImage(img)
                self.update_screen_display(photo)
            except:
                pass

    def send_back_key(self):
        if not self._input_paced(): return
        self.force_framebuffer_refresh()
        self.run_adb_command("shell input keyevent 4")
        self.after(100, self.force_framebuffer_refresh)

    def set_device_stay_awake(self):
        if not self.device_connected or self.device_stay_awake_set:
            return
        success, _, _ = self.run_adb_command("shell settings put global stay_on_while_plugged_in 3")
        if success:
            self.device_stay_awake_set = True

    def is_screen_blank(self, img):
        try:
            arr = np.array(img.convert('L'))
            return np.mean(arr) < 15.0 and np.std(arr) < 5.0
        except Exception:
            return False

    def launch_settings(self):
        self.run_adb_command("shell am start -n com.android.settings/.Settings")
        self.status_var.set("Settings launched")
        
    def go_home(self):
        self.run_adb_command("shell input keyevent 3") # KEYCODE_HOME
        self.status_var.set("Home key sent")

    def browse_apks(self):
        file_path = filedialog.askopenfilename(title="Select APK file", filetypes=[("APK files", "*.apk")])
        if file_path:
            self.status_var.set("Installing APK...")
            self.update_idletasks()
            success, stdout, stderr = self.run_adb_command(f"install -r \"{file_path}\"")
            if success:
                self.status_var.set("APK installed successfully")
                self.refresh_apps()
            else:
                self.status_var.set(f"APK installation failed")
                messagebox.showerror("Install Failed", stderr or stdout)

    def launch_app(self, package_name):
        self.run_adb_command(f"shell monkey -p {package_name} -c android.intent.category.LAUNCHER 1")
        self.status_var.set(f"Launched {package_name}")

    def uninstall_app(self, package_name):
        if messagebox.askyesno("Uninstall", f"Uninstall {package_name}?"):
            self.status_var.set(f"Uninstalling {package_name}...")
            self.update_idletasks()
            success, stdout, stderr = self.run_adb_command(f"uninstall {package_name}")
            if success:
                self.status_var.set(f"{package_name} uninstalled")
                self.refresh_apps()
            else:
                self.status_var.set("Uninstall failed")
                messagebox.showerror("Uninstall Failed", stderr or stdout)

    def on_screen_click(self, event):
        if self.input_disabled or not self._input_paced(): return
        x = int(event.x / self.display_scale)
        y = int(event.y / self.display_scale)
        if 0 <= x < self.device_width and 0 <= y < self.device_height:
            self.force_framebuffer_refresh()
            if self.control_launcher:
                self.run_adb_command("shell input keyevent 66") # ENTER
            else:
                self.run_adb_command(f"shell input tap {x} {y}")
            self.after(100, self.force_framebuffer_refresh)

    def on_screen_right_click(self, event):
        self.send_back_key()
    
    def on_mouse_wheel(self, event):
        if self.input_disabled or not self._input_paced(): return
        direction = 0
        if hasattr(event, 'delta') and event.delta != 0:
            direction = 1 if event.delta > 0 else -1
        elif hasattr(event, 'num'):
            if event.num == 4: direction = 1
            elif event.num == 5: direction = -1
        if direction == 0: return

        if self.scroll_wheel_mode_var.get():
            self.show_scroll_cursor()
            if self.disable_dpad_swap_var.get():
                keycode = 19 if direction > 0 else 20 # UP/DOWN
            else:
                keycode = 21 if direction > 0 else 22 # LEFT/RIGHT
        else:
            keycode = 19 if direction > 0 else 20 # UP/DOWN
            
        self.run_adb_command(f"shell input keyevent {keycode}")
        self.after(50, self.force_framebuffer_refresh)

    def on_mouse_wheel_click(self, event):
        if self.input_disabled or not self._input_paced(): return
        keycode = 66 if self.control_launcher else 23 # ENTER or DPAD_CENTER
        self.run_adb_command(f"shell input keyevent {keycode}")
        self.after(50, self.force_framebuffer_refresh)

    def on_key_press(self, event):
        if self.input_disabled or not self._input_paced(): return
        key = event.keysym.lower()
        dpad_map = {'w': 19, 'up': 19, 's': 20, 'down': 20, 'a': 21, 'left': 21, 'd': 22, 'right': 22}
        keycode = None
        if key in dpad_map:
            keycode = dpad_map[key]
            if self.control_launcher and self.scroll_wheel_mode_var.get() and not self.disable_dpad_swap_var.get():
                if keycode == 19: keycode = 21 # up -> left
                elif keycode == 20: keycode = 22 # down -> right
        elif key in ['return', 'e']:
            keycode = 66 if self.control_launcher else 23
        elif key == 'escape':
            keycode = 4 # BACK
        
        if keycode:
            self.run_adb_command(f"shell input keyevent {keycode}")
            self.after(50, self.force_framebuffer_refresh)

    def on_key_release(self, event):
        if self.scroll_cursor_timer:
            self.after_cancel(self.scroll_cursor_timer)
            self.hide_scroll_cursor()

    def open_adb_shell(self):
        try:
            adb_path = self.get_adb_path()
            if adb_path is None:
                messagebox.showerror("Error", "ADB not available - Please install ADB")
                return
            
            if platform.system() == "Windows":
                subprocess.Popen([adb_path, "shell"], creationflags=subprocess.CREATE_NEW_CONSOLE)
            else:
                subprocess.Popen([adb_path, "shell"])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open ADB shell: {e}")

    def show_device_info(self):
        info = []
        model, _ , _ = self.run_adb_command("shell getprop ro.product.model")
        android_v, _, _ = self.run_adb_command("shell getprop ro.build.version.release")
        info.append(f"Model: {model.strip()}")
        info.append(f"Android: {android_v.strip()}")
        messagebox.showinfo("Device Information", "\n".join(info) if info else "Unable to get info.")

    def change_device_language(self):
        if not self.device_connected:
            messagebox.showerror("Error", "Device not connected!")
            return
        self.run_adb_command("shell am start -a android.settings.LOCALE_SETTINGS")

    def cleanup(self):
        self.is_capturing = False

    def on_closing(self):
        self.cleanup()
        self.destroy()

    def _input_paced(self):
        now = time.time()
        if now - self.last_input_time < self.input_pacing_interval:
            return False
        self.last_input_time = now
        self.last_user_activity = now
        return True

    def _add_tooltip(self, widget, text):
        tooltip = tk.Toplevel(widget)
        tooltip.withdraw()
        tooltip.overrideredirect(True)
        
        label = tk.Label(tooltip, text=text, background="#fff", relief=tk.SOLID, borderwidth=1, font=(get_platform_font(), 9), wraplength=320, justify=tk.LEFT)
        label.pack(ipadx=4, ipady=2)
        def enter(event):
            x = widget.winfo_rootx() + 20
            y = widget.winfo_rooty() + 20
            tooltip.geometry(f"+{x}+{y}")
            tooltip.deiconify()
        def leave(event):
            tooltip.withdraw()
        widget.bind("<Enter>", enter)
        widget.bind("<Leave>", leave)

    def _should_auto_enable_scroll_wheel(self, package_name):
        return package_name and ("rockbox" in package_name or ".y1" in package_name)

    def show_scroll_cursor(self):
        if not self.scroll_wheel_mode_var.get() or self.ready_placeholder_shown: return
        if self.scroll_cursor_timer: self.after_cancel(self.scroll_cursor_timer)
        # Use appropriate cursor for each platform
        if platform.system() == "Windows":
            self.screen_canvas.config(cursor="wait")
        elif platform.system() == "Darwin":  # macOS
            self.screen_canvas.config(cursor="")
        else:  # Linux
            self.screen_canvas.config(cursor="")
        self.scroll_cursor_timer = self.after(self.scroll_cursor_duration, self.hide_scroll_cursor)

    def hide_scroll_cursor(self):
        if self.ready_placeholder_shown: return
        # Use appropriate cursor for each platform
        if self.scroll_wheel_mode_var.get():
            self.screen_canvas.config(cursor="")
        else:
            if platform.system() == "Windows":
                self.screen_canvas.config(cursor="hand2")
            else:
                # macOS and Linux don't have hand2 cursor, use default
                self.screen_canvas.config(cursor="")

    def take_screenshot(self):
        debug_print("take_screenshot called")
        try:
            if not self.device_connected or not self.last_screen_image:
                messagebox.showwarning("Screenshot Failed", "Device not connected or no screen data available.")
                return
            
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            default_filename = f"Y1_Screenshot_{timestamp}.png"
            file_path = filedialog.asksaveasfilename(title="Save Screenshot", defaultextension=".png", filetypes=[("PNG files", "*.png")], initialfile=default_filename)
            
            if file_path:
                try:
                    self.last_screen_image.save(file_path)
                    messagebox.showinfo("Success", f"Screenshot saved to {file_path}")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save screenshot: {e}")
        except Exception as e:
            debug_print(f"Error in take_screenshot: {e}")
            messagebox.showerror("Error", f"Failed to take screenshot: {e}")

    def show_recent_apps(self):
        self.run_adb_command("shell input keyevent 187") # KEYCODE_APP_SWITCH
        self.status_var.set("Recent Apps opened")
        
    def setup_bindings(self):
        self.bind("<Alt_L>", self.toggle_launcher_control)
        self.bind("<Alt_R>", self.toggle_launcher_control)
        self.bind_all("<Key>", self.on_key_press)
        self.bind_all("<KeyRelease>", self.on_key_release)

if __name__ == "__main__":
    print("You can minimise this window and use remote control and app install features")
    app = Y1HelperApp()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
