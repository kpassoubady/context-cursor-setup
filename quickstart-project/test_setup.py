"""Unit tests validating local Python and Cursor context-engineering readiness."""

from __future__ import annotations

import fnmatch
import importlib
import json
import re
import subprocess
import sys
import unittest
from decimal import Decimal

sys.dont_write_bytecode = True

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

ECHO_MCP_SERVER_CODE = """\
import json
import sys

for raw in sys.stdin:
    msg = json.loads(raw)
    method = msg.get("method")
    msg_id = msg.get("id")
    if method == "initialize":
        resp = {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "protocolVersion": "2025-03-26",
                "serverInfo": {"name": "quickstart-mcp-check", "version": "1.0.0"},
                "capabilities": {"tools": {}},
            },
        }
        sys.stdout.write(json.dumps(resp) + "\\n")
        sys.stdout.flush()
    elif method == "tools/list":
        resp = {
            "jsonrpc": "2.0",
            "id": msg_id,
            "result": {
                "tools": [
                    {
                        "name": "ping_context",
                        "description": "Verify local stdio MCP transport",
                        "inputSchema": {"type": "object", "properties": {}},
                    }
                ]
            },
        }
        sys.stdout.write(json.dumps(resp) + "\\n")
        sys.stdout.flush()
        break
"""


class SetupReadinessTests(unittest.TestCase):
    """Verify the local Python environment supports all course lab mechanics."""

    def test_python_version_minimum(self) -> None:
        self.assertGreaterEqual(
            sys.version_info[:2],
            (3, 10),
            f"Python 3.10+ is required; found {sys.version.split()[0]}",
        )

    def test_required_stdlib_modules_import(self) -> None:
        for mod_name in REQUIRED_STDLIB_MODULES:
            with self.subTest(module=mod_name):
                mod = importlib.import_module(mod_name)
                self.assertIsNotNone(mod)

    def test_mdc_frontmatter_and_cursorignore_simulation(self) -> None:
        sample_mdc = (
            "---\n"
            "description: Scoped payment rule check\n"
            "globs: src/payments/**/*.py\n"
            "alwaysApply: false\n"
            "---\n"
            "Use integer cents and Decimal.\n"
        )
        match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", sample_mdc, flags=re.DOTALL)
        self.assertIsNotNone(match, "Failed to parse sample .mdc YAML frontmatter")
        assert match is not None
        frontmatter_text, body = match.groups()
        self.assertIn("alwaysApply: false", frontmatter_text)
        self.assertIn("Decimal", body)
        self.assertTrue(fnmatch.fnmatch("src/payments/processor.py", "src/payments/*.py"))
        self.assertEqual(Decimal("19.99") * 100, Decimal("1999.00"))

    def test_stdio_mcp_jsonrpc_roundtrip(self) -> None:
        init_req = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {"protocolVersion": "2025-03-26", "capabilities": {}},
        }
        list_req = {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}
        payload = json.dumps(init_req) + "\n" + json.dumps(list_req) + "\n"

        proc = subprocess.run(
            [sys.executable, "-c", ECHO_MCP_SERVER_CODE],
            input=payload,
            text=True,
            capture_output=True,
            timeout=10,
            check=True,
        )
        lines = [line.strip() for line in proc.stdout.splitlines() if line.strip()]
        self.assertEqual(len(lines), 2, f"Expected 2 JSON-RPC responses, got: {lines}")

        init_resp = json.loads(lines[0])
        list_resp = json.loads(lines[1])
        self.assertEqual(
            init_resp["result"]["serverInfo"]["name"],
            "quickstart-mcp-check",
        )
        tools = list_resp["result"]["tools"]
        self.assertEqual(len(tools), 1)
        self.assertEqual(tools[0]["name"], "ping_context")


if __name__ == "__main__":
    unittest.main(verbosity=2)
