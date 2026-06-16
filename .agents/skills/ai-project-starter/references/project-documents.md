# Project Document Selection

Checked: 2026-06-05

## Selection Rule

Create the smallest document set that gives future agents enough product, technical, security, quality, and delivery context to start coding without inventing missing architecture. Do not create every possible file unless the user requests an enterprise starter or the risk profile requires it.

## Core Documents

| File | Purpose | Create when |
| --- | --- | --- |
| `README.md` | Human entrypoint, project purpose, quickstart placeholder | Almost always |
| `PROJECT_BRIEF.md` | Product vision, users, problem, scope, non-goals | Almost always |
| `PRODUCT_REQUIREMENTS.md` | Requirements, user stories, acceptance criteria | Product/app work |
| `TECHNICAL_SPEC.md` | Stack, components, interfaces, constraints | Any buildable software |
| `ARCHITECTURE.md` | System shape, boundaries, runtime/deployment views | Any non-trivial app |
| `IMPLEMENTATION_PLAN.md` | Phased plan before coding | Most projects |
| `TASKS.md` | Actionable backlog | Most projects |
| `DECISIONS.md` | Decision index and unresolved decisions | Most projects |
| `SECURITY.md` | Security baseline and approval gates | Any real app |
| `TESTING.md` | Test strategy and required checks | Any real app |
| `QUALITY_GATES.md` | Done criteria, anti-slop gates, verification | Any AI-assisted project |

## Conditional Documents

| Project trait | Add |
| --- | --- |
| API/backend | `API_CONTRACTS.md`, `DATA_MODEL.md` |
| UI/web/mobile | `UI_UX_GUIDELINES.md`, `DESIGN_SYSTEM.md` |
| Deployment | `DEPLOYMENT.md`, `OPERATIONS.md`, `OBSERVABILITY.md` |
| Enterprise/security-sensitive | `RISK_REGISTER.md`, `docs/adr/*.md`, threat model docs |
| AI product | `PROMPT_POLICY.md`, `MODEL_USAGE.md`, `EVALS.md`, `GUARDRAILS.md` |
| SaaS | `TENANCY.md`, `AUTH_RBAC.md`, `BILLING.md`, `AUDIT_LOG.md` |
| Cybersecurity | `THREAT_MODEL.md`, `ABUSE_CASES.md`, `SECURE_DEFAULTS.md`, `SECRET_HANDLING.md` |
| API | `OPENAPI_PLAN.md`, `RATE_LIMITING.md` |
| Web app | `ROUTING.md`, `SEO_ACCESSIBILITY_PERFORMANCE.md` |
| Desktop | `INSTALLER.md`, `UPDATER.md`, `SIGNING.md`, `OS_INTEGRATION.md` |
| Mobile | `APP_FLOWS.md`, `NAVIGATION.md`, `OFFLINE_STRATEGY.md`, `PERMISSIONS.md` |
| Data product | `DATA_GOVERNANCE.md` |
| Library/CLI | `PUBLIC_API.md`, `RELEASE.md` |

## Recommended Enterprise Starter

Use for enterprise, cybersecurity, SaaS, auth-heavy, AI-agent, payment, regulated, or production-adjacent projects:

- `README.md`
- `AGENTS.md`
- `PROJECT_BRIEF.md`
- `PRODUCT_REQUIREMENTS.md`
- `TECHNICAL_SPEC.md`
- `ARCHITECTURE.md`
- `IMPLEMENTATION_PLAN.md`
- `TASKS.md`
- `ROADMAP.md`
- `DECISIONS.md`
- `SECURITY.md`
- `TESTING.md`
- `QUALITY_GATES.md`
- `DATA_MODEL.md`
- `API_CONTRACTS.md`
- `UI_UX_GUIDELINES.md` if UI exists
- `DESIGN_SYSTEM.md` if UI exists
- `DEPLOYMENT.md`
- `OPERATIONS.md`
- `OBSERVABILITY.md`
- `RISK_REGISTER.md`
- `CHANGELOG.md`
- `docs/adr/0001-architecture-style.md`
- `docs/adr/0002-tech-stack.md`
- `docs/adr/0003-security-boundaries.md`
- `docs/adr/0004-data-storage.md`
- `docs/adr/0005-testing-strategy.md`

Add relevant domain-pack files from `references/domain-starter-packs.md`.

## Document Boundaries

- `PROJECT_BRIEF.md`: why, who, scope, non-goals.
- `PRODUCT_REQUIREMENTS.md`: what must work and how users experience it.
- `TECHNICAL_SPEC.md`: how the system will be built.
- `ARCHITECTURE.md`: structural boundaries and long-lived system decisions.
- `DECISIONS.md`: index of decisions; ADR files contain formal records.
- `QUALITY_GATES.md`: checks that decide whether an implementation is acceptable.
- `AGENTS.md`: durable agent behavior, commands, safety, and source order.

## Documentation Patterns

Architecture docs should cover goals, constraints, context/scope, solution strategy, building blocks, runtime view, deployment view, cross-cutting concepts, quality requirements, risks, and glossary when the project is large enough. Keep small projects lean.

ADR docs should record status, context, decision, alternatives considered, and consequences. Create an ADR when a decision is expensive, hard to reverse, security-sensitive, or likely to be debated later.

## Research Sources

- arc42 template overview: https://arc42.org/overview
- ADR resources and templates: https://www.adr.zone/
- Atlassian PRD template guidance: https://www.atlassian.com/software/confluence/templates/product-requirements
- AGENTS.md open format: https://agents.md/
