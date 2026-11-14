# macOS Installation Guide — Context Engineering for Cursor

This guide walks through installing and configuring all required tools on **macOS** (Apple Silicon `arm64` or Intel `x86_64`) for **Context Engineering for Cursor**.

For an overview of all course requirements, see the [Main Installation Guide](./install.md).

## Prerequisites

- macOS 13 (Ventura) or newer
- Terminal access (`Terminal.app` or `iTerm2`)
- Administrator permissions to install applications

---

## Step 1: Install Homebrew (If Not Already Installed)

[Homebrew](https://brew.sh/) is the standard package manager for macOS and simplifies installing Git, Python 3.12, and Cursor IDE.

Check whether Homebrew is already installed:

```bash
brew --version
```

If `brew` is not found, install it by running:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the post-install instructions printed in your terminal to add Homebrew to your `PATH` (on Apple Silicon Macs, this adds `/opt/homebrew/bin` to `~/.zprofile`).

---

## Step 2: Install Git (`2.30+`)

Check whether Git is installed:

```bash
git --version
```

If Git is missing or older than `2.30`, install or upgrade it via Homebrew (or Xcode Command Line Tools):

```bash
brew install git
```

Verify the installed version:

```bash
git --version
# Expected output: git version 2.30.0 or higher
```

---

## Step 3: Install Python 3 (`3.10+`, `3.12` Recommended)

All lab verification tests, context ring token audits, and the local `stdio` MCP server run on the Python 3 standard library (`3.10+` required, `3.12` recommended).

Check your current `python3` version:

```bash
python3 --version
```

If `python3` is not installed or is older than `3.10`, install Python 3.12 with Homebrew:

```bash
brew install python@3.12
```

Verify that `python3` and `unittest` are available:

```bash
python3 --version
python3 -m unittest --help > /dev/null && echo "Python unittest ready"
```

---

## Step 4: Install Cursor IDE (Latest Release)

Install Cursor IDE using Homebrew Cask or by downloading the universal `.dmg` installer directly from [cursor.com](https://cursor.com):

```bash
brew install --cask cursor
```

Alternatively:

1. Download the macOS installer from [https://cursor.com](https://cursor.com).
2. Open the downloaded `.dmg` file and drag **Cursor.app** into your `/Applications` folder.

### Configure Cursor IDE and Shell Command

1. Launch **Cursor** from `/Applications/Cursor.app` (or Spotlight).
2. Sign in to your Cursor account when prompted.
3. Open the Command Palette (`Cmd+Shift+P`), type **Shell Command: Install 'cursor' command in PATH**, and press `Enter`.
4. Open the Cursor Agent sidepane with `Cmd+I` and confirm the chat input and mode selector (`Shift+Tab` for Plan Mode) appear.

Verify that Cursor is installed:

```bash
ls -d /Applications/Cursor.app
cursor --version
```

*(Note: If you have not installed the `cursor` shell command in `PATH`, `/Applications/Cursor.app` is still detected automatically by the verification script.)*

---

## Step 5: Clone This Setup Repository and Run Verification

If you have not already cloned this setup repository, clone it and navigate to its root directory:

```bash
git clone https://github.com/kpassoubady/context-cursor-setup.git
cd context-cursor-setup
```

Run the pre-class verification script from [`quickstart-project/`](../quickstart-project/README.md):

```bash
python3 quickstart-project/verify_setup.py
```

Or run the macOS/Linux shell wrapper:

```bash
bash quickstart-project/verify.sh
```

Expected final output:

```text
SETUP VERIFICATION PASSED
```

---

## Troubleshooting (macOS)

- **`xcrun: error: invalid active developer path` when running `git` or `python3`:**
  Run `xcode-select --install` in Terminal to install the macOS Command Line Tools, or install `git` and `python@3.12` via Homebrew.
- **`cursor: command not found` in Terminal:**
  Open Cursor IDE, press `Cmd+Shift+P`, and run **Shell Command: Install 'cursor' command in PATH**, then open a new Terminal tab.
- **macOS Gatekeeper warning when opening Cursor:**
  Ensure you downloaded Cursor from [https://cursor.com](https://cursor.com) or via `brew install --cask cursor`, then right-click **Cursor.app** in `/Applications` and select **Open**.
- **Local `stdio` MCP server fails to start in Cursor:**
  Confirm `which python3` returns a valid Python 3.10+ interpreter and inspect **Output > MCP Logs** (`Cmd+Shift+U`) inside Cursor IDE.
