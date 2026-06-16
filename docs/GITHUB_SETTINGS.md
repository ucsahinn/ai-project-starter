# GitHub Settings

Use this page when updating the public repository after the local files are verified.

## Repository

- New repository name: `ai-project-starter`
- Legacy name: `context-engineering-project-starter`
- Visibility: public
- Website: leave blank unless a dedicated documentation site is published.
- Social preview image: `assets/social-preview.svg`

## About Description

AI Project Starter: documentation-first starter kit for AI-coded projects, project context, guardrails, and agent instruction files.

## Topics

`ai-project-starter`, `project-template`, `context-engineering`, `ai-coding`, `ai-agents`, `agent-instructions`, `codex`, `cursor`, `claude-code`, `documentation`, `developer-tools`, `security-guardrails`, `vibe-coding`, `starter-template`, `prompt-engineering`

## Checks

Run locally before changing GitHub settings:

```powershell
npm run check
git diff --check
gitleaks detect --redact --no-banner --no-git --verbose
```

`npm run check` includes the repository validator and a dry-run starter materializer smoke test. It must pass before changing GitHub metadata, tagging, pushing, or publishing release notes.

GitHub CLI metadata updates require a valid authenticated `gh` session. Do not store tokens in this repository.
