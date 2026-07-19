---
round: 402
date: 2026-07-19
type_round: 94
phase: "2.1"
current_type: character
gene: NEW1
pages: [dick-kennedy]
result: success
---

# GROW 2.1-B · R402 · NEW1 · character — 建 Dick Kennedy（Five Weeks in a Balloon 之苏格兰猎手、Ferguson 挚友，勉从气球横越非洲之神射手；FWB 新簇首个人物页，第十五批建序 123，queue 1→0）

## 执行摘要

Phase 2.1-B character 第 73 建（type_round 94），消费 R399 第十五批 discover 队列**建序 123（末候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=0 → R403 = §3(4) SCN28-zombie 补第十六批。**

**EVV5 时点更正**：stored `since_evv5`（grow_state 内、§3 实读之权威计数）R402 起始=8，逐轮 +1 → R403 起始=9（<10）、R404 起始=10（≥10 触发 §3(1b) EVV5）。故 R403 非 EVV5，而系 queue==0 之 SCN28-zombie；R404 方为 EVV5。此更正既往 R399-R401 日志「遗留问题」中「R403 EVV5」之前瞻误注（各轮实际 gene 由运行时 grow_state 判定，功能无碍）。

**Dick Kennedy**（*Five Weeks in a Balloon*）——苏格兰猎手、Ferguson 挚友，勉从气球横越非洲之神射手。挚谊同心「Dick Kennedy and Samuel Ferguson lived with one and the same heart」（FWB-003-003），苏人本色「a Scotchman, in the full acceptation of the word--open, resolute, and headstrong」（FWB-003-004），远征之臂「if Ferguson was the head and Kennedy the arm, Joe was to be the right hand of the expedition」（FWB-006-006）。虽阻其谋而忠随「go with you up to the last moment, to prevent Samuel even then from being guilty of such an act of folly」（FWB-006-023），升空同别「Ferguson, Kennedy, and Joe, waved a last good-by to their friends」（FWB-011-041）。沉静反衬「perfect calmness typified in Kennedy--such was the contrast」（FWB-003-009），初闻愕然「Kennedy stood speechless with amazement」（FWB-003-041），终为壮景所动「the stubborn Kennedy began to feel moved...gave him the vertigo」（FWB-003-067），神射猎手「descried some hares and quails...a good shot from his fowling-piece」（FWB-012-039），执拗如故「I am not going to let myself be weighed」（FWB-006-033）。共室随行「two state-rooms, comfortably fitted up, were ready for the reception of Dr. Ferguson and his friend Kennedy」（FWB-008-007），受誉勇伴「the no less courageous Kennedy, his daring companion」（FWB-008-010）。

**role=supporting**。book='Five Weeks in a Balloon'、first_appearance=FWB-003、affiliation 空、**label=Dick Kennedy，aliases=[]**。

**12 distinct solid PN**（FWB-003-003/004/009/041/067、006-006/023/033、008-007/010、011-041、012-039）：均 solid，逾门。「Kennedy」/「Mr. Kennedy」/「Dick」FWB 内单指本人，取明确指涉句。

**查重**：exact-slug dick-kennedy filesystem test -f ABSENT（bucket di）+ registry entity/label（Dick Kennedy/Kennedy）ABSENT（R399 discover 已验，本轮建前复验一致）。

**FWB 3-char VVV**：无需 RFC-0003 Note（仅 4-char 触发）。

**wikilink**：[[Five Weeks in a Balloon]]（work→five-weeks-in-a-balloon，存，FWB-008-010）——单链无悬挂。**Ferguson/Joe 角色页未建**：Relationships 二 bullet 以正文明指之 plain-text（PN grounded，不设悬挂链），俟后建再回链。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 87→**88**，registry total 1611→**1612**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=1、since_discover=2 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=2<10、queue=1>0 → NEW1 消费建序 123。消费后 queue=0 → R403 SCN28-zombie。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| dick-kennedy | NYA7pO | Five Weeks in a Balloon | supporting | FWB-003 | 12 distinct | 挚谊同心-苏人本色-远征之臂-忠随-升空同别-沉静反衬-初闻愕然-为壮景所动-神射猎手-执拗如故-共室随行-受誉勇伴；label Dick Kennedy + aliases 空；FWB 3-char 无 Note；0 超段直建；strict 首验通过；单链 [[Five Weeks in a Balloon]]（Ferguson/Joe 未建作 plain-text）|

- **dick-kennedy**：12 distinct solid PN；aliases []；character-schema 五 H2。add_page rev NYA7pO（size 2420）。quality featured 回填。pn_validator --mode strict ✓。**FWB 新簇首个人物页。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Kennedy 猎手-挚友-远征之臂-沉静-忠随因果；单称 Kennedy/Dick 消歧后取明确指涉句；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用，路径正确），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book/description 单引号）；role=supporting ∈ enum；FWB 3-char 无 Note。✔
- **registry 一致**：total 1612 character 88 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label ABSENT；registry 无 character 冲突（label Dick Kennedy 唯一）。✔
- **wikilink 完整性**：Five Weeks in a Balloon 单链存在无悬挂；Ferguson/Joe 未建作 plain-text 不悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R403 起始计数）

| 字段 | R402 起始 | R403 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 402 | 403 |
| type_round | 94 | 95 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 338 | 339 |
| last_updated_round | 402 | 403 |

## 遗留问题

1. **character 页数 88**：本轮 +1（dick-kennedy）。queue(character) 1→**0**（建序 123 消费，第十五批全数消费完毕）。registry 全库 **1612**，unknown 0。
2. **下轮 R403 = SCN28-zombie（§3(4)）**：since_evv5=9<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**，补第十六批候选（≥3），since_discover 归零。**R404 起始 since_evv5=10 → §3(1b) EVV5（pages:[]，不消费队列）。**
3. **第十五批全数消费**（建序 121-123：thomas-black/taskinar/dick-kennedy）R400-R402 NEW1 消费完毕，queue 归 0。R403 SCN28-zombie 补第十六批。**候选池提示**：nicholl（FEM/RM/TT 多值 book HK(d) 暂缓）；FWB 新簇可续挖 samuel-fergusson（Fergusson，气球远征主角）、joe（Ferguson 仆从、远征「右手」）；FC 余 mac-nab/corporal-joliffe/marbre/sabine；建前须 filesystem+registry 复验，避单作品集中。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + dick-kennedy↔（Ferguson/Joe 待建）、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT 即此类）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan——若后建 Godfrey 角色页则触发新同名冲突，暂缓）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R393 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=338→339（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
