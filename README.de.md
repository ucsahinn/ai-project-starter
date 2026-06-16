# &#129513; AI Project Starter - vollständige deutsche README

[🇬🇧](README.md) | [🇩🇪](README.de.md) | [🇪🇸](README.es.md) | [🇧🇷](README.pt-BR.md) | [🇹🇷](README.tr.md) | [🇫🇷](README.fr.md)

> Diese Datei ist eine vollständige deutsche Einstiegseite, kein kurzer Platzhalter. Sie fasst Zweck, Grenzen, Bedienung, Prüfung, Sicherheit und Veröffentlichung in einer Datei zusammen.
>
> Kanonische englische README: [README.md](README.md)

Public starter for packaging context-engineering projects with docs, examples, safety model and install guidance.

Beginnen Sie mit der kanonischen README, wenn Sie die aktuellste englische Beschreibung brauchen. Verwenden Sie diese Seite, wenn Sie den gleichen Vertrag auf Deutsch lesen wollen.

## Status und Vertrauensrahmen

|Bereich | Details|
|--- | ---|
|Status | Public repository: ucsahinn/ai-project-starter|
|Wahrheit | [Kanonische englische README](README.md)|
|Benutzer | Codex users starting context-heavy projects.; Maintainers packaging reusable agent workflows.|
|Prüfung | Docs map points to existing files.; AGENTS.md matches the intended project behavior.|
|Sicherheit | Documents project purpose, supported modes and safety boundaries.; Includes starter docs for install, usage, examples, skill structure and public repo checks.|

## Was dieses Repository ist

- A starter structure for context-engineering projects.
- A public repo template for AGENTS.md, docs, examples, security and release notes.
- A guide for progressive disclosure and reusable project knowledge.
- A reference for turning local context work into a shareable public repo.

## Was es nicht ist

- Not an official standard.
- Not a full application scaffold.
- Not a place for private datasets, customer files or credentials.
- Not a substitute for validating the generated project in its real target repo.

## Für wen es gedacht ist

- Codex users starting context-heavy projects.
- Maintainers packaging reusable agent workflows.
- Public repo authors who need a safe starter layout.
- Reviewers checking documentation completeness and safety boundaries.

## Schnellstart

1. Repository klonen oder aktualisieren.
2. README, Sicherheitsdateien und Dokumentationskarte lesen.
3. Die passenden Prüfungen ausführen.
4. Nur explizit geänderte Dateien stagen.
5. Vor Push oder Release Remote-Status, Secrets und Links erneut prüfen.

## Entscheidungshilfe

- Need reusable context -> put it in docs or references.
- Need repo behavior instructions -> AGENTS.md.
- Need examples -> keep them small, public and validated.
- Need public release -> run checklist and secret scan first.

## Repository-Karte

|Pfad | Warum es wichtig ist|
|--- | ---|
|[docs/INSTALL.md](docs/INSTALL.md) | install path|
|[docs/USAGE.md](docs/USAGE.md) | usage model|
|[docs/EXAMPLES.md](docs/EXAMPLES.md) | example workflows|
|[docs/SKILL_STRUCTURE.md](docs/SKILL_STRUCTURE.md) | skill and context layout|
|[docs/PUBLIC_REPO_CHECKLIST.md](docs/PUBLIC_REPO_CHECKLIST.md) | public-readiness checklist|
|[docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md) | safety model|
|[AGENTS.md](AGENTS.md) | working agreement|

## Arbeitsablauf

1. Clone the starter.
2. Read the supported modes.
3. Customize docs and examples to the target project.
4. Keep detailed reusable context outside the shortest entrypoint.
5. Run diff, link and secret checks before publication.

## Befehle und Prüfung

Führen Sie diese Befehle nur aus, wenn Sie das Repository lokal geclont haben und die Wirkung verstehen.

```powershell
git diff --check
gitleaks dir . --no-banner --redact
git status --short --branch
```

## Validierungs-Checkliste

- Docs map points to existing files.
- AGENTS.md matches the intended project behavior.
- Examples are public-safe and not copied from private work.
- Security model states what is out of scope.
- Remote HEAD is verified after push.

## Sicherheitsgrenze

- Documents project purpose, supported modes and safety boundaries.
- Includes starter docs for install, usage, examples, skill structure and public repo checks.
- Keeps public-ready files visible for cloning and inspection.
- Avoids private operational data and secrets.

Public-safe rule: do not add secrets, tokens, cookies, private keys, private prompts, customer data, local-only auth files, generated logs, archives or build outputs unless the canonical README explicitly says they belong in the public repo.

## Release- und Publikationshygiene

- Keep starter changes documentation-first unless scripts are intentionally added.
- Do not publish generated private project data.
- Update release notes when the public starter contract changes.
- Verify remote after push.

## Wartung

- Keep this localized README aligned with README.md when the repo contract changes.
- Prefer factual repo links over marketing claims.
- Do not invent install commands, metrics, users, releases or support promises.
- If a command is version-sensitive, re-check it before documenting it.
- When a localized file cannot be updated fully, leave a clear note instead of a partial translation.

## Beitragspfad

- Open a focused change against the smallest set of files.
- Read AGENTS.md or CONTRIBUTING.md when present before editing.
- Run the repo validation commands listed above.
- Review staged diffs explicitly before commit.
- Use security disclosure paths instead of public issues for sensitive reports.

## Definition von fertig

Fertig bedeutet: Inhalt ist lokal vollständig, Links funktionieren, Sicherheitsgrenzen sind klar, Validierung ist gelaufen, Git ist sauber und der Remote-Stand ist nach dem Push geprüft.

|Empfehlung | Warum es wichtig ist|
|--- | ---|
|Content | Public starter for packaging context-engineering projects with docs, examples, safety model and install guidance.|
|Links | All referenced local files must exist and resolve from the repository root.|
|Security | AGENTS.md matches the intended project behavior.|
|Verification | Prüfen Sie Struktur, Links, Markdown, Secrets, relevante Skripte und Remote-HEAD, bevor Sie eine öffentliche Aussage machen.|
|Remote | After push, compare local HEAD with origin/main and GitHub remote HEAD.|

## Wichtige Links

|Pfad | Warum es wichtig ist|
|--- | ---|
|[Canonical README](README.md) | README.md|
|[Install docs](docs/INSTALL.md) | docs/INSTALL.md|
|[Usage docs](docs/USAGE.md) | docs/USAGE.md|
|[Examples](docs/EXAMPLES.md) | docs/EXAMPLES.md|
|[Public repo checklist](docs/PUBLIC_REPO_CHECKLIST.md) | docs/PUBLIC_REPO_CHECKLIST.md|
|[Security model](docs/SECURITY_MODEL.md) | docs/SECURITY_MODEL.md|
