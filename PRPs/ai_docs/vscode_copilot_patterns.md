# VS Code Copilot Patterns

This document catalogs patterns, best practices, and limitations for using GitHub Copilot in VS Code agent mode.

## Prompt File Requirements
- Frontmatter must include:
  - `mode: 'agent'`
  - `tools: [...]` (VS Code Copilot tools only)
- Use YAML frontmatter, not JSON or TOML.
- Keep prompt files under 500 lines.

## Tooling Patterns
- Use only tools available in VS Code Copilot agent mode: `codebase`, `editFiles`, `runCommands`, `search`, etc.
- Avoid Claude-specific or unsupported tools.

## File Structure
- Modularize prompts, instructions, and templates.
- Place AI documentation in `PRPs/ai_docs/`.
- Use `PRPs/scripts/` for automation scripts.

## Common Pitfalls
- Exceeding file size limits (500 lines).
- Incorrect frontmatter format.
- Using unsupported tools or commands.

## Example Frontmatter
```yaml
---
mode: 'agent'
tools: ['codebase', 'editFiles', 'runCommands', 'search']
description: 'Prompt for PRP execution'
---
```
