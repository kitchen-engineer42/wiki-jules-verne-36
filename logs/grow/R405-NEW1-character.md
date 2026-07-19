---
round: 405
date: 2026-07-19
type_round: 97
phase: "2.1"
current_type: character
gene: NEW1
pages: [samuel-fergusson]
result: success
---

# GROW 2.1-B · R405 · NEW1 · character — 建 Samuel Ferguson（Five Weeks in a Balloon 之博学探险家、Victoria 号主帅，气球横越非洲之谋主；FWB 簇第二页、首个 protagonist，第十六批建序 124，queue 3→2）

## 执行摘要

Phase 2.1-B character 第 74 建（type_round 97），消费 R403 第十六批 discover 队列**建序 124（首候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=0<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=3>0 且 since_discover=1<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=2**（建序 125-126 待 R406-R407 消费）。

**Samuel Ferguson**（*Five Weeks in a Balloon*）——博学探险家、Victoria 号之主帅，气球横越非洲之谋主。少历环球「Samuel Ferguson, then twenty-two years of age, had already made his voyage around the world」（FWB-001-030），航海世家「Ferguson's father, a brave and worthy captain in the English Navy, had associated his son with him」（FWB-001-027）。壮举之主「the daring project of Dr. Samuel Ferguson, whose fine explorations our readers have frequently had the opportunity of appreciating」（FWB-002-005），远征之首「if Ferguson was the head and Kennedy the arm」（FWB-006-006），亲督其备「energetically pushed the preparations for his departure, and in person superintended the construction of his balloon」（FWB-005-002），升空同别「Ferguson, Kennedy, and Joe, waved a last good-by to their friends」（FWB-011-041）。铜心壮胆「the energetic character of Dr. Ferguson, and the heart, thrice panoplied in bronze」（FWB-002-013），躁静相衬「a restless spirit personified in Ferguson; perfect calmness typified in Kennedy」（FWB-003-009），迎难而进「as for difficulties, they were made to be overcome」（FWB-003-057），巧思发明「by an ingenious arrangement, combined the advantages of two balloons」（FWB-007-010），临险持重「Dr. Ferguson prudently kept her above the reach of the barbarian arrows」（FWB-012-038），体魄坚韧「Ferguson's constitution continued marvellously sound」（FWB-001-033）。

**role=protagonist**（FWB 主角，破自 R382 起全 supporting 单调）。book='Five Weeks in a Balloon'、first_appearance=FWB-001、affiliation 空、**label=Samuel Ferguson，aliases=['Dr. Ferguson']**。

**13 distinct solid PN**（FWB-001-027/030/033、002-005/013、003-009/057、005-002、006-006、007-010、008-010、011-041、012-038）：均 solid，逾门（≥5，达 standard 12+ 实践）。「Ferguson」/「Dr. Ferguson」/「Samuel Ferguson」FWB 内单指本人，取明确指涉句。

**查重**：exact-slug samuel-fergusson filesystem test -f ABSENT（bucket sa）+ registry entity/label 复验——「Ferguson」仅命中 victoria-balloon 之 alias「Ferguson's balloon」（气球实体，非人物），无同一人物页；Samuel Ferguson/Dr. Ferguson 作 character label ABSENT。**alias 教训延续**：R403 pierre-aronnax→aronnax、R399 pan-chao label、R386 count-dartigas=ker-karraje——本轮 registry label 并查确认无既建人物。

**FWB 3-char VVV**：无需 RFC-0003 Note（仅 4-char 触发）。

**wikilink**：[[Dick Kennedy]]（R402 既建，双向补链）、[[Five Weeks in a Balloon]]（work→five-weeks-in-a-balloon，存）——均无悬挂。**Joe 角色页未建**：Relationships bullet 以正文明指之 plain-text（PN grounded FWB-006-006，不设悬挂链），俟后建再回链。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 88→**89**，registry total 1612→**1613**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=3、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=3>0 → NEW1 消费建序 124。消费后 queue=2，R406-R407 续消费 125-126。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| samuel-fergusson | OycKCg | Five Weeks in a Balloon | protagonist | FWB-001 | 13 distinct | 少历环球-航海世家-壮举之主-远征之首-亲督其备-升空同别-铜心壮胆-躁静相衬-迎难而进-巧思发明-临险持重-体魄坚韧；label Samuel Ferguson + aliases [Dr. Ferguson]；FWB 3-char 无 Note；0 超段直建；strict 首验通过；双链 [[Dick Kennedy]]/[[Five Weeks in a Balloon]]（Joe 未建作 plain-text）|

- **samuel-fergusson**：13 distinct solid PN；aliases [Dr. Ferguson]；character-schema 五 H2。add_page rev OycKCg（size 3059）。quality featured 回填。pn_validator --mode strict ✓。**FWB 簇第二页、首个 protagonist（破全 supporting 单调）。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Ferguson 主帅-谋主-发明-持重因果；单称 Ferguson/Dr. Ferguson 消歧后取明确指涉句；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book/description 单引号）；role=protagonist ∈ enum；FWB 3-char 无 Note。✔
- **registry 一致**：total 1613 character 89 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label ABSENT（「Ferguson」仅命中 victoria-balloon 气球 alias，非人物）。✔
- **wikilink 完整性**：Dick Kennedy + Five Weeks in a Balloon 双链存在无悬挂；Joe 未建作 plain-text 不悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R406 起始计数）

| 字段 | R405 起始 | R406 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 405 | 406 |
| type_round | 97 | 98 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 341 | 342 |
| last_updated_round | 405 | 406 |

## 遗留问题

1. **character 页数 89**：本轮 +1（samuel-fergusson）。queue(character) 3→**2**（建序 124 消费）。registry 全库 **1613**，unknown 0。
2. **下轮 R406 = NEW1（§3(7)）**：since_evv5=1<10；queue=2>0 且 since_discover=2<10 → NEW1，消费建序 125 **mac-nab**（FC，FC-001，supporting，93 mentions；探险队苏格兰木匠工头、Fort Hope 营建主力；补 FC 簇）。
3. **第十六批消费**：R405 NEW1（124 samuel-fergusson ✓）→ R406 NEW1（125 mac-nab）→ R407 NEW1（126 hans-bjelke）→ queue 归 0 → R408 SCN28-zombie 补第十七批。
4. **回链回填债**（DEFERRED，非阻塞）：**dick-kennedy↔samuel-fergusson 本轮单向已链**（samuel→dick-kennedy），dick-kennedy→samuel-fergusson 反向待回填；Joe 待建双向；william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。JCE hans-bjelke（待建）可回链 professor-lidenbrock/axel。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R404 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R414 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=341→342（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
