# Usage

## Core Request

```text
Use the context-engineering-project-starter skill.
Project idea: [describe the product].
Mode: CREATE_FILES.
Quality: enterprise starter.
```

## Modes

| Mode | Use when |
| --- | --- |
| `PROMPT_ONLY` | The user wants only a prompt or final text. |
| `DOCS_ONLY` | The user wants Markdown contents but no file writes. |
| `PLAN_ONLY` | The user wants a document generation plan before file writes. |
| `CREATE_FILES` | The user wants actual starter files created. |
| `AUDIT_CONTEXT` | Existing project docs need review. |
| `REPAIR_CONTEXT` | Existing weak docs need targeted repair. |
| `ENTERPRISE_STARTER` | Security, testing, operations, observability, ADRs, and quality gates are required. |
| `VIBE_GUARDRAILS` | The goal is to prevent AI slop, scope creep, duplicate code, and architecture drift. |
| `RESEARCH_BACKED` | Tool behavior, security, or best-practice claims must be current and source-backed. |

## Domain Packs

Use one or more:

- SaaS
- cybersecurity
- AI product
- API
- web app
- mobile
- desktop
- data product
- internal tool
- library/CLI

## Good Example

```text
Use context-engineering-project-starter in CREATE_FILES + ENTERPRISE_STARTER + VIBE_GUARDRAILS mode.

Project idea:
A SaaS cybersecurity product for small security teams. It imports scanner findings, groups them by tenant, assigns remediation tasks, uses AI to draft safe remediation plans, supports RBAC and audit logs, and produces executive reports.

Assume a web app and API. Make reasonable assumptions, write them in the docs, and do not ask more than 3 blocking questions.
```

## Audit Example

```text
Use AUDIT_CONTEXT mode. Inspect the existing project docs and report missing, conflicting, stale, or weak context that would cause an AI coding agent to make poor implementation decisions.
```
