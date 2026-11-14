# Verification Quickstart — Context Engineering for Cursor

Use this self-contained verification project to confirm that your machine is ready for **Context Engineering for Cursor** before class begins.

The verification suite is safe, read-only, and requires zero external packages or API keys.

## What This Verification Checks

### Automated Pre-Class Checks (`verify_setup.py`)

1. **Python 3 Runtime (`3.10+`, `3.12` recommended):** Verifies that your Python interpreter meets the version requirement for all hands-on exercises.
2. **Python Standard Library Modules:** Confirms that `unittest`, `json`, `subprocess`, `pathlib`, `decimal`, `dataclasses`, `re`, and `fnmatch` import cleanly.
3. **Git (`2.30+`):** Confirms that `git` is installed and accessible on your `PATH`.
4. **Cursor IDE Installation:** Checks that Cursor IDE is installed in your standard application folder or via the `cursor` CLI on `PATH`.
5. **Lab Test Runner & Local `stdio` MCP Transport:** Runs the local `unittest` suite (`test_setup.py`) to verify `.cursor/rules/*.mdc` frontmatter parsing, `.cursorignore` glob matching, and a live `stdio` JSON-RPC 2.0 Model Context Protocol (`initialize` and `tools/list`) round-trip over `subprocess`.

### Day-of-Class Interactive Checks

Because interactive IDE authentication cannot be verified headlessly before class, confirm these three items inside Cursor IDE after running the script:

1. Sign in to your active Cursor account inside Cursor IDE.
2. Open the Cursor Agent sidepane with `Cmd+I` (macOS) or `Ctrl+I` (Windows/Linux).
3. Press `Shift+Tab` in the Cursor Agent prompt input to confirm **Plan Mode** is available.

---

## How to Run the Verification

From the root of this setup repository, run the verification script for your platform:

### Option 1: Direct Python Command (macOS, Windows, Linux)

```bash
python3 quickstart-project/verify_setup.py
```

*(On Windows PowerShell or Command Prompt where Python is registered as `python`, run `python quickstart-project/verify_setup.py`.)*

### Option 2: OS Wrapper Scripts

- **macOS / Linux:**

  ```bash
  bash quickstart-project/verify.sh
  ```

- **Windows (Command Prompt or PowerShell):**

  ```cmd
  quickstart-project\verify.bat
  ```

### Option 3: Run the `unittest` Suite Directly

```bash
python3 -m unittest discover -s quickstart-project -v
```

---

## Expected Output

When all required pre-class checks pass, `verify_setup.py` exits with status code `0` and ends with the success marker:

```text
========================================================================
Context Engineering for Cursor — Pre-Class Environment Verification
Platform: ...
========================================================================
[PASS] Python Runtime (3.10+): Python 3.12.x
[PASS] Python Standard Library: All 8 required stdlib modules available (dataclasses, decimal, fnmatch, json, pathlib, re, subprocess, unittest)
[PASS] Git Version Control (2.30+): git version 2.x.x
[PASS] Cursor IDE Installation: Cursor IDE CLI version ...
[PASS] Lab Runner & Local stdio MCP: Ran 4 readiness checks (unittest discovery, .mdc frontmatter, and local stdio JSON-RPC MCP round-trip): OK
------------------------------------------------------------------------
Day-of-Class Interactive Checklist (verify inside Cursor IDE):
  1. Sign in to your active Cursor account inside Cursor IDE.
  2. Open Cursor Agent sidepane with Cmd+I (macOS) or Ctrl+I (Windows/Linux).
  3. Press Shift+Tab inside the Agent input to confirm Plan Mode is available.
========================================================================
SETUP VERIFICATION PASSED
```

If any check prints `[FAIL]`, follow the instructions in [`../install/install.md`](../install/install.md), [`../install/install-mac.md`](../install/install-mac.md), or [`../install/install-win.md`](../install/install-win.md) and re-run the script until `SETUP VERIFICATION PASSED` appears.
