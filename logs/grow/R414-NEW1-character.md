---
round: 414
date: 2026-07-19
type_round: 106
phase: "2.1"
current_type: character
gene: NEW1
pages: [saknussemm]
result: success
---

# GROW 2.1-B · R414 · NEW1 · character — 建 Arne Saknussemm（A Journey to the Center of the Earth 之十六世纪冰岛炼金术士、以符文密码指引地心之路的先行者；第十八批建序 131，queue 2→1）

## 执行摘要

Phase 2.1-B character 第 81 建（type_round 106），消费 R412 第十八批 discover 队列**建序 131（次候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=9<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=2>0 且 since_discover=1<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=1**（建序 132 grauben 待消费）；**R415 起始 since_evv5=10 → R415 = §3(1b) EVV5（不消费队列）→ grauben 顺延至 R416 NEW1 消费。**

**Arne Saknussemm**（*A Journey to the Center of the Earth*）——十六世纪冰岛炼金术士、以符文密码指引地心之路的先行者。博学之士「was a very well-informed man」用拉丁文书写「currently adopted by the choice spirits of the sixteenth century」（JCE-003-035），因异端受迫「persecuted for heresy, and in 1573 his books were burned by the hands of the common hangman」（JCE-010-029）。密码藏秘「this Saknussemm concealed under his cryptogram some surprising invention」（JCE-003-022），羊皮危卷「not only the paper but Saknussemm's parchment」（JCE-004-030），指路名言「Descend, bold traveller, into the crater of the jokul of Sneffels... which I have done, Arne Saknussemm」（JCE-005-050）。先行之踪「of the three ways open before us, one had been taken by Saknussemm」（JCE-016-035），循其所示「the road that Saknussemm has shown us」（JCE-033-015）。巧护发现「the ingenious care with which Saknussemm guarded and defined his discovery」（JCE-006-042），后世灯塔「a whole army of geologists would be ready to rush into the footsteps of Arne Saknussemm」（JCE-006-010），石刻花押「'A. S.,' shouted my uncle. 'Arne Saknussemm!'」（JCE-039-052），海角留名「Cape Saknussemm」（JCE-040-004），生还先例「many years have elapsed since the return of Saknussemm to the surface」（JCE-040-030）。

**role=supporting**。book='A Journey to the Center of the Earth'、first_appearance=JCE-003、affiliation 空、**label=Arne Saknussemm，aliases=['Saknussemm']**。

**13 distinct solid PN**（JCE-003-022/035、004-030、005-050、006-010/042、010-029、016-035、033-015、039-052、040-003/004/030）：均 solid，逾门。「Saknussemm / Arne Saknussemm」JCE 内单指本人（先行炼金术士）；无消歧冲突。

**查重**：exact-slug saknussemm filesystem test -f ABSENT（bucket sa）+ registry entity/label/alias 复验——「Arne Saknussemm / Saknussemm」无既建人物页，无冲突。

**JCE 3-char VVV**：无需 RFC-0003 Note（仅 4-char 触发）。

**wikilink**：[[Professor Lidenbrock]]（professor-lidenbrock，既建）、[[Axel]]（axel，既建）、[[A Journey to the Center of the Earth]]（work，存）——三链均无悬挂。**JCE 簇再拓**（saknussemm 补入 lidenbrock/axel/hans-bjelke/fridrikssen）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 95→**96**，registry total 1619→**1620**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =9 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=2、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=2>0 → NEW1 消费建序 131。消费后 queue=1；R415 起始 since_evv5=10 → EVV5（不消费）→ R416 消费 132。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| saknussemm | vNvG4U | A Journey to the Center of the Earth | supporting | JCE-003 | 13 distinct | 博学之士-因异端受迫-密码藏秘-羊皮危卷-指路名言-先行之踪-循其所示-巧护发现-后世灯塔-石刻花押-海角留名-生还先例；label Arne Saknussemm aliases[Saknussemm]；JCE 3-char 无 Note；0 超段直建；strict 首验通过；三链 [[Professor Lidenbrock]]/[[Axel]]/[[A Journey to the Center of the Earth]] |

- **saknussemm**：13 distinct solid PN；aliases ['Saknussemm']；character-schema 五 H2。add_page rev vNvG4U（size 2633）。quality featured 回填。pn_validator --mode strict ✓。**JCE 簇再拓；Saknussemm 单指无消歧冲突。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Saknussemm 先行者-密码-遗踪因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号 / description 双引号含撇号）；role=supporting ∈ enum；JCE 3-char 无 Note。✔
- **registry 一致**：total 1620 character 96 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Professor Lidenbrock + Axel + A Journey to the Center of the Earth 三链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R415 起始计数）

| 字段 | R414 起始 | R415 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 414 | 415 |
| type_round | 106 | 107 |
| rounds_since_last_evv5 | 9 | 10 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 350 | 351 |
| last_updated_round | 414 | 415 |

## 遗留问题

1. **character 页数 96**：本轮 +1（saknussemm）。queue(character) 2→**1**（建序 131 消费）。registry 全库 **1620**，unknown 0。
2. **下轮 R415 = EVV5（§3(1b)）**：**since_evv5=10≥10 → §3(1b) EVV5 触发**（since_discover=2<10，故非 §3(1a) 合并轮）。EVV5 为 schema-reflection 轮：遍历全部 character 页（本轮起 96 页），pages:[]，仅 G4，**不消费队列**，since_evv5 归 0。扫 3 结构指标（五 H2 精确匹配 / role∈enum / book 非空）+ 追踪 2 内容债（≥5 distinct PN、prose ≤400）。**注意 role 存于 frontmatter，须解析 .md `^role:`，勿用 registry v.get('role')（空 = 假阳性）。**
3. **第十八批消费**：R413 NEW1（130 marbre ✓）→ R414 NEW1（131 saknussemm ✓）→ **R415 EVV5（不消费）**→ R416 NEW1 消费 132 grauben → queue 归 0 → R417 SCN28-zombie 补第十九批。
4. **回链回填债**（DEFERRED，非阻塞）：**JCE 簇本轮再拓**（saknussemm→professor-lidenbrock/axel，反向待回填）；sabine→marbre 反向、marbre→mac-nab/lieutenant-hobson 反向、Rae 待建、fridrikssen 反向链、samuel-fergusson/dick-kennedy→joe 反向、Mrs Mac-Nab 待建、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R404 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。**下次 EVV5 R415 复评（即下轮）**。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=350→351（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
