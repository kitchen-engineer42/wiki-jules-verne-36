# RFC-vernean-voyages-0002: build_sentence_index.py 的 PN 正则对变长 VVV（volume 方案）静默丢句

- **Status**: proposed
- **Date**: 2026-07-13
- **Issue**:
- **Source wiki**: vernean-voyages
- **Target**: `$MEMEX_ROOT/wiki/scripts/build_sentence_index.py`
- **Related**: RFC-vernean-voyages-0001（pn_structure_verify.py 同源宽度缺陷）

---

## Problem

本 wiki 为 35 部凡尔纳作品合集，采用三段 volume 方案 PN：`VVV-NNN-PPP`（LAW.md 三）。
VVV 为作品码，长度 1–4 字符（如 `TTLU`、`MI`、`AM`、`JCE`），与 `LAW.spec.md §三`
及 `pn_patterns.py` 中 `VV = [A-Za-z0-9]{1,4}` 的定义一致。

用共享 `build_sentence_index.py --lang en` 对 968 章全量构建句子库时，仅得
**25,992** 个句子单元，且大量章节报「0 条」（如 `AM`、`MI`、`TTLU`、`YEAR` 全部作品）。
与 A5 误报（RFC-0001）不同，这里是**数据实际丢失**：句子库缺失了绝大多数作品，
将直接损害 butler SCN5/QUO20、前端句级检索等下游功能。

## Root cause

`build_sentence_index.py` 顶部将段落锚点 PN 首段写死为**恰好 3 字符**：

```python
# build_sentence_index.py:34-36
_PN_RE = r'[A-Za-z0-9]{3}-\d{3,4}(?:-\d{3,4})?'   # 首段恰好 3 字符
PARA_RE = re.compile(rf'^\[({_PN_RE})\](.*)', re.DOTALL)
BLOCK_OPEN_RE = re.compile(rf'^:::\s+(image|table)\s+pn=({_PN_RE})')
```

于是 `[JCE-001-001]`（3 字符）可匹配，而 `[AM-001-001]`（2 字符）、
`[TTLU-001-001]`（4 字符）、`[DSCF-001-001]`（4 字符）均**匹配失败**，
`parse_chapter` 遍历时这些段落被整段跳过，句子单元数归零。

实测：36 个 VVV 码中仅 `JCE`/`FEM`/`WAI`/`AMB`/`ACH`/`ASC`/`SC2` 等恰好 3 字符者被索引，
占少数作品。根因与 RFC-0001（`pn_structure_verify.py` 的 `_FIRST = VOL`）**完全同源**：
共享脚本各自硬编码 3 字符 VVV，而未复用 `pn_patterns.py` 的宽度自适应 `FIRST`/`VV`。

影响范围：任何 volume 方案且 VVV 非恰好 3 字符的 wiki——包括 `LAW.spec.md §三`
自身示例 `20KL`、`80DA`、`MYST`（4 字符）。

## Proposed change

`build_sentence_index.py` 的 `_PN_RE` 首段改用宽度自适应定义，与 `pn_patterns.py`
的 `VV` 一致（向后兼容两段式纯数字 NNN）：

```python
# 方案 A：首段放宽为 1–4 字符
_PN_RE = r'[A-Za-z0-9]{1,4}-\d{3,4}(?:-\d{3,4})?'
```

或方案 B：直接从 `pn_patterns.py` 导入 `VV`/`PP` 组装 `_PN_RE`，与引擎
（`RE_PN`）、`assign_pn.py`、`build_pn_source.py` 的 PN 识别口径统一，
根除同类宽度缺陷（RFC-0001 与本 RFC 可一并修复）。

## Interim mitigation（本 wiki）

在共享脚本修复合入前，本 wiki 提供**本地包装** `wiki/scripts/build_sentence_index.py`：
导入共享模块后仅将 `PARA_RE`/`BLOCK_OPEN_RE` 覆盖为 `{1,4}` 首段版本，再委托其
`main()`，不复制分句/清理/输出逻辑（避免与上游漂移）。修复后句子库为
**968 章 / 122,989 句**（4 个「BOOK I/II」分卷分隔章无正文，0 句属预期）。
此举与本 wiki 既有 anthology 适配脚本（`build_chapter_pages.py`、`assign_pn.py`、
`generate_toc.py`）的本地化模式一致，且 BIRTH.spec.md §6-A 本就以本地路径
`wiki/scripts/build_sentence_index.py` 调用该脚本。
