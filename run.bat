@echo off
title ANYISP Scanner Launcher
cd /d "%~dp0"

echo ====================================================
echo             ANYISP SCANNER LAUNCHER
echo ====================================================
echo.

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH!
    echo Please install Python 3.10+ and check "Add Python to PATH".
    echo.
    pause
    exit /b 1
)

echo Checking dependencies...
python -c "import aiohttp, requests, bs4, colorama, tqdm, websocket, termcolor, dns.resolver" >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] Some dependencies are missing. Installing from requirements.txt...
    python -m pip install -r requirements.txt
    echo.
)

echo Starting ANYISP Scanner...
python scanner.py %*
echo.
pause
