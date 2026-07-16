---
round: 94
date: 2026-07-15
type_round: 65
phase: "2.1"
current_type: place
gene: EVV5
new_candidates: 0
pages: []
result: reflect
---

# GROW 2.1-B · R94 · EVV5 · place — 周期质量反思（模板稳定，无结构变动）

## 本轮公告

**R94 — Phase 2.1 — EVV5 — place — 全库 225 place 页 schema 反思 / 非建页 / since_evv5 归 0**

R93 后 since_evv5=10、since_discover=2、discover_streak_low=0、queue(place)=2、since_corpus=30。
决策矩阵：**since_evv5=10≥10 → 优先级 1b EVV5 触发**（抢占 queue=2<10 本会触发的优先级 3 SCN28）。
自 R83 上次 EVV5（place）以来累计 11 建/discover 轮（type_round 54→65），沿「每约 11 轮一次 EVV5」节奏
（R61→R72→R83→R94），本轮对 place 类型全部已建页面执行 `EVV5-type-pilot-reflect`：
扫描 schema 合规 + 质量模式，判断 `local/template/place-schema.md` 是否需调整。本轮不新建/编辑任何页面。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=10, since_discover=2<10 | 否 |
| **1b** | **EVV5（since_evv5 ≥ 10）** | **=10** | **触发** |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否（被 1b 抢占）|
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=2<10 | 否（被 1b 抢占）|
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =30 | 否（被 1b 抢占）|
| 6 | NEW1（默认）| — | 否 |

> queue=2<10 及 since_corpus=30≥30 本会分别在优先级 3 / 3.5 触发 discover，但 EVV5（1b）优先级最高，
> 本轮先做质量反思；discover 顺延至 R95（EVV5 不重置 since_discover / since_corpus）。

## 扫描方法与结果

对 `docs/wiki/pages/**/*.md` 中 `type: place` 的 **225** 页逐页核查五维：
(1) 4×H2 结构顺序（Overview / In the Narrative / Geography & Features / Connections）；
(2) 必填 frontmatter 字段（id/type/label/book/real_or_fictional/region/description）；
(3) `real_or_fictional` 取值合法（real|fictional）；(4) 页内引注 distinctPN ≥5；(5) 散文门 ≤400。

| 维度 | 结果 | 计数 |
|------|------|------|
| H2 结构（4 节顺序）| ✅ 全通过 | 0 违规 / 225 |
| 必填字段齐备 | ✅ 全通过 | 0 缺失 / 225 |
| real_or_fictional 合法 | ✅ 全通过 | 0 非法 / 225 |
| 页内引注 distinctPN ≥5 | ⚠ 2 页 <5 | 2（均既有 Pilot 页）|
| 散文门 ≤400 | ⚠ 24 页超 400 | 24（add_page 旁路遗留，全为既有页）|

### distinctPN <5（2 页）

`snaefellsjokull`（4）、`hong-kong`（4）——均 BIRTH Pilot 期建，承 R39/R50/R61/R72/R83 **PARK**
（Pilot 页 PN=4 债，非本类型扩张轮产物）。R64–R93 新建 78 页（含本对话区域/洲级 6 页）全 ≥5。

### 散文门 >400（24 页，全为既有页）

全库 24 place 页含超 400 字长段，max 仍为 **bay-of-talcahuano 614**、rocky-mountains 596、
strait-of-gibraltar 568、liedenbrock-sea 541、cape-of-good-hope 498……与 R83 完全一致（24 页、同 max），
系 `add_page.py` 建时不执行散文门（HK-addpage-prose-gate-bypass）所致。**24 页无一为本对话新建**：
R76 起新页（含 R92 的 5 页、R93 的 africa）建前均逐段裁至 ≤400，本轮复扫 6 新页 over-400=0、distinctPN 均 ≥8。
债无新增，已量化回填 housekeeping。

## EVV5 结论

**模板稳定，无需更新。** place-schema 三要素（4-H2 结构、7 必填字段、real_or_fictional 二值域）
在 225 页上 100% 合规，无字段普遍缺失、无某节约束不清的结构性问题。两类瑕疵均非模板缺陷：
- distinctPN<5：2 既有 Pilot 页历史债，已 PARK；
- 散文>400：24 既有页 add_page 组件旁路遗留内容卫生债，已 DEFERRED（待 RFC 后 edit_page 统一复拆）。

按 EVV5 规则「若无结构变动 → 记录『模板稳定』，继续建页节奏」，`local/template/place-schema.md`
**不修改**，不触发 backfill，不新起 RFC（组件债依 RFC-parking 记 housekeeping，用户末期批量评审）。

> **附**：本轮 registry 复扫仅剩 Robur alias 旧账 PARK（'Robur the Conqueror' → robur-the-conqueror vs robur），
> 无其他 label 冲突。全库 1293 页，unknown 0。

## EXIT-GATE 检查（EVV5 轮仅 G4 + 不变式）

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本反思日志；grow_state EVV5 six-step；无页面文件变更 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

> G1/G2/G3 不适用（本轮不新增/编辑页面）。

## state 更新（EVV5 six-step）

`current_round 94→95`；`type_round 65→66`；`rounds_since_last_evv5 10→0`（EVV5，RESET）；
`rounds_since_last_discover 2→3`（EVV5 非 discover 轮，按既有约定 +1）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 30→31`；`last_updated_round→95`。

## 遗留问题

1. **place 页数保持 225**：本轮非建页，registry 全库 1293，unknown 0。
2. **下轮 R95 = discover（优先级 3 或 3.5）**：since_evv5 归 0、queue=2<10（priority 3）且 since_corpus=31≥30
   （priority 3.5）。矩阵首匹配为优先级 3 **SCN28 表层复扫**；但 R91 demonym-stoplist 深扫已 surface 罄
   区域/国家/洲级大候选（6 个已全数消化），表层可挖空间近尽。若 R95 表层复扫 new_candidates<3 →
   discover_streak_low 0→1，place CLOSE 进入倒计时（阈值 3）。**建议 R95 优先跑 corpus-discover（3.5，深扫）**
   —— since_corpus=31 已过阈，深扫较表层更可能补出残余单作候选；若深扫亦 <3 则 corpus_streak_low +1。
3. **place 广度见底**：R93 末可建候选=0（queue 剩 Long Island/Bay of Bengal 均 real distinctPN=4<门 hold）。
   若 R95–R97 三轮 discover 均薄收，streak→3 触发 place CLOSE，转 type_queue 下一型 **event**。
4. **EVV5 节奏**：R83→R94 隔 11 轮；since_evv5 归 0，下次约 R105。
5. **EVV6 封存点预告**：Phase 2.1 关闭前（2.1-Z-0）须对每类型执行一次 EVV6 全库评审并回填均分。
6. **R77 五页补核**（承 HK-R78-tsalal-dup）：nijni-novgorod/bombay/melbourne/lima/gibraltar 待补交叉核。
7. **debt 照旧 PARK/记录**：HK-addpage-prose-gate-bypass、HK-book-colon-yaml-break、
   HK-surface-discover-pattern-undercount、featured 虚高、RFC-0003 VVV 宽度、Robur alias、
   两 Pilot 页 PN=4、24 既有页散文>400。全库建成后统一处理。
