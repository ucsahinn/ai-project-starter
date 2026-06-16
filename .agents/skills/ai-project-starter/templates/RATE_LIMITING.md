# Rate Limiting: {{PROJECT_NAME}}

## Goals

- Reduce abuse.
- Protect service reliability.
- Preserve fair tenant/user access.

## Dimensions

| Dimension | Limit | Window | Notes |
| --- | --- | --- | --- |
| {{DIMENSION_1}} | {{LIMIT_1}} | {{WINDOW_1}} | {{NOTES_1}} |

## Sensitive Operations

- {{SENSITIVE_OPERATION_1}}
- {{SENSITIVE_OPERATION_2}}

## Error Response

```json
{
  "error": {
    "code": "rate_limit_exceeded",
    "message": "Too many requests. Try again later.",
    "retryAfterSeconds": {{RETRY_AFTER_SECONDS}}
  }
}
```

## Bypass And Admin Rules

{{BYPASS_RULES}}

## Verification

- {{RATE_LIMIT_TEST_1}}
