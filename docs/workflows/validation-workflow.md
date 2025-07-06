# Validation Workflow Guide

## Purpose
Describe the validation process for code, PRPs, and workflows.

## Validation Levels
- **Level 1:** Syntax & Style (ruff, mypy)
- **Level 2:** Unit Tests (pytest)
- **Level 3:** Integration/Manual (curl, workflow tests)

## Process
1. Run each validation command in order
2. Fix any errors before proceeding
3. Document fixes and patterns
4. Repeat until all gates pass

## Automation
- Use `PRPs/scripts/validation_runner.py` to automate validation
