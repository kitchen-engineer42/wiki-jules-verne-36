---
round: 138
date: 2026-07-15
type_round: 109
phase: "2.1"
current_type: place
gene: EVV5
new_candidates: 0
pages: []
result: reflect
---

# GROW 2.1-B · R138 · EVV5 · place — 周期质量反思（模板稳定；散文债回升 32→37，本批 5 页自致，行为收紧）

## 本轮公告

**R138 — Phase 2.1 — EVV5 — place — 全库 353 place 页 schema 反思 / 非建页 / since_evv5 归 0**

R137 后 since_evv5=10、since_discover=9、discover_streak_low=1、queue(place)=9、since_corpus=74。
决策矩阵 §3 首匹配：**since_evv5=10≥10 → 优先级 1b EVV5 触发**（抢占 queue=9<10 本会触发的 priority 3）。
since_discover=9<10，故非 EVV5+SCN28 合并，纯 EVV5。自 R127 上次 place EVV5 以来累计 11 轮
（type_round 98→109），沿「每约 11 轮一次 EVV5」节奏（R105→R116→R127→R138），本轮对 place 类型
全部已建页面执行 `EVV5-type-pilot-reflect`。本轮不新建/编辑任何页面，不修改模板。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| since_evv5=10, since_discover=9<10 | 否 |
| **1b** | **EVV5（since_evv5≥10）** | **=10** | **触发** |
| 2 | CLOSE+SCN28（discover_streak_low≥3）| =1 | 否（被 1b 抢占）|
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=9<10 | 否（被 1b 抢占）|
| 7 | NEW1（默认）| — | 否 |

> queue=9<10 本会触发 discover，但 EVV5（1b）§3 首匹配最高优先。EVV5 不重置 since_discover/since_corpus，
> discover 分支顺延至 R139（届时 since_discover→10≥10 且 queue<10，双门 → SCN28）。

## 扫描方法与结果

对 `docs/wiki/pages/**/*.md` 中 `type: place` 的 **353** 页逐页核查五维：
(1) 4×H2 结构顺序（Overview / In the Narrative / Geography & Features / Connections）；
(2) 必填 frontmatter 字段（id/type/label/book/real_or_fictional/region/description）；
(3) `real_or_fictional` 取值合法（real|fictional）；(4) 页内引注 distinctPN（全 PN VVV-NNN-PPP）≥5；
(5) 散文段 ≤400 字。

| 维度 | 结果 | 计数 |
|------|------|------|
| H2 结构（4 节顺序）| ✅ 全通过 | 0 违规 / 353 |
| 必填字段齐备 | ✅ 全通过 | 0 缺失 / 353 |
| real_or_fictional 合法 | ✅ 全通过 | 0 非法 / 353 |
| 页内引注 distinctPN ≥5 | ⚠ 2 页 <5 | 2（均既有 Pilot 页，无变化）|
| 散文门 ≤400 | ⚠ 37 页超 400 | 37（较 R127 之 32 增 5）|

### 本批次（R131–R137 七页）引用合法性专核

对本对话 NEW1 七页 texas/senegal/utah/nebraska/nevada/iowa/wisconsin 逐页 pn_validator --mode strict
复核，**全部通过**（每 PN 回 sentence_index 命中真实 sid 段号）。7 页均 4-H2 结构、9/9 字段齐、rof 合法、
distinctPN≥5、无缺链。消歧裁定均在建轮日志留痕（senegal 区域 vs 河、utah 领地 vs 城/湖、nevada 剔 Sierra
山脉泛指、iowa 剔州列举、wisconsin 剔枚举、oregon 因 <5 clean 判 DEFER）。

| slug | distinctPN | PN strict | H2 顺序 | 必填字段 | 缺链 |
|------|-----------|----------|---------|---------|------|
| texas | 11 | ✓ | ✓ | 9/9 | 无 |
| senegal | 11 | ✓ | ✓ | 9/9 | 无 |
| utah | 8 | ✓ | ✓ | 9/9 | 无 |
| nebraska | 7 | ✓ | ✓ | 9/9 | 无 |
| nevada | 5 | ✓ | ✓ | 9/9 | 无 |
| iowa | 5 | ✓ | ✓ | 9/9 | 无 |
| wisconsin | 7 | ✓ | ✓ | 9/9 | 无 |

七页 PN 零缺陷，无系统性错误（无 ≥3 页共性失分），无需向模板注入 ⚠️ 提示块。

### distinctPN <5（2 页，无变化）

`snaefellsjokull`（4）、`hong-kong`（4）——均 BIRTH Pilot 期建，承 R39–R127 **PARK**
（Pilot 页 PN=4 债，非本类型扩张轮产物）。本对话新建 7 页全 ≥5。

### 散文门 >400（37 页，较 R127 之 32 增 5）——**本批 5 页自致，行为债非模板债**

全库 37 place 页含超 400 字长段。经逐页溯源，**净增 5 全为本对话 R131–R136 建页**：

| slug | 段长 | 建轮 | 成因 |
|------|------|------|------|
| nevada | 496 | R135 | Connections 收束段偏长（散文，非引文）|
| iowa | 450 | R136 | Connections 收束段偏长（散文，非引文）|
| senegal | 426 | R132 | 段内嵌 FWB 长引 |
| nebraska | 423 | R134 | 段内嵌 RC/TTLU Bad Lands 并置长引 |
| texas | 410 | R131 | 段内嵌 FEM 长引 |

其余 32 页与 R127 名单一致（Pilot + R40–R65 期建 add_page 旁路遗留 + R121/R123 长引文），max liedenbrock-sea 541。

**成因判定（诚实自陈）**：非模板缺陷（结构/字段/rof 三维 100% 合规）。属**本轮反思者本人的行为纪律回退**——
R124–R127 曾收紧「内嵌引文前评段长、Connections 控长」，但本对话 R131–R136 未续守：5 页各含一段过门
（nevada/iowa 系我自撰 Connections 段偏长，senegal/nebraska/texas 系内嵌整块直接引文）。utah/wisconsin 本批
守门（max 377/380）。

**行为自纠（前瞻，非模板变动、非本轮编辑）**：R137 wisconsin 已复归守门（380）。**R139 起 NEW1 续守纪律**：
(a) Connections 收束段控 ≤400；(b) 内嵌长直接引文单独成 blockquote 或拆句。既有 37 页 DEFERRED（RFC 后
edit_page 统一复拆，含本批 5 页）。EVV5 轮不编辑页面，故本轮不就地修复，仅记录 + 承诺后续纪律。

## EVV5 结论

**模板稳定，无需更新。** place-schema 三要素（4-H2 结构、7 必填字段、real_or_fictional 二值域）
在 353 页上 100% 合规，无字段普遍缺失、无某节约束不清的结构性问题。两类瑕疵均非模板缺陷：
- distinctPN<5：2 既有 Pilot 页历史债，PARK；
- 散文>400：37 页（32 既有 + 5 本批 R131–R136），**本批增量系反思者行为纪律回退**，DEFERRED（RFC 后
  edit_page 复拆），行为面 R137 起已收紧、R139 起续守。

按 EVV5 规则「若无结构变动 → 记录『模板稳定』，继续建页节奏」，`local/template/place-schema.md`
**不修改**（且该文件为 working-tree 既有 dirty 变更，属排除项，本轮不触碰），不触发 backfill，
不新起 RFC（组件债依 RFC-parking 记 housekeeping，用户末期批量评审）。

> **附**：registry 复扫仅剩 Robur alias 旧账 PARK（'Robur the Conqueror' → robur-the-conqueror vs robur），
> 无其他 label 冲突。全库 1421 页，unknown 0。

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

`current_round 138→139`；`type_round 109→110`；`rounds_since_last_evv5 10→0`（EVV5 RESET）；
`rounds_since_last_discover 9→10`（EVV5 非 discover 轮，+1）；`discover_streak_low` 保持 1；
`rounds_since_last_corpus_discover 74→75`；`last_updated_round→139`。

## 遗留问题

1. **place 页数保持 353**：本轮非建页，registry 全库 1421，unknown 0。
2. **下轮 R139 = SCN28（表层 discover）**：since_evv5 归 0；since_discover→10≥10 且 queue=9<10 → §3 优先级 3 触发 SCN28 补种。
   place 候选池现存 Illinois/Michigan/Missouri/Ohio/Colorado/Soudan/Guinea/Abyssinia/Indiana 9 项（部分待河/湖/泛指筛选）；
   SCN28 应宽扫补新候选并复议 held/hold 项，或对 Missouri/Ohio/Colorado 河湖消歧、Michigan vs lake-michigan 裁定。
3. **corpus-discover 顺延临界**：since_corpus=74，已远过阈 30；待表层复扫近罄时转 corpus 深扫（HK-corpus-discover-not-in-statemachine PARK）。
4. **EVV5 节奏**：R127→R138 隔 11 轮；since_evv5 归 0，下次约 R149。
5. **EVV6 封存点预告**：Phase 2.1 关闭前须对每类型执行一次 EVV6 全库评审并回填均分。
6. **散文门债量化更新**：37 页 >400（32 既有 + 5 本批 R131–R136 自致）；R137 起行为收紧，R139 起续守。
   既有债 DEFERRED（RFC 后 edit_page 复拆）。
7. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-discover-existing-type-blindspot、
   RFC-0003 VVV 宽度、Robur alias、featured 虚高、两 Pilot 页 PN=4。
8. **洲级 America/Europe/Asia 续 HOLD**：America 须与 united-states 消歧。
