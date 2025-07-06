---
mode: 'agent'
tools: ['codebase', 'editFiles', 'fetch', 'findTestFiles', 'githubRepo', 'runCommands', 'search', 'websearch']
description: 'Generate a comprehensive Product Requirements Prompt (PRP) for feature implementation'
---

# Generate Product Requirements Prompt (PRP)

Your goal is to create a comprehensive PRP for feature implementation with thorough research. Read the feature file referenced in the input to understand requirements, examples, and considerations.

## Input Requirements
Provide the feature file path using the `feature_file_path` input variable.
The feature file  is located at `${input:feature_file_path}` and contains:
- **FEATURE**: What needs to be built
- **EXAMPLES**: Code examples and patterns to follow  
- **DOCUMENTATION**: Relevant documentation links
- **OTHER CONSIDERATIONS**: Gotchas and specific requirements

## Research Process

### 1. Codebase Analysis
- Search for similar features/patterns in the current codebase
- Identify existing files to reference in the PRP
- Note current conventions and patterns to follow
- Check existing test patterns for validation approach

### 2. External Research  
- Search for similar implementations online
- Include specific documentation URLs with relevant sections
- Find implementation examples from GitHub/StackOverflow/blogs
- Research best practices and common pitfalls

## Context Assembly
The AI agent implementing the PRP only gets the context you provide. Include:
- **Documentation**: URLs with specific sections
- **Code Examples**: Real snippets from codebase  
- **Gotchas**: Library quirks, version issues
- **Patterns**: Existing approaches to follow

| Context Element | Description |
|------------------|-------------|
| Documentation    | URLs with specific sections |
| Code Examples    | Real snippets from codebase |
| Gotchas          | Library quirks, version issues |
| Patterns         | Existing approaches to follow |

## PRP Structure
Use the template guidelines at `#prp-template.instructions.md` .github/instructions/prp-template.instructions.md and include:

### Implementation Blueprint
- Start with pseudocode showing the approach
- Reference real files for patterns
- Include comprehensive error handling strategy
- List tasks in implementation order

### Validation Gates (Must be Executable)
For Python projects:
```bash
# Syntax/Style
ruff check --fix && mypy .

# Unit Tests  
uv run pytest tests/ -v
```

### Quality Checklist
- [ ] All necessary context included
- [ ] Validation gates are executable by AI
- [ ] References existing patterns
- [ ] Clear implementation path
- [ ] Error handling documented

## Advanced Features
- Add a "Validation Loop" section to the PRP, with Level 1 (syntax/style), Level 2 (unit tests), and Level 3 (integration/manual) gates.
- Include a "Context Assembly" table for all referenced files, docs, and URLs.
- Add a "ULTRATHINK" planning phase before implementation.

## Output
Save the PRP as: `PRPs/{feature-name}/{feature-name}_prp.md`

## Success Criteria
Score the PRP on a scale of 1-10 for confidence in one-pass implementation success. The goal is comprehensive context that enables successful implementation without iteration.

**CRITICAL**: After research and exploration, ULTRATHINK about the PRP approach before writing. Plan thoroughly to ensure all requirements are addressed.

**CRITICAL**: This prompt's purpose is to *generate* a PRP file. It should not execute the PRP or perform any of the tasks described within the PRP. The output is the PRP markdown file itself.
