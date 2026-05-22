# CLAUDE.md

This repo helps Claude Code understand a public agent stack and map skills back to their safest install path.

## How To Use This Repo

1. Read `docs/agent-quickstart.md`.
2. Query `data/skill-sources.json` or run `scripts/render_install_plan.py`.
3. Prefer plugin installation over copying plugin cache contents.
4. Treat custom/direct skills as inventory only unless the user provides an approved source.

## Important Files

- `data/skill-sources.json`: per-skill source, plugin, marketplace, host, and install note.
- `data/skills.json`: sanitized skill inventory.
- `data/codex-plugins.json`: Codex plugins by marketplace and public source label.
- `data/claude-plugins.json`: Claude Code plugins by marketplace, version label, and public source.
- `docs/skill-sources.md`: readable summary of install methods.
- `docs/install-guide.md`: WSL-friendly setup notes.

## Do Not Publish Or Request

- Raw auth files, config files, local plugin cache, history, memory databases, logs, cookies, tokens, or private paths.
- Full custom skill bodies unless they were manually reviewed and intentionally published.
