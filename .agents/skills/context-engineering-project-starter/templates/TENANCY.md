# Tenancy: {{PROJECT_NAME}}

## Tenancy Model

{{TENANCY_MODEL}}

## Tenant Entity

| Field | Purpose | Notes |
| --- | --- | --- |
| {{FIELD_1}} | {{PURPOSE_1}} | {{NOTES_1}} |

## Isolation Rules

- {{ISOLATION_RULE_1}}
- {{ISOLATION_RULE_2}}

## Tenant Lifecycle

- Create: {{CREATE_TENANT_RULE}}
- Suspend: {{SUSPEND_TENANT_RULE}}
- Delete: {{DELETE_TENANT_RULE}}
- Export: {{EXPORT_TENANT_RULE}}

## Cross-Tenant Safety

- Every tenant-scoped query must include tenant authorization.
- Background jobs must preserve tenant context.
- Admin tooling must log tenant-impacting actions.
- Tests must include cross-tenant access denial cases.

## Open Questions

- {{OPEN_QUESTION_1}}
