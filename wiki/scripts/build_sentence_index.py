#!/usr/bin/env python3
"""build_sentence_index.py — 本地适配版（anthology 三段 volume PN，变长 VVV）。

共享 `$MEMEX_ROOT/wiki/scripts/build_sentence_index.py` 的 `_PN_RE` 将 PN 首段写死为
`[A-Za-z0-9]{3}`（严格 3 字符）。本 wiki 为 35 部凡尔纳作品合集，VVV 长度 1–4 字符
（`AM`/`MI` 2 字符、`TTLU`/`DSCF` 4 字符，见 LAW.md 三 / pn_patterns.py `VV`），
其段落锚点 `[VVV-NNN-PPP]` 无法被严格 3 字符正则匹配，句子库会**静默丢失**
所有非 3 字符 VVV 作品（实测 968 章仅 ~26k 句，且多章 0 条）。
根因与 pn_structure_verify.py 的 A5 缺陷同源，详见
`ref/rfc/rfc-vernean-voyages-0002-sentence-index-vol-width.md`。

本地包装：导入共享模块，仅将 PN 首段放宽为 `[A-Za-z0-9]{1,4}`（向后兼容两段式纯数字
NNN，且与三段式 VVV=1–4 一致），其余分句/清理/输出逻辑全部复用共享实现，再委托
其 `main()`。不复制共享算法，避免与上游漂移。
"""
import os
import re
import sys
from pathlib import Path

MEMEX = os.environ.get("MEMEX_ROOT", str(Path.home() / "memex"))
sys.path.insert(0, os.path.join(MEMEX, "wiki/scripts"))
import build_sentence_index as base  # noqa: E402

# 放宽 PN 首段：3 段 volume 允许 VVV=1–4 字符（贪婪，遇 '-' 自然截断）
_PN_RE = r"[A-Za-z0-9]{1,4}-\d{3,4}(?:-\d{3,4})?"
base.PARA_RE = re.compile(rf"^\[({_PN_RE})\](.*)", re.DOTALL)
base.BLOCK_OPEN_RE = re.compile(rf"^:::\s+(image|table)\s+pn=({_PN_RE})")

if __name__ == "__main__":
    base.main()
