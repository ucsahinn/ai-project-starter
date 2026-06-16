# Vibe Coding Reference

Checked: 2026-06-05

## Working Definition

Vibe coding is natural-language-driven software creation where the user directs an AI coding tool, reviews outputs, runs the result, and iterates from behavior and feel. It is useful for exploration and prototypes, but it becomes fragile when product intent, architecture, security, and verification are not written down.

## Why Vibe-Coded Projects Drift

Common failure modes:

- no product brief or first milestone
- no non-goals, so every idea becomes in scope
- no architecture decisions, so the agent invents patterns per prompt
- no data model or API contract, so entities and endpoints duplicate
- no quality gates, so working demos become "done"
- no security boundaries, so auth, secrets, permissions, and logs are weak
- no review loop, so generated code accumulates without ownership
- no task list, so old unfinished work is forgotten

## Professional Vibe Coding Workflow

1. Convert idea into product outcome.
2. Identify users, workflows, and acceptance criteria.
3. Define first milestone and non-goals.
4. Decide tech stack and architecture constraints.
5. Write agent instructions and quality gates before coding.
6. Implement in small phases.
7. Verify with tests, browser/runtime checks, and security review where needed.
8. Update decisions and tasks after each phase.

## Strong Definition Of Done

A vibe-coded feature is not done when it looks plausible. It is done when:

- the requirement maps to a documented user flow or task
- acceptance criteria are met
- tests or runtime/browser checks have been run
- security-sensitive behavior is reviewed
- no duplicate implementation or undocumented architecture drift was introduced
- remaining gaps are written down instead of hidden

## Guardrails To Put In Generated Docs

Use these rules in `AGENTS.md`, `QUALITY_GATES.md`, and implementation plans:

- Do not add features outside the current milestone.
- Do not create duplicate modules, parallel data models, or alternate design systems.
- Do not perform broad refactors unless explicitly requested and planned.
- Do not implement auth, billing, cryptography, tenant isolation, or production data handling without explicit security requirements and tests.
- Do not claim completion from UI appearance alone.
- Do not deploy, publish, push, or mutate production without explicit approval.
- Always run the smallest meaningful verification before reporting done.

## Risk-Based Escalation

Low risk:

- static site, prototype UI, local toy app
- can use lean docs and basic guardrails

Medium risk:

- user accounts, API, database, payments planned later
- include architecture, data model, testing, and security baseline

High risk:

- auth, tenant data, secrets, payments, cybersecurity, AI agents, regulated data, desktop installer/updater
- use `ENTERPRISE_STARTER`, threat model, ADRs, quality gates, operations, observability, and explicit approval gates

## Research Sources

- OpenAI, How OpenAI uses Codex: https://openai.com/business/guides-and-resources/how-openai-uses-codex/
- Palo Alto Networks, What is vibe coding: https://www.paloaltonetworks.com/cyberpedia/what-is-vibe-coding
- TechTarget, Vibe coding security risks: https://www.techtarget.com/searchsecurity/tip/Vibe-coding-security-risks-and-how-to-mitigate-them
- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications
- OWASP Agentic AI threats and mitigations: https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/
- OWASP MCP Top 10: https://owasp.org/www-project-mcp-top-10/
- arXiv, Vibe Coding in Practice: https://arxiv.org/abs/2512.11922
- arXiv, From Prompting to Verification: https://arxiv.org/abs/2605.24521
