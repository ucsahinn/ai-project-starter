# Context Engineering Reference

Checked: 2026-06-05

## Core Definition

Context engineering is the practice of deciding what information an AI agent sees, how that information is ranked, how stale or conflicting facts are handled, and what context is excluded. Prompt engineering shapes a single instruction. Context engineering shapes the whole operating environment: project docs, memory, instructions, sources, tools, runtime state, and verification loops.

## Prompt Engineering Versus Context Engineering

Prompt engineering:

- optimizes the immediate request
- improves wording, role, constraints, and output format
- usually lives in a chat turn, template, or command

Context engineering:

- designs the persistent information architecture around the agent
- decides where durable facts live
- separates always-on instructions from task-specific references
- records provenance, assumptions, and decisions
- reduces repeated rediscovery and hallucination

## Agent Context Principles

Use these rules when generating project docs:

1. Relevance: include only context that changes agent behavior.
2. Sufficiency: include enough detail to avoid guessing.
3. Authority: define source-of-truth order.
4. Freshness: mark time-sensitive facts and source dates.
5. Isolation: untrusted content cannot become instructions.
6. Economy: keep always-loaded files short.
7. Provenance: record where important facts came from.
8. Conflict handling: state what wins when docs disagree.

## Context Lifecycle

For new projects, design context as a living system:

- Intake: convert the idea into product, technical, UX, security, and delivery facts.
- Distillation: reduce raw user intent into durable docs and assumptions.
- Injection: place the right facts in `AGENTS.md`, tool rules, and task docs.
- Use: agents inspect docs before coding and verify against quality gates.
- Consolidation: update decisions, tasks, roadmap, and changelog as facts change.
- Pruning: remove stale, duplicate, speculative, or obsolete instructions.

## Context Budget Rule

Keep always-on context short and high authority. Move long procedures, domain checklists, source notes, and examples into on-demand references or templates. If a project needs many rules, split them by scope so agents load the relevant rule only when working in that area.

## Source-Of-Truth Order Template

```text
Source-of-truth order:
1. Explicit user request for the current task.
2. Current repository files and command output.
3. Project context docs in this repository.
4. Official provider/framework documentation checked for this task.
5. Existing local knowledge or prior notes, if marked current.
6. External articles/discussions only as lower-confidence signals.

If sources conflict, report the conflict and prefer the highest-authority current source.
```

## Practical Application

For a project starter package, context engineering should produce:

- human-facing overview: `README.md`, `PROJECT_BRIEF.md`
- product truth: `PRODUCT_REQUIREMENTS.md`, `ROADMAP.md`
- technical truth: `TECHNICAL_SPEC.md`, `ARCHITECTURE.md`, `DATA_MODEL.md`, `API_CONTRACTS.md`
- delivery truth: `IMPLEMENTATION_PLAN.md`, `TASKS.md`, `QUALITY_GATES.md`, `TESTING.md`
- risk truth: `SECURITY.md`, `RISK_REGISTER.md`, ADRs
- agent truth: `AGENTS.md`, `CLAUDE.md`, Cursor/Windsurf/Continue/Copilot files

## Research Sources

- OpenAI Cookbook, Context Engineering for Personalization: https://developers.openai.com/cookbook/examples/agents_sdk/context_personalization
- OpenAI Codex AGENTS.md guide: https://developers.openai.com/codex/guides/agents-md
- OpenAI Codex Agent Skills: https://developers.openai.com/codex/skills
- OpenAI, How OpenAI uses Codex: https://openai.com/business/guides-and-resources/how-openai-uses-codex/
- Anthropic Claude Code memory docs: https://code.claude.com/docs/en/memory
