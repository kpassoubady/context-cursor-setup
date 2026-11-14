# Installation Guide — Context Engineering for Cursor

Complete these pre-class setup steps before attending **Context Engineering for Cursor**. Completing installation and verification ahead of time ensures you can spend the full 4-hour session on hands-on context engineering labs rather than environment setup.

## Course Outline

Review the [Course Outline](../catalog/Context-Engineering-for-Cursor-4-Hour-AM-PM-Outline.md) for session topics, learning outcomes, and schedule details.

## Required Tools and Versions

All hands-on exercises use a single technology stack based on the latest Cursor IDE and the Python 3 standard library:

| Category | Tool | Minimum Version | Purpose in Class |
| :--- | :--- | :--- | :--- |
| **AI Code Editor** | [Cursor IDE](https://cursor.com) | Latest stable release | Cursor Agent (`Cmd+I` / `Ctrl+I`), Plan Mode (`Shift+Tab`), `.cursor/rules/*.mdc`, `AGENTS.md`, `.cursor/skills/*/SKILL.md`, `.cursorignore`, `.cursor/mcp.json`, and the context ring breakdown tray |
| **Language Runtime** | [Python 3](https://www.python.org/downloads/) | `3.10+` (`3.12` recommended) | Runs all lab `unittest` suites, context ring token audits, and the local `stdio` Model Context Protocol (MCP) server using the Python standard library only |
| **Version Control** | [Git](https://git-scm.com/) | `2.30+` | Clones this setup repository and manages workspace files during class |

> **No third-party Python packages or external API keys required:** Every script, test suite, and local `stdio` MCP server used in this course relies strictly on the Python 3 standard library (`unittest`, `json`, `subprocess`, `pathlib`, `decimal`, `dataclasses`, `re`, and `fnmatch`). You do not need to install external `pip` packages or purchase third-party API keys.

## Operating-System Installation Guides

Follow the step-by-step installation guide for your operating system:

- **macOS:** [macOS Installation Guide](./install-mac.md)
- **Windows:** [Windows Installation Guide](./install-win.md)

## Cursor IDE Account and Configuration

1. **Sign in to Cursor IDE:** Launch Cursor and sign in with an active Cursor account so you can access Cursor Agent (`Cmd+I` on macOS, `Ctrl+I` on Windows/Linux) and Plan Mode (`Shift+Tab`).
2. **Optional `cursor` Shell Command:** Open the Command Palette (`Cmd+Shift+P` on macOS, `Ctrl+Shift+P` on Windows) and run **Shell Command: Install 'cursor' command in PATH** so you can open workspaces and check the CLI version from your terminal.
3. **Security & Privacy Note:** Never place live secrets, production credentials, or personal API tokens into workspace configuration files (`.cursor/mcp.json`, `.env`, or rule files). All course exercises use synthetic local fixtures.

## Verify Your Setup

After completing the installation guide for your operating system, run the standalone verification check in [`quickstart-project/`](../quickstart-project/README.md):

```bash
python3 quickstart-project/verify_setup.py
```

*(On Windows, if `python3` is registered as `python`, run `python quickstart-project/verify_setup.py`.)*

Confirm that the output ends with:

```text
SETUP VERIFICATION PASSED
```

## Day-of-Class Readiness

- **Before class:** Complete tool installation, sign in to Cursor IDE, and confirm `SETUP VERIFICATION PASSED` from `quickstart-project/verify_setup.py`.
- **At the start of class:** Your instructor will share access to the hands-on lab materials. You will open those exercises in Cursor IDE and verify that the Cursor Agent sidepane (`Cmd+I` / `Ctrl+I`) opens cleanly.
