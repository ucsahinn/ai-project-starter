# Quality Rubric

Score each category 1-5. Enterprise starter output must average at least 4.0 and score at least 4 in scope control, security, verifiability, and agent compatibility.

## Categories

### Project Specificity

- 1: Generic text could fit any project.
- 3: Some project details but many placeholders.
- 5: Uses the user's idea, users, workflows, risk profile, and constraints throughout.

### Scope Control

- 1: No non-goals or milestone boundary.
- 3: Some scope limits but not enforceable.
- 5: Clear in-scope, out-of-scope, first milestone, approval gates, and stop conditions.

### Context Quality

- 1: No source order or assumption handling.
- 3: Context is useful but not prioritized.
- 5: Source-of-truth order, assumptions, conflicts, and provenance are explicit.

### Architecture Readiness

- 1: No architectural shape.
- 3: Stack or modules named but weak boundaries.
- 5: Components, boundaries, data/API/UI/deployment implications, and ADR needs are clear.

### Security

- 1: Security missing or generic.
- 3: Mentions security but lacks boundaries.
- 5: Secrets, auth, authorization, validation, tenant/data boundaries, logging, abuse cases, and approval gates are included where relevant.

### Testing And Quality

- 1: No tests or done criteria.
- 3: Basic tests listed.
- 5: Quality gates tie requirements to checks, acceptance criteria, static analysis, runtime/browser checks, and review evidence.

### Agent Compatibility

- 1: Agent instructions vague or tool-agnostic in the wrong way.
- 3: Has AGENTS.md but weak tool-specific adapters.
- 5: Durable concise instructions, tool-specific file choices, source order, command rules, and stop conditions are clear.

### Domain Coverage

- 1: Ignores project-specific domain needs such as SaaS tenancy, AI evals, mobile offline behavior, installer updates, or API contracts.
- 3: Adds some domain docs but misses key risk files.
- 5: Selects the right domain starter pack and includes only the files needed for the project type and risk level.

### Maintainability

- 1: Encourages one-off generation and duplication.
- 3: Some maintainability notes.
- 5: Decisions, tasks, changelog, ADRs, and update rules prevent context rot.

### Anti-Slop Protection

- 1: Allows broad generation without review.
- 3: Mentions scope creep but lacks controls.
- 5: Blocks duplicate systems, speculative abstractions, placeholder completion, unverified claims, and broad refactors.

### Output Precision

- 1: Unclear file names or format.
- 3: File set is clear but sections are inconsistent.
- 5: Exact paths, focused contents, assumptions, verification, and open questions are easy to validate.

### Source Currency

- 1: Tool-specific or security claims are stale or unsourced.
- 3: Some current sources are listed but claims are not tied to authority.
- 5: Version-sensitive claims use official sources with checked dates and lower-authority sources are labeled as such.

## Red Flags

Rewrite before finalizing if any are true:

- no non-goals in a broad project
- no security baseline for a real app
- no test strategy
- no source-of-truth order
- every file has the same boilerplate sections
- agent files duplicate long docs instead of referencing them
- stack choices are claimed as user-approved when they are assumptions
- compliance or security guarantees are asserted without evidence
- implementation is authorized when the user only asked for context docs
- generated docs do not name acceptance criteria or verification
- tool-specific instruction files use deprecated paths without labeling them legacy
- optional domain docs are omitted for a clearly high-risk project
