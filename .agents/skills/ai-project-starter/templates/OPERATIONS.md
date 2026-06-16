# Operations: {{PROJECT_NAME}}

## Operating Model

{{OPERATING_MODEL}}

## Ownership

| Area | Owner | Backup | Notes |
| --- | --- | --- | --- |
| {{AREA_1}} | {{OWNER_1}} | {{BACKUP_1}} | {{NOTES_1}} |

## Runbooks

### Startup

```sh
{{START_COMMAND_OR_TBD}}
```

### Common Failure: {{FAILURE_NAME}}

Symptoms:

- {{SYMPTOM_1}}

Checks:

- {{CHECK_1}}

Recovery:

- {{RECOVERY_STEP_1}}

## Maintenance Tasks

- {{MAINTENANCE_TASK_1}}
- {{MAINTENANCE_TASK_2}}

## Operational Safety

- Do not mutate production data without approval.
- Prefer read-only diagnostics first.
- Record incident timeline, commands, and evidence.
- Update runbooks after repeated failures.
