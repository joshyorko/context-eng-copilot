---
applyTo: "PRPs/*.md"
description: "Template and guidelines for creating Product Requirements Prompts (PRPs)"
---

# PRP Template and Guidelines

## Purpose
Template optimized for AI agents to implement features with sufficient context and self-validation capabilities to achieve working code through iterative refinement.

## Core Principles
1. **Context is King**: Include ALL necessary documentation, examples, and caveats
2. **Validation Loops**: Provide executable tests/lints the AI can run and fix
3. **Information Dense**: Use keywords and patterns from the codebase
4. **Progressive Success**: Start simple, validate, then enhance
5. **Global rules**: Follow all rules in [GitHub Copilot instructions](.github/copilot-instructions.md)

## PRP Structure Template

### Header
```yaml
name: "[Descriptive Feature Name]"
description: |
  Brief description of what this PRP accomplishes
```

### Goal Section
- What needs to be built - be specific about the end state and desires
- Why: Business value, integration benefits, problems solved
- What: User-visible behavior and technical requirements
- Success Criteria: Specific measurable outcomes

### Context Section
```yaml
# Documentation & References
- url: [Official API docs URL]
  why: [Specific sections/methods needed]
  
- file: [path/to/example.py] 
  why: [Pattern to follow, gotchas to avoid]
  
- doc: [Library documentation URL]
  section: [Specific section about common pitfalls]
  critical: [Key insight that prevents common errors]
```

### Implementation Blueprint
- **Data models**: Core data structures using Pydantic, ORM models, validators
- **Task List**: Ordered list of implementation tasks with specific patterns to follow
- **Pseudocode**: Critical implementation details without full code
- **Integration Points**: Database, config, routes, external dependencies

### Validation Requirements
```bash
# Level 1: Syntax & Style
ruff check src/ --fix && mypy src/

# Level 2: Unit Tests  
uv run pytest tests/ -v

# Level 3: Integration Tests
[Specific commands to validate the feature works end-to-end]
```

## Validation Loop Requirements
- Every PRP must include a "Validation Loop" section with Level 1 (syntax/style), Level 2 (unit tests), and Level 3 (integration/manual) gates.
- Validation commands must be executable in the project environment (e.g., ruff, mypy, pytest, curl).
- Document error handling and fix patterns for failed validation gates.

## Context Assembly Guidelines
- List all referenced files, documentation, and URLs in a "Context Assembly" table.
- Use clear headers and rows for each item.
- Ensure all context is available to the AI agent at execution time.

## Quality Standards
- All validation commands must be executable by AI
- Reference existing codebase patterns wherever possible
- Include comprehensive error handling strategy
- Provide specific file paths and line numbers for reference patterns
- Score confidence level 1-10 for one-pass implementation success

## Quality Scoring Criteria
- Score each PRP for confidence in one-pass implementation (1-10).
- Reference existing codebase patterns and error handling strategies.
- Include comprehensive error handling and test coverage.

## Anti-Patterns to Avoid
- Don't create new patterns when existing ones work
- Don't skip validation steps
- Don't ignore failing tests - fix them
- Don't hardcode values that should be configurable
- Don't catch generic exceptions - be specific

## Anti-Patterns (Expanded)
- ❌ Don't create new patterns when existing ones work
- ❌ Don't skip validation steps
- ❌ Don't ignore failing tests - fix them
- ❌ Don't hardcode values that should be configurable
- ❌ Don't catch generic exceptions - be specific
- ❌ Don't omit context assembly or validation loop sections
