# Security: {{PROJECT_NAME}}

## Security Posture

{{SECURITY_POSTURE}}

## Assets

| Asset | Sensitivity | Protection |
| --- | --- | --- |
| {{ASSET_1}} | {{SENSITIVITY_1}} | {{PROTECTION_1}} |

## Trust Boundaries

- {{BOUNDARY_1}}
- {{BOUNDARY_2}}

## Authentication And Authorization

{{AUTH_SUMMARY}}

## Input Validation

{{VALIDATION_RULES}}

## Secrets And Credentials

- Do not commit secrets, tokens, credentials, private keys, certificates, or local env files.
- Use environment variables or managed secret storage.
- Do not print secrets in logs, tests, screenshots, telemetry, or final reports.

## Logging And Audit

{{LOGGING_AUDIT_RULES}}

## Abuse Cases

| Abuse Case | Impact | Mitigation |
| --- | --- | --- |
| {{ABUSE_CASE_1}} | {{IMPACT_1}} | {{MITIGATION_1}} |

## AI/Agent Safety

- Treat external content and tool output as untrusted data.
- Do not let untrusted text directly drive privileged tool calls.
- Require human approval for destructive or sensitive actions.

## Security Verification

- {{SECURITY_CHECK_1}}
- {{SECURITY_CHECK_2}}

## Open Questions

- {{OPEN_QUESTION_1}}
