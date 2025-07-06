# Context Engineering Guide

Guidelines for assembling, maintaining, and delivering context to AI agents in the workspace.

## Principles
- Provide all necessary documentation and examples in context.
- Use structured templates for PRPs and prompts.
- Modularize context: templates, scripts, docs, and instructions.

## Context Assembly Patterns
- Reference all required files in PRP context sections.
- Use tables for presenting lists or structured data.
- Avoid inline or bullet-point lists for structured data.

## Best Practices
- Keep documentation up to date as features evolve.
- Use `ai_docs/` for AI-specific knowledge and troubleshooting.
- Document integration points and validation gates.

## Example Context Section
```yaml
- file: path/to/example.py
  why: Pattern to follow
- url: https://docs.example.com
  why: API reference
```
