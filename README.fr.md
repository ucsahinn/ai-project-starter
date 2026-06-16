# &#129513; AI Project Starter - README français complet

[🇬🇧](README.md) | [🇩🇪](README.de.md) | [🇪🇸](README.es.md) | [🇧🇷](README.pt-BR.md) | [🇹🇷](README.tr.md) | [🇫🇷](README.fr.md)

> Ce fichier est une page d’entrée française complète, pas un court résumé. Il couvre objectif, limites, usage, validation, sécurité et publication.
>
> README canonique en anglais: [README.md](README.md)

Public starter for packaging context-engineering projects with docs, examples, safety model and install guidance.

Commencez par le README canonique si vous voulez la description anglaise la plus actuelle. Utilisez cette page pour lire le même contrat opérationnel en français.

## Statut et signaux de confiance

|Zone | Détail|
|--- | ---|
|Statut | Public repository: ucsahinn/ai-project-starter|
|Source de vérité | [README canonique en anglais](README.md)|
|Utilisateurs | Codex users starting context-heavy projects.; Maintainers packaging reusable agent workflows.|
|Validation | Docs map points to existing files.; AGENTS.md matches the intended project behavior.|
|Sécurité | Documents project purpose, supported modes and safety boundaries.; Includes starter docs for install, usage, examples, skill structure and public repo checks.|

## Ce que contient ce dépôt

- A starter structure for context-engineering projects.
- A public repo template for AGENTS.md, docs, examples, security and release notes.
- A guide for progressive disclosure and reusable project knowledge.
- A reference for turning local context work into a shareable public repo.

## Ce que ce dépôt n’est pas

- Not an official standard.
- Not a full application scaffold.
- Not a place for private datasets, customer files or credentials.
- Not a substitute for validating the generated project in its real target repo.

## Public visé

- Codex users starting context-heavy projects.
- Maintainers packaging reusable agent workflows.
- Public repo authors who need a safe starter layout.
- Reviewers checking documentation completeness and safety boundaries.

## Démarrage rapide

1. Clonez ou mettez à jour le dépôt.
2. Lisez README, sécurité et carte documentaire.
3. Lancez les validations adaptées.
4. Stagez uniquement les fichiers explicitement modifiés.
5. Avant push ou release, revérifiez remote, secrets et liens.

## Guide de décision

- Need reusable context -> put it in docs or references.
- Need repo behavior instructions -> AGENTS.md.
- Need examples -> keep them small, public and validated.
- Need public release -> run checklist and secret scan first.

## Carte du dépôt

|Chemin | Pourquoi c’est important|
|--- | ---|
|[docs/INSTALL.md](docs/INSTALL.md) | install path|
|[docs/USAGE.md](docs/USAGE.md) | usage model|
|[docs/EXAMPLES.md](docs/EXAMPLES.md) | example workflows|
|[docs/SKILL_STRUCTURE.md](docs/SKILL_STRUCTURE.md) | skill and context layout|
|[docs/PUBLIC_REPO_CHECKLIST.md](docs/PUBLIC_REPO_CHECKLIST.md) | public-readiness checklist|
|[docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md) | safety model|
|[AGENTS.md](AGENTS.md) | working agreement|

## Flux de travail

1. Clone the starter.
2. Read the supported modes.
3. Customize docs and examples to the target project.
4. Keep detailed reusable context outside the shortest entrypoint.
5. Run diff, link and secret checks before publication.

## Commandes et validation

Exécutez ces commandes seulement après avoir cloné le dépôt et compris ce qu’elles vérifient ou modifient.

```powershell
git diff --check
gitleaks dir . --no-banner --redact
git status --short --branch
```

## Liste de vérification

- Docs map points to existing files.
- AGENTS.md matches the intended project behavior.
- Examples are public-safe and not copied from private work.
- Security model states what is out of scope.
- Remote HEAD is verified after push.

## Limite de sécurité

- Documents project purpose, supported modes and safety boundaries.
- Includes starter docs for install, usage, examples, skill structure and public repo checks.
- Keeps public-ready files visible for cloning and inspection.
- Avoids private operational data and secrets.

Public-safe rule: do not add secrets, tokens, cookies, private keys, private prompts, customer data, local-only auth files, generated logs, archives or build outputs unless the canonical README explicitly says they belong in the public repo.

## Hygiène de release et publication

- Keep starter changes documentation-first unless scripts are intentionally added.
- Do not publish generated private project data.
- Update release notes when the public starter contract changes.
- Verify remote after push.

## Maintenance

- Keep this localized README aligned with README.md when the repo contract changes.
- Prefer factual repo links over marketing claims.
- Do not invent install commands, metrics, users, releases or support promises.
- If a command is version-sensitive, re-check it before documenting it.
- When a localized file cannot be updated fully, leave a clear note instead of a partial translation.

## Chemin de contribution

- Open a focused change against the smallest set of files.
- Read AGENTS.md or CONTRIBUTING.md when present before editing.
- Run the repo validation commands listed above.
- Review staged diffs explicitly before commit.
- Use security disclosure paths instead of public issues for sensitive reports.

## Définition de terminé

Terminé signifie: contenu complet, liens corrects, limites de sécurité claires, validation exécutée, Git propre et remote HEAD vérifié après le push.

|Recommandation | Pourquoi c’est important|
|--- | ---|
|Content | Public starter for packaging context-engineering projects with docs, examples, safety model and install guidance.|
|Links | All referenced local files must exist and resolve from the repository root.|
|Security | AGENTS.md matches the intended project behavior.|
|Verification | Validez structure, liens, Markdown, secrets, scripts pertinents et remote HEAD avant toute annonce publique.|
|Remote | After push, compare local HEAD with origin/main and GitHub remote HEAD.|

## Liens importants

|Chemin | Pourquoi c’est important|
|--- | ---|
|[Canonical README](README.md) | README.md|
|[Install docs](docs/INSTALL.md) | docs/INSTALL.md|
|[Usage docs](docs/USAGE.md) | docs/USAGE.md|
|[Examples](docs/EXAMPLES.md) | docs/EXAMPLES.md|
|[Public repo checklist](docs/PUBLIC_REPO_CHECKLIST.md) | docs/PUBLIC_REPO_CHECKLIST.md|
|[Security model](docs/SECURITY_MODEL.md) | docs/SECURITY_MODEL.md|
