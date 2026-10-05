# ANYISP Scanner (V5 & V6 Engine) - Personal Unlocked Edition

Universal SNI, CIDR, Reverse IP, Proxy, and Anti-DPI Bug Scanner.

> **Status:** 🔓 **Personal Mode Active**  
> Device ID verification and server license checks are completely disabled. Unlimited lifetime access granted.

---

## 📁 File Structure

```text
E:\New folder\
├── scanner.py          # Main entrypoint & personal launcher
├── v5_engine.py        # V5 Engine (Classic Stable)
├── v6_engine.py        # V6 Engine (2026 Premium)
├── requirements.txt    # Python dependencies
├── run.bat             # 1-click Windows launcher
├── run.sh              # 1-click Linux / Termux launcher
└── security\
    ├── __init__.py     # Security package initializer
    ├── core.py         # Hardware binding & security core (bypassed)
    └── license.py      # License validation (bypassed)
```

---

## 🚀 How to Run

### Windows:
1. Double click [`run.bat`](file:///E:/New%20folder/run.bat) (it will automatically install dependencies on first run).
2. Or open PowerShell / CMD in this folder:
   ```bash
   pip install -r requirements.txt
   python scanner.py
   ```

### Android (Termux):
```bash
pkg update && pkg install python git -y
pip install -r requirements.txt
bash run.sh
```
> **Tip:** Once launched, select option `[5]` to enable the `sni` command. From then on, you can just type `sni` anywhere in Termux!

---

## ⚡ New Features & Termux Optimizations

* 🔋 **Termux Wake-Lock:** Automatically keeps Android CPU awake during long port/host scans so your phone doesn't kill the connection when the screen turns off.
* ⚡ **Global `sni` Command:** Launch the scanner from anywhere in Termux by simply typing `sni`.
* 📁 **Export to `/sdcard/Download`:** Easily export `V6.txt` / `V4.txt` scan results directly to your phone's Download folder for one-tap import into HTTP Custom, NapsternetV, or V2ray apps.
* 📄 **In-Menu Result Viewer:** View top live hostnames and scan totals right inside the launcher without leaving the terminal.
* 🔔 **Sound & Vibration Bell:** Emits audio bells and Termux vibrations when a scan completes.

---

## ⚙️ Quick Launch Commands

| Command | Description |
| :--- | :--- |
| `sni` | Global one-word launch from anywhere in Termux |
| `python scanner.py` | Launches interactive menu (Choose V6, V5, or Utilities) |
| `python scanner.py --v6` | Directly launches V6 Engine (2026 Premium) |
| `python scanner.py --v5` | Directly launches V5 Engine (Classic) |
| `python v6_engine.py` | Directly runs V6 Engine without launcher |
| `python v5_engine.py` | Directly runs V5 Engine without launcher |

