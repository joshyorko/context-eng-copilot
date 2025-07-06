# PRP Workflow Guide

## Purpose
Step-by-step guide for creating, executing, and validating Product Requirements Prompts (PRPs).

## Steps
1. Generate a PRP using `.github/prompts/generate-prp.prompt.md`
2. Review and edit the PRP for completeness and context
3. Execute the PRP using `.github/prompts/execute-prp.prompt.md`
4. Run validation gates (ruff, mypy, pytest, integration)
5. Move completed PRPs to `PRPs/completed/`

## Best Practices
- Always include a validation loop in PRPs
- Use context assembly tables for all references
- Document all errors and fixes
