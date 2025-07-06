# Task PRP Template

## Purpose
Quickly define and execute a focused task or small feature with validation gates.

---

## Task Description
- [Describe the task or feature to be implemented.]

## Context
- [List any files, docs, or references needed.]

## Implementation Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Validation Loop

### Level 1: Syntax & Style
```bash
ruff check src/ --fix
mypy src/
```

### Level 2: Unit Tests
```bash
uv run pytest tests/ -v
```

### Level 3: Manual/Integration
- [Describe manual or integration test if needed.]

## Completion Checklist
- [ ] Code passes all validation gates
- [ ] Task is documented if needed
- [ ] No errors or warnings
