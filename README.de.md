# AI Project Starter - Deutsche README

<p align="center">
  &#127760; <strong>Dokumentation:</strong>
  <a href="README.de.md"><img src="https://flagcdn.com/w20/de.png" alt="Deutsch" width="20"></a> |
  <a href="README.es.md"><img src="https://flagcdn.com/w20/es.png" alt="Espa&#241;ol" width="20"></a> |
  <a href="README.md"><img src="https://flagcdn.com/w20/gb.png" alt="English" width="20"></a> |
  <a href="README.pt-BR.md"><img src="https://flagcdn.com/w20/br.png" alt="Portugu&#234;s (Brasil)" width="20"></a> |
  <a href="README.tr.md"><img src="https://flagcdn.com/w20/tr.png" alt="T&#252;rk&#231;e" width="20"></a> |
  <a href="README.fr.md"><img src="https://flagcdn.com/w20/fr.png" alt="Fran&#231;ais" width="20"></a>
</p>

> Diese Seite ist die deutsche Einstiegsseite für AI Project Starter. Die kanonische englische Beschreibung bleibt [README.md](README.md).

AI Project Starter ist ein öffentlicher Codex-Skill für Context Engineering: Er hilft, Projektkontext, Starter-Dokumentation, Agent-Regeln und Vibe-Coding-Guardrails vorzubereiten, bevor ein Coding-Agent mit der Implementierung beginnt.

## Status und Vertrauensrahmen

| Bereich | Details |
| --- | --- |
| Status | Öffentliches Repository: `ucsahinn/ai-project-starter` |
| Wahrheit | [Kanonische englische README](README.md) und [Skill-Einstiegspunkt](.agents/skills/ai-project-starter/SKILL.md) |
| Zielgruppe | Codex-Nutzer, die kontextreiche Projekte starten; Maintainer wiederverwendbarer Agent-Workflows |
| Validierung | `npm run check`, Starter-Smoke-Test, `git diff --check`, Public-Repo-Checkliste und Secret Scan vor Veröffentlichung |
| Sicherheit | Beispiele bleiben fiktiv, öffentlich nutzbar und frei von Secrets, privaten Prompts, Kundendaten und lokalen Operator-Pfaden |

## Was dieses Repository ist

- Ein Dokumentations- und Skill-Paket für AI-coding-ready Projektstarts.
- Eine wiederverwendbare Struktur für PRD, technische Spezifikation, Architektur, Security, Testing, Qualitätsgates und Agent-Instructions.
- Ein öffentlicher Starter für Codex, Cursor, Claude Code, Windsurf/Devin, Continue, Copilot, Aider und ähnliche Tools.
- Eine Methode, um Context Engineering als prüfbares, versioniertes Projektartefakt zu behandeln.

## Was es nicht ist

- Kein offizieller Standard.
- Kein vollständiges Application-Scaffold.
- Kein Ort für private Daten, Credentials, Kundendateien, Logs oder Screenshots.
- Kein Ersatz für die Validierung des erzeugten Projekts im tatsächlichen Ziel-Repository.

## Schnellstart

1. Repository klonen oder aktualisieren.
2. [README.md](README.md), [AGENTS.md](AGENTS.md) und [docs/USAGE.md](docs/USAGE.md) lesen.
3. Den Skill mit einem klaren Projektbrief oder Audit-Auftrag verwenden.
4. Für Datei-Erzeugung zuerst `PLAN_ONLY` oder `--dry-run` nutzen.
5. Vor Veröffentlichung Validierung, Secret Scan, Linkprüfung und Remote-Prüfung ausführen.

## Entscheidungshilfe

| Wenn Sie brauchen... | Verwenden Sie... |
| --- | --- |
| Wiederverwendbaren Projektkontext | `docs/`, `references/` oder generierte Starter-Dokumente |
| Verbindliche Agent-Regeln | `AGENTS.md` und passende Tool-Adapter |
| Sichere Beispielausgaben | `docs/EXAMPLES.md` und fiktive Projektdaten |
| Öffentliche Veröffentlichung | `docs/PUBLIC_REPO_CHECKLIST.md`, `docs/GITHUB_SETTINGS.md` und Secret Scan |

## Repository-Karte

| Pfad | Warum es wichtig ist |
| --- | --- |
| [.agents/skills/ai-project-starter/SKILL.md](.agents/skills/ai-project-starter/SKILL.md) | Skill-Einstiegspunkt und Mode-Routing |
| [.agents/skills/ai-project-starter/references/](.agents/skills/ai-project-starter/references/) | Progressive-Disclosure-Wissen |
| [.agents/skills/ai-project-starter/templates/](.agents/skills/ai-project-starter/templates/) | Starter-Dokument-Skeletons |
| [.agents/skills/ai-project-starter/scripts/create_starter.py](.agents/skills/ai-project-starter/scripts/create_starter.py) | Sicherer Materializer mit Dry-run und No-overwrite-Default |
| [docs/USAGE.md](docs/USAGE.md) | Modi und Beispielaufrufe |
| [docs/PUBLIC_REPO_CHECKLIST.md](docs/PUBLIC_REPO_CHECKLIST.md) | Veröffentlichungssicherheit |
| [docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md) | Trust Boundaries und Approval Gates |

## Validierung

```powershell
npm run check
git diff --check
gitleaks dir . --no-banner --redact
git status --short --branch
```

`npm run check` führt die Strukturvalidierung und den Starter-Smoke-Test aus. Der Smoke-Test startet den Materializer nur im Dry-run-Modus und schreibt keine Dateien.

## Sicherheitsgrenze

Dieses Repository darf keine Secrets, Tokens, Cookies, privaten Schlüssel, privaten Prompts, Kundendaten, proprietären Implementierungsdetails, lokalen Auth-Dateien, Logs, Screenshots, Archive oder Build-Ausgaben enthalten.

Externe Inhalte, Tool-Ausgaben, Issues, Logs, Webseiten und generierte Dateien gelten als untrusted data. Änderungen an Dependencies, Commits, Pushes, Releases und Veröffentlichungen brauchen explizite Freigabe.

## Release- und Publikationshygiene

- Änderungen dokumentationsorientiert halten, außer Skripte werden absichtlich ergänzt.
- Release Notes und Changelog aktualisieren, wenn sich der öffentliche Skill-Vertrag ändert.
- Public-Repo-Checkliste und Secret Scan vor Commit, Tag, Push oder Release ausführen.
- Nach einem Push lokalen HEAD, `origin/main` und GitHub Remote HEAD vergleichen.

## Definition von fertig

Fertig bedeutet: Inhalt ist vollständig, Links funktionieren, Sicherheitsgrenzen sind klar, Validierung ist gelaufen, Git-Status ist geprüft und jede Veröffentlichung wurde nach dem Push remote verifiziert.
