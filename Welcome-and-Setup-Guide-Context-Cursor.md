# Welcome to Context Engineering for Cursor!

To ensure a smooth and productive learning experience, please complete the setup before class.

## 📋 Course Overview

Review the full [Course Outline](https://github.com/kpassoubady/context-cursor-setup/blob/main/catalog/Context-Engineering-for-Cursor-4-Hour-AM-PM-Outline.md) for session topics, learning outcomes, and schedule details.

**Context Engineering for Cursor** is a 4-hour hands-on course delivered in a single half-day cohort (AM or PM). Throughout the session, you will work inside the latest release of Cursor IDE using Cursor Agent (`Cmd+I` / `Ctrl+I`), Plan Mode (`Shift+Tab`), `.cursor/rules/*.mdc`, `AGENTS.md`, progressive Agent Skills (`.cursor/skills/*/SKILL.md`), `.cursorignore`, `.cursor/mcp.json`, the context ring breakdown tray, and the Python 3 standard library.

## 🛠️ Pre-Class Setup (Required)

Follow the [Main Installation Guide](https://github.com/kpassoubady/context-cursor-setup/blob/main/install/install.md) to install and configure the required tools before class:

| Category | Tool | Minimum Version | Purpose |
| :--- | :--- | :--- | :--- |
| **AI Code Editor** | Cursor IDE | Latest stable release | Cursor Agent (`Cmd+I` / `Ctrl+I`), Plan Mode (`Shift+Tab`), `.cursor/rules/*.mdc`, `AGENTS.md`, `.cursor/skills/*/SKILL.md`, `.cursorignore`, `.cursor/mcp.json`, and context ring auditing |
| **Language Runtime** | Python 3 | `3.10+` (`3.12` recommended) | Runs all lab `unittest` suites, context ring token audits, and the local `stdio` Model Context Protocol (MCP) server using the Python standard library only |
| **Version Control** | Git | `2.30+` | Clones this setup repository and manages workspace files during class |

Step-by-step operating-system installation guides are available for [macOS](https://github.com/kpassoubady/context-cursor-setup/blob/main/install/install-mac.md) and [Windows](https://github.com/kpassoubady/context-cursor-setup/blob/main/install/install-win.md).

Once your tools are installed, open the [Verification Quickstart Project](https://github.com/kpassoubady/context-cursor-setup/blob/main/quickstart-project/README.md) and run `python3 quickstart-project/verify_setup.py` (or `python quickstart-project/verify_setup.py` on Windows) from the setup repository root to verify your environment and confirm the output ends with `SETUP VERIFICATION PASSED`.

## ✅ Checklist Before Class

- [ ] Install Git (`2.30+`) and confirm `git --version` outputs `git version 2.30.0` or higher.
- [ ] Install Python 3 (`3.10+`, `3.12` recommended) and confirm `python3 --version` (or `python --version` on Windows) outputs `Python 3.10` or higher.
- [ ] Install the latest release of Cursor IDE and sign in with your active Cursor account.
- [ ] Install the `cursor` shell command in `PATH` from the Cursor Command Palette (`Cmd+Shift+P` on macOS or `Ctrl+Shift+P` on Windows: **Shell Command: Install 'cursor' command in PATH**) and verify `cursor --version`.
- [ ] Clone this setup repository: `git clone https://github.com/kpassoubady/context-cursor-setup.git` and change into `context-cursor-setup`.
- [ ] Run `python3 -m unittest discover -s quickstart-project -v` and confirm all 4 readiness unit tests report `OK`.
- [ ] Run `python3 quickstart-project/verify_setup.py` (or `python quickstart-project/verify_setup.py` on Windows) and confirm it prints `SETUP VERIFICATION PASSED`.

## 📚 Quick Links

| Resource | Link |
| :--- | :--- |
| **Course Catalog** | [Context-Engineering-for-Cursor-4-Hour-AM-PM-Outline.md](https://github.com/kpassoubady/context-cursor-setup/blob/main/catalog/Context-Engineering-for-Cursor-4-Hour-AM-PM-Outline.md) |
| **Installation Guide** | [install/install.md](https://github.com/kpassoubady/context-cursor-setup/blob/main/install/install.md) |
| **macOS Installation Guide** | [install/install-mac.md](https://github.com/kpassoubady/context-cursor-setup/blob/main/install/install-mac.md) |
| **Windows Installation Guide** | [install/install-win.md](https://github.com/kpassoubady/context-cursor-setup/blob/main/install/install-win.md) |
| **Verification Quickstart Project** | [quickstart-project/README.md](https://github.com/kpassoubady/context-cursor-setup/blob/main/quickstart-project/README.md) |

## 🆘 Need Help?

If you encounter any issues during setup, please don't hesitate to reach out before the training day.

Looking forward to seeing you in class! 🚀
