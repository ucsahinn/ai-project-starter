# Changelog

## Unreleased

### Added

- Initial `ai-project-starter` Codex skill.
- Progressive-disclosure references for context engineering, vibe coding, project docs, agent instruction files, output modes, quality rubric, domain starter packs, and source map.
- Template set for core project docs, enterprise docs, agent adapters, ADRs, SaaS, cybersecurity, AI product, API, web, mobile, desktop, data, internal tool, and library/CLI work.
- `scripts/create_starter.py` to materialize safe starter document sets from bundled templates.
- Public repo documentation modeled after the renamed `prompt-architect` repository pattern.
- `npm run smoke:starter` to dry-run the starter materializer as part of `npm run check`.

### Security

- Added public safety checklist and security model.
- Added no-secret, no-private-data, and untrusted-context rules throughout the skill.
- Added localized README residue checks to keep public docs aligned across languages.
