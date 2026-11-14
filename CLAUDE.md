# Context Engineering for Cursor — Setup

Standalone pre-class setup repository for the 4-hour **Context Engineering for Cursor** course. Provides the detailed session outline, macOS and Windows installation guides, a student welcome and setup checklist, and a read-only Python verification quickstart.

## Tech Stack

- **Primary IDE:** Cursor IDE (latest release, with Cursor Agent, Plan Mode, Rules, Skills, `.cursorignore`, MCP, and Context Ring)
- **Language/Runtime:** Python 3.10+ (`3.12` recommended; standard library only: `unittest`, `json`, `subprocess`, `pathlib`, `decimal`, `dataclasses`, `re`, `fnmatch`)
- **Version Control:** Git 2.30+
- **Supported OS:** macOS and Windows

## Project Structure

| Path | Purpose |
| :--- | :--- |
| `Welcome-and-Setup-Guide-Context-Cursor.md` | Student-facing welcome message, pre-class checklist, and quick links (uses absolute GitHub URLs for PDF export) |
| `catalog/` | Authoritative detailed session outline (`Context-Engineering-for-Cursor-4-Hour-AM-PM-Outline.md`) |
| `install/` | Main (`install.md`), macOS (`install-mac.md`), and Windows (`install-win.md`) installation guides |
| `quickstart-project/` | Self-contained environment verification scripts (`verify_setup.py`, `test_setup.py`, `verify.sh`, `verify.bat`, `README.md`) |
| `scripts/` | Slide and diagram build/export helper scripts |
| `llm-context/` | Workspace context storage for LLM agents |

## Key Commands

```bash
# Run full pre-class environment verification (prints SETUP VERIFICATION PASSED on success)
python3 quickstart-project/verify_setup.py

# Run macOS/Linux verification wrapper
bash quickstart-project/verify.sh

# Run Windows verification wrapper
quickstart-project\verify.bat

# Run quickstart readiness unit tests directly
python3 -m unittest discover -s quickstart-project -v
```

## Conventions

- **Standalone Setup Rule:** This repository is distributed before students receive access to other course materials. Never name, link to, or instruct students to clone or open sibling course repositories.
- **Link Formatting:** Use absolute `https://github.com/kpassoubady/context-cursor-setup/...` URLs inside `Welcome-and-Setup-Guide-Context-Cursor.md` so links survive PDF export. Use relative links inside `README.md`, `install/`, and `quickstart-project/README.md`.
- **Zero External Dependencies:** Keep `quickstart-project/` limited to the Python 3 standard library with no live credentials or machine-specific paths.
- **Markdown Formatting:** Follow `.markdownlint.json` rules (heading increments `MD001` and trailing newline `MD047`).
