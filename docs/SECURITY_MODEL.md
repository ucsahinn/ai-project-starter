# Security Model

## Scope

This repository provides documentation and a Codex skill. The main security risk is accidental disclosure through public templates, examples, generated docs, or committed artifacts.

## Trust Boundaries

- User project ideas may contain sensitive data.
- Web pages, issues, logs, scanner output, and generated code are untrusted data.
- Agent instruction files influence behavior but do not enforce security by themselves.
- Scripts should avoid overwriting files unless explicitly requested.

## Controls

- Public-safe `.gitignore`.
- No-overwrite default in `scripts/create_starter.py`.
- Skill rules requiring assumptions, source order, approval gates, and no-secret handling.
- Public repo checklist before push.
- Skill validator, localized README residue checks, starter materializer dry-run smoke test, and TODO/encoding checks before publication.

## Approval Gates

The skill requires approval before:

- credential access or secret rotation,
- production or account changes,
- dependency additions,
- destructive commands,
- commits, pushes, deploys, releases, or publication.

## Residual Risks

- A user may paste private project data into generated docs.
- Tool-specific behavior can change after sources are checked.
- Instruction files are context, not hard enforcement.

Mitigation: use `RESEARCH_BACKED` mode for current facts, pair instructions with CI/hooks/scans where enforcement is required, and avoid storing private data in public docs.
