# Context Engineering for Cursor

Duration: 4 hours per cohort (AM and PM cohorts, 1 day)
Audience: Developers working in AI-assisted coding environments
Prerequisites: Familiarity with LLM concepts and terminology, basic experience with Cursor or a comparable AI development tool, and a working understanding of the Model Context Protocol (MCP)

## Delivery Model

| | Day 1 |
|---|---|
| **Morning Cohort** | Session 1 (AM) |
| **Afternoon Cohort** | Session 1 (PM, repeated) |

The instructor delivers the exact same 4-hour session twice in one day: once to the morning cohort and once as a direct repeat to the afternoon cohort. Each topic pairs a Concept and Demo block with a self-contained Breakout Lab so learners can apply each context engineering pattern immediately.

## Course Overview

As AI coding agents become more autonomous, the bottleneck in software development has shifted from syntax to context engineering. This half-day course covers environment orchestration in Cursor, moving from manual prompting and `@`-mentions to structured `.cursor/rules/*.mdc` hierarchies, `AGENTS.md`, progressive Agent Skills, `.cursorignore` boundaries, and `.cursor/mcp.json` integrations. Participants then orchestrate multi-file work using Cursor Agent, Plan Mode, isolated Subagents, and Checkpoints, and finish by diagnosing context bloat and context rot with the context ring breakdown tray.

## Main Topics Covered

- From chat to agency, balancing explicit `@`-mentions with Agentic Search, and progressive context loading with Agent Skills and Custom Modes
- Four-tier rule architectures using `.cursor/rules/*.mdc`, User Rules, Team Rules, and `AGENTS.md`
- Deep retrieval with Instant Grep, exclusion boundaries with `.cursorignore`, and external data connections with `.cursor/mcp.json`
- Orchestrating Cursor Agent (`Cmd+I` / `Ctrl+I`), Plan Mode (`Shift+Tab`), foreground and background Subagents, and Checkpoints
- Auditing token allocation in the context ring breakdown tray, managing context rot via automatic compaction, and iteratively refining rules

## Learning Outcomes

After this course, participants will be able to:

- Architect a multi-layered context strategy using `.cursor/rules/*.mdc` frontmatter, `AGENTS.md`, and progressive Agent Skills
- Connect Cursor Agent to external tools and data sources through `.cursor/mcp.json`
- Minimize context rot in long-running sessions using Plan Mode, Subagent context isolation, automatic summarization, and Checkpoints
- Tune repository discovery and exclusion boundaries with `.cursorignore` and Instant Grep
- Diagnose token allocation and rule activation failures using the context ring breakdown tray

## Project Context and Tools

Labs run inside the latest release of Cursor IDE against a shared multi-module sample repository. Participants configure `.cursor/rules/*.mdc`, `AGENTS.md`, `.cursor/skills/*/SKILL.md`, `.cursorignore`, and `.cursor/mcp.json`, and inspect live token consumption in Cursor Agent using the context ring breakdown tray.

## Day 1: Context Engineering for Cursor

### Welcome and Environment Check

Verify that every participant is running the latest Cursor IDE release, has the shared lab repository open, and can open the Cursor Agent sidepane with `Cmd+I` (Mac) or `Ctrl+I` (Windows and Linux).

### 1. From Chat to Agency and Agent Skills

Manual single-shot prompting breaks down on multi-file engineering tasks because the model needs the right environment state on every turn. This block contrasts explicit `@`-mentions (`@file`, `@folder`, `@Terminals`, `@Chats`, `@Commit`, `@Branch`) with Agentic Search, where Cursor Agent discovers relevant files on its own when the exact path is unknown. It then introduces Agent Skills (`.cursor/skills/<name>/SKILL.md`), an open standard that keeps base context lean by loading specialized workflows, scripts, and references only when needed, alongside Custom Modes (`Option+Enter` on Mac or `Alt+Enter` on Windows) to keep a skill active across an entire session.

### Breakout 1: Lab 1.1: Progressive Context with `@`-Mentions and Agent Skills

Participants compare an over-stuffed `@`-mention prompt against a targeted prompt paired with a project skill in `.cursor/skills/`. They invoke the skill with `/` for a single turn, promote it to a Custom Mode for multi-turn persistence, and verify that the skill stays scoped without bloating unrelated tasks.

Lab 1.1 Outcome: A working `.cursor/skills/` package invoked on demand and toggled as a Custom Mode in the sample repository.

### 2. Modern Rule Architectures

Large language models do not retain memory between completions, so persistent project guidance must live in structured rules injected at the start of the model context. This block covers Cursor's four rule tiers: Project Rules in `.cursor/rules/*.mdc` (noting that plain `.md` files in `.cursor/rules/` are ignored), User Rules in global Cursor settings, Team Rules managed from the dashboard, and `AGENTS.md` as a plain-markdown alternative. The demo walks through the three YAML frontmatter fields (`alwaysApply`, `description`, and `globs`) that map to Always Apply, Apply Intelligently, Apply to Specific Files, and Apply Manually (`@rule-name`), and shows how to write rules that enforce verification steps and block deprecated patterns.

### Breakout 2: Lab 2.1: Authoring `.cursor/rules/*.mdc` and `AGENTS.md`

Participants refactor an unstructured set of instructions into scoped `.cursor/rules/*.mdc` files using glob patterns, intelligent descriptions, and a root `AGENTS.md` file. They test that file-scoped rules attach only when matching files enter context and that verification rules prompt Cursor Agent to run tests after edits.

Lab 2.1 Outcome: A multi-tier `.cursor/rules/*.mdc` and `AGENTS.md` configuration verified across matching and non-matching files.

### 3. Deep Retrieval, Instant Grep, and MCP Integration

Reliable agent execution depends on keeping noisy or sensitive files out of retrieval while connecting live external context through the Model Context Protocol (MCP). This block explains how Cursor's Instant Grep builds and queries a local search index without uploading file paths or code to store search embeddings, and how `.cursorignore` (including Hierarchical Cursor Ignore and Global ignore files) blocks sensitive or generated paths from Agent, Tab, and `@`-mentions while respecting `.gitignore` and default ignores. It then covers MCP configuration via Customize > MCPs, `.cursor/mcp.json`, and `~/.cursor/mcp.json` across `stdio`, `SSE`, and `Streamable HTTP` transports, including Tools, Prompts, Resources, Roots, Elicitation, and MCP Apps.

### Breakout 3: Lab 3.1: Configuring `.cursorignore` and `.cursor/mcp.json`

Participants configure `.cursorignore` to exclude secrets and large generated directories from Agent discovery, while noting the boundary that terminal commands and MCP tools are not blocked by `.cursorignore`. They then register a local `stdio` MCP server in `.cursor/mcp.json` and query live external context directly from Cursor Agent.

Lab 3.1 Outcome: A tested `.cursorignore` policy and a working `.cursor/mcp.json` integration supplying live external data to Cursor Agent.

### 4. Orchestrating Cursor Agent, Plan Mode, and Subagents

Complex multi-file changes fail when an agent jumps straight into editing or fills its primary context window with noisy search and browser output. This block demonstrates Cursor Agent (`Cmd+I` / `Ctrl+I`) across its three core components (Instructions, Tools, and Model) and introduces Plan Mode (`Shift+Tab`), where the agent researches the codebase, asks clarifying questions, and produces an editable Markdown plan before building. It then shows how Cursor isolates noisy intermediate work into Subagents (including the built-in `Explore` and `Browser` subagents plus custom foreground and background subagents) and how automatic Checkpoints let developers preview and restore workspace files without erasing conversation history.

### Breakout 4: Lab 4.1: Plan Mode, Subagent Isolation, and Checkpoints

Participants tackle a multi-file feature refactor by switching to Plan Mode (`Shift+Tab`), refining the generated Markdown plan, saving it to the workspace, and executing it with Cursor Agent. Midway through, they trigger an intentional regression, restore the previous Checkpoint from the chat timeline, and observe how `Explore` keeps intermediate search output out of the main thread.

Lab 4.1 Outcome: A saved implementation plan executed via Cursor Agent, with a verified Checkpoint rollback and clean main-thread context.

### 5. Debugging Context and Managing Context Rot

Even with large context windows, model recall degrades as token counts climb, a failure mode known as context rot. This block shows how Cursor automatically compresses older turns into a summary when the context window nears capacity, and how to inspect exact token allocation using the context ring next to the prompt input. Clicking the ring opens the breakdown tray across eight categories: System prompt, Tools, Rules, Skills, MCP, Subagents, Summarized conversation, and Conversation. Participants learn a repeatable refinement loop for auditing which rules, MCP catalogs, or tool outputs caused a failure and tightening those artifacts before retrying.

### Breakout 5: Lab 5.1: Auditing the Context Ring Breakdown Tray and Refining Rules

Participants run a failing multi-turn agent task, open the context ring breakdown tray to identify which token categories dominated the window, and trim oversized rules and redundant attachments. They re-run the task and verify improved accuracy and lower token overhead.

Lab 5.1 Outcome: A before-and-after context ring audit and refined `.cursor/rules/*.mdc` configuration that eliminates the reproduced failure.

Day 1 Deliverable: A configured Cursor project with `.cursor/rules/*.mdc`, `AGENTS.md`, a `.cursor/skills/` package, `.cursorignore`, `.cursor/mcp.json`, a workspace plan, and a context ring audit.

### Session Breakdown Table

| Topic | Duration |
|---|---|
| Welcome and Environment Check | 5 min |
| 1. From Chat to Agency and Agent Skills | 25 min |
| Breakout 1: Lab 1.1: Progressive Context with `@`-Mentions and Agent Skills | 15 min |
| 2. Modern Rule Architectures | 25 min |
| Breakout 2: Lab 2.1: Authoring `.cursor/rules/*.mdc` and `AGENTS.md` | 15 min |
| Bio Break 1 | 10 min |
| Kahoot 1 | 10 min |
| 3. Deep Retrieval, Instant Grep, and MCP Integration | 25 min |
| Breakout 3: Lab 3.1: Configuring `.cursorignore` and `.cursor/mcp.json` | 15 min |
| 4. Orchestrating Cursor Agent, Plan Mode, and Subagents | 25 min |
| Breakout 4: Lab 4.1: Plan Mode, Subagent Isolation, and Checkpoints | 15 min |
| Bio Break 2 | 10 min |
| Kahoot 2 | 10 min |
| 5. Debugging Context and Managing Context Rot | 20 min |
| Breakout 5: Lab 5.1: Auditing the Context Ring Breakdown Tray and Refining Rules | 15 min |
| **Total** | **4 hours** |

## Documentation Currency

Reviewed against Cursor and Anthropic documentation on 2026-11-13. Cursor changes over time; the instructor should verify command names and feature behavior against current documentation before each delivery. This outline assumes the latest Cursor release as of 2026-11-13 and avoids pinning an older tool version unless a lab depends on a specific release.

- [Cursor Docs: Overview (Cursor Agent)](https://cursor.com/docs/agent/overview)
- [Cursor Docs: Prompting agents](https://cursor.com/docs/agent/prompting)
- [Cursor Docs: Plan Mode](https://cursor.com/docs/agent/plan-mode)
- [Cursor Docs: Rules](https://cursor.com/docs/rules)
- [Cursor Docs: Agent Skills](https://cursor.com/docs/skills)
- [Cursor Docs: Subagents](https://cursor.com/docs/subagents)
- [Cursor Docs: Search](https://cursor.com/docs/agent/tools/search)
- [Cursor Docs: Ignore File](https://cursor.com/docs/reference/ignore-file)
- [Cursor Docs: Model Context Protocol (MCP)](https://cursor.com/docs/mcp)
- [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)

