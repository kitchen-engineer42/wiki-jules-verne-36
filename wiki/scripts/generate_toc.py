#!/usr/bin/env python3
"""generate_toc.py — 生成合集目录页（anthology 版）。

共享 generate_toc.py 面向单书（单一 pn-prefix + parts-config）。本 wiki 为
35 部作品合集，故自建：按 book_seq（全合集物理顺序）分组，每部作品一个
二级标题，其下列出各章 wikilink。type=overview，id=TOC。
"""
import json
import os
import re
import sys
from pathlib import Path

MEMEX = os.environ.get("MEMEX_ROOT", str(Path.home() / "memex"))
sys.path.insert(0, os.path.join(MEMEX, "wiki/scripts"))
from page_bucket import page_bucket  # noqa: E402

WIKI_ROOT = Path(os.environ.get("WIKI_ROOT", os.getcwd()))
PAGES_JSON = WIKI_ROOT / "docs/wiki/pages.json"
PAGES_DIR = WIKI_ROOT / "docs/wiki/pages"


def short_label(label, book):
    """'Work — CHAPTER 1' → 'CHAPTER 1'；短篇单页 label==book → book。"""
    if label.startswith(book + " — "):
        return label[len(book) + 3:].strip()
    return label


def main():
    pages = json.loads(PAGES_JSON.read_text(encoding="utf-8"))["pages"]
    chapters = [dict(id=pid, **e) for pid, e in pages.items()
                if e.get("type") == "chapter"]
    chapters.sort(key=lambda e: e.get("book_seq", 0))

    out = ["---", "id: TOC", "type: overview", "label: Table of Contents",
           "description: 'Complete contents of the Collected Works of Jules Verne.'",
           "---", "", "# Table of Contents", ""]

    cur_book = None
    cur_part = None
    work_no = 0
    for e in chapters:
        book = e.get("book", "")
        if book != cur_book:
            work_no += 1
            cur_book = book
            cur_part = None
            out.append(f"## {work_no}. {book}")
            out.append("")
        part = e.get("part")
        if part and part != cur_part:
            cur_part = part
            out.append(f"**{part.title()}**")
            out.append("")
        disp = short_label(e["label"], book)
        out.append(f"- [[{e['id']}|{disp}]]")
    out.append("")

    text = "\n".join(out)
    slug = "TOC"
    dest = PAGES_DIR / page_bucket(slug) / f"{slug}.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")
    print(f"✓ 写入 TOC：{work_no} 部作品，{len(chapters)} 章链接 → {dest}")


if __name__ == "__main__":
    main()
