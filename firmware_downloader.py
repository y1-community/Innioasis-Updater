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
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QHBoxLayout,
                               QWidget, QListWidget, QListWidgetItem, QPushButton, QTextEdit,
                               QLabel, QComboBox, QProgressBar, QMessageBox,
                               QGroupBox, QSplitter, QStackedWidget, QCheckBox, QProgressDialog,
                               QFileDialog)
from PySide6.QtCore import QThread, Signal, Qt, QSize, QTimer
from PySide6.QtGui import QFont, QPixmap
import platform
import time
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

# Zip file management
ZIP_STORAGE_DIR = Path("firmware_downloads")
EXTRACTED_FILES_LOG = Path("extracted_files.log")

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
    # Completely silent - no output to terminal
    pass

def toggle_silent_mode():
    """Toggle silent mode on/off"""
    global SILENT_MODE
    SILENT_MODE = not SILENT_MODE
    # Only output when explicitly toggling to verbose mode
    if not SILENT_MODE:
        print("Verbose mode enabled - press Ctrl+D again to disable")
    return SILENT_MODE

def cleanup_extracted_files():
    """Clean up extracted files at startup"""
    if EXTRACTED_FILES_LOG.exists():
        try:
            with open(EXTRACTED_FILES_LOG, 'r') as f:
                files_to_clean = [line.strip() for line in f.readlines() if line.strip()]

            for file_path in files_to_clean:
                path = Path(file_path)
                if path.exists():
                    path.unlink()
                    silent_print(f"Cleaned up: {file_path}")

            # Remove the log file
            EXTRACTED_FILES_LOG.unlink()
            silent_print("Cleaned up extracted files log")
        except Exception as e:
            silent_print(f"Error cleaning up extracted files: {e}")

def log_extracted_files(files):
    """Log extracted files for cleanup"""
    try:
        with open(EXTRACTED_FILES_LOG, 'w') as f:
            for file_path in files:
                f.write(f"{file_path}\n")
    except Exception as e:
        silent_print(f"Error logging extracted files: {e}")

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


class ConfigDownloader:
    """Downloads and parses configuration files from GitHub with caching"""

    def __init__(self):
        self.config_url = "https://raw.githubusercontent.com/team-slide/Y1-helper/refs/heads/master/config.ini"
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

    def download_manifest(self):
        """Download and parse the XML manifest file with caching"""
        # Try cache first
        cached_packages = load_cache(MANIFEST_CACHE_FILE)
        if cached_packages:
            return cached_packages

        try:
            response = self.session.get(self.manifest_url, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()

            root = ET.fromstring(response.text)
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

            silent_print(f"Successfully loaded {len(packages)} packages from manifest")
            # Cache the packages
            save_cache(MANIFEST_CACHE_FILE, packages)
            return packages
        except Exception as e:
            silent_print(f"Error downloading manifest: {e}")
            return []


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

    def get_latest_release(self, repo):
        """Get the latest release information for a repository with fallback"""
        url = f"https://api.github.com/repos/{repo}/releases/latest"

        # Try with authenticated token first (since unauthenticated is failing)
        token = self.get_next_token()
        if token:
            headers = {
                'Authorization': f'token {token}',
                'Accept': 'application/vnd.github.v3+json'
            }

            try:
                response = self.session.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
                if response.status_code == 200:
                    release_data = response.json()
                    assets = release_data.get('assets', [])

                    # Find any zip asset (more flexible than just rom.zip)
                    zip_asset = None
                    for asset in assets:
                        if asset['name'].lower().endswith('.zip'):
                            zip_asset = asset
                            break

                    return {
                        'tag_name': release_data.get('tag_name', ''),
                        'name': release_data.get('name', ''),
                        'body': release_data.get('body', ''),
                        'download_url': zip_asset['browser_download_url'] if zip_asset else None,
                        'asset_name': zip_asset['name'] if zip_asset else None
                    }
                elif response.status_code == 401:
                    silent_print(f"Token authentication failed for {repo} - trying unauthenticated...")
                elif response.status_code == 403:
                    silent_print(f"Rate limited for {repo}, trying unauthenticated...")
                else:
                    silent_print(f"Error getting release for {repo}: {response.status_code}")
            except Exception as e:
                silent_print(f"Error getting release for {repo} with token: {e}")

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

                # Find any zip asset (more flexible than just rom.zip)
                zip_asset = None
                for asset in assets:
                    if asset['name'].lower().endswith('.zip'):
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

        # Try with authenticated token first
        token = self.get_next_token()
        if token:
            headers = {
                'Authorization': f'token {token}',
                'Accept': 'application/vnd.github.v3+json'
            }

            try:
                silent_print(f"Attempting authenticated request to {url} with token: {token[:10]}...")
                response = self.session.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
                silent_print(f"Authenticated response status: {response.status_code}")

                if response.status_code == 200:
                    releases_data = response.json()
                    silent_print(f"Found {len(releases_data)} total releases for {repo}")
                    releases = []

                    for release in releases_data:
                        assets = release.get('assets', [])
                        silent_print(f"Release {release.get('tag_name', 'Unknown')} has {len(assets)} assets")

                        # Find any zip asset (more flexible than just rom.zip)
                        zip_asset = None
                        for asset in assets:
                            if asset['name'].lower().endswith('.zip'):
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
                elif response.status_code == 401:
                    silent_print(f"Token authentication failed for {repo} - trying unauthenticated...")
                elif response.status_code == 403:
                    silent_print(f"Rate limited for {repo}, trying unauthenticated...")
                else:
                    silent_print(f"Error getting releases for {repo}: {response.status_code}")
            except Exception as e:
                silent_print(f"Error getting releases for {repo} with token: {e}")

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
                            if asset['name'].lower().endswith('.zip'):
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
                        if asset['name'].lower().endswith('.zip'):
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





class MTKWorker(QThread):
    """Worker thread for running MTK command with real-time output"""

    status_updated = Signal(str)
    show_installing_image = Signal()
    show_reconnect_image = Signal()
    show_presteps_image = Signal()
    mtk_completed = Signal(bool, str)
    handshake_failed = Signal()  # New signal for handshake failures
    errno2_detected = Signal()   # New signal for errno2 errors
    backend_error_detected = Signal()  # New signal for backend errors
    keyboard_interrupt_detected = Signal()  # New signal for keyboard interrupts
    disable_update_button = Signal()  # Signal to disable update button during MTK installation
    enable_update_button = Signal()   # Signal to enable update button when returning to ready state

    def __init__(self):
        super().__init__()
        self.should_stop = False

    def stop(self):
        """Stop the MTK worker"""
        self.should_stop = True

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

            device_detected = False
            flashing_started = False
            handshake_error_detected = False
            errno2_error_detected = False
            backend_error_detected = False
            keyboard_interrupt_detected = False
            usb_connection_issue_detected = False
            last_output_line = ""
            successful_completion = False

            # Interruption detection variables
            progress_detected = False
            last_progress_time = None
            interruption_timeout = 3.0  # 3 seconds timeout

            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    line = output.strip()
                    last_output_line = line  # Track the last output line

                    # Show latest output in status area (no extra whitespace)
                    self.status_updated.emit(f"MTK: {line}")

                    # Check for errno2 error
                    if "errno2" in line.lower():
                        errno2_error_detected = True
                        self.status_updated.emit("Errno2 detected - Innioasis Updater reinstall required")
                        self.errno2_detected.emit()
                        # Don't break here - continue reading output

                    # Check for handshake failed error
                    if "handshake failed" in line.lower():
                        handshake_error_detected = True
                        self.status_updated.emit("Handshake failed detected - driver issue likely")
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

                    if ".Port - Device detected :)" in line:
                        device_detected = True
                        # Switch to installing.png immediately when device is detected
                        self.show_installing_image.emit()

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

                    # Only show presteps if no device detected and no errors
                    if not device_detected and not usb_connection_issue_detected and not handshake_error_detected and not errno2_error_detected and not backend_error_detected and not keyboard_interrupt_detected:
                        self.show_presteps_image.emit()

            # If any error was detected, continue reading but mark for completion
            if handshake_error_detected or errno2_error_detected or backend_error_detected or keyboard_interrupt_detected:
                # Continue reading output to show user what's happening
                while True:
                    output = process.stdout.readline()
                    if output == '' and process.poll() is not None:
                        break
                    if output:
                        line = output.strip()
                        # Show latest output in status area (no extra whitespace)
                        self.status_updated.emit(f"MTK: {line}")

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
                        successful_completion = False
                    else:
                        # Check if the last progress was 100% or if process completed normally
                        if "100%" in last_output_line or process.returncode == 0:
                            successful_completion = True
                        else:
                            # Process stopped before 100% - likely interrupted
                            successful_completion = False
                else:
                    # No progress was detected, check if process completed successfully
                    if process.returncode == 0:
                        successful_completion = True
                    else:
                        successful_completion = False

        except Exception as e:
            self.status_updated.emit(f"MTK error: {str(e)}")
            successful_completion = False

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

            success_msg += "\nTo flash these files to your device:\n"
            success_msg += "1. Turn off your Y1\n"
            success_msg += "2. Run the following command in a new terminal:\n"
            success_msg += f"   {sys.executable} mtk.py w uboot,bootimg,recovery,android,usrdata lk.bin,boot.img,recovery.img,system.img,userdata.img\n"
            success_msg += "3. Follow the on-screen prompts to turn off your Y1"

            self.download_completed.emit(True, success_msg)

        except Exception as e:
            self.download_completed.emit(False, f"Error: {str(e)}")


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

        # Clean up any previously extracted files at startup
        cleanup_extracted_files()

        # Initialize UI first for immediate responsiveness
        self.init_ui()

        # Check for SP Flash Tool on Windows before loading data
        if platform.system() == "Windows":
            self.check_sp_flash_tool()

        # Load data asynchronously to avoid blocking UI
        QTimer.singleShot(100, self.load_data)

        # Set up theme change detection timer
        self.theme_check_timer = QTimer()
        self.theme_check_timer.timeout.connect(self.check_theme_change)
        self.theme_check_timer.start(1000)  # Check every second
        self.last_theme_state = self.is_dark_mode()

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
                
        except subprocess.TimeoutExpired:
            # If tasklist times out, assume no conflict and continue
            pass
        except Exception as e:
            # If there's any error checking for the process, continue silently
            silent_print(f"Error checking for flash tools: {e}")

    def keyPressEvent(self, event):
        """Handle key press events"""
        # Control+D to toggle silent mode
        if event.key() == Qt.Key_D and event.modifiers() == Qt.ControlModifier:
            silent_mode = toggle_silent_mode()
            if silent_mode:
                self.status_label.setText("Silent mode enabled - press Ctrl+D to disable")
            else:
                self.status_label.setText("Verbose mode enabled - press Ctrl+D to enable silent mode")
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
        self.setWindowTitle("Innioasis Y1 Updater by Ryan Specter - u/respectyarn")
        self.setGeometry(100, 100, 960, 495)



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
                border: 1px solid #0066CC;
                border-radius: 8px;
                background-color: transparent;
                min-width: 20px;
                max-width: 20px;
                padding: 2px;
            }
            QPushButton:hover {
                background-color: #0066CC;
                color: white;
            }
        """)
        help_btn.setCursor(Qt.PointingHandCursor)
        help_btn.setToolTip("Try Type A System Software first. If your scroll wheel doesn't respond after installation, install one of the Type B options.")
        help_btn.clicked.connect(self.show_device_type_help)
        device_type_layout.addWidget(help_btn)
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
        self.firmware_combo.addItem("All Software", "")
        # Default selection will be set dynamically in populate_firmware_combo
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
        package_group = QGroupBox("Available Software")
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
        self.download_btn = QPushButton("Download")
        self.download_btn.clicked.connect(self.start_download)
        self.download_btn.setEnabled(False)
        left_layout.addWidget(self.download_btn)



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
            mediatek_driver_file = Path("C:/Program Files/MediaTek/SP Driver/unins000.exe")
            usbdk_driver_file = Path("C:/Program Files/UsbDk Runtime Library/UsbDk.sys")

            # Only show the button if one of the driver files is missing
            if not mediatek_driver_file.exists() or not usbdk_driver_file.exists():
                driver_btn = QPushButton("🔧 Driver Setup")
                driver_btn.setStyleSheet("""
                    QPushButton {
                        background-color: #0066CC;
                        color: white;
                        border: none;
                        padding: 8px 16px;
                        border-radius: 20px;
                        font-weight: bold;
                        font-size: 12px;
                    }
                    QPushButton:hover {
                        background-color: #0052A3;
                    }
                    QPushButton:pressed {
                        background-color: #003D7A;
                    }
                """)
                driver_btn.clicked.connect(self.open_driver_setup_link)
                coffee_layout.addWidget(driver_btn)
            else:
                # Show "Install from .zip" button when drivers are already installed
                install_zip_btn = QPushButton("📦 Install from .zip")
                install_zip_btn.setStyleSheet("""
                    QPushButton {
                        background-color: #28A745;
                        color: white;
                        border: none;
                        padding: 8px 16px;
                        border-radius: 20px;
                        font-weight: bold;
                        font-size: 12px;
                    }
                    QPushButton:hover {
                        background-color: #218838;
                    }
                    QPushButton:pressed {
                        background-color: #1E7E34;
                    }
                """)
                install_zip_btn.clicked.connect(self.install_from_zip)
                coffee_layout.addWidget(install_zip_btn)
        else:
            # On non-Windows systems, show "Install from .zip" button
            install_zip_btn = QPushButton("📦 Install from .zip")
            install_zip_btn.setStyleSheet("""
                QPushButton {
                    background-color: #28A745;
                    color: white;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 20px;
                    font-weight: bold;
                    font-size: 12px;
                }
                QPushButton:hover {
                    background-color: #218838;
                }
                QPushButton:pressed {
                    background-color: #1E7E34;
                }
            """)
            install_zip_btn.clicked.connect(self.install_from_zip)
            coffee_layout.addWidget(install_zip_btn)

        # Reddit button
        reddit_btn = QPushButton("📱 r/innioasis")
        reddit_btn.setStyleSheet("""
            QPushButton {
                background-color: #FF4500;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 20px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #E63939;
            }
            QPushButton:pressed {
                background-color: #CC3300;
            }
        """)
        reddit_btn.clicked.connect(self.open_reddit_link)
        coffee_layout.addWidget(reddit_btn)

        # Discord button
        discord_btn = QPushButton("💬 Discord")
        discord_btn.setStyleSheet("""
            QPushButton {
                background-color: #5865F2;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 20px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #4752C4;
            }
            QPushButton:pressed {
                background-color: #3C45A5;
            }
        """)
        discord_btn.clicked.connect(self.open_discord_link)
        coffee_layout.addWidget(discord_btn)

        # Buy Us Coffee button (renamed from Buy Me Coffee)
        coffee_btn = QPushButton("☕ Buy Us Coffee")
        coffee_btn.setStyleSheet("""
            QPushButton {
                background-color: #FF5E5B;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 20px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #FF4441;
            }
            QPushButton:pressed {
                background-color: #E63939;
            }
        """)
        coffee_btn.clicked.connect(self.open_coffee_link)
        coffee_layout.addWidget(coffee_btn)

        right_layout.addLayout(coffee_layout)

        # App Update button (below social media buttons)
        update_layout = QHBoxLayout()
        update_layout.addStretch()  # Push button to the right

        self.update_btn_right = QPushButton("Check for Utility Updates")
        self.update_btn_right.setEnabled(True)  # Enable immediately
        self.update_btn_right.clicked.connect(self.launch_updater_script)
        self.update_btn_right.setToolTip("Downloads and installs the latest version of the Innioasis Updater")
        update_layout.addWidget(self.update_btn_right)
        right_layout.addLayout(update_layout)

        # Status group
        status_group = QGroupBox("Status")
        status_layout = QVBoxLayout(status_group)

        self.status_label = QLabel("Ready")
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
                border-radius: 5px;
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
        splitter.setSizes([360, 600])  # Adjusted for 960px total width

    def load_data(self):
        """Load configuration and manifest data with improved performance"""
        self.status_label.setText("Loading configuration...")
        silent_print("Loading configuration and manifest data...")

        # Clear cache at startup to ensure fresh tokens are fetched
        clear_cache()
        silent_print("Cleared cache at startup to fetch fresh tokens")

        # Download tokens
        tokens = self.config_downloader.download_config()
        if not tokens:
            silent_print("ERROR: Failed to download API tokens")
            self.status_label.setText("No API tokens available")
            return

        self.github_api = GitHubAPI(tokens)
        silent_print(f"Loaded {len(tokens)} API tokens")

        # Start parallel token validation for faster startup
        if tokens:
            silent_print(f"Loaded {len(tokens)} API tokens")
            self.status_label.setText("Validating API tokens...")
            # Start parallel token validation
            self.validate_tokens_parallel(tokens)
        else:
            silent_print("No tokens loaded")
            self.status_label.setText("No API tokens available")

        # Manifest loading is now handled asynchronously in validate_tokens_parallel
        # The UI will be populated once a working token is found or fallback occurs

    def validate_tokens_parallel(self, tokens):
        """Validate tokens in parallel for faster startup"""
        if not tokens:
            silent_print("No tokens to validate, using unauthenticated mode")
            self.status_label.setText("Using unauthenticated mode")
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
                    self.status_label.setText(f"Authenticated as {username}")

                    # Cancel remaining tasks
                    for remaining_future in future_to_token:
                        if not remaining_future.done():
                            remaining_future.cancel()

                    # Mark token as working and proceed
                    self.github_api.mark_token_working(token)
                    self.finish_data_loading([token])
                    return

        # If we get here, no tokens worked
        silent_print("All tokens failed validation, using unauthenticated mode")
        self.status_label.setText("Using unauthenticated mode")
        # Try with at least one token anyway, in case validation was too strict
        if tokens:
            silent_print("Attempting to use first token despite validation failure")
            # Check if token already has prefix to avoid double-prefixing
            first_token = tokens[0]
            if not first_token.startswith('github_pat_'):
                first_token = f"github_pat_{first_token}"
            self.github_api = GitHubAPI([first_token])
            self.finish_data_loading([tokens[0]])
        else:
            self.finish_data_loading([])

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

        # Download manifest
        self.packages = self.config_downloader.download_manifest()
        if not self.packages:
            silent_print("ERROR: Failed to download software manifest")
            self.status_label.setText("Error: Failed to download software manifest")
            return

        silent_print(f"Loaded {len(self.packages)} software packages")
        self.status_label.setText("Ready: Select a firmware to Download. Your music will stay safe.")

        # Populate UI components
        self.populate_device_type_combo()
        self.populate_device_model_combo()
        self.populate_firmware_combo()

        # Apply initial filters
        self.filter_firmware_options()

        # Use a timer to ensure the default selection is properly applied
        QTimer.singleShot(100, self.apply_initial_release_display)



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
        msg_box.exec_()



    def populate_device_type_combo(self):
        """Dynamically populate device type combo from manifest data"""
        self.device_type_combo.clear()
        self.device_type_combo.addItem("All Types", "")

        # Get unique device types from packages
        device_types = set()
        for package in self.packages:
            device_type = package.get('device_type', '')
            if device_type:
                device_types.add(device_type)

        # Add device types to combo (sorted)
        for device_type in sorted(device_types):
            self.device_type_combo.addItem(f"Type {device_type}", device_type)

        # Set default to first available type if any exist
        if len(device_types) > 0:
            first_type = sorted(device_types)[0]
            self.device_type_combo.setCurrentText(f"Type {first_type}")

    def populate_device_model_combo(self):
        """Dynamically populate device model combo from manifest data"""
        self.device_model_combo.clear()
        self.device_model_combo.addItem("All Models", "")

        # Get unique device models from packages
        device_models = set()
        for package in self.packages:
            device_model = package.get('device', '')
            if device_model:
                device_models.add(device_model)

        # Add device models to combo (sorted)
        for device_model in sorted(device_models):
            self.device_model_combo.addItem(device_model, device_model)

        # Set default to first available model if any exist
        if len(device_models) > 0:
            first_model = sorted(device_models)[0]
            self.device_model_combo.setCurrentText(first_model)

    def populate_firmware_combo(self):
        """Populate the software dropdown with package names from manifest"""
        self.firmware_combo.clear()
        self.firmware_combo.addItem("All Software", "")

        # Get current filter selections
        selected_type = self.device_type_combo.currentData()
        selected_model = self.device_model_combo.currentData()

        # Get filtered software names from packages
        software_options = []
        for package in self.packages:
            name = package.get('name', '')
            repo = package.get('repo', '')
            device_type = package.get('device_type', '')
            device_model = package.get('device', '')

            # Check device type filter
            type_match = not selected_type or device_type == selected_type

            # Check device model filter
            model_match = not selected_model or device_model == selected_model

            if name and repo and type_match and model_match:
                software_options.append((name, repo))

        # Add filtered software options to dropdown (sorted by name)
        for name, repo in sorted(software_options, key=lambda x: x[0]):
            self.firmware_combo.addItem(name, repo)

        # Set default selection to software containing "Original" if available
        default_index = 0  # Default to "All Software"
        for i in range(1, self.firmware_combo.count()):  # Skip "All Software" at index 0
            if "original" in self.firmware_combo.itemText(i).lower():
                default_index = i
                break

        self.firmware_combo.setCurrentIndex(default_index)

    def on_firmware_changed(self):
        """Handle software selection change"""
        selected_repo = self.firmware_combo.currentData()

        if selected_repo:
            # Update package list to show releases for selected software
            self.populate_releases_list()
        else:
            # "All Software" is selected - show releases from all available software
            self.populate_all_releases_list()



    def populate_releases_list(self):
        """Populate the releases list for the selected software"""
        self.package_list.clear()

        # Add loading placeholder
        loading_item = QListWidgetItem("Loading releases...")
        loading_item.setFlags(loading_item.flags() & ~Qt.ItemIsSelectable)
        self.package_list.addItem(loading_item)
        # Don't update status label - keep it as "Ready" for firmware installation status only

        selected_repo = self.firmware_combo.currentData()
        if not selected_repo:
            self.package_list.clear()
            self.package_list.addItem("Please select a software type")
            return

        # Set up timeout timer
        timeout_timer = QTimer()
        timeout_timer.setSingleShot(True)
        timeout_timer.timeout.connect(lambda: self.handle_releases_timeout())
        timeout_timer.start(60000)  # 1 minute timeout

        # Get releases for the selected repository
        try:
            silent_print(f"Attempting to load releases for {selected_repo}")
            releases = self.github_api.get_all_releases(selected_repo)
            timeout_timer.stop()  # Stop timeout if successful
            silent_print(f"Successfully loaded {len(releases) if releases else 0} releases")
        except Exception as e:
            timeout_timer.stop()
            silent_print(f"Error loading releases: {e}")
            self.package_list.clear()
            self.package_list.addItem("Unable To Load Releases")
            # Don't update status label - keep it as "Ready" for firmware installation status only
            return

        # Remove loading placeholder
        self.package_list.clear()

        if not releases:
            self.package_list.addItem(f"No releases found for {selected_repo}")
            return

        # Add releases to the list with detailed information
        for release in releases:
            # Find the package info for this release to get software name from manifest
            package_info = None
            for package in self.packages:
                if package.get('repo') == selected_repo:
                    package_info = package
                    break

            # Get software name from manifest, fallback to repo name
            software_name = package_info.get('name', selected_repo) if package_info else selected_repo

            # Detailed display format
            display_text = f"{software_name}\n"
            display_text += f"Version: {release['tag_name']}\n"

            if release.get('published_at'):
                # Format the date
                try:
                    from datetime import datetime
                    date_obj = datetime.fromisoformat(release['published_at'].replace('Z', '+00:00'))
                    display_text += f"Published: {date_obj.strftime('%Y-%m-%d %H:%M')}\n"
                except:
                    display_text += f"Published: {release['published_at']}\n"

            # Add software name to release info for button text logic
            release_with_software = release.copy()
            release_with_software['software_name'] = software_name

            item = QListWidgetItem(display_text)
            item.setData(Qt.UserRole, release_with_software)
            self.package_list.addItem(item)

        # Select the first item if available
        if self.package_list.count() > 0:
            self.package_list.setCurrentRow(0)
            first_item = self.package_list.item(0)
            if first_item:
                self.on_release_selected(first_item)

        # Keep status as Ready - don't change it for release loading
        silent_print("Releases loaded successfully")

    def handle_releases_timeout(self):
        """Handle timeout when loading releases"""
        self.package_list.clear()
        self.package_list.addItem("Unable To Load Releases")
        # Don't update status label - keep it as "Ready" for firmware installation status only
        silent_print("Timeout loading releases")

    def populate_all_releases_list(self):
        """Populate the package list with releases from all available software"""
        self.package_list.clear()

        # Get all software options that match current filters
        selected_type = self.device_type_combo.currentData()
        selected_model = self.device_model_combo.currentData()

        all_releases = []
        failed_repos = []

        for package in self.packages:
            name = package.get('name', '')
            repo = package.get('repo', '')
            device_type = package.get('device_type', '')
            device_model = package.get('device', '')

            # Check device type filter
            type_match = not selected_type or device_type == selected_type

            # Check device model filter
            model_match = not selected_model or device_model == selected_model

            if name and repo and type_match and model_match:
                # Get releases for this software with retry
                releases = self.github_api.retry_with_delay(self.github_api.get_all_releases, repo)
                if releases and len(releases) > 0:
                    for release in releases:
                        # Add software name to the release info for identification
                        release_with_software = release.copy()
                        release_with_software['software_name'] = name
                        all_releases.append(release_with_software)
                else:
                    failed_repos.append(repo)

        # Sort releases by software name (alphabetical), then by date (newest first within each software)
        # Use a custom sorting key that sorts alphabetically by software name, then by date (newest first)
        def sort_key(release):
            software_name = release.get('software_name', '')
            published_at = release.get('published_at', '')
            # Convert date string to a comparable format for sorting (newest first)
            try:
                from datetime import datetime
                date_obj = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
                timestamp = date_obj.timestamp()
            except:
                timestamp = 0
            # Return a tuple: (software_name, -timestamp) where negative timestamp ensures newest first
            return (software_name, -timestamp)

        all_releases.sort(key=sort_key)

        # Show error message if no releases were found
        if not all_releases and failed_repos:
            # Don't update status label - keep it as "Ready" for firmware installation status only
            silent_print(f"Failed to load releases from repositories: {failed_repos}")
            
            # Add helpful message to the list
            help_item = QListWidgetItem("⚠️ No releases found\n\nThis could be due to:\n• GitHub API rate limiting\n• Network connectivity issues\n• Repository access restrictions\n\nTry using 'Install from .zip' button instead")
            help_item.setFlags(help_item.flags() & ~Qt.ItemIsSelectable)  # Make it non-selectable
            help_item.setData(Qt.UserRole, None)  # No release data
            self.package_list.addItem(help_item)
            
            # Also update status to be more helpful
            self.status_label.setText("GitHub API unavailable - use 'Install from .zip' button")
        elif all_releases:
            # Don't update status label - keep it as "Ready" for firmware installation status only
            silent_print(f"Loaded {len(all_releases)} releases successfully")

        for release in all_releases:
            # Find the package info for this release to get device type and model
            package_info = None
            for package in self.packages:
                if package.get('name') == release['software_name']:
                    package_info = package
                    break

            # Simplified display format
            display_text = f"{release['software_name']}\n"
            display_text += f"Version: {release['tag_name']}\n"

            if release.get('published_at'):
                # Format the date
                try:
                    from datetime import datetime
                    date_obj = datetime.fromisoformat(release['published_at'].replace('Z', '+00:00'))
                    display_text += f"Published: {date_obj.strftime('%Y-%m-%d %H:%M')}\n"
                except:
                    display_text += f"Published: {release['published_at']}\n"

            # Show device type if "All Types" is selected
            if not self.device_type_combo.currentData() and package_info:
                device_type = package_info.get('device_type', '')
                if device_type:
                    display_text += f"Type: {device_type}\n"

            # Show device model if "All Models" is selected
            if not self.device_model_combo.currentData() and package_info:
                device_model = package_info.get('device', '')
                if device_model:
                    display_text += f"Model: {device_model}\n"

            item = QListWidgetItem(display_text)
            item.setData(Qt.UserRole, release)
            self.package_list.addItem(item)

        # Automatically select the first item for improved discoverability
        if self.package_list.count() > 0:
            self.package_list.setCurrentRow(0)
            self.package_list.setFocus()  # Give focus to the list for blue highlight
            self.download_btn.setEnabled(True)
            # Update button text for the first selected item
            first_item = self.package_list.item(0)
            self.update_download_button_text(first_item)

    def show_context_menu(self, position):
        """Show context menu for right-click on firmware items"""
        item = self.package_list.itemAt(position)
        if item is None:
            return

        # Get the firmware data from the item
        firmware_data = item.data(Qt.UserRole)
        if firmware_data is None:
            return

        from PySide6.QtWidgets import QMenu

        context_menu = QMenu(self)
        delete_action = context_menu.addAction("Delete Local Zip File")

        action = context_menu.exec_(self.package_list.mapToGlobal(position))

        if action == delete_action:
            # Extract repo_name and version from the firmware data
            repo_name = firmware_data.get('repo_name', '')
            version = firmware_data.get('version', '')

            if repo_name and version:
                if delete_zip_file(repo_name, version):
                    QMessageBox.information(self, "Success", f"Deleted zip file for {repo_name} version {version}")
                else:
                    QMessageBox.information(self, "Info", f"No local zip file found for {repo_name} version {version}")

    def populate_all_releases_list_progressive(self):
        """Populate the releases list progressively for all software"""
        self.package_list.clear()

        # Add loading placeholder
        loading_item = QListWidgetItem("Loading firmware listings...")
        loading_item.setFlags(loading_item.flags() & ~Qt.ItemIsSelectable)
        self.package_list.addItem(loading_item)

        # Get all releases progressively
        all_releases = []

        for package in self.packages:
            repo = package.get('repo')
            if not repo:
                continue

            try:
                releases = self.github_api.get_all_releases(repo)
                if releases:
                    # Add software name to each release for consistent button text logic
                    for release in releases:
                        release_with_software = release.copy()
                        release_with_software['software_name'] = package.get('name', repo)
                        all_releases.append(release_with_software)

                    # Update status less frequently to reduce UI updates
                    if len(all_releases) % 5 == 0:
                        # Don't update status label - keep it as "Ready" for firmware installation status only
                        silent_print(f"Loaded {len(all_releases)} releases...")

            except Exception as e:
                silent_print(f"Error getting releases for {repo}: {e}")
                continue

        # Remove loading placeholder and show results
        self.package_list.clear()

        if not all_releases:
            self.package_list.addItem("No releases found. Please check your internet connection.")
            return

        # Sort releases by date (newest first)
        all_releases.sort(key=lambda x: x.get('published_at', ''), reverse=True)

        # Add releases to the list
        for release in all_releases:
            software_name = release.get('software_name', 'Unknown')
            display_text = f"{software_name} - {release['tag_name']}"

            item = QListWidgetItem(display_text)
            item.setData(Qt.UserRole, release)
            self.package_list.addItem(item)

        # Select the first item if available
        if self.package_list.count() > 0:
            self.package_list.setCurrentRow(0)
            first_item = self.package_list.item(0)
            if first_item:
                self.on_release_selected(first_item)

    def update_download_button_text(self, item):
        """Update download button text based on selected item"""
        if item and item.data(Qt.UserRole):
            release_info = item.data(Qt.UserRole)

            # Check if software name contains "Original"
            software_name = release_info.get('software_name', '')
            if 'original' in software_name.lower():
                self.download_btn.setText("Download (Update / Restore)")
            else:
                self.download_btn.setText("Download")
        else:
            self.download_btn.setText("Download")

    def on_release_selected(self, item):
        """Handle release selection from the list"""
        self.download_btn.setEnabled(True)
        self.update_download_button_text(item)

    def run_mtk_command(self):
        """Run the MTK flash command with image display"""
        # Check if required files exist
        required_files = ["lk.bin", "boot.img", "recovery.img", "system.img", "userdata.img"]
        missing_files = []
        for file in required_files:
            if not Path(file).exists():
                missing_files.append(file)

        if missing_files:
            QMessageBox.warning(self, "Error", f"Missing required files: {', '.join(missing_files)}")
            return

        # Confirm with user
        reply = QMessageBox.question(
            self,
            "Get Ready",
            "Please make sure your Y1 is NOT plugged in and press OK, then follow the next instructions.",
            QMessageBox.Ok | QMessageBox.Cancel,
            QMessageBox.Cancel
        )

        if reply == QMessageBox.Cancel:
            return

        # Load and display the init steps image
        self.load_initsteps_image()

        # Start MTK worker
        self.mtk_worker = MTKWorker()
        self.mtk_worker.status_updated.connect(self.status_label.setText)
        self.mtk_worker.show_installing_image.connect(self.load_installing_image)
        self.mtk_worker.mtk_completed.connect(self.on_mtk_completed)
        self.mtk_worker.handshake_failed.connect(self.on_handshake_failed)
        self.mtk_worker.errno2_detected.connect(self.on_errno2_detected)
        self.mtk_worker.backend_error_detected.connect(self.on_backend_error_detected)
        self.mtk_worker.keyboard_interrupt_detected.connect(self.on_keyboard_interrupt_detected)
        self.mtk_worker.disable_update_button.connect(self.disable_update_button)
        self.mtk_worker.enable_update_button.connect(self.enable_update_button)

        self.mtk_worker.start()

        # Disable download button during MTK operation
        self.download_btn.setEnabled(False)

    def on_mtk_completed(self, success, message):
        """Handle MTK command completion"""
        # Stop the MTK worker to prevent it from continuing to run
        if self.mtk_worker:
            self.mtk_worker.stop()
            self.mtk_worker.wait()  # Wait for the worker to finish
            self.mtk_worker = None

        if success:
            self.status_label.setText("Install completed successfully")
            # Load and display installed.png for 30 seconds
            self.load_installed_image()

            # Cancel any existing revert timer to prevent conflicts
            if hasattr(self, '_revert_timer') and self._revert_timer:
                self._revert_timer.stop()
                self._revert_timer = None

            # Set timer to revert to startup state after 30 seconds
            self._revert_timer = QTimer()
            self._revert_timer.timeout.connect(self.revert_to_startup_state)
            self._revert_timer.setSingleShot(True)
            self._revert_timer.start(30000)
        else:
            self.status_label.setText(f"MTK command failed: {message}")
            # On Windows: First show process_ended.png image briefly, then show install error dialog
            self.load_process_ended_image()
            
            # Use a timer to show the dialog after a short delay so user sees the process_ended image
            QTimer.singleShot(2000, self.show_install_error_dialog)
            return  # Don't continue with the revert timer since user will choose action

        # Re-enable download button
        self.download_btn.setEnabled(True)

    def disable_update_button(self):
        """Disable the update button during MTK installation"""
        if hasattr(self, 'update_btn_right'):
            self.update_btn_right.setEnabled(False)
            self.update_btn_right.setText("Check for Utility Updates")

    def enable_update_button(self):
        """Enable the update button when returning to ready state"""
        if hasattr(self, 'update_btn_right'):
            self.update_btn_right.setEnabled(True)
            self.update_btn_right.setText("Check for Utility Updates")

    def on_handshake_failed(self):
        """Handle handshake failed error from MTKWorker"""
        # Stop the MTK worker to prevent it from continuing to run
        if self.mtk_worker:
            self.mtk_worker.stop()
            self.mtk_worker.wait()  # Wait for the worker to finish
            self.mtk_worker = None

        # Load and display the appropriate handshake error image for 50 seconds
        self.load_handshake_error_image()

        # Cancel any existing revert timer to prevent conflicts
        if hasattr(self, '_revert_timer') and self._revert_timer:
            self._revert_timer.stop()
            self._revert_timer = None

        # Set timer to revert to startup state after 50 seconds
        self._revert_timer = QTimer()
        self._revert_timer.timeout.connect(self.revert_to_startup_state)
        self._revert_timer.setSingleShot(True)
        self._revert_timer.start(50000)

        if platform.system() == "Windows":
            # Check if specific driver files exist
            mediatek_driver_file = Path("C:/Program Files/MediaTek/SP Driver/unins000.exe")
            usbdk_driver_file = Path("C:/Program Files/UsbDk Runtime Library/UsbDk.sys")

            if not mediatek_driver_file.exists() or not usbdk_driver_file.exists():
                # Show popup with driver setup instructions for Windows users
                reply = self.show_custom_message_box(
                    "critical",
                    "Handshake Failed - Driver Issue Detected",
                    "The MTK handshake failed, which usually indicates a driver problem.\n\n"
                    "Please check your drivers, reboot your PC, and try again.\n\n"
                    "Click OK to open the driver installation guide.",
                    QMessageBox.Ok,
                    QMessageBox.Ok
                )

                if reply == QMessageBox.Ok:
                    # Launch the driver setup URL
                    import webbrowser
                    webbrowser.open("https://www.github.com/team-slide/Innioasis-Updater#windows-64bit-intelamd-only")
            else:
                self.status_label.setText("Handshake failed. Drivers seem to be installed. Please check USB connection and reboot.")
        else:
            # No dialog for Mac users - just update status
            self.status_label.setText("Handshake failed - please check USB connection and try again")

        self.download_btn.setEnabled(True)  # Re-enable download button

    def on_errno2_detected(self):
        """Handle errno2 error from MTKWorker"""
        # Stop the MTK worker to prevent it from continuing to run
        if self.mtk_worker:
            self.mtk_worker.stop()
            self.mtk_worker.wait()  # Wait for the worker to finish
            self.mtk_worker = None

        reply = self.show_custom_message_box(
            "question",
            "Errno2 Error - Reinstall Required",
            "An errno2 error was detected, which indicates the Innioasis Updater application needs to be reinstalled.\n\n"
            "Please reinstall the Innioasis Updater application to resolve this issue.\n\n"
            "Click OK to open the download page in your browser.",
            QMessageBox.Ok | QMessageBox.Cancel,
            QMessageBox.Ok
        )

        if reply == QMessageBox.Ok:
            # Open the GitHub releases page in the default browser
            import webbrowser
            releases_url = "https://github.com/team-slide/Innioasis-Updater/releases/latest"
            webbrowser.open(releases_url)
            self.status_label.setText("GitHub releases page opened - please reinstall Innioasis Updater")
        else:
            self.status_label.setText("Errno2 error - please reinstall Innioasis Updater")

        self.download_btn.setEnabled(True)  # Re-enable download button

    def on_backend_error_detected(self):
        """Handle backend error from MTKWorker"""
        # Stop the MTK worker to prevent it from continuing to run
        if self.mtk_worker:
            self.mtk_worker.stop()
            self.mtk_worker.wait()  # Wait for the worker to finish
            self.mtk_worker = None

        reply = QMessageBox.question(
            self,
            "Backend Error - libusb Backend Issue",
            "A libusb backend error was detected, which indicates a system-level USB backend issue.\n\n"
            "This is typically caused by:\n"
            "• Missing or incompatible libusb backend\n"
            "• System USB driver conflicts\n"
            "• Incompatible macOS version\n\n"
            "To resolve this issue:\n"
            "1. Install or update libusb: brew install libusb\n"
            "2. If using Homebrew, try: brew reinstall libusb\n"
            "3. Restart your system\n"
            "4. Try the firmware installation again\n\n"
            "Click OK to open Homebrew installation instructions in your browser.",
            QMessageBox.Ok | QMessageBox.Cancel,
            QMessageBox.Ok
        )

        if reply == QMessageBox.Ok:
            # Open the Homebrew installation page in the default browser
            import webbrowser
            homebrew_url = "https://brew.sh/"
            webbrowser.open(homebrew_url)
            self.status_label.setText("Homebrew page opened - please install libusb and restart")
        else:
            self.status_label.setText("Backend error - please install libusb and restart")

        self.download_btn.setEnabled(True)  # Re-enable download button

    def on_keyboard_interrupt_detected(self):
        """Handle keyboard interrupt from MTKWorker"""
        # Stop the MTK worker to prevent it from continuing to run
        if self.mtk_worker:
            self.mtk_worker.stop()
            self.mtk_worker.wait()  # Wait for the worker to finish
            self.mtk_worker = None

        # On Windows: First show process_ended.png image briefly, then show install error dialog
        self.load_process_ended_image()
        
        # Use a timer to show the dialog after a short delay so user sees the process_ended image
        QTimer.singleShot(2000, self.show_install_error_dialog)
        return  # Don't continue with the revert timer since user will choose action

    def show_presteps_image(self):
        """Show the presteps image"""
        self.load_presteps_image()

    def set_image_with_aspect_ratio(self, pixmap):
        """Set image while maintaining aspect ratio"""
        if pixmap.isNull():
            return

        # Get the label size
        label_size = self.image_label.size()
        if label_size.width() <= 0 or label_size.height() <= 0:
            # Use minimum size if label not properly sized yet
            label_size = QSize(400, 300)

        # Scale image to fit the label while maintaining aspect ratio
        scaled_pixmap = pixmap.scaled(
            label_size,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        # Set the scaled pixmap
        self.image_label.setPixmap(scaled_pixmap)

        # Don't use setScaledContents to maintain aspect ratio
        self.image_label.setScaledContents(False)

        # Store current pixmap for resize events
        self._current_pixmap = pixmap

    def resizeEvent(self, event):
        """Handle window resize to maintain image aspect ratio"""
        super().resizeEvent(event)
        # Re-scale current image if one is loaded
        if hasattr(self, '_current_pixmap') and self._current_pixmap:
            self.set_image_with_aspect_ratio(self._current_pixmap)

    def get_platform_image_path(self, base_name):
        """Constructs a path to a platform-specific image, with a fallback to a generic one."""
        system = platform.system()
        if system == "Windows":
            suffix = "_win"
        elif system == "Darwin":
            suffix = "_mac"
        elif system == "Linux":
            suffix = "_linux"
        else:
            suffix = ""

        base_path = Path("mtkclient/gui/images")

        # Try platform-specific path first
        if suffix:
            platform_specific_path = base_path / f"{base_name}{suffix}.png"
            if platform_specific_path.exists():
                return str(platform_specific_path)

        # Fallback to generic path
        generic_path = base_path / f"{base_name}.png"
        return str(generic_path)

    def load_presteps_image(self):
        """Load presteps image with lazy loading and platform fallback."""
        if not hasattr(self, '_presteps_pixmap'):
            try:
                image_path = self.get_platform_image_path("presteps")
                self._presteps_pixmap = QPixmap(image_path)
                if self._presteps_pixmap.isNull():
                    silent_print(f"Failed to load image from {image_path}")
                    return
            except Exception as e:
                silent_print(f"Error loading presteps image: {e}")
                return

        self._current_pixmap = self._presteps_pixmap
        self.set_image_with_aspect_ratio(self._presteps_pixmap)

    def load_initsteps_image(self):
        """Load initsteps image with lazy loading and platform fallback."""
        if not hasattr(self, '_initsteps_pixmap'):
            try:
                image_path = self.get_platform_image_path("initsteps")
                self._initsteps_pixmap = QPixmap(image_path)
                if self._initsteps_pixmap.isNull():
                    silent_print(f"Failed to load image from {image_path}")
                    return
            except Exception as e:
                silent_print(f"Error loading initsteps image: {e}")
                return

        self._current_pixmap = self._initsteps_pixmap
        self.set_image_with_aspect_ratio(self._initsteps_pixmap)

    def load_installing_image(self):
        """Load installing image with lazy loading"""
        if not hasattr(self, '_installing_pixmap'):
            try:
                self._installing_pixmap = QPixmap("mtkclient/gui/images/installing.png")
                if self._installing_pixmap.isNull():
                    silent_print("Failed to load installing.png")
                    return
            except Exception as e:
                silent_print(f"Error loading installing image: {e}")
                return

        self._current_pixmap = self._installing_pixmap
        self.set_image_with_aspect_ratio(self._installing_pixmap)

    def load_installed_image(self):
        """Load installed image with lazy loading"""
        if not hasattr(self, '_installed_pixmap'):
            try:
                self._installed_pixmap = QPixmap("mtkclient/gui/images/installed.png")
                if self._installed_pixmap.isNull():
                    silent_print("Failed to load installed.png")
                    return
            except Exception as e:
                silent_print(f"Error loading installed image: {e}")
                return

        self._current_pixmap = self._installed_pixmap
        self.set_image_with_aspect_ratio(self._installed_pixmap)

    def load_handshake_error_image(self):
        """Load handshake error image with lazy loading and platform fallback."""
        if not hasattr(self, '_handshake_error_pixmap'):
            try:
                image_path = self.get_platform_image_path("handshake_err")
                self._handshake_error_pixmap = QPixmap(image_path)
                if self._handshake_error_pixmap.isNull():
                    silent_print(f"Failed to load image from {image_path}")
                    return
            except Exception as e:
                silent_print(f"Error loading handshake error image: {e}")
                return

        self._current_pixmap = self._handshake_error_pixmap
        self.set_image_with_aspect_ratio(self._handshake_error_pixmap)

    def load_process_ended_image(self):
        """Load process ended image with lazy loading"""
        if not hasattr(self, '_process_ended_pixmap'):
            try:
                self._process_ended_pixmap = QPixmap("mtkclient/gui/images/process_ended.png")
                if self._process_ended_pixmap.isNull():
                    silent_print("Failed to load process_ended.png")
                    return
            except Exception as e:
                silent_print(f"Error loading process ended image: {e}")
                return

        self._current_pixmap = self._process_ended_pixmap
        self.set_image_with_aspect_ratio(self._process_ended_pixmap)

    def open_coffee_link(self):
        """Open the Buy Us Coffee link in the default browser"""
        import webbrowser
        webbrowser.open("https://ko-fi.com/teamslide")

    def open_reddit_link(self):
        """Open the r/innioasis subreddit in the default browser"""
        import webbrowser
        webbrowser.open("https://www.reddit.com/r/innioasis")

    def open_discord_link(self):
        """Open the Discord server in the default browser"""
        import webbrowser
        webbrowser.open("https://discord.gg/jv8jEd8Uv5")

    def open_driver_setup_link(self):
        """Open the driver setup instructions in the default browser"""
        import webbrowser
        webbrowser.open("https://www.github.com/team-slide/Innioasis-Updater#windows-64bit-intelamd-only")

    def install_from_zip(self):
        """Install firmware from a local zip file"""
        from PySide6.QtWidgets import QFileDialog, QMessageBox
        
        # Open file dialog to select zip file
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Firmware ZIP File",
            "",
            "ZIP Files (*.zip)"
        )
        
        if not file_path:
            return
            
        zip_path = Path(file_path)
        if not zip_path.exists():
            QMessageBox.warning(self, "Error", "Selected file does not exist.")
            return
            
        # Confirm the installation
        reply = QMessageBox.question(
            self,
            "Confirm Installation",
            f"Install firmware from {zip_path.name}?\n\nThis will extract the zip file and prepare it for MTK installation.",
            QMessageBox.Ok | QMessageBox.Cancel,
            QMessageBox.Ok
        )
        
        if reply == QMessageBox.Cancel:
            return
            
        # Process the zip file
        self.status_label.setText("Processing zip file...")
        
        try:
            # Extract the zip file
            extracted_files = []
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(".")
                # Get list of extracted files
                extracted_files = zip_ref.namelist()
            
            # Log extracted files for cleanup
            log_extracted_files(extracted_files)
            
            self.status_label.setText("Zip file extracted successfully. Checking required files...")
            
            # Check if required files exist
            required_files = ["lk.bin", "boot.img", "recovery.img", "system.img", "userdata.img"]
            missing_files = []
            for file in required_files:
                if not Path(file).exists():
                    missing_files.append(file)
            
            if missing_files:
                error_msg = f"Missing required files: {', '.join(missing_files)}\n\n"
                error_msg += "The zip file must contain:\n"
                error_msg += "- lk.bin\n"
                error_msg += "- boot.img\n"
                error_msg += "- recovery.img\n"
                error_msg += "- system.img\n"
                error_msg += "- userdata.img\n\n"
                error_msg += "Please ensure your zip file contains all required firmware files."
                
                QMessageBox.warning(self, "Missing Files", error_msg)
                self.status_label.setText("Zip file missing required firmware files.")
                return
            
            # Show success message
            success_msg = "Firmware files successfully extracted:\n"
            for file in required_files:
                file_size = Path(file).stat().st_size
                size_mb = file_size / (1024 * 1024)
                success_msg += f"- {file} ({size_mb:.1f} MB)\n"
            
            success_msg += "\nAll required files are present. Ready for MTK installation."
            QMessageBox.information(self, "Success", success_msg)
            
            # Automatically run MTK command after a short delay
            self.status_label.setText("Starting MTK installation in 3 seconds...")
            QTimer.singleShot(3000, self.run_mtk_command)
            
        except Exception as e:
            error_msg = f"Error processing zip file: {str(e)}"
            QMessageBox.critical(self, "Error", error_msg)
            self.status_label.setText("Error processing zip file.")
            silent_print(f"Zip processing error: {e}")

    def run_driver_setup(self):
        """Runs the driver setup script (main.py)"""
        try:
            # Get the current directory where firmware_downloader.py is located
            current_dir = Path(__file__).parent
            main_py_path = current_dir / "main.py"

            if not main_py_path.exists():
                QMessageBox.warning(self, "Error", "main.py not found. Please ensure main.py is in the same directory as firmware_downloader.py.")
                return

            # Run main.py
            silent_print("Running main.py for driver setup...")
            self.status_label.setText("Running driver setup...")
            self.download_btn.setEnabled(False) # Disable download button while running

            # Use subprocess to run main.py in the current directory
            subprocess.Popen([sys.executable, str(main_py_path)], cwd=str(current_dir))

            # After main.py finishes, revert to startup state
            QTimer.singleShot(1000, self.revert_to_startup_state) # Small delay to allow main.py to start

        except Exception as e:
            silent_print(f"Error running driver setup: {e}")
            self.status_label.setText(f"Error running driver setup: {e}")
            self.download_btn.setEnabled(True)

    def revert_to_startup_state(self):
        """Revert the app to its startup state"""
        # Cancel any existing revert timer to prevent conflicts
        if hasattr(self, '_revert_timer') and self._revert_timer:
            self._revert_timer.stop()
            self._revert_timer = None

        # Load and display presteps.png (startup state)
        self.load_presteps_image()

        # Reset status
        self.status_label.setText("Ready")

        # Ensure download button is enabled
        self.download_btn.setEnabled(True)

    def populate_package_list(self):
        """Populate the package list widget with release information"""
        self.package_list.clear()

        for package in self.packages:
            device_type = package.get('device_type', '')
            device_model = package.get('device', '')

            device_type_text = f" (Type {device_type})" if device_type else ""
            device_model_text = f" [{device_model}]" if device_model else ""

            # Get latest release information
            release_info = self.github_api.get_latest_release(package['repo'])
            release_text = ""
            if release_info:
                release_text = f"\nLatest Release: {release_info.get('tag_name', 'Unknown')}"
                if release_info.get('name'):
                    release_text += f" ({release_info['name']})"

            item_text = f"{package['name']}{device_type_text}{device_model_text}\n"
            item_text += f"Repo: {package['repo']}{release_text}\n"
            item_text += f"Handler: {package['handler']}"

            item = QListWidgetItem(item_text)
            item.setData(Qt.UserRole, package)
            self.package_list.addItem(item)

        # Automatically select the first item for improved discoverability
        if self.package_list.count() > 0:
            self.package_list.setCurrentRow(0)
            self.package_list.setFocus()  # Give focus to the list for blue highlight
            self.download_btn.setEnabled(True)
            # Update button text for the first selected item
            first_item = self.package_list.item(0)
            self.update_download_button_text(first_item)

    def filter_firmware_options(self):
        """Filter software options based on device type and model"""
        # Repopulate software combo with filtered options
        self.populate_firmware_combo()

        # Update the releases list based on current software selection
        selected_repo = self.firmware_combo.currentData()
        if selected_repo:
            # Specific software selected - show only its releases
            self.populate_releases_list()
        else:
            # "All Software" selected - show all releases
            self.populate_all_releases_list()



    def start_download(self):
        """Start the download and processing process"""
        # Cancel any existing revert timer to prevent conflicts
        if hasattr(self, '_revert_timer') and self._revert_timer:
            self._revert_timer.stop()
            self._revert_timer = None

        # Stop any existing MTK worker to prevent conflicts
        if hasattr(self, 'mtk_worker') and self.mtk_worker:
            self.mtk_worker.stop()
            self.mtk_worker.wait()
            self.mtk_worker = None

        current_item = self.package_list.currentItem()
        if not current_item:
            self.status_label.setText("Error: Please select a release from the list")
            return

        release_info = current_item.data(Qt.UserRole)

        if not release_info:
            self.status_label.setText("Error: Please select a valid release from the list")
            return

        # Get the repository from the release info (for "All Firmware" selection)
        # or from the firmware combo (for specific firmware selection)
        selected_repo = self.firmware_combo.currentData()

        # If "All Software" is selected, we need to get the repo from the release info
        if not selected_repo and 'software_name' in release_info:
            # This is from "All Software" - find the repo for this software
            software_name = release_info['software_name']
            for package in self.packages:
                if package.get('name') == software_name:
                    selected_repo = package.get('repo')
                    break

        if not selected_repo:
            self.status_label.setText("Error: Could not determine repository for selected release")
            return

        if not release_info:
            QMessageBox.warning(self, "Error", f"Failed to get release information for {selected_repo}")
            return

        if not release_info['download_url']:
            # Show what assets are available
            error_msg = f"No rom.zip found in release {selected_repo} for {selected_repo}\n\n"
            error_msg += f"Release: {release_info.get('tag_name', 'Unknown')}\n"
            error_msg += f"Name: {release_info.get('name', 'Unknown')}\n\n"
            error_msg += "Available assets:\n"

            # Try to get asset list for better error reporting
            try:
                url = f"https://api.github.com/repos/{selected_repo}/releases"
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    releases_data = response.json()
                    for release in releases_data:
                        if release.get('tag_name') == selected_repo: # This line seems to be a typo, should be release.get('tag_name')
                            assets = release.get('assets', [])
                            if assets:
                                for asset in assets:
                                    error_msg += f"- {asset['name']}\n"
                            else:
                                error_msg += "- No assets found\n"
                            break
                else:
                    error_msg += "- Could not retrieve asset list\n"
            except:
                error_msg += "- Could not retrieve asset list\n"

            QMessageBox.warning(self, "Error", error_msg)
            return

        # Start download worker
        self.download_worker = DownloadWorker(release_info['download_url'], selected_repo, release_info['tag_name'])
        self.download_worker.progress_updated.connect(self.progress_bar.setValue)
        self.download_worker.status_updated.connect(self.status_label.setText)
        self.download_worker.download_completed.connect(self.on_download_completed)

        self.download_btn.setEnabled(False)
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)

        silent_print(f"Starting download for {selected_repo}...")
        silent_print(f"Release: {release_info['tag_name']}")
        silent_print(f"Download URL: {release_info['download_url']}")

        self.download_worker.start()

    def on_download_completed(self, success, output):
        """Handle download completion"""
        self.download_btn.setEnabled(True)
        self.progress_bar.setVisible(False)

        if success:
            self.status_label.setText("Download and processing completed successfully")
            print("=== PROCESSING COMPLETED ===")
            print("Firmware files have been downloaded and extracted successfully.")

            # Check if required files exist and automatically run MTK command
            required_files = ["lk.bin", "boot.img", "recovery.img", "system.img", "userdata.img"]
            if all(Path(file).exists() for file in required_files):
                silent_print("=== AUTOMATICALLY RUNNING MTK COMMAND ===")
                silent_print("The MTK flash command will now run in this application.")
                silent_print("Please turn off your Y1 when prompted.")

                # Use QTimer to delay the automatic MTK command execution slightly
                QTimer.singleShot(2000, self.run_mtk_command)  # 2 second delay
        else:
            self.status_label.setText("Download or processing failed")
            silent_print("=== PROCESSING FAILED ===")

        silent_print(output)

    def refresh_all_data(self):
        """Refresh all data (tokens, manifest, device types, models, software) with cache clearing"""
        self.status_label.setText("Refreshing data...")
        silent_print("Refreshing data...")

        # Clear cache to force fresh data
        clear_cache()

        # Download tokens
        tokens = self.config_downloader.download_config()
        if not tokens:
            silent_print("ERROR: Failed to download API tokens")
            QMessageBox.warning(self, "Error", "Failed to download API tokens. Please check your internet connection or try again later.")
            return

        self.github_api = GitHubAPI(tokens)
        silent_print(f"Loaded {len(tokens)} API tokens")

        # Download manifest
        self.packages = self.config_downloader.download_manifest()
        if not self.packages:
            silent_print("ERROR: Failed to download manifest")
            QMessageBox.warning(self, "Error", "Failed to download software manifest. Please check your internet connection or try again later.")
            return

        silent_print(f"Loaded {len(self.packages)} software packages")

        # Repopulate all combos
        self.populate_device_type_combo()
        self.populate_device_model_combo()
        self.populate_firmware_combo()

        # Apply initial filters (Type A and Y1 are already set as defaults)
        self.filter_firmware_options()

        # Show releases based on current software selection (not always "All Software")
        try:
            selected_repo = self.firmware_combo.currentData()
            if selected_repo:
                self.populate_releases_list()
            else:
                self.populate_all_releases_list_progressive()

            self.status_label.setText("Ready")
            silent_print("Data refresh complete.")
        except Exception as e:
            silent_print(f"Error populating releases: {e}")
            self.status_label.setText("Error loading releases - check internet connection")
            # Show a basic message to prevent complete failure
            self.package_list.clear()
            self.package_list.addItem("Error: Could not load releases. Please check your internet connection and try again.")

    def is_dark_mode(self):
        """Detect if the system is in dark mode"""
        try:
            # Check if the application is using a dark theme
            palette = self.palette()
            background_color = palette.color(palette.Window)

            # Calculate luminance to determine if it's dark
            luminance = (0.299 * background_color.red() +
                        0.587 * background_color.green() +
                        0.114 * background_color.blue()) / 255

            return luminance < 0.5
        except:
            # Fallback: assume light mode if detection fails
            return False

    def update_image_style(self):
        """Update the image label style based on system theme"""
        is_dark = self.is_dark_mode()

        if is_dark:
            # Dark theme styling - use transparent background to preserve PNG transparency
            self.image_label.setStyleSheet("""
                QLabel {
                    background-color: transparent;
                    border: 0.5px solid #2a2a2a;
                    border-radius: 5px;
                    color: white;
                }
            """)
        else:
            # Light theme styling - use transparent background to preserve PNG transparency
            self.image_label.setStyleSheet("""
                QLabel {
                    background-color: transparent;
                    border: 0.5px solid #f0f0f0;
                    border-radius: 5px;
                    color: #333;
                }
            """)

    def check_theme_change(self):
        """Check if the system theme has changed"""
        current_theme_state = self.is_dark_mode()
        if current_theme_state != self.last_theme_state:
            self.last_theme_state = current_theme_state
            self.update_image_style()

    def on_palette_changed(self):
        """Handle system theme changes (legacy method)"""
        self.update_image_style()

    def ensure_proper_image_sizing(self):
        """Ensure proper image sizing after window is fully initialized"""
        if hasattr(self, '_presteps_pixmap') and self._presteps_pixmap:
            self.set_image_with_aspect_ratio(self._presteps_pixmap)

    def launch_updater_script(self):
        """Launch the separate updater script to handle updates gracefully"""
        try:
            # Check if updater script exists
            updater_script_path = Path("updater.py")
            if not updater_script_path.exists():
                QMessageBox.warning(self, "Update Error",
                                  "Updater script not found. Please ensure updater.py is in the same directory.")
                return

            # Show confirmation dialog
            reply = QMessageBox.question(
                self,
                "Update Confirmation",
                "This will download and install the latest version of the Innioasis Updater.\n\n"
                "The current application will close and the updated version will be launched automatically.\n\n"
                "Do you want to continue?",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.Yes
            )

            if reply == QMessageBox.Yes:
                # Launch the updater script with -f argument for force update
                subprocess.Popen([sys.executable, str(updater_script_path), "-f"])

                # Close the current app after a short delay
                QTimer.singleShot(1000, self.close)

        except Exception as e:
            QMessageBox.warning(self, "Update Error", f"Error launching updater: {str(e)}")

    def show_install_error_dialog(self):
        """Show the install error dialog with troubleshooting options (Windows only)"""
        # Only show troubleshooting dialog on Windows
        if platform.system() != "Windows":
            # On Mac/Linux, just show process_ended image as usual
            self.load_process_ended_image()
            
            # Cancel any existing revert timer to prevent conflicts
            if hasattr(self, '_revert_timer') and self._revert_timer:
                self._revert_timer.stop()
                self._revert_timer = None

            # Set timer to revert to startup state after 30 seconds
            self._revert_timer = QTimer()
            self._revert_timer.timeout.connect(self.revert_to_startup_state)
            self._revert_timer.setSingleShot(True)
            self._revert_timer.start(30000)
            return
        
        # Windows-specific troubleshooting dialog
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Install Error")
        msg_box.setText("Something interrupted the firmware install process, would you like to try a troubleshooting run?")
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Retry)
        msg_box.setDefaultButton(QMessageBox.Yes)
        
        # Customize button text
        msg_box.button(QMessageBox.Yes).setText("Run with Troubleshooting")
        msg_box.button(QMessageBox.No).setText("Exit")
        msg_box.button(QMessageBox.Retry).setText("Retry")
        
        reply = msg_box.exec()
        
        if reply == QMessageBox.Yes:
            # Show troubleshooting instructions
            self.show_troubleshooting_instructions()
        elif reply == QMessageBox.Retry:
            # Show unplug Y1 prompt and retry normal installation
            self.show_unplug_prompt_and_retry()
        else:
            # Exit the application
            QApplication.quit()

    def show_unplug_prompt_and_retry(self):
        """Show the unplug Y1 prompt and retry normal installation"""
        # Show the same unplug prompt that's used at the start of normal installation
        reply = QMessageBox.question(
            self,
            "Get Ready",
            "Please make sure your Y1 is NOT plugged in and press OK, then follow the next instructions.",
            QMessageBox.Ok | QMessageBox.Cancel,
            QMessageBox.Cancel
        )

        if reply == QMessageBox.Cancel:
            return

        # Load and display the init steps image
        self.load_initsteps_image()

        # Start MTK worker
        self.mtk_worker = MTKWorker()
        self.mtk_worker.status_updated.connect(self.status_label.setText)
        self.mtk_worker.show_installing_image.connect(self.load_installing_image)
        self.mtk_worker.mtk_completed.connect(self.on_mtk_completed)
        self.mtk_worker.handshake_failed.connect(self.on_handshake_failed)
        self.mtk_worker.errno2_detected.connect(self.on_errno2_detected)
        self.mtk_worker.backend_error_detected.connect(self.on_backend_error_detected)
        self.mtk_worker.keyboard_interrupt_detected.connect(self.on_keyboard_interrupt_detected)
        self.mtk_worker.disable_update_button.connect(self.disable_update_button)
        self.mtk_worker.enable_update_button.connect(self.enable_update_button)

        self.mtk_worker.start()

        # Disable download button during MTK operation
        self.download_btn.setEnabled(False)

    def show_troubleshooting_instructions(self):
        """Show troubleshooting instructions and launch recovery firmware install"""
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Troubleshooting Instructions")
        msg_box.setText("Please follow these steps:\n\n"
                       "1. Connect your Y1 device via USB\n"
                       "2. Reconnect the USB cable\n"
                       "3. Insert your paperclip once when the black window appears\n\n"
                       "Click OK when ready to launch the recovery firmware installer.")
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setDefaultButton(QMessageBox.Ok)
        
        reply = msg_box.exec()
        
        if reply == QMessageBox.Ok:
            # Launch Recover Firmware Install.lnk
            self.launch_recovery_firmware_install()

    def launch_recovery_firmware_install(self):
        """Launch the Recover Firmware Install.lnk file"""
        try:
            # Look for the .lnk file in the same directory as firmware_downloader.py
            current_dir = Path.cwd()
            recovery_lnk = current_dir / "Recover Firmware Install.lnk"
            
            if recovery_lnk.exists():
                if platform.system() == "Windows":
                    # On Windows, use os.startfile to launch the .lnk file
                    os.startfile(str(recovery_lnk))
                    self.status_label.setText("Recovery Firmware Install launched successfully")
                else:
                    # On other platforms, try to open with default handler
                    subprocess.run(["xdg-open" if platform.system() == "Linux" else "open", str(recovery_lnk)])
                    self.status_label.setText("Recovery Firmware Install launched successfully")
            else:
                # If .lnk file not found, try to find alternative recovery methods
                self.status_label.setText("Recovery Firmware Install.lnk not found - please check installation")
                
                # Show error message
                QMessageBox.warning(
                    self,
                    "File Not Found",
                    "Recover Firmware Install.lnk was not found in the current directory.\n\n"
                    "Please ensure the file is present and try again."
                )
        except Exception as e:
            self.status_label.setText(f"Error launching recovery firmware install: {e}")
            
            # Show error message
            QMessageBox.critical(
                self,
                "Launch Error",
                f"Failed to launch the recovery firmware installer:\n{e}\n\n"
                "Please try launching it manually."
            )

if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)

    # Set application icon based on platform
    from PySide6.QtGui import QIcon
    import platform

    if platform.system() == "Darwin":  # macOS
        icon_path = "mtkclient/gui/images/Innioasis Updater Icon.icns"
    elif platform.system() == "Windows":
        icon_path = "mtkclient/gui/images/icon.ico"
    else:
        # Fallback to PNG for other platforms
        icon_path = "mtkclient/gui/images/icon.png"

    if Path(icon_path).exists():
        app.setWindowIcon(QIcon(icon_path))

    # Create and show the main window
    window = FirmwareDownloaderGUI()
    window.show()

    # Start the application event loop
    sys.exit(app.exec())
