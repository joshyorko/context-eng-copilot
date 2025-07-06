# Troubleshooting Guide for AI-Driven PRP Workflows

Common issues, solutions, and debugging strategies for context engineering with VS Code Copilot.

## Common Issues
| Issue | Cause | Solution |
|-------|-------|----------|
| Prompt not detected | Incorrect frontmatter | Check YAML frontmatter format |
| Validation fails | Missing validation section | Add required validation gates |
| File too large | Exceeds 500 lines | Refactor into modules |
| Unsupported tool | Non-Copilot tool used | Use only VS Code Copilot tools |

## Debugging Steps
- Check logs and validation output for error messages.
- Use `validation_runner.py` to automate checks.
- Review `ai_docs/` for known patterns and solutions.

## Resources
- [VS Code Copilot Docs](https://code.visualstudio.com/docs/copilot/copilot-tips-and-tricks)
- [GitHub Copilot Best Practices](https://docs.github.com/en/copilot/get-started/best-practices-for-using-github-copilot)
