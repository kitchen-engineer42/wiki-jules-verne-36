# RFC-vernean-voyages-0001: pn_structure_verify.py 的 A5 检查对变长 VVV（volume 方案）误报

- **Status**: proposed
- **Date**: 2026-07-13
- **Issue**:
- **Source wiki**: vernean-voyages
- **Target**: `wiki/scripts/pn_structure_verify.py`

---

## Problem

本 wiki 为 35 部凡尔纳作品合集，采用三段 volume 方案 PN：`VVV-NNN-PPP`（LAW.md 三）。
VVV 为作品码，长度 1–4 字符（如 `TTLU`、`MI`、`AM`、`JCE`），与 `LAW.spec.md §三`
及 `pn_patterns.py` 中 `VV = [A-Za-z0-9]{1,4}` 的定义一致。

全量赋号后（968 章 / 58,399 个 `[VVV-NNN-PPP]` 锚点），`pn_structure_verify.py --scheme volume`
报告 A5「段首遗漏 PN」45,397 处。但被点名的行**明明已带 PN 锚点**，例如：

```
AM-ch01.md:14 [A5] 段首遗漏 PN: [AM-001-001]No doubt the following narrative will
```

同一批页面经 `build_pn_source.py`（PRE20）可正确提取 58,395 条 PN，D 类（编号连续性）
亦报「无问题」。故数据本身正确，A5 为误报。

## Root cause

`pn_structure_verify.py` 顶部将第一段匹配片段写死为**严格三字符**：

```python
# pn_structure_verify.py:24-25
_FIRST = VOL           # VOL = r'[A-Za-z0-9]{3}'，仅匹配恰好 3 字符
_RE_PN_ANCHOR = re.compile(r'^\[(' + _FIRST + r')-(' + PP + r')(?:-(' + PP + r'))?\]\s*(.*)')
```

而 `pn_patterns.py` 已为 volume 方案提供**宽度自适应**的复合片段 `FIRST`
（3 段时用 `VV`=1–4 字符，2 段时退回 `VOL`=3 字符），并据此导出规范锚点
正则 `PN_ANCHOR_RE`。验证器却绕过 `PN_ANCHOR_RE`/`FIRST`，自建 `_FIRST = VOL`，
导致所有 VVV≠3 字符的锚点（本 wiki 的 `AM`/`MI`/`TTLU` 等，占多数作品）无法匹配，
第二遍扫描将其全部误判为「段首遗漏 PN」。

影响范围：任何 volume 方案且 VVV 非恰好 3 字符的 wiki——包括 `LAW.spec.md §三`
自身示例 `20KL`、`80DA`（4 字符）、`MYST`（4 字符）。

## Proposed change

`pn_structure_verify.py` 复用 `pn_patterns.py` 的规范定义，不再自建严格片段：

```python
# 方案 A：直接改用复合 FIRST
from pn_patterns import FIRST, PP
_FIRST = FIRST         # 宽度自适应：3 段允许 1–4 字符，2 段仍严格 3 字符
```

或方案 B：直接引用 `pn_patterns.PN_ANCHOR_RE` 作为唯一锚点判定源，删除本地
`_RE_PN_ANCHOR`，使验证器与引擎（`RE_PN`）、`build_pn_source.py` 的 PN 识别口径统一。

在修复合入前，本 wiki 将 FIX24 的 A5 项**标注为不阻塞**：数据经 `build_pn_source.py`
与自建 `assign_pn.py --verify` 双重确认连续、完整，A5 纯属验证器正则宽度缺陷。
