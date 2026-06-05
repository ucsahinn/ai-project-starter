# Quality Gates: {{PROJECT_NAME}}

## Definition Of Done

A change is not done until:

- it satisfies the current requirement and acceptance criteria
- it stays within scope and non-goals
- it preserves documented security and architecture boundaries
- required checks pass or are explicitly blocked with reason
- user-facing behavior is verified in the relevant runtime or browser when applicable
- docs are updated for changed commands, decisions, or behavior

## Required Gates

| Gate | Required Evidence |
| --- | --- |
| Scope | Change maps to a documented task or requirement |
| Security | No secrets exposed; auth/data boundaries preserved |
| Tests | {{TEST_EVIDENCE}} |
| Build | {{BUILD_EVIDENCE}} |
| UX | {{UX_EVIDENCE}} |
| Docs | Changed behavior or decisions documented |

## Anti-Slop Rules

- No placeholder features marked complete.
- No duplicate implementations of the same concept.
- No broad refactors without approval.
- No speculative abstractions.
- No unverified success claims.
- No hidden dependency additions.

## Stop Conditions

Stop and ask before:

- changing product scope
- changing security boundaries
- changing data model or migrations
- adding paid services or external accounts
- deploying, publishing, committing, pushing, or releasing

## Review Checklist

- [ ] Requirements satisfied
- [ ] Non-goals respected
- [ ] Tests/checks run
- [ ] Security reviewed
- [ ] Docs updated
- [ ] Risks reported
