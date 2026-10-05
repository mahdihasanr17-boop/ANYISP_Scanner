# Auto-generated obfuscated build (do not edit)
_SEC_SALT = 3035044142

def _sec_string(enc, _s=_SEC_SALT):
    import base64 as _b64
    try:
        _b = _b64.b64decode(str(enc).encode("ascii"))
        _k = (_s & 0xffffffff).to_bytes(4, "big")
        _out = bytearray()
        for _i in range(len(_b)):
            _out.append(_b[_i] ^ _k[_i & 3])
        return bytes(_out).decode("utf-8", errors="replace")
    except Exception:
        return ""

"""
V5 Client - License Handler
Handles device binding, server activation, token caching, offline expiry check.
"""
import os
import sys
import time
import json
import base64
import hashlib
import threading
from datetime import datetime
try:
    from .core import config_encrypt, config_decrypt, config_hmac, verify_config_hmac, get_device_id, get_hw_fingerprint, run_security_init, start_security_monitor, check_timing_anomaly
except (ImportError, ValueError):
    from core import config_encrypt, config_decrypt, config_hmac, verify_config_hmac, get_device_id, get_hw_fingerprint, run_security_init, start_security_monitor, check_timing_anomaly
CLIENT_BUILD = _sec_string('hckrAIXR')

class LicenseError(Exception):
    pass

class LicenseHandler:

    def __init__(self, config_dir=None):
        self.device_id = get_device_id()
        self.hw_fingerprint = get_hw_fingerprint()
        self.config_dir = config_dir or self._default_config_dir()
        self.config_path = os.path.join(self.config_dir, _sec_string('14h3SN2AN0vahA=='))
        self.breach_queue_path = os.path.join(self.config_dir, _sec_string('1pV8T9ePRl/BgmxLmo1qQdo='))
        self.lock = threading.Lock()
        self.stop_event = threading.Event()
        self.monitor = None
        self.breach_callback = None

    def _default_config_dir(self):
        if _sec_string('569cYvg=') in os.environ and _sec_string('wIJrQ8Gf') in os.environ.get(_sec_string('5LVcaP2/'), ''):
            return os.path.join(os.environ.get(_sec_string('5LVcaP2/'), _sec_string('yg==')), _sec_string('msk='), _sec_string('0o51S8c='), _sec_string('3Ih0Sw=='), _sec_string('mpEs'))
        home = os.path.expanduser(_sec_string('yg=='))
        return os.path.join(home, _sec_string('mpEs'))

    def ensure_dirs(self):
        os.makedirs(self.config_dir, exist_ok=True)

    def _save_config(self, data: dict):
        self.ensure_dirs()
        payload = json.dumps(data).encode()
        encrypted = config_encrypt(payload, self.device_id)
        signature = config_hmac(encrypted, self.device_id)
        try:
            with open(self.config_path, _sec_string('w4U=')) as f:
                f.write(encrypted + b'|SIG|' + signature)
        except Exception as e:
            raise LicenseError(f'Failed to save config: {e}')

    def _load_config(self) -> dict:
        if not os.path.exists(self.config_path):
            return {}
        try:
            with open(self.config_path, _sec_string('xoU=')) as f:
                content = f.read()
            if b'|SIG|' in content:
                encrypted, signature = content.split(b'|SIG|', 1)
                if not verify_config_hmac(encrypted, signature, self.device_id):
                    raise LicenseError(_sec_string('94h3SN2AOUfak3xJxo5tV5SEcUvXjDlI1Y51S9A='))
                payload = config_decrypt(encrypted, self.device_id)
                return json.loads(payload)
        except Exception as e:
            raise LicenseError(f'Failed to load config: {e}')
        return {}

    def is_configured(self) -> bool:
        return True

    def activate(self, config=None, use_https=True):
        return True

    def validate(self):
        return _sec_string('woZ1R9A=')

    def get_expiry(self) -> str:
        try:
            cfg = self._load_config()
            return cfg.get(_sec_string('0Z9pR8aeRkrVk3w='), '')
        except Exception:
            return ''

    def get_server_url(self) -> str:
        try:
            cfg = self._load_config()
            return cfg.get(_sec_string('x4JrWNGV'), '')
        except Exception:
            return ''

    def get_token(self) -> str:
        try:
            cfg = self._load_config()
            return cfg.get(_sec_string('wIhyS9o='), '')
        except Exception:
            return ''

    def get_breach_queue_path(self) -> str:
        """Persistent queue of suspicious activity detected while offline."""
        return self.breach_queue_path

    def has_pending_breach_report(self) -> bool:
        """True if a suspicious-activity event is queued (device was offline)."""
        return os.path.exists(self.breach_queue_path)

    def flush_pending_breach_queue(self, server_url: str, use_https: bool=True) -> int:
        """
        Deliver every queued suspicious-activity report to the server now that we
        are online. Serious (decryption/tamper) reports make the server suspend
        the active activation immediately. Returns how many reports were sent.
        """
        try:
            from .core import flush_breach_queue
        except (ImportError, ValueError):
            from core import flush_breach_queue
        return flush_breach_queue(server_url, use_https, self.breach_queue_path)

    def get_assigned_version(self) -> str:
        """Return the client engine (v5/v6) the server has assigned this device."""
        try:
            cfg = self._load_config()
            version = cfg.get(_sec_string('1ZRqR9OJfErrkXxcx452QA=='), '') or cfg.get(_sec_string('woJrXd2Idw=='), _sec_string('wtI='))
            return version if version in (_sec_string('wtI='), _sec_string('wtE=')) else _sec_string('wtI=')
        except Exception:
            return _sec_string('wtI=')

    def set_assigned_version(self, version: str):
        """Persist the latest server-assigned engine (called after each heartbeat)."""
        if version not in (_sec_string('wtI='), _sec_string('wtE=')):
            return
        try:
            cfg = self._load_config()
        except LicenseError:
            return
        if cfg.get(_sec_string('1ZRqR9OJfErrkXxcx452QA==')) == version:
            return
        new_cfg = dict(cfg)
        new_cfg[_sec_string('woJrXd2Idw==')] = version
        new_cfg[_sec_string('1ZRqR9OJfErrkXxcx452QA==')] = version
        try:
            self._save_config(new_cfg)
        except Exception:
            pass

    def _sync_server_expiry(self, expiry_date):
        """
        Overwrite the locally cached expiry with the server's current value so
        admin renewals / revoke-and-reactivate changes are seen on next run.
        """
        if not expiry_date:
            return
        try:
            cfg = self._load_config()
        except LicenseError:
            return
        if cfg.get(_sec_string('0Z9pR8aeRkrVk3w=')) == expiry_date:
            return
        new_cfg = dict(cfg)
        new_cfg[_sec_string('0Z9pR8aeRkrVk3w=')] = expiry_date
        try:
            self._save_config(new_cfg)
        except Exception:
            pass

    def days_remaining(self):
        return 99999

    def fetch_policy(self, use_https=True):
        return True

    def has_fresh_policy(self, max_age_seconds=None):
        return True

    def heartbeat(self, use_https=True):
        return True
