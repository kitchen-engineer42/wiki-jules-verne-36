---
round: 1
date: 2026-07-13
phase: 9
gene: SCN27
type: technology
pages: [columbiad, lunar-projectile, the-terror, ruhmkorff-apparatus, diving-apparatus]
result: accept
---

# R1 — SCN27 technology r1（Phase 9-B 首轮）

## 执行摘要

Phase 9-B 类型循环第一轮，类型 `technology`（Phase 7 权重 16%，先建基础类型）。用 NEW1 建 5 个 standard 页，全部 corpus-grounded（每句有据）。选页依「语料信息最丰富」原则，覆盖凡尔纳标志性机器/发明/仪器，跨 4 部作品，兼顾大型载具与便携仪器：

- **Columbiad**（FEM，From the Earth to the Moon）— 900 英尺登月巨炮
- **The Projectile / 铝制炮弹车**（RM，Round the Moon）— 载人登月弹舱
- **The Terror / Épouvante**（MW，Master of the World）— Robur 四模式机器（陆/水/潜/空）
- **Ruhmkorff Apparatus**（JCE，Journey to the Centre of the Earth）— 便携电感应灯
- **Rouquayrol Diving Apparatus**（TTLU，Twenty Thousand Leagues）— 自持式潜水装具

Nautilus（9-A 试建页）不重复计入本批。每页均达 standard：4 节结构（Overview / Design & Operation / Role in the Story / Science & Speculation）、≥5 条 PN 引注、类型专属 frontmatter 全填、quality=standard。

引注方法：`corpus_search.py` 定位候选段落 → 读章节页原文核对 → 仅采用 grep 逐字核验过的引文（发现 sentence-index 与页面存在个别 PN 错位，如 MW-004-044 spindle 快照与页面正文不符，一律以页面正文为准）。

## 页面处理记录

| slug | type | 作品(VVV) | 引注数 | PN 来源示例 | quality | QUO7 |
|------|------|-----------|--------|-------------|---------|------|
| columbiad | technology | FEM | 11 | FEM-008-012/027, FEM-015-006/007/008/022 | standard | 无问题 |
| lunar-projectile | technology | RM | 9 | RM-001-003/007/039/065, RM-005-010, RM-009-017 | standard | 无问题 |
| the-terror | technology | MW | 10 | MW-004-044, MW-013-007/027, MW-015-026/028, MW-017-042/069 | standard | 无问题 |
| ruhmkorff-apparatus | technology | JCE | 6 | JCE-011-029, JCE-018-027/028/032, JCE-020-030 | standard | 无问题 |
| diving-apparatus | technology | TTLU | 8 | TTLU-015-073/075/077/079, TTLU-016-012/019/024 | standard | 无问题 |

## EXIT-GATE 检查

- E（渲染/格式）：QUO7 全部「无问题」；bucket 结构正常（pages/ 根无散落 .md）。
- 已知 caveat（继承 9-A 处置）：4 字符 VVV（TTLU）行内引注因共享 `pn-citation` 插件 3 字符正则暂渲染为纯文本，数据正确，待 RFC-0003（parked）上游修复；本轮 FEM/RM/MW/JCE 多为 2–3 字符 VVV，渲染不受影响，TTLU 页（diving-apparatus）引注同样为合法数据。
- 完整 E1–E5 出口门在本类型三轮结束后统一执行（见 9-B 流程）。

## 遗留问题

- 跨页 wikilink 目标（[[Gun Club]]、[[Robur]]、[[Professor Lidenbrock]]、[[Captain Nemo]]）多数尚未建页，当前为 want-link，待 character/organization 轮次补齐后由 9-C wikify 回填。
- sentence-index 与章节页存在个别 PN 错位（PN 宽度缺陷同源），已通过「页面正文逐字核验」规避；供 RFC-0002 佐证。
