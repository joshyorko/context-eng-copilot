---
applyTo: "PRPs/*.md"
description: "Standards for validation commands and error handling in PRPs"
---

# Validation Gates Instructions

## Purpose
Define standards for validation commands and error handling in Product Requirements Prompts (PRPs).

## Validation Gate Levels
- **Level 1:** Syntax & Style (e.g., ruff, mypy)
- **Level 2:** Unit Tests (e.g., pytest)
- **Level 3:** Integration/Manual (e.g., curl, workflow tests)

## Requirements
- All validation commands must be executable in the project environment
- Document expected output and error handling for each gate
- Repeat validation until all gates pass

## Error Handling Patterns
- Analyze error output and root cause
- Apply recommended fixes or patterns
- Document fix in PRP if non-obvious
- Never skip validation steps
