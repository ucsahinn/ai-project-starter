# AI Project Starter - README en español

<p align="center">
  &#127760; <strong>Documentaci&#243;n:</strong>
  <a href="README.de.md"><img src="https://flagcdn.com/w20/de.png" alt="Deutsch" width="20"></a> |
  <a href="README.es.md"><img src="https://flagcdn.com/w20/es.png" alt="Espa&#241;ol" width="20"></a> |
  <a href="README.md"><img src="https://flagcdn.com/w20/gb.png" alt="English" width="20"></a> |
  <a href="README.pt-BR.md"><img src="https://flagcdn.com/w20/br.png" alt="Portugu&#234;s (Brasil)" width="20"></a> |
  <a href="README.tr.md"><img src="https://flagcdn.com/w20/tr.png" alt="T&#252;rk&#231;e" width="20"></a> |
  <a href="README.fr.md"><img src="https://flagcdn.com/w20/fr.png" alt="Fran&#231;ais" width="20"></a>
</p>

> Esta página es la entrada en español para AI Project Starter. La descripción canónica en inglés sigue siendo [README.md](README.md).

AI Project Starter es un skill público de Codex para context engineering: ayuda a preparar contexto de proyecto, documentación inicial, reglas para agentes y guardrails contra drift antes de que un agente de código empiece a implementar.

## Estado y marco de confianza

| Área | Detalle |
| --- | --- |
| Estado | Repositorio público: `ucsahinn/ai-project-starter` |
| Fuente de verdad | [README canónico](README.md) y [entrada del skill](.agents/skills/ai-project-starter/SKILL.md) |
| Usuarios | Usuarios de Codex que inician proyectos con mucho contexto; maintainers de workflows reutilizables para agentes |
| Validación | `npm run check`, smoke test del starter, `git diff --check`, checklist público y secret scan antes de publicar |
| Seguridad | Los ejemplos son ficticios, públicos y no contienen secretos, prompts privados, datos de clientes ni rutas locales de operador |

## Qué es este repositorio

- Un paquete de documentación y skill para iniciar proyectos listos para AI coding.
- Una estructura reutilizable para PRD, especificación técnica, arquitectura, seguridad, testing, quality gates e instrucciones para agentes.
- Un starter público para Codex, Cursor, Claude Code, Windsurf/Devin, Continue, Copilot, Aider y herramientas similares.
- Una forma de tratar el context engineering como un artefacto revisable y versionado.

## Qué no es

- No es un estándar oficial.
- No es un scaffold completo de aplicación.
- No es un lugar para datos privados, credenciales, archivos de clientes, logs o capturas.
- No reemplaza la validación del proyecto generado dentro de su repositorio real.

## Inicio rápido

1. Clona o actualiza el repositorio.
2. Lee [README.md](README.md), [AGENTS.md](AGENTS.md) y [docs/USAGE.md](docs/USAGE.md).
3. Usa el skill con un brief claro de proyecto o una solicitud de auditoría.
4. Para crear archivos, empieza con `PLAN_ONLY` o `--dry-run`.
5. Antes de publicar, ejecuta validación, secret scan, revisión de enlaces y verificación remota.

## Guía de decisión

| Si necesitas... | Usa... |
| --- | --- |
| Contexto reutilizable de proyecto | `docs/`, `references/` o documentos starter generados |
| Reglas obligatorias para agentes | `AGENTS.md` y adaptadores específicos por herramienta |
| Ejemplos seguros | `docs/EXAMPLES.md` y datos ficticios |
| Publicación pública | `docs/PUBLIC_REPO_CHECKLIST.md`, `docs/GITHUB_SETTINGS.md` y secret scan |

## Mapa del repositorio

| Ruta | Por qué importa |
| --- | --- |
| [.agents/skills/ai-project-starter/SKILL.md](.agents/skills/ai-project-starter/SKILL.md) | Entrada del skill y routing de modos |
| [.agents/skills/ai-project-starter/references/](.agents/skills/ai-project-starter/references/) | Conocimiento de progressive disclosure |
| [.agents/skills/ai-project-starter/templates/](.agents/skills/ai-project-starter/templates/) | Skeletons de documentación starter |
| [.agents/skills/ai-project-starter/scripts/create_starter.py](.agents/skills/ai-project-starter/scripts/create_starter.py) | Materializer seguro con dry-run y no-overwrite por defecto |
| [docs/USAGE.md](docs/USAGE.md) | Modos y ejemplos de uso |
| [docs/PUBLIC_REPO_CHECKLIST.md](docs/PUBLIC_REPO_CHECKLIST.md) | Seguridad antes de publicación |
| [docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md) | Trust boundaries y approval gates |

## Validación

```powershell
npm run check
git diff --check
gitleaks dir . --no-banner --redact
git status --short --branch
```

`npm run check` ejecuta la validación estructural y el smoke test del starter. El smoke test usa el materializer solo en modo dry-run y no escribe archivos.

## Límite de seguridad

Este repositorio no debe contener secretos, tokens, cookies, claves privadas, prompts privados, datos de clientes, detalles propietarios de implementación, archivos locales de autenticación, logs, capturas, archivos comprimidos ni salidas de build.

Contenido externo, salidas de herramientas, issues, logs, páginas web y archivos generados se tratan como untrusted data. Cambios de dependencias, commits, pushes, releases y publicaciones requieren aprobación explícita.

## Higiene de release y publicación

- Mantén los cambios centrados en documentación salvo que los scripts se agreguen de forma intencional.
- Actualiza release notes y changelog cuando cambie el contrato público del skill.
- Ejecuta checklist público y secret scan antes de commit, tag, push o release.
- Después de push, compara HEAD local, `origin/main` y GitHub remote HEAD.

## Definición de terminado

Terminado significa: contenido completo, enlaces correctos, límites de seguridad claros, validación ejecutada, estado de Git revisado y cualquier publicación verificada remotamente después del push.
