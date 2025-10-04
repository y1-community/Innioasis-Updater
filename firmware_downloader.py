
Gemini
What can Gemini do
in Google Drive
Summarize a topic
based on files in my Drive
Summarize a folder
in my Drive
Sales pitch ideator
Create compelling sales pitches that resonate with your audience and drive conversions.
Learning coach
Here to help you learn and practice new concepts. Tell me what you'd like to learn, and I'll help you get started.
Sentiment analyser
Analyse customer feedback to reveal trends and make recommendations.
Your Gems will appear across Workspace
Gemini in Workspace can make mistakes, so double-check responses. Learn more
#!/usr/bin/env python3
"""
Firmware Downloader for MTK Client
Downloads firmware releases from XML manifest and processes them with mtk.py
"""

import sys
import os
import zipfile
import subprocess
import threading
import requests
import configparser
import json
import pickle
import shutil
import argparse
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET
from datetime import datetime, date
import random
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
                               QWidget, QListWidget, QListWidgetItem, QPushButton, QTextEdit,
                               QLabel, QComboBox, QProgressBar, QMessageBox,
                               QGroupBox, QSplitter, QStackedWidget, QCheckBox, QProgressDialog,
                               QFileDialog, QDialog, QTabWidget, QScrollArea)
from PySide6.QtCore import QThread, Signal, Qt, QSize, QTimer, QPropertyAnimation, QEasingCurve, QObject
from PySide6.QtGui import QFont, QPixmap, QTextDocument, QPalette
import platform
import time
import logging
from collections import defaultdict
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

# Import AppKit for macOS Dock hiding (only on macOS)
if platform.system() == "Darwin":
    try:
        import AppKit
    except ImportError:
        AppKit = None

# Global silent mode flag - controls terminal output
SILENT_MODE = True

def parse_version_designations(version_name):
    """Parse version names and extract designations with flexible adjective handling"""
    designations = []
    
    # Define adjectives that can modify their nearest neighbor
    adjectives = ['compatible', 'aware', 'supported', 'enabled', 'disabled', 'ready', 'optimized', 'enhanced']
    
    # Extract only the part after the last dash (this is the actual version number)
    import re
    # First remove long hex strings at the end (like -13057e75dc29a1a7!)
    clean_version = re.sub(r'-[a-f0-9]{16,}!?$', '', version_name)
    # Remove any remaining trailing dashes or exclamation marks
    clean_version = clean_version.rstrip('-!')
    
    # Extract only the numbers after the last dash
    if '-' in clean_version:
        last_part = clean_version.split('-')[-1]
        # Check if the last part contains only numbers (and possibly dots)
        if re.match(r'^[\d.]+$', last_part):
            clean_version = last_part
    
    # Parse designations from the original version name
    # Split by dashes and process each part
    parts = version_name.split('-')
    
    for i, part in enumerate(parts):
        # Skip if it's the version number part
        if re.match(r'^[\d.]+$', part):
            continue
            
        # Skip if it's a hex string
        if re.match(r'^[a-f0-9]{16,}!?$', part):
            continue
            
        # Handle special cases first
        if part == 'nightly':
            designations.append('Nightly')
        elif part == '360p':
            designations.append('360p / Y1 Theme Compatible')
        elif part == 'wifi' or part == 'wi-fi':
            designations.append('Wi-Fi')
        elif part == 'rockbox':
            designations.append('with Rockbox')
        elif part == 'usb':
            designations.append('USB')
        elif part == 'ethernet':
            designations.append('Ethernet')
        elif part == 'hdmi':
            designations.append('HDMI')
        elif part == 'audio':
            designations.append('Audio')
        elif part == 'video':
            designations.append('Video')
        elif part == 'camera':
            designations.append('Camera')
        elif part == 'gps':
            designations.append('GPS')
        elif part == 'nfc':
            designations.append('NFC')
        elif part == 'lte':
            designations.append('LTE')
        elif part == '5g':
            designations.append('5G')
        elif part == 'ipod' and i + 1 < len(parts) and parts[i + 1] == 'theme':
            # Handle "ipod-theme" case
            if i + 2 < len(parts) and parts[i + 2] in adjectives:
                # Check for adjective after "ipod-theme"
                adjective = parts[i + 2]
                designations.append(f'240p iPod / 360p Y1 Themes {adjective.title()}')
            else:
                designations.append('240p iPod themes / 360p Y1 Themes')
        elif part == 'theme' and i > 0 and parts[i - 1] == 'ipod':
            # Skip this as it's handled above
            continue
        else:
            # Check if this part is followed by an adjective
            if i + 1 < len(parts) and parts[i + 1] in adjectives:
                adjective = parts[i + 1]
                # Capitalize the main part and add the adjective
                main_part = part.replace('-', ' ').title()
                designations.append(f'{main_part} {adjective.title()}')
            else:
                # Just add the part as-is, capitalized
                if part not in adjectives:  # Don't add standalone adjectives
                    designations.append(part.replace('-', ' ').title())
    
    return {
        'clean_version': clean_version.strip(),
        'designations': designations
    }

def get_display_version(version_info, published_date):
    """Get the display version - either version number or published date based on length"""
    version_text = version_info['clean_version']
    
    # If version is longer than 8 characters, use published date instead
    if len(version_text) > 8:
        if published_date:
            try:
                from datetime import datetime
                date_obj = datetime.fromisoformat(published_date.replace('Z', '+00:00'))
                return format_fancy_date(date_obj)
            except:
                return published_date
        else:
            return "Unknown Date"
    
    return version_text

def format_fancy_date(date_obj):
    """Format date in a fancy, simplified way without time"""
    from datetime import datetime, timedelta
    
    now = datetime.now(date_obj.tzinfo) if date_obj.tzinfo else datetime.now()
    today = now.date()
    yesterday = today - timedelta(days=1)
    date_only = date_obj.date()
    
    if date_only == today:
        return "Today"
    elif date_only == yesterday:
        return "Yesterday"
    elif (today - date_only).days <= 7:
        # Within the last week
        return date_obj.strftime('%A')  # Day name (Monday, Tuesday, etc.)
    elif (today - date_only).days <= 30:
        # Within the last month
        return date_obj.strftime('%b %d')  # Jan 15, Feb 3, etc.
    else:
        # Older than a month
        return date_obj.strftime('%b %Y')  # Jan 2024, Feb 2024, etc.

def format_designations_text(designations):
    """Format designations as text with visual indicators"""
    if not designations:
        return ""
    
    # Map designations to emoji indicators
    emoji_map = {
        'Nightly': '🟠',
        '360p': '🟡',
        'Wi-Fi': '📶',
        'with Rockbox ': '🔵',
        'USB': '🔌',
        'Ethernet': '🌐',
        'HDMI': '📺',
        'Audio': '🔊',
        'Video': '🎥',
        'Camera': '📷',
        'GPS': '📍',
        'NFC': '📱',
        'LTE': '📡',
        '5G': '📡',
    }
    
    formatted_designations = []
    for designation in designations:
        # Check for iPod themes variations
        if 'iPod Themes' in designation:
            formatted_designations.append(f"✅ {designation}")
        else:
            # Try to find a matching emoji, fallback to generic
            emoji = '⚪'
            for key, value in emoji_map.items():
                if designation.startswith(key):
                    emoji = value
                    break
            formatted_designations.append(f"{emoji} {designation}")
    
    return " | ".join(formatted_designations)

# Zip file management
ZIP_STORAGE_DIR = Path("firmware_downloads")
EXTRACTED_FILES_LOG = Path("extracted_files.log")

# Installation tracking
INSTALLATION_MARKER_FILE = Path("firmware_installation_in_progress.flag")

# Caching configuration
CACHE_DIR = Path(".cache")
CACHE_DIR.mkdir(exist_ok=True)
CONFIG_CACHE_FILE = CACHE_DIR / "config_cache.json"
MANIFEST_CACHE_FILE = CACHE_DIR / "manifest_cache.json"
CACHE_DURATION = 300  # 5 minutes cache duration

# Performance optimization
MAX_CONCURRENT_REQUESTS = 3
REQUEST_TIMEOUT = 8
TOKEN_VALIDATION_TIMEOUT = 10

def silent_print(*args, **kwargs):
    """Print function that respects silent mode - completely silent by default"""
    if SILENT_MODE:
        # Completely silent - no output to terminal
        pass
    else:
        print(*args, **kwargs)

# Easter Egg System - Seasonal Emojis
def is_us_user():
    """Check if the user is in the US based on system locale/region"""
    try:
        import locale
        # Get the system locale
        system_locale = locale.getdefaultlocale()[0]
        if system_locale:
            # Check if locale starts with 'en_US' or contains 'US'
            return system_locale.startswith('en_US') or 'US' in system_locale
    except:
        pass
    
    try:
        # Fallback: check environment variables
        import os
        lc_all = os.environ.get('LC_ALL', '')
        lang = os.environ.get('LANG', '')
        return 'en_US' in lc_all or 'en_US' in lang or 'US' in lc_all or 'US' in lang
    except:
        pass
    
    # Default to True if we can't determine (assume US for safety)
    return True

def is_thanksgiving_region():
    """Check if the user is in a region that celebrates Thanksgiving (US/Canada)"""
    try:
        import locale
        # Get the system locale
        system_locale = locale.getdefaultlocale()[0]
        if system_locale:
            # Check for US or Canadian locales
            return (system_locale.startswith('en_US') or 
                   system_locale.startswith('en_CA') or 
                   'US' in system_locale or 
                   'CA' in system_locale)
    except:
        pass
    
    try:
        # Fallback: check environment variables
        import os
        lc_all = os.environ.get('LC_ALL', '')
        lang = os.environ.get('LANG', '')
        return ('en_US' in lc_all or 'en_CA' in lc_all or 
                'en_US' in lang or 'en_CA' in lang or
                'US' in lc_all or 'CA' in lc_all or
                'US' in lang or 'CA' in lang)
    except:
        pass
    
    # Default to True if we can't determine (assume US for safety)
    return True

def get_seasonal_emoji():
    """Get seasonal emoji based on current date - Christmas and Halloween easter eggs!"""
    today = date.today()
    month = today.month
    day = today.day
    
    # Christmas Season: December 25 - January 5 (12 days of Christmas)
    if (month == 12 and day >= 25) or (month == 1 and day <= 5):
        christmas_emojis = [
            "🎄", "🎅", "🤶", "🎁", "❄️", "⛄", "🦌", "🔔", "🌟", "🎊", "🎉", "✨"
        ]
        # Use day to pick emoji (Dec 25 = first emoji, Jan 5 = last emoji)
        if month == 12:
            # December 25-31: days 25-31
            emoji_index = (day - 25) % len(christmas_emojis)
        else:
            # January 1-5: days 1-5 (continue from December)
            emoji_index = (day + 6) % len(christmas_emojis)  # +6 because Dec 25-31 = 7 days
        return christmas_emojis[emoji_index]
    
    # Halloween Season: October 25-31
    elif month == 10 and 25 <= day <= 31:
        halloween_emojis = [
            "🎃", "👻", "🦇", "🕷️", "🕸️", "💀", "🧙‍♀️", "🧛‍♂️", "🦹‍♀️", "🎭", "⚰️", "🦴"
        ]
        # Use day of month to pick emoji (25th = first emoji, 31st = last emoji)
        emoji_index = (day - 25) % len(halloween_emojis)
        return halloween_emojis[emoji_index]
    
    # Thanksgiving Season: November 20-30 - only for US/Canada
    elif month == 11 and 20 <= day <= 30 and is_thanksgiving_region():
        thanksgiving_emojis = [
            "🦃", "🍗", "🥧", "🌽", "🍂", "🍁", "🦌", "🌾", "🏠", "👨‍👩‍👧‍👦", "🙏", "🍽️"
        ]
        emoji_index = (day - 20) % len(thanksgiving_emojis)
        return thanksgiving_emojis[emoji_index]
    
    # St. Patrick's Day: March 17
    elif month == 3 and day == 17:
        st_patricks_emojis = [
            "🍀", "☘️", "🌈", "🍺", "🥃", "🇮🇪", "🧚‍♀️", "🪙", "🎩", "🎭", "🎪", "🎨"
        ]
        return random.choice(st_patricks_emojis)
    
    # Valentine's Day: February 14
    elif month == 2 and day == 14:
        valentines_emojis = [
            "💕", "💖", "💗", "💘", "💝", "💞", "💟", "❤️", "🧡", "💛", "💚", "💙"
        ]
        return random.choice(valentines_emojis)
    
    # Easter Season: March 22 - April 25 (approximate range)
    elif month == 3 and day >= 22:
        easter_emojis = [
            "🐰", "🐣", "🥚", "🌷", "🌸", "🦋", "🐛", "🌱", "🌿", "🍃", "🌺", "🌼"
        ]
        emoji_index = (day - 22) % len(easter_emojis)
        return easter_emojis[emoji_index]
    elif month == 4 and day <= 25:
        easter_emojis = [
            "🐰", "🐣", "🥚", "🌷", "🌸", "🦋", "🐛", "🌱", "🌿", "🍃", "🌺", "🌼"
        ]
        emoji_index = (day + 9) % len(easter_emojis)  # +9 because March 22-31 = 10 days
        return easter_emojis[emoji_index]
    
    # New Year's Day: January 1
    elif month == 1 and day == 1:
        new_year_emojis = [
            "🎊", "🎉", "🥳", "🍾", "🥂", "🎆", "🎇", "✨", "🌟", "💫", "🎈", "🎁"
        ]
        return random.choice(new_year_emojis)
    
    # Independence Day (US): July 4 - only for US users
    elif month == 7 and day == 4 and is_us_user():
        independence_emojis = [
            "🇺🇸", "🎆", "🎇", "⭐", "🌟", "💥", "🎊", "🎉", "🏛️", "🗽", "🦅", "🎪"
        ]
        return random.choice(independence_emojis)
    
    # Summer Solstice: June 20-22 (approximate)
    elif month == 6 and 20 <= day <= 22:
        summer_emojis = [
            "☀️", "🌞", "🌻", "🌺", "🏖️", "🏝️", "🌊", "🏄‍♂️", "🏄‍♀️", "🌴", "🍉", "🍓"
        ]
        emoji_index = (day - 20) % len(summer_emojis)
        return summer_emojis[emoji_index]
    
    # No seasonal emoji
    return ""

def get_seasonal_emoji_random():
    """Get a random seasonal emoji if in season, otherwise return empty string"""
    today = date.today()
    month = today.month
    day = today.day
    
    # Christmas Season: December 25 - January 5
    if (month == 12 and day >= 25) or (month == 1 and day <= 5):
        christmas_emojis = [
            "🎄", "🎅", "🤶", "🎁", "❄️", "⛄", "🦌", "🔔", "🌟", "🎊", "🎉", "✨"
        ]
        return random.choice(christmas_emojis)
    
    # Halloween Season: October 25-31
    elif month == 10 and 25 <= day <= 31:
        halloween_emojis = [
            "🎃", "👻", "🦇", "🕷️", "🕸️", "💀", "🧙‍♀️", "🧛‍♂️", "🦹‍♀️", "🎭", "⚰️", "🦴"
        ]
        return random.choice(halloween_emojis)
    
    # Thanksgiving Season: November 20-30 - only for US/Canada
    elif month == 11 and 20 <= day <= 30 and is_thanksgiving_region():
        thanksgiving_emojis = [
            "🦃", "🍗", "🥧", "🌽", "🍂", "🍁", "🦌", "🌾", "🏠", "👨‍👩‍👧‍👦", "🙏", "🍽️"
        ]
        return random.choice(thanksgiving_emojis)
    
    # St. Patrick's Day: March 17
    elif month == 3 and day == 17:
        st_patricks_emojis = [
            "🍀", "☘️", "🌈", "🍺", "🥃", "🇮🇪", "🧚‍♀️", "🪙", "🎩", "🎭", "🎪", "🎨"
        ]
        return random.choice(st_patricks_emojis)
    
    # Valentine's Day: February 14
    elif month == 2 and day == 14:
        valentines_emojis = [
            "💕", "💖", "💗", "💘", "💝", "💞", "💟", "❤️", "🧡", "💛", "💚", "💙"
        ]
        return random.choice(valentines_emojis)
    
    # Easter Season: March 22 - April 25
    elif (month == 3 and day >= 22) or (month == 4 and day <= 25):
        easter_emojis = [
            "🐰", "🐣", "🥚", "🌷", "🌸", "🦋", "🐛", "🌱", "🌿", "🍃", "🌺", "🌼"
        ]
        return random.choice(easter_emojis)
    
    # New Year's Day: January 1
    elif month == 1 and day == 1:
        new_year_emojis = [
            "🎊", "🎉", "🥳", "🍾", "🥂", "🎆", "🎇", "✨", "🌟", "💫", "🎈", "🎁"
        ]
        return random.choice(new_year_emojis)
    
    # Independence Day (US): July 4 - only for US users
    elif month == 7 and day == 4 and is_us_user():
        independence_emojis = [
            "🇺🇸", "🎆", "🎇", "⭐", "🌟", "💥", "🎊", "🎉", "🏛️", "🗽", "🦅", "🎪"
        ]
        return random.choice(independence_emojis)
    
    # Summer Solstice: June 20-22
    elif month == 6 and 20 <= day <= 22:
        summer_emojis = [
            "☀️", "🌞", "🌻", "🌺", "🏖️", "🏝️", "🌊", "🏄‍♂️", "🏄‍♀️", "🌴", "🍉", "🍓"
        ]
        return random.choice(summer_emojis)
    
    return ""

def is_christmas_season():
    """Check if it's Christmas season (12 days of Christmas: Dec 25 - Jan 5)"""
    today = date.today()
    return (today.month == 12 and today.day >= 25) or (today.month == 1 and today.day <= 5)

def is_halloween_season():
    """Check if it's Halloween season"""
    today = date.today()
    return today.month == 10 and 25 <= today.day <= 31

def is_thanksgiving_season():
    """Check if it's Thanksgiving season"""
    today = date.today()
    return today.month == 11 and 20 <= today.day <= 30

def is_st_patricks_day():
    """Check if it's St. Patrick's Day"""
    today = date.today()
    return today.month == 3 and today.day == 17

def is_valentines_day():
    """Check if it's Valentine's Day"""
    today = date.today()
    return today.month == 2 and today.day == 14

def is_easter_season():
    """Check if it's Easter season"""
    today = date.today()
    return (today.month == 3 and today.day >= 22) or (today.month == 4 and today.day <= 25)

def is_new_years_day():
    """Check if it's New Year's Day"""
    today = date.today()
    return today.month == 1 and today.day == 1

def is_independence_day():
    """Check if it's Independence Day (US)"""
    today = date.today()
    return today.month == 7 and today.day == 4

def is_summer_solstice():
    """Check if it's Summer Solstice"""
    today = date.today()
    return today.month == 6 and 20 <= today.day <= 22

# toggle_silent_mode function removed - debug mode is now controlled by keyboard shortcut

def cleanup_extracted_files():
    """Clean up extracted files at startup"""
    # Note: This function is now disabled to prevent conflicts with installation tracking
    # Extracted files are now managed by the installation marker system
    silent_print("Extracted files cleanup disabled - using installation marker system instead")
    return

def cleanup_firmware_files():
    """Clean up extracted firmware files (lk.bin, boot.img, etc.)"""
    try:
        firmware_files = ["lk.bin", "boot.img", "recovery.img", "system.img", "userdata.img"]
        cleaned_count = 0
        
        for file_name in firmware_files:
            file_path = Path(file_name)
            if file_path.exists():
                file_path.unlink()
                cleaned_count += 1
                silent_print(f"Cleaned up firmware file: {file_name}")
        
        if cleaned_count > 0:
            silent_print(f"Cleaned up {cleaned_count} firmware files")
        else:
            silent_print("No firmware files found to clean up")
            
    except Exception as e:
        silent_print(f"Error cleaning up firmware files: {e}")

def load_redundant_files_list():
    """Load redundant files list from local file or remote URL"""
    try:
        # Try local file first
        local_file = Path("redundant_files.txt")
        if local_file.exists():
            silent_print("Loading redundant files list from local file")
            with open(local_file, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            # Try remote URL
            silent_print("Loading redundant files list from remote URL")
            response = requests.get("https://innioasis.app/redundant_files.txt", timeout=10)
            response.raise_for_status()
            content = response.text
        
        # Parse the content
        redundant_files = {}
        current_platform = None
        
        for line in content.split('\n'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            if '=' in line:
                platform, files = line.split('=', 1)
                platform = platform.strip()
                files = files.strip()
                
                if platform == 'all':
                    redundant_files['all'] = [f.strip().strip('"') for f in files.split(',') if f.strip()]
                elif platform in ['mac', 'linux', 'win']:
                    redundant_files[platform] = [f.strip().strip('"') for f in files.split(',') if f.strip()]
        
        silent_print(f"Loaded redundant files list: {redundant_files}")
        return redundant_files
        
    except Exception as e:
        silent_print(f"Error loading redundant files list: {e}")
        return {}

def cleanup_redundant_files():
    """Clean up redundant files based on platform and redundant_files.txt"""
    try:
        current_platform = platform.system().lower()
        if current_platform == "darwin":
            platform_key = "mac"
        elif current_platform == "linux":
            platform_key = "linux"
        elif current_platform == "windows":
            platform_key = "win"
        else:
            platform_key = "unknown"
        
        silent_print(f"Cleaning up redundant files for platform: {platform_key}")
        
        # Load redundant files list
        redundant_files = load_redundant_files_list()
        if not redundant_files:
            silent_print("No redundant files list found, skipping cleanup")
            return
        
        current_dir = Path.cwd()
        removed_count = 0
        
        # Clean up files for all platforms
        if 'all' in redundant_files:
            for pattern in redundant_files['all']:
                removed_count += remove_files_by_pattern(current_dir, pattern)
        
        # Clean up platform-specific files
        if platform_key in redundant_files:
            for pattern in redundant_files[platform_key]:
                removed_count += remove_files_by_pattern(current_dir, pattern)
        
        if removed_count > 0:
            silent_print(f"Cleaned up {removed_count} redundant files")
        else:
            silent_print("No redundant files found to clean up")
        
        # Remove redundant_files.txt after cleanup is complete
        try:
            redundant_files_path = Path("redundant_files.txt")
            if redundant_files_path.exists():
                redundant_files_path.unlink()
                silent_print("Removed redundant_files.txt after cleanup")
        except Exception as e:
            silent_print(f"Error removing redundant_files.txt: {e}")
            
    except Exception as e:
        silent_print(f"Error during redundant files cleanup: {e}")

def remove_files_by_pattern(directory, pattern):
    """Remove files or directories matching a pattern in the given directory and subdirectories"""
    removed_count = 0
    try:
        # Check if pattern is a directory (no file extension and exists as directory)
        pattern_path = directory / pattern
        if pattern_path.exists() and pattern_path.is_dir():
            # Remove entire directory
            import shutil
            shutil.rmtree(pattern_path)
            silent_print(f"Removed redundant directory: {pattern}")
            removed_count += 1
        elif '*' in pattern:
            # Handle wildcard patterns - search recursively in subdirectories
            for file_path in directory.rglob(pattern):
                if file_path.is_file():
                    file_path.unlink()
                    silent_print(f"Removed redundant file: {file_path.relative_to(directory)}")
                    removed_count += 1
                elif file_path.is_dir():
                    import shutil
                    shutil.rmtree(file_path)
                    silent_print(f"Removed redundant directory: {file_path.relative_to(directory)}")
                    removed_count += 1
        else:
            # Handle specific file names - search recursively in subdirectories
            for file_path in directory.rglob(pattern):
                if file_path.is_file():
                    file_path.unlink()
                    silent_print(f"Removed redundant file: {file_path.relative_to(directory)}")
                    removed_count += 1
                elif file_path.is_dir():
                    import shutil
                    shutil.rmtree(file_path)
                    silent_print(f"Removed redundant directory: {file_path.relative_to(directory)}")
                    removed_count += 1
    except Exception as e:
        silent_print(f"Error removing files/directories matching pattern '{pattern}': {e}")
    
    return removed_count

def log_extracted_files(files):
    """Log extracted files for cleanup"""
    # Note: This function is now disabled to prevent conflicts with installation tracking
    # Extracted files are now managed by the installation marker system
    silent_print("Extracted files logging disabled - using installation marker system instead")
    return

def create_installation_marker():
    """Create a marker file to indicate firmware installation is in progress"""
    try:
        INSTALLATION_MARKER_FILE.touch()
        silent_print("Created installation marker file")
    except Exception as e:
        silent_print(f"Error creating installation marker: {e}")

def remove_installation_marker():
    """Remove the installation marker file when installation completes successfully"""
    try:
        if INSTALLATION_MARKER_FILE.exists():
            INSTALLATION_MARKER_FILE.unlink()
            silent_print("Removed installation marker file - installation completed successfully")
    except Exception as e:
        silent_print(f"Error removing installation marker: {e}")

def check_for_failed_installation():
    """Check if there was a failed firmware installation"""
    if INSTALLATION_MARKER_FILE.exists():
        silent_print("Detected failed firmware installation - showing troubleshooting options")
        return True
    return False

def get_zip_path(repo_name, version):
    """Get the path for a specific zip file"""
    safe_repo_name = repo_name.replace('/', '_')
    return ZIP_STORAGE_DIR / f"{safe_repo_name}_{version}.zip"

def load_cache(cache_file):
    """Load data from cache if it exists and is not expired"""
    try:
        if cache_file.exists():
            with open(cache_file, 'r') as f:
                cached_data = json.load(f)

            # Check if cache is still valid
            if time.time() - cached_data.get('timestamp', 0) < CACHE_DURATION:
                silent_print(f"Using cached data from {cache_file}")
                return cached_data.get('data')
            else:
                silent_print(f"Cache expired for {cache_file}")
        return None
    except Exception as e:
        silent_print(f"Error loading cache {cache_file}: {e}")
        return None

def save_cache(cache_file, data):
    """Save data to cache with timestamp"""
    try:
        cache_data = {
            'timestamp': time.time(),
            'data': data
        }
        with open(cache_file, 'w') as f:
            json.dump(cache_data, f)
        silent_print(f"Cached data to {cache_file}")
    except Exception as e:
        silent_print(f"Error saving cache {cache_file}: {e}")

def clear_cache():
    """Clear all cached data"""
    try:
        for cache_file in [CONFIG_CACHE_FILE, MANIFEST_CACHE_FILE]:
            if cache_file.exists():
                cache_file.unlink()
                silent_print(f"Cleared cache: {cache_file}")
    except Exception as e:
        silent_print(f"Error clearing cache: {e}")



def delete_zip_file(repo_name, version):
    """Delete a specific zip file"""
    zip_path = get_zip_path(repo_name, version)
    if zip_path.exists():
        zip_path.unlink()
        return True
    return False

def delete_all_cached_zips():
    """Delete all cached zip files in the firmware_downloads directory"""
    try:
        if not ZIP_STORAGE_DIR.exists():
            return 0
        
        deleted_count = 0
        for zip_file in ZIP_STORAGE_DIR.glob("*.zip"):
            try:
                zip_file.unlink()
                deleted_count += 1
                silent_print(f"Deleted cached zip: {zip_file.name}")
            except Exception as e:
                silent_print(f"Error deleting {zip_file.name}: {e}")
        
        return deleted_count
    except Exception as e:
        silent_print(f"Error deleting cached zips: {e}")
        return 0


class ConfigDownloader:
    """Downloads and parses configuration files from GitHub with caching"""

    def __init__(self):
        self.config_url = "https://innioasis.app/config.ini"
        self.manifest_url = "https://raw.githubusercontent.com/team-slide/slidia/refs/heads/main/slidia_manifest.xml"
        self.session = requests.Session()
        self.session.timeout = REQUEST_TIMEOUT

    def download_config(self):
        """Download and parse the config.ini file to extract API tokens with caching"""
        # Try cache first
        cached_tokens = load_cache(CONFIG_CACHE_FILE)
        if cached_tokens:
            return cached_tokens

        try:
            silent_print("Downloading tokens from remote config...")
            silent_print(f"Config URL: {self.config_url}")
            response = self.session.get(self.config_url, timeout=REQUEST_TIMEOUT)
            silent_print(f"Response status: {response.status_code}")

            if response.status_code != 200:
                silent_print(f"Failed to download config: HTTP {response.status_code}")
                silent_print(f"Response text: {response.text[:200]}...")
                
                # Check if it's a rate limit issue
                if response.status_code == 403:
                    silent_print("GitHub API rate limited - this is normal for unauthenticated requests")
                    silent_print("The app will work with limited functionality until rate limit resets")
                elif response.status_code == 404:
                    silent_print("Config file not found - check if the repository structure has changed")
                elif response.status_code >= 500:
                    silent_print("GitHub server error - temporary issue, will retry later")
                
                return []

            response.raise_for_status()

            config = configparser.ConfigParser()
            config.read_string(response.text)

            silent_print(f"Config sections found: {list(config.sections())}")

            tokens = []
            if 'api_keys' in config:
                silent_print("Found api_keys section")
                for key, value in config['api_keys'].items():
                    if key.startswith('key_') and value.strip():
                        # Handle different token formats
                        token = value.strip()

                        # Remove github_pat_ prefix if present (tokens are stored without prefix for obfuscation)
                        if token.startswith('github_pat_'):
                            token = token[11:]  # Remove prefix

                        # Store token without prefix for consistency
                        if token and len(token) > 10:  # Basic validation
                            tokens.append(token)
                            silent_print(f"Added token: {key} -> {token[:10]}...")

            # Also check legacy token
            if 'github' in config and 'token' in config['github']:
                silent_print("Found legacy github token")
                token = config['github']['token'].strip()

                # Store legacy token without prefix for consistency
                if token.startswith('github_pat_'):
                    token = token[11:]  # Remove prefix

                if token and len(token) > 10 and token not in tokens:
                    tokens.append(token)
                    silent_print(f"Added legacy token: {token[:10]}...")

            silent_print(f"Successfully loaded {len(tokens)} tokens from remote config")
            if tokens:
                silent_print(f"First token preview: {tokens[0][:10]}...")
                # Cache the tokens
                save_cache(CONFIG_CACHE_FILE, tokens)
            else:
                silent_print("No valid tokens found in config - will use unauthenticated mode")
            return tokens
        except Exception as e:
            silent_print(f"Error downloading config: {e}")
            silent_print("Falling back to unauthenticated requests only")
            return []

    def download_manifest(self, use_local_first=True):
        """Download and parse the XML manifest file with local-first loading for instant startup"""
        # Try cache first
        cached_packages = load_cache(MANIFEST_CACHE_FILE)
        if cached_packages:
            silent_print("Using cached manifest for instant startup")
            return cached_packages

        # Load local manifest first for instant startup
        if use_local_first:
            local_packages = self.load_local_manifest()
            if local_packages:
                silent_print(f"Loaded {len(local_packages)} packages from local manifest for instant startup")
                # Cache the local packages immediately
                save_cache(MANIFEST_CACHE_FILE, local_packages)
                # Start background refresh of remote manifest
                self.refresh_remote_manifest_async()
                return local_packages

        # Fallback to remote download if no local manifest
        return self.download_remote_manifest()

    def load_local_manifest(self):
        """Load manifest from local slidia_manifest.xml file"""
        try:
            local_manifest_path = Path("slidia_manifest.xml")
            if not local_manifest_path.exists():
                silent_print("Local manifest not found")
                return []
            
            silent_print("Loading local manifest for instant startup...")
            with open(local_manifest_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            root = ET.fromstring(content)
            packages = self.parse_manifest_xml(root)
            silent_print(f"Successfully loaded {len(packages)} packages from local manifest")
            return packages
        except Exception as e:
            silent_print(f"Error loading local manifest: {e}")
            return []

    def download_remote_manifest(self):
        """Download manifest from remote URL"""
        try:
            silent_print("Downloading remote manifest...")
            response = self.session.get(self.manifest_url, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()

            root = ET.fromstring(response.text)
            packages = self.parse_manifest_xml(root)
            silent_print(f"Successfully loaded {len(packages)} packages from remote manifest")
            # Cache the packages
            save_cache(MANIFEST_CACHE_FILE, packages)
            return packages
        except Exception as e:
            silent_print(f"Error downloading remote manifest: {e}")
            return []

    def parse_manifest_xml(self, root):
        """Parse XML manifest and return packages list"""
        packages = []
        
        # Handle the actual manifest structure with <slidia> root
        if root.tag == 'slidia':
            # Find all package elements within the slidia root
            for package in root.findall('package'):
                pkg_data = package.attrib
                package_info = {
                    'name': pkg_data.get('name', 'Unknown'),
                    'device_type': pkg_data.get('device_type', ''),
                    'repo': pkg_data.get('repo', ''),
                    'device': pkg_data.get('device', ''),
                    'url': pkg_data.get('url', ''),
                    'type': pkg_data.get('type', ''),
                    'handler': pkg_data.get('handler', '')
                }
                packages.append(package_info)
                silent_print(f"Parsed package: {package_info['name']} -> {package_info['repo']}")
        else:
            # Fallback to old structure for backward compatibility
            for package in root.findall('package'):
                pkg_data = package.attrib
                package_info = {
                    'name': pkg_data.get('name', 'Unknown'),
                    'device_type': pkg_data.get('device_type', ''),
                    'repo': pkg_data.get('repo', ''),
                    'device': pkg_data.get('device', ''),
                    'url': pkg_data.get('url', ''),
                    'type': pkg_data.get('type', ''),
                    'handler': pkg_data.get('handler', '')
                }
                packages.append(package_info)
                silent_print(f"Parsed package (fallback): {package_info['name']} -> {package_info['repo']}")
        
        return packages

    def refresh_remote_manifest_async(self):
        """Refresh manifest from remote source in background"""
        def refresh_worker():
            try:
                silent_print("Refreshing manifest from remote source in background...")
                remote_packages = self.download_remote_manifest()
                if remote_packages:
                    # Update the packages if we got a successful remote load
                    self.packages = remote_packages
                    silent_print(f"Background refresh completed: {len(remote_packages)} packages")
                else:
                    silent_print("Background refresh failed, keeping local manifest")
            except Exception as e:
                silent_print(f"Background manifest refresh error: {e}")
        
        # Start background refresh in a separate thread
        import threading
        refresh_thread = threading.Thread(target=refresh_worker, daemon=True)
        refresh_thread.start()


import time
import random
from collections import defaultdict

class GitHubAPI:
    """GitHub API wrapper for fetching release information with rate limiting and caching"""

    def __init__(self, tokens):
        self.tokens = tokens
        self.token_usage = defaultdict(int)  # Track API calls per token
        self.last_reset = time.time()
        self.hourly_limit = 25  # Limit calls per hour per token
        self.call_timestamps = defaultdict(list)  # Track call timestamps for rate limiting
        self.working_tokens = set()  # Track which tokens are known to work
        self.session = requests.Session()
        self.session.timeout = REQUEST_TIMEOUT

        # Unauthenticated rate limiting (more lenient: 60 requests per hour)
        self.unauth_calls = []
        self.unauth_hourly_limit = 60

        # Caching for releases to improve fallback reliability
        self.releases_cache = {}
        self.cache_duration = 3600  # 1 hour cache duration

    def get_next_token(self):
        """Get the next available token with load balancing and rate limiting"""
        if not self.tokens:
            return None

        current_time = time.time()

        # Clean up old timestamps (older than 1 hour)
        for token in self.call_timestamps:
            self.call_timestamps[token] = [ts for ts in self.call_timestamps[token]
                                         if current_time - ts < 3600]

        # Find tokens that haven't exceeded hourly limit
        available_tokens = []
        working_available = []
        regular_available = []

        for token in self.tokens:
            if len(self.call_timestamps[token]) < self.hourly_limit:
                available_tokens.append(token)
                if self.is_token_working(token):
                    working_available.append(token)
                else:
                    regular_available.append(token)

        if not available_tokens:
            # All tokens are rate limited, return None instead of infinite loop
            silent_print("All tokens are rate limited, returning None")
            return None

        # Prioritize working tokens, then fall back to regular tokens
        if working_available:
            selected_token = random.choice(working_available)
            silent_print(f"Using working token: {selected_token[:10]}...")
        else:
            selected_token = random.choice(regular_available)
            silent_print(f"Using regular token: {selected_token[:10]}...")

        # Record this API call
        self.call_timestamps[selected_token].append(current_time)

        # Ensure token has github_pat_ prefix for GitHub API
        if not selected_token.startswith('github_pat_'):
            selected_token = f"github_pat_{selected_token}"

        return selected_token

    def mark_token_working(self, token):
        """Mark a token as working (remove github_pat_ prefix if present)"""
        if token.startswith('github_pat_'):
            token = token[11:]  # Remove prefix
        self.working_tokens.add(token)
        silent_print(f"Marked token as working: {token[:10]}...")

    def is_token_working(self, token):
        """Check if a token is known to work"""
        if token.startswith('github_pat_'):
            token = token[11:]  # Remove prefix
        return token in self.working_tokens

    def can_make_unauth_request(self):
        """Check if we can make an unauthenticated request (rate limit: 30/hour)"""
        current_time = time.time()

        # Clean up old calls (older than 1 hour)
        self.unauth_calls = [ts for ts in self.unauth_calls if current_time - ts < 3600]

        # Check if we're under the limit
        if len(self.unauth_calls) < self.unauth_hourly_limit:
            return True

        silent_print(f"Unauthenticated rate limit reached ({len(self.unauth_calls)}/hour)")
        return False

    def record_unauth_request(self):
        """Record an unauthenticated API call"""
        self.unauth_calls.append(time.time())
        silent_print(f"Recorded unauthenticated API call ({len(self.unauth_calls)}/hour)")

    def retry_with_delay(self, func, *args, max_retries=3, delay=1):
        """Retry a function with exponential backoff"""
        for attempt in range(max_retries):
            try:
                result = func(*args)
                if result is not None:
                    return result
            except Exception as e:
                silent_print(f"Attempt {attempt + 1} failed: {e}")

            if attempt < max_retries - 1:
                time.sleep(delay * (2 ** attempt))  # Exponential backoff

        return None

    def make_authenticated_request(self, url, repo):
        """Make an authenticated request with robust token fallback"""
        # Try all available tokens in sequence
        for token in self.tokens:
            # Add github_pat_ prefix if not present
            full_token = token if token.startswith('github_pat_') else f'github_pat_{token}'
            
            headers = {
                'Authorization': f'token {full_token}',
                'Accept': 'application/vnd.github.v3+json'
            }

            try:
                response = self.session.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
                if response.status_code == 200:
                    # Mark this token as working
                    self.working_tokens.add(token)
                    return response
                elif response.status_code == 401:
                    silent_print(f"Token authentication failed for {repo} with token {token[:10]}...")
                    continue  # Try next token
                elif response.status_code == 403:
                    silent_print(f"Rate limited for {repo} with token {token[:10]}...")
                    continue  # Try next token
                else:
                    silent_print(f"Error getting release for {repo} with token {token[:10]}...: {response.status_code}")
                    continue  # Try next token
            except Exception as e:
                silent_print(f"Error getting release for {repo} with token {token[:10]}...: {e}")
                continue  # Try next token
        
        return None

    def get_latest_release(self, repo):
        """Get the latest release information for a repository with fallback"""
        url = f"https://api.github.com/repos/{repo}/releases/latest"

        # Try authenticated requests with all available tokens
        if self.tokens:
            response = self.make_authenticated_request(url, repo)
            if response:
                release_data = response.json()
                assets = release_data.get('assets', [])

                # Find firmware assets
                zip_asset = None
                for asset in assets:
                    if asset['name'].lower() == 'rom.zip':
                        zip_asset = asset
                        break

                result = {
                    'tag_name': release_data.get('tag_name', ''),
                    'name': release_data.get('name', ''),
                    'body': release_data.get('body', ''),
                    'download_url': zip_asset['browser_download_url'] if zip_asset else None,
                    'asset_name': zip_asset['name'] if zip_asset else None
                }
                
                # Cache this successful response
                if result['download_url']:
                    self.cache_releases(repo, [result])
                
                return result

        # Try unauthenticated as fallback (with rate limiting)
        if not self.can_make_unauth_request():
            silent_print("Unauthenticated rate limit reached, trying cached data...")
            # Try to get cached latest release if available
            cached_releases = self.get_cached_releases(repo)
            if cached_releases and len(cached_releases) > 0:
                latest_cached = cached_releases[0]  # First one should be latest
                silent_print(f"Returning cached latest release for {repo}: {latest_cached.get('tag_name', 'Unknown')}")
                return latest_cached
            return None

        try:
            self.record_unauth_request()
            response = self.session.get(url, timeout=REQUEST_TIMEOUT)
            if response.status_code == 200:
                release_data = response.json()
                assets = release_data.get('assets', [])

                # Find firmware assets
                zip_asset = None
                for asset in assets:
                    if asset['name'].lower() == 'rom.zip':
                        zip_asset = asset
                        break

                result = {
                    'tag_name': release_data.get('tag_name', ''),
                    'name': release_data.get('name', ''),
                    'body': release_data.get('body', ''),
                    'download_url': zip_asset['browser_download_url'] if zip_asset else None,
                    'asset_name': zip_asset['name'] if zip_asset else None
                }
                
                # Cache this successful response
                if result['download_url']:
                    self.cache_releases(repo, [result])
                
                return result
            elif response.status_code == 403:
                silent_print(f"Unauthenticated request rate limited for {repo}")
                # Try to get cached data if available
                cached_releases = self.get_cached_releases(repo)
                if cached_releases and len(cached_releases) > 0:
                    latest_cached = cached_releases[0]
                    silent_print(f"Returning cached latest release for {repo}: {latest_cached.get('tag_name', 'Unknown')}")
                    return latest_cached
            else:
                silent_print(f"Unauthenticated request failed for {repo}: {response.status_code}")
        except Exception as e:
            silent_print(f"Error getting release for {repo} unauthenticated: {e}")

        # Final fallback: try to get cached data
        cached_releases = self.get_cached_releases(repo)
        if cached_releases and len(cached_releases) > 0:
            latest_cached = cached_releases[0]
            silent_print(f"Returning cached latest release for {repo}: {latest_cached.get('tag_name', 'Unknown')}")
            return latest_cached

        return None

    def get_all_releases(self, repo):
        """Get all releases for a repository with improved performance"""
        url = f"https://api.github.com/repos/{repo}/releases"

        # Try authenticated requests with all available tokens
        if self.tokens:
            response = self.make_authenticated_request(url, repo)
            if response:
                silent_print(f"Authenticated response status: {response.status_code}")
                if response.status_code == 200:
                    releases_data = response.json()
                    silent_print(f"Found {len(releases_data)} total releases for {repo}")
                    releases = []

                    for release in releases_data:
                        assets = release.get('assets', [])
                        silent_print(f"Release {release.get('tag_name', 'Unknown')} has {len(assets)} assets")

                        # Find firmware assets
                        zip_asset = None
                        for asset in assets:
                            if asset['name'].lower() == 'rom.zip':
                                zip_asset = asset
                                silent_print(f"Found zip asset: {asset['name']}")
                                break

                        if zip_asset:  # Include releases with any zip file
                            releases.append({
                                'tag_name': release.get('tag_name', ''),
                                'name': release.get('name', ''),
                                'body': release.get('body', ''),
                                'published_at': release.get('published_at', ''),
                                'download_url': zip_asset['browser_download_url'],
                                'asset_name': zip_asset['name'],
                                'asset_size': zip_asset.get('size', 0)
                            })
                            silent_print(f"Added release {release.get('tag_name', 'Unknown')} with zip asset")
                        else:
                            silent_print(f"No zip assets found for release {release.get('tag_name', 'Unknown')}")

                    silent_print(f"Returning {len(releases)} releases with zip assets")
                    return releases

        # Try unauthenticated as fallback (with rate limiting)
        if not self.can_make_unauth_request():
            silent_print("Unauthenticated rate limit reached, trying alternative fallback...")
            # Try to get cached data if available
            cached_releases = self.get_cached_releases(repo)
            if cached_releases:
                silent_print(f"Returning {len(cached_releases)} cached releases for {repo}")
                return cached_releases
            
            # If no cached data and rate limited, try to make one more request anyway
            # This helps when the rate limit is just about to reset
            silent_print("Rate limited but trying one more request for critical data...")
            try:
                response = self.session.get(url, timeout=REQUEST_TIMEOUT)
                if response.status_code == 200:
                    silent_print("Rate limit bypass successful!")
                    releases_data = response.json()
                    releases = []
                    
                    for release in releases_data:
                        assets = release.get('assets', [])
                        zip_asset = None
                        for asset in assets:
                            if asset['name'].lower() == 'rom.zip':
                                zip_asset = asset
                                break
                        
                        if zip_asset:
                            releases.append({
                                'tag_name': release.get('tag_name', ''),
                                'name': release.get('name', ''),
                                'body': release.get('body', ''),
                                'published_at': release.get('published_at', ''),
                                'download_url': zip_asset['browser_download_url'],
                                'asset_name': zip_asset['name'],
                                'asset_size': zip_asset.get('size', 0)
                            })
                    
                    if releases:
                        self.cache_releases(repo, releases)
                        return releases
            except Exception as e:
                silent_print(f"Rate limit bypass failed: {e}")
            
            return []

        try:
            self.record_unauth_request()
            silent_print(f"Attempting unauthenticated request to {url}")
            response = self.session.get(url, timeout=REQUEST_TIMEOUT)
            silent_print(f"Unauthenticated response status: {response.status_code}")

            if response.status_code == 200:
                releases_data = response.json()
                silent_print(f"Unauthenticated: Found {len(releases_data)} total releases for {repo}")
                releases = []

                for release in releases_data:
                    assets = release.get('assets', [])

                    # Find any zip asset (more flexible than just rom.zip)
                    zip_asset = None
                    for asset in assets:
                        if asset['name'].lower() == 'rom.zip':
                            zip_asset = asset
                            break

                    if zip_asset:  # Include releases with any zip file
                        releases.append({
                            'tag_name': release.get('tag_name', ''),
                            'name': release.get('name', ''),
                            'body': release.get('body', ''),
                            'published_at': release.get('published_at', ''),
                            'download_url': zip_asset['browser_download_url'],
                            'asset_name': zip_asset['name'],
                            'asset_size': zip_asset.get('size', 0)
                        })

                silent_print(f"Unauthenticated: Returning {len(releases)} releases with zip assets")
                # Cache the successful unauthenticated response
                self.cache_releases(repo, releases)
                return releases
            elif response.status_code == 403:
                silent_print(f"Unauthenticated request rate limited for {repo}")
                # Try to get cached data if available
                cached_releases = self.get_cached_releases(repo)
                if cached_releases:
                    silent_print(f"Returning {len(cached_releases)} cached releases for {repo}")
                    return cached_releases
            else:
                silent_print(f"Unauthenticated request failed for {repo}: {response.status_code}")
        except Exception as e:
            silent_print(f"Error getting releases for {repo} unauthenticated: {e}")

        # Final fallback: try to get cached data
        cached_releases = self.get_cached_releases(repo)
        if cached_releases:
            silent_print(f"Returning {len(cached_releases)} cached releases for {repo}")
            return cached_releases

        silent_print(f"No releases found for {repo} - returning empty list")
        return []

    def get_cached_releases(self, repo):
        """Get cached releases for a repository if available and not expired"""
        if repo in self.releases_cache:
            cache_time, releases = self.releases_cache[repo]
            if time.time() - cache_time < self.cache_duration:
                silent_print(f"Using cached releases for {repo} (age: {time.time() - cache_time:.0f}s)")
                return releases
            else:
                # Remove expired cache entry
                del self.releases_cache[repo]
        return None

    def cache_releases(self, repo, releases):
        """Cache releases for a repository"""
        self.releases_cache[repo] = (time.time(), releases)
        silent_print(f"Cached {len(releases)} releases for {repo}")

    def clear_expired_cache(self):
        """Clear expired cache entries"""
        current_time = time.time()
        expired_repos = []
        for repo, (cache_time, _) in self.releases_cache.items():
            if current_time - cache_time >= self.cache_duration:
                expired_repos.append(repo)
        
        for repo in expired_repos:
            del self.releases_cache[repo]
            silent_print(f"Cleared expired cache for {repo}")

    def cleanup_cache_periodically(self):
        """Clean up expired cache entries periodically"""
        self.clear_expired_cache()
        # Schedule next cleanup in 10 minutes
        QTimer.singleShot(600000, self.cleanup_cache_periodically)





class DebugOutputWindow(QWidget):
    """Debug output window for showing mtk.py output in real-time"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("MTK Debug Output - Labs Mode")
        self.setGeometry(200, 200, 800, 600)
        
        # Create layout
        layout = QVBoxLayout(self)
        
        # Title label
        title_label = QLabel("MTK.py Output (Debug Mode)")
        title_label.setStyleSheet("font-size: 14px; font-weight: bold; margin: 5px;")
        layout.addWidget(title_label)
        
        # Output text area
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setFont(QFont("Consolas", 10))
        layout.addWidget(self.output_text)
        
        # Clear button
        clear_btn = QPushButton("Clear Output")
        clear_btn.clicked.connect(self.clear_output)
        layout.addWidget(clear_btn)
        
        # Close button
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)
    
    def append_output(self, text):
        """Append text to the output area"""
        self.output_text.append(text)
        # Auto-scroll to bottom
        cursor = self.output_text.textCursor()
        cursor.movePosition(cursor.End)
        self.output_text.setTextCursor(cursor)
    
    def clear_output(self):
        """Clear the output area"""
        self.output_text.clear()


class SPFlashToolWorker(QThread):
    """Worker thread for running SP Flash Tool command with real-time output"""

    status_updated = Signal(str)
    show_installing_image = Signal()
    show_initsteps_image = Signal()
    show_installed_image = Signal()
    show_please_wait_image = Signal()
    spflash_completed = Signal(bool, str)
    disable_update_button = Signal()  # Signal to disable update button during SP Flash Tool installation
    enable_update_button = Signal()   # Signal to enable update button when returning to ready state

    def __init__(self):
        super().__init__()
        self.should_stop = False
        # Set up the flash_tool.exe command with the XML file
        current_dir = Path.cwd()
        self.spflash_command = [
            str(current_dir / "flash_tool.exe"),
            "-i",
            str(current_dir / "install_rom_sp.xml")
        ]
        
    def stop(self):
        """Stop the SP Flash Tool worker"""
        self.should_stop = True

    def run(self):
        """Run the SP Flash Tool command and monitor output"""
        try:
            silent_print(f"Starting SP Flash Tool command: {self.spflash_command}")
            
            # Start the flash_tool.exe process
            process = subprocess.Popen(
                self.spflash_command,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=0,
                universal_newlines=True
            )
            
            # Ensure process doesn't hang indefinitely
            process_timeout = 1800  # 30 minutes timeout for SP Flash Tool
            process_start_time = time.time()
            
            # Phase tracking variables
            please_wait_phase = True  # Start with please wait phase
            instructions_phase = False
            installing_phase = False
            completed_phase = False
            
            # Read output line by line
            while True:
                if self.should_stop:
                    if process.poll() is None:
                        process.terminate()
                    break
                    
                # Check for timeout
                if time.time() - process_start_time > process_timeout:
                    silent_print("SP Flash Tool process timeout - terminating")
                    process.terminate()
                    break
                
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                    
                if output:
                    line = output.strip()
                    silent_print(f"{line}")
                    
                    # Phase detection based on flash_tool.exe output patterns
                    
                    # Please wait phase: Show "Please wait..." until "Search usb" is detected
                    if please_wait_phase and not line.startswith("Search usb"):
                        # Keep showing please wait image and status
                        self.show_please_wait_image.emit()
                        self.status_updated.emit("Please wait...")
                        # Don't emit the actual flash tool output yet
                        continue
                    
                    # Instructions phase: When "Search usb" is detected, show instructions
                    elif line.startswith("Search usb"):
                        please_wait_phase = False
                        instructions_phase = True
                        installing_phase = False
                        completed_phase = False
                        self.show_initsteps_image.emit()
                        self.status_updated.emit("Please turn off your Y1 (or insert paperclip in hidden button) and connect it via USB")
                        # Don't show the raw flash tool output, keep the user-friendly message
                        
                    # Continue with instructions phase until installing phase
                    elif instructions_phase and not installing_phase and not completed_phase:
                        if ("Downloading" in line or
                            "Downloading & Connecting to DA" in line or
                            "connect DA end stage" in line or
                            "COM port is open" in line or
                            "Download DA now" in line or
                            "Formatting Flash" in line or
                            "Format Succeeded" in line or
                            "executing DADownloadAll" in line or
                            "DA report" in line or
                            "% of" in line or
                            "download speed" in line or
                            "Download Succeeded" in line):
                            # Transition to installing phase
                            instructions_phase = False
                            installing_phase = True
                            self.show_installing_image.emit()
                            self.disable_update_button.emit()
                            self.status_updated.emit(f"{line}")
                        else:
                            # Continue showing instructions and flash tool output
                            self.status_updated.emit(f"{line}")
                        
                    # Installing phase: Downloading and flashing operations
                    elif installing_phase and not completed_phase:
                        if ("Downloading" in line or
                            "Downloading & Connecting to DA" in line or
                            "connect DA end stage" in line or
                            "COM port is open" in line or
                            "Download DA now" in line or
                            "Formatting Flash" in line or
                            "Format Succeeded" in line or
                            "executing DADownloadAll" in line or
                            "DA report" in line or
                            "% of" in line or
                            "download speed" in line or
                            "Download Succeeded" in line):
                            self.status_updated.emit(f"{line}")
                        elif (line.startswith("Disconnect!") or
                              "All command exec done!" in line or
                              "FlashTool_EnableWatchDogTimeout" in line):
                            # Transition to completion phase
                            completed_phase = True
                            installing_phase = False
                            if line.startswith("Disconnect!"):
                                self.show_installed_image.emit()
                                self.status_updated.emit("Install Complete, please disconnect your Y1 and hold the center button")
                            else:
                                self.show_installing_image.emit()  # Use installing image for other completion indicators
                                self.status_updated.emit(f"Flash Tool: {line}")
                        else:
                            self.status_updated.emit(f"Flash Tool: {line}")
                        
                    # Completion phase: Final cleanup and disconnection
                    elif completed_phase:
                        if line.startswith("Disconnect!"):
                            self.show_installed_image.emit()
                            self.status_updated.emit("Install Complete, please disconnect your Y1 and hold the center button")
                        else:
                            self.status_updated.emit(f"Flash Tool: {line}")
                        
                        
                    # Other output
                    else:
                        self.status_updated.emit(f"Flash Tool: {line}")
            
            # Wait for process to complete
            process.wait()
            
            # Determine success based on completion phase
            if completed_phase:
                silent_print("Flash Tool completed successfully")
                self.spflash_completed.emit(True, "Software installation completed successfully")
            else:
                silent_print("Flash Tool did not complete successfully")
                self.spflash_completed.emit(False, "Please check that drivers are installed and that you restarted your computer")
                
        except Exception as e:
            silent_print(f"Error running Flash Tool: {e}")
            self.spflash_completed.emit(False, f"Error running Flash Tool: {e}")
        finally:
            self.enable_update_button.emit()


class MTKWorker(QThread):
    """Worker thread for running MTK command with real-time output"""

    status_updated = Signal(str)
    show_installing_image = Signal()
    show_reconnect_image = Signal()
    show_presteps_image = Signal()
    show_please_wait_image = Signal()  # Signal for showing please_wait image during "Please wait..." status
    show_initsteps_image = Signal()  # New signal for showing initsteps after first empty line
    show_instructions_image = Signal()  # Signal for showing initsteps when instructions are displayed
    mtk_completed = Signal(bool, str)
    handshake_failed = Signal()  # New signal for handshake failures
    errno2_detected = Signal()   # New signal for errno2 errors
    usb_io_error_detected = Signal()  # New signal for USB IO errors
    backend_error_detected = Signal()  # New signal for backend errors
    keyboard_interrupt_detected = Signal()  # New signal for keyboard interrupts
    show_try_again_dialog = Signal()  # New signal for showing try again dialog
    disable_update_button = Signal()  # Signal to disable update button during MTK installation
    enable_update_button = Signal()   # Signal to enable update button when returning to ready state

    def __init__(self, debug_mode=False, debug_window=None):
        super().__init__()
        self.should_stop = False
        self.debug_mode = debug_mode
        self.debug_window = debug_window
        self.initsteps_timer = None  # Timer for 1.5 second delay fallback
        
        # Platform-specific progress bar characters
        if platform.system() == "Windows":
            # Windows: Use ASCII characters that display properly
            self.progress_filled = "#"
            self.progress_empty = "-"
        else:
            # Linux/macOS: Use box drawing characters
            self.progress_filled = "█"
            self.progress_empty = "░"

    def stop(self):
        """Stop the MTK worker"""
        self.should_stop = True

    def fix_progress_bar_chars(self, line):
        """Fix progress bar characters for platform compatibility"""
        if platform.system() == "Windows":
            # Replace box drawing characters with ASCII equivalents on Windows
            line = line.replace("█", self.progress_filled)
            line = line.replace("░", self.progress_empty)
            # Also handle other common box drawing characters that might appear
            line = line.replace("â-ª", self.progress_filled)  # Common mojibake
            line = line.replace("â", self.progress_filled)    # Partial mojibake
            line = line.replace("ª", self.progress_empty)     # Partial mojibake
        return line

    def run(self):
        cmd = [
            sys.executable, "mtk.py", "w",
            "uboot,bootimg,recovery,android,usrdata",
            "lk.bin,boot.img,recovery.img,system.img,userdata.img"
        ]

        try:
            # Don't emit status message - let MTK output be displayed clearly
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=0,
                universal_newlines=True
            )
            
            # Ensure process doesn't hang indefinitely
            process_timeout = 300  # 5 minutes timeout
            process_start_time = time.time()

            device_detected = False
            flashing_started = False
            handshake_error_detected = False
            errno2_error_detected = False
            backend_error_detected = False
            keyboard_interrupt_detected = False
            usb_connection_issue_detected = False
            usb_io_error_detected = False
            last_output_line = ""
            successful_completion = False
            first_empty_line_detected = False  # Track if we've seen the first empty line
            initsteps_start_time = None  # Track when initsteps phase started
            initsteps_timeout = 12  # 12 seconds timeout for initsteps phase
            last_status_update = time.time()  # Track when status was last updated
            status_check_interval = 2  # Check status every 2 seconds
            current_status = ""  # Track current status message

            # Interruption detection variables
            progress_detected = False
            last_progress_time = None
            interruption_timeout = 3.0  # 3 seconds timeout
            
            # Track installation state
            active_installation_started = False
            last_wrote_line_seen = False

            # Start 1.5 second timer as fallback to show initsteps if no empty line is detected
            self.initsteps_timer = QTimer()
            self.initsteps_timer.setSingleShot(True)
            # Timer callback will be checked inside the main loop where active_installation_started is available
            self.initsteps_timer.start(1500)  # 1.5 seconds

            while True:
                # Check for timeout - but don't terminate during active installation
                if time.time() - process_start_time > process_timeout:
                    if active_installation_started:
                        silent_print("MTK process timeout during active installation - continuing to wait for completion")
                        # Don't terminate during active installation, just continue waiting
                    else:
                        silent_print("MTK process timeout - terminating")
                        process.terminate()
                        break
                
                # Check if we need to update status due to lack of output
                current_time = time.time()
                if current_time - last_status_update > status_check_interval:
                    # If no output for a while, emit empty status to trigger instruction message
                    # But only if we're not in a specific status state like "Please wait..." or active install
                    if current_status not in ["Please wait...", "Please disconnect your Y1 and restart the app"] and not progress_detected and not active_installation_started:
                        self.status_updated.emit("")
                        self.show_instructions_image.emit()
                        last_status_update = current_time
                
                # Check if initsteps timer has expired and show initsteps if appropriate
                if hasattr(self, 'initsteps_timer') and not self.initsteps_timer.isActive() and not first_empty_line_detected and not active_installation_started:
                    self.show_initsteps_image.emit()
                    first_empty_line_detected = True  # Mark as detected to prevent multiple emissions
                    
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    # Small delay to keep GUI responsive
                    time.sleep(0.01)  # 10ms delay
                    line = output.strip()
                    last_output_line = line  # Track the last output line

                    # Check for first empty line from mtk.py and emit initsteps signal
                    if not first_empty_line_detected and line == "":
                        first_empty_line_detected = True
                        # Only show initsteps if not in active installation
                        if not active_installation_started:
                            self.show_initsteps_image.emit()

                    # Fix progress bar characters for platform compatibility
                    fixed_line = self.fix_progress_bar_chars(line)
                    
                    # CRITICAL: Set active_installation_started IMMEDIATELY when first progress or wrote line is detected
                    # This must happen before any other processing to prevent initsteps.png from showing
                    if not active_installation_started and ("progress" in line.lower() or line.lower().startswith("wrote")):
                        active_installation_started = True
                        silent_print("Active installation started - process will not be terminated until completion")
                    
                    # Show debug output in separate window if debug mode is enabled
                    if self.debug_mode and self.debug_window:
                        self.debug_window.append_output(f"MTK: {fixed_line}")
                    
                    # Check if this is empty status or dots (awaiting connection) and show installing.png
                    if device_detected and (fixed_line == "" or fixed_line.startswith(".") or fixed_line.strip() == ""):
                        # Only show installing.png if we're in active installation state
                        if active_installation_started:
                            self.show_installing_image.emit()
                        # Mark initsteps phase start time
                        if initsteps_start_time is None:
                            initsteps_start_time = time.time()
                    
                    # Handle status message replacement for blank/dots output
                    if fixed_line == "" or fixed_line.startswith(".") or fixed_line.strip() == "":
                        # Only show instruction message if not in active installation
                        if not active_installation_started:
                            # When mtk.py only displays blank output or dots/periods, show instruction message
                            self.status_updated.emit("Please follow the instructions below to install the software on your Y1")
                            current_status = "Please follow the instructions below to install the software on your Y1"
                            # Only show initsteps image if we're not in an active install (no progress detected) AND not in active installation state
                            if not progress_detected and not active_installation_started:
                                self.show_instructions_image.emit()
                            last_status_update = time.time()  # Update status time
                        
                        # Check if we've been in initsteps phase too long - but not during active installation
                        if initsteps_start_time is not None and (time.time() - initsteps_start_time) > initsteps_timeout:
                            # Only kill the process if we're not in active installation state
                            if not active_installation_started:
                                # Kill the process and restart
                                if process.poll() is None:
                                    process.terminate()
                                self.show_try_again_dialog.emit()
                                break
                            else:
                                # During active installation, just reset the timer to prevent false termination
                                initsteps_start_time = time.time()
                                silent_print("Reset initsteps timer during active installation")
                    else:
                        # Show latest output in status area (no extra whitespace)
                        self.status_updated.emit(f"MTK: {fixed_line}")
                        current_status = f"MTK: {fixed_line}"  # Track current status
                        # Reset initsteps timer when we get real output
                        initsteps_start_time = None
                        last_status_update = time.time()  # Update status time

                    # Check for errno2 error
                    if "errno2" in line.lower():
                        errno2_error_detected = True
                        self.status_updated.emit("Errno2 detected - Innioasis Updater reinstall required")
                    
                    # Check for USBError(5) - Input/Output Error (SP Flash Tool sparse images)
                    if "usberror(5" in line.lower() or "input/output error" in line.lower():
                        usb_io_error_detected = True
                        self.status_updated.emit("USBError(5) - ROM incompatible with Method 1")
                        self.usb_io_error_detected.emit()
                        # Don't break here - continue reading output

                    # Check for handshake failed error (generalized detection)
                    if any(phrase in line.lower() for phrase in [
                        "handshake failed", 
                        "handshake error", 
                        "connection failed", 
                        "device not responding",
                        "timeout",
                        "connection timeout",
                        "device timeout",
                        "no device found",
                        "device not found",
                        "connection refused",
                        "failed to connect",
                        "connection error"
                    ]):
                        handshake_error_detected = True
                        self.status_updated.emit("Connection issue detected - please unplug your Y1 and try again")
                        self.handshake_failed.emit()
                        # Don't break here - continue reading output

                    # Check for backend error
                    if "nobackenderror" in line.lower() or "no backend available" in line.lower():
                        backend_error_detected = True
                        self.status_updated.emit("Backend error detected - libusb backend issue")
                        self.backend_error_detected.emit()
                        # Don't break here - continue reading output

                    # Check for USB connection issue (AttributeError: 'NoneType' object has no attribute 'hex')
                    if "attributerror: 'nonetype' object has no attribute 'hex'" in line.lower():
                        usb_connection_issue_detected = True
                        self.status_updated.emit("Please unplug the USB cable from your Y1 and reconnect it.")
                        self.show_reconnect_image.emit()
                        # Don't break here - continue reading output

                    # Check for keyboard interrupt
                    if "keyboardinterrupt" in line.lower() or "keyboard interrupt" in line.lower() or "interrupted by user" in line.lower():
                        keyboard_interrupt_detected = True
                        self.status_updated.emit("Something stopped the install process, give it another try...")
                        self.keyboard_interrupt_detected.emit()
                        # Don't break here - continue reading output

                    # Check for Preloader status (indicates slow USB connection or freeze)
                    if "preloader" in line.lower():
                        if ".........." in line:
                            # This indicates slow USB connection, show appropriate status - here is where we'll implement the automatic restart of the firmware installation for Method 1 - this makes more sense than the app freezing - which it almost always does in scenarios where this message will be shown
                            self.status_updated.emit("USB connection timed out. Please force quit the app if not responding and restart it.")
                            # Show initsteps image for instruction message - but not during active installation
                            if not active_installation_started:
                                self.show_instructions_image.emit()
                            last_status_update = time.time()  # Update status time
                        else:
                            # Just "Preloader" without dots indicates freeze state
                            self.status_updated.emit("MTK: Preloader")
                            current_status = "MTK: Preloader"  # Track current status
                            # Show initsteps image for instruction message - but not during active installation
                            if not active_installation_started:
                                self.show_instructions_image.emit()
                            last_status_update = time.time()  # Update status time
                    
                    # Check for BROM status (indicates waiting for device)
                    if "brom" in line.lower():
                        # This indicates waiting for device, show please wait message
                        self.status_updated.emit("Please wait...")
                        current_status = "Please wait..."  # Track current status
                        # Show please_wait image for please wait status
                        self.show_please_wait_image.emit()
                        last_status_update = time.time()  # Update status time
                        # Don't treat this as an error, just continue

                    if ".Port - Device detected :)" in line:
                        device_detected = True
                        # Don't switch to installing.png yet - wait for proper timing

                    # Check if flashing has started (look for write operations)
                    if device_detected and ("Write" in line or "Progress:" in line) and not flashing_started:
                        flashing_started = True

                    # Check for progress indicator and show installing.png
                    if "progress" in line.lower():
                        self.show_installing_image.emit()
                        # Disable update button when MTK installation starts
                        self.disable_update_button.emit()
            # Track progress for interruption detection
            progress_detected = True
            last_progress_time = time.time()
            # Don't emit status message - let MTK output be displayed clearly
            
            # Check for Progress or Wrote lines to show installing.png and display output in status
            if "progress" in line.lower() or line.lower().startswith("wrote"):
                self.show_installing_image.emit()
                # Display the actual mtk.py output in status field
                self.status_updated.emit(f"MTK: {fixed_line}")
                current_status = f"MTK: {fixed_line}"
                last_status_update = time.time()
                
                # active_installation_started is now set immediately when progress/wrote is first detected above
                
                # Track if we've seen a "Wrote" line
                if line.lower().startswith("wrote"):
                    last_wrote_line_seen = True
                    silent_print("Wrote line detected - installation may be completing")

                    # Only show presteps if no device detected and no errors
                    if not device_detected and not usb_connection_issue_detected and not handshake_error_detected and not errno2_error_detected and not backend_error_detected and not keyboard_interrupt_detected:
                        self.show_presteps_image.emit()

            # If any error was detected, continue reading but mark for completion
            if handshake_error_detected or errno2_error_detected or backend_error_detected or keyboard_interrupt_detected:
                # Continue reading output to show user what's happening
                while True:
                    # Check for timeout - but don't terminate during active installation
                    if time.time() - process_start_time > process_timeout:
                        if active_installation_started:
                            silent_print("MTK process timeout during active installation error reading - continuing to wait for completion")
                            # Don't terminate during active installation, just continue waiting
                        else:
                            silent_print("MTK process timeout during error reading - terminating")
                            process.terminate()
                            break
                        
                    output = process.stdout.readline()
                    if output == '' and process.poll() is not None:
                        break
                    if output:
                        # Small delay to keep GUI responsive
                        time.sleep(0.01)  # 10ms delay
                        line = output.strip()
                        # Fix progress bar characters for platform compatibility
                        fixed_line = self.fix_progress_bar_chars(line)
                        # Show latest output in status area (no extra whitespace)
                        self.status_updated.emit(f"MTK: {fixed_line}")

            # Wait for process to complete
            process.wait()

            # Check if process completed before device detection
            if not device_detected:
                if process.returncode != 0:
                    # Process failed before device detection
                    successful_completion = False
                else:
                    successful_completion = True
            else:
                # Device was detected, check completion based on progress
                if progress_detected and last_progress_time:
                    time_since_last_progress = time.time() - last_progress_time
                    if time_since_last_progress > interruption_timeout:
                        # Process was interrupted - no progress for 3+ seconds
                        # But only if we're not in active installation state
                        if active_installation_started:
                            # During active installation, wait longer for completion
                            if time_since_last_progress > (interruption_timeout * 2):  # Double the timeout during active installation
                                successful_completion = False
                            else:
                                # Still in active installation, consider it successful if process exited normally
                                successful_completion = (process.returncode == 0)
                        else:
                            successful_completion = False
                    else:
                        # Check if the last progress was 100% or if process completed normally
                        # Also check if the last line begins with "wrote" (indicates successful completion)
                        if "100%" in last_output_line or process.returncode == 0 or last_output_line.lower().startswith("wrote"):
                            successful_completion = True
                        else:
                            # Process stopped before 100% - likely interrupted
                            successful_completion = False
                else:
                    # No progress was detected, check if process completed successfully
                    # Also check if the last line begins with "wrote" (indicates successful completion)
                    if process.returncode == 0 or last_output_line.lower().startswith("wrote"):
                        successful_completion = True
                    else:
                        successful_completion = False

        except Exception as e:
            silent_print(f"MTK Worker error: {str(e)}")
            self.status_updated.emit(f"MTK error: {str(e)}")
            successful_completion = False
            # Ensure process is terminated on error
            try:
                if 'process' in locals() and process.poll() is None:
                    process.terminate()
            except:
                pass

        # Clean up timer
        if self.initsteps_timer:
            self.initsteps_timer.stop()
            self.initsteps_timer = None

        # Enable update button when returning to ready state
        self.enable_update_button.emit()

        if self.should_stop:
            self.mtk_completed.emit(False, "MTK command cancelled")
        elif usb_connection_issue_detected:
            self.mtk_completed.emit(False, "USB connection issue - please reconnect device")
        elif handshake_error_detected:
            self.mtk_completed.emit(False, "Handshake failed - driver setup required")
        elif errno2_error_detected:
            self.mtk_completed.emit(False, "Errno2 error - Innioasis Updater reinstall required")
        elif usb_io_error_detected:
            self.mtk_completed.emit(False, "USBError(5) - ROM incompatible with Method 1")
        elif backend_error_detected:
            self.mtk_completed.emit(False, "Backend error - libusb backend issue")
        elif keyboard_interrupt_detected:
            self.mtk_completed.emit(False, "Something stopped the install process, give it another try...")
        elif successful_completion:
            self.mtk_completed.emit(True, "Install completed successfully")
        else:
            # Process ended but was interrupted (no progress for 3+ seconds)
            self.mtk_completed.emit(False, "Install process interrupted - please try again")


class DownloadWorker(QThread):
    """Worker thread for downloading and processing firmware"""

    progress_updated = Signal(int)
    status_updated = Signal(str)
    download_completed = Signal(bool, str)

    def __init__(self, download_url, repo_name, version):
        super().__init__()
        self.download_url = download_url
        self.repo_name = repo_name
        self.version = version

    def run(self):
        try:
            self.status_updated.emit("Downloading...")

            # Download the file
            response = requests.get(self.download_url, stream=True, timeout=30)
            response.raise_for_status()

            total_size = int(response.headers.get('content-length', 0))
            downloaded = 0
            start_time = time.time()

            # Create downloads directory if it doesn't exist
            ZIP_STORAGE_DIR.mkdir(exist_ok=True)

            zip_path = get_zip_path(self.repo_name, self.version)

            with open(zip_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_size > 0:
                            progress = int((downloaded / total_size) * 100)
                            self.progress_updated.emit(progress)

                            # Calculate ETA
                            elapsed_time = time.time() - start_time
                            if elapsed_time > 0:
                                download_speed = downloaded / elapsed_time
                                remaining_bytes = total_size - downloaded
                                eta_seconds = remaining_bytes / download_speed if download_speed > 0 else 0

                                # Format ETA
                                if eta_seconds < 60:
                                    eta_str = f"{eta_seconds:.0f}s"
                                elif eta_seconds < 3600:
                                    eta_str = f"{eta_seconds/60:.0f}m"
                                else:
                                    eta_str = f"{eta_seconds/3600:.1f}h"

                                # Format file size
                                downloaded_mb = downloaded / (1024 * 1024)
                                total_mb = total_size / (1024 * 1024)

                                status_msg = f"Downloading... {progress}% ({downloaded_mb:.1f}MB / {total_mb:.1f}MB) - ETA: {eta_str}"
                                self.status_updated.emit(status_msg)

            self.status_updated.emit("Download completed. Extracting...")

            # Extract the zip file
            extracted_files = []
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(".")
                # Get list of extracted files
                extracted_files = zip_ref.namelist()

            # Log extracted files for cleanup
            log_extracted_files(extracted_files)

            self.status_updated.emit("Extraction completed. Files ready for MTK processing.")

            # Check if required files exist
            required_files = ["lk.bin", "boot.img", "recovery.img", "system.img", "userdata.img"]
            missing_files = []
            for file in required_files:
                if not Path(file).exists():
                    missing_files.append(file)

            if missing_files:
                error_msg = f"Missing required files: {', '.join(missing_files)}"
                self.download_completed.emit(False, error_msg)
                return

            # Show success message with file list and instructions
            success_msg = "Firmware files successfully extracted:\n"
            for file in required_files:
                file_size = Path(file).stat().st_size
                size_mb = file_size / (1024 * 1024)
                success_msg += f"- {file} ({size_mb:.1f} MB)\n"

            success_msg += "\nFor the best results:\n"
            success_msg += "1. Make sure your Y1 is disconnect until you're asked\n"
            success_msg += "2. Follow the on screen guidance during the process"
            success_msg += f""
            success_msg += ""

            self.download_completed.emit(True, success_msg)

        except Exception as e:
            self.download_completed.emit(False, f"Error: {str(e)}")


class ThemeMonitor(QObject):
    """Monitors system theme changes and emits signals for UI updates"""
    theme_changed = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.running = False
        self.thread = None
        self.last_theme = None
        
    def start_monitoring(self):
        """Start the theme monitoring thread"""
        if self.running:
            return
            
        self.running = True
        self.thread = threading.Thread(target=self._monitor_theme, daemon=True)
        self.thread.start()
        
    def stop_monitoring(self):
        """Stop the theme monitoring thread"""
        self.running = False
        if self.thread:
            self.thread.join(timeout=1.0)
            
    def _monitor_theme(self):
        """Background thread that monitors system theme changes"""
        while self.running:
            try:
                current_theme = self._get_current_theme()
                if current_theme != self.last_theme:
                    self.last_theme = current_theme
                    self.theme_changed.emit()
                time.sleep(1.0)  # Check every second
            except Exception as e:
                # Silently handle errors to prevent thread crashes
                time.sleep(2.0)
                
    def _get_current_theme(self):
        """Get the current system theme (light/dark)"""
        try:
            if platform.system() == "Darwin":  # macOS
                return self._get_macos_theme()
            elif platform.system() == "Windows":  # Windows
                return self._get_windows_theme()
            else:  # Linux and others
                return self._get_linux_theme()
        except:
            return "unknown"
            
    def _get_macos_theme(self):
        """Get macOS theme using system preferences"""
        try:
            import subprocess
            result = subprocess.run(['defaults', 'read', '-g', 'AppleInterfaceStyle'], 
                                  capture_output=True, text=True, timeout=2)
            return "dark" if result.returncode == 0 and result.stdout.strip() else "light"
        except:
            return "light"
            
    def _get_windows_theme(self):
        """Get Windows theme using registry"""
        try:
            import winreg
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, 
                              r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize") as key:
                value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
                return "light" if value else "dark"
        except:
            return "light"
            
    def _get_linux_theme(self):
        """Get Linux theme using environment variables"""
        try:
            # Check common environment variables
            gtk_theme = os.environ.get('GTK_THEME', '').lower()
            if 'dark' in gtk_theme:
                return "dark"
            elif 'light' in gtk_theme:
                return "light"
                
            # Check for dark mode indicators
            color_scheme = os.environ.get('COLORSCHEME', '').lower()
            if 'dark' in color_scheme:
                return "dark"
            elif 'light' in color_scheme:
                return "light"
                
            return "light"  # Default to light
        except:
            return "light"


class FirmwareDownloaderGUI(QMainWindow):
    """Main GUI window for the firmware downloader"""

    def __init__(self):
        super().__init__()
        self.config_downloader = ConfigDownloader()
        self.github_api = None
        self.packages = []
        self.download_worker = None
        self.mtk_worker = None
        self.images_loaded = False  # Track if images are loaded
        # Set default installation method based on platform
        if platform.system() == "Windows":
            self.installation_method = "spflash"  # Default to Method 1 (Guided) on Windows
        else:
            self.installation_method = "guided"  # Default to Method 1 (Guided) on other platforms
        # Always use method functionality removed - app now always defaults to Method 1
        self.debug_mode = False  # Default debug mode disabled
        self.last_attempted_method = None  # Track the last attempted installation method
        
        # Initialize shortcut settings with defaults (Windows only)
        if platform.system() == "Windows":
            # Legacy settings (kept for compatibility)
            self.desktop_shortcuts_enabled = True  # Default to enabled
            self.startmenu_shortcuts_enabled = True  # Default to enabled
            self.auto_cleanup_enabled = True  # Default to enabled
            
            # New individual shortcut settings with proper defaults
            self.desktop_updater_enabled = True  # Desktop: Innioasis Updater.lnk
            self.desktop_toolkit_enabled = False  # Desktop: No Toolkit
            self.startmenu_updater_enabled = True  # Start Menu: Innioasis Updater.lnk
            self.startmenu_toolkit_enabled = True  # Start Menu: Innioasis Toolkit.lnk
        
        # Initialize automatic utility updates setting (all platforms)
        self.auto_utility_updates_enabled = True  # Default to enabled

        # Initialize theme monitor for dynamic theme switching
        self.theme_monitor = ThemeMonitor(self)
        self.theme_monitor.theme_changed.connect(self.refresh_button_styles)
        self.theme_monitor.start_monitoring()

        # Initialize UI first for immediate responsiveness
        self.init_ui()

        # Handle version check file and macOS app update message (non-blocking)
        QTimer.singleShot(50, self.handle_version_check)

        # Clean up any previously extracted files at startup (non-blocking)
        QTimer.singleShot(50, cleanup_extracted_files)

        # Clean up orphaned processes at startup (Windows only, non-blocking)
        if platform.system() == "Windows":
            QTimer.singleShot(50, self.stop_flash_tool_processes)

        # Check for SP Flash Tool on Windows before loading data
        if platform.system() == "Windows":
            # Delay the flash tool check to avoid blocking startup
            QTimer.singleShot(100, self.check_sp_flash_tool)
            # Download troubleshooting shortcuts if missing
            QTimer.singleShot(200, self.ensure_troubleshooting_shortcuts)
            # Check for old shortcuts and offer cleanup
            QTimer.singleShot(400, self.check_and_cleanup_old_shortcuts)

        # Check for failed installation and show troubleshooting options
        QTimer.singleShot(300, self.check_failed_installation_on_startup)
        
        # Clean up RockboxUtility.zip at startup
        QTimer.singleShot(500, self.cleanup_rockbox_utility_zip)
        
        # Check for UsbDk cleanup on Windows - DISABLED
        # UsbDk cleanup prompt removed as it doesn't actually remove anything
        # if platform.system() == "Windows":
        #     QTimer.singleShot(600, self.check_usbdk_cleanup)

        # Ensure troubleshooting shortcuts are available
        QTimer.singleShot(500, self.ensure_troubleshooting_shortcuts_available)

        # Download latest updater.py during launch
        QTimer.singleShot(600, self.download_latest_updater)

        # Preload critical images with web fallback
        QTimer.singleShot(700, self.preload_critical_images)

        # Load data asynchronously to avoid blocking UI
        QTimer.singleShot(100, self.load_data)
        
        # Load saved installation preferences
        QTimer.singleShot(200, self.load_installation_preferences)
        
        # Apply shortcut settings on startup (Windows only)
        if platform.system() == "Windows":
            QTimer.singleShot(300, self.apply_shortcut_settings_on_startup)
        
        # Check for macOS one-time update file and restore preferences
        if platform.system() == "Darwin":
            QTimer.singleShot(400, self.check_macos_one_time_update)
        
        # Restore original installation method when session ends
        QTimer.singleShot(300, self.restore_original_installation_method)

        # Set up theme change detection timer
        self.theme_check_timer = QTimer()
        self.theme_check_timer.timeout.connect(self.check_theme_change)
        self.theme_check_timer.start(1000)  # Check every second
        self.last_theme_state = self.is_dark_mode

    def handle_version_check(self):
        """Handle version check file and show macOS app update message for new users"""
        try:
            version_file = Path(".version")
            current_version = "1.6.8"
            
            # Read the last used version
            last_version = None
            if version_file.exists():
                try:
                    last_version = version_file.read_text().strip()
                except Exception as e:
                    logging.warning(f"Could not read .version file: {e}")
            
            # Write current version to file
            try:
                version_file.write_text(current_version)
            except Exception as e:
                logging.warning(f"Could not write .version file: {e}")
            
            # macOS app update message removed as requested
                
        except Exception as e:
            logging.error(f"Error in handle_version_check: {e}")

    def check_sp_flash_tool(self):
        """Check if any flash tool is running on Windows and show warning"""
        try:
            # Use tasklist to get all running processes
            result = subprocess.run(['tasklist', '/FO', 'CSV'], 
                                  capture_output=True, text=True, timeout=5)
            
            if result.returncode == 0:
                # Check for any executable containing "flash" in the name
                flash_processes = []
                for line in result.stdout.split('\n'):
                    if 'flash' in line.lower() and '.exe' in line.lower():
                        # Extract the process name from CSV format
                        parts = line.split(',')
                        if len(parts) >= 2:
                            process_name = parts[0].strip('"')
                            if 'flash' in process_name.lower():
                                flash_processes.append(process_name)
                
                if flash_processes:
                    # Flash tool(s) detected, show warning dialog
                    process_list = '\n'.join(f"• {process}" for process in flash_processes)
                    msg_box = QMessageBox(self)
                    msg_box.setWindowTitle("Flash Tool Detected")
                    msg_box.setIcon(QMessageBox.Warning)
                    msg_box.setText("Flash tool(s) are currently running on your system.")
                    msg_box.setInformativeText(
                        f"The following flash tool(s) must be closed before running Innioasis Updater "
                        f"to prevent conflicts with USB device access and flashing operations:\n\n"
                        f"{process_list}\n\n"
                        f"Please close all flash tools completely and then restart Innioasis Updater."
                    )
                    msg_box.setStandardButtons(QMessageBox.Ok)
                    msg_box.setDefaultButton(QMessageBox.Ok)
                    
                    # Show the dialog
                    msg_box.exec()
                    
                    # Optionally, you could close the application here
                    # self.close()
                
        except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
            # If tasklist times out or is not available, assume no conflict and continue
            silent_print("Flash tool check skipped - tasklist not available")
        except Exception as e:
            # If there's any error checking for the process, continue silently
            silent_print(f"Error checking for flash tools: {e}")

    def ensure_troubleshooting_shortcuts(self):
        """Download troubleshooting shortcuts if they're missing (Windows only)"""
        if platform.system() != "Windows":
            return
            
        # Check if shortcuts exist
        current_dir = Path.cwd()
        recovery_lnk = current_dir / "Recover Firmware Install.lnk"
        sp_flash_tool_lnk = current_dir / "Recover Firmware Install - SP Flash Tool.lnk"
        
        # If both shortcuts exist, no need to download
        if recovery_lnk.exists() and sp_flash_tool_lnk.exists():
            silent_print("Troubleshooting shortcuts already exist")
            return

    def check_and_cleanup_old_shortcuts(self):
        """Check for old shortcuts and offer to remove them (Windows only)"""
        if platform.system() != "Windows":
            return
            
        try:
            silent_print("Starting shortcut cleanup check...")
            
            # Comprehensive cleanup of all Y1 Helper and related shortcuts
            self.comprehensive_shortcut_cleanup()
            
            # Ensure Innioasis Updater shortcuts are properly set up
            self.ensure_innioasis_updater_shortcuts()
            self.ensure_innioasis_toolkit_shortcuts()
                
        except Exception as e:
            silent_print(f"Error during shortcut cleanup: {e}")
            import traceback
            silent_print(f"Full error traceback: {traceback.format_exc()}")

    def cleanup_rockbox_utility_zip(self):
        """Clean up RockboxUtility.zip - extract to assets on Windows, delete on other platforms"""
        try:
            current_dir = Path.cwd()
            rockbox_zip = current_dir / "RockboxUtility.zip"
            
            if not rockbox_zip.exists():
                return  # No zip file to process
            
            silent_print("Found RockboxUtility.zip, processing...")
            
            if platform.system() == "Windows":
                # On Windows: Extract to assets directory
                assets_dir = current_dir / "assets"
                assets_dir.mkdir(exist_ok=True)  # Create assets directory if it doesn't exist
                
                try:
                    with zipfile.ZipFile(rockbox_zip, 'r') as zip_ref:
                        zip_ref.extractall(assets_dir)
                        silent_print(f"Extracted RockboxUtility.zip to {assets_dir}")
                    
                    # Delete the zip file after successful extraction
                    rockbox_zip.unlink()
                    silent_print("Deleted RockboxUtility.zip after extraction")
                    
                except Exception as e:
                    silent_print(f"Error extracting RockboxUtility.zip: {e}")
                    # Still try to delete the zip file even if extraction failed
                    try:
                        rockbox_zip.unlink()
                        silent_print("Deleted RockboxUtility.zip despite extraction error")
                    except Exception as delete_error:
                        silent_print(f"Error deleting RockboxUtility.zip: {delete_error}")
            else:
                # On other platforms: Just delete the zip file
                try:
                    rockbox_zip.unlink()
                    silent_print("Deleted RockboxUtility.zip (not needed on this platform)")
                except Exception as e:
                    silent_print(f"Error deleting RockboxUtility.zip: {e}")
                    
        except Exception as e:
            silent_print(f"Error processing RockboxUtility.zip: {e}")

    def check_usbdk_cleanup(self):
        """Check if UsbDk driver should be cleaned up and offer removal - DISABLED"""
        # This function is no longer called as UsbDk cleanup doesn't actually remove anything
        return

    def show_usbdk_cleanup_dialog(self):
        """Show dialog offering to remove UsbDk driver"""
        try:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("USB Development Kit Cleanup")
            msg_box.setText("USB Development Kit Driver Detected")
            msg_box.setInformativeText(
                "The USB Development Kit (UsbDk) driver is no longer needed for Innioasis Updater.\n\n"
                "Would you like to remove it to clean up your system?\n\n"
                "This will:\n"
                "• Uninstall the UsbDk driver\n"
                "• Remove the UsbDk Runtime Library directory\n"
                "• Reboot your PC to complete the cleanup"
            )
            msg_box.setIcon(QMessageBox.Information)
            
            # Create buttons
            uninstall_btn = msg_box.addButton("Remove UsbDk Driver", QMessageBox.ActionRole)
            keep_btn = msg_box.addButton("Keep Driver", QMessageBox.RejectRole)
            
            # Set default button
            msg_box.setDefaultButton(uninstall_btn)
            
            # Show dialog
            reply = msg_box.exec()
            clicked_button = msg_box.clickedButton()
            
            if clicked_button == uninstall_btn:
                self.perform_usbdk_cleanup()
            else:
                silent_print("User chose to keep UsbDk driver")
                
        except Exception as e:
            silent_print(f"Error showing UsbDk cleanup dialog: {e}")

    def perform_usbdk_cleanup(self):
        """Perform the actual UsbDk driver cleanup"""
        try:
            silent_print("Starting UsbDk driver cleanup...")
            
            # Step 1: Run UsbDkController.exe -u to uninstall
            usbdk_controller = Path("C:/Program Files/UsbDk Runtime Library/UsbDkController.exe")
            if usbdk_controller.exists():
                silent_print("Running UsbDk uninstaller...")
                try:
                    result = subprocess.run(
                        [str(usbdk_controller), "-u"],
                        capture_output=True,
                        text=True,
                        timeout=60,
                        creationflags=subprocess.CREATE_NO_WINDOW
                    )
                    silent_print(f"UsbDk uninstaller result: {result.returncode}")
                    if result.stdout:
                        silent_print(f"UsbDk uninstaller output: {result.stdout}")
                    if result.stderr:
                        silent_print(f"UsbDk uninstaller error: {result.stderr}")
                except subprocess.TimeoutExpired:
                    silent_print("UsbDk uninstaller timed out")
                except Exception as e:
                    silent_print(f"Error running UsbDk uninstaller: {e}")
            else:
                silent_print("UsbDk controller not found, proceeding with directory cleanup")
            
            # Step 2: Delete the UsbDk Runtime Library directory
            usbdk_dir = Path("C:/Program Files/UsbDk Runtime Library")
            if usbdk_dir.exists():
                silent_print("Removing UsbDk Runtime Library directory...")
                try:
                    import shutil
                    shutil.rmtree(usbdk_dir, ignore_errors=True)
                    silent_print("UsbDk Runtime Library directory removed")
                except Exception as e:
                    silent_print(f"Error removing UsbDk directory: {e}")
            else:
                silent_print("UsbDk Runtime Library directory not found")
            
            # Step 3: Show reboot dialog
            self.show_reboot_dialog()
            
        except Exception as e:
            silent_print(f"Error during UsbDk cleanup: {e}")

    def show_reboot_dialog(self):
        """Show dialog asking user to reboot"""
        try:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Restart Required")
            msg_box.setText("UsbDk Driver Cleanup Complete")
            msg_box.setInformativeText(
                "The UsbDk driver has been removed from your system.\n\n"
                "Please restart your PC to complete the cleanup process.\n\n"
                "When you return to Innioasis Updater, you'll have a fully working setup! 🎉"
            )
            msg_box.setIcon(QMessageBox.Information)
            
            # Create buttons
            reboot_now_btn = msg_box.addButton("Restart Now", QMessageBox.ActionRole)
            reboot_later_btn = msg_box.addButton("Restart Later", QMessageBox.RejectRole)
            
            # Set default button
            msg_box.setDefaultButton(reboot_now_btn)
            
            # Show dialog
            reply = msg_box.exec()
            clicked_button = msg_box.clickedButton()
            
            if clicked_button == reboot_now_btn:
                self.initiate_system_reboot()
            else:
                silent_print("User chose to restart later")
                
        except Exception as e:
            silent_print(f"Error showing reboot dialog: {e}")

    def initiate_system_reboot(self):
        """Initiate a system reboot"""
        try:
            silent_print("Initiating system reboot...")
            
            # Use Windows shutdown command to reboot
            subprocess.run(
                ["shutdown", "/r", "/t", "10", "/c", "Innioasis Updater: Restarting to complete UsbDk cleanup"],
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            
            # Show countdown dialog
            self.show_reboot_countdown()
            
        except Exception as e:
            silent_print(f"Error initiating reboot: {e}")

    def show_reboot_countdown(self):
        """Show countdown dialog before reboot"""
        try:
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("System Restarting")
            msg_box.setText("Your PC will restart in 10 seconds...")
            msg_box.setInformativeText(
                "The system is restarting to complete the UsbDk driver cleanup.\n\n"
                "Innioasis Updater will close now.\n\n"
                "Thank you for using Innioasis Updater! 🚀"
            )
            msg_box.setIcon(QMessageBox.Information)
            
            # Add only OK button
            msg_box.addButton("OK", QMessageBox.AcceptRole)
            
            # Show dialog
            msg_box.exec()
            
            # Close the application
            QApplication.quit()
            
        except Exception as e:
            silent_print(f"Error showing reboot countdown: {e}")

    def comprehensive_shortcut_cleanup(self):
        """Silent comprehensive cleanup of all Y1 Helper and related shortcuts - no user interaction"""
        if platform.system() != "Windows":
            return
            
        try:
            cleaned_count = 0
            
            # Clean up desktop shortcuts using wildcards
            desktop_path = Path.home() / "Desktop"
            if desktop_path.exists():
                # Remove shortcuts matching patterns
                patterns = ["*Y1*", "*SP Flash*", "*Innioasis*"]
                for pattern in patterns:
                    for item in desktop_path.glob(pattern):
                        if item.is_file() and item.suffix.lower() == '.lnk':
                            try:
                                item.unlink()
                                cleaned_count += 1
                                silent_print(f"Removed desktop shortcut: {item.name}")
                            except Exception as e:
                                silent_print(f"Error removing {item.name}: {e}")
            
            # Clean up start menu shortcuts using wildcards
            start_menu_paths = self.get_all_start_menu_paths()
            for start_menu_path in start_menu_paths:
                if start_menu_path.exists():
                    # Remove shortcuts matching patterns
                    patterns = ["*Y1*", "*SP Flash*", "*Innioasis*"]
                    for pattern in patterns:
                        for item in start_menu_path.glob(pattern):
                            if item.is_file() and item.suffix.lower() == '.lnk':
                                try:
                                    item.unlink()
                                    cleaned_count += 1
                                    silent_print(f"Removed start menu shortcut: {item.name}")
                                except Exception as e:
                                    silent_print(f"Error removing {item.name}: {e}")
                    
                    # Remove Y1 Helper folder if it exists
                    y1_helper_folder = start_menu_path / "Y1 Helper"
                    if y1_helper_folder.exists() and y1_helper_folder.is_dir():
                        try:
                            shutil.rmtree(y1_helper_folder)
                            cleaned_count += 1
                            silent_print(f"Removed Y1 Helper folder: {y1_helper_folder}")
                        except Exception as e:
                            silent_print(f"Error removing Y1 Helper folder: {e}")
            
            silent_print(f"Silent comprehensive shortcut cleanup completed: {cleaned_count} items removed")
            
            # Create current shortcuts if enabled in settings
            if getattr(self, 'desktop_shortcuts_enabled', True):
                self.ensure_desktop_shortcuts()
            if getattr(self, 'startmenu_shortcuts_enabled', True):
                self.ensure_startmenu_shortcuts()
                
        except Exception as e:
            silent_print(f"Error during comprehensive shortcut cleanup: {e}")

    def get_all_start_menu_paths(self):
        """Get comprehensive list of all possible start menu paths"""
        paths = []
        
        # User-specific paths
        user_paths = [
            Path.home() / "AppData" / "Roaming" / "Microsoft" / "Windows" / "Start Menu" / "Programs",
            Path.home() / "AppData" / "Local" / "Microsoft" / "Windows" / "Start Menu" / "Programs"
        ]
        
        # System-wide paths
        system_paths = [
            Path("C:/ProgramData/Microsoft/Windows/Start Menu/Programs"),
            Path("C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp"),
            Path("C:/Users/Public/Start Menu/Programs"),
            Path("C:/Users/Public/Desktop")
        ]
        
        # Environment variable paths
        env_paths = []
        if "PROGRAMDATA" in os.environ:
            env_paths.append(Path(os.environ["PROGRAMDATA"]) / "Microsoft" / "Windows" / "Start Menu" / "Programs")
            env_paths.append(Path(os.environ["PROGRAMDATA"]) / "Microsoft" / "Windows/Start Menu/Programs" / "StartUp")
        
        if "PUBLIC" in os.environ:
            env_paths.append(Path(os.environ["PUBLIC"]) / "Start Menu" / "Programs")
            env_paths.append(Path(os.environ["PUBLIC"]) / "Desktop")
        
        # Combine all paths and filter existing ones
        all_paths = user_paths + system_paths + env_paths
        
        silent_print(f"Checking {len(all_paths)} potential start menu paths...")
        
        for path in all_paths:
            silent_print(f"Checking path: {path} (exists: {path.exists()})")
            if path.exists():
                paths.append(path)
                silent_print(f"Found start menu path: {path}")
                
                # Specifically check for the Y1 Helper.lnk file in this path
                y1_helper_lnk = path / "Y1 Helper.lnk"
                if y1_helper_lnk.exists():
                    silent_print(f"*** FOUND Y1 Helper.lnk at: {y1_helper_lnk} ***")
        
        silent_print(f"Total valid start menu paths found: {len(paths)}")
        return paths

    def ensure_innioasis_updater_shortcuts(self):
        """Ensure Innioasis Updater shortcuts are properly set up using appropriate source"""
        try:
            # Use the new method to get appropriate shortcut source
            source_shortcut = self.get_appropriate_shortcut_source()
            
            if not source_shortcut:
                silent_print("Appropriate Innioasis Updater shortcut source not found")
                return
            
            # Check desktop
            desktop_path = Path.home() / "Desktop"
            desktop_shortcut = desktop_path / "Innioasis Updater.lnk"
            
            # Force replacement of existing shortcut
            if desktop_shortcut.exists():
                try:
                    desktop_shortcut.unlink()  # Remove existing shortcut
                    silent_print(f"Removed existing desktop shortcut: Innioasis Updater.lnk")
                except Exception as e:
                    silent_print(f"Warning: Could not remove existing desktop shortcut: {e}")
            
            try:
                shutil.copy2(source_shortcut, desktop_shortcut)
                auto_updates_enabled = getattr(self, 'auto_utility_updates_enabled', True)
                shortcut_type = "regular" if auto_updates_enabled else "skip-update"
                silent_print(f"Added Innioasis Updater shortcut to desktop ({shortcut_type})")
            except Exception as e:
                silent_print(f"Error adding desktop shortcut: {e}")
            
            # Get comprehensive list of start menu paths
            start_menu_paths = self.get_all_start_menu_paths()
            
            for start_menu_path in start_menu_paths:
                if start_menu_path.exists():
                    start_menu_shortcut = start_menu_path / "Innioasis Updater.lnk"
                    # Force replacement of existing shortcut
                    if start_menu_shortcut.exists():
                        try:
                            start_menu_shortcut.unlink()  # Remove existing shortcut
                            silent_print(f"Removed existing start menu shortcut: Innioasis Updater.lnk")
                        except Exception as e:
                            silent_print(f"Warning: Could not remove existing start menu shortcut: {e}")
                    
                    try:
                        shutil.copy2(source_shortcut, start_menu_shortcut)
                        auto_updates_enabled = getattr(self, 'auto_utility_updates_enabled', True)
                        shortcut_type = "regular" if auto_updates_enabled else "skip-update"
                        silent_print(f"Added Innioasis Updater shortcut to start menu: {start_menu_path} ({shortcut_type})")
                    except Exception as e:
                        silent_print(f"Error adding start menu shortcut: {e}")
                            
        except Exception as e:
            silent_print(f"Error ensuring Innioasis Updater shortcuts: {e}")

    def ensure_innioasis_toolkit_shortcuts(self):
        """Ensure Innioasis Toolkit shortcuts are properly set up"""
        try:
            current_dir = Path.cwd()
            innioasis_toolkit_shortcut = current_dir / "Innioasis Toolkit.lnk"
            
            if not innioasis_toolkit_shortcut.exists():
                silent_print("Innioasis Toolkit.lnk not found in current directory")
                return
            
            # Check desktop
            desktop_path = Path.home() / "Desktop"
            desktop_shortcut = desktop_path / "Innioasis Toolkit.lnk"
            
            if not desktop_shortcut.exists():
                try:
                    shutil.copy2(innioasis_toolkit_shortcut, desktop_shortcut)
                    silent_print(f"Added Innioasis Toolkit shortcut to desktop")
                except Exception as e:
                    silent_print(f"Error adding desktop shortcut: {e}")
            
            # Get comprehensive list of start menu paths
            start_menu_paths = self.get_all_start_menu_paths()
            
            for start_menu_path in start_menu_paths:
                if start_menu_path.exists():
                    start_menu_shortcut = start_menu_path / "Innioasis Toolkit.lnk"
                    if not start_menu_shortcut.exists():
                        try:
                            shutil.copy2(innioasis_toolkit_shortcut, start_menu_shortcut)
                            silent_print(f"Added Innioasis Toolkit shortcut to start menu: {start_menu_path}")
                        except Exception as e:
                            silent_print(f"Error adding start menu shortcut: {e}")
                            
        except Exception as e:
            silent_print(f"Error ensuring Innioasis Toolkit shortcuts: {e}")

    def show_shortcut_cleanup_dialog(self, old_shortcuts):
        """Silently remove old shortcuts without user interaction"""
        try:
            if not old_shortcuts:
                return
                
            silent_print(f"Found {len(old_shortcuts)} old shortcuts, removing silently...")
            self.remove_old_shortcuts(old_shortcuts)
                
        except Exception as e:
            silent_print(f"Error during silent shortcut cleanup: {e}")

    def remove_old_shortcuts(self, old_shortcuts):
        """Remove old shortcuts and folders"""
        try:
            removed_count = 0
            failed_items = []
            
            for location, item_path in old_shortcuts:
                try:
                    item_path = Path(item_path)
                    if item_path.exists():
                        if item_path.is_file():
                            item_path.unlink()
                        elif item_path.is_dir():
                            shutil.rmtree(item_path)
                        removed_count += 1
                        silent_print(f"Removed: {item_path}")
                except PermissionError:
                    # Some items may need admin privileges
                    failed_items.append(f"{item_path} (needs admin)")
                except Exception as e:
                    failed_items.append(f"{item_path} ({e})")
            
            # Show results
            if failed_items:
                silent_print(f"Successfully removed {removed_count} items.")
                silent_print(f"Some items could not be removed (may need admin privileges): {', '.join(failed_items)}")
            else:
                silent_print(f"Successfully removed {removed_count} old shortcuts and folders.")
                
        except Exception as e:
            silent_print(f"Error during cleanup: {e}")

    def check_and_replace_y1_helper_shortcuts(self):
        """Check for Y1 Helper and Y1 Remote Control shortcuts and clean up to desired state"""
        if platform.system() != "Windows":
            return
            
        try:
            shortcuts_to_cleanup = []
            y1_helper_desktop_shortcut = None
            
            # Check desktop for shortcuts
            desktop_path = Path.home() / "Desktop"
            if desktop_path.exists():
                # Check for Y1 Helper.lnk specifically (will be replaced with Innioasis Updater)
                y1_helper_exact = desktop_path / "Y1 Helper.lnk"
                if y1_helper_exact.exists():
                    y1_helper_desktop_shortcut = str(y1_helper_exact)
                
                # Check for other Y1 Helper variants
                for item in desktop_path.glob("*Y1 Helper*.lnk"):
                    if item.name != "Y1 Helper.lnk":  # Skip the exact match we already found
                        shortcuts_to_cleanup.append(("Desktop", str(item), "Y1 Helper variant"))
                
                # Check for Y1 Remote Control variants
                for item in desktop_path.glob("*Y1 Remote Control*.lnk"):
                    shortcuts_to_cleanup.append(("Desktop", str(item), "Y1 Remote Control variant"))
            
            # Check Start Menu for shortcuts
            start_menu_paths = [
                Path.home() / "AppData" / "Roaming" / "Microsoft" / "Windows" / "Start Menu" / "Programs",
                Path.home() / "AppData" / "Local" / "Microsoft" / "Windows" / "Start Menu" / "Programs"
            ]
            
            for start_menu_path in start_menu_paths:
                if start_menu_path.exists():
                    # Check for Y1 Helper folder (will be deleted entirely)
                    y1_helper_folder = start_menu_path / "Y1 Helper"
                    if y1_helper_folder.exists():
                        shortcuts_to_cleanup.append(("Start Menu Folder", str(y1_helper_folder), "Y1 Helper folder"))
                    
                    # Check for individual Y1 Helper shortcuts
                    for item in start_menu_path.glob("*Y1 Helper*.lnk"):
                        shortcuts_to_cleanup.append(("Start Menu", str(item), "Y1 Helper shortcut"))
                    
                    # Check for Y1 Remote Control variants
                    for item in start_menu_path.glob("*Y1 Remote Control*.lnk"):
                        shortcuts_to_cleanup.append(("Start Menu", str(item), "Y1 Remote Control variant"))
            
            # Always ensure proper desktop shortcut exists
            self.ensure_proper_desktop_shortcut()
            
            # If exact Y1 Helper.lnk found on desktop, offer Innioasis Updater replacement
            if y1_helper_desktop_shortcut:
                self.show_innioasis_updater_replacement_dialog(y1_helper_desktop_shortcut)
            
            # If other shortcuts found, offer cleanup
            if shortcuts_to_cleanup:
                self.show_comprehensive_cleanup_dialog(shortcuts_to_cleanup)
                
        except Exception as e:
            silent_print(f"Error checking for shortcuts: {e}")

    def show_innioasis_updater_replacement_dialog(self, y1_helper_desktop_shortcut):
        """Show dialog offering to replace Y1 Helper.lnk with Innioasis Updater.lnk"""
        try:
            # Check if Innioasis Updater.lnk exists in the same directory
            current_dir = Path.cwd()
            innioasis_updater_shortcut = current_dir / "Innioasis Updater.lnk"
            
            if not innioasis_updater_shortcut.exists():
                silent_print("Innioasis Updater.lnk not found in current directory")
                return
            
            message = "Found Y1 Helper.lnk on your desktop that can be replaced with Innioasis Updater:\n\n"
            message += "Desktop:\n"
            silent_print(f"Found Y1 Helper shortcut: {Path(y1_helper_desktop_shortcut).name}")
            silent_print("Replacing with Innioasis Updater shortcut...")
            self.replace_y1_helper_with_innioasis_updater(y1_helper_desktop_shortcut, str(innioasis_updater_shortcut))
                
        except Exception as e:
            silent_print(f"Error showing Innioasis Updater replacement dialog: {e}")

    def replace_y1_helper_with_innioasis_updater(self, old_shortcut_path, new_shortcut_path):
        """Replace Y1 Helper.lnk with Innioasis Updater.lnk on desktop"""
        try:
            old_shortcut = Path(old_shortcut_path)
            new_shortcut = Path(new_shortcut_path)
            
            if not old_shortcut.exists():
                silent_print("Y1 Helper.lnk no longer exists on desktop")
                return
            
            if not new_shortcut.exists():
                silent_print("Innioasis Updater.lnk not found in current directory")
                return
            
            # Copy Innioasis Updater.lnk to desktop
            desktop_path = Path.home() / "Desktop"
            desktop_innioasis_shortcut = desktop_path / "Innioasis Updater.lnk"
            
            shutil.copy2(new_shortcut, desktop_innioasis_shortcut)
            
            # Remove the old Y1 Helper.lnk
            old_shortcut.unlink()
            
            silent_print("Successfully replaced Y1 Helper.lnk with Innioasis Updater.lnk on your desktop.")
            silent_print(f"Replaced: {old_shortcut} -> {desktop_innioasis_shortcut}")
            
        except PermissionError:
            silent_print("Could not replace the shortcut. You may need to run as administrator.")
        except Exception as e:
            silent_print(f"Error during replacement: {e}")

    def ensure_proper_desktop_shortcut(self):
        """Ensure Innioasis Updater.lnk exists on desktop"""
        try:
            desktop_path = Path.home() / "Desktop"
            if not desktop_path.exists():
                return
            
            # Check if Innioasis Updater.lnk already exists on desktop
            desktop_innioasis_shortcut = desktop_path / "Innioasis Updater.lnk"
            if desktop_innioasis_shortcut.exists():
                silent_print("Innioasis Updater.lnk already exists on desktop")
                return
            
            # Check if the shortcut exists in current directory
            current_dir = Path.cwd()
            source_shortcut = current_dir / "Innioasis Updater.lnk"
            if not source_shortcut.exists():
                silent_print("Innioasis Updater.lnk not found in current directory")
                return
            
            # Copy the shortcut to desktop
            shutil.copy2(source_shortcut, desktop_innioasis_shortcut)
            silent_print(f"Added Innioasis Updater.lnk to desktop")
            
        except Exception as e:
            silent_print(f"Error ensuring proper desktop shortcut: {e}")

    def show_comprehensive_cleanup_dialog(self, old_shortcuts):
        """Show dialog offering to clean up all old shortcuts"""
        try:
            # Group shortcuts by location for better display
            desktop_items = [item for location, item in old_shortcuts if location == "Desktop"]
            desktop_subfolder_items = [item for location, item in old_shortcuts if location == "Desktop Subfolder"]
            start_menu_items = [item for location, item in old_shortcuts if location == "Start Menu"]
            start_menu_subfolder_items = [item for location, item in old_shortcuts if location == "Start Menu Subfolder"]
            start_menu_folders = [item for location, item in old_shortcuts if location == "Start Menu Folder"]
            
            message = "Found old shortcuts and folders that should be cleaned up:\n\n"
            
            if desktop_items:
                message += "Desktop:\n"
                for item in desktop_items:
                    message += f"• {Path(item).name}\n"
                message += "\n"
            
            if desktop_subfolder_items:
                message += "Desktop Subfolders:\n"
                for item in desktop_subfolder_items:
                    message += f"• {Path(item).name}\n"
                message += "\n"
            
            if start_menu_items:
                message += "Start Menu:\n"
                for item in start_menu_items:
                    message += f"• {Path(item).name}\n"
                message += "\n"
            
            if start_menu_subfolder_items:
                message += "Start Menu Subfolders:\n"
                for item in start_menu_subfolder_items:
                    message += f"• {Path(item).name}\n"
                message += "\n"
            
            if start_menu_folders:
                message += "Start Menu Folders (will be deleted):\n"
                for item in start_menu_folders:
                    message += f"• {Path(item).name}\n"
                message += "\n"
            
            message += "This will clean up all old Y1 Helper and related shortcuts and ensure you have:\n"
            message += "• Innioasis Updater.lnk on desktop\n"
            message += "• Innioasis Toolkit.lnk on desktop\n"
            silent_print(f"Found {len(old_shortcuts)} old shortcuts and folders, proceeding with cleanup...")
            self.perform_comprehensive_cleanup(old_shortcuts)
                
        except Exception as e:
            silent_print(f"Error showing comprehensive cleanup dialog: {e}")

    def perform_comprehensive_cleanup(self, old_shortcuts):
        """Perform comprehensive cleanup of old shortcuts and ensure proper ones exist"""
        try:
            removed_count = 0
            failed_items = []
            
            # First, remove all old shortcuts and folders
            for location, item_path in old_shortcuts:
                try:
                    item_path = Path(item_path)
                    if item_path.exists():
                        if location == "Start Menu Folder":
                            # Delete the entire folder
                            shutil.rmtree(item_path)
                            removed_count += 1
                            silent_print(f"Deleted folder: {item_path}")
                        else:
                            # Remove the shortcut
                            item_path.unlink()
                            removed_count += 1
                            silent_print(f"Removed shortcut: {item_path}")
                except PermissionError:
                    # Some items may need admin privileges
                    failed_items.append(f"{item_path} (needs admin)")
                except Exception as e:
                    failed_items.append(f"{item_path} ({e})")
            
            # Now ensure proper shortcuts exist
            self.ensure_innioasis_updater_shortcuts()
            self.ensure_innioasis_toolkit_shortcuts()
            
            # Show results silently
            if failed_items:
                silent_print(f"Successfully cleaned up {removed_count} items.")
                silent_print(f"Some items could not be removed (may need admin privileges): {', '.join(failed_items)}")
            else:
                silent_print(f"Successfully cleaned up {removed_count} old shortcuts and folders.")
                silent_print("Your system now has:")
                silent_print("• Innioasis Updater.lnk on desktop")
                silent_print("• Innioasis Toolkit.lnk on desktop")
                silent_print("• Innioasis Updater.lnk in Start Menu")
                silent_print("• Innioasis Toolkit.lnk in Start Menu")
                
        except Exception as e:
            silent_print(f"Error during cleanup: {e}")

    def ensure_proper_start_menu_shortcuts(self):
        """Ensure proper shortcuts exist in Start Menu"""
        try:
            current_dir = Path.cwd()
            start_menu_paths = [
                Path.home() / "AppData" / "Roaming" / "Microsoft" / "Windows" / "Start Menu" / "Programs",
                Path.home() / "AppData" / "Local" / "Microsoft" / "Windows" / "Start Menu" / "Programs"
            ]
            
            # Check if proper shortcuts already exist
            innioasis_updater_exists = False
            innioasis_y1_remote_exists = False
            innioasis_toolkit_exists = False
            
            for start_menu_path in start_menu_paths:
                if start_menu_path.exists():
                    if (start_menu_path / "Innioasis Updater.lnk").exists():
                        innioasis_updater_exists = True
                    if (start_menu_path / "Innioasis Y1 Remote Control.lnk").exists():
                        innioasis_y1_remote_exists = True
                    if (start_menu_path / "Innioasis Toolkit.lnk").exists():
                        innioasis_toolkit_exists = True
            
            # Copy missing shortcuts from current directory
            if not innioasis_updater_exists:
                source_updater = current_dir / "Innioasis Updater.lnk"
                if source_updater.exists():
                    # Copy to first available start menu path
                    for start_menu_path in start_menu_paths:
                        if start_menu_path.exists():
                            dest_updater = start_menu_path / "Innioasis Updater.lnk"
                            shutil.copy2(source_updater, dest_updater)
                            silent_print(f"Added Innioasis Updater.lnk to {start_menu_path}")
                            break
            
            if not innioasis_y1_remote_exists:
                source_remote = current_dir / "Innioasis Y1 Remote Control.lnk"
                if source_remote.exists():
                    # Copy to first available start menu path
                    for start_menu_path in start_menu_paths:
                            dest_remote = start_menu_path / "Innioasis Y1 Remote Control.lnk"
                            shutil.copy2(source_remote, dest_remote)
                            silent_print(f"Added Innioasis Y1 Remote Control.lnk to {start_menu_path}")
                            break
            
            if not innioasis_toolkit_exists:
                source_toolkit = current_dir / "Innioasis Toolkit.lnk"
                if source_toolkit.exists():
                    # Copy to first available start menu path
                    for start_menu_path in start_menu_paths:
                        if start_menu_path.exists():
                            dest_toolkit = start_menu_path / "Innioasis Toolkit.lnk"
                            shutil.copy2(source_toolkit, dest_toolkit)
                            silent_print(f"Added Innioasis Toolkit.lnk to {start_menu_path}")
                            break
                            
        except Exception as e:
            silent_print(f"Error ensuring proper start menu shortcuts: {e}")

    def show_y1_helper_replacement_dialog(self, y1_helper_shortcuts):
        """Show dialog offering to replace Y1 Helper shortcuts with Y1 Remote Control"""
        try:
            # Group shortcuts by location for better display
            desktop_items = [item for location, item in y1_helper_shortcuts if location == "Desktop"]
            start_menu_items = [item for location, item in y1_helper_shortcuts if location == "Start Menu"]
            start_menu_folders = [item for location, item in y1_helper_shortcuts if location == "Start Menu Folder"]
            
            message = "Found Y1 Helper shortcuts that can be replaced with Y1 Remote Control:\n\n"
            
            if desktop_items:
                message += "Desktop:\n"
                for item in desktop_items:
                    message += f"• {Path(item).name}\n"
                message += "\n"
            
            if start_menu_items:
                message += "Start Menu:\n"
                for item in start_menu_items:
                    message += f"• {Path(item).name}\n"
                message += f"• {item}\n"
                message += "\n"
            
            if start_menu_folders:
                message += "Start Menu Folders (will be deleted):\n"
                for item in start_menu_folders:
                    message += f"• {item}\n"
                message += "\n"
            
            silent_print(f"Found {len(y1_helper_shortcuts)} Y1 Helper shortcuts, replacing with Y1 Remote Control...")
            self.replace_y1_helper_shortcuts(y1_helper_shortcuts)
                
        except Exception as e:
            silent_print(f"Error showing Y1 Helper replacement dialog: {e}")

    def replace_y1_helper_shortcuts(self, y1_helper_shortcuts):
        """Replace Y1 Helper shortcuts with Y1 Remote Control"""
        try:
            replaced_count = 0
            failed_items = []
            
            for location, item_path in y1_helper_shortcuts:
                try:
                    item_path = Path(item_path)
                    if item_path.exists():
                        if location == "Start Menu Folder":
                            # Delete the entire folder
                            shutil.rmtree(item_path)
                            replaced_count += 1
                            silent_print(f"Deleted folder: {item_path}")
                        else:
                            # Replace shortcut with Y1 Remote Control
                            new_shortcut_name = item_path.name.replace("Y1 Helper", "Y1 Remote Control")
                            new_shortcut_path = item_path.parent / new_shortcut_name
                            
                            # Copy the shortcut and modify it to point to Y1 Remote Control
                            shutil.copy2(item_path, new_shortcut_path)
                            
                            # Remove the old Y1 Helper shortcut
                            item_path.unlink()
                            
                            replaced_count += 1
                            silent_print(f"Replaced: {item_path} -> {new_shortcut_path}")
                except PermissionError:
                    # Some items may need admin privileges
                    failed_items.append(f"{item_path} (needs admin)")
                except Exception as e:
                    failed_items.append(f"{item_path} ({e})")
            
            # Show results silently
            if failed_items:
                silent_print(f"Successfully replaced {replaced_count} shortcuts.")
                silent_print(f"Some shortcuts could not be replaced (may need admin privileges): {', '.join(failed_items)}")
            else:
                silent_print(f"Successfully replaced {replaced_count} Y1 Helper shortcuts with Y1 Remote Control.")
                
        except Exception as e:
            silent_print(f"Error during replacement: {e}")
            
        # Download troubleshooting shortcuts
        self.download_troubleshooting_shortcuts()

    def download_troubleshooting_shortcuts(self):
        """Download and extract troubleshooting shortcuts zip file"""
        try:
            self.status_label.setText("Downloading troubleshooting shortcuts...")
            silent_print("Downloading troubleshooting shortcuts...")
            
            # Download URL for troubleshooting shortcuts
            url = "https://github.com/team-slide/Innioasis-Updater/releases/download/1.0.0/Troubleshooters.-.Windows.zip"
            
            # Download the zip file
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()
            
            # Save to temporary zip file
            temp_zip = Path("troubleshooters_temp.zip")
            with open(temp_zip, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            
            silent_print("Downloaded troubleshooting shortcuts zip file")
            
            # Extract the zip file to current directory
            with zipfile.ZipFile(temp_zip, 'r') as zip_ref:
                zip_ref.extractall(".")
            
            silent_print("Extracted troubleshooting shortcuts")
            
            # Check if Troubleshooters - Windows.zip was extracted and extract its contents
            troubleshooters_zip = Path("Troubleshooters - Windows.zip")
            if troubleshooters_zip.exists():
                silent_print("Found Troubleshooters - Windows.zip, extracting nested contents...")
                with zipfile.ZipFile(troubleshooters_zip, 'r') as nested_zip:
                    nested_zip.extractall(".")
                silent_print("Extracted nested troubleshooting shortcuts")
                
                # Remove the nested zip file after extraction
                troubleshooters_zip.unlink()
                silent_print("Removed nested zip file")
            
            # Delete the temporary zip file
            temp_zip.unlink()
            silent_print("Cleaned up temporary zip file")
            
            # Verify shortcuts were extracted
            current_dir = Path.cwd()
            recovery_lnk = current_dir / "Recover Firmware Install.lnk"
            sp_flash_tool_lnk = current_dir / "Recover Firmware Install - SP Flash Tool.lnk"
            
            if recovery_lnk.exists() and sp_flash_tool_lnk.exists():
                self.status_label.setText("Troubleshooting shortcuts downloaded successfully")
                silent_print("Troubleshooting shortcuts downloaded and extracted successfully")
                # Auto-clear status after 3 seconds
                QTimer.singleShot(3000, lambda: self.status_label.setText("Ready"))
            else:
                self.status_label.setText("Warning: Some troubleshooting shortcuts may be missing")
                silent_print("Warning: Some troubleshooting shortcuts may be missing after extraction")
                # Auto-clear warning after 3 seconds
                QTimer.singleShot(3000, lambda: self.status_label.setText("Ready"))
                
        except Exception as e:
            self.status_label.setText("Failed to download troubleshooting shortcuts")
            silent_print(f"Error downloading troubleshooting shortcuts: {e}")
            # Auto-clear error status after 3 seconds
            QTimer.singleShot(3000, lambda: self.status_label.setText("Ready"))
            # Don't show error dialog - this is not critical for basic functionality

    def ensure_troubleshooting_shortcuts_available(self):
        """Ensure troubleshooting shortcuts are available, extract from zip if needed"""
        try:
            current_dir = Path.cwd()
            recovery_lnk = current_dir / "Recover Firmware Install.lnk"
            sp_flash_tool_lnk = current_dir / "Recover Firmware Install - SP Flash Tool.lnk"
            
            # Check if shortcuts exist
            if recovery_lnk.exists() and sp_flash_tool_lnk.exists():
                silent_print("Troubleshooting shortcuts already available")
                return
            
            # Check if Troubleshooters - Windows.zip exists and extract it
            troubleshooters_zip = current_dir / "Troubleshooters - Windows.zip"
            if troubleshooters_zip.exists():
                silent_print("Found Troubleshooters - Windows.zip, extracting shortcuts...")
                try:
                    with zipfile.ZipFile(troubleshooters_zip, 'r') as zip_ref:
                        zip_ref.extractall(current_dir)
                    
                    # Remove the zip file after extraction
                    troubleshooters_zip.unlink()
                    silent_print("Troubleshooting shortcuts extracted successfully")
                    
                    # Verify extraction
                    if recovery_lnk.exists() and sp_flash_tool_lnk.exists():
                        silent_print("Troubleshooting shortcuts verified")
                    else:
                        silent_print("Warning: Troubleshooting shortcuts still missing after extraction")
                        
                except Exception as e:
                    silent_print(f"Error extracting troubleshooting shortcuts: {e}")
            else:
                silent_print("No troubleshooting shortcuts zip found")
                
        except Exception as e:
            silent_print(f"Error ensuring troubleshooting shortcuts: {e}")

    def check_failed_installation_on_startup(self):
        """Check for failed installation on startup and show troubleshooting options"""
        if not check_for_failed_installation():
            return
            
        # Check driver availability for Windows users
        if platform.system() == "Windows":
            driver_info = self.check_drivers_and_architecture()
            
            if driver_info['is_arm64']:
                # ARM64 Windows: No installation methods available
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("ARM64 Windows - No Installation Methods")
                msg_box.setText("Firmware installation is not supported on ARM64 Windows.")
                msg_box.setInformativeText("You can download firmware files, but to install them please use WSLg, Linux, or another computer.")
                msg_box.setIcon(QMessageBox.Information)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec()
                remove_installation_marker()
                return
                
            elif not driver_info['can_install_firmware']:
                # No drivers: No installation methods available
                msg_box = QMessageBox(self)
                msg_box.setWindowTitle("Drivers Required")
                msg_box.setText("No installation methods available. Please install drivers to enable firmware installation.")
                msg_box.setInformativeText("Click OK to open the driver installation guide.")
                msg_box.setIcon(QMessageBox.Warning)
                msg_box.setStandardButtons(QMessageBox.Ok)
                msg_box.exec()
                remove_installation_marker()
                self.open_driver_setup_link()
                return
            
        # Show failed installation dialog with troubleshooting options
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Firmware Installation Incomplete")
        msg_box.setText("A previous firmware installation appears to have been interrupted or failed.")
        msg_box.setInformativeText("Would you like to try troubleshooting the installation?")
        msg_box.setIcon(QMessageBox.Warning)
        
        # Create simplified buttons for troubleshooting options
        try_again_btn = msg_box.addButton("Try Again", QMessageBox.ActionRole)
        settings_btn = msg_box.addButton("Settings", QMessageBox.ActionRole)
        quit_app_btn = msg_box.addButton("Quit App", QMessageBox.RejectRole)
        
        # Set default button
        msg_box.setDefaultButton(try_again_btn)
        
        reply = msg_box.exec()
        clicked_button = msg_box.clickedButton()
        
        if clicked_button == try_again_btn:
            # Try Again - use Method 1 (default method for the platform)
            remove_installation_marker()
            if platform.system() == "Windows":
                # Windows: Use guided SP Flash Tool process (Method 1)
                self.try_method_3()
            else:
                # Non-Windows: Use guided MTKclient process (Method 1)
                self.stop_mtk_processes()
                self.cleanup_libusb_state()
                QTimer.singleShot(1000, self.run_mtk_command)
        elif clicked_button == settings_btn:
            # Settings - clear marker and open settings dialog
            remove_installation_marker()
            self.show_settings_dialog()
        else:
            # Quit App - exit the application
            QApplication.quit()

    def ensure_recovery_shortcut(self):
        """Ensure recovery shortcut exists, download if missing"""
        current_dir = Path.cwd()
        recovery_lnk = current_dir / "Recover Firmware Install.lnk"
        
        if recovery_lnk.exists():
            return True
            
        # Shortcut missing, try to download
        self.status_label.setText("Recovery shortcut missing, downloading...")
        self.download_troubleshooting_shortcuts()
        # Auto-clear status after 3 seconds
        QTimer.singleShot(3000, lambda: self.status_label.setText("Ready"))
        
        # Check again after download
        if recovery_lnk.exists():
            return True
            
        # Still missing, show error
        QMessageBox.warning(
            self,
            "Shortcut Missing",
            "The recovery firmware installer shortcut could not be downloaded.\n\n"
            "Please check your internet connection and try again."
        )
        return False

    def ensure_sp_flash_tool_shortcut(self):
        """Ensure SP Flash Tool shortcut exists, download if missing"""
        current_dir = Path.cwd()
        sp_flash_tool_lnk = current_dir / "Recover Firmware Install - SP Flash Tool.lnk"
        
        if sp_flash_tool_lnk.exists():
            return True
            
        # Shortcut missing, try to download
        self.status_label.setText("SP Flash Tool shortcut missing, downloading...")
        self.download_troubleshooting_shortcuts()
        # Auto-clear status after 3 seconds
        QTimer.singleShot(3000, lambda: self.status_label.setText("Ready"))
        
        # Check again after download
        if sp_flash_tool_lnk.exists():
            return True
            
        # Still missing, show error
        QMessageBox.warning(
            self,
            "Shortcut Missing",
            "The SP Flash Tool shortcut could not be downloaded.\n\n"
            "Please check your internet connection and try again."
        )
        return False

    def keyPressEvent(self, event):
        """Handle key press events"""
        # Control+D (Windows/Linux) or Cmd+D (macOS) to toggle debug mode
        if event.key() == Qt.Key_D and (event.modifiers() == Qt.ControlModifier or event.modifiers() == Qt.MetaModifier):
            self.debug_mode = not self.debug_mode
            if self.debug_mode:
                self.status_label.setText("Debug mode enabled - guided installations will show full output")
            else:
                self.status_label.setText("Debug mode disabled - guided installations will show minimal output")
        else:
            super().keyPressEvent(event)




    def show_custom_message_box(self, icon_type, title, message, buttons=QMessageBox.Ok, default_button=QMessageBox.Ok):
        """Show a message box with standard system icons"""
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(buttons)
        msg_box.setDefaultButton(default_button)

        # Set appropriate icon type
        if icon_type == "information":
            msg_box.setIcon(QMessageBox.Information)
        elif icon_type == "warning":
            msg_box.setIcon(QMessageBox.Warning)
        elif icon_type == "critical":
            msg_box.setIcon(QMessageBox.Critical)
        elif icon_type == "question":
            msg_box.setIcon(QMessageBox.Question)
        else:
            msg_box.setIcon(QMessageBox.NoIcon)

        return msg_box.exec()

    def init_ui(self):
        """Initialize the user interface"""
        # Add seasonal emoji to window title
        seasonal_emoji = get_seasonal_emoji()
        title_emoji = f" {seasonal_emoji}" if seasonal_emoji else ""
        self.setWindowTitle(f"Innioasis Updater v1.6.8{title_emoji}")
        self.setGeometry(100, 100, 1220, 574)
        
        # Set fixed window size to maintain layout
        self.setFixedSize(1220, 600)
        
        # Force normal window state (not maximized)
        self.setWindowState(Qt.WindowNoState)



        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create main layout
        main_layout = QVBoxLayout(central_widget)

        # Create splitter for resizable sections
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)

        # Left panel - Package selection
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)

        # Device filters
        filter_group = QGroupBox()
        filter_layout = QVBoxLayout(filter_group)

        # Device type filter
        device_type_layout = QHBoxLayout()
        device_type_layout.addWidget(QLabel("Device Type:"))

        self.device_type_combo = QComboBox()
        self.device_type_combo.currentTextChanged.connect(self.filter_firmware_options)
        device_type_layout.addWidget(self.device_type_combo)

        # Add help button with tooltip (to the right of dropdown)
        help_btn = QPushButton("?")
        help_btn.setStyleSheet("""
            QPushButton {
                color: #0066CC;
                font-weight: bold;
                font-size: 12px;
                margin-left: 5px;
                border: none;
                background-color: transparent;
                min-width: 24px;
                max-width: 24px;
                min-height: 24px;
                max-height: 24px;
                padding: 0px;
            }
            QPushButton:hover {
                background-color: rgba(0, 102, 204, 0.1);
                color: #0066CC;
            }
        """)
        help_btn.setCursor(Qt.PointingHandCursor)
        help_btn.setToolTip("Try Type A System Software first. If your scroll wheel doesn't respond after installation, install one of the Type B options.")
        help_btn.clicked.connect(self.show_device_type_help)
        device_type_layout.addWidget(help_btn)
        
        # Add Settings button (combines Tools and Settings functionality)
        seasonal_emoji = get_seasonal_emoji_random()
        settings_text = f"Settings{seasonal_emoji}" if seasonal_emoji else "Settings"
        self.settings_btn = QPushButton(settings_text)
        self.settings_btn.setFixedSize(80, 24)  # Fixed width and height for consistent alignment
        self.settings_btn.setStyleSheet("""
            QPushButton {
                background-color: palette(base);
                color: palette(text);
                border: 1px solid palette(mid);
                padding: 4px 8px;
                border-radius: 3px;
                font-weight: bold;
                font-size: 11px;
                min-height: 24px;
            }
            QPushButton:hover {
                background-color: palette(highlight);
                color: palette(highlighted-text);
            }
            QPushButton:pressed {
                background-color: palette(dark);
                color: palette(light);
            }
        """)
        self.settings_btn.setCursor(Qt.PointingHandCursor)
        self.settings_btn.setToolTip("Settings and Tools - Installation method, shortcuts, and Y1 Remote Control")
        self.settings_btn.clicked.connect(self.show_settings_dialog)
        device_type_layout.addWidget(self.settings_btn)
        
        # Add small spacing between Settings and Toolkit buttons
        device_type_layout.addSpacing(4)
        
        # Add Toolkit button for all platforms
        seasonal_emoji = get_seasonal_emoji_random()
        toolkit_text = f"Toolkit{seasonal_emoji}" if seasonal_emoji else "Toolkit"
        self.toolkit_btn = QPushButton(toolkit_text)
        self.toolkit_btn.setFixedSize(80, 24)  # Fixed width and height for consistent alignment
        self.toolkit_btn.setStyleSheet("""
            QPushButton {
                background-color: palette(base);
                color: palette(text);
                border: 1px solid palette(mid);
                padding: 4px 8px;
                border-radius: 3px;
                font-weight: bold;
                font-size: 11px;
                min-height: 24px;
            }
            QPushButton:hover {
                background-color: palette(highlight);
                color: palette(highlighted-text);
            }
            QPushButton:pressed {
                background-color: palette(dark);
                color: palette(light);
            }
        """)
        self.toolkit_btn.setCursor(Qt.PointingHandCursor)
        self.toolkit_btn.setToolTip("Open Innioasis Toolkit - Access all utilities and tools")
        self.toolkit_btn.clicked.connect(self.show_tools_dialog)
        device_type_layout.addWidget(self.toolkit_btn)
        
        device_type_layout.addStretch()

        # Device model filter
        device_model_layout = QHBoxLayout()
        device_model_layout.addWidget(QLabel("Device Model:"))

        self.device_model_combo = QComboBox()
        self.device_model_combo.currentTextChanged.connect(self.filter_firmware_options)
        device_model_layout.addWidget(self.device_model_combo)
        device_model_layout.addStretch()

        # Software filter (Repository)
        software_layout = QHBoxLayout()
        software_layout.addWidget(QLabel("Software:"))

        self.firmware_combo = QComboBox()
        # No "All Software" option - users must select specific software
        # Default selection will be set dynamically in populate_firmware_combo
        self.firmware_combo.currentTextChanged.connect(self.update_package_group_title)
        self.firmware_combo.currentTextChanged.connect(self.on_firmware_changed)
        # Make the software dropdown wider
        self.firmware_combo.setMinimumWidth(300)
        software_layout.addWidget(self.firmware_combo)
        software_layout.addStretch()

        filter_layout.addLayout(device_type_layout)
        filter_layout.addLayout(device_model_layout)
        filter_layout.addLayout(software_layout)

        left_layout.addWidget(filter_group)

        # Package list (now shows releases for selected repository)
        package_group = QGroupBox("Available System Software")
        self.package_group = package_group  # Store reference for dynamic updates
        package_layout = QVBoxLayout(package_group)

        self.package_list = QListWidget()
        self.package_list.itemClicked.connect(self.on_release_selected)
        self.package_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.package_list.customContextMenuRequested.connect(self.show_context_menu)

        # Add loading placeholder
        loading_item = QListWidgetItem("Loading...")
        loading_item.setFlags(loading_item.flags() & ~Qt.ItemIsSelectable)  # Make it non-selectable
        self.package_list.addItem(loading_item)

        package_layout.addWidget(self.package_list)

        left_layout.addWidget(package_group)

        # Download button
        seasonal_emoji = get_seasonal_emoji_random()
        download_text = f"Download{seasonal_emoji}" if seasonal_emoji else "Download"
        self.download_btn = QPushButton(download_text)
        self.download_btn.clicked.connect(self.start_download)
        self.download_btn.setEnabled(False)
        colors = self.get_theme_colors()
        self.download_btn.setStyleSheet("""
            QPushButton {
                background-color: #007AFF;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 3px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #0056CC;
            }
            QPushButton:pressed {
                background-color: #004499;
            }
            QPushButton:disabled {
                background-color: palette(mid);
                color: palette(text);
                opacity: 0.5;
            }
        """)
        left_layout.addWidget(self.download_btn)
        
        # Initially enable settings button (it will be disabled during operations if needed)
        self.settings_btn.setEnabled(True)
        # Enable toolkit button for all platforms
        if hasattr(self, 'toolkit_btn'):
            self.toolkit_btn.setEnabled(True)
        print("DEBUG: Settings button initially enabled")



        # Right panel - Status and output
        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)

        # Top right - Creator credit and social buttons
        coffee_layout = QHBoxLayout()

        # Creator credit
        creator_label = QLabel("Created by Ryan Specter of Team Slide")
        creator_label.setStyleSheet("""
            QLabel {
                color: #666666;
                font-size: 11px;
                font-style: italic;
            }
        """)
        coffee_layout.addWidget(creator_label)

        coffee_layout.addStretch()  # Push buttons to the right

        # Driver Setup button - Windows only, and only if drivers are missing
        if platform.system() == "Windows":
            driver_info = self.check_drivers_and_architecture()
            
            if driver_info['is_arm64']:
                # ARM64 Windows: Show ARM64-specific message
                arm64_btn = QPushButton("ARM64 Notice")
                arm64_btn.setStyleSheet("""
                    QPushButton {
                        background-color: palette(button);
                        color: palette(button-text);
                        border: 1px solid palette(mid);
                        padding: 8px 16px;
                        border-radius: 3px;
                        font-weight: bold;
                        font-size: 12px;
                    }
                    QPushButton:hover {
                        background-color: palette(highlight);
                        color: palette(highlighted-text);
                    }
                    QPushButton:pressed {
                        background-color: palette(dark);
                        color: palette(light);
                    }
                """)
                arm64_btn.clicked.connect(self.open_arm64_info)
                coffee_layout.addWidget(arm64_btn)
                
            elif not driver_info['has_mtk_driver'] and not driver_info['has_usbdk_driver']:
                # No drivers: Show "Install MediaTek & UsbDk Drivers" button
                driver_btn = QPushButton("🔧 Install MediaTek & UsbDk Drivers")
                driver_btn.setStyleSheet("""
                    QPushButton {
                        background-color: palette(button);
                        color: palette(button-text);
                        border: 1px solid palette(mid);
                        padding: 8px 16px;
                        border-radius: 3px;
                        font-weight: bold;
                        font-size: 12px;
                    }
                    QPushButton:hover {
                        background-color: palette(highlight);
                        color: palette(highlighted-text);
                    }
                    QPushButton:pressed {
                        background-color: palette(dark);
                        color: palette(light);
                    }
                """)
                driver_btn.clicked.connect(self.open_driver_setup_link)
                coffee_layout.addWidget(driver_btn)
                
            elif driver_info['has_mtk_driver'] and not driver_info['has_usbdk_driver']:
                # Only MTK driver: No additional UI elements needed
                pass
                
                # Only show "Install from .zip" button if not on ARM64 Windows
                if not driver_info['is_arm64']:
                    install_zip_btn = QPushButton("📦 Install from .zip")
                    install_zip_btn.setStyleSheet("""
                        QPushButton {
                            background-color: palette(button);
                            color: palette(button-text);
                            border: 1px solid palette(mid);
                            padding: 8px 16px;
                            border-radius: 3px;
                            font-weight: bold;
                            font-size: 12px;
                        }
                        QPushButton:hover {
                            background-color: palette(highlight);
                            color: palette(highlighted-text);
                        }
                        QPushButton:pressed {
                            background-color: palette(dark);
                            color: palette(light);
                        }
                    """)
                    install_zip_btn.clicked.connect(self.install_from_zip)
                    coffee_layout.addWidget(install_zip_btn)
                
            else:
                # Both drivers available: Show "Install from .zip" button (but not on ARM64)
                if not driver_info['is_arm64']:
                    install_zip_btn = QPushButton("📦 Install from .zip")
                    install_zip_btn.setStyleSheet("""
                        QPushButton {
                            background-color: palette(button);
                            color: palette(button-text);
                            border: 1px solid palette(mid);
                            padding: 8px 16px;
                            border-radius: 3px;
                            font-weight: bold;
                            font-size: 12px;
                        }
                        QPushButton:hover {
                            background-color: palette(highlight);
                            color: palette(highlighted-text);
                        }
                        QPushButton:pressed {
                            background-color: palette(dark);
                            color: palette(light);
                        }
                    """)
                    install_zip_btn.clicked.connect(self.install_from_zip)
                    coffee_layout.addWidget(install_zip_btn)
        else:
            # On non-Windows systems, show "Install from .zip" button
            install_zip_btn = QPushButton("📦 Install from .zip")
            install_zip_btn.setStyleSheet("""
                QPushButton {
                    background-color: palette(button);
                    color: palette(button-text);
                    border: 1px solid palette(mid);
                    padding: 8px 16px;
                    border-radius: 3px;
                    font-weight: bold;
                    font-size: 12px;
                }
                QPushButton:hover {
                    background-color: palette(highlight);
                    color: palette(highlighted-text);
                }
                QPushButton:pressed {
                    background-color: palette(dark);
                    color: palette(light);
                }
            """)
            install_zip_btn.clicked.connect(self.install_from_zip)
            coffee_layout.addWidget(install_zip_btn)

        # Reddit button moved to About tab

        # Discord button
        seasonal_emoji = get_seasonal_emoji_random()
        discord_text = f"Get Help{seasonal_emoji}" if seasonal_emoji else "Get Help"
        discord_btn = QPushButton(discord_text)
        discord_btn.setStyleSheet("""
            QPushButton {
                background-color: palette(base);
                color: palette(text);
                border: 1px solid palette(mid);
                padding: 8px 16px;
                border-radius: 3px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: palette(highlight);
                color: palette(highlighted-text);
            }
            QPushButton:pressed {
                background-color: palette(dark);
                color: palette(light);
            }
        """)
        discord_btn.clicked.connect(self.open_discord_link)
        coffee_layout.addWidget(discord_btn)

        # About button (opens Settings dialog to About tab)
        about_btn = QPushButton("About")
        about_btn.setStyleSheet("""
            QPushButton {
                background-color: palette(base);
                color: palette(text);
                border: 1px solid palette(mid);
                padding: 8px 16px;
                border-radius: 3px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: palette(highlight);
                color: palette(highlighted-text);
            }
            QPushButton:pressed {
                background-color: palette(dark);
                color: palette(light);
            }
        """)
        about_btn.clicked.connect(self.show_settings_dialog)
        coffee_layout.addWidget(about_btn)

        right_layout.addLayout(coffee_layout)

        # App Update button (below social media buttons)
        update_layout = QHBoxLayout()
        update_layout.addStretch()  # Push button to the right

        self.update_btn_right = QPushButton("Check for Utility Updates")
        self.update_btn_right.setEnabled(True)  # Enable immediately
        self.update_btn_right.clicked.connect(self.launch_updater_script)
        self.update_btn_right.setToolTip("Downloads and installs the latest version of the Innioasis Updater")
        colors = self.get_theme_colors()
        self.update_btn_right.setStyleSheet("""
            QPushButton {
                background-color: palette(base);
                color: palette(text);
                border: 1px solid palette(mid);
                padding: 8px 16px;
                border-radius: 3px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: palette(highlight);
                color: palette(highlighted-text);
            }
            QPushButton:pressed {
                background-color: palette(dark);
                color: palette(light);
            }
            QPushButton:disabled {
                background-color: palette(mid);
                color: palette(text);
                opacity: 0.5;
            }
        """)
        update_layout.addWidget(self.update_btn_right)
        right_layout.addLayout(update_layout)

        # Status group
        status_group = QGroupBox("Status")
        status_layout = QVBoxLayout(status_group)

        self.status_label = QLabel("Please follow the instructions below to install this software on your Y1")
        self.status_label.setWordWrap(True)
        self.status_label.setMinimumHeight(30)  # Reduced height for compact display
        self.status_label.setMaximumHeight(40)  # Added maximum height constraint
        status_layout.addWidget(self.status_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setMinimumHeight(20)  # Ensure progress bar has proper height
        self.progress_bar.setMaximumHeight(25)  # Set maximum height for consistency
        status_layout.addWidget(self.progress_bar)

        right_layout.addWidget(status_group)

        # Output group
        output_group = QGroupBox("Getting Ready:")
        output_layout = QVBoxLayout(output_group)

        # Image display area
        self.image_label = QLabel()
        self.image_label.setMinimumSize(400, 300)  # Set minimum size for proper initial display
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet("""
            QLabel {
                background-color: transparent;
                border: 1px solid #cccccc;
                border-radius: 3px;
                color: #333;
            }
        """)

        # Load initial image with proper sizing
        self.load_presteps_image()

        # Ensure proper image sizing after window is fully initialized
        QTimer.singleShot(100, self.ensure_proper_image_sizing)

        output_layout.addWidget(self.image_label)

        right_layout.addWidget(output_group)

        # Add panels to splitter
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([480, 720])  # Adjusted for 1220px total width
        
        # Store references for panel hiding/showing functionality
        self.splitter = splitter
        self.left_panel = left_panel
        self.right_panel = right_panel
        self.original_splitter_sizes = [480, 720]  # Store original sizes for restoration
        self.panel_hidden = False  # Track panel state

        # Check for test.py availability asynchronously to avoid blocking GUI launch
        self.check_test_py_availability_async()
        
        # Add status bar for driver information
        if platform.system() == "Windows":
            self.create_driver_status_bar()
    
    def is_test_py_available(self):
        """Check if test.py is available locally or at innioasis.app"""
        try:
            # Check local file first
            local_test_py = Path("test.py")
            if local_test_py.exists():
                return True
            
            # Check remote availability
            try:
                response = requests.get("https://innioasis.app/test.py", timeout=5)
                if response.status_code == 200:
                    return True
            except:
                pass
            
            return False
        except Exception:
            return False
    
    def check_test_py_availability_async(self):
        """Check for test.py availability asynchronously and add Labs link if available"""
        def check_and_add_labs():
            try:
                # Check local file first (fast)
                local_test_py = Path("test.py")
                if local_test_py.exists():
                    self.add_labs_link()
                    return
                
                # Check remote availability (slow, but async)
                try:
                    response = requests.get("https://innioasis.app/test.py", timeout=5)
                    if response.status_code == 200:
                        self.add_labs_link()
                except:
                    pass
            except Exception:
                pass
        
        # Run the check in a separate thread to avoid blocking GUI
        import threading
        thread = threading.Thread(target=check_and_add_labs, daemon=True)
        thread.start()
    
    def add_labs_link(self):
        """Add the Labs link to the GUI (called from async thread)"""
        # Use QTimer to safely update GUI from background thread
        QTimer.singleShot(0, self._add_labs_link_safe)
    
    def _add_labs_link_safe(self):
        """Safely add Labs link to GUI from main thread"""
        try:
            # Check if we already added the labs link
            if hasattr(self, 'labs_link'):
                return
            
            labs_layout = QHBoxLayout()
            labs_layout.addStretch()  # Push to the right
            
            # Check if current file is test.py or firmware_downloader.py
            current_file = Path(__file__).name
            if current_file == "test.py":
                labs_text = "Labs ON"
            else:
                labs_text = "Labs OFF"
                
            self.labs_link = QLabel(labs_text)
            self.labs_link.setStyleSheet("""
                QLabel {
                    color: #0066CC;
                    font-size: 11px;
                    text-decoration: underline;
                    cursor: pointer;
                }
                QLabel:hover {
                    color: #004499;
                }
            """)
            self.labs_link.setCursor(Qt.PointingHandCursor)
            self.labs_link.mousePressEvent = self.switch_to_labs_version
            labs_layout.addWidget(self.labs_link)
            
            # Find the main layout and add the labs layout
            # We need to find the right layout to add to
            main_widget = self.centralWidget()
            if main_widget:
                main_layout = main_widget.layout()
                if main_layout:
                    main_layout.addLayout(labs_layout)
        except Exception as e:
            silent_print(f"Error adding labs link: {e}")
    
    def download_test_py(self):
        """Download test.py from innioasis.app with progress bar"""
        try:
            # Create progress dialog
            progress_dialog = QDialog(self)
            progress_dialog.setWindowTitle("Downloading test.py")
            progress_dialog.setFixedSize(400, 150)
            progress_dialog.setModal(True)
            
            layout = QVBoxLayout(progress_dialog)
            
            # Status label
            status_label = QLabel("Downloading test.py from innioasis.app...")
            status_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(status_label)
            
            # Progress bar
            progress_bar = QProgressBar()
            progress_bar.setRange(0, 0)  # Indeterminate progress
            layout.addWidget(progress_bar)
            
            # Show dialog
            progress_dialog.show()
            QApplication.processEvents()
            
            # Download the file
            url = "https://innioasis.app/test.py"
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()
            
            # Get file size for progress tracking
            total_size = int(response.headers.get('content-length', 0))
            if total_size > 0:
                progress_bar.setRange(0, total_size)
                progress_bar.setValue(0)
            
            # Download and save file
            downloaded = 0
            with open("test.py", "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_size > 0:
                            progress_bar.setValue(downloaded)
                        QApplication.processEvents()
            
            # Update status
            status_label.setText("Download completed successfully!")
            progress_bar.setValue(progress_bar.maximum())
            QApplication.processEvents()
            
            # Close dialog after a brief delay
            QTimer.singleShot(1000, progress_dialog.accept)
            progress_dialog.exec()
            
            return True
            
        except Exception as e:
            # Close dialog on error
            if 'progress_dialog' in locals():
                progress_dialog.close()
            silent_print(f"Error downloading test.py: {e}")
            return False

    def create_driver_status_bar(self):
        """Create a status bar showing driver information for Windows users"""
        driver_info = self.check_drivers_and_architecture()
        
        # Create status bar
        status_bar = self.statusBar()
        
        if driver_info['is_arm64']:
            # ARM64 Windows: Show ARM64-specific message
            status_bar.showMessage("Only 'Tools' is available on ARM64 Windows, please use WSLg, Linux or another computer for Software Installs")
        elif not driver_info['has_mtk_driver']:
            # No MTK driver: Show driver requirement message
            status_bar.showMessage("MTK USB Driver not installed. Click 'Install Windows Drivers' to use Innioasis Updater.")
        else:
            # MTK driver available (with or without UsbDk): No status message needed
            status_bar.showMessage("")

    def stop_mtk_processes(self):
        """Stop any running MTK processes"""
        try:
            if platform.system() == "Windows":
                # Stop any running mtk.py processes on Windows
                subprocess.run(['taskkill', '/F', '/IM', 'python.exe', '/FI', 'WINDOWTITLE eq *mtk*'], 
                              capture_output=True, timeout=5)
            else:
                # Stop any running mtk.py processes on Unix-like systems
                subprocess.run(['pkill', '-f', 'mtk.py'], capture_output=True, timeout=5)
            silent_print("Stopped any running MTK processes")
        except Exception as e:
            silent_print(f"Error stopping MTK processes: {e}")

    def cleanup_libusb_state(self):
        """Clean up libusb state and USB device connections"""
        try:
            if platform.system() == "Windows":
                # On Windows, try to reset USB devices
                silent_print("Cleaning up USB state on Windows...")
                # This is a placeholder - actual USB reset would require more complex implementation
            else:
                # On Unix-like systems, try to reset USB devices
                silent_print("Cleaning up USB state on Unix-like system...")
                # This is a placeholder - actual USB reset would require more complex implementation
            silent_print("USB state cleanup completed")
        except Exception as e:
            silent_print(f"Error during USB state cleanup: {e}")

    def revert_to_startup_state(self):
        """Revert the application to its startup state"""
        try:
            # Reset status and progress
            # Add seasonal emoji to ready status
            seasonal_emoji = get_seasonal_emoji_random()
            ready_text = f"Ready{seasonal_emoji}" if seasonal_emoji else "Ready"
            self.status_label.setText(ready_text)
            self.progress_bar.setVisible(False)
            
            # Load initial image
            self.load_presteps_image()
            
            # Restore left panel to default state
            self.show_left_panel()
            
            # Update driver status bar if on Windows
            if platform.system() == "Windows":
                self.create_driver_status_bar()
                
            silent_print("Application reverted to startup state")
        except Exception as e:
            silent_print(f"Error reverting to startup state: {e}")

    def run_mtk_command(self):
        """Run the MTK command for firmware installation"""
        try:
            # Check driver availability for Windows users
            if platform.system() == "Windows":
                driver_info = self.check_drivers_and_architecture()
                
                if driver_info['is_arm64']:
                    QMessageBox.information(
                        self,
                        "ARM64 Windows Not Supported",
                        "Firmware installation is not supported on ARM64 Windows.\n\n"
                        "You can download firmware files, but to install them please use:\n"
                        "• WSLg (Windows Subsystem for Linux with GUI)\n"
                        "• Linux (dual boot or live USB)\n"
                        "• Another computer with x64 Windows"
                    )
                    return
                    
                elif not driver_info['can_install_firmware']:
                    QMessageBox.warning(
                        self,
                        "Drivers Required",
                        "No installation methods available. Please install drivers to enable firmware installation.\n\n"
                        "Click OK to open the driver installation guide."
                    )
                    self.open_driver_setup_link()
                    return
            
            # Create installation marker
            create_installation_marker()
            
            # Start MTK worker
            if not self.mtk_worker or not self.mtk_worker.isRunning():
                # Create debug window if debug mode is enabled
                debug_window = None
                if getattr(self, 'debug_mode', False):
                    debug_window = DebugOutputWindow(self)
                    debug_window.show()
                
                self.mtk_worker = MTKWorker(debug_mode=getattr(self, 'debug_mode', False), debug_window=debug_window)
                self.mtk_worker.status_updated.connect(self.update_status)
                self.mtk_worker.show_installing_image.connect(self.load_installing_image)
                self.mtk_worker.show_reconnect_image.connect(self.load_handshake_error_image)
                self.mtk_worker.show_presteps_image.connect(self.load_presteps_image)
                self.mtk_worker.show_please_wait_image.connect(self.load_please_wait_image)
                self.mtk_worker.show_initsteps_image.connect(self.load_initsteps_image)
                self.mtk_worker.show_instructions_image.connect(self.load_initsteps_image)
                self.mtk_worker.show_try_again_dialog.connect(self.show_try_again_dialog)
                self.mtk_worker.mtk_completed.connect(self.handle_mtk_completion)
                self.mtk_worker.handshake_failed.connect(self.handle_handshake_failure)
                self.mtk_worker.errno2_detected.connect(self.handle_errno2_error)
                self.mtk_worker.backend_error_detected.connect(self.handle_backend_error)
                self.mtk_worker.keyboard_interrupt_detected.connect(self.handle_keyboard_interrupt)
                self.mtk_worker.disable_update_button.connect(self.disable_update_button)
                self.mtk_worker.enable_update_button.connect(self.enable_update_button)
                self.mtk_worker.start()
                
                self.status_label.setText("Starting MTK installation...")
                silent_print("MTK worker started")
            else:
                silent_print("MTK worker already running")
                
        except Exception as e:
            silent_print(f"Error starting MTK command: {e}")
            self.status_label.setText(f"Error starting MTK command: {e}")

    def update_status(self, message):
        """Update the status label with a message"""
        if not message or message.strip() == "":
            self.status_label.setText("Please follow the instructions below to install this software on your Y1")
        elif message.strip() == "MTK: Preloader":
            # Just "MTK: Preloader" indicates freeze state
            self.status_label.setText("Please disconnect your Y1 and restart the app")
        elif message.startswith("MTK:") and (message.strip() == "MTK:" or 
                                              message.strip() == "MTK:..........." or 
                                              message.strip() == "MTK: ..........." or
                                              message.strip() == "MTK: .........." or
                                              message.strip() == "MTK: ........" or
                                              message.strip() == "MTK: ......." or
                                              message.strip() == "MTK: ......" or
                                              message.strip() == "MTK: ....." or
                                              message.strip() == "MTK: ...." or
                                              message.strip() == "MTK: ..." or
                                              message.strip() == "MTK: .." or
                                              message.strip() == "MTK: ." or
                                              message.strip() == "MTK: " or  # Just "MTK: " with space
                                              message.strip().startswith("MTK:...") or  # Lines beginning with dots
                                              message.strip().startswith("MTK:  ") or  # Lines with just spaces
                                              len(message.strip()) <= 10):  # Very short MTK messages likely indicate waiting
            # MTK is waiting for device connection or showing dots/spaces
            self.status_label.setText("Now please follow the instructions displayed below. Please force quit the app if not responding and restart it.")
        else:
            self.status_label.setText(message)

    def handle_mtk_completion(self, success, message):
        """Handle MTK command completion"""
        if success:
            # Add seasonal emoji to completion message
            seasonal_emoji = get_seasonal_emoji_random()
            completion_text = f"Installation completed successfully{seasonal_emoji}" if seasonal_emoji else "Installation completed successfully"
            self.status_label.setText(completion_text)
            self.load_installed_image()
            remove_installation_marker()
            # Restore left panel after successful installation
            self.show_left_panel()
        else:
            self.status_label.setText(f"Installation failed: {message}")
            self.load_process_ended_image()
            remove_installation_marker()
            # Restore left panel after failed installation
            self.show_left_panel()
            # Revert to startup state after showing error
            QTimer.singleShot(3000, self.revert_to_startup_state)

    def handle_handshake_failure(self):
        """Handle handshake failure"""
        self.status_label.setText("Please unplug your Y1 and try again")
        self.load_initsteps_image()

    def handle_errno2_error(self):
        """Handle errno2 error"""
        self.status_label.setText("Errno2 error - Innioasis Updater reinstall required")
        self.load_process_ended_image()
        # Revert to startup state after showing error
        QTimer.singleShot(3000, self.revert_to_startup_state)

    def handle_backend_error(self):
        """Handle backend error"""
        self.status_label.setText("Backend error - libusb backend issue")
        self.load_process_ended_image()
        # Revert to startup state after showing error
        QTimer.singleShot(3000, self.revert_to_startup_state)

    def handle_keyboard_interrupt(self):
        """Handle keyboard interrupt"""
        self.status_label.setText("Installation interrupted by user")
        self.load_process_ended_image()
        # Revert to startup state after showing error
        QTimer.singleShot(3000, self.revert_to_startup_state)

    def disable_update_button(self):
        """Disable the update button during MTK installation"""
        if hasattr(self, 'update_btn_right'):
            self.update_btn_right.setEnabled(False)

    def enable_update_button(self):
        """Enable the update button when returning to ready state"""
        if hasattr(self, 'update_btn_right'):
            self.update_btn_right.setEnabled(True)

    def show_troubleshooting_instructions(self):
        """Show Method 2 troubleshooting instructions"""
        try:
            # Load Method 2 image
            self.load_method2_image()
            
            # Show dialog with Method 2 instructions
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Method 2 - in Terminal Troubleshooting")
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setText("Method 2: in Terminal Direct Installation")
            msg_box.setInformativeText(
                "This method uses the MTKclient library directly for firmware installation.\n\n"
                "Please follow the on-screen instructions and ensure your device is properly connected.\n\n"
                "If this method fails, you may need to check your drivers or try Method 3 (SP Flash Tool Console Mode)."
            )
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.exec()
            
        except Exception as e:
            silent_print(f"Error showing Method 2 instructions: {e}")

    def try_method_3(self):
        """Try Method 3 - SP Flash Tool (Windows only) - Guided Process"""
        try:
            if platform.system() != "Windows":
                QMessageBox.warning(
                    self,
                    "Method 3 Not Available",
                    "Method 3 (SP Flash Tool) is only available on Windows."
                )
                return
            
            # No need to check for shortcut since we're using flash_tool.exe directly
            
            # Load please wait image initially
            self.load_please_wait_image()
            
            # Show dialog with Method 3 instructions
            reply = QMessageBox.question(
                self,
                "Software Install instructions",
                "Power off your Y1:\n"
                "Make sure is NOT connected then, Press OK.\n\n"
                "Then follow the on screen instructions...\n\n"
                "Powering Off: You can also insert a pin/paper clip in the hole on the bottom).",
                QMessageBox.Ok | QMessageBox.Cancel,
                QMessageBox.Ok
            )
            
            if reply == QMessageBox.Cancel:
                # Show appropriate buttons again when cancelled
                self.show_appropriate_buttons_for_spflash()
                # Show left panel again when cancelled
                self.show_left_panel()
                return
            
            # No need to stop MTK processes since Method 3 uses flash_tool.exe directly
            
            # Check if flash_tool.exe and install_rom_sp.xml exist
            current_dir = Path.cwd()
            flash_tool_exe = current_dir / "flash_tool.exe"
            install_rom_xml = current_dir / "install_rom_sp.xml"
            
            if not flash_tool_exe.exists():
                # Show appropriate buttons again when flash tool is missing
                self.show_appropriate_buttons_for_spflash()
                # Show left panel again when flash tool is missing
                self.show_left_panel()
                QMessageBox.critical(
                    self,
                    "Flash Tool Not Found",
                    "flash_tool.exe not found. Please ensure it's properly installed."
                )
                return
                
            if not install_rom_xml.exists():
                # Show appropriate buttons again when XML is missing
                self.show_appropriate_buttons_for_spflash()
                # Show left panel again when XML is missing
                self.show_left_panel()
                QMessageBox.critical(
                    self,
                    "Install ROM XML Not Found",
                    "install_rom_sp.xml not found. Please ensure it's properly installed."
                )
                return
            
            # Start the SP Flash Tool worker
            self.spflash_worker = SPFlashToolWorker()
            self.spflash_worker.status_updated.connect(self.status_label.setText)
            self.spflash_worker.show_installing_image.connect(self.load_installing_image)
            self.spflash_worker.show_initsteps_image.connect(self.load_method3_image)  # Use initsteps_sp.png for SP Flash Tool initsteps
            self.spflash_worker.show_installed_image.connect(self.load_installed_image)  # Use installed.png for completion
            self.spflash_worker.show_please_wait_image.connect(self.load_please_wait_image)  # Use please_wait.png for initial phase
            self.spflash_worker.spflash_completed.connect(self.on_spflash_completed)
            self.spflash_worker.disable_update_button.connect(self.disable_update_button)
            self.spflash_worker.enable_update_button.connect(self.enable_update_button)
            
            # Hide inappropriate buttons for SP Flash Tool method
            self.hide_inappropriate_buttons_for_spflash()
            
            # Hide left panel for SP Flash Tool installation to focus user attention on instructions
            self.hide_left_panel()
            
            # Disable remaining buttons during installation
            self.settings_btn.setEnabled(False)
            if hasattr(self, 'toolkit_btn'):
                self.toolkit_btn.setEnabled(False)
            
            # Start the worker
            self.spflash_worker.start()
            
        except Exception as e:
            silent_print(f"Error starting Method 3: {e}")
            # Show appropriate buttons again in case of error
            self.show_appropriate_buttons_for_spflash()
            # Show left panel again in case of error
            self.show_left_panel()
            QMessageBox.critical(
                self,
                "Method 3 Error",
                f"Failed to start SP Flash Tool:\n{e}"
            )

    def on_spflash_completed(self, success, message):
        """Handle SP Flash Tool completion"""
        try:
            # Show appropriate buttons for SP Flash Tool method
            self.show_appropriate_buttons_for_spflash()
            
            # Show left panel again after installation
            self.show_left_panel()
            
            # Re-enable buttons
            self.settings_btn.setEnabled(True)
            if hasattr(self, 'toolkit_btn'):
                self.toolkit_btn.setEnabled(True)
            
            if success:
                # Show success message and load completion image
                self.status_label.setText("Your software installation completed successfully")
                # Load the installed completion image
                self.load_installed_image()
                
                # Show success dialog with seasonal emoji
                seasonal_emoji = get_seasonal_emoji_random()
                dialog_title = f"Installation Complete{seasonal_emoji}" if seasonal_emoji else "Installation Complete"
                QMessageBox.information(
                    self,
                    dialog_title,
                    "Your installation has completed successfully!\n\n"
                    "Please disconnect your Y1 and hold the middle button to turn it on."
                )
            else:
                # Show error message and revert to startup state
                self.status_label.setText(f"Flash Tool installation failed: {message}")
                QMessageBox.critical(
                    self,
                    "Installation Failed",
                    f"Installation failed:\n{message}\n\n"
                    "Please disconnect your Y1 from USB and try again, if this fails visit troubleshooting.innioasis.app."
                )
                # Revert to startup state after showing error
                self.revert_to_startup_state()
                
        except Exception as e:
            silent_print(f"Error handling Flash Tool completion: {e}")

    def try_method_4(self):
        """Try SP Flash Tool GUI (Windows only) - Launches SP Flash Tool - GUI.lnk from Toolkit directory"""
        try:
            if platform.system() != "Windows":
                QMessageBox.warning(
                    self,
                    "SP Flash Tool GUI Not Available",
                    "SP Flash Tool GUI is only available on Windows."
                )
                return
            
            # Check if SP Flash Tool - GUI.lnk exists in Toolkit directory
            current_dir = Path.cwd()
            toolkit_dir = current_dir / "Toolkit"
            sp_flash_tool_lnk = toolkit_dir / "SP Flash Tool - GUI.lnk"
            
            if not sp_flash_tool_lnk.exists():
                QMessageBox.critical(
                    self,
                    "SP Flash Tool GUI Not Found",
                    "SP Flash Tool - GUI.lnk not found in Toolkit directory. Please ensure it's properly installed."
                )
                return
            
            # Show dialog with SP Flash Tool GUI instructions
            reply = QMessageBox.question(
                self,
                "SP Flash Tool GUI",
                "SP Flash Tool GUI will now launch.\n\n"
                "Power off your Y1:\n"
                "Make sure is NOT connected then, Press OK.\n\n"
                "Then follow the on screen instructions...\n\n"
                "Powering Off: You can also insert a pin/paper clip in the hole on the bottom).\n\n"
                "This method launches the SP Flash Tool GUI interface.",
                QMessageBox.Ok | QMessageBox.Cancel,
                QMessageBox.Ok
            )
            
            if reply == QMessageBox.Cancel:
                return
            
            # Launch SP Flash Tool - GUI.lnk from Toolkit directory using proper Windows method
            try:
                # Use os.startfile() to properly launch .lnk files on Windows
                import os
                os.startfile(str(sp_flash_tool_lnk))
                silent_print(f"Launched SP Flash Tool GUI: {sp_flash_tool_lnk}")
                
                # Show success message
                QMessageBox.information(
                    self,
                    "SP Flash Tool GUI Launched",
                    "Your downloaded ROM is loaded into SP Flash Tool's GUI\n\n"
                    "Make sure you power off your Y1 and select Format All + Download in the drop down menu."
                )
                
                # Revert to ready and presteps.png state after successful launch
                self.revert_to_startup_state()
                
            except Exception as e:
                silent_print(f"Error launching SP Flash Tool GUI: {e}")
                QMessageBox.critical(
                    self,
                    "Launch Error",
                    f"Failed to launch SP Flash Tool GUI:\n\n{e}"
                )
            
        except Exception as e:
            silent_print(f"Error in SP Flash Tool GUI method: {e}")
            QMessageBox.critical(
                self,
                "Error",
                f"An error occurred: {e}"
            )

    def try_method_3_console(self):
        """Try Method 3 - SP Flash Tool Console Mode (Windows only) - Launches SP Flash Tool.lnk from Toolkit directory"""
        try:
            if platform.system() != "Windows":
                QMessageBox.warning(
                    self,
                    "Method 3 Not Available",
                    "Method 3 (SP Flash Tool Console Mode) is only available on Windows."
                )
                return
            
            # Check if SP Flash Tool.lnk exists in Toolkit directory
            current_dir = Path.cwd()
            toolkit_dir = current_dir / "Toolkit"
            sp_flash_tool_lnk = toolkit_dir / "SP Flash Tool.lnk"
            
            if not sp_flash_tool_lnk.exists():
                QMessageBox.critical(
                    self,
                    "SP Flash Tool Console Mode Not Found",
                    "SP Flash Tool.lnk not found in Toolkit directory. Please ensure it's properly installed."
                )
                return
            
            # Show dialog with Method 3 Console Mode instructions
            reply = QMessageBox.question(
                self,
                "SP Flash Tool Console Mode",
                "SP Flash Tool Console Mode will now launch.\n\n"
                "Power off your Y1:\n"
                "Make sure is NOT connected then, Press OK.\n\n"
                "Then follow the on screen instructions...\n\n"
                "Powering Off: You can also insert a pin/paper clip in the hole on the bottom).\n\n"
                "This method launches the SP Flash Tool console interface.",
                QMessageBox.Ok | QMessageBox.Cancel,
                QMessageBox.Ok
            )
            
            if reply == QMessageBox.Cancel:
                return
            
            # Launch SP Flash Tool.lnk from Toolkit directory using proper Windows method
            try:
                # Use os.startfile() to properly launch .lnk files on Windows
                import os
                os.startfile(str(sp_flash_tool_lnk))
                silent_print(f"Launched SP Flash Tool Console Mode: {sp_flash_tool_lnk}")
                
                # Show success message
                QMessageBox.information(
                    self,
                    "SP Flash Tool Console Mode Launched",
                    "SP Flash Tool Console Mode has been launched successfully.\n\n"
                    "Please follow the instructions in the SP Flash Tool window to complete the installation."
                )
                
                # Revert to ready and presteps.png state after successful launch
                self.revert_to_startup_state()
                
            except Exception as e:
                silent_print(f"Error launching SP Flash Tool Console Mode: {e}")
                QMessageBox.critical(
                    self,
                    "Launch Error",
                    f"Failed to launch SP Flash Tool Console Mode:\n\n{e}"
                )
            
        except Exception as e:
            silent_print(f"Error in SP Flash Tool Console Mode method: {e}")
            QMessageBox.critical(
                self,
                "Error",
                f"An error occurred: {e}"
            )

    def load_method2_image(self):
        """Load Method 2 troubleshooting image"""
        try:
            if not hasattr(self, '_method2_pixmap'):
                image_path = self.get_platform_image_path("method2")
                self._method2_pixmap = QPixmap(image_path)
                if self._method2_pixmap.isNull():
                    silent_print(f"Failed to load Method 2 image from {image_path}")
                    return
            
            self._current_pixmap = self._method2_pixmap
            self.set_image_with_aspect_ratio(self._method2_pixmap)
        except Exception as e:
            silent_print(f"Error loading Method 2 image: {e}")
            return

    def load_method3_image(self):
        """Load Method 3 SP Flash Tool initsteps image"""
        try:
            if not hasattr(self, '_method3_pixmap'):
                # Use initsteps_sp.png directly (Windows-only method, no platform suffix needed)
                image_path = Path("mtkclient/gui/images/initsteps_sp.png")
                self._method3_pixmap = QPixmap(str(image_path))
                if self._method3_pixmap.isNull():
                    silent_print(f"Failed to load Method 3 SP Flash Tool image from {image_path}")
                    return
            
            self._current_pixmap = self._method3_pixmap
            self.set_image_with_aspect_ratio(self._method3_pixmap)
        except Exception as e:
            silent_print(f"Error loading Method 3 SP Flash Tool image: {e}")

    def load_installed_image(self):
        """Load installed completion image"""
        try:
            if not hasattr(self, '_installed_pixmap'):
                image_path = self.get_platform_image_path("installed")
                self._installed_pixmap = QPixmap(image_path)
                if self._installed_pixmap.isNull():
                    silent_print(f"Failed to load installed image from {image_path}")
                    return
            
            self._current_pixmap = self._installed_pixmap
            self.set_image_with_aspect_ratio(self._installed_pixmap)
        except Exception as e:
            silent_print(f"Error loading installed image: {e}")
            return

    def load_please_wait_image(self):
        """Load please wait image"""
        try:
            if not hasattr(self, '_please_wait_pixmap'):
                image_path = self.get_platform_image_path("please_wait")
                self._please_wait_pixmap = QPixmap(image_path)
                if self._please_wait_pixmap.isNull():
                    silent_print(f"Failed to load please wait image from {image_path}")
                    return
            
            self._current_pixmap = self._please_wait_pixmap
            self.set_image_with_aspect_ratio(self._please_wait_pixmap)
        except Exception as e:
            silent_print(f"Error loading please wait image: {e}")
            return

    def load_method4_image(self):
        """Load SP Flash Tool GUI Method image"""
        try:
            if not hasattr(self, '_method4_pixmap'):
                # Try method4.png first, fallback to method3.png if not found
                image_path = self.get_platform_image_path("method4")
                self._method4_pixmap = QPixmap(image_path)
                if self._method4_pixmap.isNull():
                    silent_print(f"SP Flash Tool GUI Method image not found, trying fallback to method3.png")
                    # Fallback to method3.png
                    fallback_path = self.get_platform_image_path("method3")
                    self._method4_pixmap = QPixmap(fallback_path)
                    if self._method4_pixmap.isNull():
                        silent_print(f"Failed to load SP Flash Tool GUI Method fallback image from {fallback_path}")
                        return
            
            self._current_pixmap = self._method4_pixmap
            self.set_image_with_aspect_ratio(self._method4_pixmap)
        except Exception as e:
            silent_print(f"Error loading SP Flash Tool GUI Method image: {e}")
            return

    def load_data(self):
        """Load configuration and manifest data with instant startup optimization"""
        self.status_label.setText("Loading configuration...")
        silent_print("Loading configuration and manifest data...")

        # Load manifest first for instant startup (no token validation needed)
        self.packages = self.config_downloader.download_manifest(use_local_first=True)
        if self.packages:
            silent_print(f"Loaded {len(self.packages)} software packages from local manifest")
            self.status_label.setText("Ready: Select system software to Download. Your music will stay safe.")
            
            # Initialize github_api with empty tokens for immediate UI population
            # This allows the UI to work while tokens are loaded in background
            self.github_api = GitHubAPI([])
            silent_print("Initialized GitHub API with empty tokens for instant startup")
            
            # Populate UI components immediately
            self.populate_device_type_combo()
            self.populate_device_model_combo()
            self.populate_firmware_combo()
            self.filter_firmware_options()
            QTimer.singleShot(100, self.apply_initial_release_display)
            self.status_label.setText("Ready")
            silent_print("Data loading complete - instant startup achieved")
        
        # Start background token validation and remote manifest refresh
        QTimer.singleShot(100, self.load_tokens_and_validate_background)

    def load_tokens_and_validate_background(self):
        """Load and validate tokens in background without blocking UI"""
        try:
            # Clear cache at startup to ensure fresh tokens are fetched
            clear_cache()
            silent_print("Cleared cache at startup to fetch fresh tokens")

            # Download tokens
            tokens = self.config_downloader.download_config()
            if not tokens:
                silent_print("No API tokens available - using unauthenticated mode")
                return

            # Replace the empty GitHubAPI with properly initialized one
            self.github_api = GitHubAPI(tokens)
            silent_print(f"Loaded {len(tokens)} API tokens")

            # Start parallel token validation in background
            if tokens:
                silent_print(f"Validating {len(tokens)} API tokens in background...")
                # Start parallel token validation
                self.validate_tokens_parallel(tokens)
            else:
                silent_print("No tokens loaded - continuing with unauthenticated mode")
                return

        except Exception as e:
            silent_print(f"Background token loading error: {e}")
            # Continue with unauthenticated mode

    def validate_tokens_parallel(self, tokens):
        """Validate tokens in parallel for faster startup"""
        if not tokens:
            silent_print("No tokens to validate, using unauthenticated mode")
            # Don't update status label - keep it as "Ready" for user experience
            self.finish_data_loading([])
            return

        def validate_single_token(token):
            """Validate a single token"""
            try:
                # Check if token already has prefix to avoid double-prefixing
                if token.startswith('github_pat_'):
                    test_token = token
                else:
                    test_token = f"github_pat_{token}"
                silent_print(f"Testing token: {test_token[:20]}...")

                headers = {
                    'Authorization': f'token {test_token}',
                    'Accept': 'application/vnd.github.v3+json'
                }

                response = requests.get('https://api.github.com/user',
                                      headers=headers,
                                      timeout=TOKEN_VALIDATION_TIMEOUT)

                silent_print(f"Token validation response: {response.status_code}")

                if response.status_code == 200:
                    user_data = response.json()
                    silent_print(f"Token valid - authenticated as: {user_data.get('login', 'Unknown')}")
                    return token, user_data.get('login', 'Unknown')
                elif response.status_code == 401:
                    silent_print(f"Token invalid (401 Unauthorized)")
                    return None, None
                elif response.status_code == 403:
                    silent_print(f"Token rate limited (403 Forbidden) - will retry later")
                    # Don't mark rate-limited tokens as invalid, they might work later
                    return None, None
                else:
                    silent_print(f"Token failed - status: {response.status_code}")
                    return None, None

            except Exception as e:
                silent_print(f"Token validation error: {e}")
                return None, None

        # Use ThreadPoolExecutor for parallel validation
        with ThreadPoolExecutor(max_workers=min(len(tokens), MAX_CONCURRENT_REQUESTS)) as executor:
            # Submit all token validation tasks
            future_to_token = {executor.submit(validate_single_token, token): token for token in tokens}

            # Process results as they complete
            for future in as_completed(future_to_token):
                token, username = future.result()
                if token is not None:
                    # Found a working token, cancel other tasks and proceed
                    silent_print(f"Found working token for user: {username}")
                    # Don't update status label - keep it as "Ready" for user experience

                    # Cancel remaining tasks
                    for remaining_future in future_to_token:
                        if not remaining_future.done():
                            remaining_future.cancel()

                    # Mark token as working and proceed
                    self.github_api.mark_token_working(token)
                    silent_print("Background token validation completed - authenticated mode enabled")
                    return

        # If we get here, no tokens worked
        silent_print("All tokens failed validation, using unauthenticated mode")
        # Try with at least one token anyway, in case validation was too strict
        if tokens:
            silent_print("Attempting to use first token despite validation failure")
            # Check if token already has prefix to avoid double-prefixing
            first_token = tokens[0]
            if not first_token.startswith('github_pat_'):
                first_token = f"github_pat_{first_token}"
            self.github_api = GitHubAPI([first_token])
            silent_print("Background token validation completed - fallback mode enabled")
        else:
            silent_print("Background token validation completed - unauthenticated mode enabled")

    def finish_data_loading(self, working_tokens):
        """Complete data loading with working tokens"""
        self.status_label.setText("Loading software manifest...")

        # Ensure all tokens have github_pat_ prefix for GitHub API class
        api_tokens = []
        for token in working_tokens:
            if not token.startswith('github_pat_'):
                api_tokens.append(f"github_pat_{token}")
            else:
                api_tokens.append(token)

        silent_print(f"Prepared {len(api_tokens)} tokens for GitHub API")
        for i, token in enumerate(api_tokens):
            silent_print(f"Token {i+1}: {token[:20]}...")

        # Create GitHub API with properly formatted tokens
        self.github_api = GitHubAPI(api_tokens)
        
        # Start periodic cache cleanup
        self.github_api.cleanup_cache_periodically()

        # Download manifest (local-first for instant startup)
        self.packages = self.config_downloader.download_manifest(use_local_first=True)
        if not self.packages:
            silent_print("ERROR: Failed to load software manifest")
            self.status_label.setText("Error: Failed to load software manifest")
            return

        silent_print(f"Loaded {len(self.packages)} software packages")
        self.status_label.setText("Ready: Select system software to Download. Your music will stay safe.")

        # Populate UI components
        self.populate_device_type_combo()
        self.populate_device_model_combo()
        self.populate_firmware_combo()

        # Apply initial filters
        self.filter_firmware_options()

        # Use a timer to ensure the default selection is properly applied
        QTimer.singleShot(100, self.apply_initial_release_display)

        # Native widgets automatically adapt to theme changes - no timer needed

        self.status_label.setText("Ready")
        silent_print("Data loading complete")

    def apply_initial_release_display(self):
        """Apply the initial release display based on default software selection"""
        selected_repo = self.firmware_combo.currentData()
        if selected_repo:
            # Show releases for selected software
            self.populate_releases_list()
        else:
            # Show releases from all available software progressively
            self.populate_all_releases_list_progressive()

    def show_device_type_help(self):
        """Show device type help information in a dialog box"""
        help_text = """<h3>Device Type Selection Guide</h3>

<p><b>Type A Devices:</b> This is the recommended starting point for most users. Install this first to see if it meets your needs.</p>

<p><b>Type B Devices:</b> If your scroll wheel doesn't respond properly after installing Type A, try one of the Type B options. These are alternative configurations that may resolve scroll wheel issues.</p>

<p><b>Recommendation:</b> Always start with Type A. Only move to Type B if you experience scroll wheel problems.</p>"""

        # Create a native system dialog box
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Device Type Help")
        msg_box.setText(help_text)
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setDefaultButton(QMessageBox.Ok)

        # Ensure it uses native system styling
        msg_box.setModal(True)
        msg_box.exec()

    def open_y1_remote_control(self):
        """Open Y1 Remote Control application without closing firmware downloader"""
        print("DEBUG: Tools button clicked! open_y1_remote_control method called.")
        
        # Check if any operations are in progress
        if INSTALLATION_MARKER_FILE.exists():
            print("DEBUG: Installation marker exists, showing warning.")
            QMessageBox.warning(self, "Operation in Progress", 
                              "Cannot open Y1 Helper while firmware installation or troubleshooting is in progress.\n\nPlease wait for the current operation to complete.")
            return
        
        try:
            if platform.system() == "Windows":
                # On Windows, use the Toolkit shortcut to get separate process/taskbar icon
                toolkit_shortcut = Path("Toolkit") / "Remote Control.lnk"
                if toolkit_shortcut.exists():
                    subprocess.Popen([str(toolkit_shortcut)], shell=True)
                    self.status_label.setText("Y1 Remote Control launched successfully")
                else:
                    # Fallback to direct y1_helper.py if shortcut not found
                    y1_helper_path = Path("y1_helper.py")
                    if y1_helper_path.exists():
                        subprocess.Popen([sys.executable, str(y1_helper_path)])
                        self.status_label.setText("Y1 Remote Control launched successfully")
                    else:
                        QMessageBox.error(self, "Error", 
                                        "Y1 Remote Control not found. Please ensure y1_helper.py is in the same directory.")
            else:
                # On non-Windows systems, use direct Python execution
                y1_helper_path = Path("y1_helper.py")
                if y1_helper_path.exists():
                    subprocess.Popen([sys.executable, str(y1_helper_path)])
                    self.status_label.setText("Y1 Remote Control launched successfully")
                else:
                    QMessageBox.error(self, "Error", 
                                    "Y1 Remote Control not found. Please ensure y1_helper.py is in the same directory.")
        except Exception as e:
            QMessageBox.error(self, "Error", f"Failed to launch Y1 Remote Control: {e}")

    def open_toolkit_folder(self):
        """Open the Innioasis Toolkit folder in File Explorer (Windows only)"""
        try:
            if platform.system() != "Windows":
                return
            
            # Open the actual Toolkit folder in %LocalAppData%\Innioasis Updater\Toolkit
            toolkit_path = Path.home() / "AppData" / "Local" / "Innioasis Updater" / "Toolkit"
            
            if toolkit_path.exists():
                # Open the folder in File Explorer
                subprocess.run(["explorer", str(toolkit_path)], check=True)
                self.status_label.setText("Toolkit folder opened in File Explorer")
            else:
                QMessageBox.warning(self, "Toolkit Not Found", 
                                  f"Toolkit folder not found at:\n{toolkit_path}\n\nPlease ensure the toolkit is properly installed.")
        except Exception as e:
            QMessageBox.error(self, "Error", f"Failed to open toolkit folder: {e}")
    
    def launch_240p_theme_downloader(self):
        """Launch the 240p theme downloader"""
        try:
            script_path = Path("rockbox_240p_theme_downloader.py")
            if script_path.exists():
                subprocess.Popen([sys.executable, str(script_path)])
                self.status_label.setText("240p Theme Downloader launched")
            else:
                QMessageBox.warning(self, "File Not Found", 
                                  "240p Theme Downloader not found. Please ensure rockbox_240p_theme_downloader.py is in the same directory.")
        except Exception as e:
            QMessageBox.error(self, "Error", f"Failed to launch 240p Theme Downloader: {e}")
    
    def launch_360p_theme_downloader(self):
        """Launch the 360p theme downloader"""
        try:
            script_path = Path("rockbox_360p_theme_downloader.py")
            if script_path.exists():
                subprocess.Popen([sys.executable, str(script_path)])
                self.status_label.setText("360p Theme Downloader launched")
            else:
                QMessageBox.warning(self, "File Not Found", 
                                  "360p Theme Downloader not found. Please ensure rockbox_360p_theme_downloader.py is in the same directory.")
        except Exception as e:
            QMessageBox.error(self, "Error", f"Failed to launch 360p Theme Downloader: {e}")
    
    def launch_storage_management_tool(self):
        """Launch the storage management tool"""
        try:
            script_path = Path("manage_storage.py")
            if script_path.exists():
                subprocess.Popen([sys.executable, str(script_path)])
                self.status_label.setText("Storage Management Tool launched")
            else:
                QMessageBox.warning(self, "File Not Found", 
                                  "Storage Management Tool not found. Please ensure manage_storage.py is in the same directory.")
        except Exception as e:
            QMessageBox.error(self, "Error", f"Failed to launch Storage Management Tool: {e}")
    
    def launch_rockbox_utility(self):
        """Launch Rockbox Utility from Toolkit directory"""
        try:
            # Get the LocalAppData path
            local_app_data = os.environ.get('LOCALAPPDATA', '')
            if not local_app_data:
                QMessageBox.warning(self, "Error", "Could not find LocalAppData directory")
                return
            
            # Construct the path to Rockbox Utility.lnk
            rockbox_utility_path = Path(local_app_data) / "Innioasis Updater" / "Toolkit" / "Rockbox Utility.lnk"
            
            if rockbox_utility_path.exists():
                # Launch the shortcut
                subprocess.Popen([str(rockbox_utility_path)])
                self.status_label.setText("Rockbox Utility launched")
            else:
                QMessageBox.warning(self, "File Not Found", 
                                  f"Rockbox Utility not found at:\n{rockbox_utility_path}\n\nPlease ensure the Toolkit is properly installed.")
        except Exception as e:
            QMessageBox.error(self, "Error", f"Failed to launch Rockbox Utility: {e}")
    
    def show_settings_dialog(self, initial_tab="about"):
        """Show enhanced settings dialog with installation method and shortcut management"""
        silent_print(f"Opening settings dialog with initial_tab: {initial_tab}")
        dialog = QDialog(self)
        dialog.setWindowTitle("Settings")
        dialog.setFixedSize(590, 520)  # Reduced width by 160px and height by 80px for better proportions
        dialog.setModal(True)
        # Use native styling - no custom stylesheet for automatic theme adaptation
        
        layout = QVBoxLayout(dialog)
        
        # Create tabbed interface or sections
        tab_widget = QTabWidget()
        # Use native styling - no custom stylesheet for automatic theme adaptation
        layout.addWidget(tab_widget)
        
        # Installation Method Tab
        install_tab = QWidget()
        # Use native styling - no custom stylesheet for automatic theme adaptation
        install_layout = QVBoxLayout(install_tab)
        install_layout.setSpacing(8)  # Reduce spacing between widgets
        install_layout.setContentsMargins(10, 10, 10, 10)  # Set consistent margins
        
        
        # Check driver status for Windows users
        driver_info = None
        if platform.system() == "Windows":
            driver_info = self.check_drivers_and_architecture()
            
            # Show driver status message
            if driver_info['is_arm64']:
                status_label = QLabel("⚠️ ARM64 Windows Detected")
                status_label.setStyleSheet("color: #FF6B35; font-weight: bold; margin: 2px;")
                install_layout.addWidget(status_label)
                
                status_desc = QLabel("Only firmware downloads are available on ARM64 Windows.\nPlease use WSLg, Linux, or another computer for software installation.")
                status_desc.setStyleSheet("color: #666; margin: 2px;")
                install_layout.addWidget(status_desc)
                
                # Disable method selection for ARM64
                method_combo = QComboBox()
                method_combo.addItem("No installation methods available on ARM64 Windows", "")
                method_combo.setEnabled(False)
                install_layout.addWidget(method_combo)
                
                # Skip the rest of the dialog for ARM64
                button_layout = QHBoxLayout()
                button_layout.addStretch()
                ok_btn = QPushButton("OK")
                ok_btn.clicked.connect(dialog.accept)
                button_layout.addWidget(ok_btn)
                install_layout.addLayout(button_layout)
                tab_widget.addTab(install_tab, "Installation")
                dialog.exec()
                return
                
            elif not driver_info['can_install_firmware']:
                status_label = QLabel("⚠️ Drivers Required")
                status_label.setStyleSheet("color: #FF6B35; font-weight: bold; margin: 2px;")
                install_layout.addWidget(status_label)
                
                status_desc = QLabel("No installation methods available. Please install drivers to enable firmware installation.\n\nMore methods will become available if you install the USB Development Kit driver.")
                status_desc.setStyleSheet("color: #666; margin: 2px;")
                install_layout.addWidget(status_desc)
                
                # Disable method selection when no drivers
                method_combo = QComboBox()
                method_combo.addItem("No installation methods available without drivers", "")
                method_combo.setEnabled(False)
                install_layout.addWidget(method_combo)
                
                # Skip the rest of the dialog when no drivers
                button_layout = QHBoxLayout()
                button_layout.addStretch()
                ok_btn = QPushButton("OK")
                ok_btn.clicked.connect(dialog.accept)
                button_layout.addWidget(ok_btn)
                install_layout.addLayout(button_layout)
                tab_widget.addTab(install_tab, "Installation")
                dialog.exec()
                return
                
        
        # Description
        desc_label = QLabel("This setting will be used for the next firmware installation.")
        desc_label.setStyleSheet("margin: 2px;")
        install_layout.addWidget(desc_label)
        
        # Method selection
        method_label = QLabel("Installation Method:")
        # Use native styling - no custom stylesheet for automatic theme adaptation
        install_layout.addWidget(method_label)
        
        self.method_combo = QComboBox()
        
        # Add methods based on driver availability
        if platform.system() == "Windows" and driver_info:
            if driver_info['has_mtk_driver'] and driver_info['has_usbdk_driver']:
                # Both drivers available: All methods (Windows order: SP Flash Tool first, then Guided/MTKclient)
                # Add seasonal emojis to method names
                seasonal_emoji = get_seasonal_emoji_random()
                method1_text = f"Method 1 - Guided{seasonal_emoji}" if seasonal_emoji else "Method 1 - Guided"
                method2_text = f"Method 2 - SP Flash Tool GUI{seasonal_emoji}" if seasonal_emoji else "Method 2 - SP Flash Tool GUI"
                method3_text = f"Method 3 - SP Flash Tool Console Mode{seasonal_emoji}" if seasonal_emoji else "Method 3 - SP Flash Tool Console Mode"
                method4_text = f"SP Flash Tool GUI Method{seasonal_emoji}" if seasonal_emoji else "SP Flash Tool GUI Method"
                method5_text = f"Method 5 - MTKclient (advanced){seasonal_emoji}" if seasonal_emoji else "Method 5 - MTKclient (advanced)"
                
                self.method_combo.addItem(method1_text, "spflash")
                self.method_combo.addItem(method2_text, "spflash4")
                self.method_combo.addItem(method3_text, "spflash_console")
                self.method_combo.addItem(method4_text, "guided")
                self.method_combo.addItem(method5_text, "mtkclient")
            elif driver_info['has_mtk_driver'] and not driver_info['has_usbdk_driver']:
                # Only MTK driver: Only Method 1, 2, and 3 (SP Flash Tool methods)
                seasonal_emoji = get_seasonal_emoji_random()
                method1_text = f"Method 1 - Guided (Only available method){seasonal_emoji}" if seasonal_emoji else "Method 1 - Guided (Only available method)"
                method2_text = f"Method 2 - SP Flash Tool GUI{seasonal_emoji}" if seasonal_emoji else "Method 2 - SP Flash Tool GUI"
                method3_text = f"Method 3 - SP Flash Tool Console Mode{seasonal_emoji}" if seasonal_emoji else "Method 3 - SP Flash Tool Console Mode"
                
                self.method_combo.addItem(method1_text, "spflash")
                self.method_combo.addItem(method2_text, "spflash4")
                self.method_combo.addItem(method3_text, "spflash_console")
            elif not driver_info['has_mtk_driver'] and driver_info['has_usbdk_driver']:
                # Only UsbDk driver: Only Method 5 (MTKclient)
                seasonal_emoji = get_seasonal_emoji_random()
                method5_text = f"Method 5 - MTKclient (advanced) (Only available method){seasonal_emoji}" if seasonal_emoji else "Method 5 - MTKclient (advanced) (Only available method)"
                self.method_combo.addItem(method5_text, "mtkclient")
            else:
                # No drivers: No methods
                self.method_combo.addItem("No installation methods available", "")
        else:
            # Non-Windows: Standard methods
            seasonal_emoji = get_seasonal_emoji_random()
            method1_text = f"Method 1 - Guided{seasonal_emoji}" if seasonal_emoji else "Method 1 - Guided"
            method2_text = f"Method 2 - in Terminal{seasonal_emoji}" if seasonal_emoji else "Method 2 - in Terminal"
            
            self.method_combo.addItem(method1_text, "guided")
            self.method_combo.addItem(method2_text, "mtkclient")
        
        # Set current method
        current_method = getattr(self, 'installation_method', 'guided')
        index = self.method_combo.findData(current_method)
        if index >= 0:
            self.method_combo.setCurrentIndex(index)
        
        install_layout.addWidget(self.method_combo)
        
        # Always use this method checkbox removed - app now always defaults to Method 1
        
        # Debug mode is now controlled by keyboard shortcut (Ctrl+D/Cmd+D)
        # No checkbox needed in settings
        
        # Automatic Utility Updates checkbox moved to About tab
        
        
        # Add About tab first (will be added later)
        
        # Shortcut Management Tab (Windows only)
        if platform.system() == "Windows":
            shortcut_tab = QWidget()
            shortcut_layout = QVBoxLayout(shortcut_tab)
            
            shortcut_title = QLabel("Shortcut Management")
            shortcut_title.setStyleSheet("font-size: 14px; font-weight: bold; margin: 5px;")
            shortcut_layout.addWidget(shortcut_title)
            
            # Desktop shortcuts section
            desktop_group = QGroupBox("Desktop Shortcuts")
            desktop_layout = QVBoxLayout(desktop_group)
            
            self.desktop_updater_checkbox = QCheckBox("Updater")
            self.desktop_updater_checkbox.setToolTip("Create Innioasis Updater shortcut on desktop")
            desktop_updater = getattr(self, 'desktop_updater_enabled', True)
            self.desktop_updater_checkbox.setChecked(desktop_updater)
            self.desktop_updater_checkbox.toggled.connect(self.on_desktop_updater_toggled)
            desktop_layout.addWidget(self.desktop_updater_checkbox)
            
            self.desktop_toolkit_checkbox = QCheckBox("Toolkit")
            self.desktop_toolkit_checkbox.setToolTip("Create Innioasis Toolkit shortcut on desktop")
            desktop_toolkit = getattr(self, 'desktop_toolkit_enabled', False)  # Default to False for desktop
            self.desktop_toolkit_checkbox.setChecked(desktop_toolkit)
            self.desktop_toolkit_checkbox.toggled.connect(self.on_desktop_toolkit_toggled)
            desktop_layout.addWidget(self.desktop_toolkit_checkbox)
            
            shortcut_layout.addWidget(desktop_group)
            
            # Start menu shortcuts section
            startmenu_group = QGroupBox("Start Menu Shortcuts")
            startmenu_layout = QVBoxLayout(startmenu_group)
            
            self.startmenu_updater_checkbox = QCheckBox("Updater")
            self.startmenu_updater_checkbox.setToolTip("Create Innioasis Updater shortcut in start menu")
            startmenu_updater = getattr(self, 'startmenu_updater_enabled', True)
            self.startmenu_updater_checkbox.setChecked(startmenu_updater)
            self.startmenu_updater_checkbox.toggled.connect(self.on_startmenu_updater_toggled)
            startmenu_layout.addWidget(self.startmenu_updater_checkbox)
            
            self.startmenu_toolkit_checkbox = QCheckBox("Toolkit")
            self.startmenu_toolkit_checkbox.setToolTip("Create Innioasis Toolkit shortcut in start menu")
            startmenu_toolkit = getattr(self, 'startmenu_toolkit_enabled', True)
            self.startmenu_toolkit_checkbox.setChecked(startmenu_toolkit)
            self.startmenu_toolkit_checkbox.toggled.connect(self.on_startmenu_toolkit_toggled)
            startmenu_layout.addWidget(self.startmenu_toolkit_checkbox)
            
            shortcut_layout.addWidget(startmenu_group)
            
            # Note: Automatic cleanup is always enabled and not exposed to users
            # as it's required for proper shortcut management
            
            # Add shortcut tab to tab widget
            tab_widget.addTab(shortcut_tab, "Shortcuts")
        
        # About Tab
        about_tab = QWidget()
        # Use native styling - no custom stylesheet for automatic theme adaptation
        about_layout = QVBoxLayout(about_tab)
        about_layout.setAlignment(Qt.AlignCenter)
        
        # App icon (load from mtkclient/gui/images/icon.png)
        icon_label = QLabel()
        icon_path = Path("mtkclient/gui/images/icon.png")
        if icon_path.exists():
            try:
                pixmap = QPixmap(str(icon_path))
                # Scale the icon to a larger size for better visibility
                scaled_pixmap = pixmap.scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                icon_label.setPixmap(scaled_pixmap)
            except Exception as e:
                # Fallback to emoji if icon loading fails
                icon_label.setText("📱")
                icon_label.setStyleSheet("""
                    QLabel {
                        font-size: 80px;
                        color: #007AFF;
                        margin: 20px;
                    }
                """)
        else:
            # Fallback to emoji if icon file doesn't exist
            icon_label.setText("📱")
            icon_label.setStyleSheet("""
                QLabel {
                    font-size: 64px;
                    color: #007AFF;
                    margin: 20px;
                }
            """)
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setFixedHeight(100)  # Ensure enough space for the icon
        icon_label.setContentsMargins(0, 10, 0, 10)  # Add vertical padding
        about_layout.addWidget(icon_label)
        
        # Determine seasonal message
        if is_christmas_season():
            seasonal_message = "🎄 Merry Christmas! 🎅"
        elif is_halloween_season():
            seasonal_message = "🎃 Happy Halloween! 👻"
        elif is_thanksgiving_season() and is_thanksgiving_region():
            seasonal_message = "🦃 Happy Thanksgiving! 🍗"
        elif is_st_patricks_day():
            seasonal_message = "🍀 Happy St. Patrick's Day! ☘️"
        elif is_valentines_day():
            seasonal_message = "💕 Happy Valentine's Day! 💖"
        elif is_easter_season():
            seasonal_message = "🐰 Happy Easter! 🐣"
        elif is_new_years_day():
            seasonal_message = "🎊 Happy New Year! 🎉"
        elif is_independence_day() and is_us_user():
            seasonal_message = "🇺🇸 Happy Independence Day! 🎆"
        elif is_summer_solstice():
            seasonal_message = "☀️ Happy Summer Solstice! 🌞"
        else:
            seasonal_message = ""
        
        # App name - use seasonal message as title if available, otherwise use default title
        if seasonal_message:
            app_name_label = QLabel(seasonal_message)
            app_name_label.setStyleSheet("font-size: 20px; font-weight: bold; margin: 18px 10px 10px 10px; color: #FF6B35;")  # Use seasonal color
        else:
            app_name_label = QLabel("Innioasis Updater")
            app_name_label.setStyleSheet("font-size: 20px; font-weight: bold; margin: 18px 10px 10px 10px;")  # Default styling
        app_name_label.setAlignment(Qt.AlignCenter)
        about_layout.addWidget(app_name_label)
        
        # App description
        desc_label = QLabel("Official Firmware Installer created by Y1 users in collaboration with Innioasis")
        desc_label.setStyleSheet("font-size: 12px; margin: 10px;")
        desc_label.setAlignment(Qt.AlignCenter)
        desc_label.setWordWrap(True)
        about_layout.addWidget(desc_label)
        
        # Remove redundant version line - version will be shown in credits
        
        # Special thanks label
        special_thanks_label = QLabel("A special thanks to:")
        special_thanks_label.setStyleSheet("font-size: 12px; font-weight: bold; margin: 10px;")
        special_thanks_label.setAlignment(Qt.AlignCenter)
        about_layout.addWidget(special_thanks_label)
        
        # Credits section with line-by-line display and fade transitions
        credits_container = QWidget()
        credits_container.setFixedHeight(50)  # Single line height
        credits_container.setStyleSheet("""
            QWidget {
                background-color: transparent;
                border: none;
            }
        """)
        
        # Create a container for the credits label
        credits_label_container = QWidget()
        credits_label_container.setFixedHeight(50)  # Single line height
        credits_label_container.setStyleSheet("""
            QWidget {
                background-color: transparent;
                border: none;
            }
        """)
        
        credits_label = QLabel()
        credits_label.setStyleSheet("""
            font-size: 10px;
            margin: 5px;
            padding: 8px;
        """)
        credits_label.setAlignment(Qt.AlignCenter)
        credits_label.setOpenExternalLinks(True)
        credits_label.setWordWrap(False)  # Disable word wrap for horizontal scrolling
        
        # Use proper layout centering instead of manual geometry
        credits_container_layout = QVBoxLayout(credits_container)
        credits_container_layout.setContentsMargins(0, 0, 0, 0)
        credits_container_layout.setAlignment(Qt.AlignCenter)
        credits_container_layout.addWidget(credits_label)
        
        about_layout.addWidget(credits_container)
        
        # Set up line-by-line display with fade transitions
        self.setup_credits_line_display(credits_label, credits_container)
        
        # Automatic Utility Updates checkbox
        self.auto_utility_updates_checkbox = QCheckBox("Check for Updates Automatically")
        self.auto_utility_updates_checkbox.setToolTip("When checked, Innioasis Updater will automatically check for and download utility updates")
        
        # Set checkbox state based on saved preference and .no_updates file
        # Check if .no_updates file exists to determine current state
        no_updates_file = Path(".no_updates")
        if no_updates_file.exists():
            # .no_updates file exists, so automatic updates are disabled
            auto_utility_updates = False
        else:
            # .no_updates file doesn't exist, use saved preference (default to True)
            auto_utility_updates = getattr(self, 'auto_utility_updates_enabled', True)
        self.auto_utility_updates_checkbox.setChecked(auto_utility_updates)
        
        # Connect checkbox change to shortcut update (Windows only)
        if platform.system() == "Windows":
            self.auto_utility_updates_checkbox.stateChanged.connect(self.update_shortcuts_for_auto_updates)
        
        # Center the checkbox
        checkbox_layout = QHBoxLayout()
        checkbox_layout.addStretch()
        checkbox_layout.addWidget(self.auto_utility_updates_checkbox)
        checkbox_layout.addStretch()
        about_layout.addLayout(checkbox_layout)
        
        # Reddit button
        seasonal_emoji = get_seasonal_emoji_random()
        reddit_text = f"📱 r/innioasis{seasonal_emoji}" if seasonal_emoji else "📱 r/innioasis"
        reddit_btn = QPushButton(reddit_text)
        reddit_btn.setStyleSheet("""
            QPushButton {
                background-color: palette(base);
                color: palette(text);
                border: 1px solid palette(mid);
                padding: 8px 16px;
                border-radius: 3px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: palette(highlight);
                color: palette(highlighted-text);
            }
            QPushButton:pressed {
                background-color: palette(dark);
                color: palette(light);
            }
        """)
        reddit_btn.clicked.connect(self.open_reddit_link)
        
        # Center the reddit button
        reddit_layout = QHBoxLayout()
        reddit_layout.addStretch()
        reddit_layout.addWidget(reddit_btn)
        reddit_layout.addStretch()
        about_layout.addLayout(reddit_layout)
        
        # Support The Devs button
        support_btn = QPushButton("Support The Devs")
        support_btn.setStyleSheet("""
            QPushButton {
                background-color: palette(base);
                color: palette(text);
                border: 1px solid palette(mid);
                padding: 8px 16px;
                border-radius: 3px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: palette(highlight);
                color: palette(highlighted-text);
            }
            QPushButton:pressed {
                background-color: palette(dark);
                color: palette(light);
            }
        """)
        support_btn.clicked.connect(self.open_coffee_link)
        
        # Center the support button
        support_layout = QHBoxLayout()
        support_layout.addStretch()
        support_layout.addWidget(support_btn)
        support_layout.addStretch()
        about_layout.addLayout(support_layout)
        
        # Add some spacing
        about_layout.addStretch()
        
        # Add tabs to tab widget in order
        tab_widget.addTab(about_tab, "About")
        tab_widget.addTab(install_tab, "Installation")
        
        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(dialog.reject)
        button_layout.addWidget(cancel_btn)
        
        save_btn = QPushButton("Save")
        save_btn.clicked.connect(lambda: self.save_settings(dialog))
        button_layout.addWidget(save_btn)
        
        layout.addLayout(button_layout)
        
        # Set initial tab based on parameter
        if initial_tab == "about":
            tab_widget.setCurrentIndex(0)  # About tab
        elif initial_tab == "installation":
            tab_widget.setCurrentIndex(1)  # Installation tab
        elif initial_tab == "shortcuts":
            # Shortcuts t
