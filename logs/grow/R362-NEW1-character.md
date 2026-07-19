---
round: 362
date: 2026-07-19
type_round: 54
phase: "2.1"
current_type: character
gene: NEW1
pages: [doctor-clawbonny]
result: success
---

# GROW 2.1-B · R362 · NEW1 · character — 建 Doctor Clawbonny（Forward 号博学随船医生、北极远征之百科随员；ACH 补 captain-hatteras 簇；第七批建序 94）

## 执行摘要

Phase 2.1-B character 第 44 建（type_round 54），消费 R355 第七批 discover 队列**建序 94**。决策机 §3 首匹配 **NEW1**
（since_evv5=0<10；discover_streak_low=0<3；queue(character)=5>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=4。**

**Doctor Clawbonny**（*The Adventures of Captain Hatteras*）——Forward 号博学随船医生，名义为医、志在博物。招募信匿名荐之「Dr. Clawbonny, of this town, who will introduce himself to you when necessary」（ACH-002-007），实为「a doctor, and a good one, though practising little」（ACH-003-054），中年已成 savant、跻身利物浦学界。持信登船「If Dr. Clawbonny wishes to embark on board the 'Forward' for a long cruise, he may introduce himself to the commander」（ACH-003-042）；其在使船员心安——「the admission of the doctor on board had given the crew more confidence」，盖「they knew that where the worthy doctor went they could follow」（ACH-004-002）。极地雪橇队定员，与 Hatteras 商议后成行「a short discussion about it between Hatteras and Clawbonny, the journey was persisted in」（ACH-028-003），队为「four men, Hatteras, Clawbonny, Bell, and Simpson, and seven dogs」（ACH-028-013）。舱室即浮动博物馆——履任即「in his element」（ACH-004-004），方寸间可瞬成「a doctor, a mathematician, an astronomer, a geographer, a botanist, or a conchologist」（ACH-004-006）。学识自谦「they pretend that I am learned; they are mistaken, commander」（ACH-003-047），船员却叹「the doctor has an answer to everything」（ACH-004-015）；仁厚「would have tamed a tiger」（ACH-004-007）。向老水手 Johnson 求知「Clawbonny was getting information from the old sailor」（ACH-007-003）；释冰原之理「scientific men, and Dr. Clawbonny amongst them」（ACH-024-002）、化雪墙为庇护（ACH-024-007）。

**role=supporting**。book='The Adventures of Captain Hatteras'（YAML 单引号，LAW §8）、first_appearance=ACH-002、affiliation 空、**label=Doctor Clawbonny，aliases=[]**。

**14 distinct solid PN**（ACH-002-007、003-042/047/054、004-002/004/006/007/015、007-003、024-002/007、028-003/013）：均 solid，逾门。

**查重**：exact-slug doctor-clawbonny filesystem + registry entity ABSENT（R355 discover 已验，本轮建前复验一致）。

**ACH 2-char VVV**：无需 RFC-0003 Note。

**wikilink（ACH 簇补 captain-hatteras）**：[[Captain Hatteras]]（character，存）/ [[The Adventures of Captain Hatteras]]（work，存）——二链互链无悬挂。Johnson/Bell/Simpson（未建）暂纯文本（DEFERRED）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 58→**59**，registry total 1582→**1583**，unknown 恒 0。build_registry 3 alias warn（Hector Servadac + Robur + Claudius Bombarnac，均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=5、since_discover=6 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =5>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=5>0，按既有实践走 NEW1 消费建序 94。消费后 queue=4。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| doctor-clawbonny | tAzPSF | The Adventures of Captain Hatteras | supporting | ACH-002 | 14 distinct | Forward 博学随船医生-名医志博物-持信登船-在使船员心安-极地雪橇队员-舱室浮动博物馆-学识自谦-仁厚；label Doctor Clawbonny + aliases 空；ACH 2-char 无 Note；0 超段直建；strict 首验通过；互链 [[Captain Hatteras]]/[[The Adventures of Captain Hatteras]] |

- **doctor-clawbonny**：14 distinct solid PN；aliases []；character-schema 五 H2。add_page rev tAzPSF。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Clawbonny 身份-招募-博学-仁厚-极地随行因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：14 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号）；ACH 2-char 无 Note。✔
- **registry 一致**：total 1583 character 59 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Doctor Clawbonny 唯一）。✔
- **wikilink 完整性**：Captain Hatteras / The Adventures of Captain Hatteras 二链存在无悬挂；Johnson/Bell/Simpson 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R363 起始计数）

| 字段 | R362 起始 | R363 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 362 | 363 |
| type_round | 54 | 55 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 6 | 7 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 298 | 299 |
| last_updated_round | 362 | 363 |

## 遗留问题

1. **character 页数 59**：本轮 +1（doctor-clawbonny）。queue(character) 5→**4**（建序 94 消费）。registry 全库 **1583**，unknown 0。
2. **下轮 R363 = NEW1（§3(7)）**：since_evv5=1<10；discover_streak_low=0<3；queue(character)=4>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 95（tudor-brown，book The Waif of the Cynthia，pn_anchor WC-010，role antagonist）。**下次 EVV5 于 R371 起始达 since_evv5=10。**
3. **第七批剩 4 候选（建序 95-98）**：tudor-brown/uncle-prudent/ker-karraje/major-noltitz。R363 起 NEW1 续消费。queue 归 0 后 R367 起 SCN28-zombie 第八批 discover。
4. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、dirk-peters→Arthur Pym、william-guy→Arthur Pym、james-starr→Nell/Simon Ford、claudius-bombarnac→Major Noltitz、erik→Schwaryencrona/Durrien、j-t-maston→Captain Nicholl、cousin-benedict→Mrs. Weldon、mrs-weldon→Captain Hull/Negoro、captain-hull→Negoro、captain-grant→Robert、doctor-clawbonny→Johnson/Bell/Simpson。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R361 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=298→299（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
