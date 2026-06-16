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
npm run check
```

`npm run check` includes repository structure, skill metadata, public-safety, legacy-name, localized README residue checks, placeholder scans, and the starter materializer dry-run smoke test.
