# Source Map

Checked: 2026-06-16

Codex-specific behavior was refreshed from the official Codex manual on 2026-06-16 for skills, AGENTS.md discovery, MCP, plugins, subagents, and permissions.

Use this map when updating the skill or when generating context docs that depend on current tool behavior. Prefer primary/official sources. Treat articles, news, papers, and community discussions as secondary signals unless they document a risk pattern that official docs do not yet cover.

## Agent Instruction Files

| Area | Source | Use |
| --- | --- | --- |
| Codex `AGENTS.md` | https://developers.openai.com/codex/guides/agents-md | Codex instruction discovery, precedence, byte limits, nested overrides, verification. |
| Codex Skills | https://developers.openai.com/codex/skills | Skill anatomy, repo-scoped `.agents/skills`, progressive disclosure. |
| AGENTS.md format | https://agents.md/ | Cross-agent shared instruction file conventions. |
| Claude Code memory | https://code.claude.com/docs/en/memory | `CLAUDE.md`, `.claude/rules`, imports, line guidance, precedence, non-enforcement caveats. |
| Cursor rules | https://cursor.com/docs/rules | `.cursor/rules`, `AGENTS.md`, and legacy `.cursorrules`. |
| Devin/Windsurf Cascade rules | https://docs.devin.ai/desktop/cascade/memories | `.devin/rules`, `.windsurf/rules`, `.windsurfrules`, rule activation modes and limits. |
| Continue rules | https://docs.continue.dev/customize/rules | `.continue/rules` and project-specific local rules. |
| Aider conventions | https://aider.chat/docs/usage/conventions.html | `CONVENTIONS.md`, `/read`, `--read`, `.aider.conf.yml` read-only conventions. |
| GitHub Copilot instructions | https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions | `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`, `AGENTS.md`. |

## Context, Planning, And Docs

| Area | Source | Use |
| --- | --- | --- |
| Context engineering | https://developers.openai.com/cookbook/examples/agents_sdk/context_personalization | Context as state, memory, injection, and inspectable persistent notes. |
| PRD | https://www.atlassian.com/agile/requirements | Product requirements, purpose, features, user needs, success criteria. |
| Architecture template | https://arc42.org/overview | Architecture goals, constraints, views, risks, quality requirements, glossary. |
| ADR templates | https://adr.github.io/adr-templates/ | ADR status, context, decision, alternatives, consequences. |
| ADR generator/reference | https://www.adr.zone/ | Multiple ADR formats and decision-record guidance. |

## Security And AI-Agent Safety

| Area | Source | Use |
| --- | --- | --- |
| OpenAI prompt injection | https://openai.com/index/prompt-injections/ | Untrusted content, explicit instructions, least privilege, confirmations. |
| Running Codex safely | https://openai.com/index/running-codex-safely/ | Sandboxing, approvals, network policy, credentials, audit trails. |
| OpenAI safety best practices | https://developers.openai.com/api/docs/guides/safety-best-practices | HITL, constrained input/output, safety identifiers, limitation disclosure. |
| Agent builder safety | https://developers.openai.com/api/docs/guides/agent-builder-safety | Prompt injection and tool-use safety for agents. |
| OWASP LLM Top 10 | https://owasp.org/www-project-top-10-for-large-language-model-applications | LLM app risk categories. |
| OWASP Agentic AI | https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/ | Agentic threat modeling. |
| OWASP MCP Top 10 | https://owasp.org/www-project-mcp-top-10/ | MCP-specific risks and mitigations. |

## Vibe Coding And AI-Assisted Development

| Area | Source | Use |
| --- | --- | --- |
| OpenAI Codex usage | https://openai.com/business/guides-and-resources/how-openai-uses-codex/ | Real-world Codex usage and documentation practices. |
| Vibe coding overview | https://www.paloaltonetworks.com/cyberpedia/what-is-vibe-coding | Definition, benefits, and risks. |
| Vibe coding risks | https://www.techtarget.com/searchsecurity/tip/Vibe-coding-security-risks-and-how-to-mitigate-them | Security and maintainability risks. |

## Confidence Rules

- Official docs: high confidence for tool behavior at date checked.
- Security standards and vendor guidance: high-to-medium confidence; still adapt to project context.
- Practitioner articles: medium confidence; use for patterns, not definitive support claims.
- Academic papers: useful for risk evidence, but do not turn preliminary research into operational requirements without review.
- Community posts: leads only; verify before encoding as skill behavior.
