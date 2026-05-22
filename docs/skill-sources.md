# Skill Sources

Este arquivo resume como cada grupo de skills deve ser resolvido por um agente.

A lista completa por skill fica em `data/skill-sources.json`. Este documento e o JSON indicam origem e caminho de instalação, mas não publicam conteúdo bruto de skills customizadas.

## Por Host

| host | skills |
| --- | ---: |
| claude-code | 1545 |
| codex | 270 |
| shared-agents | 352 |

## Por Metodo

| install_method | skills |
| --- | ---: |
| bundled-runtime | 6 |
| manual-review | 715 |
| plugin | 1446 |

## Por Resolucao

| resolution_status | skills |
| --- | ---: |
| manual-source-required | 716 |
| marketplace-or-bundled | 124 |
| public-source | 1327 |

## Como Interpretar

- `plugin`: instale ou habilite o plugin indicado pelo campo `plugin` e use `source_url_or_label` para descobrir o repo ou marketplace publico.
- `bundled-runtime`: vem junto do runtime do Codex; atualizar o runtime e o plugin bundled costuma ser o caminho correto.
- `manual-review`: skill direta ou customizada; este repo nao publica o conteudo dela. Use apenas um repo fonte aprovado ou um `SKILL.md` revisado.

## Amostra

| skill | host | method | resolution | plugin | source |
| --- | --- | --- | --- | --- | --- |
| a11y-debugging | claude-code | plugin | public-source | chrome-devtools-mcp | https://github.com/anthropics/claude-plugins-official |
| a11y-debugging | claude-code | plugin | public-source | chrome-devtools-mcp | https://github.com/anthropics/claude-plugins-official |
| access | claude-code | plugin | public-source | telegram | https://github.com/anthropics/claude-plugins-official |
| access | codex | plugin | public-source | telegram | https://github.com/anthropics/claude-plugins-official |
| agent-browser | codex | plugin | marketplace-or-bundled | vercel | OpenAI curated plugin marketplace |
| agent-browser-verify | codex | plugin | marketplace-or-bundled | vercel | OpenAI curated plugin marketplace |
| agent-development | claude-code | plugin | public-source | plugin-dev | https://github.com/anthropics/claude-plugins-official |
| agent-development | codex | plugin | public-source | plugin-dev | https://github.com/anthropics/claude-plugins-official |
| agents-sdk | codex | plugin | marketplace-or-bundled | cloudflare | OpenAI curated plugin marketplace |
| agents-sdk | codex | plugin | marketplace-or-bundled | openai-developers | OpenAI curated plugin marketplace |
| ai-elements | codex | plugin | marketplace-or-bundled | vercel | OpenAI curated plugin marketplace |
| ai-gateway | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| ai-gateway | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| ai-gateway | codex | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| ai-gateway | codex | plugin | marketplace-or-bundled | vercel | OpenAI curated plugin marketplace |
| ai-generation-persistence | codex | plugin | marketplace-or-bundled | vercel | OpenAI curated plugin marketplace |
| ai-sdk | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| ai-sdk | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| ai-sdk | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| ai-sdk | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| ai-sdk | codex | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| ai-sdk | codex | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| ai-sdk | codex | plugin | marketplace-or-bundled | vercel | OpenAI curated plugin marketplace |
| analyzing-experiment-session-replays | claude-code | plugin | public-source | posthog | https://github.com/anthropics/claude-plugins-official |
| analyzing-experiment-session-replays | claude-code | plugin | public-source | posthog | https://github.com/anthropics/claude-plugins-official |
| analyzing-experiment-session-replays | codex | plugin | public-source | posthog | https://github.com/anthropics/claude-plugins-official |
| android-emulator-qa | codex | plugin | marketplace-or-bundled | test-android-apps | OpenAI curated plugin marketplace |
| android-performance | codex | plugin | marketplace-or-bundled | test-android-apps | OpenAI curated plugin marketplace |
| appkit-interop | codex | plugin | marketplace-or-bundled | build-macos-apps | OpenAI curated plugin marketplace |
| attack-path-analysis | codex | plugin | marketplace-or-bundled | codex-security | OpenAI curated plugin marketplace |
| auditing-experiments-flags | claude-code | plugin | public-source | posthog | https://github.com/anthropics/claude-plugins-official |
| auditing-experiments-flags | claude-code | plugin | public-source | posthog | https://github.com/anthropics/claude-plugins-official |
| auditing-experiments-flags | codex | plugin | public-source | posthog | https://github.com/anthropics/claude-plugins-official |
| auditing-warehouse-data-health | claude-code | plugin | public-source | posthog | https://github.com/anthropics/claude-plugins-official |
| auditing-warehouse-data-health | claude-code | plugin | public-source | posthog | https://github.com/anthropics/claude-plugins-official |
| auditing-warehouse-data-health | codex | plugin | public-source | posthog | https://github.com/anthropics/claude-plugins-official |
| auth | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| auth | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| auth | codex | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| auth | codex | plugin | marketplace-or-bundled | vercel | OpenAI curated plugin marketplace |
| authoring-log-alerts | claude-code | plugin | public-source | posthog | https://github.com/anthropics/claude-plugins-official |
| authoring-log-alerts | codex | plugin | public-source | posthog | https://github.com/anthropics/claude-plugins-official |
| babysit | claude-code | plugin | public-source | claude-mem | https://github.com/thedotmack/claude-mem |
| babysit | claude-code | plugin | public-source | claude-mem | https://github.com/thedotmack/claude-mem |
| babysit | claude-code | plugin | public-source | claude-mem | https://github.com/thedotmack/claude-mem |
| babysit | claude-code | plugin | public-source | claude-mem | https://github.com/thedotmack/claude-mem |
| benchmark-agents | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| benchmark-agents | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| benchmark-agents | codex | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| benchmark-e2e | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| benchmark-e2e | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| benchmark-e2e | codex | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| benchmark-sandbox | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| benchmark-sandbox | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| benchmark-sandbox | codex | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| benchmark-testing | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| benchmark-testing | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| benchmark-testing | codex | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| bootstrap | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| bootstrap | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| bootstrap | codex | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| bootstrap | codex | plugin | marketplace-or-bundled | vercel | OpenAI curated plugin marketplace |
| brainstorming | claude-code | plugin | public-source | superpowers | https://github.com/anthropics/claude-plugins-official |
| brainstorming | codex | plugin | public-source | superpowers | https://github.com/anthropics/claude-plugins-official |
| brainstorming | codex | plugin | marketplace-or-bundled | superpowers | OpenAI curated plugin marketplace |
| build-chatgpt-app | codex | plugin | marketplace-or-bundled | openai-developers | OpenAI curated plugin marketplace |
| build-run-debug | codex | plugin | marketplace-or-bundled | build-macos-apps | OpenAI curated plugin marketplace |
| building-ai-agent-on-cloudflare | codex | plugin | marketplace-or-bundled | cloudflare | OpenAI curated plugin marketplace |
| building-mcp-server-on-cloudflare | codex | plugin | marketplace-or-bundled | cloudflare | OpenAI curated plugin marketplace |
| canva-branded-presentation | codex | plugin | marketplace-or-bundled | canva | OpenAI curated plugin marketplace |
| canva-resize-for-all-social-media | codex | plugin | marketplace-or-bundled | canva | OpenAI curated plugin marketplace |
| canva-translate-design | codex | plugin | marketplace-or-bundled | canva | OpenAI curated plugin marketplace |
| chat-sdk | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| chat-sdk | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| chat-sdk | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| chat-sdk | claude-code | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| chat-sdk | codex | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| chat-sdk | codex | plugin | public-source | vercel | https://github.com/anthropics/claude-plugins-official |
| chat-sdk | codex | plugin | marketplace-or-bundled | vercel | OpenAI curated plugin marketplace |
| chatgpt-app-submission | codex | plugin | marketplace-or-bundled | openai-developers | OpenAI curated plugin marketplace |
