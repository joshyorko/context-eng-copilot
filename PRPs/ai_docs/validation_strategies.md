# Validation Strategies for PRPs

How to design, implement, and automate validation gates for Product Requirements Prompts (PRPs).

## Validation Loop Levels
- **Level 1:** Structure and compatibility (file formats, frontmatter, patterns)
- **Level 2:** Content validation (template sections, doc structure, script shebangs)
- **Level 3:** Integration testing (prompt execution, workflow validation)

## Automation
- Use scripts in `PRPs/scripts/` to automate validation gates.
- Integrate with VS Code terminal and testing tools (pytest, ruff, mypy).

## Error Handling
- Analyze error patterns and apply recommended fixes.
- Repeat validation until all gates pass.

## Example Validation Command
```bash
grep -r "mode: 'agent'" .github/prompts/
```
