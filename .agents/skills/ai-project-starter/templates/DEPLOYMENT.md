# Deployment: {{PROJECT_NAME}}

## Deployment Target

{{DEPLOYMENT_TARGET}}

## Environments

| Environment | Purpose | Data | Access |
| --- | --- | --- | --- |
| Local | Development | Synthetic/local | Developers |
| Staging | Pre-production validation | {{STAGING_DATA_RULE}} | {{STAGING_ACCESS}} |
| Production | Live service | {{PRODUCTION_DATA_RULE}} | {{PRODUCTION_ACCESS}} |

## Build

```sh
{{BUILD_COMMAND_OR_TBD}}
```

## Configuration

- {{CONFIG_ITEM_1}}
- {{CONFIG_ITEM_2}}

## Secrets

- Store secrets in {{SECRET_STORE_OR_TBD}}.
- Do not commit `.env`, keys, tokens, certificates, or generated secret files.
- Rotate secrets through an approved process only.

## Release Process

1. {{RELEASE_STEP_1}}
2. {{RELEASE_STEP_2}}
3. {{RELEASE_STEP_3}}

## Rollback

{{ROLLBACK_PLAN}}

## Deployment Approval Gates

Ask before production deployment, DNS changes, database migrations, paid service changes, credential rotation, or release publication.
