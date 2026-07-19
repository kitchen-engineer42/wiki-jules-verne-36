---
round: 335
date: 2026-07-19
type_round: 28
phase: "2.1"
current_type: character
gene: NEW1
pages: [captain-grant]
result: success
---

# GROW 2.1-B · R335 · NEW1 · character — 建 Captain Grant（瓶中文书所寻之失踪船长）

## 执行摘要

Phase 2.1-B character 第 23 建（type_round 28），消费 R330 第四批 discover 队列**建序 73**。决策机 §3 首匹配 **NEW1**
（since_evv5=5<10；discover_streak_low=0<3；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**Captain Grant / Harry Grant**（*In Search of the Castaways*）——失踪之苏格兰船长、Britannia 号船主，瓶中文书点名「the BRITANNIA, Captain Grant」（SC-002-072），Glenarvan 一读即认「It is just that same Captain Grant」（SC-002-075）。硬汉鳏父「Captain Grant was a fearless sailor」、「lost his wife when Robert was born」（SC-004-003）。文书载其将「be taken prisoners」（SC-002-079），Helena 追述夫「determined to lay the document before the Lords of the Admiralty」（SC-003-037），海军部拒后 Glenarvan 自任其事「Let us go, Edward; let us start off and search for Captain Grant!」（SC-004-044）。踪迹终指新西兰「the ... BRITANNIA ... has foundered ... on the coast of New Zealand」（SC-063-101），Maria Theresa 岛寻获生还，子呼「my father is there!」（SC-064-070），终与叛徒对质「Ayrton ... found himself face to face with Harry Grant」（SC-065-068）。其志不折「A man like my father doesn't die till he has finished his work」（SC-064-043），子誓「never cease searching for my father, who would never have given us up」（SC-064-039）；且怀殖民壮志「the project ... which made you so popular in our old country」（SC-065-019），Helena 誉之「a grand project of yours, and worthy of a noble heart」（SC-065-021）。

**role=supporting**。book=In Search of the Castaways、first_appearance=**SC-002**（实证首现，非队列所记 SC-001）、affiliation 空、aliases=['Harry Grant']。

**13 distinct solid PN**（SC-002-072/075/079、003-037、004-003/044、063-101、064-039/043/070、065-019/021/068）：均 solid，逾门。

**查重**：exact-slug captain-grant filesystem + registry entity ABSENT。alias 'Harry Grant' 经 build_registry 无冲突。

**SC 2-char VVV**：无需 RFC-0003 Note。

**wikilink（同书簇）**：[[Mary Grant]]（存）、[[Lord Glenarvan]]（id glenarvan，存）、[[Ayrton]]（存）、[[In Search of the Castaways]]（work，存）——四链均存在无悬挂。Robert Grant 暂纯文本（建序 74 未建，R336 建后可回链）。

prose-gate：add_page 初稿 3 超段（Role 两段 495/418、Character 500），各拆一刀后 0 超门再建。**引注**：strict 首验即通过，无需修正。quality featured 未剥离。

character 计数 37→**38**，registry total 1561→**1562**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=2>0、since_discover=4 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=2>0，按既有实践走 NEW1 消费建序 73。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| captain-grant | pXtzPd | In Search of the Castaways | supporting | SC-002 | 13 distinct | 失踪苏格兰船长-瓶中文书-新西兰寻获-殖民壮志；alias Harry Grant 无冲突；first_appearance 实证 SC-002；SC 2-char 无 Note；拆 3 超段；strict 首验通过；Robert 暂纯文本；[[Mary Grant]]/[[Lord Glenarvan]]/[[Ayrton]]/work 互链 |

- **captain-grant**：13 distinct solid PN；aliases ['Harry Grant']；character-schema 五 H2。add_page rev pXtzPd。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Grant 失踪-寻获-志向因果；strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；alias Harry Grant；SC 2-char 无 Note。✔
- **registry 一致**：total 1562 character 38 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug + entity ABSENT；alias 'Harry Grant' 无冲突。✔
- **wikilink 完整性**：Mary Grant/Lord Glenarvan/Ayrton/In Search of the Castaways 四链存在无悬挂；Robert Grant 暂纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R336 起始计数）

| 字段 | R335 起始 | R336 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 335 | 336 |
| type_round | 27 | 28 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 4 | 5 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 271 | 272 |
| last_updated_round | 335 | 336 |

## 遗留问题

1. **character 页数 38**：本轮 +1（captain-grant）。queue(character) 2→**1**（建序 73 消费；余 74：robert-grant）。registry 全库 **1562**，unknown 0。
2. **下轮 R336 = NEW1（§3(7)）**：since_evv5=6<10；queue(character)=1>0 → §3(7) NEW1，消费建序 74（robert-grant）——**队列末位，消费后 queue 归 0**。Robert Grant（book In Search of the Castaways，pn_anchor SC-003，role supporting，SC 2-char 无 Note）——Grant 船长幼子、勇毅随队寻父；建成后可回链 [[Captain Grant]]/[[Mary Grant]]，并回填 captain-grant 页的 Robert 纯文本为链接（另轮 edit_page 视需要）。
3. **R337 预判 = SCN28-zombie（§3(4)）**：R336 消费建序 74 后 queue(character)=0 → §3(4) 触发第五批 discover。深池候选：Sangarre（MS 女间谍）、单作品主角（Hector Servadac / Mathias Sandorf / Kaw-djer / Kéraban / Wilhelm Storitz / Nicholl / Hans 等）。
4. **EVV5 下次约 R339**（since_evv5 于 R329 复位，+10）。
5. **SC 簇扩张**：glenarvan/paganel/ayrton/mary-grant/john-mangles/mcnabbs/thalcave + captain-grant，建序 74（robert-grant）后 SC 簇达九实体。
6. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label 张力（R321 裁例）。
7. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
8. **散文门债 + character 内容债**（R318/R329 EVV5 识别）：7 页 PN<5 + 11 页 over-400，DEFERRED backfill。
9. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
10. **corpus-discover 顺延**：since_corpus=271→272（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
