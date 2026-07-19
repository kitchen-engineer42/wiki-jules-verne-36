---
round: 419
date: 2026-07-19
type_round: 111
phase: "2.1"
current_type: character
gene: NEW1
pages: [rae]
result: success
---

# GROW 2.1-B · R419 · NEW1 · character — 建 Rae（The Fur Country 之探险队铁匠、Fort Hope 营建与筏架之匠人，御熊之役自愿冒险的勇者；消费第十九批建序 134，queue 2→1）

## 执行摘要

Phase 2.1-B character 第 84 建（type_round 111），消费 R417 第十九批 discover 队列**建序 134**。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=2>0 且 since_discover=1<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=1（建序 135 martha）。**

**Rae**（*The Fur Country*）——探险队之铁匠、Fort Hope 营建与筏架之匠人。精于锻工「Rae was most skilful at blacksmith's work, and with the aid of a little portable forge he was able to make all the pins, tenons, bolts, nails, screws, nuts, &c., required in carpentry」（FC-013-004），携妻居堡（FC-014-002）。司凝水器「Rae set up his condensers for collecting the vapour」（FC-017-008）。御熊之役受召为勇者「called together Long, Mac-Nab, and Rae the blacksmith, as the bravest men in his party」（FC-021-032），三人自愿冒险（FC-021-039），登阁窥熊「Rae climbed up to the trap-door of the loft, and peeping through it, made sure that the bears were still on the roof」（FC-021-043），危中救官（FC-021-055），复守望不懈（FC-021-047）。弃岛时寻得铁栓造筏「the blacksmith, Rae, had fortunately found a large number of the iron bolts... invaluable for firmly fastening together the different portions of the framework of the raft」（FC-042-028）。Hobson 深信之「consulted Sergeant Long, Mac-Nab, Rae, Marbre, and Sabine, in whom he had great confidence」（FC-043-030）。

**role=supporting**。book='The Fur Country'、first_appearance=FC-013、affiliation 空、**label=Rae，aliases=[]**。

**12 distinct solid PN**（FC-013-004、014-002、017-008、018-009、021-032/039/043/047/055、035-005、042-028、043-030）：均 solid，逾门。**消歧关键**：FC-001-027、FC-007-009 之「Rae」乃史上北极探险家 John Rae（与 Franklin/Mackenzie 并列），**非本铁匠角色，已排除**，避免史实人物与虚构角色混淆。正文引注均取铁匠 Rae 语境。

**查重**：exact-slug rae filesystem test -f ABSENT（bucket ra）+ registry entity/label/alias 复验——「Rae / rae」无既建人物页，无冲突。

**FC 2-char VVV**：无需 RFC-0003 Note（仅 4-char 触发）。

**wikilink**：[[Mac-Nab]]（mac-nab，既建，FC-035-005）、[[Marbre]]（marbre，既建，FC-035-005）、[[Jaspar Hobson]]（lieutenant-hobson，既建，FC-043-030）、[[Sabine]]（sabine，既建，FC-043-030）、[[The Fur Country]]（work，存，FC-042-028）——五链均无悬挂。**Mrs Rae 页未建**：正文以 PN-grounded 行内文字呈现（FC-018-009），未设悬挂链。**FC 簇再拓**（rae 补入 mac-nab/marbre/lieutenant-hobson/sabine，FC 簇继续收束）。

prose-gate：初稿 1 超段（404，御熊三引合段）→ 拆为两段（受召自愿 / 登阁窥熊），复核 0 over-400。**引注**：strict 首验即通过。quality featured 回填。

character 计数 98→**99**，registry total 1622→**1623**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=2、since_discover=1 | 否* |
| 4 | SCN28-zombie（queue==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=2>0 → NEW1 消费建序 134。消费后 queue=1 → R420 继续 NEW1（建序 135 martha）。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| rae | W6Wcn1 | The Fur Country | supporting | FC-013 | 12 distinct | 精于锻工-携妻居堡-司凝水器-御熊受召-三人自愿-登阁窥熊-危中救官-守望不懈-寻栓造筏-Hobson 深信；label Rae；FC 2-char 无 Note；1 超段拆解后 0 over-400；strict 首验通过；五链 [[Mac-Nab]]/[[Marbre]]/[[Jaspar Hobson]]/[[Sabine]]/[[The Fur Country]]；史实探险家 John Rae（FC-001-027/007-009）排除 |

- **rae**：12 distinct solid PN；aliases []；character-schema 五 H2。add_page rev W6Wcn1（size 3087）。quality featured 回填。pn_validator --mode strict ✓。**FC 簇再拓；铁匠 Rae 与史实探险家 John Rae 消歧排除。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指铁匠 Rae 锻工-御熊-造筏因果；strict ✓。史实 John Rae 引注排除。✔
- **G2 段落 ≤400 字**：初稿 1 超门（404）→ 拆解后 0（awk 复核）。✔
- **G3 ≥5 distinct PN**：12 solid，逾门。✔
- **G4 脚本建页**：add_page 建页（自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号 / description 单引号含转义撇号）；role=supporting ∈ enum；FC 2-char 无 Note。✔
- **registry 一致**：total 1623 character 99 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Mac-Nab + Marbre + Jaspar Hobson + Sabine + The Fur Country 五链存在无悬挂；Mrs Rae 行内文字无悬挂链。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R420 起始计数）

| 字段 | R419 起始 | R420 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 419 | 420 |
| type_round | 111 | 112 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 355 | 356 |
| last_updated_round | 419 | 420 |

## 遗留问题

1. **character 页数 99**：本轮 +1（rae）。queue(character) 2→**1**（建序 134 消费）。registry 全库 **1623**，unknown 0。
2. **下轮 R420 = NEW1（§3(7)）**：since_evv5=4<10；queue=1>0 且 since_discover=2<10 → NEW1，消费建序 135 **martha**（JCE Lidenbrock 教授之忠仆女佣，24 mentions，首现 JCE-001；完足 Lidenbrock 家宅 教授/Axel/Gräuben/Martha）。**消费后 queue=0 → R421 SCN28-zombie 补第二十批。**
3. **第十九批消费进度**：R418 NEW1（133 joliffe ✓）→ R419 NEW1（134 rae ✓）→ R420 NEW1（135 martha 待）→ queue 归 0 → R421 SCN28-zombie 补第二十批。**EVV5 时点**：since_evv5 R420 起始=4 → R426 起始=10 → **R426 = §3(1b) EVV5**（除非期间 discover 令 since_discover≥10 触发 §3(1a) 合并轮）。
4. **回链回填债**（DEFERRED，非阻塞）：**FC 簇本轮再拓**（rae→mac-nab/marbre/lieutenant-hobson/sabine 反向、Mrs Rae 待建）；joliffe→lieutenant-hobson/mac-nab/sabine/marbre 反向、Mrs Joliffe 待建、martha 待建、JCE 簇（martha→professor-lidenbrock/axel/grauben 反向、grauben/saknussemm/fridrikssen 反向链）、samuel-fergusson/dick-kennedy→joe 反向、Mrs Mac-Nab 待建、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R415 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R426 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=355→356（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
