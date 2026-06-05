# Signing: {{PROJECT_NAME}}

## Signing Scope

{{SIGNING_SCOPE}}

## Certificates And Keys

| Asset | Storage | Access |
| --- | --- | --- |
| {{SIGNING_ASSET_1}} | {{STORAGE_1}} | {{ACCESS_1}} |

## Rules

- Do not commit signing keys, certificates, passwords, or PFX/P12 files.
- Keep signing material in managed secret storage or secure signing service.
- Limit signing access to release workflow.
- Log signing events without exposing secret material.

## Verification

- {{SIGNING_VERIFICATION_1}}

## Rotation Or Revocation

{{ROTATION_REVOCATION_RULE}}
