# &#129513; AI Project Starter - README completa en español

[&#127468;&#127463; English](README.md) | [&#127465;&#127466; Deutsch](README.de.md) | [&#127466;&#127480; Español](README.es.md) | [&#127463;&#127479; Português (Brasil)](README.pt-BR.md) | [&#127481;&#127479; Türkçe](README.tr.md) | [&#127467;&#127479; Français](README.fr.md)

> Este archivo es una portada completa en español, no un resumen corto. Cubre propósito, límites, uso, validación, seguridad y publicación.
>
> README canónico en inglés: [README.md](README.md)

Public starter for packaging context-engineering projects with docs, examples, safety model and install guidance.

Empieza por el README canónico si necesitas la descripción inglesa más actual. Usa esta página cuando quieras el mismo contrato operativo en español.

## Estado y señales de confianza

|Área | Detalle|
|--- | ---|
|Estado | Public repository: ucsahinn/ai-project-starter|
|Fuente de verdad | [README canónico en inglés](README.md)|
|Usuarios | Codex users starting context-heavy projects.; Maintainers packaging reusable agent workflows.|
|Validación | Docs map points to existing files.; AGENTS.md matches the intended project behavior.|
|Seguridad | Documents project purpose, supported modes and safety boundaries.; Includes starter docs for install, usage, examples, skill structure and public repo checks.|

## Qué es este repositorio

- A starter structure for context-engineering projects.
- A public repo template for AGENTS.md, docs, examples, security and release notes.
- A guide for progressive disclosure and reusable project knowledge.
- A reference for turning local context work into a shareable public repo.

## Qué no es

- Not an official standard.
- Not a full application scaffold.
- Not a place for private datasets, customer files or credentials.
- Not a substitute for validating the generated project in its real target repo.

## Para quién es

- Codex users starting context-heavy projects.
- Maintainers packaging reusable agent workflows.
- Public repo authors who need a safe starter layout.
- Reviewers checking documentation completeness and safety boundaries.

## Inicio rápido

1. Clona o actualiza el repositorio.
2. Lee README, seguridad y el mapa de documentación.
3. Ejecuta las validaciones adecuadas.
4. Prepara solo los archivos cambiados de forma explícita.
5. Antes de push o release, revisa remoto, secretos y enlaces otra vez.

## Guía de decisión

- Need reusable context -> put it in docs or references.
- Need repo behavior instructions -> AGENTS.md.
- Need examples -> keep them small, public and validated.
- Need public release -> run checklist and secret scan first.

## Mapa del repositorio

|Ruta | Por qué importa|
|--- | ---|
|[docs/INSTALL.md](docs/INSTALL.md) | install path|
|[docs/USAGE.md](docs/USAGE.md) | usage model|
|[docs/EXAMPLES.md](docs/EXAMPLES.md) | example workflows|
|[docs/SKILL_STRUCTURE.md](docs/SKILL_STRUCTURE.md) | skill and context layout|
|[docs/PUBLIC_REPO_CHECKLIST.md](docs/PUBLIC_REPO_CHECKLIST.md) | public-readiness checklist|
|[docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md) | safety model|
|[AGENTS.md](AGENTS.md) | working agreement|

## Flujo de trabajo

1. Clone the starter.
2. Read the supported modes.
3. Customize docs and examples to the target project.
4. Keep detailed reusable context outside the shortest entrypoint.
5. Run diff, link and secret checks before publication.

## Comandos y validación

Ejecuta estos comandos solo después de clonar el repositorio y entender qué escriben o verifican.

```powershell
git diff --check
gitleaks dir . --no-banner --redact
git status --short --branch
```

## Lista de verificación

- Docs map points to existing files.
- AGENTS.md matches the intended project behavior.
- Examples are public-safe and not copied from private work.
- Security model states what is out of scope.
- Remote HEAD is verified after push.

## Límite de seguridad

- Documents project purpose, supported modes and safety boundaries.
- Includes starter docs for install, usage, examples, skill structure and public repo checks.
- Keeps public-ready files visible for cloning and inspection.
- Avoids private operational data and secrets.

Public-safe rule: do not add secrets, tokens, cookies, private keys, private prompts, customer data, local-only auth files, generated logs, archives or build outputs unless the canonical README explicitly says they belong in the public repo.

## Higiene de release y publicación

- Keep starter changes documentation-first unless scripts are intentionally added.
- Do not publish generated private project data.
- Update release notes when the public starter contract changes.
- Verify remote after push.

## Mantenimiento

- Keep this localized README aligned with README.md when the repo contract changes.
- Prefer factual repo links over marketing claims.
- Do not invent install commands, metrics, users, releases or support promises.
- If a command is version-sensitive, re-check it before documenting it.
- When a localized file cannot be updated fully, leave a clear note instead of a partial translation.

## Ruta de contribución

- Open a focused change against the smallest set of files.
- Read AGENTS.md or CONTRIBUTING.md when present before editing.
- Run the repo validation commands listed above.
- Review staged diffs explicitly before commit.
- Use security disclosure paths instead of public issues for sensitive reports.

## Definición de terminado

Terminado significa: contenido completo, enlaces correctos, límites de seguridad claros, validación ejecutada, Git limpio y remote HEAD verificado después del push.

|Recomendación | Por qué importa|
|--- | ---|
|Content | Public starter for packaging context-engineering projects with docs, examples, safety model and install guidance.|
|Links | All referenced local files must exist and resolve from the repository root.|
|Security | AGENTS.md matches the intended project behavior.|
|Verification | Valida estructura, enlaces, Markdown, secretos, scripts relevantes y remote HEAD antes de afirmar que algo está publicado.|
|Remote | After push, compare local HEAD with origin/main and GitHub remote HEAD.|

## Enlaces importantes

|Ruta | Por qué importa|
|--- | ---|
|[Canonical README](README.md) | README.md|
|[Install docs](docs/INSTALL.md) | docs/INSTALL.md|
|[Usage docs](docs/USAGE.md) | docs/USAGE.md|
|[Examples](docs/EXAMPLES.md) | docs/EXAMPLES.md|
|[Public repo checklist](docs/PUBLIC_REPO_CHECKLIST.md) | docs/PUBLIC_REPO_CHECKLIST.md|
|[Security model](docs/SECURITY_MODEL.md) | docs/SECURITY_MODEL.md|
