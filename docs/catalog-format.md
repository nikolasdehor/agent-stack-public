# Catalog Format

O catálogo usa dados sanitizados para ser útil sem expor estado local.

## Skills

Campos em `data/skills.json`:

| Campo | Significado |
| --- | --- |
| `name` | Nome público da skill |
| `description` | Descrição do frontmatter, quando existe |
| `category` | Categoria inferida por palavras-chave |
| `source` | Origem lógica, sem path absoluto |
| `relative_path` | Caminho relativo sanitizado |
| `has_frontmatter` | Se a skill tem frontmatter YAML |

## Skill Sources

Campos em `data/skill-sources.json`:

| Campo | Significado |
| --- | --- |
| `skill` | Nome público da skill |
| `category` | Categoria inferida |
| `host` | Host esperado, como `codex`, `claude-code` ou `shared-agents` |
| `install_method` | Caminho seguro de instalação: `plugin`, `bundled-runtime`, `manual-review` ou `unknown` |
| `resolution_status` | Se a origem é `public-source`, `marketplace-or-bundled` ou `manual-source-required` |
| `plugin` | Plugin que fornece a skill, quando conhecido |
| `marketplace` | Marketplace ou namespace do plugin |
| `source` | Origem lógica da skill no inventário |
| `source_url_or_label` | Repo público, marketplace ou rótulo de runtime bundled |
| `source_locator` | Localizador relativo sanitizado |
| `install_note` | Nota curta para agentes e humanos |

## Plugins

Campos em `data/codex-plugins.json` e `data/claude-plugins.json`:

| Campo | Significado |
| --- | --- |
| `plugin` | Nome público |
| `marketplace` | Marketplace ou namespace público |
| `version` | Versão quando disponível |
| `status` | Status público, sem auth state |
| `source` | Link público ou nota de origem |
| `category` | Categoria inferida |

## MCPs

Campos em `data/mcp-servers.json`:

| Campo | Significado |
| --- | --- |
| `name` | Nome público do servidor |
| `transport` | Tipo aproximado, como `stdio` ou `remote-http` |
| `category` | Categoria inferida |
| `public_note` | Lembrete de que args/envs foram omitidos |

## Limitações

As categorias são heurísticas. Elas servem para navegação e triagem, não como taxonomia perfeita.

O inventário também não afirma que uma skill ou plugin é recomendado para todo mundo. Ele documenta um stack real, com curadoria e limites.
