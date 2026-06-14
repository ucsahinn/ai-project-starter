# Context Engineering Project Starter

<p align="center">
  <a href="README.de.md">&#127465;&#127466; Deutsch</a> ? <a href="README.es.md">&#127466;&#127480; Espa&ntilde;ol</a> ? <a href="README.md">&#127468;&#127463; English</a> ? <a href="README.pt-BR.md">&#127463;&#127479; Portugu&ecirc;s (Brasil)</a> ? <a href="README.tr.md">&#127481;&#127479; T&uuml;rk&ccedil;e</a> ? <a href="README.fr.md">&#127467;&#127479; French</a>
</p>

Pacote de skill para Codex que cria briefs, especificacoes, arquitetura, tarefas, guardrails e instrucoes de agente antes de codar.

## Por que este repositorio existe

Pacote de skill para Codex que cria briefs, especificacoes, arquitetura, tarefas, guardrails e instrucoes de agente antes de codar.

Esta pagina localizada e mantida para que leitores entendam o repositorio sem depender apenas de uma etiqueta curta de idioma. A referencia canonica profunda continua em README.md; esta pagina traz contexto suficiente para escolher a entrada, o limite de seguranca e a verificacao correta.

## Para quem e

Founders, times de produto e developers que querem comecar AI coding com contexto duravel, nao prompts improvisados.

## Comeco rapido

| Se voce precisa... | Abra |
| --- | --- |
| Usage guide | [docs/USAGE.md](docs/USAGE.md) |
| Install guide | [docs/INSTALL.md](docs/INSTALL.md) |
| Examples | [docs/EXAMPLES.md](docs/EXAMPLES.md) |
| Skill structure | [docs/SKILL_STRUCTURE.md](docs/SKILL_STRUCTURE.md) |
| Security model | [docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md) |
| Public repo checklist | [docs/PUBLIC_REPO_CHECKLIST.md](docs/PUBLIC_REPO_CHECKLIST.md) |

## Mapa do repositorio

- .agents/skills/context-engineering-project-starter/SKILL.md - skill entrypoint
- docs/ - usage, install, examples, structure and security
- AGENTS.md - repo operating guidance
- RELEASE_NOTES.md / CHANGELOG.md - public history
- SECURITY.md - disclosure and safety rules

## Validacao e higiene de release

Antes de commit ou publicacao, revise links, Markdown, validacao existente do repo e Gitleaks.

Caminho recomendado de release/readiness:

1. Revise o README relevante e os documentos linkados.
2. Execute a validacao do repositorio quando existir um comando.
3. Verifique links Markdown e assets locais.
4. Execute Gitleaks ou o secret scan configurado.
5. Verifique origin/main depois do push antes de afirmar que a publicacao terminou.

## Limite de seguranca e escopo publico

Arquivos starter nao devem sobrescrever trabalho existente. Dados privados, segredos e caminhos locais ficam fora de exemplos e templates.

## Contribuicao e manutencao

Mantenha as paginas localizadas alinhadas com o README canonico quando escopo, passos de instalacao, regras de release ou limites de seguranca mudarem. Nao adicione afirmacoes sem respaldo no repositorio, docs live do produto ou evidencia publica de release.

## Padrao de completude

Este README localizado nao e uma nota curta. Ele explica proposito, entrada, superficies do repositorio, validacao, limite de seguranca e referencias canonicas.

Referencia canonica: [README.md](README.md).
