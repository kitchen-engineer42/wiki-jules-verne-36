---
round: 328
date: 2026-07-19
type_round: 21
phase: "2.1"
current_type: character
gene: NEW1
pages: [ivan-ogareff]
result: success
---

# GROW 2.1-B · R328 · NEW1 · character — 建 Ivan Ogareff（叛徒上校、鞑靼入侵之隐手）

## 执行摘要

Phase 2.1-B character 第 18 建（type_round 21），消费 R322 第三批 discover 队列**建序 68**（末位）——**queue(character) 归 0**。决策机 §3 首匹配 **NEW1**
（since_evv5=9<10；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。

**Ivan Ogareff**（*Michael Strogoff*）——失宠俄国军官叛国者，宫廷谓之「the traitor Ivan Ogareff」（MS-002-023）。军衔上校（MS-015-004），「terrible as any of the most savage Tartar chieftains」而「an educated soldier」（MS-015-005）。其为入侵之隐手：警长问「Ivan Ogareff has a hand in this Tartar rebellion」（MS-003-041），彼越 Ural 往「foment rebellion amongst」Kirghiz（MS-003-042）；叛乱之外更深——「is also playing the part of a traitor」、Grand Duke 之「personal enemy」（MS-003-048），而「Irkutsk was the real object of Ivan Ogareff」（MS-015-008）。为近 Grand Duke，冒 Michael Strogoff 之名——「the only name they could give to Ivan Ogareff」（MS-033-018）；至时「opened the window and stationed himself at the North angle of the side terrace」发信号（MS-033-020）。复仇为其引擎：「thirsting for vengeance」、「aims at the life of my brother」（MS-003-042）；受 knout 公辱，「not a man to forgive」、「his vengeance would be merciless」（MS-023-016）；绰号「the Scarred Cheek」、着「the uniform of a Tartar officer」（MS-023-007），冷然判死「'You shall die!'」（MS-023-038）；狡黠识破「the pretended Nicholas Korpanoff was Michael Strogoff, courier of the Czar」（MS-015-095）。

**role=antagonist**。book=Michael Strogoff、first_appearance=MS-002、affiliation 空、aliases=['The Scarred Cheek']。

**14 distinct solid PN**（MS-002-023、003-041/042/048、015-004/005/008/095、023-007/016/038、033-018/020）：均 solid，逾门。

**查重**：exact-slug ivan-ogareff filesystem + registry entity ABSENT。

**MS 2-char VVV**：无需 RFC-0003 Note。

**wikilink（同书簇）**：[[Michel Strogoff]]（R321 character）、[[Michael Strogoff]]（work）——二链均存在无悬挂。Sangarre 纯文本（未建）。MS 簇达四实体（michel-strogoff/michael-strogoff/nadia/ivan-ogareff + events）。

prose-gate：add_page 初稿 2 超段（439/570），拆段后 0 超门。**pn_validator strict 首过 ✓**（无 edit_page，quality featured 未剥离）。**aliases 首度非空**：'The Scarred Cheek'（MS-023-007 绰号），label 唯一性无冲突。

character 计数 32→**33**，registry total 1556→**1557**，unknown 恒 0。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =9 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=1>0、since_discover=5 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue(character)=1>0，按既有实践走 NEW1 消费建序 68（末位）。本轮后 queue 归 0。

## 页面处理记录

| slug | rev | book | role | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| ivan-ogareff | 6P6cY5 | Michael Strogoff | antagonist | MS-002 | 14 distinct | 叛徒上校-隐手-复仇-冒名单指；MS 2-char 无 Note；拆 2 超段；strict 首过 ✓；alias The Scarred Cheek；[[Michel Strogoff]]/[[Michael Strogoff]] 互链 |

- **ivan-ogareff**：14 distinct solid PN；aliases ['The Scarred Cheek']；character-schema 五 H2。add_page rev 6P6cY5。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Ogareff 叛徒-隐手-复仇-冒名因果；strict 首过 ✓。✔
- **G2 段落 ≤400 字**：拆段后散文段 0 超门。✔
- **G3 ≥5 distinct PN**：14 solid，逾门。✔
- **G4 脚本建页**：add_page 建页，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段；MS 2-char 无 Note。✔
- **registry 一致**：total 1557 character 33 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug + entity ABSENT；registry 无 character 冲突；alias 'The Scarred Cheek' 无碰撞。✔
- **wikilink 完整性**：Michel Strogoff/Michael Strogoff 二链存在无悬挂；Sangarre 纯文本。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R329 起始计数）

| 字段 | R328 起始 | R329 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 328 | 329 |
| type_round | 20 | 21 |
| rounds_since_last_evv5 | 9 | 10 |
| rounds_since_last_discover | 5 | 6 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 264 | 265 |
| last_updated_round | 328 | 329 |

## 遗留问题

1. **character 页数 33**：本轮 +1（ivan-ogareff）。queue(character) 1→**0**（建序 68 末位消费）。registry 全库 **1557**，unknown 0。
2. **下轮 R329 = EVV5 反射轮（§3(1b)）**：since_evv5=10≥10 → §3(1b) EVV5 优先触发（§3(1a) 需同时 since_discover≥10，此处 since_discover=6<10，故非 1a）。EVV5 为 character schema 反射轮：反思 character-schema、模板与既建 33 页共性，pages:[]，EXIT-GATE 仅 G4，since_evv5 复位 0。**注意**：EVV5 不建页、不消费 discover，queue 仍 0。
3. **R330 起 queue==0 → SCN28-zombie 第四批 discover（§3(4)）**：EVV5 后 R330 若 queue 仍 0 触发 §3(4) 勘探补给。深池尚存：SC（Robert Grant/Captain Grant）、MS（Marfa Strogoff/Sangarre/Feofar-Khan/Harry Blount/Alcide Jolivet）、DSCF（Mrs. Weldon/Cousin Benedict/Tom/Dick Sand）、单作品主角（Hector Servadac/Mathias Sandorf/Kaw-djer/Kéraban/Wilhelm Storitz/Nicholl/Hans）。第四批 ≥3 候选以保 discover_streak_low=0。
4. **MS 簇达四实体**：michel-strogoff/michael-strogoff/nadia/ivan-ogareff + events strogoff-blinding/assault-on-irkutsk 互链成群。
5. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label 归一；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label 张力（R321 裁例）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R318 EVV5 识别）：7 页 PN<5 + 11 页 over-400，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=264→265（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
