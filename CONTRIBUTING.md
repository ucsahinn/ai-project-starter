# Contributing

Contributions are welcome when they improve context engineering quality, source accuracy, skill usability, documentation clarity, or safety.

## Good Contributions

- Better project starter templates.
- Stronger domain starter packs.
- Better agent instruction adapters.
- Source-backed updates for Codex, Claude Code, Cursor, Continue, Copilot, Aider, or Devin/Windsurf behavior.
- Security and quality-gate improvements.
- Clearer examples.

## Rules

- Keep `SKILL.md` concise and move detail to `references/` or `templates/`.
- Do not add private data, secrets, proprietary prompts, local logs, screenshots, or internal URLs.
- Prefer official docs for tool-specific behavior.
- Mark assumptions and outdated-risk notes for version-sensitive facts.
- Validate the skill before opening a change.

## Validation

Run:

```sh
python C:\Users\ulasc\.codex\skills\.system\skill-creator\scripts\quick_validate.py .agents\skills\context-engineering-project-starter
```

Also run:

```sh
rg -n "TODO|\[TODO" .agents\skills\context-engineering-project-starter
rg -n "[^\x00-\x7F]" .agents\skills\context-engineering-project-starter
```
