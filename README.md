
# Context Engineering Intro

**Context Engineering** is the discipline of designing, documenting, and automating the context that AI coding assistants need to deliver reliable, high-quality software. This repository is a living reference for building, validating, and evolving context-driven workflows using Product Requirements Prompts (PRPs), validation gates, and AI documentation.

---

## 🧠 Philosophy

> "Most AI failures are context failures, not model failures."

This project demonstrates how to:
- Systematically encode project knowledge, rules, and patterns for AI agents
- Use PRPs to drive feature development and validation
- Integrate documentation, planning, and validation into a single workflow

---

## 📂 Repository Structure

```
context-engineering-intro/
├── .github/                  # Copilot instructions, prompts, and coding standards
├── PRPs/                     # Product Requirements Prompts, templates, scripts, docs
│   ├── ai_docs/              # AI-specific docs: context, validation, troubleshooting
│   ├── completed/            # Archive of completed PRPs
│   ├── examples/             # Example PRPs
│   ├── scripts/              # PRP/validation automation scripts
│   ├── templates/            # PRP templates (base, planning, spec, task)
├── EXECUTED_PRPS/            # Output of executed PRPs (feature implementations)
├── examples/                 # Code patterns and reference implementations
├── docs/                     # Planning, task tracking, workflow docs
│   ├── PLANNING.md           # Architecture, standards, integration points
│   ├── TASK.md               # Task tracking and completion
│   └── workflows/            # PRP, validation, troubleshooting workflows
└── README.md                 # This file
```

---

## 🚦 PRP Workflow

1. **Describe a feature** in `INITIAL.md` (or a new file)
2. **Generate a PRP** using Copilot and `.github/prompts/generate-prp.prompt.md`
3. **Review and refine** the PRP (requirements, context, validation gates)
4. **Execute the PRP** using `.github/prompts/execute-prp.prompt.md`
5. **Validate** with automated gates (syntax, tests, integration)
6. **Track progress** in `docs/TASK.md`
7. **Document patterns** in `PRPs/ai_docs/` as they evolve

All PRPs must include a "Validation Loop" section with Level 1 (syntax/style), Level 2 (unit tests), and Level 3 (integration/manual) gates. Use `PRPs/scripts/validation_runner.py` to automate validation.

---

## 🛠️ Key Files & Folders

- `.github/copilot-instructions.md`: Project-wide Copilot rules and conventions
- `PRPs/ai_docs/`: AI documentation for context assembly and troubleshooting
- `PRPs/scripts/`: Automation for PRP and validation workflows
- `docs/PLANNING.md`: Architecture, coding standards, and update policy
- `docs/TASK.md`: Task tracking and completion
- `EXECUTED_PRPS/`: All generated/implemented features

---

## 🧩 Contributing & Extending

1. **Add new features** by creating a PRP and following the workflow above
2. **Update documentation** in `PRPs/ai_docs/` and `docs/` as standards evolve
3. **Keep all code under 500 lines per file** (see `.github/copilot-instructions.md`)
4. **Write Pytest unit tests** for all new logic (see `/tests` in feature folders)
5. **Mark completed tasks** in `docs/TASK.md` and add new TODOs as discovered

---

## 📝 References & Resources

- [docs/PLANNING.md](docs/PLANNING.md): Architecture & standards
- [PRPs/ai_docs/](PRPs/ai_docs/): AI documentation & troubleshooting
- [PRPs/scripts/validation_runner.py](PRPs/scripts/validation_runner.py): Validation automation
- [Robocorp RCC](https://robocorp.com/docs/rcc/)
- [Context Engineering Best Practices](https://www.philschmid.de/context-engineering)

---

**For details on the fetch-repos-bot example, see** `examples/fetch-repos-bot/README.md`.