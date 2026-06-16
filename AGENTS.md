# AI Project Starter Operating Rules

## Mission

This repository maintains a public Codex skill for creating AI-coding-ready project context, starter documentation, agent instruction files, and vibe-coding guardrails before implementation starts.

## Source Of Truth

1. Current user request.
2. Current repository files.
3. `.agents/skills/ai-project-starter/SKILL.md`.
4. Skill references and templates.
5. Official provider documentation for current tool behavior.
6. Public repo docs in `docs/`.

## Workflow

- Use `rg` or `rg --files` first.
- Keep `SKILL.md` concise; move detail to `references/`, `templates/`, or `scripts/`.
- Prefer official docs for tool-specific behavior.
- Keep examples fictional and public-safe.
- Validate the skill after edits.
- Preserve unrelated user work.

## Hard Boundaries

- Do not store secrets, credentials, private prompts, customer data, internal company data, logs, screenshots, private URLs, or local paths.
- Do not add generated build output, archives, installers, dependency folders, or local agent state.
- Do not commit, push, publish, release, or deploy unless explicitly asked.
- Do not broaden the repository into an app or service; this is a skill and documentation package.

## Validation

Run after skill edits:

```sh
npm run check
```

Before commit or push, inspect `git status --short`, stage explicit files, review `git diff --cached`, and run a secret scan when available.
