# AI Project Starter - README française

<p align="center">
  &#127760; <strong>Documentation:</strong>
  <a href="README.de.md"><img src="https://flagcdn.com/w20/de.png" alt="Deutsch" width="20"></a> |
  <a href="README.es.md"><img src="https://flagcdn.com/w20/es.png" alt="Espa&#241;ol" width="20"></a> |
  <a href="README.md"><img src="https://flagcdn.com/w20/gb.png" alt="English" width="20"></a> |
  <a href="README.pt-BR.md"><img src="https://flagcdn.com/w20/br.png" alt="Portugu&#234;s (Brasil)" width="20"></a> |
  <a href="README.tr.md"><img src="https://flagcdn.com/w20/tr.png" alt="T&#252;rk&#231;e" width="20"></a> |
  <a href="README.fr.md"><img src="https://flagcdn.com/w20/fr.png" alt="Fran&#231;ais" width="20"></a>
</p>

> Cette page est l'entrée française pour AI Project Starter. La description canonique en anglais reste [README.md](README.md).

AI Project Starter est un skill Codex public pour le context engineering: il aide à préparer le contexte de projet, la documentation de démarrage, les règles d'agents et les guardrails anti-drift avant qu'un agent de code commence l'implémentation.

## Statut et cadre de confiance

| Zone | Détail |
| --- | --- |
| Statut | Référentiel public: `ucsahinn/ai-project-starter` |
| Source de vérité | [README canonique](README.md) et [point d'entrée du skill](.agents/skills/ai-project-starter/SKILL.md) |
| Utilisateurs | Utilisateurs Codex qui démarrent des projets riches en contexte; mainteneurs de workflows d'agents réutilisables |
| Validation | `npm run check`, smoke test du starter, `git diff --check`, checklist publique et secret scan avant publication |
| Sécurité | Les exemples sont fictifs, publics et sans secrets, prompts privés, données client ni chemins locaux d'opérateur |

## Ce que contient ce dépôt

- Un paquet de documentation et de skill pour démarrer des projets prêts pour l'AI coding.
- Une structure réutilisable pour PRD, spécification technique, architecture, sécurité, tests, quality gates et instructions d'agents.
- Un starter public pour Codex, Cursor, Claude Code, Windsurf/Devin, Continue, Copilot, Aider et outils similaires.
- Une méthode pour traiter le context engineering comme un artefact vérifiable et versionné.

## Ce que ce dépôt n'est pas

- Ce n'est pas un standard officiel.
- Ce n'est pas un scaffold complet d'application.
- Ce n'est pas un emplacement pour données privées, identifiants, fichiers client, logs ou captures.
- Ce n'est pas un substitut à la validation du projet généré dans son vrai référentiel cible.

## Démarrage rapide

1. Clonez ou mettez à jour le dépôt.
2. Lisez [README.md](README.md), [AGENTS.md](AGENTS.md) et [docs/USAGE.md](docs/USAGE.md).
3. Utilisez le skill avec un brief projet clair ou une demande d'audit.
4. Pour créer des fichiers, commencez par `PLAN_ONLY` ou `--dry-run`.
5. Avant publication, exécutez validation, secret scan, vérification des liens et vérification remote.

## Guide de décision

| Si vous avez besoin de... | Utilisez... |
| --- | --- |
| Contexte projet réutilisable | `docs/`, `references/` ou documents starter générés |
| Règles obligatoires pour agents | `AGENTS.md` et adaptateurs par outil |
| Exemples sûrs | `docs/EXAMPLES.md` et données fictives |
| Publication publique | `docs/PUBLIC_REPO_CHECKLIST.md`, `docs/GITHUB_SETTINGS.md` et secret scan |

## Carte du dépôt

| Chemin | Pourquoi c'est important |
| --- | --- |
| [.agents/skills/ai-project-starter/SKILL.md](.agents/skills/ai-project-starter/SKILL.md) | Point d'entrée du skill et routing des modes |
| [.agents/skills/ai-project-starter/references/](.agents/skills/ai-project-starter/references/) | Connaissance en progressive disclosure |
| [.agents/skills/ai-project-starter/templates/](.agents/skills/ai-project-starter/templates/) | Skeletons de documentation starter |
| [.agents/skills/ai-project-starter/scripts/create_starter.py](.agents/skills/ai-project-starter/scripts/create_starter.py) | Materializer sûr avec dry-run et no-overwrite par défaut |
| [docs/USAGE.md](docs/USAGE.md) | Modes et exemples d'utilisation |
| [docs/PUBLIC_REPO_CHECKLIST.md](docs/PUBLIC_REPO_CHECKLIST.md) | Sécurité avant publication |
| [docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md) | Trust boundaries et approval gates |

## Validation

```powershell
npm run check
git diff --check
gitleaks dir . --no-banner --redact
git status --short --branch
```

`npm run check` exécute la validation structurelle et le smoke test du starter. Le smoke test lance le materializer uniquement en mode dry-run et n'écrit aucun fichier.

## Limite de sécurité

Ce dépôt ne doit contenir aucun secret, token, cookie, clé privée, prompt privé, donnée client, détail propriétaire d'implémentation, fichier local d'authentification, log, capture, archive ou sortie de build.

Les contenus externes, sorties d'outils, issues, logs, pages web et fichiers générés sont traités comme untrusted data. Les changements de dépendances, commits, pushes, releases et publications exigent une approbation explicite.

## Hygiène de release et publication

- Garder les changements centrés sur la documentation sauf si des scripts sont ajoutés intentionnellement.
- Mettre à jour release notes et changelog lorsque le contrat public du skill change.
- Exécuter checklist publique et secret scan avant commit, tag, push ou release.
- Après push, comparer HEAD local, `origin/main` et GitHub remote HEAD.

## Définition de terminé

Terminé signifie: contenu complet, liens corrects, limites de sécurité claires, validation exécutée, état Git vérifié et toute publication vérifiée à distance après le push.
