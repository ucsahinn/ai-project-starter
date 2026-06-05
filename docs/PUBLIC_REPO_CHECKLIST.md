# Public Repo Checklist

Use before committing or pushing.

## Secrets

- [ ] No `.env` or `.env.*` files.
- [ ] No API keys, tokens, cookies, private keys, certificates, PFX/P12 files, or credentials.
- [ ] No private URLs, internal endpoints, customer data, or proprietary prompts.

## Artifacts

- [ ] No logs, screenshots, Playwright reports, test output, coverage folders, build output, dependency folders, archives, installers, or local caches.
- [ ] No AI agent local state, memory, sessions, or scratch files.

## Documentation

- [ ] Examples are fictional and reusable.
- [ ] Tool-specific claims are backed by official docs or clearly marked as lower confidence.
- [ ] Security and quality rules do not claim guarantees.
- [ ] README, SECURITY, CONTRIBUTING, CHANGELOG, and docs are consistent.

## Git Hygiene

- [ ] `git status --short` reviewed.
- [ ] Explicit files staged.
- [ ] `git diff --cached` reviewed.
- [ ] Secret scan run when available.
- [ ] Remote branch verified after push.
