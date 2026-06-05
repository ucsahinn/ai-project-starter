# Skill Structure

```text
.agents/skills/context-engineering-project-starter/
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
|-- references/
|   |-- agent-instruction-files.md
|   |-- context-engineering.md
|   |-- domain-starter-packs.md
|   |-- output-templates.md
|   |-- project-documents.md
|   |-- quality-rubric.md
|   |-- source-map.md
|   `-- vibe-coding.md
|-- scripts/
|   `-- create_starter.py
`-- templates/
```

## Design

- `SKILL.md` stays short and handles routing, workflow, mode selection, and stop conditions.
- `references/` contains on-demand procedural knowledge and current source maps.
- `templates/` contains starter document skeletons.
- `scripts/create_starter.py` materializes selected templates safely.

## Progressive Disclosure

Codex should load only the files needed for the user's request. For example:

- SaaS project: load `domain-starter-packs.md` and SaaS templates.
- Agent context request: load `agent-instruction-files.md` and agent templates.
- Context audit: load `quality-rubric.md` and `output-templates.md`.
- Research-backed update: load `source-map.md` first, then refresh official sources.
