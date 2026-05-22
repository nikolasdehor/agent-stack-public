#!/usr/bin/env python3
"""Generate a sanitized public inventory for a Codex + Claude Code stack."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path


HOME = Path.home()
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DOCS_DIR = ROOT / "docs"

def build_sensitive_patterns() -> list[re.Pattern[str]]:
    patterns = [
        re.compile(r"/Users/[^\s`'\"<>]+"),
        re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", re.IGNORECASE),
        re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"),
        re.compile(r"sk-(?:proj|live|test)-[A-Za-z0-9_-]{20,}"),
        re.compile(r"sk-[A-Za-z0-9_-]{48,}"),
        re.compile(r"ghp_[A-Za-z0-9_]+"),
        re.compile(r"gho_[A-Za-z0-9_]+"),
    ]
    if HOME.name:
        patterns.append(re.compile(rf"\b{re.escape(HOME.name)}\b", re.IGNORECASE))
    return patterns


SENSITIVE_PATTERNS = build_sensitive_patterns()
REVISION_PATTERN = re.compile(r"\b[0-9a-f]{12,40}\b", re.IGNORECASE)

DIRECT_SKILL_SOURCES = {"codex-direct", "agents-direct", "claude-direct", "claude-dot-agents"}

FORBIDDEN_PATH_MARKERS = [
    "/.git/",
    "/node_modules/",
    "/tests/",
    "plugin-backup",
    "plugin-install",
    "temp_git",
    "temp_subdir",
    ".bak",
    ".backup",
]

CATEGORY_KEYWORDS = {
    "frontend": ["frontend", "react", "next", "ui", "ux", "tailwind", "shadcn", "web-design"],
    "backend": ["backend", "api", "fastapi", "django", "nestjs", "laravel", "spring", "database"],
    "security": ["security", "secure", "audit", "threat", "vulnerability", "zeroize", "semgrep", "supply-chain"],
    "cloud-deploy": ["vercel", "cloudflare", "deploy", "devops", "docker", "railway", "hostinger"],
    "browser-automation": ["browser", "chrome", "playwright", "e2e"],
    "docs-content": ["docs", "documentation", "article", "markdown", "slides", "video", "writing"],
    "github-repo-ops": ["github", "git", "pr", "review", "ci", "commit"],
    "ai-agent-ops": ["agent", "agents", "mcp", "memory", "claude", "codex", "openai", "superpowers"],
    "data-analytics": ["data", "analytics", "posthog", "spreadsheet", "postgres", "supabase", "clickhouse"],
}


def run(args: list[str]) -> str:
    try:
        return subprocess.check_output(args, text=True, stderr=subprocess.DEVNULL)
    except Exception:
        return ""


def sanitize_text(value: str) -> str:
    sanitized = value
    for pattern in SENSITIVE_PATTERNS:
        sanitized = pattern.sub("[redacted]", sanitized)
    sanitized = REVISION_PATTERN.sub("revision", sanitized)
    return sanitized


def safe_relative(path: Path) -> str:
    for base_name, base in [
        ("codex-skills", HOME / ".codex" / "skills"),
        ("agents-skills", HOME / ".agents" / "skills"),
        ("claude-skills", HOME / ".claude" / "skills"),
        ("claude-dot-agents-skills", HOME / ".claude" / ".agents" / "skills"),
        ("codex-plugin-cache", HOME / ".codex" / "plugins" / "cache"),
        ("claude-plugin-cache", HOME / ".claude" / "plugins" / "cache"),
    ]:
        try:
            rel = path.relative_to(base)
        except ValueError:
            continue
        return sanitize_text(f"{base_name}/{rel}")
    return sanitize_text(str(path))


def read_frontmatter(skill_file: Path) -> dict[str, str]:
    try:
        text = skill_file.read_text(errors="replace")
    except Exception:
        return {}
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    block = text[4:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if value in {">", ">-", "|", "|-"}:
            value = ""
        if key in {"name", "description", "origin"}:
            data[key] = sanitize_text(value)
    return data


def infer_category(name: str, description: str = "") -> str:
    haystack = f"{name} {description}".lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(keyword in haystack for keyword in keywords):
            return category
    return "general"


def collect_skills() -> list[dict[str, str]]:
    roots = [
        ("codex-direct", HOME / ".codex" / "skills"),
        ("agents-direct", HOME / ".agents" / "skills"),
        ("claude-direct", HOME / ".claude" / "skills"),
        ("claude-dot-agents", HOME / ".claude" / ".agents" / "skills"),
        ("codex-plugin-derived", HOME / ".codex" / "plugins" / "cache"),
        ("claude-plugin-derived", HOME / ".claude" / "plugins" / "cache"),
    ]
    rows: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for source, root in roots:
        if not root.exists():
            continue
        for skill_file in root.rglob("SKILL.md"):
            rel = safe_relative(skill_file)
            if any(marker in rel for marker in FORBIDDEN_PATH_MARKERS):
                continue
            meta = read_frontmatter(skill_file)
            skill_dir = skill_file.parent.name
            name = meta.get("name") or skill_dir
            description = meta.get("description", "")
            if source in DIRECT_SKILL_SOURCES:
                description = ""
            key = (source, rel)
            if key in seen:
                continue
            seen.add(key)
            rows.append(
                {
                    "name": sanitize_text(name),
                    "description": description,
                    "category": infer_category(name, description),
                    "source": source,
                    "relative_path": rel,
                    "has_frontmatter": str(bool(meta)).lower(),
                }
            )
    return sorted(rows, key=lambda item: (item["source"], item["name"], item["relative_path"]))


def collect_codex_plugins() -> list[dict[str, str]]:
    config_path = HOME / ".codex" / "config.toml"
    if not config_path.exists():
        return []
    plugins: dict[str, dict[str, bool]] = {}
    current_key: str | None = None
    for raw_line in config_path.read_text(errors="replace").splitlines():
        line = raw_line.strip()
        match = re.match(r'^\[plugins\."([^"]+)"\]$', line)
        if match:
            current_key = match.group(1)
            plugins[current_key] = {}
            continue
        if current_key and line.startswith("enabled"):
            plugins[current_key]["enabled"] = line.split("=", 1)[1].strip().lower() == "true"
    rows = []
    for key, value in sorted(plugins.items()):
        name, _, marketplace = key.partition("@")
        rows.append(
            {
                "plugin": sanitize_text(name),
                "marketplace": sanitize_text(marketplace),
                "status": "enabled" if value.get("enabled") else "disabled",
                "source": infer_plugin_source(marketplace),
                "category": infer_category(name),
            }
        )
    return rows


def collect_codex_mcps() -> list[dict[str, str]]:
    config_path = HOME / ".codex" / "config.toml"
    if not config_path.exists():
        return []
    rows: list[dict[str, str]] = []
    current_name: str | None = None
    current: dict[str, str] | None = None
    for raw_line in config_path.read_text(errors="replace").splitlines():
        line = raw_line.strip()
        match = re.match(r"^\[mcp_servers\.([A-Za-z0-9_-]+)\]$", line)
        if match:
            if current:
                rows.append(current)
            current_name = match.group(1)
            current = {
                "name": sanitize_text(current_name),
                "transport": "unknown",
                "category": infer_category(current_name),
                "public_note": "Name only. Command args, URLs, env vars, and auth state intentionally omitted.",
            }
            continue
        if not current:
            continue
        if line.startswith("url"):
            current["transport"] = "remote-http"
        elif line.startswith("command"):
            current["transport"] = "stdio"
    if current:
        rows.append(current)
    return sorted(rows, key=lambda item: item["name"])


def infer_plugin_source(marketplace: str) -> str:
    mapping = {
        "claude-plugins-official": "https://github.com/anthropics/claude-plugins-official",
        "openai-curated": "OpenAI curated plugin marketplace",
        "openai-bundled": "Bundled with Codex",
        "openai-primary-runtime": "Bundled Codex primary runtime",
    }
    return mapping.get(marketplace, marketplace)


def collect_claude_plugins() -> list[dict[str, str]]:
    installed_path = HOME / ".claude" / "plugins" / "installed_plugins.json"
    marketplaces_path = HOME / ".claude" / "plugins" / "known_marketplaces.json"
    if not installed_path.exists():
        return []
    installed = json.loads(installed_path.read_text())
    known = {}
    if marketplaces_path.exists():
        known = json.loads(marketplaces_path.read_text())
    rows = []
    for key, installs in sorted(installed.get("plugins", {}).items()):
        name, _, marketplace = key.partition("@")
        install = installs[0] if installs else {}
        source = known.get(marketplace, {}).get("source", {})
        repo = source.get("repo") if isinstance(source, dict) else None
        source_label = f"https://github.com/{repo}" if repo else marketplace
        rows.append(
            {
                "plugin": sanitize_text(name),
                "marketplace": sanitize_text(marketplace),
                "version": sanitize_text(str(install.get("version", "unknown"))),
                "status": "enabled",
                "source": source_label,
                "category": infer_category(name),
            }
        )
    return rows


def write_json(path: Path, data: object) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def write_markdown_table(path: Path, rows: list[dict[str, str]], columns: list[str], title: str, intro: str) -> None:
    lines = [f"# {title}", "", intro, ""]
    lines.append("| " + " | ".join(columns) + " |")
    lines.append("| " + " | ".join(["---"] * len(columns)) + " |")
    for row in rows:
        values = [
            sanitize_text(str(row.get(column, "")))
            .replace("\n", " ")
            .replace("|", "\\|")
            for column in columns
        ]
        lines.append("| " + " | ".join(values) + " |")
    path.write_text("\n".join(lines) + "\n")


def write_summary(skills: list[dict[str, str]], codex_plugins: list[dict[str, str]], claude_plugins: list[dict[str, str]]) -> None:
    by_source = Counter(skill["source"] for skill in skills)
    by_category = Counter(skill["category"] for skill in skills)
    summary = {
        "generated_for": "public documentation",
        "privacy_note": "Sanitized inventory. No auth files, logs, memory databases, local config, or raw plugin cache contents are included.",
        "counts": {
            "skills_total": len(skills),
            "codex_plugins_configured": len(codex_plugins),
            "claude_plugins_registered": len(claude_plugins),
        },
        "skills_by_source": dict(sorted(by_source.items())),
        "skills_by_category": dict(sorted(by_category.items())),
    }
    write_json(DATA_DIR / "summary.json", summary)


def main() -> int:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    skills = collect_skills()
    codex_plugins = collect_codex_plugins()
    claude_plugins = collect_claude_plugins()
    codex_mcps = collect_codex_mcps()

    write_json(DATA_DIR / "skills.json", skills)
    write_json(DATA_DIR / "codex-plugins.json", codex_plugins)
    write_json(DATA_DIR / "claude-plugins.json", claude_plugins)
    write_json(DATA_DIR / "mcp-servers.json", codex_mcps)
    write_summary(skills, codex_plugins, claude_plugins)

    featured_skills = [
        skill
        for skill in skills
        if skill["source"] in {"codex-direct", "agents-direct", "claude-direct", "claude-dot-agents"}
    ]
    write_markdown_table(
        DOCS_DIR / "skills-inventory.md",
        featured_skills,
        ["name", "category", "source", "description"],
        "Skills Inventory",
        "Skills diretas aparecem por nome, categoria e origem. Descrições de skills customizadas ficam vazias por segurança.",
    )
    write_markdown_table(
        DOCS_DIR / "codex-plugins.md",
        codex_plugins,
        ["plugin", "category", "marketplace", "status", "source"],
        "Codex Plugins",
        "Plugins configurados no Codex, com marketplace, status e origem publica quando conhecida.",
    )
    write_markdown_table(
        DOCS_DIR / "claude-code-plugins.md",
        claude_plugins,
        ["plugin", "category", "marketplace", "version", "status", "source"],
        "Claude Code Plugins",
        "Plugins registrados no Claude Code, com versao e fonte publica quando conhecida.",
    )
    write_markdown_table(
        DOCS_DIR / "mcp-servers.md",
        codex_mcps,
        ["name", "category", "transport", "public_note"],
        "MCP Servers",
        "MCPs sao publicados apenas por nome e transporte aproximado. Args, env vars, URLs e auth state ficam fora.",
    )

    all_text = "\n".join(path.read_text(errors="replace") for path in DATA_DIR.glob("*.json"))
    for pattern in SENSITIVE_PATTERNS:
        if pattern.search(all_text):
            print(f"Sensitive pattern still present: {pattern.pattern}", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
