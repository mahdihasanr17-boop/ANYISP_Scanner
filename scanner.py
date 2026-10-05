# Auto-generated obfuscated build (do not edit)
_SEC_SALT = 2839264508

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
Universal ANYISP Scanner - One install, both engines.
The server decides (per user) which engine this device runs: V5 or V6.
After activation the assigned version is stored locally, and every heartbeat
re-checks the panel setting so flipping V5<->V6 takes effect on next run.
"""
import os
import sys
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass
import json
import time
import base64
import hashlib
import asyncio
import platform
import threading
import subprocess
from datetime import datetime
CLIENT_VERSION = _sec_string('nhWM0pk=')
try:
    from security.core import get_device_id, get_hw_fingerprint, run_security_init, get_build_props
    from security.license import LicenseHandler, LicenseError
    SECURITY_AVAILABLE = True
except ImportError:
    try:
        from client.security.core import get_device_id, get_hw_fingerprint, run_security_init, get_build_props
        from client.security.license import LicenseHandler, LicenseError
        SECURITY_AVAILABLE = True
    except ImportError:
        try:
            from core import get_device_id, get_hw_fingerprint, run_security_init, get_build_props
            from license import LicenseHandler, LicenseError
            SECURITY_AVAILABLE = True
        except ImportError:
            SECURITY_AVAILABLE = False
SERVER_URL = _sec_string('wU/IjNoBk9PfDpGKnxbencpQ2ZLNFdOS217SmMxJkp/GVg==')
SERVER_PORT = 443
USE_HTTPS = True
CLIENT_BUILD = _sec_string('mBWO0pgN')
TIMEOUT = 15
COLORS = {_sec_string('217Y'): _sec_string('smCNx5oK0Q=='), _sec_string('zknZmcc='): _sec_string('smCNx5oJ0Q=='), _sec_string('0F7QkMZM'): _sec_string('smCNx5oI0Q=='), _sec_string('y1fJmQ=='): _sec_string('smCNx5oP0Q=='), _sec_string('xFrbmcdP3Q=='): _sec_string('smCNx5oO0Q=='), _sec_string('ykLdkg=='): _sec_string('smCNx5oN0Q=='), _sec_string('3lPViMw='): _sec_string('smCNx5oM0Q=='), _sec_string('217Pmd0='): _sec_string('smCMkQ=='), _sec_string('zVLR'): _sec_string('smCOkQ==')}

def c(color, text):
    return f"{COLORS.get(color, COLORS[_sec_string('217Pmd0=')])}{text}{COLORS[_sec_string('217Pmd0=')]}"

def show_device_id():
    if not SECURITY_AVAILABLE:
        print(c(_sec_string('217Y'), _sec_string('+l7fidtSyIWJVtOY3FfZ3NxV3YrIUtCdy1fZ')))
        return
    device_id = get_device_id()
    print(c(_sec_string('ykLdkg=='), _sec_string('7X7qtep+nLXtG/+z+WKG3A==')) + c(_sec_string('zknZmcc='), device_id))
    print(c(_sec_string('zVLR'), _sec_string('+l7SmIlP1JXaG/W4iU/T3N1T2dzIX9GVxxvIk4la34jATd2IzBvFk9xJnJDAWNmS2l6S')))
    input(c(_sec_string('0F7QkMZM'), _sec_string('o2vOmdpInLnHT9mOiU/T3MpU0ojAVcmZhxWS')))

def grad(text, c1, c2):
    n = len(text)
    if n <= 1:
        return text
    out = []
    for i, ch in enumerate(text):
        t = i / (n - 1)
        r = int(c1[0] + (c2[0] - c1[0]) * t)
        g = int(c1[1] + (c2[1] - c1[1]) * t)
        b = int(c1[2] + (c2[2] - c1[2]) * t)
        out.append(f"\x1b[38;2;{r};{g};{b}m{ch}")
    return "".join(out) + "\x1b[0m"

def show_logo():
    C_CYAN = (0, 240, 255)
    C_PINK = (255, 40, 160)
    C_GOLD = (255, 200, 40)
    
    logo = [
        "  █████  ███▄    █▓██   ██▓██▓  ██████ ",
        " ██   ██ █▒██    █▒▒██ ██▒ ▓█▒ ▒█     ░",
        " ███████ █▒ █    █▒ ▒███░  ▒█░ ░█████  ",
        " ██   ██ █▒  █   █▒  ▒█▒   ▒█░     ▒█▒ ",
        " ██   ██ █▒   ████▒  ▒█▒   ░█░ ▒█████▒ "
    ]
    print()
    print(grad(" ╭──────────────────────────────────────────╮", C_CYAN, C_PINK))
    for line in logo:
        print(f" │{grad(line.center(42), C_CYAN, C_PINK)}│")
    subtitle = "====== ANYISP SNI HUNTER v6.0 ======".center(42)
    print(f" │{grad(subtitle, C_PINK, C_GOLD)}│")
    author = "★ MODDED BY FORIDUL ★".center(42)
    print(f" │{grad(author, C_GOLD, C_CYAN)}│")
    print(grad(" ╰──────────────────────────────────────────╯", C_PINK, C_CYAN))
    print(f"  \x1b[38;2;0;255;136m● MODE: PERSONAL UNLOCKED  \x1b[38;2;255;200;40m● ACCESS: LIFETIME (∞)\x1b[0m\n")

def clear_screen():
    os.system(_sec_string('ylfZnds=')) if os.name == _sec_string('2VTPldE=') else os.system(_sec_string('ylfP'))

def run_security_check(handler=None):
    return True

def first_time_activation(handler):
    clear_screen()
    show_logo()
    print(c(_sec_string('0F7QkMZM'), _sec_string('73Lur/0b6LXkfpy96m/1quhv9bPn')))
    print(c(_sec_string('zVLR'), f'Build: {CLIENT_BUILD}'))
    print(c(_sec_string('ykLdkg=='), _sec_string('7V7KlcpenLXtAZw=')) + c(_sec_string('zknZmcc='), handler.device_id))
    print(c(_sec_string('zVLR'), _sec_string('+l7SmIlP1JXaG/iZ31LfmYly+NzdVJyIwV6cnc1W1ZKJT9Pczl7I3MhY35naSJI=')))
    print()
    print(c(_sec_string('ykLdkg=='), _sec_string('+l7OisxJnKn7d4bc')) + c(_sec_string('3lPViMw='), SERVER_URL + f':{SERVER_PORT}'))
    again = input(c(_sec_string('0F7QkMZM'), _sec_string('o2jZjt9eztz8afDcylTOjsxYyMOJE8XTxxKG3A=='))).strip().lower()
    if again not in (_sec_string('0A=='), ''):
        print(c(_sec_string('217Y'), _sec_string('+VfZndpenJnNUsjc+n7uquxp46n7d5yVxxvIlMBInI/KSdWM3ReciMFe0tzbXpGO3FWS')))
        input(c(_sec_string('0F7QkMZM'), _sec_string('+UnZj9ob+ZLdXs7ShxU=')))
        sys.exit(1)
    print(c(_sec_string('ykLdkg=='), _sec_string('o3rfiMBN3YjAVdvShxU=')))
    handler.activate({_sec_string('2l7OisxJ44nbVw=='): SERVER_URL, _sec_string('2VTOiA=='): SERVER_PORT, _sec_string('3EjZo8FPyIza'): USE_HTTPS, _sec_string('3VLRmcZOyA=='): TIMEOUT})
    print(c(_sec_string('zknZmcc='), _sec_string('o3rfiMBN3YjMX5yP3FjfmdpI2onFV8Xd')))
    time.sleep(1)
    print(c(_sec_string('ykLdkg=='), f'Engine assigned by server: {handler.get_assigned_version().upper()}'))
    input(c(_sec_string('0F7QkMZM'), _sec_string('+UnZj9ob+ZLdXs7ShxU=')))

def run_assigned_engine(handler, version):
    if str(version).lower() == 'v5':
        mod = 'v5_engine'
    else:
        mod = 'v6_engine'
    try:
        engine = __import__(mod)
    except ImportError as e:
        print(c(_sec_string('217Y'), f'Could not load {str(version).upper()} engine: {e}'))
        input(c(_sec_string('0F7QkMZM'), 'Press Enter to exit...'))
        return
    engine.SERVER_DAYS_REMAINING = 99999
    try:
        engine.run_engine()
    finally:
        notify_scan_finished()

def make_activation_config():
    return {_sec_string('2l7OisxJ44nbVw=='): SERVER_URL, _sec_string('2VTOiA=='): SERVER_PORT, _sec_string('3EjZo8FPyIza'): USE_HTTPS, _sec_string('3VLRmcZOyA=='): TIMEOUT}

def try_refresh_activation(handler, attempts=2):
    """
    Re-activate this device against the server: mints a fresh session token and
    picks up the latest expiry / engine assignment. This is the no-reinstall
    recovery for revoked-then-reactivated licenses. Returns True on success.
    """
    for i in range(attempts):
        print(c(_sec_string('0F7QkMZM'), f'\n  [!] Refreshing activation from server ({i + 1}/{attempts})...'))
        try:
            handler.activate(make_activation_config())
            print(c(_sec_string('zknZmcc='), _sec_string('iRvns+JmnL3KT9WKyE/Vk8cbzpnPSdmPwV7Y0ols2ZDKVNGZiVndn8Ia')))
            return True
        except LicenseError as e:
            print(c(_sec_string('217Y'), f'  [X] Server said: {e}'))
            if i + 1 < attempts:
                again = input(c(_sec_string('0F7QkMZM'), _sec_string('iRuc3Ikb6I7QG92byFLSw4kTxdPHEobc'))).strip().lower()
                if again not in (_sec_string('0A=='), ''):
                    break
    return False

def _wipe_config(handler):
    """Remove the saved activation so a fresh one can be issued (config only)."""
    try:
        if handler.is_configured() and os.path.exists(handler.config_path):
            os.remove(handler.config_path)
    except Exception:
        pass
    try:
        if os.path.exists(handler.breach_queue_path):
            os.remove(handler.breach_queue_path)
    except Exception:
        pass

def handle_cli_command(handler):
    """scanner --refresh  /  scanner --reset  /  scanner --forced-refresh"""
    args = sys.argv[1:]
    if not args:
        return False
    cmd = args[0].lower().lstrip(_sec_string('hA=='))
    if cmd in (_sec_string('217Pmd0='), _sec_string('217VktpP3ZDF')):
        _wipe_config(handler)
        print(c(_sec_string('zknZmcc='), _sec_string('5lfY3MhYyJXfWsiVxlWcn8Ve3Y7MX5Lc+k/djt1S0puJXc6Z2lOcncpP1YrIT9WTxxWS0g==')))
        first_time_activation(handler)
        return True
    if cmd in (_sec_string('217ajsxI1A=='), _sec_string('214='), _sec_string('217Smd4='), _sec_string('z1TOn8xfkY7MXc6Z2lM='), _sec_string('216RncpP1YrIT9k=')):
        if not handler.is_configured():
            print(c(_sec_string('0F7QkMZM'), _sec_string('51Scj8hN2ZiJWt+IwE3diMBU0tzPVMmSzRWcrtxV0pXHXJyawEnPiIRP1ZHMG92f3VLKnd1S05KHFZI=')))
            first_time_activation(handler)
            return True
        print(c(_sec_string('ykLdkg=='), _sec_string('+17ajsxI1JXHXJydyk/VishP1ZPHG9qOxlacj8xJypnbFZLS')))
        if try_refresh_activation(handler, attempts=3):
            print(c(_sec_string('zknZmcc='), _sec_string('o3/TkswVnL3KT9WKyE/Vk8cbzpnPSdmPwV7Y3IQb1onaT5yO3FWc29pY3ZLHXs7biU/T3NpP3Y7dFQ==')))
        else:
            print(c(_sec_string('217Y'), _sec_string('o2nZmttez5SJXd2VxV7Y0olv1JmJSNmO317O3NpaxY+JT9SV2hvYmd9S35mJUs/cx1TI3MhYyJXfXpI=')))
            print(c(_sec_string('0F7QkMZM'), _sec_string('6lTSiMhYyNzpc92fwl7OjNtS0ZmbDojcgVPIiNlIhtOGT5KRzBT0ncpQ2Y7ZSdWRzAmJyIAb3ZLNG8+Zx1+ciMFSz9zNXsqVyl6cte0B')))
            print(c(_sec_string('ykLdkg=='), handler.device_id))
        return True
    return False

def notify_scan_finished():
    import shutil as _sh
    try:
        sys.stdout.write('\a\a\a')
        sys.stdout.flush()
    except Exception:
        pass
    if _sh.which('termux-vibrate'):
        try:
            subprocess.run(['termux-vibrate', '-d', '400'], capture_output=True)
        except Exception:
            pass
    if _sh.which('termux-notification'):
        try:
            subprocess.run(['termux-notification', '--title', 'ANYISP Scanner', '--content', 'Scan session completed! Results saved.'], capture_output=True)
        except Exception:
            pass

def view_results():
    candidates = [('V6.txt', 'V6 Results'), ('V4.txt', 'V5 Results')]
    existing = [(f, name) for f, name in candidates if os.path.exists(f) and os.path.getsize(f) > 0]
    clear_screen()
    show_logo()
    if not existing:
        print("  \x1b[38;2;255;60;60m[-] No scan results found yet. Run an engine scan first!\x1b[0m\n")
        input("  \x1b[38;2;0;240;255mPress Enter to return to menu...\x1b[0m")
        return
    for fname, name in existing:
        try:
            with open(fname, 'r', encoding='utf-8', errors='replace') as f:
                lines = [l.strip() for l in f if l.strip()]
        except Exception as e:
            print(f"  \x1b[38;2;255;60;60m[-] Error reading {fname}: {e}\x1b[0m")
            continue
        print(f"  \x1b[38;2;0;255;136m[+] File: {fname} ({name}) - Total {len(lines)} items\x1b[0m")
        preview = lines[:20]
        for idx, line in enumerate(preview, 1):
            print(f"    \x1b[38;2;0;240;255m{idx:02d}.\x1b[0m \x1b[38;2;240;240;240m{line}\x1b[0m")
        if len(lines) > 20:
            print(f"    \x1b[38;2;255;200;40m... and {len(lines) - 20} more entries in {fname}\x1b[0m")
        print()
    input("  \x1b[38;2;0;240;255mPress Enter to return to menu...\x1b[0m")

def export_results():
    candidates = ['V6.txt', 'V4.txt']
    found = [f for f in candidates if os.path.exists(f) and os.path.getsize(f) > 0]
    clear_screen()
    show_logo()
    if not found:
        print("  \x1b[38;2;255;60;60m[-] No result files found to export. Run a scan first!\x1b[0m\n")
        input("  \x1b[38;2;0;240;255mPress Enter to return to menu...\x1b[0m")
        return
    
    dest_dirs = [
        '/sdcard/Download',
        '/storage/emulated/0/Download',
        os.path.expanduser('~/storage/downloads'),
        os.path.expanduser('~/Downloads'),
        os.path.join(os.environ.get('USERPROFILE', ''), 'Downloads')
    ]
    target_dir = None
    for d in dest_dirs:
        if os.path.isdir(d):
            target_dir = d
            break
            
    if not target_dir:
        target_dir = os.path.abspath(os.path.dirname(__file__))
        
    print(f"  \x1b[38;2;0;255;136m[+] Target directory: {target_dir}\x1b[0m\n")
    import shutil as _sh
    copied = []
    for f in found:
        dest_file = os.path.join(target_dir, f)
        try:
            _sh.copy(f, dest_file)
            copied.append(dest_file)
        except Exception as e:
            print(f"  \x1b[38;2;255;60;60m[-] Error copying {f}: {e}\x1b[0m")
            
    if copied:
        print("  \x1b[38;2;0;255;136m[✓] Successfully exported files:\x1b[0m")
        for cp in copied:
            print(f"    \x1b[38;2;255;200;40m📁 {cp}\x1b[0m")
        print("\n  \x1b[38;2;240;240;240mYou can now open them in your file manager or VPN apps!\x1b[0m")
    input("\n  \x1b[38;2;0;240;255mPress Enter to return to menu...\x1b[0m")

def auto_setup_termux():
    try:
        curr_dir = os.path.abspath(os.path.dirname(__file__))
        prefix = os.environ.get('PREFIX', '')
        if prefix and os.path.isdir(os.path.join(prefix, 'bin')):
            for cmd_name in ('sni', 'snr'):
                bin_path = os.path.join(prefix, 'bin', cmd_name)
                try:
                    with open(bin_path, 'w', encoding='utf-8') as f:
                        f.write(f'#!/data/data/com.termux/files/usr/bin/bash\ncd "{curr_dir}" && python scanner.py "$@"\n')
                    os.chmod(bin_path, 0o755)
                except Exception:
                    pass
                
        bashrc = os.path.expanduser('~/.bashrc')
        try:
            existing = ""
            if os.path.exists(bashrc):
                with open(bashrc, 'r', encoding='utf-8', errors='ignore') as f:
                    existing = f.read()
            
            with open(bashrc, 'a', encoding='utf-8') as f:
                if "alias sni=" not in existing:
                    f.write(f"\nalias sni='cd \"{curr_dir}\" && python scanner.py'\n")
                if "alias snr=" not in existing:
                    f.write(f"alias snr='cd \"{curr_dir}\" && python scanner.py'\n")
        except Exception:
            pass
    except Exception:
        pass

def keyword_domain_finder():
    clear_screen()
    show_logo()
    print("  \x1b[38;2;0;255;136m[+] Keyword Domain Finder (Powered by crt.sh)\x1b[0m\n")
    keyword = input("  \x1b[38;2;0;240;255m❯ Enter keyword (e.g. robi): \x1b[0m").strip()
    if not keyword:
        return
    
    print(f"\n  \x1b[38;2;255;200;40m[*] Searching for domains containing '{keyword}'... Please wait.\x1b[0m")
    try:
        import urllib.request
        import json
        
        url = f"https://crt.sh/?q=%25{keyword}%25&output=json"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        res = urllib.request.urlopen(req, timeout=30)
        
        if res.getcode() == 200:
            data = json.loads(res.read())
            domains = set()
            for entry in data:
                name_value = entry.get('name_value', '')
                for domain in name_value.split('\n'):
                    domain = domain.strip().lower()
                    if not domain or '*' in domain:
                        continue
                    if keyword.lower() in domain:
                        domains.add(domain)
                        
            if not domains:
                print("  \x1b[38;2;255;60;60m[-] No domains found.\x1b[0m")
            else:
                print(f"  \x1b[38;2;0;255;136m[✓] Found {len(domains)} unique domains!\x1b[0m\n")
                filename = f"{keyword}_domains.txt"
                with open(filename, 'w', encoding='utf-8') as f:
                    for d in sorted(domains):
                        f.write(f"{d}\n")
                print(f"  \x1b[38;2;240;240;240m[i] Results saved to: {filename}\x1b[0m")
                
                preview = list(sorted(domains))[:10]
                for d in preview:
                    print(f"    - {d}")
                if len(domains) > 10:
                    print(f"    ... and {len(domains) - 10} more.")
        else:
             print(f"  \x1b[38;2;255;60;60m[-] Server returned status code: {res.getcode()}\x1b[0m")
    except Exception as e:
        print(f"\n  \x1b[38;2;255;60;60m[-] Error fetching domains: {e}\x1b[0m")
        print("  \x1b[38;2;240;240;240m[!] Hint: The server might be rate-limiting. Try a more specific keyword like 'robi.com.bd'\x1b[0m")
        
    input("\n  \x1b[38;2;0;240;255mPress Enter to return to menu...\x1b[0m")

def update_scanner():
    clear_screen()
    show_logo()
    print("  \x1b[38;2;0;255;136m[+] Updating ANYISP Scanner from GitHub...\x1b[0m\n")
    try:
        import subprocess
        result = subprocess.run(['git', 'pull'], capture_output=True, text=True)
        if result.returncode == 0:
            if "Already up to date." in result.stdout:
                print(f"  \x1b[38;2;0;240;255m{result.stdout.strip()}\x1b[0m")
            else:
                print(f"  \x1b[38;2;0;240;255m{result.stdout.strip()}\x1b[0m")
                print("\n  \x1b[38;2;0;255;136m[✓] Update successful! Please restart the scanner.\x1b[0m")
        else:
            print(f"  \x1b[38;2;255;60;60m[-] Update failed:\x1b[0m\n{result.stderr.strip()}")
    except Exception as e:
        print(f"  \x1b[38;2;255;60;60m[-] Error running git pull: {e}\x1b[0m")
    input("\n  \x1b[38;2;0;240;255mPress Enter to return to menu...\x1b[0m")

def main():
    auto_setup_termux()
    args = [a.lower() for a in sys.argv[1:]]
    if '--v5' in args or '-5' in args:
        run_assigned_engine(None, 'v5')
        return
    elif '--v6' in args or '-6' in args:
        run_assigned_engine(None, 'v6')
        return

    C_CYAN = (0, 240, 255)
    C_PINK = (255, 40, 160)

    while True:
        clear_screen()
        show_logo()
        card_top = " ╭───[ LAUNCH & UTILITIES ]─────────────────╮"
        card_bot = " ╰──────────────────────────────────────────╯"
        print(grad(card_top, C_CYAN, C_PINK))
        print(" │  \x1b[38;2;0;240;255m[1]\x1b[0m \x1b[38;2;240;240;240mV6 Engine (2026 Premium - Pro)      \x1b[0m│")
        print(" │  \x1b[38;2;255;100;200m[2]\x1b[0m \x1b[38;2;240;240;240mV5 Engine (Classic Stable)          \x1b[0m│")
        print(" │  \x1b[38;2;0;255;136m[3]\x1b[0m \x1b[38;2;240;240;240mView Scan Results (V6 / V4)         \x1b[0m│")
        print(" │  \x1b[38;2;255;200;40m[4]\x1b[0m \x1b[38;2;240;240;240mExport Results to Downloads         \x1b[0m│")
        print(" │  \x1b[38;2;140;180;255m[5]\x1b[0m \x1b[38;2;240;240;240mKeyword Domain Finder               \x1b[0m│")
        print(" │  \x1b[38;2;255;100;200m[6]\x1b[0m \x1b[38;2;240;240;240mUpdate Scanner (Git Pull)           \x1b[0m│")
        print(" │  \x1b[38;2;255;60;60m[0]\x1b[0m \x1b[38;2;240;240;240mExit Session                        \x1b[0m│")
        print(grad(card_bot, C_PINK, C_CYAN))
        print()
        ans = input("\x1b[38;2;0;240;255m❯ \x1b[38;2;255;200;40mChoose option \x1b[38;2;160;160;160m[0-6, default: 1]\x1b[38;2;0;240;255m: \x1b[0m").strip()
        if ans == '2':
            print(f"\n\x1b[38;2;0;255;136m[+] Launching V5 Engine with Lifetime Access...\x1b[0m\n")
            time.sleep(0.5)
            run_assigned_engine(None, 'v5')
        elif ans == '3':
            view_results()
        elif ans == '4':
            export_results()
        elif ans == '5':
            keyword_domain_finder()
        elif ans == '6':
            update_scanner()
        elif ans in ('0', 'q', 'exit'):
            print('Exiting...')
            return
        else:
            print(f"\n\x1b[38;2;0;255;136m[+] Launching V6 Engine with Lifetime Access...\x1b[0m\n")
            time.sleep(0.5)
            run_assigned_engine(None, 'v6')
if __name__ == _sec_string('9mTRncBV46M='):
    try:
        main()
    except KeyboardInterrupt:
        print(c(_sec_string('0F7QkMZM'), _sec_string('o37Eld1S0puHFZI=')))
        sys.exit(0)
    except Exception as e:
        print(c(_sec_string('217Y'), f'Fatal error: {e}'))
        input(c(_sec_string('0F7QkMZM'), _sec_string('+UnZj9ob+ZLdXs7ShxU=')))
        sys.exit(1)
