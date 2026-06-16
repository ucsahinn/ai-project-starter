# Observability: {{PROJECT_NAME}}

## Goals

- Detect user-impacting failures quickly.
- Make debugging possible without exposing sensitive data.
- Track product and system health for the first milestone.

## Signals

| Signal | Purpose | Tool/Source |
| --- | --- | --- |
| Logs | {{LOG_PURPOSE}} | {{LOG_TOOL}} |
| Metrics | {{METRIC_PURPOSE}} | {{METRIC_TOOL}} |
| Traces | {{TRACE_PURPOSE}} | {{TRACE_TOOL}} |
| Alerts | {{ALERT_PURPOSE}} | {{ALERT_TOOL}} |

## Key Events

- {{EVENT_1}}
- {{EVENT_2}}

## Sensitive Data Rules

- Do not log secrets, tokens, credentials, private keys, session cookies, raw PII, or sensitive payloads.
- Redact identifiers when full values are not required.
- Prefer stable request IDs for correlation.

## Alert Conditions

- {{ALERT_CONDITION_1}}
- {{ALERT_CONDITION_2}}

## Dashboards

- {{DASHBOARD_1}}

## Open Questions

- {{OPEN_QUESTION_1}}
