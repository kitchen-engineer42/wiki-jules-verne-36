---
round: 105
date: 2026-07-15
type_round: 76
phase: "2.1"
current_type: place
gene: EVV5
new_candidates: 0
pages: []
result: reflect
---

# GROW 2.1-B · R105 · EVV5 · place — 周期质量反思（模板稳定，无结构变动）

## 本轮公告

**R105 — Phase 2.1 — EVV5 — place — 全库 260 place 页 schema 反思 / 非建页 / since_evv5 归 0**

R104 后 since_evv5=10、since_discover=1、discover_streak_low=0、queue(place)≈32、since_corpus=41。
决策矩阵：**since_evv5=10≥10 → 优先级 1b EVV5 触发**（抢占 queue≥10 本不触发的 priority 3、及 since_corpus=41≥30 本会触发的 priority 3.5）。
自 R94 上次 EVV5（place）以来累计 11 建/discover 轮（type_round 65→76），沿「每约 11 轮一次 EVV5」节奏
（R61→R72→R83→R94→R105），本轮对 place 类型全部已建页面执行 `EVV5-type-pilot-reflect`：
扫描 schema 合规 + 质量模式，判断 `local/template/place-schema.md` 是否需调整。本轮不新建/编辑任何页面。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=10, since_discover=1<10 | 否 |
| **1b** | **EVV5（since_evv5 ≥ 10）** | **=10** | **触发** |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否（被 1b 抢占）|
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue≈32≥10, since_discover=1<10 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =41 | 否（被 1b 抢占）|
| 6 | NEW1（默认）| — | 否 |

> since_corpus=41≥30 本会在优先级 3.5 触发 corpus-discover，但 EVV5（1b）优先级最高，
> 本轮先做质量反思；corpus-discover 顺延（EVV5 不重置 since_corpus）。

## 扫描方法与结果

对 `docs/wiki/pages/**/*.md` 中 `type: place` 的 **260** 页逐页核查五维：
(1) 4×H2 结构顺序（Overview / In the Narrative / Geography & Features / Connections）；
(2) 必填 frontmatter 字段（id/type/label/book/real_or_fictional/region/description）；
(3) `real_or_fictional` 取值合法（real|fictional）；(4) 页内引注 distinctPN ≥5；(5) 散文门 ≤400。

| 维度 | 结果 | 计数 |
|------|------|------|
| H2 结构（4 节顺序）| ✅ 全通过 | 0 违规 / 260 |
| 必填字段齐备 | ✅ 全通过 | 0 缺失 / 260 |
| real_or_fictional 合法 | ✅ 全通过 | 0 非法 / 260 |
| 页内引注 distinctPN ≥5 | ⚠ 2 页 <5 | 2（均既有 Pilot 页）|
| 散文门 ≤400 | ⚠ 24 页超 400 | 24（add_page 旁路遗留，全为既有页）|

### distinctPN <5（2 页）

`snaefellsjokull`（4）、`hong-kong`（4）——均 BIRTH Pilot 期建，承 R39/R50/R61/R72/R83/R94 **PARK**
（Pilot 页 PN=4 债，非本类型扩张轮产物）。R95–R104 新建 35 页（含本对话 R100-R104 的 20 页）全 ≥5。

### 散文门 >400（24 页，全为既有页）

全库 24 place 页含超 400 字长段，max 仍为 **bay-of-talcahuano 614**——与 R94 完全一致（24 页、同 max），
系 `add_page.py` 建时不执行散文门（HK-addpage-prose-gate-bypass）所致。**24 页无一为本对话新建**：
R100-R104 新建 20 页（italy…congo）建前均逐段裁至 ≤400，本轮复扫全 over-400=0、distinctPN 均 ≥5。
债无新增，已量化回填 housekeeping。

## EVV5 结论

**模板稳定，无需更新。** place-schema 三要素（4-H2 结构、7 必填字段、real_or_fictional 二值域）
在 260 页上 100% 合规，无字段普遍缺失、无某节约束不清的结构性问题。两类瑕疵均非模板缺陷：
- distinctPN<5：2 既有 Pilot 页历史债，已 PARK；
- 散文>400：24 既有页 add_page 组件旁路遗留内容卫生债，已 DEFERRED（待 RFC 后 edit_page 统一复拆）。

按 EVV5 规则「若无结构变动 → 记录『模板稳定』，继续建页节奏」，`local/template/place-schema.md`
**不修改**，不触发 backfill，不新起 RFC（组件债依 RFC-parking 记 housekeeping，用户末期批量评审）。

> **附**：本轮 registry 复扫仅剩 Robur alias 旧账 PARK（'Robur the Conqueror' → robur-the-conqueror vs robur），
> 无其他 label 冲突。全库 1328 页，unknown 0。

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

`current_round 105→106`；`type_round 76→77`；`rounds_since_last_evv5 10→0`（EVV5，RESET）；
`rounds_since_last_discover 1→2`（EVV5 非 discover 轮，按既有约定 +1）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 41→42`；`last_updated_round→106`。

## 遗留问题

1. **place 页数保持 260**：本轮非建页，registry 全库 1328，unknown 0。
2. **下轮 R106 = NEW1（消化 R103 discover 残余候选）**：since_evv5 归 0；since_discover=2<10 且 queue≈32≥10 → priority 3 不触发；since_corpus=42≥30 名义触发 priority 3.5，但表层候选（~32）充裕、可建 backlog 未罄 → **NEW1（priority 6）默认，corpus-discover 顺延**。建议 R106 续批取 Mediterranean/Pacific/Atlantic（洋/海层，聚焦航段确指句）或 Hamburg/Petersburg/Valparaiso（城市单源）。
3. **corpus-discover 顺延临界**：since_corpus=42，已远过阈；待表层 ~32 候选消化近罄且表层复扫 0 新时，再评 corpus 深扫补单作残余候选。
4. **EVV5 节奏**：R94→R105 隔 11 轮；since_evv5 归 0，下次约 R116。
5. **EVV6 封存点预告**：Phase 2.1 关闭前（2.1-Z-0）须对每类型执行一次 EVV6 全库评审并回填均分。
6. **R77 五页补核**（承 HK-R78-tsalal-dup）：nijni-novgorod/bombay/melbourne/lima/gibraltar 待补交叉核；R104 建 argentine/congo 与 chili/angola 邻接，交叉核一并纳入。
7. **debt 照旧 PARK/记录**：HK-addpage-prose-gate-bypass（24 页）、HK-book-colon-yaml-break、featured 虚高、RFC-0003 VVV 宽度、Robur alias、两 Pilot 页 PN=4。全库建成后统一处理。
8. **England/France 国级页评估**（承 R96-R104）：城市页密集顾虑未解，R106+ 专项评估。
