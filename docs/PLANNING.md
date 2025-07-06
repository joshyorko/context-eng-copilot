# Project Architecture & Planning Guide

## Overview
This document describes the architecture, coding standards, and integration points for the context-engineering-intro project.

## Architecture
- Modular structure: prompts, templates, scripts, ai_docs, workflows
- All files under 500 lines (Copilot constraint)
- Use VS Code Copilot-compatible frontmatter for prompts

## Coding Standards
- Use clear, consistent imports (prefer relative imports within packages)
- Organize code by feature and responsibility
- Use python_dotenv and load_env() for environment variables
- Always create Pytest unit tests for new features
- Place tests in `/tests` mirroring main app structure

## Tooling & Dependencies
- Use venv_linux for Python commands
- Use ruff, mypy, pytest for validation
- Document all dependencies in README.md

## Integration Points
- Prompts: `.github/prompts/`
- Instructions: `.github/instructions/`
- AI Docs: `PRPs/ai_docs/`
- Scripts: `PRPs/scripts/`
- Templates: `PRPs/templates/`
- Workflows: `docs/workflows/`

## Update Policy
- Update this file when architecture or standards change
- Reference this file in all major PRPs and documentation
