# AGENTS.md

This repository is a public, sanitized map of a Codex and Claude Code agent stack. Treat it as an inventory and install guide, not as a raw backup.

## Start Here

- Read `README.md` for the human overview.
- Read `docs/agent-quickstart.md` for the agent workflow.
- Use `data/skill-sources.json` as the source of truth for skill origin and install method.
- Use `scripts/render_install_plan.py` to answer questions like "how do I install this skill?" or "which skills are plugin-derived?"

## Safety Rules

- Do not infer that this repo contains raw custom skill bodies. It does not.
- Do not ask users to copy private local directories, auth files, plugin caches, logs, memories, or config files.
- For `manual-review` skills, ask for an approved public source repo or a reviewed `SKILL.md` before installing.
- For `plugin` skills, install or enable the named plugin through the host tool or public source, then let the host expose its skills.
- For `bundled-runtime` skills, update the host runtime rather than copying cache files.

## Useful Commands

```bash
python3 scripts/render_install_plan.py --summary
python3 scripts/render_install_plan.py --skill frontend
python3 scripts/render_install_plan.py --host claude-code --method plugin
bash scripts/privacy_check.sh
```

Before publishing changes, run the privacy check and a secret scan if available.
