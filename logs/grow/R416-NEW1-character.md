---
round: 416
date: 2026-07-19
type_round: 108
phase: "2.1"
current_type: character
gene: NEW1
pages: [grauben]
result: success
---

# GROW 2.1-B · R416 · NEW1 · character — 建 Gräuben（A Journey to the Center of the Earth 之 Lidenbrock 教女、Axel 未婚妻、鼓励远征的维尔兰矿物学家；收束第十八批，建序 132，queue 1→0）

## 执行摘要

Phase 2.1-B character 第 82 建（type_round 108），消费 R412 第十八批 discover 队列**建序 132（末候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=0<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=1>0 且 since_discover=3<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=0 → R417 触发 SCN28-zombie 补第十九批。**

**Gräuben**（*A Journey to the Center of the Earth*）——Lidenbrock 之教女、Axel 之未婚妻、鼓励远征的维尔兰矿物学家。教女之身「a young Virlandaise of seventeen」（JCE-001-032），碧眼金发「a lovely blue-eyed blonde, rather given to gravity and seriousness」深爱 Axel（JCE-003-040），矿物名家「Mademoiselle Gräuben was an accomplished mineralogist; she could have taught a few things to a savant」（JCE-003-041）。不劝反励「what, Gräuben, won't you dissuade me from such an undertaking?」（JCE-007-021），受托理家「solemnly investing Gräuben with the reins of government」（JCE-007-074），执手送别「hand in hand, but in silence」（JCE-007-029）。远隔难见「Gräuben was far away; and I never hoped to see her again」（JCE-008-034），地心念之「my poor Gräuben」（JCE-027-007），冀望重逢「the thought of meeting my little Gräuben again」（JCE-019-026）。爱之切切「I love you well, my own dear Gräuben!」（JCE-003-056），海港留名「let it be called Port Gräuben; it will look very well upon the map」（JCE-032-005），归而缔婚「I was to be married to Gräuben that day」（JCE-036-009），重逢之喜「the joy of Gräuben」（JCE-045-005）。

**role=supporting**。book='A Journey to the Center of the Earth'、first_appearance=JCE-001、affiliation 空、**label=Gräuben，aliases=[]**。

**13 distinct solid PN**（JCE-001-032、003-040/041/056、007-021/029/074、008-034、019-026、027-007、032-005、036-009、045-005）：均 solid，逾门。「Gräuben」JCE 内单指本人（Axel 未婚妻）；无消歧冲突。

**查重**：exact-slug grauben filesystem test -f ABSENT（bucket gr）+ registry entity/label/alias 复验——「Gräuben / grauben」无既建人物页，无冲突。

**JCE 3-char VVV**：无需 RFC-0003 Note（仅 4-char 触发）。

**wikilink**：[[Axel]]（axel，既建）、[[Professor Lidenbrock]]（professor-lidenbrock，既建）、[[A Journey to the Center of the Earth]]（work，存）——三链均无悬挂。**Martha 页未建**：正文未设链（可后续 discover）。**JCE 簇本轮再拓**（grauben 补入 lidenbrock/axel/hans-bjelke/fridrikssen/saknussemm，JCE 簇共 6 人物页）。

prose-gate：add_page 初稿 0 超段（awk 复核 0 over-400），直接建。**引注**：strict 首验即通过。quality featured 回填。

character 计数 96→**97**，registry total 1620→**1621**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=1、since_discover=3 | 否* |
| 4 | SCN28-zombie（queue==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=1>0 → NEW1 消费建序 132。消费后 queue=0 → R417 SCN28-zombie。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| grauben | dzOF4e | A Journey to the Center of the Earth | supporting | JCE-001 | 13 distinct | 教女之身-碧眼金发-矿物名家-不劝反励-受托理家-执手送别-远隔难见-地心念之-冀望重逢-爱之切切-海港留名-归而缔婚-重逢之喜；label Gräuben；JCE 3-char 无 Note；0 超段直建；strict 首验通过；三链 [[Axel]]/[[Professor Lidenbrock]]/[[A Journey to the Center of the Earth]] |

- **grauben**：13 distinct solid PN；aliases []；character-schema 五 H2。add_page rev dzOF4e（size 2363）。quality featured 回填。pn_validator --mode strict ✓。**JCE 簇再拓（共 6 页）；Gräuben 单指无消歧冲突。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Gräuben 教女-未婚妻-矿物家因果；strict ✓。✔
- **G2 段落 ≤400 字**：初稿 0 超门（awk 复核）。✔
- **G3 ≥5 distinct PN**：13 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号 / description 双引号含撇号）；role=supporting ∈ enum；JCE 3-char 无 Note。✔
- **registry 一致**：total 1621 character 97 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Axel + Professor Lidenbrock + A Journey to the Center of the Earth 三链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R417 起始计数）

| 字段 | R416 起始 | R417 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 416 | 417 |
| type_round | 108 | 109 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 352 | 353 |
| last_updated_round | 416 | 417 |

## 遗留问题

1. **character 页数 97**：本轮 +1（grauben）。queue(character) 1→**0**（建序 132 消费，第十八批全数消费完毕）。registry 全库 **1621**，unknown 0。
2. **下轮 R417 = SCN28-zombie（§3(4)）**：since_evv5=1<10；**queue(character)=0 → §3(4) SCN28-zombie 触发**，补第十九批 discover 候选（≥3），since_discover 归 0。候选池：FC 剩余 corporal-joliffe/rae；JCE martha（Lidenbrock 女仆，24 mentions）；其他作品核心配角。跨作品多样化，filesystem+registry 双查重。
3. **第十八批消费完毕**：R413 NEW1（130 marbre ✓）→ R414 NEW1（131 saknussemm ✓）→ R415 EVV5（不消费）→ R416 NEW1（132 grauben ✓）→ queue 归 0 → R417 SCN28-zombie 补第十九批。**EVV5 时点**：since_evv5 R417 起始=1 → R426 起始=10 → **R426 = §3(1b) EVV5**（除非期间 discover 令 since_discover≥10 触发 §3(1a) 合并轮）。
4. **回链回填债**（DEFERRED，非阻塞）：**JCE 簇本轮再拓**（grauben→axel/professor-lidenbrock，反向待回填；Martha 待建）；saknussemm→lidenbrock/axel 反向、fridrikssen 反向、sabine↔marbre 反向、marbre→mac-nab/lieutenant-hobson 反向、Rae 待建、samuel-fergusson/dick-kennedy→joe 反向、Mrs Mac-Nab 待建、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R415 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R426 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=352→353（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
