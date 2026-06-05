#!/usr/bin/env python3
"""Create a project-context starter document set from bundled templates.

This script is intentionally conservative:
- it never overwrites existing files unless --force is passed
- it creates parent directories as needed
- it replaces only stable project-wide placeholders
- it leaves domain-specific placeholders for Codex to customize
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable


TEMPLATE_TO_PATH = {
    "README.md": "README.md",
    "AGENTS.md": "AGENTS.md",
    "PROJECT_BRIEF.md": "PROJECT_BRIEF.md",
    "PRODUCT_REQUIREMENTS.md": "PRODUCT_REQUIREMENTS.md",
    "TECHNICAL_SPEC.md": "TECHNICAL_SPEC.md",
    "ARCHITECTURE.md": "ARCHITECTURE.md",
    "IMPLEMENTATION_PLAN.md": "IMPLEMENTATION_PLAN.md",
    "TASKS.md": "TASKS.md",
    "ROADMAP.md": "ROADMAP.md",
    "DECISIONS.md": "DECISIONS.md",
    "SECURITY.md": "SECURITY.md",
    "TESTING.md": "TESTING.md",
    "QUALITY_GATES.md": "QUALITY_GATES.md",
    "DATA_MODEL.md": "DATA_MODEL.md",
    "API_CONTRACTS.md": "API_CONTRACTS.md",
    "UI_UX_GUIDELINES.md": "UI_UX_GUIDELINES.md",
    "DESIGN_SYSTEM.md": "DESIGN_SYSTEM.md",
    "DEPLOYMENT.md": "DEPLOYMENT.md",
    "OPERATIONS.md": "OPERATIONS.md",
    "OBSERVABILITY.md": "OBSERVABILITY.md",
    "RISK_REGISTER.md": "RISK_REGISTER.md",
    "CHANGELOG.md": "CHANGELOG.md",
    "CLAUDE.md": "CLAUDE.md",
    "claude-project-rule.md": ".claude/rules/project.md",
    "cursor-project.mdc": ".cursor/rules/project.mdc",
    "cursorrules": ".cursorrules",
    "devin-project-rule.md": ".devin/rules/project.md",
    "windsurfrules": ".windsurfrules",
    "continue-rules.md": ".continue/rules.md",
    "copilot-instructions.md": ".github/copilot-instructions.md",
    "github-project.instructions.md": ".github/instructions/project.instructions.md",
    "aider-conf.yml": ".aider.conf.yml",
    "CONVENTIONS.md": "CONVENTIONS.md",
    "PROJECT_CONTEXT.md": ".codex/PROJECT_CONTEXT.md",
    "WORKING_RULES.md": ".codex/WORKING_RULES.md",
    "adr-0001-architecture-style.md": "docs/adr/0001-architecture-style.md",
    "adr-0002-tech-stack.md": "docs/adr/0002-tech-stack.md",
    "adr-0003-security-boundaries.md": "docs/adr/0003-security-boundaries.md",
    "adr-0004-data-storage.md": "docs/adr/0004-data-storage.md",
    "adr-0005-testing-strategy.md": "docs/adr/0005-testing-strategy.md",
}

CORE = [
    "README.md",
    "AGENTS.md",
    "PROJECT_BRIEF.md",
    "PRODUCT_REQUIREMENTS.md",
    "TECHNICAL_SPEC.md",
    "ARCHITECTURE.md",
    "IMPLEMENTATION_PLAN.md",
    "TASKS.md",
    "DECISIONS.md",
    "SECURITY.md",
    "TESTING.md",
    "QUALITY_GATES.md",
]

ENTERPRISE = [
    "ROADMAP.md",
    "DATA_MODEL.md",
    "API_CONTRACTS.md",
    "UI_UX_GUIDELINES.md",
    "DESIGN_SYSTEM.md",
    "DEPLOYMENT.md",
    "OPERATIONS.md",
    "OBSERVABILITY.md",
    "RISK_REGISTER.md",
    "CHANGELOG.md",
    "adr-0001-architecture-style.md",
    "adr-0002-tech-stack.md",
    "adr-0003-security-boundaries.md",
    "adr-0004-data-storage.md",
    "adr-0005-testing-strategy.md",
]

AGENT_FILES = [
    "CLAUDE.md",
    "claude-project-rule.md",
    "cursor-project.mdc",
    "devin-project-rule.md",
    "continue-rules.md",
    "copilot-instructions.md",
    "github-project.instructions.md",
    "PROJECT_CONTEXT.md",
    "WORKING_RULES.md",
]

LEGACY_AGENT_FILES = [
    "cursorrules",
    "windsurfrules",
    "aider-conf.yml",
    "CONVENTIONS.md",
]

PACKS = {
    "minimal": CORE,
    "enterprise": CORE + ENTERPRISE + AGENT_FILES,
    "agents": ["AGENTS.md"] + AGENT_FILES,
    "agents-legacy": ["AGENTS.md"] + AGENT_FILES + LEGACY_AGENT_FILES,
    "saas": ["TENANCY.md", "AUTH_RBAC.md", "BILLING.md", "AUDIT_LOG.md", "DATA_MODEL.md", "API_CONTRACTS.md"],
    "cybersecurity": ["THREAT_MODEL.md", "ABUSE_CASES.md", "SECURE_DEFAULTS.md", "SECRET_HANDLING.md", "RISK_REGISTER.md"],
    "ai-product": ["PROMPT_POLICY.md", "MODEL_USAGE.md", "EVALS.md", "GUARDRAILS.md", "OBSERVABILITY.md"],
    "api": ["API_CONTRACTS.md", "OPENAPI_PLAN.md", "RATE_LIMITING.md", "DATA_MODEL.md"],
    "web": ["ROUTING.md", "UI_UX_GUIDELINES.md", "DESIGN_SYSTEM.md", "SEO_ACCESSIBILITY_PERFORMANCE.md"],
    "mobile": ["APP_FLOWS.md", "NAVIGATION.md", "OFFLINE_STRATEGY.md", "PERMISSIONS.md", "UI_UX_GUIDELINES.md"],
    "desktop": ["INSTALLER.md", "UPDATER.md", "SIGNING.md", "OS_INTEGRATION.md"],
    "data": ["DATA_MODEL.md", "DATA_GOVERNANCE.md", "OBSERVABILITY.md"],
    "internal-tool": ["AUTH_RBAC.md", "AUDIT_LOG.md", "OPERATIONS.md", "UI_UX_GUIDELINES.md"],
    "library-cli": ["PUBLIC_API.md", "RELEASE.md", "TESTING.md"],
}


def unique(items: Iterable[str]) -> list[str]:
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


def load_templates(mode_names: list[str]) -> list[str]:
    selected: list[str] = []
    for mode in mode_names:
        if mode not in PACKS:
            known = ", ".join(sorted(PACKS))
            raise SystemExit(f"Unknown pack '{mode}'. Known packs: {known}")
        selected.extend(PACKS[mode])
    return unique(selected)


def render_template(text: str, project_name: str) -> str:
    return text.replace("{{PROJECT_NAME}}", project_name)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create context starter docs from templates.")
    parser.add_argument("--skill-dir", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--project-name", required=True)
    parser.add_argument(
        "--pack",
        action="append",
        default=["minimal"],
        help="Starter pack to include. Can be repeated. Examples: enterprise, saas, cybersecurity.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing files.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned writes without writing files.")
    args = parser.parse_args()

    template_dir = args.skill_dir / "templates"
    if not template_dir.is_dir():
        raise SystemExit(f"Template directory not found: {template_dir}")

    selected = load_templates(args.pack)
    planned: list[tuple[Path, Path]] = []
    for template_name in selected:
        source = template_dir / template_name
        if not source.is_file():
            raise SystemExit(f"Template not found: {source}")
        relative_output = TEMPLATE_TO_PATH.get(template_name, template_name)
        planned.append((source, args.output_dir / relative_output))

    for source, target in planned:
        status = "overwrite" if target.exists() else "create"
        print(f"{status}: {target}")

    if args.dry_run:
        return 0

    for source, target in planned:
        if target.exists() and not args.force:
            raise SystemExit(f"Refusing to overwrite existing file without --force: {target}")
        target.parent.mkdir(parents=True, exist_ok=True)
        rendered = render_template(source.read_text(encoding="utf-8"), args.project_name)
        target.write_text(rendered, encoding="utf-8", newline="\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
