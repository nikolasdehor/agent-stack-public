# Agent Quickstart

Use this repo to understand the stack, choose what to install, and avoid copying private state.

## Agent Workflow

1. Read `data/summary.json` to understand the size of the stack.
2. Read `data/skill-sources.json` when a task mentions a specific skill.
3. If `install_method` is `plugin`, install or enable the listed plugin from `source_url_or_label`.
4. If `install_method` is `bundled-runtime`, update the host runtime.
5. If `install_method` is `manual-review`, do not install from this repo. Ask for an approved source repo or reviewed skill file.

## Fast Queries

```bash
python3 scripts/render_install_plan.py --summary
python3 scripts/render_install_plan.py --skill react
python3 scripts/render_install_plan.py --host codex --method plugin
python3 scripts/render_install_plan.py --host claude-code --category security
```

## How To Read `skill-sources.json`

| Field | Meaning |
| --- | --- |
| `skill` | Skill name |
| `category` | Heuristic category |
| `host` | Intended host: `codex`, `claude-code`, `shared-agents`, or `manual` |
| `install_method` | Safe install route |
| `resolution_status` | Whether the source is public, bundled/marketplace, or requires manual source review |
| `plugin` | Plugin that contributes the skill, when known |
| `marketplace` | Plugin marketplace or namespace |
| `source_url_or_label` | Public repo, marketplace label, or bundled runtime label |
| `source_locator` | Sanitized relative locator, useful for debugging origin |
| `install_note` | Human-readable install guidance |

## Install Method Policy

| Method | Meaning |
| --- | --- |
| `plugin` | Install the plugin using the host tool or the public source. Do not copy cache folders. |
| `bundled-runtime` | Update the host app/runtime. The skill is shipped with it. |
| `manual-review` | Inventory only. The raw skill body is not published here. |
| `unknown` | No safe install route was inferred. |

## Practical Use

When a user says "set up my work machine like this stack", start from plugin-derived rows. They have public repos or marketplace labels and are safer to reproduce.

For direct/custom skills, make a checklist rather than an installer. The checklist should say which skills are desired and which source repo or reviewed `SKILL.md` is still needed.
