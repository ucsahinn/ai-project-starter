# Secret Handling: {{PROJECT_NAME}}

## Secret Types

| Secret | Storage | Rotation | Access |
| --- | --- | --- | --- |
| {{SECRET_TYPE_1}} | {{STORAGE_1}} | {{ROTATION_1}} | {{ACCESS_1}} |

## Rules

- Do not commit secrets, tokens, private keys, certificates, API keys, cookies, or local env files.
- Do not print, log, screenshot, or report secret values.
- Redact secret-like values in diagnostics and final reports.
- Use managed secret storage for deployed environments.
- Treat leaked secret-like values as compromised until rotated.

## Local Development

{{LOCAL_SECRET_RULES}}

## CI/CD

{{CI_SECRET_RULES}}

## Rotation

{{ROTATION_PROCESS}}

## Verification

- {{SECRET_SCAN_COMMAND_OR_TBD}}
