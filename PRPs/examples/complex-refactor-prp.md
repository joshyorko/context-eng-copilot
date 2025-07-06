name: "Complex Refactor Example PRP"
description: |
  Demonstrates a multi-file refactor with comprehensive validation and context assembly.

## Goal
Refactor user authentication to use JWT tokens.

## Why
- Improve security and scalability
- Replace legacy session-based auth

## What
- Implement JWT-based login/logout
- Update all auth-protected endpoints

### Success Criteria
- [ ] All endpoints use JWT auth
- [ ] Legacy session code removed
- [ ] All tests pass

## All Needed Context
### Documentation & References
- url: https://jwt.io/introduction/
  why: JWT structure and best practices
- file: src/auth/session.py
  why: Current session logic to replace
- file: src/auth/jwt_utils.py
  why: JWT helper functions
- docfile: PRPs/ai_docs/context_engineering_guide.md
  why: Context assembly and integration

### Known Gotchas
# CRITICAL: Use RS256 for production
# CRITICAL: Update tests for new auth

## Implementation Blueprint
### Data models and structure
- JWT payload model
- Auth response schemas

### list of tasks to be completed
Task 1:
MODIFY src/auth/session.py:
  - REMOVE session logic
Task 2:
CREATE src/auth/jwt_auth.py:
  - IMPLEMENT JWT login/logout
Task 3:
MODIFY src/api/routes.py:
  - UPDATE endpoints to use JWT auth
Task 4:
MODIFY tests/test_auth.py:
  - UPDATE tests for JWT

### Per task pseudocode
# Task 2
async def login(user):
    # Validate user, issue JWT
    ...

### Integration Points
CONFIG:
  - add to: config/settings.py
ROUTES:
  - update: src/api/routes.py

## Validation Loop
### Level 1: Syntax & Style
ruff check src/ --fix
mypy src/

### Level 2: Unit Tests
uv run pytest tests/ -v

### Level 3: Integration
curl -X POST http://localhost:8000/auth/login

## Completion Checklist
- [ ] All validation gates pass
- [ ] Legacy code removed
- [ ] Docs updated
