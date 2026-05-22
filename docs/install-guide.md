# Install Guide

This guide is for recreating the public parts of the stack on another machine, including Windows with WSL.

## Recommended Order

1. Install Codex and Claude Code using their official installers or current package instructions.
2. Clone this repo.
3. Run the install plan script.
4. Install plugin-derived capabilities first.
5. Review custom/direct skills separately.

```bash
git clone <this-repo-url>
cd agent-stack-public
python3 scripts/render_install_plan.py --summary
python3 scripts/render_install_plan.py --method plugin --limit 200
```

## WSL Notes

- Keep Codex and Claude Code config inside the WSL user home when running Linux tooling.
- Do not copy macOS auth/config folders into WSL.
- Re-authenticate tools on the work machine instead of moving tokens.
- Install plugins from public sources or marketplaces, not from another machine's cache.

## Plugin-Derived Skills

Plugin-derived skills are the easiest to reproduce. Look up rows with:

```bash
python3 scripts/render_install_plan.py --host codex --method plugin
python3 scripts/render_install_plan.py --host claude-code --method plugin
```

Each row points to a plugin name, marketplace, and source label. Use the host tool's current plugin installation flow.

## Bundled Runtime Skills

Bundled runtime skills should be handled by updating the host runtime:

```bash
python3 scripts/render_install_plan.py --method bundled-runtime
```

Do not copy bundled cache folders between machines.

## Custom Or Direct Skills

Custom/direct skills are intentionally listed without raw bodies.

```bash
python3 scripts/render_install_plan.py --method manual-review --limit 200
```

For each wanted skill, use one of these safe routes:

- install it from its own public repo;
- ask the owner for a reviewed `SKILL.md`;
- recreate it from public documentation;
- skip it if it depends on private workflow, secrets, customer context, or local paths.

## Verification

After editing this repo or regenerating data:

```bash
python3 scripts/generate_inventory.py
bash scripts/privacy_check.sh
```

If available, also run:

```bash
detect-secrets scan --all-files .
```
