# Agent Stack

Mapa público de um ambiente de trabalho com Codex, Claude Code, skills, plugins, MCPs e rotinas de verificação.

Este repositório não é um backup do meu computador. Ele é uma documentação curada do stack: quais capacidades uso, como organizo agentes e quais limites sigo para não publicar credenciais, histórico, memórias ou configuração privada.

Para agentes, o arquivo mais útil é `data/skill-sources.json`: ele mapeia cada skill para host, plugin, marketplace, fonte pública quando conhecida e método seguro de instalação.

## Snapshot

Gerado em 2026-05-22.

| Área | Total |
| --- | ---: |
| Skills mapeadas | 2.167 |
| Plugins configurados no Codex | 44 |
| Plugins registrados no Claude Code | 56 |
| MCPs documentados por nome | 6 |

## O Que Este Repo Mostra

- Como organizo skills por capacidade: frontend, backend, segurança, repo ops, browser automation, deploy, documentação e operações de agentes.
- Quais plugins ficam no meu radar para Codex e Claude Code.
- Quais MCPs aparecem no stack, apenas por nome e transporte.
- Como penso em orquestração: agente principal integra, subagentes recebem escopos delimitados e a validação real fecha o trabalho.
- Como publicar um stack de agentes sem transformar o repo em vazamento de estado local.

## O Que Fica Fora

- `auth.json`, tokens, chaves, cookies, `.env` e sessões.
- `config.toml`, MCP args/envs reais, headers, URLs privadas e estado de login.
- Logs, histórico, bancos SQLite, memórias, transcrições e cache bruto de plugins.
- Paths locais, nomes de clientes, IPs privados ou dados de projetos fechados.

## Catálogo

| Documento | Conteúdo |
| --- | --- |
| [Skills inventory](docs/skills-inventory.md) | Skills diretas, com categoria, origem e descrição pública quando disponível |
| [Skill sources](docs/skill-sources.md) | Origem e método seguro de instalação por grupo de skills |
| [Agent quickstart](docs/agent-quickstart.md) | Fluxo para Codex, Claude Code e outros agentes consumirem este repo |
| [Install guide](docs/install-guide.md) | Guia seguro para recriar o stack em outra máquina ou WSL |
| [Codex plugins](docs/codex-plugins.md) | Plugins habilitados no Codex, por marketplace e categoria |
| [Claude Code plugins](docs/claude-code-plugins.md) | Plugins registrados no Claude Code, versão e origem pública quando disponível |
| [MCP servers](docs/mcp-servers.md) | MCPs por nome, transporte e nota de privacidade |
| [Privacy boundaries](docs/privacy-boundaries.md) | O modelo de publicação segura deste repo |
| [Workflows](docs/workflows.md) | Como uso o stack em tarefas reais sem publicar dados sensíveis |
| [Architecture](docs/architecture.md) | Visão do stack em camadas |

## Categorias

| Categoria | Papel |
| --- | --- |
| `ai-agent-ops` | Orquestração, memória, MCP, prompts, agentes e runtime |
| `browser-automation` | Navegação local, screenshots, QA visual e E2E |
| `cloud-deploy` | Deploy, infra, Vercel, Cloudflare, VPS e CI/CD |
| `data-analytics` | Supabase, PostHog, Postgres, planilhas e observabilidade |
| `docs-content` | Escrita, docs, apresentações, vídeo e conteúdo |
| `frontend` | React, Next.js, UI, mobile, design e experiência |
| `backend` | APIs, bancos, frameworks server-side e integrações |
| `github-repo-ops` | GitHub, PRs, revisão, testes, CI e repo hygiene |
| `security` | Auditorias, threat modeling, findings e hardening |

## Como Atualizar O Inventário

O gerador lê diretórios locais conhecidos e escreve apenas dados sanitizados em `data/` e `docs/`.

```bash
python3 scripts/generate_inventory.py
python3 scripts/render_install_plan.py --summary
bash scripts/privacy_check.sh
```

O script foi escrito para funcionar em Python 3.9+.

## Princípios

1. Documentar capacidades, não estado privado.
2. Preferir categorias e fontes públicas em vez de dumps de arquivos.
3. Tratar skills customizadas como potencialmente sensíveis.
4. Nunca publicar config real de MCP ou credenciais.
5. Fechar toda alteração pública com uma varredura de privacidade.

## Status

Este repo é um snapshot vivo. Ele deve ser lido como mapa editorial do stack, não como instalador automático.
