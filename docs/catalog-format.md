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
