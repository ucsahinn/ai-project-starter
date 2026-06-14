# Context Engineering Project Starter

<p align="center">
  <a href="README.de.md">&#127465;&#127466; Deutsch</a> ? <a href="README.es.md">&#127466;&#127480; Espa&ntilde;ol</a> ? <a href="README.md">&#127468;&#127463; English</a> ? <a href="README.pt-BR.md">&#127463;&#127479; Portugu&ecirc;s (Brasil)</a> ? <a href="README.tr.md">&#127481;&#127479; T&uuml;rk&ccedil;e</a> ? <a href="README.fr.md">&#127467;&#127479; French</a>
</p>

Paquete de skill para Codex que crea briefs, especificaciones, arquitectura, tareas, guardrails e instrucciones de agente antes de codificar.

## Por que existe este repositorio

Paquete de skill para Codex que crea briefs, especificaciones, arquitectura, tareas, guardrails e instrucciones de agente antes de codificar.

Esta portada localizada se mantiene para que el lector entienda el repositorio sin depender de una etiqueta de idioma corta. La referencia canonica profunda sigue en README.md; esta pagina contiene suficiente contexto para elegir el punto de entrada, el limite de seguridad y la verificacion correcta.

## Para quien es

Founders, equipos de producto y developers que quieren empezar AI coding con contexto duradero, no prompts improvisados.

## Inicio rapido

| Si necesitas... | Abre |
| --- | --- |
| Usage guide | [docs/USAGE.md](docs/USAGE.md) |
| Install guide | [docs/INSTALL.md](docs/INSTALL.md) |
| Examples | [docs/EXAMPLES.md](docs/EXAMPLES.md) |
| Skill structure | [docs/SKILL_STRUCTURE.md](docs/SKILL_STRUCTURE.md) |
| Security model | [docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md) |
| Public repo checklist | [docs/PUBLIC_REPO_CHECKLIST.md](docs/PUBLIC_REPO_CHECKLIST.md) |

## Mapa del repositorio

- .agents/skills/context-engineering-project-starter/SKILL.md - skill entrypoint
- docs/ - usage, install, examples, structure and security
- AGENTS.md - repo operating guidance
- RELEASE_NOTES.md / CHANGELOG.md - public history
- SECURITY.md - disclosure and safety rules

## Validacion e higiene de release

Antes de commit o publicacion, revisa links, Markdown, validacion existente del repo y Gitleaks.

Ruta recomendada de release/readiness:

1. Revisar el README relevante y los documentos enlazados.
2. Ejecutar la validacion del repositorio cuando exista un comando.
3. Comprobar links Markdown y assets locales.
4. Ejecutar Gitleaks o el secret scan configurado.
5. Verificar origin/main despues del push antes de afirmar que la publicacion termino.

## Limite de seguridad y alcance publico

Los archivos starter no deben sobrescribir trabajo existente. Datos privados, secretos y rutas locales quedan fuera de ejemplos y templates.

## Contribucion y mantenimiento

Mant?n las paginas localizadas alineadas con el README canonico cuando cambien el alcance, los pasos de instalacion, las reglas de release o los limites de seguridad. No agregues afirmaciones que no esten respaldadas por el repositorio, docs live del producto o evidencia publica de release.

## Estandar de completitud

Este README localizado no es una nota corta. Explica proposito, entrada, superficies del repositorio, validacion, limite de seguridad y referencias canonicas.

Referencia canonica: [README.md](README.md).
