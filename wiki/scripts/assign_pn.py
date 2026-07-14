#!/usr/bin/env python3
"""assign_pn.py — 为章节页正文段落赋 PN（三段 volume 方案 VVV-NNN-PPP）。

改编自 PRE7-chapter-pn-assign（gene），pn_format = "{pn_prefix}-{ppp:03d}"。
pn_prefix（=VVV-NNN）从各页 frontmatter 读取；正文每个自然段段首前置
`[VVV-NNN-PPP]`（WIKI_LANG=en，半角，紧靠正文无空格，见 LAW.md 三）。

幂等：若某页正文已含 `[{pn_prefix}-` 标记则跳过。
路径经 pages.json 的 path 字段定位（禁止从 id 推导）。

用法：
  python3 wiki/scripts/assign_pn.py            # 全量
  python3 wiki/scripts/assign_pn.py --only TTLU-ch01   # 单章（pilot）
  python3 wiki/scripts/assign_pn.py --verify   # 仅验证连续性，不改写
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

WIKI_ROOT = Path(os.environ.get("WIKI_ROOT", os.getcwd()))
PAGES_JSON = WIKI_ROOT / "docs/wiki/pages.json"
PAGES_DIR = WIKI_ROOT / "docs/wiki/pages"

_HEADING_RE = re.compile(r"^#{1,6} ")
_FM_RE = re.compile(r"^---\s*\n.*?\n---\s*\n", re.DOTALL)
_PN_PREFIX_FIELD_RE = re.compile(r'(?m)^pn_prefix:\s*"?([^"\n]+)"?\s*$')


def split_frontmatter(text: str):
    m = _FM_RE.match(text)
    if not m:
        return "", text
    return text[: m.end()], text[m.end():]


def assign_chapter(body: str, pn_prefix: str):
    """→ (标注后 body, 段落数)。段首前置 [pn_prefix-PPP]；特殊块整块一号。"""
    paras = body.split("\n\n")
    out = []
    ppp = 1
    for raw in paras:
        para = raw.strip()
        if not para or _HEADING_RE.match(para):
            out.append(raw)
            continue
        pn = f"{pn_prefix}-{ppp:03d}"
        if para.startswith("```"):
            out.append(raw.rstrip() + f"\n<!-- pn={pn} -->")
        elif para.startswith("::: image") or para.startswith("![" ):
            out.append(f"::: image pn={pn}\n" + para + ("\n:::" if not para.startswith(":::") else ""))
        else:
            out.append(f"[{pn}]" + raw)
        ppp += 1
    return "\n\n".join(out), ppp - 1


def has_pn(body: str, pn_prefix: str) -> bool:
    return f"[{pn_prefix}-" in body or f"pn={pn_prefix}-" in body


def verify_sequence(body: str, pn_prefix: str):
    esc = re.escape(pn_prefix)
    nums = [int(x) for x in re.findall(rf"\[{esc}-(\d{{3}})\]", body)]
    nums += [int(x) for x in re.findall(rf"pn={esc}-(\d{{3}})", body)]
    nums = sorted(set(nums))
    errs = []
    for i, n in enumerate(nums):
        if i and n != nums[i - 1] + 1:
            errs.append(f"{pn_prefix}: 跳号 {nums[i-1]:03d}→{n:03d}")
    return errs, len(nums)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="仅处理该 page id")
    ap.add_argument("--verify", action="store_true", help="仅验证连续性")
    args = ap.parse_args()

    pages = json.loads(PAGES_JSON.read_text(encoding="utf-8"))["pages"]
    chapters = [(pid, e) for pid, e in pages.items() if e.get("type") == "chapter"]
    if args.only:
        chapters = [(pid, e) for pid, e in chapters if pid == args.only]
        if not chapters:
            sys.exit(f"未找到章节 {args.only}")

    changed = skipped = total_pn = 0
    all_errs = []
    for pid, e in chapters:
        fp = PAGES_DIR / e["path"]
        text = fp.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        m = _PN_PREFIX_FIELD_RE.search(fm)
        if not m:
            all_errs.append(f"{pid}: frontmatter 缺 pn_prefix")
            continue
        pn_prefix = m.group(1).strip()

        if args.verify:
            errs, n = verify_sequence(body, pn_prefix)
            all_errs += errs
            total_pn += n
            continue

        if has_pn(body, pn_prefix):
            skipped += 1
            errs, n = verify_sequence(body, pn_prefix)
            all_errs += errs
            total_pn += n
            continue

        new_body, n = assign_chapter(body, pn_prefix)
        fp.write_text(fm + new_body, encoding="utf-8")
        changed += 1
        total_pn += n

    if args.verify:
        print(f"验证：{len(chapters)} 章，{total_pn} 个 PN")
    else:
        print(f"赋号：改写 {changed} 章，跳过 {skipped} 章（已有 PN），共 {total_pn} 个 PN")
    if all_errs:
        print(f"✗ {len(all_errs)} 个问题：")
        for e in all_errs[:20]:
            print(f"  {e}")
        sys.exit(1)
    print("✓ PN 连续性验证通过")


if __name__ == "__main__":
    main()
