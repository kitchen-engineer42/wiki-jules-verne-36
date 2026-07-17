---
round: 149
date: 2026-07-15
type_round: 120
phase: "2.1"
current_type: place
gene: EVV5
new_candidates: 0
pages: []
result: reflect
---

# GROW 2.1-B · R149 · EVV5 · place — 周期质量反思（模板稳定；散文债持平 37，本批 9 页零自致，行为纪律已内化）

## 本轮公告

**R149 — Phase 2.1 — EVV5 — place — 全库 362 place 页 schema 反思 / 非建页 / since_evv5 归 0**

R148 后 since_evv5=10、since_discover=9、discover_streak_low=0、queue(place)≈12、since_corpus=85。
决策矩阵 §3 首匹配：**since_evv5=10≥10 → 优先级 1b EVV5 触发**。since_discover=9<10，故非 EVV5+SCN28 合并，纯 EVV5。
自 R138 上次 place EVV5 以来累计 11 轮（type_round 109→120），沿「每约 11 轮一次 EVV5」节奏
（R116→R127→R138→R149），本轮对 place 类型全部已建页面执行 `EVV5-type-pilot-reflect`。
本轮不新建/编辑任何页面，不修改模板。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| since_evv5=10, since_discover=9<10 | 否 |
| **1b** | **EVV5（since_evv5≥10）** | **=10** | **触发** |
| 2 | CLOSE+SCN28（discover_streak_low≥3）| =0 | 否（被 1b 抢占）|
| 3 | SCN28（queue<10 或 since_discover≥10）| queue≈12≥10、since_discover=9<10 | 否 |
| 7 | NEW1（默认）| — | 否 |

> EVV5（1b）§3 首匹配最高优先。EVV5 不重置 since_discover/since_corpus，
> discover 分支顺延至 R150（届时 since_discover→10≥10 → §3 优先级 3 触发 SCN28）。

## 扫描方法与结果

对 `docs/wiki/pages/**/*.md` 中 `type: place` 的 **362** 页逐页核查五维：
(1) 4×H2 结构顺序（Overview / In the Narrative / Geography & Features / Connections）；
(2) 必填 frontmatter 字段（id/type/label/book/real_or_fictional/region/description）；
(3) `real_or_fictional` 取值合法（real|fictional）；(4) 页内引注 distinctPN（全 PN VVV-NNN-PPP）≥5；
(5) 散文段 ≤400 字。

| 维度 | 结果 | 计数 |
|------|------|------|
| H2 结构（4 节顺序）| ✅ 全通过 | 0 违规 / 362 |
| 必填字段齐备 | ✅ 全通过 | 0 缺失 / 362 |
| real_or_fictional 合法 | ✅ 全通过 | 0 非法 / 362 |
| 页内引注 distinctPN ≥5 | ⚠ 2 页 <5 | 2（均既有 Pilot 页，无变化）|
| 散文门 ≤400 | ⚠ 37 页超 400 | 37（较 R138 持平，本批 9 页零自致）|

### 本批次（R140–R148 九页）引用合法性专核

对本对话 NEW1 九页 connecticut/sacramento/pennsylvania/kentucky/massachusetts/soudan/guinea/illinois/ohio
逐页 pn_validator --mode strict 复核，**全部通过**（每 PN 回 sentence_index 命中真实 sid 段号）。9 页均
4-H2 结构、7/7 字段齐、rof 合法、distinctPN≥5、散文 max ≤400、无缺链。消歧裁定均在建轮日志留痕。

| slug | distinctPN | PN strict | H2 顺序 | 必填字段 | 散文 max | 消歧要点 |
|------|-----------|----------|---------|---------|---------|---------|
| connecticut | 7 | ✓ | ✓ | 7/7 | 374 | AM Jeorling 母州；剔州列举 |
| sacramento | 6 | ✓ | ✓ | 7/7 | 320 | 剔 EHLA Amazon pampas 异指 + SF 街 |
| pennsylvania | 8 | ✓ | ✓ | 7/7 | 358 | RC Weldon Institute/Philadelphia |
| kentucky | 6 | ✓ | ✓ | 7/7 | 366 | Mammoth Cave；剔 Kentucky oxen 牛种 |
| massachusetts | 7 | ✓ | ✓ | 7/7 | 333 | Cyrus Smith 母州/Cambridge 天文台 |
| soudan | 9 | ✓ | ✓ | 7/7 | 341 | FWB Victoria 越边界；剔 demonym |
| guinea | 6 | ✓ | ✓ | 7/7 | 354 | Gulf of Guinea；剔 New Guinea/动植物 |
| illinois | 7 | ✓ | ✓ | 7/7 | 319 | AM Dirk Peters@Vandalia；剔 Chicago 列举 |
| ohio | 6 | ✓ | ✓ | 7/7 | 343 | MW Terror 追捕 Toledo；剔州列举/Ohio River |

九页 PN 零缺陷，无系统性错误（无 ≥3 页共性失分），无需向模板注入 ⚠️ 提示块。

### distinctPN <5（2 页，无变化）

`snaefellsjokull`（4）、`hong-kong`（4）——均 BIRTH Pilot 期建，承 R39–R138 **PARK**
（Pilot 页 PN=4 债，非本类型扩张轮产物）。本对话新建 9 页全 ≥5（min soudan/pennsylvania... 实 min=6）。

### 散文门 >400（37 页，较 R138 持平）——**本批 9 页零自致，行为纪律已内化**

全库 37 place 页含超 400 字长段，与 R138 名单**完全一致**（32 既有 + R131–R136 五页）。
**本对话 R140–R148 九页净增 0**：每页首版或经就地复拆后 max ∈[319,374]，全 ≤400。

**行为面判定（对照 R138 自陈）**：R138 曾诚实自陈 R131–R136 五页行为纪律回退（自撰 Connections 段偏长 +
内嵌长引文未拆）。本对话**已兑现 R138「R139 起续守」承诺**——九页建轮中，connecticut(R140 首版 4 段超,
就地复拆 374)、kentucky(R143 FF 段 456→复拆 366)、guinea(R146 FWB 段 515→复拆 354) 三页首版超门即
edit_page 就地复拆；其余六页首版即守门。**散文债自 R138 起停止增长**，纪律回退已纠正。

## EVV5 结论

**模板稳定，无需更新。** place-schema 三要素（4-H2 结构、7 必填字段、real_or_fictional 二值域）
在 362 页上 100% 合规，无字段普遍缺失、无某节约束不清的结构性问题。两类瑕疵均非模板缺陷：
- distinctPN<5：2 既有 Pilot 页历史债，PARK；
- 散文>400：37 页（与 R138 持平），本批零增量，**行为面纪律已内化**，既有债 DEFERRED（RFC 后 edit_page 复拆）。

按 EVV5 规则「若无结构变动 → 记录『模板稳定』，继续建页节奏」，`local/template/place-schema.md`
**不修改**（且该文件为 working-tree 既有 dirty 变更，属排除项，本轮不触碰），不触发 backfill，
不新起 RFC（组件债依 RFC-parking 记 housekeeping，用户末期批量评审）。

> **附**：registry 复扫仅剩 Robur alias 旧账 PARK（'Robur the Conqueror' → robur-the-conqueror vs robur），
> 无其他 label 冲突。全库 1430 页，unknown 0。

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

`current_round 149→150`；`type_round 120→121`；`rounds_since_last_evv5 10→0`（EVV5 RESET）；
`rounds_since_last_discover 9→10`（EVV5 非 discover 轮，+1）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 85→86`；`last_updated_round→150`。

## 遗留问题

1. **place 页数保持 362**：本轮非建页，registry 全库 1430，unknown 0。
2. **下轮 R150 = SCN28（表层 discover）**：since_evv5 归 0；since_discover→10≥10 → §3 优先级 3 触发 SCN28 补种。
   净 buildable 持续收窄（R145 起既有 queue 优质项渐罄，多项试筛 <gate DEFER：Missouri 州主体不可建、
   Virginia 净4、Louisiana 净3、Abyssinia 净3）。R150 SCN28 应宽扫补新候选并复议 held/hold 项，
   或对 Colorado（疑河）、Michigan（vs lake-michigan）河湖消歧裁定。
3. **corpus-discover 顺延临界**：since_corpus=85，已远过阈 30；待表层复扫近罄时转 corpus 深扫（HK-corpus-discover-not-in-statemachine PARK）。
4. **EVV5 节奏**：R138→R149 隔 11 轮；since_evv5 归 0，下次约 R160。
5. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
6. **散文门债量化更新**：37 页 >400（与 R138 持平，本批 9 页零自致）；行为纪律已内化，既有债 DEFERRED（RFC 后 edit_page 复拆）。
7. **debt 照旧 PARK/记录**：HK-queue-size-scope（净 buildable≪nominal，多轮再证）、HK-premature-saturation-claim、
   HK-compute-quality-fullrun-regrade、HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、
   HK-discover-existing-type-blindspot、RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
8. **洲级 America/Europe/Asia 续 HOLD**：America 须与 united-states 消歧。
