@echo off
setlocal
set "SCRIPT_DIR=%~dp0"

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    python "%SCRIPT_DIR%verify_setup.py"
    exit /b %ERRORLEVEL%
)

where python3 >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    python3 "%SCRIPT_DIR%verify_setup.py"
    exit /b %ERRORLEVEL%
)

echo [FAIL] Neither python nor python3 was found on PATH.
echo See install\install-win.md or install\install.md for installation instructions.
exit /b 1
