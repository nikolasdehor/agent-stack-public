#!/usr/bin/env python3
"""Render a safe install/use plan from the public skill manifest."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "skill-sources.json"


def load_rows() -> list[dict[str, str]]:
    return json.loads(DATA_PATH.read_text())


def matches(row: dict[str, str], args: argparse.Namespace) -> bool:
    if args.host and row["host"] != args.host:
        return False
    if args.category and row["category"] != args.category:
        return False
    if args.method and row["install_method"] != args.method:
        return False
    if args.skill and args.skill.lower() not in row["skill"].lower():
        return False
    return True


def markdown_table(rows: list[dict[str, str]]) -> str:
    columns = ["skill", "host", "install_method", "resolution_status", "plugin", "marketplace", "source_url_or_label"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for row in rows:
        values = [row.get(column, "").replace("|", "\\|") for column in columns]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def print_summary(rows: list[dict[str, str]]) -> None:
    print("# Agent Stack Install Summary\n")
    for title, key in [
        ("By host", "host"),
        ("By install method", "install_method"),
        ("By resolution status", "resolution_status"),
        ("By category", "category"),
    ]:
        print(f"## {title}\n")
        for value, count in sorted(Counter(row[key] for row in rows).items()):
            print(f"- {value}: {count}")
        print()

    print("## Install method meaning\n")
    print("- plugin: install or enable the listed plugin from its marketplace or public source.")
    print("- bundled-runtime: update the host runtime; the skill is supplied by a bundled plugin.")
    print("- manual-review: this repo lists the skill, but does not publish its raw contents.")


def print_rows(rows: list[dict[str, str]], limit: int) -> None:
    if not rows:
        print("No matching skills found.")
        return
    shown = rows[:limit]
    print(markdown_table(shown))
    if len(rows) > limit:
        print(f"\nShowing {limit} of {len(rows)} matches. Increase --limit to see more.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", action="store_true", help="show aggregate counts and method meanings")
    parser.add_argument("--skill", help="filter by skill name substring")
    parser.add_argument("--host", choices=["codex", "claude-code", "shared-agents", "manual"])
    parser.add_argument("--category")
    parser.add_argument("--method", choices=["plugin", "bundled-runtime", "manual-review", "unknown"])
    parser.add_argument("--limit", type=int, default=80)
    args = parser.parse_args()

    rows = load_rows()
    filtered = [row for row in rows if matches(row, args)]
    if args.summary or not any([args.skill, args.host, args.category, args.method]):
        print_summary(filtered)
    else:
        print_rows(filtered, args.limit)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
