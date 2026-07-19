---
round: 420
date: 2026-07-19
type_round: 112
phase: "2.1"
current_type: character
gene: NEW1
pages: [martha]
result: success
---

# GROW 2.1-B · R420 · NEW1 · character — 建 Martha（A Journey to the Center of the Earth 之 Lidenbrock 家忠仆女佣，胆怯而多嘴、传扬远征之讯于天下；消费第十九批建序 135，queue 1→0）

## 执行摘要

Phase 2.1-B character 第 85 建（type_round 112），消费 R417 第十九批 discover 队列**建序 135（末候选）**。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=1>0 且 since_discover=2<10 → §3(3)/(4) 否；stub%=0 → §3(7) NEW1）。**本轮消费后 queue(character)=0 → R421 触发 SCN28-zombie 补第二十批。**

**Martha**（*A Journey to the Center of the Earth*）——Lidenbrock 教授 Königstrasse 宅邸之忠仆女佣、持家掌厨之好妇人。名之曰「our good housekeeper Martha」（JCE-002-038），列于宅中「living contents」（JCE-001-032）。忧膳「Martha must have concluded that she was very much behindhand, for the dinner had only just been put into the oven」（JCE-001-003）。教授闭户破译如尼密文，闭锁其中「when our good Martha wanted to go to market, she found the door locked」（JCE-005-018），叩门无应（JCE-005-011），空储（JCE-005-022），终得释「Martha was set at liberty, ran off to the market」（JCE-006-003）。启程挥别「Martha and the young girl, standing at the door, waved their last farewell」（JCE-007-077），多嘴传讯天下「thanks to Martha's ineradicable tattling, the news that the Professor had gone to discover a way to the centre of the earth had spread over the whole civilised world」（JCE-045-008）。胆怯避主怒「Martha took to her heels for safety」（JCE-002-040），闻门砰然而奔出（JCE-004-002），忧困而伤怀（JCE-005-020）。

**role=supporting**。book='A Journey to the Center of the Earth'、first_appearance=JCE-001、affiliation 空、**label=Martha，aliases=[]**。

**15 distinct solid PN**（JCE-001-003/032、002-038/040/043、004-002、005-011/018/019/020/022、006-003、007-077、045-005/008）：均 solid，逾门。「Martha」JCE 内单指本人（女仆）；无消歧冲突。

**查重**：exact-slug martha filesystem test -f ABSENT（bucket ma）+ registry entity/label/alias 复验——「Martha / martha」无既建人物页，无冲突。

**JCE 3-char VVV**：无需 RFC-0003 Note（仅 4-char 触发）。

**wikilink**：[[Professor Lidenbrock]]（professor-lidenbrock，既建，JCE-002-043）、[[Axel]]（axel，既建，JCE-005-019）、[[Gräuben]]（grauben，既建，JCE-007-077）、[[A Journey to the Center of the Earth]]（work，存，JCE-007-077）——四链均无悬挂。**JCE 簇完足**（martha 补入 professor-lidenbrock/axel/grauben，Lidenbrock 家宅四人齐备：教授/Axel/Gräuben/Martha）。

prose-gate：add_page 建页时 strict 报 JCE-005-019 关键词重叠 1.56%<2%（引注为释义未直引），改直引「should Martha and I be victims...」后重跑 → 复核 strict 全通过；edit_page 复建时报 Relationships 三 bullet 连行合并 513 字超 400 门 → 三 bullet 间插空行分段 → 复核 0 over-400 且 strict 通过。**引注**：修订后 strict 全通过。quality featured 回填。

character 计数 99→**100**，registry total 1623→**1624**，unknown 恒 0。build_registry 3 alias warn（均 parked HK）。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=1、since_discover=2 | 否* |
| 4 | SCN28-zombie（queue==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

> *queue=1>0 → NEW1 消费建序 135。消费后 queue=0 → R421 SCN28-zombie 补第二十批。

## 页面处理记录

| slug | rev | book | role | first_app | 页内引注 | 消歧/要点 |
|------|-----|------|------|-----------|---------|----------|
| martha | Q5fLcr | A Journey to the Center of the Earth | supporting | JCE-001 | 15 distinct | 持家掌厨-忧膳-闭锁空储-终得释-启程挥别-多嘴传讯-胆怯避怒-忧困伤怀；label Martha；JCE 3-char 无 Note；add_page→JCE-005-019 改直引；edit_page→Relationships 分段修散文门；strict 通过；四链 [[Professor Lidenbrock]]/[[Axel]]/[[Gräuben]]/[[A Journey to the Center of the Earth]] |

- **martha**：15 distinct solid PN；aliases []；character-schema 五 H2。add_page rev AahfNV（size 3060）→ edit_page rev Q5fLcr（size 3098）。quality featured 回填。pn_validator --mode strict ✓。**JCE 家宅簇完足；Martha 单指无消歧冲突。**

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Martha 女仆-持家-闭锁-胆怯-多嘴因果；JCE-005-019 释义改直引后 strict ✓。✔
- **G2 段落 ≤400 字**：edit_page 报 Relationships 合并块 513 → 分段后 0 over-400（awk + edit_page 双复核）。✔
- **G3 ≥5 distinct PN**：15 solid，逾门。✔
- **G4 脚本建页**：add_page 建页 + edit_page 修订（均自 repo 根调用），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：character-schema 五 H2；frontmatter 全字段（book 单引号 / description 单引号含转义撇号）；role=supporting ∈ enum；JCE 3-char 无 Note。✔
- **registry 一致**：total 1624 character 100 unknown 0；3 alias warn（均 parked HK）。✔
- **查重充分**：exact-slug + entity/label/alias ABSENT；registry 无 character 冲突。✔
- **wikilink 完整性**：Professor Lidenbrock + Axel + Gräuben + A Journey to the Center of the Earth 四链存在无悬挂。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R421 起始计数）

| 字段 | R420 起始 | R421 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 420 | 421 |
| type_round | 112 | 113 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 356 | 357 |
| last_updated_round | 420 | 421 |

## 遗留问题

1. **character 页数 100**：本轮 +1（martha）。queue(character) 1→**0**（建序 135 消费，第十九批全数消费完毕）。registry 全库 **1624**，unknown 0。
2. **下轮 R421 = SCN28-zombie（§3(4)）**：since_evv5=5<10；**queue(character)=0 → §3(4) SCN28-zombie 触发**，补第二十批 discover 候选（≥3），since_discover 归 0。候选池：跨作品剩余具名配角（FC Mrs Joliffe/Mrs Rae/Mrs Mac-Nab 三妇；其他作品核心配角）。filesystem test -f + registry label/alias 双查重。
3. **第十九批消费完毕**：R418 NEW1（133 joliffe ✓）→ R419 NEW1（134 rae ✓）→ R420 NEW1（135 martha ✓）→ queue 归 0 → R421 SCN28-zombie 补第二十批。**EVV5 时点**：since_evv5 R421 起始=5 → R426 起始=10 → **R426 = §3(1b) EVV5**（除非期间 discover 令 since_discover≥10 触发 §3(1a) 合并轮）。
4. **回链回填债**（DEFERRED，非阻塞）：**JCE 家宅簇完足**（martha→professor-lidenbrock/axel/grauben，反向待回填）；joliffe→lieutenant-hobson/mac-nab/sabine/marbre 反向、rae→mac-nab/marbre/lieutenant-hobson/sabine 反向、Mrs Joliffe/Mrs Rae/Mrs Mac-Nab 待建、grauben/saknussemm/fridrikssen 反向链、samuel-fergusson/dick-kennedy→joe 反向、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R415 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R426 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=356→357（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
