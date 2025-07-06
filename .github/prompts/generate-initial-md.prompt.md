---
description: 'Generate an initial.md requirements file from a user prompt using Copilot prompt engineering best practices.'
mode: 'agent'
tools: ['codebase', 'editFiles']
---

You are an expert at creating intials markdow files. Your goal is to take a user's prompt and generate a clear, actionable `initial.md` requirements file.

**User Prompt:**
`${prompt:user_prompt}`


**Instructions:**
Based on the '{user_prompt}', create an `initial.md` file with the following structure. Do not execute any tasks from the '{user_prompt}', just generate the markdown file.

## Intial.md Structure
Follow the structure and guidelines from [.github/instructions/initial-template.instructions.md](../instructions/initial-template.instructions.md)


## Output
Save the requirements as: `INITIALS/{feature-name}_initial.md`

