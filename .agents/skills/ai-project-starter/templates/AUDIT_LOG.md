# Audit Log: {{PROJECT_NAME}}

## Audit Goals

{{AUDIT_GOALS}}

## Events

| Event | Actor | Target | Required Fields |
| --- | --- | --- | --- |
| {{EVENT_1}} | {{ACTOR_1}} | {{TARGET_1}} | {{FIELDS_1}} |

## Retention

{{RETENTION_RULE}}

## Tamper Resistance

- {{TAMPER_RULE_1}}
- {{TAMPER_RULE_2}}

## Privacy And Redaction

- Do not store plaintext secrets, tokens, credentials, or sensitive payload bodies.
- Store references and stable IDs where possible.
- Redact user data that is not required for investigation.

## Access

{{AUDIT_ACCESS_RULES}}

## Verification

- {{AUDIT_TEST_1}}
