# Install

## Copy Into A Repository

Copy this folder into the target repository:

```text
.agents/skills/ai-project-starter/
```

Codex reads repository skills from `.agents/skills` along the current working directory path up to the repository root.

## Use From This Repository

Ask Codex:

```text
Use the ai-project-starter skill to prepare project context docs for: [project idea]
```

## Optional Scripted Starter

Dry-run an enterprise SaaS security starter:

```sh
python .agents/skills/ai-project-starter/scripts/create_starter.py --output-dir ./example-output --project-name "Acme Security SaaS" --pack enterprise --pack saas --pack cybersecurity --dry-run
```

Create the files:

```sh
python .agents/skills/ai-project-starter/scripts/create_starter.py --output-dir ./example-output --project-name "Acme Security SaaS" --pack enterprise --pack saas --pack cybersecurity
```

The script refuses to overwrite files unless `--force` is passed.
