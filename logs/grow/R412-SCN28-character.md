---
round: 412
date: 2026-07-19
type_round: 104
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R412 · SCN28-zombie · character — 第十八批 discover：补 3 候选（marbre/saknussemm/grauben），queue 0→3，since_discover 归零；完成 FC 猎手配对 + JCE 簇具名人物补全

## 执行摘要

Phase 2.1-B character discover 轮（type_round 104）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=7<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第十七批（建序 127-129）R409-R411 全数消费（3 建：joe/sabine/fridrikssen），queue 归 0，本轮触发 zombie discover。

**第十八批 3 候选**（=3 → discover_streak_low 保持 0）——FC 猎手配对收束 + JCE 簇余下具名人物：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 130 | marbre | The Fur Country | FC | FC-006 | supporting | 69 | ABSENT | FC 补 sabine/lieutenant-hobson/mac-nab |
| 131 | saknussemm | A Journey to the Center of the Earth | JCE | JCE-003 | supporting | 43 | ABSENT | JCE 补 professor-lidenbrock/axel/hans-bjelke/fridrikssen |
| 132 | grauben | A Journey to the Center of the Earth | JCE | JCE-001 | supporting | 34 | ABSENT | JCE 补 axel/professor-lidenbrock |

**候选说明**：
- **marbre**（FC）——探险队之加拿大猎人、与 Sabine 并肩之首席猎手；69 mentions。完成 FC 猎手二人组（sabine 已建 R410）。首现 FC-006。
- **saknussemm**（JCE）——十六世纪冰岛炼金术士、以符文密码指引地心之路的先行者；43 mentions。补 JCE 簇（启程之源）。首现 JCE-003。
- **grauben**（JCE）——Axel 之维尔兰未婚妻、鼓励其远征的坚贞恋人；34 mentions。补 JCE 簇（情感线）。首现 JCE-001。

**dup-check 汇总**：3 候选 exact-slug filesystem test -f 全 ABSENT（bucket ma/sa/gr）；registry entity label + alias 均 ABSENT，无冲突。全 mentions ≥34 grounded。**排除**：impey-barbicane（filesystem test -f 假 ABSENT 但 registry label「barbicane」+ alias「barbicane」既有 slug barbicane，同一实体已建——registry 查捕获，教训延续 R403 pierre-aronnax/R399 pan-chao）；cyrus-harding/gideon-spilett/nadia/ivan-ogareff/harry-blount/alcide-jolivet/aouda/fix/paganel（各主角既建，filesystem EXISTS）；nicholl（FEM/RM/TT 多值 book HK(d) 暂缓）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=0、since_discover=3 | （被 §3(4) 先匹配）|
| **4** | **SCN28-zombie（queue(character)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 130-132）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：本轮为 discover 轮，无建页无编辑；仅更新 grow_state + queue.md（追加候选）+ 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 filesystem dup-check ABSENT、registry entity+label+alias 无冲突。✔
- **grounding**：全 3 mentions ≥34（marbre 69、saknussemm 43、grauben 34），均足支撑 ≥5 distinct solid PN。✔
- **alias 排除**：impey-barbicane 经 registry label+alias 复验命中既有 slug barbicane，排除；nicholl 多值 book 暂缓。✔
- **既有页排除**：3 候选 test -f + registry label/alias 全 ABSENT；各主角 filesystem EXISTS 已排除。✔
- **since_discover 归零**：3→0。✔

## 六步状态机（SCN28，grow_state 存 R413 起始计数）

| 字段 | R412 起始 | R413 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 412 | 413 |
| type_round | 104 | 105 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 3 | 0（SCN28 归零）|
| discover_streak_low | 0 | 0（new_candidates=3≥3）|
| rounds_since_last_corpus_discover | 348 | 349 |
| last_updated_round | 412 | 413 |

## 遗留问题

1. **character 页数 94（本轮无建）**：queue(character) 0→**3**（建序 130-132）。registry 全库 **1618**，unknown 0。
2. **下轮 R413 = NEW1（§3(7)）**：since_evv5=8<10；queue=3>0 且 since_discover=0<10 → NEW1，消费建序 130 **marbre**（FC 首席猎手，69 mentions，配对 [[Sabine]]，完成 FC 猎手二人组）。
3. **第十八批 3 候选（建序 130-132）**：marbre/saknussemm/grauben。R413-R415 NEW1 消费 → queue 归 0 → R416 SCN28-zombie 补第十九批。**EVV5 时点**：since_evv5 R413 起始=8，逐轮 +1 → R415 起始=10 → **R415 = §3(1b) EVV5**（除非期间 discover 令 since_discover≥10 触发 §3(1a) 合并轮）。若 R413/R414 消费 marbre/saknussemm 后 R415 起始 since_evv5=10 触发 EVV5（不消费队列），则 grauben（132）顺延至 R416 NEW1 消费。
4. **回链回填债**（DEFERRED，非阻塞）：sabine→marbre（待建）反向、fridrikssen→professor-lidenbrock/hans-bjelke/axis 反向、samuel-fergusson/dick-kennedy→joe 反向、Mrs Mac-Nab 待建、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R404 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R415 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=348→349（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
