---
round: 359
date: 2026-07-19
type_round: 51
phase: "2.1"
current_type: character
gene: NEW1
pages: [mrs-weldon]
result: success
---

# GROW 2.1-B · R359 · NEW1 · character — 建 Mrs. Weldon（Pilgrim 号船主之妻、勇毅乘客，历沉船与非洲囚困；DSCF 簇扩；第七批建序 92）

## 执行摘要

Phase 2.1-B character 第 42 建（type_round 51），消费 R355 第七批 discover 队列**建序 92**。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10；discover_streak_low=0<3；queue(character)=7>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=6。**

**Mrs. Weldon**（*Dick Sand: A Captain at Fifteen*）——Pilgrim 号船主之妻、勇毅乘客，携子与表亲归航，终历沉船与非洲囚困。「the wife of the 'Pilgrim's' owner」携子 Jack 与 Cousin Benedict（DSCF-001-013），「a courageous woman, whom the sea did not frighten」（DSCF-001-018）。乘 Pilgrim 归美（DSCF-001-050），Captain Hull 告以「if you take passage on board the 'Pilgrim,' it is on your own responsibility」（DSCF-001-056），其援夫之信任以答（DSCF-001-059），舱内「installed on board the 'Pilgrim' as comfortably as possible」（DSCF-002-003）。其恻隐驱动情节——见浮筏叹「perhaps there are some unhappy shipwrecked ones on that raft」（DSCF-003-008）；Dick 携众脱险，誓「my husband and I, we shall never forget what you have just done」（DSCF-013-017）。非洲警觉渐增——疑 Negoro「what is Negoro doing?」（DSCF-014-020），且「made suspicious first of all by Negoro's disappearance, observed the newly-arrived with extreme attention」（DSCF-015-054）。遇厄泰然「did not complain, and philosophically took her misfortune in patience」（DSCF-005-003），持信念峻拒奴役「We have no longer any slaves in the United States... The North abolished slavery long ago」（DSCF-015-070），母性及于 Dick「regarded him as her child--a large elder brother of her little Jack」（DSCF-001-023）。

**role=supporting**。book='Dick Sand: A Captain at Fifteen'（work 页 label 含冒号，YAML 单引号，LAW §8）、first_appearance=DSCF-001、affiliation 空、**label=Mrs. Weldon，aliases=[]**。

**14 distinct solid PN**（DSCF-001-013/018/023/050/056/059、002-003、003-008、005-003/022、013-017、014-020、015-054/070）：均 solid，逾门。

**查重**：exact-slug mrs-weldon filesystem + registry entity ABSENT（R355 discover 已验，本轮建前复验一致）。

**DSCF 2-char VVV**：无需 RFC-0003 Note。

**wikilink（DSCF 簇扩）**：[[Dick Sand]]（character，存）/ [[Cousin Benedict]]（character，R358 建）/ [[Dick Sand: A Captain at Fifteen]]（work，存）——三链互链无悬挂。Captain Hull（未建，建序 93 待建）/ Negoro 暂纯文本（DEFERRED）。

prose-gate：add_page 初稿 1 超段（432），插空行拆一刀后 0 超门再建。**引注**：strict 首验即通过。quality featured 未剥离。

character 计数 56→**57**，registry total 1580→**1581**，unknown 恒 0。build_registry 3 alias warn（Hector Servadac + Robur + Claudius Bombarnac，均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=7、since_discover=3 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =7>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=7>0，按既有实践走 NEW1 消费建序 92。消费后 queue=6。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| mrs-weldon | hrUxLu | Dick Sand: A Captain at Fifteen | supporting | DSCF-001 | 14 distinct | Pilgrim 船主之妻-勇毅乘客-恻隐驱动-非洲警觉-泰然持信-母性及 Dick；label Mrs. Weldon + aliases 空；book 冒号单引号；DSCF 2-char 无 Note；拆 1 超段；strict 首验通过；互链 [[Dick Sand]]/[[Cousin Benedict]]/[[Dick Sand: A Captain at Fifteen]] |

- **mrs-weldon**：14 distinct solid PN；aliases []；character-schema 五 H2。add_page rev hrUxLu。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Weldon 船主妻-归航-恻隐-非洲警觉-泰然持信因果；strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：14 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 冒号单引号）；DSCF 2-char 无 Note。✔
- **registry 一致**：total 1581 character 57 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突（label Mrs. Weldon 唯一）。✔
- **wikilink 完整性**：Dick Sand / Cousin Benedict / Dick Sand: A Captain at Fifteen 三链存在无悬挂；Captain Hull/Negoro 纯文本无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R360 起始计数）

| 字段 | R359 起始 | R360 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 359 | 360 |
| type_round | 51 | 52 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 295 | 296 |
| last_updated_round | 359 | 360 |

## 遗留问题

1. **character 页数 57**：本轮 +1（mrs-weldon）。queue(character) 7→**6**（建序 92 消费）。registry 全库 **1581**，unknown 0。
2. **下轮 R360 = NEW1（§3(7)）**：since_evv5=9<10；discover_streak_low=0<3；queue(character)=6>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 93（captain-hull，book Dick Sand: A Captain at Fifteen，pn_anchor DSCF-001，role supporting）——Pilgrim 号船长、捕鲸罹难。
3. **EVV5 时序更正**：since_evv5 于 R351 起始归 0（R350 EVV5 后），逐轮 +1 → R360 起始=9（<10，NEW1），**R361 起始达 10 → §3(1b) EVV5 触发**（此前 R353-R358 日志误记为 R360，实为 R361，off-by-one 更正）。
4. **DSCF 簇渐成**：cousin-benedict + mrs-weldon + dick-sand（既有）+ hercules（既有）+ dick-sand-a-captain-at-fifteen(work)。Captain Hull（建序 93）续建。
5. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、dirk-peters→Arthur Pym、william-guy→Arthur Pym、james-starr→Nell/Simon Ford、claudius-bombarnac→Major Noltitz、erik→Schwaryencrona/Durrien、j-t-maston→Captain Nicholl、cousin-benedict→Mrs. Weldon、mrs-weldon→Captain Hull/Negoro、captain-grant→Robert。
6. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
7. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
8. **散文门债 + character 内容债**（R350 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
9. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
10. **corpus-discover 顺延**：since_corpus=295→296（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
