---
round: 333
date: 2026-07-19
type_round: 26
phase: "2.1"
current_type: character
gene: NEW1
pages: [harry-blount]
result: success
---

# GROW 2.1-B · R333 · NEW1 · character — 建 Harry Blount（刻板英国记者）

## 执行摘要

Phase 2.1-B character 第 21 建（type_round 26），消费 R330 第四批 discover 队列**建序 71**。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10；discover_streak_low=0<3；queue(character)=4>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**Harry Blount**（*Michael Strogoff*）——报道鞑靼入侵之英国战地记者，「Harry Blount was the name of the Englishman」（MS-002-039），供稿 Daily Telegraph，自信「the readers of the Daily Telegraph would not fail to be as well informed as Alcide Jolivet's 'cousin'」（MS-005-049）。沉默寡言、观察入微「speaking little, but listening much」（MS-005-047）。战场上与 Jolivet「no longer traveling companions, but rivals, enemies」（MS-018-034）；抢占电报窗口「took possession of the wicket」（MS-018-037），以童年诗句拖延占线「telegraphing some verses learned in his childhood」（MS-018-050）。采访负伤「Harry Blount fell to the ground wounded in the shoulder」（MS-018-071），与 Jolivet 同被掳入鞑靼营「had also been taken to the Tartar camp」（MS-020-021），仍直问同伴（MS-020-040）。刻板严谨——「Alcide spoke in sentences; Blount replied by monosyllables」（MS-013-018）、「a methodical eater」（MS-013-021）；带英式戒心「'Too much ambition has lost the greatest empires,' answered Blount」（MS-020-044）；至终「the reserved Englishman」（MS-029-042），然守信「'On my word as a gentleman,' added Blount」（MS-029-050），狼战不怯「fought bravely with the brutes」（MS-030-025）。

**role=supporting**。book=Michael Strogoff、first_appearance=MS-002、affiliation 空、aliases 空。

**17 distinct solid PN**（MS-002-039、005-047/049、013-018/021、018-034/037/050/071、020-021/022/040/044、029-042/050/057、030-025）：均 solid，逾门。

**查重**：exact-slug harry-blount filesystem + registry entity ABSENT。

**MS 2-char VVV**：无需 RFC-0003 Note。

**wikilink（同书簇）**：[[Alcide Jolivet]]（R332，本轮回链达成）、[[Michel Strogoff]]（R321）、[[Michael Strogoff]]（work）——三链均存在无悬挂。R332 遗留的 Jolivet-Blount 回链于本轮闭合。

prose-gate：add_page 初稿 3 超段（Overview 480、Role 484、Character 769），各拆一刀后 0 超门。**引注**：strict 首验即通过，无需修正。add_page rev MWj9rh，quality featured 未剥离。

character 计数 35→**36**，registry total 1559→**1560**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=4>0、since_discover=2 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =4>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=4>0，按既有实践走 NEW1 消费建序 71。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| harry-blount | MWj9rh | Michael Strogoff | supporting | MS-002 | 17 distinct | 英国 Daily Telegraph 记者-刻板严谨-电报窗口竞逐-负伤被掳-守信勇战；MS 2-char 无 Note；拆 3 超段；strict 首验通过无修正；[[Alcide Jolivet]]/[[Michel Strogoff]]/[[Michael Strogoff]] 互链，Jolivet-Blount 回链闭合 |

- **harry-blount**：17 distinct solid PN；aliases 空；character-schema 五 H2。add_page rev MWj9rh。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Blount 记者-竞逐-负伤-刻板因果；strict ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：17 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；MS 2-char 无 Note。✔
- **registry 一致**：total 1560 character 36 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Alcide Jolivet/Michel Strogoff/Michael Strogoff 三链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R334 起始计数）

| 字段 | R333 起始 | R334 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 333 | 334 |
| type_round | 25 | 26 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 269 | 270 |
| last_updated_round | 333 | 334 |

## 遗留问题

1. **character 页数 36**：本轮 +1（harry-blount）。queue(character) 4→**3**（建序 71 消费；余 72-74：feofar-khan/captain-grant/robert-grant）。registry 全库 **1560**，unknown 0。
2. **下轮 R334 = NEW1（§3(7)）**：since_evv5=4<10；queue(character)=3>0 → §3(7) NEW1，消费建序 72（feofar-khan）。Feofar-Khan（book Michael Strogoff，pn_anchor MS-003，role antagonist，MS 2-char 无 Note）——Bukhara 埃米尔、鞑靼入侵名义首领、判 Michael 目盲之刑；与 ivan-ogareff/michel-strogoff 可互链，event the-sentence-of-feofar-khan 可回链。
3. **EVV5 下次约 R339**（since_evv5 于 R329 复位，+10）。
4. **MS 簇达七实体**：michel-strogoff/michael-strogoff/nadia/ivan-ogareff/marfa-strogoff/alcide-jolivet/harry-blount 互链成群；建序 72（feofar）建成后 MS 达八实体。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label 张力（R321 裁例）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R318/R329 EVV5 识别）：7 页 PN<5 + 11 页 over-400，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=269→270（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
