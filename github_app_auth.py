#!/usr/bin/env python3
"""
GitHub App API Authentication Module
Handles GitHub App authentication using JWT tokens and installation access tokens
"""

import os
import time
import json
import base64
import hashlib
import hmac
import requests
from pathlib import Path
from typing import Optional, Dict, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GitHubAppAuth:
    """GitHub App authentication handler"""
    
    def __init__(self, app_id: str, private_key_path: str, installation_id: str):
        self.app_id = app_id
        self.private_key_path = private_key_path
        self.installation_id = installation_id
        self.installation_token = None
        self.token_expires_at = 0
        self.session = requests.Session()
        self.session.timeout = 10
        
    def _load_private_key(self) -> str:
        """Load the private key from file"""
        try:
            with open(self.private_key_path, 'r') as f:
                return f.read()
        except Exception as e:
            logger.error(f"Failed to load private key from {self.private_key_path}: {e}")
            raise
    
    def _generate_jwt_token(self) -> str:
        """Generate a JWT token for GitHub App authentication"""
        import jwt
        
        private_key = self._load_private_key()
        now = int(time.time())
        
        payload = {
            'iat': now - 60,  # Issued at (1 minute ago to account for clock skew)
            'exp': now + 600,  # Expires in 10 minutes
            'iss': self.app_id  # Issuer (GitHub App ID)
        }
        
        try:
            token = jwt.encode(payload, private_key, algorithm='RS256')
            return token
        except Exception as e:
            logger.error(f"Failed to generate JWT token: {e}")
            raise
    
    def _get_installation_token(self) -> Optional[str]:
        """Get installation access token"""
        if self.installation_token and time.time() < self.token_expires_at:
            return self.installation_token
        
        try:
            jwt_token = self._generate_jwt_token()
            headers = {
                'Authorization': f'Bearer {jwt_token}',
                'Accept': 'application/vnd.github.v3+json'
            }
            
            url = f'https://api.github.com/app/installations/{self.installation_id}/access_tokens'
            response = self.session.post(url, headers=headers)
            
            if response.status_code == 201:
                data = response.json()
                self.installation_token = data['token']
                # Set expiration time (GitHub tokens expire in 1 hour)
                self.token_expires_at = time.time() + 3600
                logger.info("Successfully obtained installation access token")
                return self.installation_token
            else:
                logger.error(f"Failed to get installation token: {response.status_code} - {response.text}")
                return None
                
        except Exception as e:
            logger.error(f"Error getting installation token: {e}")
            return None
    
    def get_auth_headers(self) -> Dict[str, str]:
        """Get authentication headers for API requests"""
        token = self._get_installation_token()
        if token:
            return {
                'Authorization': f'token {token}',
                'Accept': 'application/vnd.github.v3+json'
            }
        return {}
    
    def make_authenticated_request(self, url: str, method: str = 'GET', **kwargs) -> Optional[requests.Response]:
        """Make an authenticated request to GitHub API"""
        headers = self.get_auth_headers()
        if 'headers' in kwargs:
            headers.update(kwargs['headers'])
        kwargs['headers'] = headers
        
        try:
            response = self.session.request(method, url, **kwargs)
            return response
        except Exception as e:
            logger.error(f"Error making authenticated request to {url}: {e}")
            return None

class ConfigManager:
    """Manages configuration loading from local file or remote source"""
    
    def __init__(self, base_dir: str = None):
        self.base_dir = Path(base_dir) if base_dir else Path.cwd()
        self.config_file = self.base_dir / "config.ini"
        self.remote_config_url = "https://raw.githubusercontent.com/team-slide/Y1-helper/refs/heads/master/config.ini"
        self.cache_file = self.base_dir / ".cache" / "config_cache.json"
        self.cache_duration = 3600  # 1 hour
        
    def _load_config_from_file(self, config_path: Path) -> Optional[Dict[str, Any]]:
        """Load configuration from a local file"""
        try:
            import configparser
            config = configparser.ConfigParser()
            config.read(config_path)
            
            # Convert to dictionary
            config_dict = {}
            for section in config.sections():
                config_dict[section] = dict(config[section])
            
            return config_dict
        except Exception as e:
            logger.error(f"Failed to load config from {config_path}: {e}")
            return None
    
    def _download_remote_config(self) -> Optional[Dict[str, Any]]:
        """Download configuration from remote source"""
        try:
            response = requests.get(self.remote_config_url, timeout=10)
            if response.status_code == 200:
                # Save to temporary file and load
                temp_config = self.base_dir / "temp_config.ini"
                with open(temp_config, 'w') as f:
                    f.write(response.text)
                
                config_dict = self._load_config_from_file(temp_config)
                temp_config.unlink()  # Clean up
                return config_dict
            else:
                logger.error(f"Failed to download remote config: {response.status_code}")
                return None
        except Exception as e:
            logger.error(f"Error downloading remote config: {e}")
            return None
    
    def _load_cache(self) -> Optional[Dict[str, Any]]:
        """Load configuration from cache"""
        try:
            if self.cache_file.exists():
                with open(self.cache_file, 'r') as f:
                    cache_data = json.load(f)
                
                # Check if cache is still valid
                if time.time() - cache_data.get('timestamp', 0) < self.cache_duration:
                    return cache_data.get('config')
        except Exception as e:
            logger.error(f"Failed to load config cache: {e}")
        return None
    
    def _save_cache(self, config: Dict[str, Any]):
        """Save configuration to cache"""
        try:
            self.cache_file.parent.mkdir(exist_ok=True)
            cache_data = {
                'config': config,
                'timestamp': time.time()
            }
            with open(self.cache_file, 'w') as f:
                json.dump(cache_data, f)
        except Exception as e:
            logger.error(f"Failed to save config cache: {e}")
    
    def load_config(self) -> Optional[Dict[str, Any]]:
        """Load configuration with fallback chain: local file -> cache -> remote"""
        # Try local config file first
        if self.config_file.exists():
            config = self._load_config_from_file(self.config_file)
            if config:
                logger.info("Loaded configuration from local file")
                self._save_cache(config)
                return config
        
        # Try cache
        config = self._load_cache()
        if config:
            logger.info("Loaded configuration from cache")
            return config
        
        # Try remote config
        config = self._download_remote_config()
        if config:
            logger.info("Loaded configuration from remote source")
            self._save_cache(config)
            return config
        
        logger.error("Failed to load configuration from any source")
        return None
    
    def get_github_app_config(self) -> Optional[Dict[str, str]]:
        """Get GitHub App configuration"""
        config = self.load_config()
        if not config:
            return None
        
        # Try local GitHub App config first
        if 'github_app' in config:
            app_config = config['github_app']
            if all(key in app_config for key in ['app_id', 'private_key_path', 'installation_id']):
                return app_config
        
        # Try remote GitHub App config
        if 'github_app_remote' in config:
            app_config = config['github_app_remote']
            if all(key in app_config for key in ['app_id', 'private_key_path', 'installation_id']):
                return app_config
        
        return None
    
    def get_fallback_tokens(self) -> list:
        """Get fallback PAT tokens"""
        config = self.load_config()
        if not config:
            return []
        
        tokens = []
        
        # Get tokens from api_keys section
        if 'api_keys' in config:
            for key, value in config['api_keys'].items():
                if key.startswith('key_') and value.strip():
                    tokens.append(value.strip())
        
        # Get legacy token
        if 'github' in config and 'token' in config['github']:
            token = config['github']['token'].strip()
            if token and token not in tokens:
                tokens.append(token)
        
        return tokens

def create_github_app_auth(base_dir: str = None) -> Optional[GitHubAppAuth]:
    """Create GitHub App authentication instance"""
    config_manager = ConfigManager(base_dir)
    app_config = config_manager.get_github_app_config()
    
    if not app_config:
        logger.warning("No GitHub App configuration found")
        return None
    
    try:
        # Resolve private key path
        private_key_path = app_config['private_key_path']
        if not os.path.isabs(private_key_path):
            private_key_path = os.path.join(base_dir or '.', private_key_path)
        
        return GitHubAppAuth(
            app_id=app_config['app_id'],
            private_key_path=private_key_path,
            installation_id=app_config['installation_id']
        )
    except Exception as e:
        logger.error(f"Failed to create GitHub App auth: {e}")
        return None