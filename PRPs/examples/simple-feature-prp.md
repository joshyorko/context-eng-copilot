name: "Simple Feature Example PRP"
description: |
  Demonstrates the new PRP template and validation loop for a basic feature.

## Goal
Implement a hello world endpoint.

## Why
- Provide a minimal working example for new contributors
- Test PRP workflow and validation gates

## What
- Add `/hello` endpoint returning JSON `{ "message": "Hello, world!" }`

### Success Criteria
- [ ] `/hello` returns correct response
- [ ] Code passes all validation gates

## All Needed Context
### Documentation & References
- file: src/api/routes.py
  why: Where endpoints are registered
- docfile: PRPs/ai_docs/vscode_copilot_patterns.md
  why: Endpoint pattern and Copilot constraints

### Known Gotchas
# CRITICAL: Endpoint must use async def

## Implementation Blueprint
### Data models and structure
- No new models needed

### list of tasks to be completed
Task 1:
MODIFY src/api/routes.py:
  - ADD async endpoint `/hello`
  - RETURN JSON response

### Per task pseudocode
# Task 1
async def hello():
    return {"message": "Hello, world!"}

### Integration Points
ROUTES:
  - add to: src/api/routes.py

## Validation Loop
### Level 1: Syntax & Style
ruff check src/ --fix
mypy src/

### Level 2: Unit Tests
uv run pytest tests/ -v

### Level 3: Manual/Integration
curl -X GET http://localhost:8000/hello

## Completion Checklist
- [ ] All validation gates pass
- [ ] Example is documented
