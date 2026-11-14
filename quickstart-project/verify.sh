#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if command -v python3 >/dev/null 2>&1; then
    python3 "${SCRIPT_DIR}/verify_setup.py"
elif command -v python >/dev/null 2>&1; then
    python "${SCRIPT_DIR}/verify_setup.py"
else
    echo "[FAIL] Neither python3 nor python was found on PATH."
    echo "See install/install-mac.md or install/install.md for installation instructions."
    exit 1
fi
