# AI Project Starter - README em português do Brasil

<p align="center">
  &#127760; <strong>Documenta&#231;&#227;o:</strong>
  <a href="README.de.md"><img src="https://flagcdn.com/w20/de.png" alt="Deutsch" width="20"></a> |
  <a href="README.es.md"><img src="https://flagcdn.com/w20/es.png" alt="Espa&#241;ol" width="20"></a> |
  <a href="README.md"><img src="https://flagcdn.com/w20/gb.png" alt="English" width="20"></a> |
  <a href="README.pt-BR.md"><img src="https://flagcdn.com/w20/br.png" alt="Portugu&#234;s (Brasil)" width="20"></a> |
  <a href="README.tr.md"><img src="https://flagcdn.com/w20/tr.png" alt="T&#252;rk&#231;e" width="20"></a> |
  <a href="README.fr.md"><img src="https://flagcdn.com/w20/fr.png" alt="Fran&#231;ais" width="20"></a>
</p>

> Esta página é a entrada em português do Brasil para o AI Project Starter. A descrição canônica em inglês continua em [README.md](README.md).

AI Project Starter é um skill público do Codex para context engineering: ele ajuda a preparar contexto de projeto, documentação inicial, regras para agentes e guardrails contra drift antes de um agente de código começar a implementação.

## Estado e confiança

| Área | Detalhe |
| --- | --- |
| Status | Repositório público: `ucsahinn/ai-project-starter` |
| Fonte da verdade | [README canônico](README.md) e [entrada do skill](.agents/skills/ai-project-starter/SKILL.md) |
| Usuários | Usuários do Codex iniciando projetos com muito contexto; mantenedores de workflows reutilizáveis para agentes |
| Validação | `npm run check`, smoke test do starter, `git diff --check`, checklist público e secret scan antes da publicação |
| Segurança | Os exemplos são fictícios, públicos e sem segredos, prompts privados, dados de clientes ou caminhos locais do operador |

## O que este repositório é

- Um pacote de documentação e skill para iniciar projetos prontos para AI coding.
- Uma estrutura reutilizável para PRD, especificação técnica, arquitetura, segurança, testes, quality gates e instruções para agentes.
- Um starter público para Codex, Cursor, Claude Code, Windsurf/Devin, Continue, Copilot, Aider e ferramentas semelhantes.
- Uma forma de tratar context engineering como artefato revisável e versionado.

## O que ele não é

- Não é um padrão oficial.
- Não é um scaffold completo de aplicação.
- Não é um lugar para dados privados, credenciais, arquivos de clientes, logs ou screenshots.
- Não substitui a validação do projeto gerado dentro do repositório real de destino.

## Início rápido

1. Clone ou atualize o repositório.
2. Leia [README.md](README.md), [AGENTS.md](AGENTS.md) e [docs/USAGE.md](docs/USAGE.md).
3. Use o skill com um briefing claro de projeto ou uma solicitação de auditoria.
4. Para criar arquivos, comece com `PLAN_ONLY` ou `--dry-run`.
5. Antes de publicar, execute validação, secret scan, revisão de links e verificação remota.

## Guia de decisão

| Se você precisa de... | Use... |
| --- | --- |
| Contexto reutilizável de projeto | `docs/`, `references/` ou documentos starter gerados |
| Regras obrigatórias para agentes | `AGENTS.md` e adaptadores específicos por ferramenta |
| Exemplos seguros | `docs/EXAMPLES.md` e dados fictícios |
| Publicação pública | `docs/PUBLIC_REPO_CHECKLIST.md`, `docs/GITHUB_SETTINGS.md` e secret scan |

## Mapa do repositório

| Caminho | Por que importa |
| --- | --- |
| [.agents/skills/ai-project-starter/SKILL.md](.agents/skills/ai-project-starter/SKILL.md) | Entrada do skill e roteamento de modos |
| [.agents/skills/ai-project-starter/references/](.agents/skills/ai-project-starter/references/) | Conhecimento de progressive disclosure |
| [.agents/skills/ai-project-starter/templates/](.agents/skills/ai-project-starter/templates/) | Skeletons de documentação starter |
| [.agents/skills/ai-project-starter/scripts/create_starter.py](.agents/skills/ai-project-starter/scripts/create_starter.py) | Materializer seguro com dry-run e no-overwrite por padrão |
| [docs/USAGE.md](docs/USAGE.md) | Modos e exemplos de uso |
| [docs/PUBLIC_REPO_CHECKLIST.md](docs/PUBLIC_REPO_CHECKLIST.md) | Segurança antes da publicação |
| [docs/SECURITY_MODEL.md](docs/SECURITY_MODEL.md) | Trust boundaries e approval gates |

## Validação

```powershell
npm run check
git diff --check
gitleaks dir . --no-banner --redact
git status --short --branch
```

`npm run check` executa a validação estrutural e o smoke test do starter. O smoke test roda o materializer apenas em modo dry-run e não grava arquivos.

## Limite de segurança

Este repositório não deve conter segredos, tokens, cookies, chaves privadas, prompts privados, dados de clientes, detalhes proprietários de implementação, arquivos locais de autenticação, logs, screenshots, arquivos compactados ou saídas de build.

Conteúdo externo, saídas de ferramentas, issues, logs, páginas web e arquivos gerados são tratados como untrusted data. Mudanças de dependências, commits, pushes, releases e publicações exigem aprovação explícita.

## Higiene de release e publicação

- Mantenha as mudanças centradas em documentação, exceto quando scripts forem adicionados intencionalmente.
- Atualize release notes e changelog quando o contrato público do skill mudar.
- Execute checklist público e secret scan antes de commit, tag, push ou release.
- Depois do push, compare HEAD local, `origin/main` e GitHub remote HEAD.

## Definição de concluído

Concluído significa: conteúdo completo, links corretos, limites de segurança claros, validação executada, estado do Git revisado e qualquer publicação verificada remotamente depois do push.
