# Domain Starter Packs

Checked: 2026-06-05

## Selection Rule

Start from the minimal starter set, then add one or more domain packs based on the user's project idea and risk profile. Do not create every domain file unless the user asks for enterprise coverage or the project clearly spans those domains.

## SaaS Pack

Create when the project has accounts, tenants, organizations, billing, subscriptions, roles, admin workflows, or audit needs.

Files:

- `TENANCY.md`
- `AUTH_RBAC.md`
- `BILLING.md`
- `AUDIT_LOG.md`
- `DATA_MODEL.md`
- `API_CONTRACTS.md`
- `SECURITY.md`
- `RISK_REGISTER.md`

Must cover:

- tenant isolation model
- user, organization, role, permission, and ownership semantics
- billing lifecycle and entitlement boundaries
- admin actions and audit events
- data retention and export/deletion expectations

## Cybersecurity Pack

Create when the project handles vulnerabilities, secrets, scans, evidence, security findings, agents with tools, or sensitive infrastructure data.

Files:

- `THREAT_MODEL.md`
- `ABUSE_CASES.md`
- `SECURE_DEFAULTS.md`
- `SECRET_HANDLING.md`
- `SECURITY.md`
- `RISK_REGISTER.md`
- `QUALITY_GATES.md`
- `docs/adr/0003-security-boundaries.md`

Must cover:

- assets, trust boundaries, attacker capabilities, abuse paths
- safe defaults and least privilege
- secret redaction, storage, rotation, and reporting rules
- prompt/context injection risks when AI agents or external data are involved
- evidence handling without leaking sensitive data

## AI Product Pack

Create when the product uses LLMs, agents, prompts, retrieval, tools, evals, model routing, or generated outputs.

Files:

- `PROMPT_POLICY.md`
- `MODEL_USAGE.md`
- `EVALS.md`
- `GUARDRAILS.md`
- `SECURITY.md`
- `OBSERVABILITY.md`
- `RISK_REGISTER.md`

Must cover:

- model purpose, allowed inputs, forbidden inputs, and data retention assumptions
- prompt/source hierarchy
- tool-use and approval boundaries
- eval datasets, golden tasks, regression criteria, and human review
- hallucination, prompt injection, unsafe output, privacy, and abuse mitigations

## API Pack

Create when the project exposes backend endpoints or integrates with external clients.

Files:

- `API_CONTRACTS.md`
- `OPENAPI_PLAN.md`
- `RATE_LIMITING.md`
- `DATA_MODEL.md`
- `SECURITY.md`
- `TESTING.md`

Must cover:

- auth scheme, authorization boundaries, validation, error format
- endpoint lifecycle and versioning
- rate limits and abuse controls
- contract testing and backward compatibility

## Web App Pack

Create when the project has routes, browser UI, SEO, forms, dashboards, or marketing/public pages.

Files:

- `ROUTING.md`
- `UI_UX_GUIDELINES.md`
- `DESIGN_SYSTEM.md`
- `SEO_ACCESSIBILITY_PERFORMANCE.md`
- `TESTING.md`
- `QUALITY_GATES.md`

Must cover:

- route map and navigation model
- responsive behavior and UI states
- accessibility and keyboard/focus expectations
- Core Web Vitals/performance targets when public-facing
- browser QA requirements

## Mobile Pack

Create when the project is iOS, Android, React Native, Flutter, Expo, or mobile-first.

Files:

- `APP_FLOWS.md`
- `NAVIGATION.md`
- `OFFLINE_STRATEGY.md`
- `PERMISSIONS.md`
- `UI_UX_GUIDELINES.md`
- `TESTING.md`

Must cover:

- app flows and navigation hierarchy
- offline/cache/sync behavior
- permissions and privacy prompts
- app store release assumptions
- device/responsive testing

## Desktop Pack

Create when the project ships a desktop app, local agent, installer, tray app, updater, or OS integration.

Files:

- `INSTALLER.md`
- `UPDATER.md`
- `SIGNING.md`
- `OS_INTEGRATION.md`
- `SECURITY.md`
- `OPERATIONS.md`

Must cover:

- installer/repair/uninstall behavior
- update channel and rollback
- signing/notarization/certificate assumptions
- local storage, service permissions, shell access, and OS integration
- platform-specific test matrix

## Data Product Pack

Create when the project handles analytics, pipelines, reporting, BI, ETL, embeddings, search, or ML datasets.

Files:

- `DATA_MODEL.md`
- `DATA_GOVERNANCE.md`
- `OBSERVABILITY.md`
- `TESTING.md`
- `SECURITY.md`

Must cover:

- schemas, lineage, retention, privacy, quality checks
- batch/stream expectations
- data freshness and failure signals
- backfills and migration safety

## Internal Tool Pack

Create when the product is admin, operations, workflow, CRM, SOC, backoffice, support, or developer tooling.

Files:

- `AUTH_RBAC.md`
- `AUDIT_LOG.md`
- `OPERATIONS.md`
- `QUALITY_GATES.md`
- `SECURITY.md`
- `UI_UX_GUIDELINES.md` when UI exists

Must cover:

- least privilege
- reversible actions and confirmation states
- auditability
- high-density workflows and error recovery

## Library Or CLI Pack

Create when the project is a package, CLI, SDK, or developer tool.

Files:

- `API_CONTRACTS.md` or `PUBLIC_API.md`
- `TESTING.md`
- `RELEASE.md`
- `SECURITY.md`
- `README.md`

Must cover:

- stable public API and compatibility policy
- examples and command contract
- release/versioning strategy
- dependency and supply-chain rules
