---
title: ActionServer Agent - Initial PRP
author: automated-agent
date: 2025-08-17
confidence_estimate: 8
---

# ActionServer Agent — Product Requirements Prompt (PRP)

Short: Build a minimal LangGraph agent that exposes the Action Server Toolkit as LangChain-style tools, following patterns used in `examples/oap-langgraph-tools-agent` and `examples/lang_sema4_example.py`.

## One-line plan
Create `agents/actionserver_agent/` which wires a Planner, a ToolNode (wrapping ActionServerToolkit tools), and a Summarizer, implements guardrails (SAFE_MODE, AUTO_APPROVE, arg-echoing, confirmation for mutating ops), provides `.env.example`, README, langgraph.json entry, and a smoke/demo runner/Makefile target.

## Requirements mapping
- Input: user natural-language intent
- Output: final natural-language answer and a structured JSON summary
- Agent components: Planner, ToolNode (ActionServer tools), Summarizer
- Env config: `ACTION_SERVER_URL`, `SAFE_MODE`, `AUTO_APPROVE`
- Deliverables: `agents/actionserver_agent/agent.py`, `__init__.py`, `README.md`, `.env.example`, `langgraph.json` entry, `make demo-actionserver-agent` Makefile target or demo script

## ULTRATHINK (high-level pre-implementation reasoning)

- Follow the example agent wiring from `examples/oap-langgraph-tools-agent/tools_agent/agent.py` and tools utilities in `tools_agent/utils/tools.py`.
- Use `langchain_sema4.ActionServerToolkit` exactly as `examples/lang_sema4_example.py` demonstrates: instantiate toolkit with a base url and call `get_tools()` to receive tool objects.
- Wrap each toolkit tool into a LangChain-style StructuredTool (or use `langchain_core.tools.tool` decorator) and then expose via `ToolNode` to the LangGraph.
- Implement guardrail wrappers that: validate inputs, echo args, respect SAFE_MODE (dry-run), and prompt for confirmation before mutating operations (unless AUTO_APPROVE=true). Mutating operations list is taken from the feature file.
- For file edits, always call `get_file_contents(path)` first and return a proposed patch rather than edit directly.
- Tests: smoke test that runs in SAFE_MODE (no network) and, if ACTION_SERVER_URL points to a live server, runs a live demo.

## Context Assembly (files & docs referenced)

| Context Element | Path / URL | Purpose |
|---|---|---|
| Example agent wiring | `examples/oap-langgraph-tools-agent/tools_agent/agent.py` | Graph wiring, config schema pattern, model init and create_react_agent usage |
| Tool utilities | `examples/oap-langgraph-tools-agent/tools_agent/utils/tools.py` | Dynamic MCP tool wrapping, error handling pattern for auth | 
| ActionServer example | `examples/lang_sema4_example.py` | How to instantiate `ActionServerToolkit` and bind tools |
| Feature spec | `INITIALS/actionserver_agent_initial.md` | Source requirements and acceptance criteria |
| PRP generation prompt | `.github/prompts/generate-prp.prompt.md` | This PRP's template and validation gate requirements |

## Implementation blueprint (pseudocode + files)

Pseudocode:

1. agents/actionserver_agent/__init__.py
   - package exports: build_graph, demo runner

2. agents/actionserver_agent/agent.py
   - load dotenv
   - read env: ACTION_SERVER_URL (default from .env.example), SAFE_MODE, AUTO_APPROVE
   - instantiate ActionServerToolkit(url=ACTION_SERVER_URL, report_trace=True)
   - sema4_tools = toolkit.get_tools()
   - For each tool in sema4_tools:
       - wrap it in a guardrail wrapper: validate args, echo planned args, if SAFE_MODE -> simulate response; else call real tool
       - attach mutating flag for operations that change state
   - create ToolNode from wrapped tools
   - implement Planner: a runnable that turns user intent into the initial model prompt (or single step); reuse pattern from `examples/oap...` `graph()` function that creates a react agent or custom planner runnable
   - Summarizer: after the tool execution loop ends, summarize the conversation (human readable + structured JSON) and return both
   - Build LangGraph graph: start -> planner -> tool_node -> summarizer -> END

3. agents/actionserver_agent/utils.py (helper functions)
   - is_mutating_tool(tool_name) -> bool (based on known list)
   - simulate_tool_response(tool_name, args) -> sample response
   - require_confirmation(prompt_text) -> bool (interactive or based on AUTO_APPROVE)
   - create_wrapped_tool(original_tool) -> StructuredTool that performs guardrail behavior

4. agents/actionserver_agent/.env.example
   - ACTION_SERVER_URL=http://localhost:8282
   - SAFE_MODE=true
   - AUTO_APPROVE=false

5. agents/actionserver_agent/README.md
   - Run instructions, env vars, example prompts, troubleshooting

6. langgraph.json (add entry in repo root or agents folder)
   - Add an entry mirroring `examples/oap-langgraph-tools-agent/langgraph.json` with path to new `agents/actionserver_agent` graph builder

7. Makefile target / demo script
   - `make demo-actionserver-agent` -> sets env and runs a short demo using `python -m agents.actionserver_agent.agent_demo` or similar. Support SAFE_MODE and live runs.

Tasks (in implementation order):
- [ ] Create package skeleton `agents/actionserver_agent/` with `agent.py`, `__init__.py`, `utils.py`
- [ ] Add `.env.example` and README.md
- [ ] Implement toolkit instantiation and tool wrapping
- [ ] Implement Planner runnable (simple prompt-to-tool-decider)
- [ ] Implement Summarizer runnable to return text + structured JSON summary
- [ ] Add langgraph.json entry
- [ ] Add Makefile/demo script
- [ ] Add basic unit tests for wrapper behavior and SAFE_MODE
- [ ] Add smoke test (Makefile target) and run locally

## Error handling strategy

- Fail fast with clear error messages for missing env (ACTION_SERVER_URL if SAFE_MODE=false)
- Wrap external calls in try/except; surface ToolException-like errors as user-facing messages, not stack traces
- For toolkit auth/interaction_required errors, reuse pattern in `tools_agent/utils/tools.wrap_mcp_authenticate_tool` to turn into a user-friendly prompt
- When in SAFE_MODE, never perform network mutating calls; instead return deterministic simulated outputs and log the would-be call (without secrets)
- On file edits: always fetch file via `get_file_contents(path)` and produce a patch suggestion; if patch generation fails, return a structured error and do not attempt to write

## Guardrails specification

- SAFE_MODE (default true in `.env.example`): wrapper returns simulated response and prints a dry-run banner
- Arg echoing: before executing a tool, the agent returns a short message echoing the args for confirmation
- Confirmation step: for mutating operations (create_robot, pull_robot, run_robot, run_task, task_testrun, wrap_robot, unwrap_robot, any docs that modify, etc), require user confirmation unless `AUTO_APPROVE=true`.
- Interactive confirmations can be: (a) if running in CLI/demo: prompt for y/n, (b) if running in a non-interactive environment: rely on `AUTO_APPROVE` env var

## Tool wrapping behavior (detailed)

- Wrapper steps when tool is invoked:
  1. Validate required args per the tool's input schema and types
  2. Echo planned call to the user: `Calling {tool} with {args}`
  3. If SAFE_MODE == true:
       - Log `DRY-RUN: {tool}({args})` and return a simulated response (shape matches expected schema when possible)
  4. Else:
       - If tool is mutating and AUTO_APPROVE != true: require confirmation (interactive prompt or error)
       - Execute underlying toolkit tool and return result
  5. If the tool raises an auth/interaction-required error, convert to a ToolException with a link or instructions (see examples/tools.wrap_mcp_authenticate_tool)

## Validation Gates (executable)

Level 1 — Syntax/Style (run locally):

```
ruff check --fix && mypy .
```

Level 2 — Unit Tests (run locally):

```
# run tests (pytest) - fast smoke tests
uv run pytest tests/ -q
```

Level 3 — Manual / Integration:

```
# 1) SAFE_MODE demo (no Action Server required)
make demo-actionserver-agent

# 2) Live demo (requires Action Server running and ACTION_SERVER_URL pointing to it)
ACTION_SERVER_URL=http://localhost:8282 SAFE_MODE=false make demo-actionserver-agent
```

Notes: the repo uses `examples/oap-langgraph-tools-agent/pyproject.toml` for dependency reference; mirror pins if adding new runtime deps.

## Tests to add (minimal)

- tests/test_wrapper_safe_mode.py — ensure when SAFE_MODE=true, wrappers return simulated responses and do not call network code
- tests/test_wrapper_confirmation.py — ensure mutating tools require explicit AUTO_APPROVE or confirmation
- tests/test_get_file_contents_patch.py — test that file-edit flow returns a proposed patch given a sample content

## Implementation examples & snippets (real code references)

- Instantiate ActionServerToolkit (from `examples/lang_sema4_example.py`):

```
from langchain_sema4 import ActionServerToolkit
toolkit = ActionServerToolkit(url=ACTION_SERVER_URL, report_trace=True)
sema4_tools = toolkit.get_tools()
model_with_tools = model.bind_tools(sema4_tools)
tool_node = ToolNode(sema4_tools)
```

- Wrap MCP auth errors like `examples/oap-langgraph-tools-agent/tools_agent/utils/tools.wrap_mcp_authenticate_tool` to present friendly messages to the LLM/user.

## Context Table (all referenced files and why)

| File | Purpose |
|---|---|
| `examples/oap-langgraph-tools-agent/tools_agent/agent.py` | Agent wiring pattern and GraphConfig pydantic schema example |
| `examples/oap-langgraph-tools-agent/tools_agent/utils/tools.py` | Tool wrapping utilities and error handling examples |
| `examples/lang_sema4_example.py` | How to instantiate and use ActionServerToolkit and ToolNode |
| `INITIALS/actionserver_agent_initial.md` | Feature source and acceptance criteria |

## Risk / Gotchas

- The ActionServer Toolkit package (`langchain_sema4` or similar) may change function signatures; follow `lang_sema4_example.py` usage exactly and test the common tools listed in Acceptance Criteria.
- If the toolkit needs authentication, the agent must gracefully surface the interaction flow (see MCP error handling pattern) rather than crash.
- Non-interactive environments must rely on `AUTO_APPROVE=true` for mutating ops; document clearly in README.

## Quality checklist

- [ ] All necessary context included — DONE
- [ ] Validation gates are executable by AI — DONE (commands included)
- [ ] References existing patterns — DONE (example files cited)
- [ ] Clear implementation path — DONE (pseudocode, tasks)
- [ ] Error handling documented — DONE

## Score (confidence)

- Confidence: 8/10 — This PRP is comprehensive enough for a one-pass implementation given the repo examples and the `lang_sema4_example.py` usage. Minor adjustments may be needed for exact toolkit auth behaviors or schema mismatches.

## Next steps (developer tasks)

1. Create the package skeleton and implement the guardrail wrappers and tool wrapping.
2. Add README and `.env.example`.
3. Add Makefile demo target and tests.
4. Run validation gates and iterate until green.

---

Save path: PRPs/actionserver_agent_initial/actionserver_agent_initial_prp.md
