---
round: 255
date: 2026-07-18
type_round: 21
phase: "2.1"
current_type: event
gene: EVV5
pages: []
result: reflect
mean_score: 81
---

# GROW 2.1-B · R255 · EVV5 · event — event 类型 schema 反思（全 31 页评审，均分 81，模板验证通过）

## 执行摘要

Phase 2.1-B event 类型**第二次 EVV5 schema 反思**（type_round 21）。R254 NEW1 后 since_evv5 累至 10，
R255-start since_evv5=10≥10 → 决策机 §3(1b) **EVV5**（since_discover=1<10 不触 §3(1a) 组合轮）。

EVV5 为**反思轮，非建页**：扫描全类型 31 event 页，比对 event-schema（四 H2 + 专属字段 book/location/pn_anchor），
识别系统性问题，评均分，据结论决定是否更新模板。**pages: []，registry 恒 1506，event 恒 31，unknown 0。**

## 全类型扫描结果（31 event 页）

**结构一致性（合格）**：
- 四 H2（Overview / What Happens / Significance / Participants & Setting）：**31/31 全含，0 缺节**。
- 专属字段 book/location/pn_anchor：**31/31 frontmatter 完整**。
- quality：31/31 featured（add_page 自动回填；featured re-grade DEFERRED，不在本轮处理）。

**PN 丰度（系统性发现）**：
- 达 ≥5 distinct solid PN（现行 G3 门）：**18/31**——R234–R242 八页 + R245–R254 八页（新建 event 全达 7–9 PN）+ 2 早期页。
- **低于 ≥5 门：13/31**（早期 butler/种子层所建，成于现行 PN 门之前，与 R244 EVV5 记录同一批 13 页，无变化）：

| slug | distinct PN | 作品 |
|------|-------------|------|
| liedenbrock-cipher | 3 | JCE |
| snaefells-descent | 3 | JCE |
| date-line-revelation | 3 | AWED |
| columbiad-launch | 4 | FEM |
| fogg-hires-passepartout | 4 | AWED |
| gun-club-moon-proposal | 4 | FEM |
| lincoln-island-landing | 4 | MI |
| lunar-orbit-miss | 4 | RM |
| nemo-death | 4 | MI |
| north-pole-volcano | 4 | ACH |
| sea-monster-hunt | 4 | TTLU |
| stromboli-eruption-return | 4 | JCE |
| tabor-island-castaway | 4 | MI |

## 反思结论

1. **模板验证通过（无结构变动）**：event-schema 四 H2 + book/location/pn_anchor 字段体系健全。
   R245–R254 新建 8 页（burning-of-chancellor 起至 wreck-of-the-dream）全部在现行模板下达 7–9 distinct PN，
   一次成型，pn_anchor 锚定 + 单事件单指核方法论稳定。**模板不需修改**——问题不在模板，而在 13 早期页成于更松 PN 门。
2. **均分 81 ≥ 75 门**（较 R244 的 78 上升 3）：结构 31/31 合格（+），PN 丰度 18/31 达门（占比由 R244 的 43% 升至 58%）。
   加权估算 ≈ (18×87 + 13×72)/31 ≈ 81。**≥75 → 模板可用，event 批量建设继续。**
3. **系统性债（DEFERRED enrichment）**：13/31（42%）早期 event 页 distinct PN <5，低于现行 G3 门。
   与 R244 记录同一批 13 页，本轮**无新增、无消解**。属 **PN 回填 enrichment 债**，非本反思轮职责（EVV5 不建页/不改页）。
   留待后续 RCH2 enrich 轮或 Phase 2.1-Z EVV6 前统一补引。与既有「featured re-grade DEFERRED」一致：不在本轮重建/重评。

## 决策矩阵（EVV5）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| since_evv5=10；since_discover=1<10 | 否 |
| **1b** | **EVV5（since_evv5≥10）** | **=10** | **触发** |
| 2 | CLOSE+SCN28（streak≥3）| =0 | — |
| 3–7 | SCN28/RCH2/NEW1 | — | — |

## 页面处理记录

本轮为 EVV5 反思，无建页、无改页。产出反思报告（本日志）。

## EXIT-GATE 检查（EVV5 轮）

- **G1–G4**：无建页/改页，N/A（反思轮）。
- **registry 一致**：total 1506 event 31 unknown 0 恒定（无写页）。✔
- **反思充分**：全 31 页结构 + PN 丰度双维扫描；模板决策有据（均分 81≥75，无结构变动）。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean（本轮不触 -schema.md，模板不改）。✔

## 六步状态机（EVV5，grow_state 存 R256 起始计数）

| 字段 | R255 起始 | R256 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 255 | 256 |
| type_round | 21 | 22 |
| rounds_since_last_evv5 | 10 | **0（EVV5 reset）** |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 191 | 192 |
| last_updated_round | 255 | 256 |

## 遗留问题

1. **event 页数 31**（反思轮无建页）。queue(event)=2（建序 17-18 待建）。registry 全库 1506，unknown 0。
2. **下轮 R256 = NEW1（event）**：EVV5 reset since_evv5=0，queue(event)=2>0 → §3(7) NEW1。
   建 queue 建序 17 **The New Aberfoyle Explosion**（UC，UC-005）。UC 2-char，无需 RFC-0003 Note。
   建时核 New Aberfoyle 煤矿 firedamp（瓦斯）爆炸单指（UC-005-011「examined the place attacked by the explosion」），与 UC-016 矿井淹没区分。
3. **event PN 回填债（R244 起记录）**：13/31 早期 event 页 distinct PN <5（见上表），与 R244 同一批，无变化。
   留待后续 RCH2 enrich 或 Phase 2.1-Z EVV6 前统一补引至 ≥5。**本轮不重建**（EVV5 反思轮职责边界 + featured re-grade DEFERRED）。
4. **event 模板验证通过**：无结构变动，pn_anchor + 单指核方法论稳定；R245–R254 八页均达 7–9 PN 佐证。
5. **散文门债**：37 页 >400（既有 DEFERRED）。
6. **corpus-discover 顺延**：since_corpus=191→192（dead 变量）。
7. **EVV6 封存点**：Phase 2.1 关闭前须对每类型执行 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）；
   event 类型 EVV6 时须一并处理本轮记录的 13 页 PN 回填债。
8. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
