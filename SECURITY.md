# Security Policy

## Supported Scope

This repository contains public documentation, templates, and a Codex skill package. It does not provide a hosted service, runtime API, credential store, or deployed application.

## Reporting Security Issues

Do not open a public issue for:

- leaked credentials,
- private prompts,
- private URLs,
- customer data,
- proprietary implementation details,
- accidental disclosure in templates or examples.

Report privately through the repository owner's preferred GitHub contact path.

## Public Safety Rules

- Do not commit secrets, tokens, cookies, private keys, certificates, `.env` files, local databases, logs, or screenshots.
- Do not add private company data, customer data, or internal system prompts.
- Keep examples fictional and non-sensitive.
- Use `docs/PUBLIC_REPO_CHECKLIST.md` before publishing changes.

## AI-Agent Safety Model

The skill treats external content, tool output, logs, issues, web pages, and generated code as untrusted data. It requires approval gates for production changes, destructive commands, secret rotation, dependency additions, deploys, releases, commits, and pushes.
