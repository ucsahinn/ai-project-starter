# Output Templates And Modes

## Mode: PLAN_ONLY

Output:

```md
## Context Starter Plan

Project summary:
- ...

Assumptions:
- ...

Recommended files:
| File | Why needed | Priority |
| --- | --- | --- |

Generation order:
1. ...

Risks:
- ...

Stop:
No files written. Wait for explicit approval before creating files.
```

## Mode: DOCS_ONLY

Output file-labeled sections:

````md
## README.md

```markdown
...
```

## AGENTS.md

```markdown
...
```
````

Do not include commentary unless the user requested it.

## Mode: CREATE_FILES

Actions:

1. Inspect existing docs first.
2. Create directories as needed.
3. Write selected files from templates and project facts.
4. Re-read created files or run a markdown/file listing check.
5. Report created files, assumptions, verification, and open questions.

## Template-To-Path Map

Most templates map directly to root-level Markdown files. Use these special mappings:

| Template | Output path |
| --- | --- |
| `claude-project-rule.md` | `.claude/rules/project.md` |
| `cursor-project.mdc` | `.cursor/rules/project.mdc` |
| `cursorrules` | `.cursorrules` |
| `devin-project-rule.md` | `.devin/rules/project.md` |
| `windsurfrules` | `.windsurfrules` |
| `continue-rules.md` | `.continue/rules.md` or `.continue/rules/project.md` |
| `copilot-instructions.md` | `.github/copilot-instructions.md` |
| `github-project.instructions.md` | `.github/instructions/project.instructions.md` |
| `aider-conf.yml` | `.aider.conf.yml` |
| `PROJECT_CONTEXT.md` | `.codex/PROJECT_CONTEXT.md` |
| `WORKING_RULES.md` | `.codex/WORKING_RULES.md` |
| `adr-0001-architecture-style.md` | `docs/adr/0001-architecture-style.md` |
| `adr-0002-tech-stack.md` | `docs/adr/0002-tech-stack.md` |
| `adr-0003-security-boundaries.md` | `docs/adr/0003-security-boundaries.md` |
| `adr-0004-data-storage.md` | `docs/adr/0004-data-storage.md` |
| `adr-0005-testing-strategy.md` | `docs/adr/0005-testing-strategy.md` |

When writing files, create parent directories first. Do not overwrite existing files without reading and preserving existing decisions.

## Mode: AUDIT_CONTEXT

Lead with findings:

```md
## Findings

High:
- [file] Problem, impact, fix.

Medium:
- ...

Low:
- ...

## Coverage Matrix

| Area | Current state | Gap | Recommendation |
| --- | --- | --- | --- |

## Repair Plan

1. ...
```

## Mode: REPAIR_CONTEXT

Rules:

- Preserve existing decisions.
- Patch weak sections instead of rewriting everything.
- Mark unresolved conflicts.
- Add missing quality/security/source-of-truth sections.

Final report:

```md
Updated:
- ...

Verification:
- ...

Remaining gaps:
- ...
```

## Mode: ENTERPRISE_STARTER

Required coverage:

- product brief and PRD
- architecture and technical spec
- API/data/UI docs where relevant
- security baseline and threat boundaries
- testing strategy and quality gates
- operations, observability, deployment, rollback
- ADRs for stack, architecture style, data storage, security boundaries, testing
- agent instruction files
- relevant domain starter pack files from `references/domain-starter-packs.md`

## Mode: VIBE_GUARDRAILS

Prioritize these files:

- `AGENTS.md`
- `PROJECT_BRIEF.md`
- `PRODUCT_REQUIREMENTS.md`
- `IMPLEMENTATION_PLAN.md`
- `TASKS.md`
- `QUALITY_GATES.md`
- `SECURITY.md`
- `TESTING.md`

Required guardrail sections:

- first milestone
- non-goals
- no duplicate systems rule
- no broad refactor rule
- verification-before-done rule
- approval-required actions
- current task boundary

## Mode: RESEARCH_BACKED

Use when tool behavior, security policy, deployment platform, framework versions, model/provider capabilities, legal/compliance expectations, or AI-agent safety claims may have changed.

Output:

- concise source list with authority and date checked when commentary is allowed
- explicit assumptions
- generated docs or plan
- unresolved uncertainty

Rules:

- Prefer official docs.
- Use secondary sources only for risk patterns or practical examples.
- Do not present blog/community claims as official behavior.

## Standard File Sections

Use these selectively:

- Purpose
- Scope
- Non-goals
- Assumptions
- Requirements
- Technical decisions
- Risks
- Acceptance criteria
- Agent instructions
- Verification method
- Open questions

Do not paste all sections into every file. Choose sections that match the file purpose.
