---
round: 72
date: 2026-07-15
type_round: 43
phase: "2.1"
current_type: place
gene: EVV5
new_candidates: 0
pages: []
result: reflect
---

# GROW 2.1-B · R72 · EVV5 · place — 周期质量反思（模板稳定，无结构变动）

## 本轮公告

**R72 — Phase 2.1 — EVV5 — place — 全库 165 place 页 schema 反思 / 非建页 / since_evv5 归 0**

R71 后 since_evv5=10、since_discover=3、discover_streak_low=0、queue(place)=9、since_corpus=8。
决策矩阵：**since_evv5=10≥10 → 优先级 1b EVV5 触发**（抢占 queue<10 本会触发的优先级 3 SCN28）。
自 place 类型开扩以来累计 10 建页轮（type_round 33→43 区间），按「每 10 轮一次 EVV5」节奏，
本轮对 place 类型全部已建页面执行 `EVV5-type-pilot-reflect`：扫描 schema 合规 + 质量模式，
判断 `local/template/place-schema.md` 是否需调整。本轮不新建/编辑任何页面。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=10, since_discover=3<10 | 否 |
| **1b** | **EVV5（since_evv5 ≥ 10）** | **=10** | **触发** |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否（被 1b 抢占）|
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=9<10 | 否（被 1b 抢占）|
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =8 | 否 |
| 6 | NEW1（默认）| — | 否 |

> queue=9<10 本会在优先级 3 触发 SCN28，但 EVV5（1b）优先级更高，本轮先做质量反思；
> discover 顺延至 R73（EVV5 不重置 since_discover，R73 时 queue 仍 9<10 → SCN28）。

## 扫描方法与结果

对 `docs/wiki/pages/**/*.md` 中 `type: place` 的 **165** 页逐页核查五维：
(1) 4×H2 结构顺序（Overview / In the Narrative / Geography & Features / Connections）；
(2) 必填 frontmatter 字段（id/type/label/book/real_or_fictional/region/description）；
(3) `real_or_fictional` 取值合法（real|fictional）；(4) 页内引注 distinctPN ≥5；(5) 散文门 ≤400。

| 维度 | 结果 | 计数 |
|------|------|------|
| H2 结构（4 节顺序）| ✅ 全通过 | 0 违规 / 165 |
| 必填字段齐备 | ✅ 全通过 | 0 缺失 / 165 |
| real_or_fictional 合法 | ✅ 全通过 | 0 非法 / 165 |
| 页内引注 distinctPN ≥5 | ⚠ 2 页 <5 | 2（均既有 Pilot 页）|
| 散文门 ≤400 | ⚠ 24 页超 400 | 24（add_page 旁路遗留）|

### distinctPN <5（2 页）

`snaefellsjokull`（4）、`hong-kong`（4）——均 BIRTH Pilot 期建，承 R39/R50/R61 **PARK**
（Pilot 页 PN=4 债，非本类型扩张轮产物）。R64–R71 新建 40 页全 ≥5。

### 散文门 >400（24 页）

全库 24 place 页含超 400 字长段（最大 cape-of-good-hope 498），系 `add_page.py` 建时不执行散文门
（HK-addpage-prose-gate-bypass 已录）所致。多为 R60 前既有页；R64–R71 本 place 轮新建 40 页建前
均逐段裁至 ≤400，无一违规。已量化回填至 housekeeping（HK-addpage-prose-gate-bypass §EVV5 全库量化）。

## EVV5 结论

**模板稳定，无需更新。** place-schema 三要素（4-H2 结构、7 必填字段、real_or_fictional 二值域）
在 165 页上 100% 合规，无字段普遍缺失、无某节约束不清的结构性问题。两类瑕疵均非模板缺陷：
- distinctPN<5：2 既有 Pilot 页历史债，已 PARK；
- 散文>400：add_page 组件旁路遗留内容卫生债，已 DEFERRED（待 RFC 后 edit_page 统一复拆）。

按 EVV5 规则「若无结构变动 → 记录『模板稳定』，继续建页节奏」，`local/template/place-schema.md`
**不修改**，不触发 backfill，不新起 RFC（组件债依 RFC-parking 记 housekeeping，用户末期批量评审）。

## EXIT-GATE 检查（EVV5 轮仅 G4 + 不变式）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本反思日志；housekeeping 量化回填；grow_state EVV5 six-step；无页面文件变更 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

> G1/G2/G3 不适用（本轮不新增/编辑页面）。

## state 更新（EVV5 six-step）

`current_round 72→73`；`type_round 43→44`；`rounds_since_last_evv5 10→0`（EVV5，RESET）；
`rounds_since_last_discover 3→4`（EVV5 非 discover 轮，按既有约定 +1）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 8→9`；`last_updated_round→73`。

## 遗留问题

1. **place 页数保持 165**：本轮非建页，registry 全库 1233，unknown 0。
2. **下轮 R73 = SCN28（优先级 3）**：since_evv5 归 0、queue=9<10、since_discover=4<10、since_corpus=9<30
   → 优先级 3 SCN28 触发（表层复扫补种 place 候选）。R68 补种 15 已全消费，需新一轮 discover 补给。
   注：单作强候选渐稀，R73 复扫或转向跨源候选精核 + 剩余城市（Semipolatinsk/Tobolsk/Nijni 等 MS 群、
   Belem/Tabatinga EHLA、Yokohama AWED 等）与既有 6 跨源候选。
3. **EVV6 封存点预告**：Phase 2.1 关闭前（2.1-Z-0）须对每类型执行一次 EVV6 全库评审并回填均分。
4. **两 Pilot 页 PN=4**、**24 页散文>400**：均已录 housekeeping/PARK，全库建成后统一处理。
5. **debt 照旧 PARK/记录**：HK-book-colon-yaml-break、HK-surface-discover-pattern-undercount、
   featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报。
