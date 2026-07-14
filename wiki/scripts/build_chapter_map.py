#!/usr/bin/env python3
"""build_chapter_map.py — 生成 local/butler/chapter-map.md（anthology 版）。

共享 `$MEMEX_ROOT/wiki/scripts/butler/build_chapter_map.py` 假设**单书**：从语料正则
抽取带阿拉伯数字捕获组的章节号生成连续 NNN。本 wiki 为 35 部凡尔纳作品合集，968 章
标题为罗马数字 / 纯文本（`CHAPTER I`、`The Blockade Runners` 等），无单一阿拉伯章号，
且 NNN 需按作品分段（VVV-NNN），共享脚本无法处理（实测 0 章）。

本地生成器改从权威源 `docs/wiki/pages.json`（type=chapter）读取，按 book_seq 排序，
输出 `PN 前缀（VVV-NNN）| 作品 | 章节标题` 表，供 butler 运行时参考。
与本 wiki 既有 anthology 本地脚本（build_chapter_pages / generate_toc / assign_pn）一致。

用法：
  python3 wiki/scripts/build_chapter_map.py            # 写入
  python3 wiki/scripts/build_chapter_map.py --dry-run  # 预览不写
"""
import argparse
import json
import os
from pathlib import Path

WIKI_ROOT = Path(os.environ.get("WIKI_ROOT", os.getcwd()))
PAGES_JSON = WIKI_ROOT / "docs/wiki/pages.json"
PAGES_DIR = WIKI_ROOT / "docs/wiki/pages"
OUT_PATH = WIKI_ROOT / "local/butler/chapter-map.md"


def _read_pn_prefix(rel_path):
    """从章节页 frontmatter 读取 pn_prefix（pages.json 未透传此字段）。"""
    fp = PAGES_DIR / rel_path
    for line in fp.read_text(encoding="utf-8").splitlines():
        if line.startswith("pn_prefix:"):
            return line.split(":", 1)[1].strip().strip('"').strip("'")
        if line.startswith("# "):
            break
    return ""


def collect():
    pages = json.loads(PAGES_JSON.read_text(encoding="utf-8"))["pages"]
    rows = []
    for pid, e in pages.items():
        if e.get("type") != "chapter":
            continue
        pn_prefix = e.get("pn_prefix") or _read_pn_prefix(e.get("path", ""))
        book = e.get("book", "")
        label = e.get("label", pid)
        seq = e.get("book_seq", e.get("chapter", 0)) or 0
        rows.append((int(seq), pn_prefix, book, label))
    rows.sort(key=lambda r: r[0])
    return rows


def render(rows):
    max_pn = max((len(r[1]) for r in rows), default=8)
    max_book = max((len(r[2]) for r in rows), default=8)
    body = []
    for _seq, pn, book, label in rows:
        body.append(f"| `{pn}`{' ' * (max_pn - len(pn))} | {book}{' ' * (max_book - len(book))} | {label} |")
    return f"""\
# PN 章节映射表（anthology）

PN 格式：`VVV-NNN-PPP`（作品码-作品内章号-段号，见 LAW.md 三）。
本表列出 `pn_prefix = VVV-NNN`（每章唯一）↔ 作品 / 章节标题。

语料来源：`corpus/raw/doc_final.md`（35 部作品 / {len(rows)} 章）

## 章节编号映射

| PN 前缀 | 作品 | 语料章节标题 |
|---------|------|-------------|
{chr(10).join(body)}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    rows = collect()
    if not rows:
        raise SystemExit("未找到 type=chapter 页面")
    text = render(rows)
    if args.dry_run:
        print(text[:1200])
        print(f"... 共 {len(rows)} 章 → {OUT_PATH}")
        return
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(text, encoding="utf-8")
    print(f"已写入 {OUT_PATH}（{len(rows)} 章节）")


if __name__ == "__main__":
    main()
