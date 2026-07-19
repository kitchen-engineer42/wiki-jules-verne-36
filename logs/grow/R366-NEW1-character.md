---
round: 366
date: 2026-07-19
type_round: 58
phase: "2.1"
current_type: character
gene: NEW1
pages: [major-noltitz]
result: success
---

# GROW 2.1-B · R366 · NEW1 · character — 建 Major Noltitz（The Adventures of a Special Correspondent 俄军军医、Bombarnac 之向导与知己；ASC 配对 claudius-bombarnac；第七批建序 98 末位，queue 归零）

## 执行摘要

Phase 2.1-B character 第 48 建（type_round 58），消费 R355 第七批 discover 队列**建序 98（末位）**。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=0，第七批告罄。R367 起 §3(4) SCN28-zombie 第八批 discover。**

> **决策注**：R366 起始 since_discover=10，literal §3(3) SCN28（since_discover≥discover_periodic_interval）触发。然既有实践——queue(character)>0 时走 NEW1 消费候选，SCN28 discover 仅在 queue==0（§3(4) zombie）启。故本轮 NEW1 消费末位候选，消费后 queue 归零，discover 顺延至 R367。

**Major Noltitz**（*The Adventures of a Special Correspondent*）——俄军军医，Bombarnac 之向导与知己。以职衔登场「a doctor in the Russian army, and they call him Major Noltitz」（ASC-004-032），初见于餐桌少数通程旅客间（ASC-004-047）；记者一见倾心「I like this Major Noltitz... I hope to make his acquaintance very soon」（ASC-006-039）。长途成其向导「my good fortune furnished me with a companion, or I should rather say a guide, in Major Noltitz」（ASC-007-002）；坦率相识「I am a Frenchman, Claudius Bombarnac... and you are Major Noltitz of the Russian army」（ASC-007-004），继以「become more than mere traveling companions」之议（ASC-007-006）；作向导述铁路史「of the facts which had gradually prepared the conquest of Turkestan and its definite incorporation with the Russian」帝国（ASC-007-017）。目敏而识微——「as much struck as I was at the behavior of my lord Faruskiar」（ASC-015-070），危近仍「to watch Faruskiar and the Mongols」（ASC-020-006）；危局判确，直指叛徒「the rascal who sent us on to the Nanking line, who would have hurled us into the Tjon valley, to walk off with the imperial treasure, is Faruskiar」（ASC-025-044）；善交游，与船长静谈于耐海之少数间（ASC-004-087）。

**role=supporting**。book='The Adventures of a Special Correspondent'（YAML 单引号，LAW §8）、first_appearance=ASC-004、affiliation=Russian army、**label=Major Noltitz，aliases=[]**。

**11 distinct solid PN**（ASC-004-032/047/087、006-039、007-002/004/006/017、015-070、020-006、025-044）：均 solid，逾门。

**查重**：exact-slug major-noltitz filesystem + registry entity ABSENT（R355 discover 已验，本轮建前复验一致）。

**ASC 3-char VVV**：ASC 为 3 字符，等宽 3——无需 RFC-0003 Note（Note 仅 4-char VVV 需）。

**wikilink（ASC 配对 claudius-bombarnac）**：[[Claudius Bombarnac]]（character，存）/ [[The Adventures of a Special Correspondent]]（work，存）——二链互链无悬挂。Faruskiar（未建）暂纯文本（DEFERRED）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 62→**63**，registry total 1586→**1587**，unknown 恒 0。build_registry 3 alias warn（Hector Servadac + Robur + Claudius Bombarnac，均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=1、since_discover=10 | 触发* |
| 4 | SCN28-zombie（queue(character)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（既有实践优先）** | **—** | **触发** |

> *§3(3) literal 触发（since_discover=10），但既有实践 queue(character)=1>0 时优先 NEW1 消费末位候选（SCN28 discover 仅在 queue 归零后启）。消费后 queue=0 → R367 §3(4) SCN28-zombie。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| major-noltitz | ct4em0 | The Adventures of a Special Correspondent | supporting | ASC-004 | 11 distinct | 俄军军医-Bombarnac 向导知己-述铁路史-目敏识微-揭 Faruskiar 之叛-善交游；label Major Noltitz + aliases 空；affiliation Russian army；ASC 3-char 无 Note；0 超段直建；strict 首验通过；互链 [[Claudius Bombarnac]]/[[The Adventures of a Special Correspondent]] |

- **major-noltitz**：11 distinct solid PN；aliases []；character-schema 五 H2。add_page rev ct4em0。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Major Noltitz 军医身份-向导-铁路史-识微-揭叛-交游因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：11 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号、affiliation Russian army）；ASC 3-char 无 Note。✔
- **registry 一致**：total 1587 character 63 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Major Noltitz 唯一）。✔
- **wikilink 完整性**：Claudius Bombarnac / The Adventures of a Special Correspondent 二链存在无悬挂；Faruskiar 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R367 起始计数）

| 字段 | R366 起始 | R367 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 366 | 367 |
| type_round | 58 | 59 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 10 | 11 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 302 | 303 |
| last_updated_round | 366 | 367 |

## 遗留问题

1. **character 页数 63**：本轮 +1（major-noltitz）。queue(character) 1→**0**（建序 98 末位消费，第七批告罄）。registry 全库 **1587**，unknown 0。
2. **下轮 R367 = SCN28-zombie（§3(4)）**：since_evv5=5<10；discover_streak_low=0<3；**queue(character)=0 → §3(4) SCN28-zombie 触发**，第八批 discover（补候选队列，pages:[]，仅 G4，since_discover 归 0）。产出 ≥3 grounded+dup-checked 候选，追加 queue.md `<!-- [character] R367 建序 99+ ... -->` 行 + discover-note。stage：grow_state + R367-SCN28 日志 + queue.md。**下次 EVV5 于 R371 起始达 since_evv5=10。**
3. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、dirk-peters→Arthur Pym、william-guy→Arthur Pym、james-starr→Nell/Simon Ford、claudius-bombarnac→Major Noltitz/Faruskiar、erik→Schwaryencrona/Durrien/Tudor Brown、j-t-maston→Captain Nicholl、cousin-benedict→Mrs. Weldon、mrs-weldon→Captain Hull/Negoro、captain-hull→Negoro、captain-grant→Robert、doctor-clawbonny→Johnson/Bell/Simpson、tudor-brown→Patrick O'Donoghan、uncle-prudent→Phil Evans、ker-karraje→Engineer Serko/Simon Hart、major-noltitz→Faruskiar。
4. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
5. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
6. **散文门债 + character 内容债**（R361 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
7. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
8. **corpus-discover 顺延**：since_corpus=302→303（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
