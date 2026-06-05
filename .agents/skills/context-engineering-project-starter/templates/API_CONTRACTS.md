# API Contracts: {{PROJECT_NAME}}

## API Goals

{{API_GOALS}}

## Auth Scheme

{{AUTH_SCHEME}}

## Global Rules

- Validate all inputs.
- Return consistent error responses.
- Do not expose internal errors or sensitive data.
- Apply authorization checks at the resource boundary.
- Rate-limit sensitive or abuse-prone endpoints.

## Endpoints

| Method | Path | Purpose | Auth | Request | Response |
| --- | --- | --- | --- | --- | --- |
| {{METHOD}} | `{{PATH}}` | {{PURPOSE}} | {{AUTH}} | {{REQUEST_MODEL}} | {{RESPONSE_MODEL}} |

## Error Format

```json
{
  "error": {
    "code": "{{ERROR_CODE}}",
    "message": "{{SAFE_MESSAGE}}",
    "requestId": "{{REQUEST_ID}}"
  }
}
```

## Validation Rules

- {{VALIDATION_RULE_1}}
- {{VALIDATION_RULE_2}}

## Versioning

{{VERSIONING_RULE}}

## Open Questions

- {{OPEN_QUESTION_1}}
