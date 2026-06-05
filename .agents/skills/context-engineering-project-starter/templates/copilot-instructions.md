# GitHub Copilot Repository Instructions: {{PROJECT_NAME}}

Use this repository's project docs as context before proposing or changing code.

Priority docs:

- `AGENTS.md`
- `PROJECT_BRIEF.md`
- `PRODUCT_REQUIREMENTS.md`
- `TECHNICAL_SPEC.md`
- `ARCHITECTURE.md`
- `QUALITY_GATES.md`

Build and validation commands:

```sh
{{SETUP_COMMAND_OR_TBD}}
{{LINT_COMMAND_OR_TBD}}
{{TEST_COMMAND_OR_TBD}}
{{BUILD_COMMAND_OR_TBD}}
```

Rules:

- Keep changes scoped to the current issue or task.
- Do not create duplicate systems or broad rewrites.
- Preserve security, auth, validation, and data boundaries.
- Do not expose secrets or sensitive data.
- Report verification evidence and remaining risks.
