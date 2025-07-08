---
mode: 'agent'
tools: ['changes', 'codebase', 'editFiles', 'extensions', 'fetch', 'findTestFiles', 'githubRepo', 'new', 'problems', 'runCommands', 'runNotebooks', 'runTasks', 'search', 'searchResults', 'terminalLastCommand', 'terminalSelection', 'testFailure', 'usages', 'vscodeAPI']
description: 'Execute a Product Requirements Prompt (PRP) to implement a feature'
---

# Execute Product Requirements Prompt (PRP)

Your goal is to implement a feature using a comprehensive PRP file that contains all necessary context and requirements.

## Input Requirements
Provide the PRP file path (e.g., `PRPs/{feature-name}/multi-agent-system.md`) that contains the complete implementation specification.

## Execution Process

### 1. Load PRP Context
- Read the specified PRP file completely
- Follow the structure and guidelines from [.github/instructions/prp-template.instructions.md](.github/instructions/prp-template.instructions.md)
- Understand all context and requirements
- Follow all instructions in the PRP
- Extend research if gaps are identified
- Ensure you have complete context before proceeding

### 2. ULTRATHINK Planning
- Create a comprehensive implementation plan addressing all requirements
- Break down complex tasks into smaller, manageable steps
- Identify implementation patterns from existing code to follow
- Plan validation strategy for each component

### 3. Implementation
- Execute the PRP systematically
- Follow the task order specified in the PRP
- Implement all code according to the specifications
- Apply existing patterns and conventions from the codebase
- Handle errors as specified in the PRP

### 4. Validation Loop
- Run each validation command specified in the PRP
- Fix any failures that occur
- Re-run validation until all tests pass
- Follow the error handling patterns from the PRP

### 5. Completion Verification
- Ensure all checklist items from the PRP are completed
- Run the final validation suite
- Verify all requirements have been met
- Reference the PRP again to confirm nothing was missed

### 6. Status Reporting
- Report completion status with summary of what was implemented
- Note any deviations from the original PRP (if any)
- Confirm all validation gates pass

## Advanced Features
- Add a "ULTRATHINK" planning phase before implementation.
- Add a "Validation Loop" section with Level 1, 2, and 3 gates.
- Document error handling and fix patterns for failed validation gates.

## Implementation Guidelines
- Follow the [GitHub Copilot instructions](../copilot-instructions.md) for coding standards
- Use existing patterns and conventions from the codebase
- Implement comprehensive error handling as specified
- Create tests following the established patterns
- Document code according to project standards

## Validation Requirements
All validation commands from the PRP must pass before considering the implementation complete. If validation fails:
1. Analyze the error patterns specified in the PRP
2. Apply the recommended fixes
3. Re-run validation
4. Repeat until all tests pass

**Note**: Never skip validation steps. The goal is working, tested code that meets all PRP requirements.
