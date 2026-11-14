# Windows Installation Guide — Context Engineering for Cursor

This guide walks through installing and configuring all required tools on **Windows 10/11** (`64-bit`) for **Context Engineering for Cursor**.

For an overview of all course requirements, see the [Main Installation Guide](./install.md).

## Prerequisites

- Windows 10 (build 19041+) or Windows 11 (64-bit)
- PowerShell or Windows Terminal
- Administrator permissions to install applications (Winget, Chocolatey, or standard installers)

---

## Step 1: Install Git for Windows (`2.30+`)

Check whether Git is already installed in PowerShell:

```powershell
git --version
```

If Git is not installed or is older than `2.30`, install it using **Winget** (built into Windows 10/11) or download the installer from [git-scm.com](https://git-scm.com/download/win):

```powershell
winget install --id Git.Git -e --source winget
```

*(Alternatively, with Chocolatey: `choco install git -y`.)*

Close and reopen PowerShell so your `PATH` refreshes, then verify:

```powershell
git --version
# Expected output: git version 2.30.0 or higher
```

---

## Step 2: Install Python 3 (`3.10+`, `3.12` Recommended)

All lab verification tests, context ring token audits, and the local `stdio` MCP server run on the Python 3 standard library (`3.10+` required, `3.12` recommended).

Check whether Python 3 is installed:

```powershell
python --version
```

If Python is not installed, opens the Microsoft Store stub, or reports a version older than `3.10`, install Python 3.12 via **Winget** or from [python.org/downloads/windows/](https://www.python.org/downloads/windows/):

```powershell
winget install --id Python.Python.3.12 -e --source winget
```

> **Important (Installer Checkbox):** If you use the graphical installer from `python.org`, check **"Add python.exe to PATH"** on the first screen before clicking **Install Now**.

Close and reopen PowerShell, then verify that Python and `unittest` work:

```powershell
python --version
python -m unittest --help
```

> **Tip (`python3` vs. `python` on Windows):** On Windows, the standard Python installer registers `python` and the `py` launcher (`py -3`). Where course instructions show `python3`, you can run either `python` or `python3` if an alias is configured. To prevent the Windows Store stub from intercepting `python3`, open **Settings > Apps > Advanced app settings > App execution aliases** and turn off the **App Installer** aliases for `python.exe` and `python3.exe` if they point to the Store stub.

---

## Step 3: Install Cursor IDE (Latest Release)

Install Cursor IDE using **Winget** or by downloading the Windows installer from [cursor.com](https://cursor.com):

```powershell
winget install --id Anysphere.Cursor -e --source winget
```

Alternatively:

1. Download the Windows installer from [https://cursor.com](https://cursor.com).
2. Run the installer executable and complete the setup wizard.

### Configure Cursor IDE and Shell Command

1. Launch **Cursor** from the Start Menu.
2. Sign in to your Cursor account when prompted.
3. Open the Command Palette (`Ctrl+Shift+P`), type **Shell Command: Install 'cursor' command in PATH**, and press `Enter`.
4. Open the Cursor Agent sidepane with `Ctrl+I` and confirm the chat input and mode selector (`Shift+Tab` for Plan Mode) appear.

Verify that the `cursor` command is reachable in a new PowerShell window:

```powershell
cursor --version
```

---

## Step 4: Clone This Setup Repository and Run Verification

If you have not already cloned this setup repository, clone it and navigate to its root directory:

```powershell
git clone https://github.com/kpassoubady/context-cursor-setup.git
cd context-cursor-setup
```

Run the pre-class verification script from [`quickstart-project/`](../quickstart-project/README.md):

```powershell
python quickstart-project/verify_setup.py
```

Or run the Windows batch wrapper:

```cmd
quickstart-project\verify.bat
```

Expected final output:

```text
SETUP VERIFICATION PASSED
```

---

## Troubleshooting (Windows)

- **`python` or `python3` opens the Microsoft Store instead of running Python:**
  Open **Settings > Apps > Advanced app settings > App execution aliases** and disable the `python.exe` and `python3.exe` aliases that point to **App Installer**, then ensure your Python 3.12 installation directory (`%LocalAppData%\Programs\Python\Python312\`) is on your user `PATH`.
- **`cursor` is not recognized in PowerShell:**
  Open Cursor IDE, press `Ctrl+Shift+P`, run **Shell Command: Install 'cursor' command in PATH**, and restart PowerShell. The verification script also checks standard Windows install paths (`%LocalAppData%\Programs\cursor\Cursor.exe`).
- **Local `stdio` MCP server fails to start in Lab 3.1 on Windows:**
  If your system registers Python as `python` rather than `python3`, set `"command": "python"` in `.cursor/mcp.json` during class and inspect **Output > MCP Logs** (`Ctrl+Shift+U`).
