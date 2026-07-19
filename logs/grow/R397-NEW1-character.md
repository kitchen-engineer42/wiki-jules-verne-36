---
round: 397
date: 2026-07-19
type_round: 89
phase: "2.1"
current_type: character
gene: NEW1
pages: [phina-hollaney]
result: success
---

# GROW 2.1-B · R397 · NEW1 · character — 建 Phina Hollaney（Godfrey Morgan 之未婚妻、Kolderup 教女、劝行环游而于旧金山守候的恋人，终为新娘；GM 簇补 william-kolderup，第十四批建序 119，queue 2→1）

## 执行摘要

Phase 2.1-B character 第 69 建（type_round 89），消费 R395 第十四批 discover 队列**建序 119**。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=2>0 → §3(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=1（建序 120 madge 待 R398）。**

**Phina Hollaney**（*Godfrey Morgan*）——William Kolderup 之教女、Godfrey 之未婚妻，劝爱人先游世界再成婚、于旧金山守候归来，终为其新娘。初现即巨贾教女「Phina Hollaney was the goddaughter of William W. Kolderup」（GM-003-014），婚约既定「Godfrey Morgan was going to marry Phina Hollaney」（GM-003-025）。非但不阻反劝其行「the departure of Godfrey, who, before he gets married, wants to see a little of the world」（GM-003-046），力主放行「pleaded...must let Godfrey go...thought it carefully over」（GM-003-054）。善琴寄情「Phina's hand sought the key-board and rippled along a series of sinking sevenths, which spoke of a plaintive sadness」（GM-003-021），别时最镇定「Phina showed herself much the most composed」（GM-005-041）。恋人 Godfrey 流落时首念及她「his first thought was for Phina, his betrothed, whom he had so stupidly refused to make his wife」（GM-010-009），肖像随行「Phina's portrait had its allotted place in Godfrey's cabin」（GM-005-035），婚后誓言「with you, my dear husband, I fear nothing from anywhere」（GM-022-115）。教父 Kolderup 团聚「Phina and Uncle Will asked Godfrey to do the honours of his island」（GM-022-063）。Godfrey 以其名命岛「I'll call it Phina Island, in memory of her」（GM-010-062），终为新娘含笑「Phina Island... is quite uninhabitable」（GM-022-112）。

**role=supporting**。book='Godfrey Morgan'、first_appearance=GM-003、affiliation 空、**label=Phina Hollaney，aliases=[]**（Phina 系正文简称，未入 alias；phina 非 work 名，不触 HK(e) 同名风险）。

**12 distinct solid PN**（GM-003-014/021/025/046/054、005-035/041、010-009/062、022-063/112/115）：均 solid，逾门。注意 corpus 内「Phina」兼指人物与「Phina Island」（Godfrey 以其名命岛），本页仅取指人物之句。

**查重**：exact-slug phina-hollaney filesystem test -f ABSENT（bucket ph）+ registry entity/label（Phina Hollaney/Phina）ABSENT（R395 discover 已验，本轮建前复验一致）。

**GM 2-char VVV**：无需 RFC-0003 Note。

**wikilink**：[[William W. Kolderup]]（character，R394 建，GM-022-063）/ [[Godfrey Morgan]]（work，存，GM-010-062）——二链互链无悬挂。Godfrey（角色页未建）以正文明指、不设悬挂链。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 83→**84**，registry total 1607→**1608**，unknown 恒 0。build_registry 3 alias warn（均 parked HK；本次 tail 显 1）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=2、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue(character)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *since_discover=1<10、queue=2>0 → NEW1 消费建序 119。消费后 queue=1。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| phina-hollaney | iuFL07 | Godfrey Morgan | supporting | GM-003 | 12 distinct | 巨贾教女-婚约既定-劝行环游-力主放行-善琴寄情-别时最镇定-恋人首念-肖像随行-婚后誓言-教父团聚-以其名命岛-终为新娘；label Phina Hollaney + aliases 空；Phina/Phina Island 消歧仅取指人物句；GM 2-char 无 Note；0 超段直建；strict 首验通过；互链 [[William W. Kolderup]]/[[Godfrey Morgan]] |

- **phina-hollaney**：12 distinct solid PN；aliases []；character-schema 五 H2。add_page rev iuFL07（size 2172）。quality featured 回填。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Phina 教女-婚约-劝行-善琴-守候-新娘因果；Phina Island 消歧后仅取指人物句；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用，路径正确），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book/description 单引号）；role=supporting ∈ enum；GM 2-char 无 Note。✔
- **registry 一致**：total 1608 character 84 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label ABSENT；registry 无 character 冲突（label Phina Hollaney 唯一）。✔
- **wikilink 完整性**：William W. Kolderup / Godfrey Morgan 二链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R398 起始计数）

| 字段 | R397 起始 | R398 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 397 | 398 |
| type_round | 89 | 90 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 333 | 334 |
| last_updated_round | 397 | 398 |

## 遗留问题

1. **character 页数 84**：本轮 +1（phina-hollaney）。queue(character) 2→**1**（建序 119 消费）。registry 全库 **1608**，unknown 0。
2. **下轮 R398 = NEW1（§3(7)）**：since_evv5=4<10 → §3(1) 否；discover_streak_low=0<3；queue(character)=1>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 120（madge，book The Fur Country，pn_anchor FC-001，role supporting）。**消费后 queue 归 0 → R399 = §3(4) SCN28-zombie 补第十五批。下次 EVV5 于 R403 起始达 since_evv5=10。**
3. **第十四批余 1 候选（建序 120）**：madge，R398 NEW1 消费 → queue 归 0 → R399 SCN28-zombie。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + william-kolderup→Phina Hollaney、paulina-barnett/lieutenant-hobson→Kalumah、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan——若后建 Godfrey 角色页则触发新同名冲突，暂缓）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R393 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=333→334（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
