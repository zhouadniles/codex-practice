#!/usr/bin/env python3
"""A minimal AI news radar inspired by Thysrael/Horizon.

Features:
- Load RSS feeds from config.json
- Deduplicate items by URL/title
- Keep top N newest items
- Render markdown daily briefing (Chinese/English headings)
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.request import urlopen
import xml.etree.ElementTree as ET


@dataclass
class Item:
    title: str
    link: str
    source: str
    published: str


def load_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def parse_rss(url: str, source: str, limit: int = 10) -> list[Item]:
    with urlopen(url, timeout=15) as resp:
        raw = resp.read()
    root = ET.fromstring(raw)
    out: list[Item] = []
    for node in root.findall(".//item")[:limit]:
        out.append(
            Item(
                title=(node.findtext("title") or "").strip(),
                link=(node.findtext("link") or "").strip(),
                source=source,
                published=(node.findtext("pubDate") or "").strip(),
            )
        )
    return out


def dedupe(items: Iterable[Item]) -> list[Item]:
    seen: set[str] = set()
    result: list[Item] = []
    for item in items:
        key = item.link or item.title
        if key and key not in seen:
            seen.add(key)
            result.append(item)
    return result


def render_markdown(items: list[Item], date: dt.date) -> str:
    lines = [
        f"# Horizon Mini 日报 / Daily Briefing ({date.isoformat()})",
        "",
        "## 今日要点 / Highlights",
    ]
    if not items:
        lines.append("- 暂无内容 / No items")
    for i, it in enumerate(items, 1):
        lines.append(f"{i}. [{it.title}]({it.link})  ")
        lines.append(f"   来源/Source: **{it.source}** · 发布时间: {it.published or 'N/A'}")
    return "\n".join(lines) + "\n"


def run(config_path: Path, output_path: Path) -> None:
    cfg = load_config(config_path)
    rss_cfg = cfg.get("rss", [])
    max_items = int(cfg.get("max_items", 20))
    collected: list[Item] = []
    for feed in rss_cfg:
        if not feed.get("enabled", True):
            continue
        collected.extend(parse_rss(feed["url"], feed.get("name", feed["url"]), feed.get("limit", 10)))

    items = dedupe(collected)[:max_items]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_markdown(items, dt.date.today()), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a minimal daily briefing from RSS.")
    parser.add_argument("--config", default="config.json", help="Path to config file")
    parser.add_argument("--output", default="docs/daily.md", help="Output markdown path")
    args = parser.parse_args()
    run(Path(args.config), Path(args.output))


if __name__ == "__main__":
    main()
