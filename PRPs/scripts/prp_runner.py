#!/usr/bin/env python3
"""
VS Code Copilot-compatible PRP runner script.
- Loads a PRP markdown file
- Prints out the planning, implementation, and validation steps
- Designed for interactive and headless use in VS Code
"""
import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Run a PRP in VS Code Copilot environment.")
    parser.add_argument("--prp-path", help="Path to PRP markdown file", required=True)
    parser.add_argument("--interactive", action="store_true", help="Interactive mode (print sections and wait for user)")
    args = parser.parse_args()

    prp_path = Path(args.prp_path)
    if not prp_path.exists():
        print(f"PRP file not found: {prp_path}", file=sys.stderr)
        sys.exit(1)

    content = prp_path.read_text()
    print("\n=== PRP: Planning Section ===\n")
    planning = extract_section(content, ["Goal", "Why", "What", "Success Criteria"])
    print(planning)
    if args.interactive:
        input("Press Enter to continue to Implementation...")

    print("\n=== PRP: Implementation Blueprint ===\n")
    blueprint = extract_section(content, ["Implementation Blueprint", "Data models", "list of tasks", "pseudocode", "Integration Points"])
    print(blueprint)
    if args.interactive:
        input("Press Enter to continue to Validation...")

    print("\n=== PRP: Validation Loop ===\n")
    validation = extract_section(content, ["Validation Loop", "Level 1", "Level 2", "Level 3", "Checklist"])
    print(validation)
    print("\nPRP run complete.")

def extract_section(content, headers):
    lines = content.splitlines()
    result = []
    capture = False
    for line in lines:
        if any(h in line for h in headers):
            capture = True
        elif capture and (line.strip().startswith('##') or line.strip().startswith('# ')):
            break
        if capture:
            result.append(line)
    return '\n'.join(result)

if __name__ == "__main__":
    main()
