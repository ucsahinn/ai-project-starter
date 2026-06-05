# Agent Instruction Files

Checked: 2026-06-05

## Design Rule

Use one shared root instruction file when possible, then thin tool-specific adapters. Avoid duplicating long rules across many files. Prefer `AGENTS.md` for shared project rules, and create tool-specific files when the user uses that tool or asks for broad agent compatibility.

## Supported Files And Current Notes

| Tool | File(s) | Notes |
| --- | --- | --- |
| Codex | `AGENTS.md`; repo skills in `.agents/skills/<name>/SKILL.md` | Codex discovers `AGENTS.md` in global and project scopes and uses skill `description` for implicit invocation. |
| Claude Code | `CLAUDE.md`, `.claude/CLAUDE.md`, `.claude/rules/*.md` | Claude Code reads `CLAUDE.md`, not `AGENTS.md`; import `@AGENTS.md` to avoid duplication. Keep each CLAUDE.md concise, preferably under 200 lines. |
| Cursor | `.cursor/rules/*.mdc`, `AGENTS.md`, `.cursorrules` legacy | Project Rules are preferred; `.cursorrules` is supported but legacy/deprecated. |
| Windsurf / Devin Desktop Cascade | `.devin/rules/*.md`, `.windsurf/rules/*.md`, `AGENTS.md`, `.windsurfrules` legacy | Prefer `.devin/rules`; legacy Windsurf paths can be included for compatibility. |
| Continue | `.continue/rules/*` or `.continue/rules.md` | Local rules are version-controlled and best for project-specific conventions. |
| GitHub Copilot | `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`, `AGENTS.md` | Repo-wide file gives guidance for build/test/validation; path-specific instructions use frontmatter. |
| Aider | `AGENTS.md` via `.aider.conf.yml` or `--read`; `CONVENTIONS.md` via `/read` or `--read` | Aider can read convention files as read-only context and cache them when prompt caching is enabled. |

## Agent File Contents

Every agent instruction file should include:

- project mission in 2-4 lines
- source-of-truth order
- setup/build/test/lint/run commands if known
- architecture and directory map if known
- scope and non-goals
- safety and secret handling
- quality gates
- approval-required actions
- final report expectations

They should not rely on instruction text as a hard security control. For hard enforcement, pair instructions with hooks, CI, sandboxing, permissions, tests, or policy.

## Adapter Patterns

`CLAUDE.md`:

```md
@AGENTS.md

## Claude Code Notes
- Use plan mode for broad or security-sensitive changes.
- Keep `CLAUDE.md` concise; move detailed procedures to docs or skills.
```

Cursor project rule:

```mdc
---
description: Project-wide engineering rules
alwaysApply: true
---

Follow `AGENTS.md` as the shared project instruction source. Prefer existing architecture, tests, and quality gates before adding new patterns.
```

Windsurf/Devin rule:

```md
# Project Rules

Follow `AGENTS.md` as the shared project instruction source. Use the current milestone and quality gates before coding.
```

Devin/Cascade rule frontmatter:

```md
---
trigger: model_decision
description: Project context and engineering guardrails for {{PROJECT_NAME}}
---

Follow `AGENTS.md` as the shared project instruction source. Load this rule for broad planning, architecture, security, testing, and context repair work.
```

Continue rule:

```md
# Project Rules

Use `AGENTS.md`, `PROJECT_BRIEF.md`, `TECHNICAL_SPEC.md`, and `QUALITY_GATES.md` as project context before changing code.
```

Copilot instructions:

```md
# Repository Instructions

Read `AGENTS.md` first. Use the documented setup, build, test, and validation commands. Keep changes within the current task and report verification evidence.
```

Copilot path-specific instructions:

```md
---
applyTo: "src/api/**"
---

Follow `API_CONTRACTS.md`, `SECURITY.md`, and `QUALITY_GATES.md` for API changes.
```

Aider config:

```yaml
read:
  - AGENTS.md
  - CONVENTIONS.md
```

## Anti-Duplication Rule

Do not paste the full content of every project doc into every agent instruction file. Cross-reference stable docs and include only the rules that must always be visible.

## Research Sources

- OpenAI Codex AGENTS.md guide: https://developers.openai.com/codex/guides/agents-md
- OpenAI Codex Agent Skills: https://developers.openai.com/codex/skills
- AGENTS.md open format: https://agents.md/
- Claude Code memory docs: https://code.claude.com/docs/en/memory
- Cursor Rules docs: https://cursor.com/docs/rules
- Devin Desktop Cascade memories and rules: https://docs.devin.ai/desktop/cascade/memories
- Continue rules docs: https://docs.continue.dev/customize/rules
- Aider conventions docs: https://aider.chat/docs/usage/conventions.html
- GitHub Copilot repository instructions: https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions
