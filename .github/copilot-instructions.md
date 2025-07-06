# GitHub Copilot Instructions

## Project Awareness & Context
- Always read `PLANNING.md` at the start of a new conversation to understand the project's architecture, goals, style, and constraints.
- Check `TASK.md` before starting a new task. If the task isn't listed, add it with a brief description and today's date.
- Use consistent naming conventions, file structure, and architecture patterns as described in `PLANNING.md`.
- Use venv_linux (the virtual environment) whenever executing Python commands, including for unit tests.

## Code Structure & Modularity
- Never create a file longer than 500 lines of code. If a file approaches this limit, refactor by splitting it into modules or helper files.
- Organize code into clearly separated modules, grouped by feature or responsibility.
  For agents this looks like:
    - `agent.py` - Main agent definition and execution logic 
    - `tools.py` - Tool functions used by the agent 
    - `prompts.py` - System prompts
- Use clear, consistent imports (prefer relative imports within packages).
- Use python_dotenv and load_env() for environment variables.

## Testing & Reliability
- Always create Pytest unit tests for new features (functions, classes, routes, etc).
- After updating any logic, check whether existing unit tests need to be updated. If so, do it.
- Tests should live in a `/tests` folder mirroring the main app structure.
  - Include at least:
    - 1 test for expected use
    - 1 edge case
    - 1 failure case

## Task Completion
- Mark completed tasks in `TASK.md` immediately after finishing them.
- Add new sub-tasks or TODOs discovered during development to `TASK.md` under a "Discovered During Work" section.

# Robocorp RCC Instructions – Style & Convention Guide

> **Audience**: Engineers, SREs, and technical writers who craft READMEs, `AGENTS.md`, CI scripts, or runbooks for projects that rely on **Robocorp RCC** for environment management and automation.
>
> **Why it matters**: Precise, reproducible instructions shorten build times, reduce on‑call noise, and keep distributed teams in sync.

---

## 1  Voice & Tone

| Guideline       | ✅ Good                                 | 🚫 Avoid                 |
| --------------- | -------------------------------------- | ------------------------ |
| **Voice**       | Active, directive                      | Passive or speculative   |
| **Mood**        | Imperative (“Run `rcc run`…”)          | Questions (“Should I…?”) |
| **Length**      | Concise (≤ 120 chars)                  | Paragraphs of back‑story |
| **Perspective** | 2nd‑person or subject‑less imperatives | 1st‑person (“I will…”)   |

---

## 2  Instruction Anatomy

```
# ► Purpose         (1 line — what automation or env this touches)
# ► Command         (single RCC or shell command)
# ► Flags/Options   (bullet list; order by priority)
# ► Constraints     (optional — version pins, offline mode, etc.)
# ► Example Output  (optional, trimmed)
```

```bash
# Purpose: Build frozen holotree after editing conda.yaml
# Command: rcc holotree vars
# Constraints:
#   * Must run from repo root
#   * Internet required on first build only
# Example Output:
#   Holotree ID 035f… ready ✅
```

> **Tip**: Use distinct markers (`Purpose:`, `Command:`) so readers — and future parsers — can reliably locate each part.

---

## 3  Formatting Conventions

* **Markdown headings** (`##`) for major sections; keep hierarchy shallow.
* **Code fences** `bash … ` or `yaml … ` for all commands and config snippets.
* **One command ≠ one block**: break up long workflows into atomic, copy‑pasta‑safe steps.

---

## 4  Style Rules

1. **Start with an action verb**: *Run*, *Build*, *Freeze*, *Export*.
2. **Specify singular intent**; avoid chains like “Run X **and** Y **then** Z…”.
3. **Declare environment files explicitly** (`conda.yaml`, `holotree.json`).
4. **Pin versions** in samples; use placeholders (`<VERSION>`) only when truly variable.
5. **Prefer present tense** (**“Run”** not **“Running”**).
6. **Reference paths relative to repo root**; avoid `$HOME` unless universal.
7. **Document offline/air‑gapped modes** if supported.
8. **Never commit secrets** — demonstrate with `REDACTED` or `<TOKEN>`.

---

## 5  Naming & Structure Conventions

| Entity                        | Pattern                | Example                    |
| ----------------------------- | ---------------------- | -------------------------- |
| Holotree export               | `holotree-<date>.json` | `holotree-2025-07-03.json` |
| Tasks section in `robot.yaml` | Title‑case verb phrase | `Build Environment`        |
| Shell scripts                 | `kebab-case.sh`        | `start-consumers.sh`       |
| Env variables                 | `UPPER_SNAKE`          | `RCC_CONFIG_FILE`          |

---

## 6  Examples

### ✅ Good

```bash
# Purpose: Run unit tests inside RCC sandbox
# Command: rcc task testrun
```

### 🚫 Bad

```bash
# maybe tests?
rcc task testrun || true
```

---

## 7  Checklist Before Merge

* [ ] Action verb present
* [ ] Command tested in a fresh clone
* [ ] Version pins / constraints clear
* [ ] Offline considerations noted (if any)
* [ ] Secrets redacted or mocked

---

## 8  Reference Links

* RCC README → [https://github.com/robocorp/rcc](https://github.com/robocorp/rcc)
* RCC Workflow Guide → [https://robocorp.com/docs/rcc/workflow](https://robocorp.com/docs/rcc/workflow)
* Robocorp Tasks Library → [https://pypi.org/project/robocorp-tasks/](https://pypi.org/project/robocorp-tasks/)
* Holotree Concept → [https://robocorp.com/docs/rcc/holotree](https://robocorp.com/docs/rcc/holotree)

---

### Change Log

| Version | Date       | Author       | Notes                                                 |
| ------- | ---------- | ------------ | ----------------------------------------------------- |
| 2.0     | 2025‑07‑03 | Joshua Yorko | Reworked for pure RCC focus; removed Codex references |

## File and Folder Creation
- All files and folders created should be placed in `EXECUTED_PRPS/{feature_name}/`.

## MCP (Model Context Protocol) Data Presentation
- Always present data returned by the MCP (such as lists, collections, or sets of items) in a Markdown table format for easy readability.
- If the data is a list of items, objects, or any structured collection, use a table with clear headers and rows for each item.
- Avoid presenting lists or itemized data as plain bullet points or inline text—prefer tables for clarity.
- Ensure tables are formatted for copy-paste and quick scanning.

## Documentation & Explainability
- Update `README.md` when new features are added, dependencies change, or setup steps are modified.
- Comment non-obvious code and ensure everything is understandable to a mid-level developer.
- When writing complex logic, add an inline `# Reason:` comment explaining the why, not just the what.

## AI Behavior Rules
- Never assume missing context. Ask questions if uncertain.
- Never hallucinate libraries or functions – only use known, verified Python packages.
- Always confirm file paths and module names exist before referencing them in code or tests.
- Never delete or overwrite existing code unless explicitly instructed to or if part of a task from `TASK.md`.

---
## PRP Workflow Integration
- Use `.github/prompts/generate-prp.prompt.md` to generate PRPs with full context and validation loops.
- Use `.github/prompts/execute-prp.prompt.md` to execute PRPs and follow the implementation and validation process.
- Reference `PRPs/ai_docs/` for context-specific documentation, patterns, and troubleshooting.
- All PRPs must include a "Validation Loop" section with Level 1 (syntax/style), Level 2 (unit tests), and Level 3 (integration/manual) gates.
- Use `PRPs/scripts/validation_runner.py` to automate validation gates.
- Ensure all referenced files and links in PRPs and docs are valid and up to date.
- Update `README.md` and `docs/PLANNING.md` when workflows or standards change.
