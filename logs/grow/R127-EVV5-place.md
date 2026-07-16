---
round: 127
date: 2026-07-15
type_round: 98
phase: "2.1"
current_type: place
gene: EVV5
new_candidates: 0
pages: []
result: reflect
---

# GROW 2.1-B · R127 · EVV5 · place — 周期质量反思（模板稳定，prose 债量化增至 32）

## 本轮公告

**R127 — Phase 2.1 — EVV5 — place — 全库 343 place 页 schema 反思 / 非建页 / since_evv5 归 0**

R126 后 since_evv5=10、since_discover=4、discover_streak_low=0、queue(place)≈6、since_corpus=63。
决策矩阵 §3 首匹配：**since_evv5=10≥10 → 优先级 1b EVV5 触发**（抢占 queue<10 本会触发的 priority 3、
及 since_corpus=63≥30 的项目扩展 corpus-discover）。since_discover=4<10，故非 EVV5+SCN28 合并，纯 EVV5。
自 R116 上次 place EVV5 以来累计 11 轮（type_round 87→98），沿「每约 11 轮一次 EVV5」节奏
（R61→R72→R83→R94→R105→R116→R127），本轮对 place 类型全部已建页面执行 `EVV5-type-pilot-reflect`。
本轮不新建/编辑任何页面，不修改模板。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| since_evv5=10, since_discover=4<10 | 否 |
| **1b** | **EVV5（since_evv5≥10）** | **=10** | **触发** |
| 2 | CLOSE+SCN28（discover_streak_low≥3）| =0 | 否（被 1b 抢占）|
| 3 | SCN28（queue<10 或 since_discover≥10）| queue≈6<10 | 否（被 1b 抢占）|
| 3.5 | SCN28-corpus（since_corpus≥30，项目扩展）| =63 | 否（被 1b 抢占；非 §3 分支，记 HK-corpus-discover-not-in-statemachine PARK）|
| 7 | NEW1（默认）| — | 否 |

> queue≈6<10 与 since_corpus=63≥30 本会触发 discover，但 EVV5（1b）§3 首匹配最高优先，
> 本轮先做质量反思。EVV5 不重置 since_discover/since_corpus，两 discover 分支顺延至 R128。

## 扫描方法与结果

对 `docs/wiki/pages/**/*.md` 中 `type: place` 的 **343** 页逐页核查五维：
(1) 4×H2 结构顺序（Overview / In the Narrative / Geography & Features / Connections）；
(2) 必填 frontmatter 字段（id/type/label/book/real_or_fictional/region/description）；
(3) `real_or_fictional` 取值合法（real|fictional）；(4) 页内引注 distinctPN（全 PN VVV-NNN-PPP）≥5；
(5) 散文段 ≤400 字。

| 维度 | 结果 | 计数 |
|------|------|------|
| H2 结构（4 节顺序）| ✅ 全通过 | 0 违规 / 343 |
| 必填字段齐备 | ✅ 全通过 | 0 缺失 / 343 |
| real_or_fictional 合法 | ✅ 全通过 | 0 非法 / 343 |
| 页内引注 distinctPN ≥5 | ⚠ 2 页 <5 | 2（均既有 Pilot 页）|
| 散文门 ≤400 | ⚠ 32 页超 400 | 32（add_page 旁路遗留 + 部分近轮长引文段）|

### 本批次（R126 四页）引用合法性专核

对上批 NEW1（R126）四页 salt-lake-city/charleston/richmond/washington 逐页实质核（非倚赖 featured 自动分）：
每 PN 回 `data/sentence_index/VVV-NNN.jsonl` 核 sid 段号真实存在，全部命中；4 页均 4-H2 结构、
9/9 字段齐、散文全 ≤400（复扫无一进 over-400 名单）、无缺链/破折号链。

| slug | distinctPN | PN 存在性 | H2 顺序 | 必填字段 | 散文>400 | 缺链 |
|------|-----------|----------|---------|---------|---------|------|
| salt-lake-city | 5 | 全存在 | ✓ | 9/9 | 0 | 无 |
| charleston | 12 | 全存在 | ✓ | 9/9 | 0 | 无 |
| richmond | 8 | 全存在 | ✓ | 9/9 | 0 | 无 |
| washington | 8 | 全存在 | ✓ | 9/9 | 0 | 无 |

四页零缺陷，无系统性错误（无 ≥3 页共性失分），无需向模板注入 ⚠️ 提示块。

### distinctPN <5（2 页，无变化）

`snaefellsjokull`（4）、`hong-kong`（4）——均 BIRTH Pilot 期建，承 R39–R116 **PARK**
（Pilot 页 PN=4 债，非本类型扩张轮产物）。R117–R126 新建 20 页全 ≥5。

### 散文门 >400（32 页，较 R116 之 24 增 8）——含近轮长引文段

全库 32 place 页含超 400 字长段，max **bay-of-talcahuano 614**。较 R116（24 页）**净增 8**，
经逐页溯源，8 页增量**全为本对话较早轮（R121/R123）建页**，成因为**内嵌长直接引文**将整段推过 400：

| slug | 段长 | 建轮 | 成因 |
|------|------|------|------|
| timbuctoo | 516 | R121 | 段内嵌 FWB Timbuctoo 沿革长引 |
| florida | 504 | R121 | 段内嵌 FEM「Ponce de Leon 1512」史料长引 |
| spitzbergen | 476 | R123 | ACH 极地长句 |
| newfoundland | 463 | R123 | TN/ACH 渔场长句 |
| boston | 452 | R123 | MW/BR 长句 |
| kamtchatka | 429 | R121 | FC 长句 |
| south-pole | 426 | R121 | TTLU 南极长句 |
| philadelphia | 422 | R123 | RC/MW 长句 |

其余 24 页与 R116 名单一致（Pilot + R40–R65 期建，add_page 旁路遗留），max liedenbrock-sea 541。

**成因判定**：非模板缺陷（结构/字段/rof 三维 100% 合规）。属两类内容卫生债：
(a) distinctPN<5：2 Pilot 页历史债，PARK；(b) 散文>400：`add_page.py` 建时不执行散文门
（HK-addpage-prose-gate-bypass），DEFERRED 待 RFC 后 edit_page 统一复拆。

**行为自纠（前瞻，非模板变动）**：R121/R123 的 8 页因内嵌整块直接引文致段超门。R124–R126 起
已收紧——长直接引文单独成 blockquote 行或拆句，故 R124/R125/R126 建页复扫 over-400=0。
后续建页续守此纪律：内嵌引文前评段长，超门即拆。

## EVV5 结论

**模板稳定，无需更新。** place-schema 三要素（4-H2 结构、7 必填字段、real_or_fictional 二值域）
在 343 页上 100% 合规，无字段普遍缺失、无某节约束不清的结构性问题。两类瑕疵均非模板缺陷：
- distinctPN<5：2 既有 Pilot 页历史债，PARK；
- 散文>400：32 页（24 既有 + 8 近轮长引文段）add_page 组件旁路 + 引文纪律偶疏，DEFERRED。

按 EVV5 规则「若无结构变动 → 记录『模板稳定』，继续建页节奏」，`local/template/place-schema.md`
**不修改**（且该文件为 working-tree 既有 dirty 变更，属排除项，本轮不触碰），不触发 backfill，
不新起 RFC（组件债依 RFC-parking 记 housekeeping，用户末期批量评审）。

> **附**：本轮 registry 复扫仅剩 Robur alias 旧账 PARK（'Robur the Conqueror' → robur-the-conqueror vs robur），
> 无其他 label 冲突。全库 1411 页，unknown 0。

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

`current_round 127→128`；`type_round 98→99`；`rounds_since_last_evv5 10→0`（EVV5 RESET）；
`rounds_since_last_discover 4→5`（EVV5 非 discover 轮，+1）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 63→64`；`last_updated_round→128`。

## 遗留问题

1. **place 页数保持 343**：本轮非建页，registry 全库 1411，unknown 0。
2. **下轮 R128 = SCN28（表层 discover）**：since_evv5 归 0；queue≈6<10 → §3 优先级 3 触发 SCN28 补种。
   place 候选池近罄（洲级 Asia/Europe/America HOLD + Long Island/Bay of Bengal 4<门 hold + Panama 消歧未决），
   需宽式扫描补新候选或复议 held/hold 项升格。若表层 0 新且 since_corpus=64≥30，则转 corpus 深扫。
3. **corpus-discover 顺延临界**：since_corpus=64，已远过阈；待表层复扫 0 新时转 corpus 深扫补单作残余。
4. **EVV5 节奏**：R116→R127 隔 11 轮；since_evv5 归 0，下次约 R138。
5. **EVV6 封存点预告**：Phase 2.1 关闭前（2.1-Z-0）须对每类型执行一次 EVV6 全库评审并回填均分。
6. **散文门债量化更新**：32 页 >400（24 既有 + 8 近轮 R121/R123 长引文）；行为纪律 R124 起收紧，
   R124–R126 建页 over-400=0。既有债 DEFERRED（RFC 后 edit_page 复拆），无新增自 R124。
7. **discover blindspot 累积（≥5 例）**：pacific/atlantic/ural/caspian/baikal——PHQ 批量补裸名 alias +
   probe 去 Sea/Mountains/River/Ocean/Lake 前后缀。归 HK-discover-existing-type-blindspot（PARK）。
8. **PHQ 待决候选**：Amsterdam 荷城（<5 门）；Rome/Petersburg/Athens（称号/缩写系，真城确指 <门）；
   Lucknow（SC:7 澳洲路点非印度城）；真俄 Archangel（1 PN<门）；Panama 消歧（isthmus/gulf/city/route）。
9. **amsterdam-island R45 页不合规**：H1 + bullet Connections + aliases list——PHQ，待 RFC 后 edit_page 整改。
10. **debt 照旧 PARK/记录**：HK-addpage-prose-gate-bypass（32 页）、HK-book-colon-yaml-break、featured 虚高、
    RFC-0003 VVV 宽度、Robur alias、两 Pilot 页 PN=4、HK-corpus-discover-not-in-statemachine。建成后统一处理。
11. **洲级 America/Europe/Asia 续 HOLD**：America 须与 united-states 消歧；England 221/France 169 国级页价值待评。
