#!/usr/bin/env python3
"""
Validation runner for PRP workflows in VS Code Copilot environment.
- Runs validation gates (lint, type check, tests) as defined in PRP templates
- Prints results and highlights failures
"""
import subprocess
import sys

def run_command(cmd, desc):
    print(f"\n--- {desc} ---")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"FAILED: {desc}", file=sys.stderr)
        sys.exit(result.returncode)
    print(f"PASSED: {desc}")

def main():
    # Level 1: Syntax & Style
    run_command("ruff check src/ --fix", "Lint (ruff)")
    run_command("mypy src/", "Type Check (mypy)")
    # Level 2: Unit Tests
    run_command("uv run pytest tests/ -v", "Unit Tests (pytest)")
    # Level 3: Integration (manual step or add more commands as needed)
    print("\nAll validation gates passed.")

if __name__ == "__main__":
    main()
