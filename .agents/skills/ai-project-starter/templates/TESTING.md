# Testing Strategy: {{PROJECT_NAME}}

## Testing Goals

- Prove core user workflows work.
- Catch regressions in security, data, and API behavior.
- Keep AI-generated changes reviewable and verifiable.

## Test Layers

| Layer | Scope | Tooling | Required |
| --- | --- | --- | --- |
| Unit | {{UNIT_SCOPE}} | {{UNIT_TOOL}} | {{YES_NO}} |
| Integration | {{INTEGRATION_SCOPE}} | {{INTEGRATION_TOOL}} | {{YES_NO}} |
| E2E | {{E2E_SCOPE}} | {{E2E_TOOL}} | {{YES_NO}} |
| Security | {{SECURITY_SCOPE}} | {{SECURITY_TOOL}} | {{YES_NO}} |

## Required Checks

```sh
{{LINT_COMMAND_OR_TBD}}
{{TEST_COMMAND_OR_TBD}}
{{TYPECHECK_COMMAND_OR_TBD}}
{{BUILD_COMMAND_OR_TBD}}
```

## Acceptance Test Scenarios

1. {{SCENARIO_1}}
2. {{SCENARIO_2}}
3. {{SCENARIO_3}}

## Browser Or Runtime QA

- Desktop behavior: {{DESKTOP_QA}}
- Mobile behavior: {{MOBILE_QA}}
- Keyboard/focus: {{FOCUS_QA}}
- Empty/loading/error states: {{STATE_QA}}

## Test Data

{{TEST_DATA_RULES}}

## Known Gaps

- {{TEST_GAP_1}}
