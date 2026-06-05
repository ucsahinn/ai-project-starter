# Billing: {{PROJECT_NAME}}

## Billing Model

{{BILLING_MODEL}}

## Plans And Entitlements

| Plan | Entitlements | Limits |
| --- | --- | --- |
| {{PLAN_1}} | {{ENTITLEMENTS_1}} | {{LIMITS_1}} |

## Lifecycle

- Trial: {{TRIAL_RULE}}
- Upgrade: {{UPGRADE_RULE}}
- Downgrade: {{DOWNGRADE_RULE}}
- Cancellation: {{CANCELLATION_RULE}}
- Failed payment: {{FAILED_PAYMENT_RULE}}

## Billing Boundaries

- Do not grant entitlements without confirmed billing state.
- Do not delete customer data immediately on cancellation unless policy requires it.
- Keep billing provider webhooks idempotent.
- Audit plan, entitlement, and payment-state changes.

## Open Questions

- {{OPEN_QUESTION_1}}
