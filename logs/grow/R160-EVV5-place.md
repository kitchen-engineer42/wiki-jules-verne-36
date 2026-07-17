---
round: 160
date: 2026-07-16
type_round: 131
phase: "2.1"
current_type: place
gene: EVV5
pages: []
result: reflect
---

# GROW 2.1-B · R160 · EVV5 · place — 周期 schema 反思（place 全类型扫描，模板稳定）

## 本轮公告

**R160 — Phase 2.1 — EVV5 — place — schema 反思 / 非建页 / since_evv5 归 0**

自 R150（上次 EVV5 前）起累计 10 建/discover 轮（since_evv5 达 10≥evv5_interval），
决策矩阵 §3(1b) 首匹配 **EVV5**（since_evv5=10≥10；since_discover=4<10 故非 EVV5+SCN28 合并轮）。
本轮对当前扩张类型 place 全库 370 页扫描，反思 `place-schema.md` 是否需调整。**不建页**。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| **1a** | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| since_evv5=10、since_discover=4<10 | 否 |
| **1b** | EVV5（since_evv5≥10）| =10 | **触发** |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue_size<10 或 since_discover≥10）| — | 否（被 EVV5 优先抢占）|
| 7 | NEW1（默认）| — | 否 |

## 扫描方法与结果

对 `docs/wiki/pages.json` 全部 `type==place`（370 页）扫描通用字段完整性、quality 分布、
schema 四 H2 结构一致性，并抽样近建 5 页（Formentera/Ceuta/Samarkand/Callao/Maryland）核对模板遵从。

| 检查项 | 结果 | 判定 |
|--------|------|------|
| place 页总数 | 370 | 与 registry 一致 |
| 通用字段 label/description/book 缺失 | 0 | ✔ 无缺失 |
| region/real_or_fictional | pages.json 不投影该二字段（仅存于页 frontmatter）| ✘ 非缺陷（registry 投影设计，非页面问题）|
| quality=featured | 355 | add_page.py 自动回填 |
| quality=none | 15 | **既有页**（add_page 自动回填前建）；属既有 featured-regrade DEFERRED 债，非本轮 EVV5 结构问题 |
| schema 四 H2（Overview/In the Narrative/Geography & Features/Connections）| 抽样 5 页全符 | ✔ 结构稳定 |
| Connections 散文（无 [[wikilink]]）| 抽样全符 | ✔ backlinks 不变 |

**quality=none 15 页清单**（既有，非本批）：aberfoyle, astrakhan, bolivia, cape-tchelynskin,
connecticut, dublin, easter-island, guinea, hudsons-bay, kentucky, lake-tanganyika, massachusetts,
niagara-falls, pennsylvania, victoria-island。均为 add_page 自动回填 quality 前建的存量页；
纳入既有 featured-regrade DEFERRED 债（HK-compute-quality-fullrun-regrade），本轮不动。

## EVV5 结论

**模板稳定，无需更新。** place-schema.md 四 H2 结构在近 10 轮建页（R150–R159：Nantucket/Tunis/
Tripoli/Maryland/Formentera/Ceuta/Samarkand/Callao 共 8 建 + R150/R155 两 SCN28）中全程遵从，
无字段约束不清、无普遍缺失、无结构性歧义。**不修改 `local/template/place-schema.md`**（该文件属既有排除项，
本轮亦无结构变动理由触及）、**不 backfill 存量页**、**不新起 RFC**。

> **观察（非行动项）**：pages.json 不投影 region/real_or_fictional，故全库统计脚本无法从 registry 核对该二字段——
> 需读页 frontmatter 方可校验。此为 registry 投影设计，非 place-schema 缺陷；记录备 Phase 2.1-Z EVV6 参考。

## EXIT-GATE 检查（EVV5 轮仅 G4 + 不变式）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本 reflect 日志；grow_state EVV5 six-step（since_evv5 RESET 0）；无页面文件变更 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

> G1/G2/G3/G5 不适用（本轮不新增/编辑页面）。

## state 更新（EVV5 six-step）

`current_round 160→161`；`type_round 131→132`；`rounds_since_last_evv5 10→0`（**EVV5 RESET**）；
`rounds_since_last_discover 4→5`（EVV5 非 discover 轮，+1）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 96→97`；`last_updated_round→161`。

## 遗留问题

1. **place 页数保持 370**：本轮非建页，registry 全库 1438，unknown 0。
2. **下轮 R161 = SCN28**：EVV5 已 reset since_evv5=0；**R155 补种批全消、净 buildable 罄** → §3(3) 实务 SCN28 深层补种（宽扫南美/东欧/近东/远东中层 toponym，未测区尚多）。依 memory feedback「Exhaustively re-scan before claiming saturation」。
3. **R155 补种建序完成回顾**：Formentera→Ceuta→Samarkand→Callao 4/4 全消，均 ≥5 solid distinctPN，覆盖新源（ASC/PL/SC）与新区（Balearic/中亚/秘鲁）。
4. **featured-regrade DEFERRED**：15 place 页 quality=none（存量），纳入既有全库 regrade 债；Phase 2.1-Z EVV6 前不动。
5. **散文门债**：37 页 >400（既有 DEFERRED）。
6. **EVV5 节奏**：本轮 reset，下次约 R171（since_evv5 再达 10）。
7. **corpus-discover 顺延临界**：since_corpus=96（HK-corpus-discover-not-in-statemachine PARK）。
8. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分；本轮观察（region/rof 不投影）记录备 EVV6 参考。
9. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
10. **洲级 America/Europe/Asia 续 HOLD**。
