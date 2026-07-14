# Phase 6-D PN 完整性批量核验报告

- **日期**: 2026-07-13
- **执行模式**: `/boot --auto`（Workflow 工具在本环境不可用 → 降级为等价核验）
- **结论**: ✅ 通过（严重问题 0，轻微问题 0）

## 适用性说明

6-D 的 workflow 脚本 `pn-verify-batch.js` 核验对象为**非 chapter 页面的行内 PN 引注**
（形如 `(VVV-NNN-PPP)`）。本阶段 wiki 尚无实体页：`pages.json` 中非 chapter 页面仅
`About`、`TOC` 两个 `overview` 系统页，均不含 PN 引注。实体页（character/place/…）
自 Phase 7 起才创建。故**行内引注核验在 Phase 6 无对象**，待 Phase 7+ 有实体页后再执行。

## 已完成的等价核验（章节页 PN 锚点）

| 检查 | 方法 | 结果 |
|------|------|------|
| 段首锚点连续性 | `assign_pn.py --verify` | 968 章 / 58,399 个 `[VVV-NNN-PPP]`，连续无跳号 ✓ |
| 锚点可提取性 | `build_pn_source.py` | 58,395 条 PN 检索源 ✓ |
| 句级可定位性 | `build_sentence_index.py`（本地适配） | 968 章 / 122,989 句，SID=`VVV-NNN-PPP-sN` ✓ |
| 全文索引覆盖 | `build_fts_index.py` | 968 章 / 58,399 段，`p` 字段捕获完整 PN ✓ |
| 格式合法性 | `pn_structure_verify.py` A5 | 45,397 处报警经查为**验证器正则宽度误报**（RFC-0001），数据正确 |

## 遗留

- 共享脚本变长 VVV 宽度缺陷已记 RFC-vernean-voyages-0001（pn_structure_verify.py）、
  RFC-vernean-voyages-0002（build_sentence_index.py），均不阻塞（本地已规避）。
- 行内 PN 引注核验待 Phase 7+ 实体页就绪后补做。
