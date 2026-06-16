# &#129513; Context Engineering Project Starter - README completa em português do Brasil

[🇬🇧](README.md) | [🇩🇪](README.de.md) | [🇪🇸](README.es.md) | [🇧🇷](README.pt-BR.md) | [🇹🇷](README.tr.md) | [🇫🇷](README.fr.md)

> Este arquivo é uma porta de entrada completa em português do Brasil, não um resumo curto. Ele cobre objetivo, limites, uso, validação, segurança e publicação.
>
> README canônico em inglês: [README.md](README.md)

Public starter for packaging context-engineering projects with docs, examples, safety model and install guidance.

Comece pelo README canônico quando precisar da descrição em inglês mais atual. Use esta página para ler o mesmo contrato operacional em português do Brasil.

## Estado e sinais de confiança

|Área | Detalhe|
|--- | ---|
|Status | Public repository: ucsahinn/context-engineering-project-starter|
|Fonte da verdade | [README canônico em inglês](README.md)|
|Usuários | Codex users starting context-heavy projects.; Maintainers packaging reusable agent workflows.|
|Validação | Docs map points to existing files.; AGENTS.md matches the intended project behavior.|
|Segurança | Documents project purpose, supported modes and safety boundaries.; Includes starter docs for install, usage, examples, skill structure and public repo checks.|

## O que este repositório é

- A starter structure for context-engineering projects.
- A public repo template for AGENTS.md, docs, examples, security and release notes.
- A guide for progressive disclosure and reusable project knowledge.
- A reference for turning local context work into a shareable public repo.

## O que ele não é

- Not an official standard.
- Not a full application scaffold.
- Not a place for private datasets, customer files or credentials.
- Not a substitute for validating the generated project in its real target repo.

## Para quem é

- Codex users starting context-heavy projects.
- Maintainers packaging reusable agent workflows.
- Public repo authors who need a safe starter layout.
- Reviewers checking documentation completeness and safety boundaries.

## Início rápido

1. Clone ou atualize o repositório.
2. Leia README, segurança e mapa de documentação.
3. Execute as validações adequadas.
4. Stage somente os arquivos alterados de forma explícita.
5. Antes de push ou release, revise remoto, segredos e links novamente.

## Guia de decisão

- Need reusable context -> put it in docs or references.
- Need repo behavior instructions -> AGENTS.md.
- Need examples -> keep them small, public and validated.
- Need public release -> run checklist and secret scan first.

## Mapa do repositório

|Caminho | Por que importa|
|--- | ---|
|[docs/INSTALL.md](docs/INSTALL.md) | install path|
|[docs/USAGE.md](docs/USAGE.md) | usage model|
|[docs/EXAMPLES.md](docs/EXAMPLES.md) | example workflows|
|[docs/SKILL_STRUCTURE.md](docs/SKILL_STRUCTURE.md) | skill and context layout|
|[docs/PUBLIC_REPO_CHECKLIST.md](docs/PUBLIC_REPO_CHECKLIST.md) | public-readiness checklist|
|[docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md) | safety model|
|[AGENTS.md](AGENTS.md) | working agreement|

## Fluxo de trabalho

1. Clone the starter.
2. Read the supported modes.
3. Customize docs and examples to the target project.
4. Keep detailed reusable context outside the shortest entrypoint.
5. Run diff, link and secret checks before publication.

## Comandos e validação

Execute estes comandos somente depois de clonar o repositório e entender o que eles verificam ou escrevem.

```powershell
git diff --check
gitleaks dir . --no-banner --redact
git status --short --branch
```

## Lista de verificação

- Docs map points to existing files.
- AGENTS.md matches the intended project behavior.
- Examples are public-safe and not copied from private work.
- Security model states what is out of scope.
- Remote HEAD is verified after push.

## Limite de segurança

- Documents project purpose, supported modes and safety boundaries.
- Includes starter docs for install, usage, examples, skill structure and public repo checks.
- Keeps public-ready files visible for cloning and inspection.
- Avoids private operational data and secrets.

Public-safe rule: do not add secrets, tokens, cookies, private keys, private prompts, customer data, local-only auth files, generated logs, archives or build outputs unless the canonical README explicitly says they belong in the public repo.

## Higiene de release e publicação

- Keep starter changes documentation-first unless scripts are intentionally added.
- Do not publish generated private project data.
- Update release notes when the public starter contract changes.
- Verify remote after push.

## Manutenção

- Keep this localized README aligned with README.md when the repo contract changes.
- Prefer factual repo links over marketing claims.
- Do not invent install commands, metrics, users, releases or support promises.
- If a command is version-sensitive, re-check it before documenting it.
- When a localized file cannot be updated fully, leave a clear note instead of a partial translation.

## Caminho de contribuição

- Open a focused change against the smallest set of files.
- Read AGENTS.md or CONTRIBUTING.md when present before editing.
- Run the repo validation commands listed above.
- Review staged diffs explicitly before commit.
- Use security disclosure paths instead of public issues for sensitive reports.

## Definição de concluído

Concluído significa: conteúdo completo, links corretos, limites de segurança claros, validação executada, Git limpo e remote HEAD verificado depois do push.

|Recomendação | Por que importa|
|--- | ---|
|Content | Public starter for packaging context-engineering projects with docs, examples, safety model and install guidance.|
|Links | All referenced local files must exist and resolve from the repository root.|
|Security | AGENTS.md matches the intended project behavior.|
|Verification | Valide estrutura, links, Markdown, segredos, scripts relevantes e remote HEAD antes de afirmar que algo foi publicado.|
|Remote | After push, compare local HEAD with origin/main and GitHub remote HEAD.|

## Links importantes

|Caminho | Por que importa|
|--- | ---|
|[Canonical README](README.md) | README.md|
|[Install docs](docs/INSTALL.md) | docs/INSTALL.md|
|[Usage docs](docs/USAGE.md) | docs/USAGE.md|
|[Examples](docs/EXAMPLES.md) | docs/EXAMPLES.md|
|[Public repo checklist](docs/PUBLIC_REPO_CHECKLIST.md) | docs/PUBLIC_REPO_CHECKLIST.md|
|[Security model](docs/SECURITY_MODEL.md) | docs/SECURITY_MODEL.md|
