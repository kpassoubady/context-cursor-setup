#!/usr/bin/env python3
"""Pre-class environment verification script for Context Engineering for Cursor."""

from __future__ import annotations

import importlib
import os
import pathlib
import platform
import re
import shutil
import subprocess
import sys
import unittest

sys.dont_write_bytecode = True

MIN_PYTHON = (3, 10)
RECOMMENDED_PYTHON = (3, 12)
MIN_GIT = (2, 30)

REQUIRED_STDLIB_MODULES = (
    "dataclasses",
    "decimal",
    "fnmatch",
    "json",
    "pathlib",
    "re",
    "subprocess",
    "unittest",
)


def _parse_version_tuple(raw: str) -> tuple[int, int]:
    match = re.search(r"(\d+)\.(\d+)", raw)
    if not match:
        return (0, 0)
    return (int(match.group(1)), int(match.group(2)))


def check_python() -> tuple[bool, str]:
    current = sys.version_info[:2]
    version_str = sys.version.split()[0]
    if current < MIN_PYTHON:
        return (
            False,
            f"Python {version_str} detected (minimum required is 3.10; 3.12 recommended)",
        )
    rec_note = (
        ""
        if current >= RECOMMENDED_PYTHON
        else " (meets 3.10+ minimum; 3.12 recommended)"
    )
    return (True, f"Python {version_str}{rec_note}")


def check_stdlib_modules() -> tuple[bool, str]:
    missing: list[str] = []
    for mod_name in REQUIRED_STDLIB_MODULES:
        try:
            importlib.import_module(mod_name)
        except Exception:
            missing.append(mod_name)
    if missing:
        return (False, f"Missing standard library modules: {', '.join(missing)}")
    return (
        True,
        f"All {len(REQUIRED_STDLIB_MODULES)} required stdlib modules available "
        f"({', '.join(REQUIRED_STDLIB_MODULES)})",
    )


def check_git() -> tuple[bool, str]:
    git_bin = shutil.which("git")
    if not git_bin:
        return (False, "Git CLI not found on PATH (install Git 2.30+)")
    try:
        proc = subprocess.run(
            [git_bin, "--version"],
            text=True,
            capture_output=True,
            timeout=10,
            check=False,
        )
    except Exception as exc:
        return (False, f"Failed to execute git --version: {exc}")

    output = (proc.stdout or proc.stderr).strip()
    if proc.returncode != 0:
        return (False, f"git --version exited with code {proc.returncode}: {output}")

    parsed = _parse_version_tuple(output)
    if parsed < MIN_GIT:
        return (False, f"{output} detected (minimum required is Git 2.30+)")
    return (True, output)


def _candidate_cursor_paths() -> list[pathlib.Path]:
    home = pathlib.Path.home()
    candidates: list[pathlib.Path] = [
        pathlib.Path("/Applications/Cursor.app"),
        home / "Applications" / "Cursor.app",
        pathlib.Path("/usr/bin/cursor"),
        pathlib.Path("/usr/local/bin/cursor"),
    ]
    local_app_data = os.environ.get("LOCALAPPDATA")
    if local_app_data:
        candidates.append(
            pathlib.Path(local_app_data) / "Programs" / "cursor" / "Cursor.exe"
        )
    program_files = os.environ.get("ProgramFiles")
    if program_files:
        candidates.append(pathlib.Path(program_files) / "Cursor" / "Cursor.exe")
    return candidates


def check_cursor_ide() -> tuple[bool, str]:
    cursor_cli = shutil.which("cursor")
    cli_version = None
    if cursor_cli:
        try:
            proc = subprocess.run(
                [cursor_cli, "--version"],
                text=True,
                capture_output=True,
                timeout=10,
                check=False,
            )
            lines = [
                line.strip()
                for line in (proc.stdout or "").splitlines()
                if line.strip()
            ]
            if proc.returncode == 0 and lines:
                cli_version = lines[0]
        except Exception:
            cli_version = None

    found_paths = [p for p in _candidate_cursor_paths() if p.exists()]

    if cli_version:
        location_note = f" ({found_paths[0]})" if found_paths else f" ({cursor_cli})"
        return (True, f"Cursor IDE CLI version {cli_version}{location_note}")

    if cursor_cli:
        return (True, f"Cursor CLI found at {cursor_cli}")

    if found_paths:
        return (
            True,
            f"Cursor application found at {found_paths[0]} "
            "(optional: install 'cursor' command in PATH via Cmd+Shift+P / Ctrl+Shift+P)",
        )

    return (
        False,
        "Cursor IDE not detected on PATH or in standard application folders. "
        "Install Cursor from https://cursor.com",
    )


def check_unittest_and_stdio_mcp() -> tuple[bool, str]:
    quickstart_dir = pathlib.Path(__file__).resolve().parent
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=str(quickstart_dir), pattern="test_*.py")
    runner = unittest.TextTestRunner(stream=open(os.devnull, "w"), verbosity=0)
    result = runner.run(suite)
    if not result.wasSuccessful() or result.testsRun == 0:
        return (
            False,
            f"Quickstart unittest & stdio MCP smoke suite failed "
            f"(ran {result.testsRun}, failures={len(result.failures)}, errors={len(result.errors)})",
        )
    return (
        True,
        f"Ran {result.testsRun} readiness checks (unittest discovery, .mdc frontmatter, "
        "and local stdio JSON-RPC MCP round-trip): OK",
    )


def main() -> int:
    print("=" * 72)
    print("Context Engineering for Cursor — Pre-Class Environment Verification")
    print(f"Platform: {platform.system()} {platform.release()} ({platform.machine()})")
    print("=" * 72)

    checks = [
        ("Python Runtime (3.10+)", check_python),
        ("Python Standard Library", check_stdlib_modules),
        ("Git Version Control (2.30+)", check_git),
        ("Cursor IDE Installation", check_cursor_ide),
        ("Lab Runner & Local stdio MCP", check_unittest_and_stdio_mcp),
    ]

    all_passed = True
    for label, fn in checks:
        passed, detail = fn()
        status = "[PASS]" if passed else "[FAIL]"
        print(f"{status} {label}: {detail}")
        if not passed:
            all_passed = False

    print("-" * 72)
    print("Day-of-Class Interactive Checklist (verify inside Cursor IDE):")
    print("  1. Sign in to your active Cursor account inside Cursor IDE.")
    print("  2. Open Cursor Agent sidepane with Cmd+I (macOS) or Ctrl+I (Windows/Linux).")
    print("  3. Press Shift+Tab inside the Agent input to confirm Plan Mode is available.")
    print("=" * 72)

    if all_passed:
        print("SETUP VERIFICATION PASSED")
        return 0

    print("SETUP VERIFICATION FAILED")
    print(
        "Review install/install.md (or install/install-mac.md and install/install-win.md) "
        "to resolve any [FAIL] items above, then re-run this script."
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
