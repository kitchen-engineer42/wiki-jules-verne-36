---
round: 334
date: 2026-07-19
type_round: 27
phase: "2.1"
current_type: character
gene: NEW1
pages: [feofar-khan]
result: success
---

# GROW 2.1-B · R334 · NEW1 · character — 建 Feofar-Khan（Bukhara 埃米尔、鞑靼入侵首领）

## 执行摘要

Phase 2.1-B character 第 22 建（type_round 27），消费 R330 第四批 discover 队列**建序 72**。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**Feofar-Khan**（*Michael Strogoff*）——Bukhara 埃米尔、鞑靼入侵之名义首领，「The present chief, Feofar-Khan, followed in the steps of his predecessors」（MS-003-063），「the fierce and ambitious Feofar now governed this corner of Tartary」（MS-003-065）；蔑称沙皇「designat[ing] the Emperor of Russia by this strange title」（MS-021-034）。营中候其副手 Ogareff「Feofar-Khan was expecting his lieutenant」（MS-021-024），以独裁者之简慢听命「'I have no need to question you,' said he; 'speak, Ivan'」（MS-021-028）；其召令起草原「the Kirghiz hordes rose at the voice of Feofar-Khan」（MS-021-029）。Tomsk 城下以蛮华出巡「Feofar mounted his favorite horse, which carried on its head an aigrette of diamonds」（MS-023-004），朝众叹其「magnificence ... and all the Eastern pomp」（MS-023-010）。凶相毕露「a man of forty, tall, rather pale, of a fierce countenance, and evil eyes」（MS-021-025）；怒斥俘囚「in a voice trembling with fury」（MS-023-046）、判刑「'Look while you may,' exclaimed Feofar-Kahn」（MS-024-002）；其刽子手「carried out the sentences of Feofar-Khan against offenders」（MS-024-010），斥 Michael 为奸细「You came to see our goings out and comings in, Russian spy」（MS-024-040），判「not death, but blindness」（MS-024-041）。

**role=antagonist**。book=Michael Strogoff、first_appearance=MS-003、affiliation 空、aliases 空。

**14 distinct solid PN**（MS-003-063/065、021-024/025/028/029/034、023-004/010/046、024-002/010/040/041）：均 solid，逾门。

**查重**：exact-slug feofar-khan filesystem + registry entity ABSENT。

**MS 2-char VVV**：无需 RFC-0003 Note。

**wikilink（同书簇）**：[[Ivan Ogareff]]（R328）、[[Michel Strogoff]]（R321）、[[Michael Strogoff]]（work）——三链均存在无悬挂。queue 备注「event the-sentence-of-feofar-khan 可互链」经查该 event 页**不存在**，为避免悬挂本轮不链。

prose-gate：add_page 初稿 Overview/Character 两超段，拆段后仍余 Overview 403，edit_page rev BKjmPq 再拆 Overview 为二段后 0 超门。**引注**：strict 首验即通过，无需引注修正。quality featured 未剥离。

character 计数 36→**37**，registry total 1560→**1561**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=3>0、since_discover=3 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=3>0，按既有实践走 NEW1 消费建序 72。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| feofar-khan | BKjmPq | Michael Strogoff | antagonist | MS-003 | 14 distinct | Bukhara 埃米尔-入侵名义首领-受 Ogareff 命-判 Michael 目盲；MS 2-char 无 Note；拆 3 超段（含 edit_page 补拆 Overview）；strict 首验通过；event 页缺不链；[[Ivan Ogareff]]/[[Michel Strogoff]]/[[Michael Strogoff]] 互链 |

- **feofar-khan**：14 distinct solid PN；aliases 空；character-schema 五 H2。add_page rev 8W9Heu→edit_page rev BKjmPq。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Feofar 入侵首领-受命-判刑因果；strict ✓。✔
- **G2 段落 ≤400 字**：edit_page 补拆后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：14 solid，逾门。✔
- **G4 脚本建页**：add_page/edit_page 建页改页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；MS 2-char 无 Note。✔
- **registry 一致**：total 1561 character 37 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Ivan Ogareff/Michel Strogoff/Michael Strogoff 三链存在无悬挂；feofar event 页缺不链。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R335 起始计数）

| 字段 | R334 起始 | R335 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 334 | 335 |
| type_round | 26 | 27 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 270 | 271 |
| last_updated_round | 334 | 335 |

## 遗留问题

1. **character 页数 37**：本轮 +1（feofar-khan）。queue(character) 3→**2**（建序 72 消费；余 73-74：captain-grant/robert-grant，均 SC 簇）。registry 全库 **1561**，unknown 0。
2. **下轮 R335 = NEW1（§3(7)）**：since_evv5=5<10；queue(character)=2>0 → §3(7) NEW1，消费建序 73（captain-grant）。Captain Grant（book In Search of the Castaways，pn_anchor SC-001，role supporting，SC 2-char 无 Note）——失踪苏格兰船长、瓶中文书所寻之人、Mary/Robert 之父；与 mary-grant/robert-grant/glenarvan 可互链。
3. **EVV5 下次约 R339**（since_evv5 于 R329 复位，+10）。
4. **MS 簇达八实体**：michel-strogoff/michael-strogoff/nadia/ivan-ogareff/marfa-strogoff/alcide-jolivet/harry-blount/feofar-khan 互链成群，MS 簇本轮达成八实体规模。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label 张力（R321 裁例）。新增观察：queue 备注引用的 event the-sentence-of-feofar-khan 页不存在，如日后建该 event 可回链 feofar-khan（非 HK，仅记录）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R318/R329 EVV5 识别）：7 页 PN<5 + 11 页 over-400，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=270→271（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
