---
round: 409
date: 2026-07-19
type_round: 101
phase: "2.1"
current_type: character
gene: NEW1
pages: [joe]
result: success
---

# GROW 2.1-B · R409 · NEW1 · character — 建 Joe（Five Weeks in a Balloon 之 Ferguson 忠仆兼远征「右手」、机敏乐天的随行侍从；收束气球远征三人组，第十七批建序 127，queue 3→2）

## 执行摘要

Phase 2.1-B character 第 77 建（type_round 101），消费 R408 第十七批 discover 队列**建序 127（首候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=3>0 且 since_discover=0<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=2**（建序 128-129 待 R410-R411 消费）。

**Joe**（*Five Weeks in a Balloon*）——Ferguson 之忠仆兼远征「右手」、机敏乐天的随行侍从。侍从之名「Dr. Ferguson had a servant who answered with alacrity to the name of Joe」（FWB-006-002），远征右手「if Ferguson was the head and Kennedy the arm, Joe was to be the right hand of the expedition」（FWB-006-006），忠贞不贰「Joe will always stick to the doctor!」（FWB-006-020），巧解锚缆「thanks to a skilful manoeuvre achieved by Joe, the anchor was disengaged」（FWB-013-008），共担值守「the three o'clock morning watch」（FWB-012-071），升空同别「Ferguson, Kennedy, and Joe, waved a last good-by to their friends」（FWB-011-041）。身手矫捷「Joe would certainly have received the appointment」（FWB-006-005，体操教授之喻），敏捷下树「slipping nimbly down the tree」（FWB-013-054），人皆爱之「every body liked him for his frankness and good-humor」（FWB-009-004），欢腾雀跃「fairly dancing and breaking out in laughable remarks」（FWB-008-008），微役亦乐「as proud and happy as a prince」（FWB-011-037）。

**role=supporting**。book='Five Weeks in a Balloon'、first_appearance=FWB-006、affiliation 空、**label=Joe，aliases=[]**。

**14 distinct solid PN**（FWB-006-002/003/005/006/020、008-008、009-004、011-037/041、012-033/071、013-008/054/055）：均 solid，逾门。**消歧执行**（queue discover-note 警示）：「Joe」FWB 531 mentions 极高，本页严格取明指 Ferguson 侍从 Joe 之句（其言行、身份、旁白描述），排除对话中泛称他人之句。

**查重**：exact-slug joe filesystem test -f ABSENT（bucket jo）+ registry entity/label/alias 复验——「Joe」无既建人物页，无冲突。

**FWB 3-char VVV**：无需 RFC-0003 Note（仅 4-char 触发）。

**wikilink**：[[Samuel Ferguson]]（R405 既建）、[[Dick Kennedy]]（R402 既建）、[[Five Weeks in a Balloon]]（work，存）——三链均无悬挂。**FWB 气球远征三人组收束**（fergusson/kennedy/joe 三页齐备，互链成簇）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 91→**92**，registry total 1615→**1616**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=3、since_discover=0 | 否* |
| 4 | SCN28-zombie（queue==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=3>0 → NEW1 消费建序 127。消费后 queue=2，R410-R411 续消费 128-129。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| joe | RkyCoh | Five Weeks in a Balloon | supporting | FWB-006 | 14 distinct | 侍从之名-远征右手-忠贞不贰-巧解锚缆-共担值守-升空同别-身手矫捷-敏捷下树-人皆爱之-欢腾雀跃-微役亦乐；label Joe；FWB 3-char 无 Note；0 超段直建；strict 首验通过；三链 [[Samuel Ferguson]]/[[Dick Kennedy]]/[[Five Weeks in a Balloon]]（气球三人组收束）；531 mentions 严格消歧取明指侍从句 |

- **joe**：14 distinct solid PN；aliases []；character-schema 五 H2。add_page rev RkyCoh（size 2356）。quality featured 回填。pn_validator --mode strict ✓。**FWB 气球远征三人组收束；531 高频 mentions 消歧执行到位。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Joe 侍从-右手-矫捷-忠贞因果；531 高频 mentions 消歧后严格取明指 Ferguson 侍从之句，排除对话泛称；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：14 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book/description 单引号）；role=supporting ∈ enum；FWB 3-char 无 Note。✔
- **registry 一致**：total 1616 character 92 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Samuel Ferguson + Dick Kennedy + Five Weeks in a Balloon 三链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R410 起始计数）

| 字段 | R409 起始 | R410 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 409 | 410 |
| type_round | 101 | 102 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 345 | 346 |
| last_updated_round | 409 | 410 |

## 遗留问题

1. **character 页数 92**：本轮 +1（joe）。queue(character) 3→**2**（建序 127 消费）。registry 全库 **1616**，unknown 0。
2. **下轮 R410 = NEW1（§3(7)）**：since_evv5=5<10；queue=2>0 且 since_discover=1<10 → NEW1，消费建序 128 **sabine**（FC，FC-004，supporting，54 mentions；探险队加拿大猎人、觅食队主力射手；补 FC 簇）。
3. **第十七批消费**：R409 NEW1（127 joe ✓）→ R410 NEW1（128 sabine）→ R411 NEW1（129 fridrikssen）→ queue 归 0 → R412 SCN28-zombie 补第十八批。**EVV5 时点**：since_evv5 R410 起始=5，逐轮 +1 → R415 起始=10 → **R415 = §3(1b) EVV5**。
4. **回链回填债**（DEFERRED，非阻塞）：**FWB 气球三人组本轮互链已成**（joe→samuel-fergusson/dick-kennedy，反向待回填 samuel-fergusson/dick-kennedy→joe）；Mrs Mac-Nab 待建、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R404 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R415 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=345→346（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
