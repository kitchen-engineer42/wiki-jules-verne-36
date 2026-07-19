---
round: 406
date: 2026-07-19
type_round: 98
phase: "2.1"
current_type: character
gene: NEW1
pages: [mac-nab]
result: success
---

# GROW 2.1-B · R406 · NEW1 · character — 建 Mac-Nab（The Fur Country 之苏格兰木匠工头，Fort Hope 营建与逃生大船之主力；FC 簇第七页，第十六批建序 125，queue 2→1）

## 执行摘要

Phase 2.1-B character 第 75 建（type_round 98），消费 R403 第十六批 discover 队列**建序 125**。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=2>0 且 since_discover=2<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=1**（建序 126 待 R407 消费）。

**Mac-Nab**（*The Fur Country*）——探险队之苏格兰木匠工头、Fort Hope 营建之主力。营建之主「Hobson and Mac-Nab the carpenter went to choose the site of the principal house」（FC-013-005），万物皆造「the carpenter Mac-Nab constructed a most substantial table」（FC-014-002），统率工班「the business of Mac-Nab and his men」（FC-013-013），筑垒设哨「to erect a wooden sentry-box commanding the coast-line」（FC-014-011），勤勉不辍「Mac-Nab and his subordinates set to work zealously, and completed their task in a few days」（FC-019-003），受命造舟「Mac-Nab was ordered to commence the construction of a huge boat」（FC-026-003），偕众造船「Petersen, Belcher, Garry, Pond, and Hope...worked zealously at the construction of a boat」（FC-028-006）。技捷务实「was able to proceed very rapidly without endangering the safety of the building」（FC-013-014），亦善射猎「Sabine and Mac-Nab might many a time have shot a very valuable animal」（FC-011-019），临挫忧惧「poor Mac-Nab was in despair...had not reckoned upon such a contingency when he constructed the roof」（FC-021-025），列名勇者「Long, Mac-Nab, and Rae the blacksmith, as the bravest men in his party」（FC-021-032），忠而顾家「volunteered for the perilous service...reminded the other two that they were married」（FC-021-039）。

**role=supporting**。book='The Fur Country'、first_appearance=FC-011、affiliation 空、**label=Mac-Nab，aliases=[]**。

**13 distinct solid PN**（FC-011-019、013-005/013/014、014-002/011、017-027、019-003、021-025/032/039、026-003、028-006）：均 solid，逾门。「Mac-Nab」FC 内消歧——本页取男性木匠工头之指涉句，**严格区分 Mrs Mac-Nab（其妻）**（FC-017-027 引「the head carpenter」明指本人为骄傲之父）。

**查重**：exact-slug mac-nab filesystem test -f ABSENT（bucket ma）+ registry entity/label 复验——命中既有 **mcnabbs（Major McNabbs）**，然系 *In Search of the Castaways* 之 Paganel 同伴少校，**异作品异实体**（label「Major McNabbs」≠「Mac-Nab」，book 异，role 异）；FC 木匠 Mac-Nab 作 character label ABSENT，无冲突。**同名异实体辨析教训延续**（HK(e) 同名 label 类）。

**FC 2-char VVV**：无需 RFC-0003 Note（仅 4-char 触发）。

**wikilink**：[[Jaspar Hobson]]（lieutenant-hobson，既建，FC 簇）、[[The Fur Country]]（work，存）——均无悬挂。**Mrs Mac-Nab 页未建**：Relationships bullet 以正文明指之 plain-text（PN grounded FC-017-027，不设悬挂链）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 89→**90**，registry total 1613→**1614**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=2、since_discover=2 | 否* |
| 4 | SCN28-zombie（queue==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=2>0 → NEW1 消费建序 125。消费后 queue=1，R407 消费 126。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| mac-nab | OgnzT7 | The Fur Country | supporting | FC-011 | 13 distinct | 营建之主-万物皆造-统率工班-筑垒设哨-勤勉不辍-受命造舟-偕众造船-技捷务实-亦善射猎-临挫忧惧-列名勇者-忠而顾家；label Mac-Nab；FC 2-char 无 Note；0 超段直建；strict 首验通过；双链 [[Jaspar Hobson]]/[[The Fur Country]]（Mrs Mac-Nab 未建作 plain-text）；严格区分 mcnabbs（异作品少校）|

- **mac-nab**：13 distinct solid PN；aliases []；character-schema 五 H2。add_page rev OgnzT7（size 2894）。quality featured 回填。pn_validator --mode strict ✓。**FC 簇第七页；同名 mcnabbs 辨析确认异实体。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Mac-Nab 木匠-工头-造舟-勇者因果；「Mac-Nab」消歧后取男性工头指涉句，排除 Mrs Mac-Nab；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book/description 单引号）；role=supporting ∈ enum；FC 2-char 无 Note。✔
- **registry 一致**：total 1614 character 90 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug ABSENT；命中 mcnabbs（Major McNabbs）经辨析确认异作品异实体，无冲突。✔
- **wikilink 完整性**：Jaspar Hobson + The Fur Country 双链存在无悬挂；Mrs Mac-Nab 未建作 plain-text 不悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R407 起始计数）

| 字段 | R406 起始 | R407 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 406 | 407 |
| type_round | 98 | 99 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 342 | 343 |
| last_updated_round | 406 | 407 |

## 遗留问题

1. **character 页数 90**：本轮 +1（mac-nab）。queue(character) 2→**1**（建序 125 消费）。registry 全库 **1614**，unknown 0。
2. **下轮 R407 = NEW1（§3(7)）**：since_evv5=2<10；queue=1>0 且 since_discover=3<10 → NEW1，消费建序 126 **hans-bjelke**（JCE，JCE-011，supporting，153 mentions；冰岛绒鸭猎人、Lidenbrock 地心探险之沉默向导；可回链 [[Professor Lidenbrock]]/[[Axel]]）。**消费后 queue=0 → R408 SCN28-zombie 补第十七批。**
3. **第十六批消费**：R405 NEW1（124 samuel-fergusson ✓）→ R406 NEW1（125 mac-nab ✓）→ R407 NEW1（126 hans-bjelke）→ queue 归 0 → R408 SCN28-zombie。
4. **回链回填债**（DEFERRED，非阻塞）：dick-kennedy→samuel-fergusson 反向、Mrs Mac-Nab 待建、Joe 待建、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。JCE hans-bjelke（待建）可回链 professor-lidenbrock/axel。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）；（f）**同名异实体人物 label**（Mac-Nab vs Major McNabbs——本轮 slug 分立 mac-nab/mcnabbs、label 各异，无冲突，仅记录辨析）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R404 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R414 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=342→343（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
