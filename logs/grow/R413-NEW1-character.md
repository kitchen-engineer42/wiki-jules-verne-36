---
round: 413
date: 2026-07-19
type_round: 105
phase: "2.1"
current_type: character
gene: NEW1
pages: [marbre]
result: success
---

# GROW 2.1-B · R413 · NEW1 · character — 建 Marbre（The Fur Country 之首席猎手、与 Sabine 并肩之加拿大猎人、最先窥破浮岛之危的老猎手；完成 FC 猎手二人组，第十八批建序 130，queue 3→2）

## 执行摘要

Phase 2.1-B character 第 80 建（type_round 105），消费 R412 第十八批 discover 队列**建序 130（首候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=8<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=3>0 且 since_discover=0<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=2**（建序 131-132 待 R414-R415 消费；但 R415 起始 since_evv5=10 或触发 EVV5，则 132 顺延）。

**Marbre**（*The Fur Country*）——探险队之首席猎手、与 Sabine 并肩之加拿大猎人、最先窥破浮岛之危的老猎手。首席猎手「the chief hunters of the expedition were the soldiers Marbre and Sabine, both very expert at their business」（FC-006-024），入选精兵「two--Marbre and Sabine--were skilful hunters」（FC-013-004），剥皮而归「Marbre and Sabine taking immediate possession, carried off their skins」（FC-006-057），四季供给「Sabine and Marbre killed a good many Polar hares」（FC-020-002）。最先知危「Marbre, upon whom the truth had first dawned, confided his suspicions to Mac-Nab the carpenter and Rae the blacksmith」（FC-035-005），面陈长官「the hunter Marbre approached Hobson, and said to him in a significant tone」（FC-028-021），所报重大「Marbre's tidings were of grave importance」（FC-028-036）。老猎难欺「old trappers like us are not to be taken in」（FC-006-033），惜用弹药「spare our powder and shot」（FC-006-042），谙于诡术「skilled in all the artifices which sportsmen employ in stalking their prey」（FC-014-014），献策设阱「in accordance with the advice of Marbre the hunter, a reindeer trap was constructed」（FC-019-003），料敌如神「I know well enough what creature has fallen into our pit」（FC-019-009），掷索擒兽「Marbre flung his running noose skilfully over its neck and pulled it tightly」（FC-037-020）。

**role=supporting**。book='The Fur Country'、first_appearance=FC-006、affiliation 空、**label=Marbre，aliases=[]**。

**14 distinct solid PN**（FC-006-024/033/042/057、013-004、014-014、019-003/009、020-002、028-011/021/036、035-005、037-020）：均 solid，逾门。「Marbre」FC 内单指本人（探险队猎人）；「Marbre and Sabine」并称句取其明指 Marbre 属性/言行者。

**查重**：exact-slug marbre filesystem test -f ABSENT（bucket ma）+ registry entity/label/alias 复验——「Marbre」无既建人物页，无冲突。

**FC 2-char VVV**：无需 RFC-0003 Note（仅 4-char 触发）。

**wikilink**：[[Sabine]]（sabine，R410 既建）、[[Jaspar Hobson]]（lieutenant-hobson，既建）、[[Mac-Nab]]（mac-nab，R406 既建）、[[The Fur Country]]（work，存）——四链均无悬挂。**Rae the blacksmith 页未建**：Relationships/正文以明指之 plain-text（PN grounded FC-035-005，不设悬挂链）。**FC 猎手二人组收束**（sabine/marbre 齐备，互链）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 94→**95**，registry total 1618→**1619**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=3、since_discover=0 | 否* |
| 4 | SCN28-zombie（queue==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=3>0 → NEW1 消费建序 130。消费后 queue=2，R414-R415 续消费 131-132。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| marbre | KEU0WC | The Fur Country | supporting | FC-006 | 14 distinct | 首席猎手-入选精兵-剥皮而归-四季供给-最先知危-面陈长官-所报重大-老猎难欺-惜用弹药-谙于诡术-献策设阱-料敌如神-掷索擒兽；label Marbre；FC 2-char 无 Note；0 超段直建；strict 首验通过；四链 [[Sabine]]/[[Jaspar Hobson]]/[[Mac-Nab]]/[[The Fur Country]]（Rae 未建作 plain-text）；FC 猎手二人组收束 |

- **marbre**：14 distinct solid PN；aliases []；character-schema 五 H2。add_page rev KEU0WC（size 2742）。quality featured 回填。pn_validator --mode strict ✓。**FC 猎手二人组收束（sabine+marbre）；Marbre 并称句消歧取明指 Marbre 者。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Marbre 猎人-知危-老练因果；「Marbre and Sabine」并称句取明指 Marbre 属性/言行者；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：14 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book/description 单引号）；role=supporting ∈ enum；FC 2-char 无 Note。✔
- **registry 一致**：total 1619 character 95 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Sabine + Jaspar Hobson + Mac-Nab + The Fur Country 四链存在无悬挂；Rae 未建作 plain-text 不悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R414 起始计数）

| 字段 | R413 起始 | R414 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 413 | 414 |
| type_round | 105 | 106 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 349 | 350 |
| last_updated_round | 413 | 414 |

## 遗留问题

1. **character 页数 95**：本轮 +1（marbre）。queue(character) 3→**2**（建序 130 消费）。registry 全库 **1619**，unknown 0。
2. **下轮 R414 = NEW1（§3(7)）**：since_evv5=9<10；queue=2>0 且 since_discover=1<10 → NEW1，消费建序 131 **saknussemm**（JCE，JCE-003，supporting，43 mentions；十六世纪冰岛炼金术士、符文密码先行者；可回链 [[Professor Lidenbrock]]/[[Axel]]）。
3. **第十八批消费**：R413 NEW1（130 marbre ✓）→ R414 NEW1（131 saknussemm）→ queue=1 → **R415 起始 since_evv5=10 → §3(1b) EVV5**（不消费队列）→ R416 NEW1 消费 132 grauben → queue 归 0 → R417 SCN28-zombie 补第十九批。**EVV5 时点确认**：since_evv5 R414 起始=9 → R415 起始=10 → **R415 = EVV5**。
4. **回链回填债**（DEFERRED，非阻塞）：**FC 猎手二人组本轮互链已成**（marbre→sabine，反向 sabine→marbre 待回填）；marbre→mac-nab/lieutenant-hobson 反向、Rae 待建、fridrikssen 反向链、samuel-fergusson/dick-kennedy→joe 反向、Mrs Mac-Nab 待建、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R404 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R415 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=349→350（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
