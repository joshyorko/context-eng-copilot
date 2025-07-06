name: "Refactor Copilot Agent Structure - Integrate PRPs-Agentic-Eng Patterns"
description: |
  Enhance the current VS Code Copilot agent workspace structure by integrating beneficial 
  patterns from PRPs-agentic-eng while maintaining compatibility with GitHub Copilot's 
  native agent mode and tools.

---

## Goal

Refactor the current workspace's Copilot agent structure to integrate proven patterns from the PRPs-agentic-eng repository, creating a more robust, modular, and maintainable system for context engineering and AI-assisted development. The enhancement should preserve existing VS Code Copilot compatibility while adding advanced PRP workflows, better organization, and comprehensive documentation patterns.

## Why

- **Enhanced Context Engineering**: Current workspace lacks systematic approach to providing AI with comprehensive context
- **Better Organization**: Need modular structure for prompts, templates, and documentation similar to PRPs-agentic-eng
- **Validation Loops**: Missing executable validation gates that ensure working code on first pass
- **Knowledge Management**: No centralized location for AI-specific documentation and patterns
- **Workflow Optimization**: Current PRP workflow is basic compared to the sophisticated PRPs-agentic-eng approach
- **Team Scalability**: Need patterns that work for both individual developers and teams

## What

Transform the workspace into a comprehensive context engineering platform with:
- Enhanced PRP templates with validation loops
- AI documentation directory for context-specific knowledge
- Modular prompt organization with clear separation of concerns
- VS Code Copilot-compatible agent structure
- Executable validation gates for quality assurance
- Scripts for PRP automation and workflow management

### Success Criteria

- [ ] All files under 500 lines (copilot-instructions.md constraint)
- [ ] Enhanced PRP templates with validation loops integrated
- [ ] AI documentation directory (`ai_docs/`) created with relevant content
- [ ] Modular prompt file organization implemented
- [ ] All existing VS Code Copilot functionality preserved
- [ ] New PRP workflow scripts compatible with VS Code environment
- [ ] Documentation updated to reflect new structure
- [ ] Example PRPs demonstrating new capabilities

## All Needed Context

### Documentation & References

```yaml
# MUST READ - Include these in your context window
- file: examples/PRPs-agentic-eng/README.md
  why: Complete overview of PRPs-agentic-eng methodology and structure
  
- file: examples/PRPs-agentic-eng/PRPs/templates/prp_base.md
  why: Advanced PRP template pattern with validation loops and context assembly
  
- file: examples/PRPs-agentic-eng/PRPs/example-from-workshop-mcp-crawl4ai-refactor-1.md
  why: Real-world example of comprehensive PRP with full implementation blueprint
  
- file: .github/copilot-instructions.md
  why: Current VS Code Copilot instructions that must be preserved and enhanced
  
- file: .github/prompts/generate-prp.prompt.md
  why: Current PRP generation prompt that needs enhancement
  
- file: .github/instructions/prp-template.instructions.md
  why: Current PRP template instructions to be upgraded
  
- url: https://code.visualstudio.com/docs/copilot/copilot-tips-and-tricks
  why: VS Code Copilot best practices for agent mode and instructions files
  
- url: https://docs.github.com/en/copilot/get-started/best-practices-for-using-github-copilot
  why: GitHub Copilot best practices for effective prompting and context
```

### Current Codebase Structure

```bash
context-engineering-intro/
├── .github/
│   ├── copilot-instructions.md        # Global Copilot instructions
│   ├── prompts/
│   │   ├── generate-prp.prompt.md     # Basic PRP generation
│   │   ├── execute-prp.prompt.md      # Basic PRP execution
│   │   ├── generate-initial-md.prompt.md
│   │   └── prompt-engineer.prompt.md
│   └── instructions/
│       ├── prp-template.instructions.md    # Basic PRP template
│       └── initial-template.instructions.md
├── PRPs/
│   └── templates/
│       └── prp_base.md               # Basic template
├── examples/
│   └── PRPs-agentic-eng/             # Source of patterns to integrate
├── INITIALS/
│   └── refactor-copilot-agent-structure_initial.md
├── .vscode/
│   ├── settings.json
│   └── mcp.json
└── README.md
```

### Target Enhanced Structure

```bash
context-engineering-intro/
├── .github/
│   ├── copilot-instructions.md        # Enhanced with new patterns
│   ├── prompts/
│   │   ├── generate-prp.prompt.md     # Enhanced with PRPs-agentic-eng patterns
│   │   ├── execute-prp.prompt.md      # Enhanced with validation loops
│   │   ├── planning-create.prompt.md  # NEW: Planning document generation
│   │   ├── review-general.prompt.md   # NEW: Code review capabilities
│   │   └── debug-workflow.prompt.md   # NEW: Debugging workflow
│   └── instructions/
│       ├── prp-template.instructions.md    # Enhanced template guidelines
│       ├── ai-docs.instructions.md         # NEW: AI documentation standards
│       └── validation-gates.instructions.md # NEW: Validation requirements
├── PRPs/
│   ├── templates/
│   │   ├── prp_base.md               # Enhanced with validation loops
│   │   ├── prp_planning.md           # NEW: Planning template
│   │   ├── prp_spec.md               # NEW: Specification template
│   │   └── prp_task.md               # NEW: Task template
│   ├── scripts/
│   │   ├── prp_runner.py             # NEW: VS Code compatible runner
│   │   └── validation_runner.py      # NEW: Validation automation
│   ├── ai_docs/                      # NEW: AI-specific documentation
│   │   ├── vscode_copilot_patterns.md
│   │   ├── context_engineering_guide.md
│   │   ├── validation_strategies.md
│   │   └── troubleshooting_guide.md
│   └── completed/                    # NEW: Completed PRPs archive
├── examples/                          # Enhanced with more patterns
└── docs/                             # NEW: Enhanced documentation
    ├── PLANNING.md                   # Project architecture guide
    ├── TASK.md                       # Task tracking
    └── workflows/                    # Workflow documentation
```

### Known Gotchas & VS Code Copilot Constraints

```python
# CRITICAL: VS Code Copilot agent mode requires specific prompt file format
# Front matter must use YAML with mode: 'agent' and tools array
# Example:
# ---
# mode: 'agent'  
# tools: ['codebase', 'editFiles', 'runCommands']
# description: 'Tool description'
# ---

# CRITICAL: .github/copilot-instructions.md is automatically detected
# Must maintain existing format and file location for VS Code compatibility

# CRITICAL: Instructions files use applyTo pattern for file targeting
# Example: applyTo: "PRPs/*.md" for PRP-specific instructions

# CRITICAL: VS Code Copilot tools are different from Claude Code tools
# Available tools: codebase, editFiles, fetch, findTestFiles, githubRepo, 
# runCommands, search, websearch (not Claude-specific tools)

# CRITICAL: File size limit of 500 lines from copilot-instructions.md
# Must ensure modular structure to stay within limits

# CRITICAL: Python environment is venv_linux not standard venv
# All Python commands must use this environment
```

## Implementation Blueprint

### Data Models and Structure

The refactor will maintain VS Code Copilot compatibility while adding advanced patterns:

```yaml
# Enhanced prompt file structure
prompt_files:
  front_matter:
    mode: 'agent'  # Required for VS Code Copilot
    tools: ['codebase', 'editFiles', 'runCommands', 'search']  # VS Code tools only
    description: 'Clear description of prompt purpose'
  content:
    structured_sections: true
    validation_gates: true
    context_assembly: true

# AI documentation structure  
ai_docs:
  purpose: "Context-specific documentation for AI agents"
  format: "Markdown with clear headings and examples"
  categories:
    - patterns: "Code and workflow patterns"
    - troubleshooting: "Common issues and solutions" 
    - validation: "Testing and quality strategies"
    - context: "Context engineering guidelines"

# Enhanced PRP structure
prp_templates:
  base_sections:
    - goal: "What needs to be built"
    - context: "All necessary documentation and examples"
    - blueprint: "Implementation plan with pseudocode"
    - validation: "Executable validation gates"
    - checklist: "Quality verification steps"
```

### List of Tasks to Complete the PRP (In Order)

```yaml
Task 1 - Create AI Documentation Directory:
CREATE PRPs/ai_docs/:
  - MKDIR PRPs/ai_docs/
  - CREATE vscode_copilot_patterns.md with VS Code-specific patterns
  - CREATE context_engineering_guide.md with context assembly strategies
  - CREATE validation_strategies.md with testing approaches
  - CREATE troubleshooting_guide.md with common issues

Task 2 - Enhance PRP Templates:
MODIFY PRPs/templates/prp_base.md:
  - ADD validation loops section from examples/PRPs-agentic-eng/PRPs/templates/prp_base.md
  - ADD context assembly patterns
  - ADD implementation blueprint structure
  - PRESERVE VS Code Copilot compatibility

CREATE PRPs/templates/prp_planning.md:
  - MIRROR pattern from examples/PRPs-agentic-eng/PRPs/templates/prp_planning.md
  - ADAPT for VS Code Copilot environment
  - INCLUDE diagram generation capabilities

CREATE PRPs/templates/prp_spec.md:
  - PATTERN from examples/PRPs-agentic-eng/PRPs/templates/prp_spec.md
  - FOCUS on technical specifications
  - INCLUDE API design patterns

CREATE PRPs/templates/prp_task.md:
  - SIMPLE task-oriented template
  - QUICK PRP generation for smaller features
  - VALIDATION gates included

Task 3 - Create PRP Automation Scripts:
CREATE PRPs/scripts/:
  - MKDIR PRPs/scripts/
  
CREATE PRPs/scripts/prp_runner.py:
  - ADAPT from examples/PRPs-agentic-eng/PRPs/scripts/prp_runner.py
  - MODIFY for VS Code Copilot instead of Claude Code
  - USE VS Code terminal integration
  - PRESERVE interactive and headless modes

CREATE PRPs/scripts/validation_runner.py:
  - NEW script for running validation gates
  - INTEGRATE with VS Code testing
  - SUPPORT pytest, ruff, mypy validation

Task 4 - Enhance Prompt Files:
MODIFY .github/prompts/generate-prp.prompt.md:
  - ADD research process from examples/PRPs-agentic-eng
  - ADD context assembly strategies
  - ADD validation gate generation
  - PRESERVE VS Code Copilot tools compatibility

MODIFY .github/prompts/execute-prp.prompt.md:
  - ADD ULTRATHINK planning phase
  - ADD validation loop execution
  - ADD error handling patterns
  - ENSURE comprehensive implementation approach

CREATE .github/prompts/planning-create.prompt.md:
  - NEW prompt for planning document generation
  - INCLUDE architecture diagramming
  - ADD task breakdown capabilities

CREATE .github/prompts/review-general.prompt.md:
  - CODE review capabilities
  - PATTERN analysis
  - BEST practice recommendations

Task 5 - Enhance Instructions Files:
MODIFY .github/instructions/prp-template.instructions.md:
  - ADD validation loop requirements
  - ADD context assembly guidelines
  - ADD quality scoring criteria
  - INCLUDE anti-patterns section

CREATE .github/instructions/ai-docs.instructions.md:
  - GUIDELINES for AI documentation creation
  - STRUCTURE standards for ai_docs/ content
  - MAINTENANCE requirements

CREATE .github/instructions/validation-gates.instructions.md:
  - STANDARDS for validation commands
  - EXECUTABLE requirement specifications
  - ERROR handling patterns

Task 6 - Create Project Management Files:
CREATE docs/PLANNING.md:
  - PROJECT architecture overview
  - CODING standards and patterns
  - TOOL and dependency guidelines
  - INTEGRATION points documentation

CREATE docs/TASK.md:
  - TASK tracking format
  - COMPLETION criteria
  - DISCOVERED work section template

Task 7 - Enhance Copilot Instructions:
MODIFY .github/copilot-instructions.md:
  - ADD PRP workflow integration
  - ADD ai_docs/ directory usage
  - ADD validation gate requirements
  - PRESERVE existing project awareness patterns
  - ENSURE file stays under 500 lines

Task 8 - Create Example PRPs:
CREATE PRPs/examples/:
  - MKDIR PRPs/examples/
  
CREATE PRPs/examples/simple-feature-prp.md:
  - DEMONSTRATE new template usage
  - SHOW validation gates in action
  - EXAMPLE of context assembly

CREATE PRPs/examples/complex-refactor-prp.md:
  - ADVANCED PRP example
  - MULTI-file refactoring
  - COMPREHENSIVE validation strategy

Task 9 - Update Documentation:
MODIFY README.md:
  - UPDATE structure documentation
  - ADD new workflow explanations
  - INCLUDE ai_docs/ usage guide
  - PRESERVE existing quick start

CREATE docs/workflows/:
  - MKDIR docs/workflows/
  - CREATE prp-workflow.md with step-by-step guide
  - CREATE validation-workflow.md with testing strategies
  - CREATE troubleshooting-workflow.md with debugging approaches

Task 10 - Final Integration and Testing:
CREATE PRPs/completed/:
  - MKDIR for completed PRP archive
  
VALIDATE all new files:
  - ENSURE VS Code Copilot compatibility
  - TEST prompt file frontmatter format
  - VERIFY instruction file applyTo patterns
  - CONFIRM script functionality

UPDATE .vscode/settings.json:
  - ENSURE github.copilot.chat.codeGeneration.useInstructionFiles: true
  - ADD any new VS Code specific settings
```

### Per Task Pseudocode

```python
# Task 1 - AI Documentation Creation
# Pattern: Create comprehensive context for AI agents
def create_ai_docs():
    """Create ai_docs/ directory with context-specific documentation."""
    # PATTERN: Follow examples/PRPs-agentic-eng/PRPs/ai_docs/ structure
    # ADAPT: Focus on VS Code Copilot instead of Claude Code
    # INCLUDE: VS Code-specific patterns and limitations
    
# Task 2 - Template Enhancement  
def enhance_prp_templates():
    """Upgrade PRP templates with validation loops and context assembly."""
    # PATTERN: Use examples/PRPs-agentic-eng/PRPs/templates/prp_base.md structure
    # PRESERVE: VS Code Copilot compatibility
    # ADD: Executable validation commands
    # INCLUDE: Context assembly strategies
    
# Task 3 - Script Adaptation
def create_prp_scripts():
    """Adapt PRP runner for VS Code environment."""
    # CRITICAL: VS Code doesn't have Claude Code CLI
    # PATTERN: Use VS Code terminal integration instead
    # PRESERVE: Interactive and headless modes
    # ADAPT: Validation commands for VS Code environment
    
# Task 4 - Prompt Enhancement
def enhance_prompt_files():
    """Upgrade prompt files with advanced PRP patterns."""
    # CRITICAL: Maintain VS Code Copilot frontmatter format
    # ADD: Research and context assembly phases
    # INCLUDE: Validation gate generation
    # PRESERVE: VS Code tools compatibility
```

### Integration Points

```yaml
VSCODE_INTEGRATION:
  settings: ".vscode/settings.json - github.copilot.chat.codeGeneration.useInstructionFiles"
  prompts: ".github/prompts/ - frontmatter must use mode: 'agent'"
  instructions: ".github/instructions/ - applyTo patterns for file targeting"
  
COPILOT_AGENT_MODE:
  tools: "Limited to VS Code Copilot tools: codebase, editFiles, runCommands, search"
  instructions: "Automatic detection of .github/copilot-instructions.md"
  validation: "Must use VS Code terminal for command execution"
  
PROJECT_STRUCTURE:
  ai_docs: "PRPs/ai_docs/ for AI-specific context and documentation"
  templates: "PRPs/templates/ for enhanced PRP templates"
  scripts: "PRPs/scripts/ for automation (adapted for VS Code)"
  examples: "PRPs/examples/ for demonstrating new capabilities"
  
DOCUMENTATION:
  planning: "docs/PLANNING.md for project architecture"
  tasks: "docs/TASK.md for task tracking"
  workflows: "docs/workflows/ for process documentation"
```

## Validation Loop

### Level 1: Structure and Compatibility

```bash
# Verify VS Code Copilot compatibility
# Check that frontmatter format is correct in all prompt files
grep -r "mode: 'agent'" .github/prompts/
grep -r "tools:" .github/prompts/

# Verify instruction file patterns
grep -r "applyTo:" .github/instructions/

# Check file size constraints (must be under 500 lines)
find . -name "*.md" -exec wc -l {} + | awk '$1 > 500 {print $2 " exceeds 500 lines (" $1 ")"}'
```

### Level 2: Content Validation

```bash
# Validate that all AI docs are properly structured
find PRPs/ai_docs/ -name "*.md" -exec head -1 {} \; | grep -c "^#"

# Check that PRP templates include validation sections
grep -r "Validation Loop" PRPs/templates/
grep -r "Level 1:" PRPs/templates/
grep -r "Level 2:" PRPs/templates/

# Verify scripts are executable and have proper shebangs
find PRPs/scripts/ -name "*.py" -exec head -1 {} \; | grep -c "#!/usr/bin/env"
```

### Level 3: Integration Testing

```bash
# Test VS Code Copilot instructions detection
# Start VS Code and verify that .github/copilot-instructions.md is detected
# This requires manual verification in VS Code interface

# Test prompt file functionality
# Use VS Code Copilot chat to test new prompt files
# Verify that agent mode works with enhanced prompts

# Test PRP workflow
# Generate a test PRP using enhanced generate-prp prompt
# Execute test PRP using enhanced execute-prp prompt
# Verify validation gates execute properly
```

## Quality Checklist

- [ ] All VS Code Copilot compatibility preserved
- [ ] Enhanced PRP templates with validation loops created
- [ ] AI documentation directory (ai_docs/) populated
- [ ] PRP automation scripts adapted for VS Code
- [ ] Enhanced prompt files maintain proper frontmatter
- [ ] Instruction files use correct applyTo patterns
- [ ] File size constraints respected (under 500 lines)
- [ ] Project documentation updated
- [ ] Example PRPs demonstrate new capabilities
- [ ] Validation gates are executable in VS Code environment

## Confidence Score: 8/10

**Reasoning**: High confidence due to:
- Clear understanding of both current structure and target patterns
- Comprehensive research of VS Code Copilot requirements
- Detailed task breakdown with specific patterns to follow
- Strong validation strategy with multiple levels
- Preservation of existing functionality while adding enhancements
- Modular approach allows incremental implementation

**Potential challenges**: 
- Script adaptation from Claude Code to VS Code environment
- Ensuring all new patterns maintain VS Code Copilot compatibility
- Balancing feature richness with file size constraints

---

## Anti-Patterns to Avoid

- ❌ Don't break VS Code Copilot compatibility by using Claude-specific patterns
- ❌ Don't exceed 500-line file size limit specified in copilot-instructions.md
- ❌ Don't use tools not available in VS Code Copilot agent mode
- ❌ Don't modify frontmatter format in prompt files (.github/prompts/)
- ❌ Don't create circular dependencies between enhanced components
- ❌ Don't skip validation gate implementation - they ensure working code
- ❌ Don't ignore existing project patterns when adding new structure
- ❌ Don't copy Claude Code CLI commands that won't work in VS Code
