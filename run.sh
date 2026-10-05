#!/usr/bin/env bash
# ANYISP Scanner Linux / Termux Launcher

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
cd "$DIR"

# Prevent Android CPU from sleeping during background scans
if command -v termux-wake-lock >/dev/null 2>&1; then
    termux-wake-lock
    trap 'command -v termux-wake-unlock >/dev/null 2>&1 && termux-wake-unlock' EXIT INT TERM
fi

# Auto-configure global 'sni' shortcut in Termux
if [ -n "$PREFIX" ] && [ -d "$PREFIX/bin" ] && [ ! -f "$PREFIX/bin/sni" ]; then
    cat << 'EOF' > "$PREFIX/bin/sni"
#!/data/data/com.termux/files/usr/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
# Look up target script location
EOF
    cat << EOF >> "$PREFIX/bin/sni"
cd "$DIR" && python scanner.py "\$@"
EOF
    chmod +x "$PREFIX/bin/sni" 2>/dev/null
fi

echo "===================================================="
echo "           ANYISP SCANNER LAUNCHER (LINUX/TERMUX)"
echo "===================================================="
echo

if ! command -v python &> /dev/null; then
    echo "[ERROR] Python is not installed!"
    echo "In Termux, run: pkg install python"
    exit 1
fi

python -c "import aiohttp, requests, bs4, colorama, tqdm, websocket, termcolor, dns.resolver" >/dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "[!] Installing missing dependencies..."
    pip install -r requirements.txt
    echo
fi

echo "Starting ANYISP Scanner..."
python scanner.py "$@"
