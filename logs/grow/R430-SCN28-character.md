---
round: 430
date: 2026-07-19
type_round: 122
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R430 · SCN28-zombie · character — 第二十二批 discover：补 3 候选（bell/harris/isaac-hakkabut），queue 0→3，since_discover 归零；收束 ACH 陆行小队 + 开 DSCF/OC 两簇纵深

## 执行摘要

Phase 2.1-B character discover 轮（type_round 122）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=3<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第二十一批（建序 139-141）R427-R429 全数消费（3 建：johnson/altamont/olbinett），queue 归 0，本轮触发 zombie discover。

**第二十二批 3 候选**（=3 → discover_streak_low 保持 0）——跨三作品避单作品集中，收束 ACH 陆行小队 + 开 DSCF/OC 两簇纵深：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 142 | bell | The Adventures of Captain Hatteras | ACH | ACH-003 | supporting | 183 | ABSENT | ACH 补 captain-hatteras/clawbonny/shandon/johnson/altamont |
| 143 | harris | Dick Sand, A Captain at Fifteen | DSCF | DSCF-015 | supporting | 248 | ABSENT | DSCF 补 dick-sand/negoro/hercules |
| 144 | isaac-hakkabut | Off on a Comet | OC | OC-019 | supporting | 86 | ABSENT | OC 补 ben-zoof/palmyrin-rosette |

**候选说明**：
- **bell**（ACH）——Forward 号之木匠、Hatteras 陆行北极小队之匠人与斥候；183 mentions。收束 ACH 陆行小队（现有 captain-hatteras/clawbonny/shandon/johnson/altamont 五页）。首现 ACH-003。
- **harris**（DSCF）——诱骗 Dick Sand 一行深入非洲、与 Negoro 同谋之美籍奸细；248 mentions。开 DSCF 纵深（现有 dick-sand/negoro/hercules）。首现 DSCF-015。
- **isaac-hakkabut**（OC）——Hansa 号之吝啬犹太商贩、彗星世界中唯利是图的守财者；86 mentions。开 OC 纵深（现有 ben-zoof/palmyrin-rosette）。首现 OC-019。

**dup-check 汇总**：3 候选 exact-slug filesystem test -f 全 ABSENT（bucket be/ha/is）；registry entity label + alias 均 ABSENT（Python 精确复验），无冲突。全 mentions ≥86 grounded。**排除（registry-catch）**：servadac（registry label「Hector Servadac」→ 既有 slug hector-servadac，HK(e)）；fergusson（registry label「Samuel Fergusson」→ 既有 samuel-fergusson）；kennedy（label「Dick Kennedy」→ dick-kennedy）；palmyrin-rosette/ben-zoof/dick-sand/negoro/hercules（各既建，registry label EXISTS）。**注**：bell 之 label「Bell」于 SC/TTLU 各有 1 处同名一次性提及，但 ACH 内 183 提及单指 Forward 木匠 Bell，建页锚定 ACH 单一实体（潜在同名 HK 留意，非本轮阻塞）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=0、since_discover=4 | （被 §3(4) 先匹配）|
| **4** | **SCN28-zombie（queue(character)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 142-144）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：本轮为 discover 轮，无建页无编辑；仅更新 grow_state + queue.md（追加候选）+ 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 filesystem dup-check ABSENT、registry entity+label+alias 精确复验无冲突。✔
- **grounding**：全 3 mentions ≥86（harris 248、bell 183、isaac-hakkabut 86），均足支撑 ≥5 distinct solid PN。✔
- **registry-catch 排除**：servadac/fergusson/kennedy/palmyrin-rosette/ben-zoof/dick-sand/negoro/hercules 经 registry label EXISTS 命中既建，排除。✔
- **既有页排除**：3 候选 test -f + registry label/alias 全 ABSENT。✔
- **since_discover 归零**：4→0。✔

## 六步状态机（SCN28，grow_state 存 R431 起始计数）

| 字段 | R430 起始 | R431 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 430 | 431 |
| type_round | 122 | 123 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 4 | 0（SCN28 归零）|
| discover_streak_low | 0 | 0（new_candidates=3≥3）|
| rounds_since_last_corpus_discover | 366 | 367 |
| last_updated_round | 430 | 431 |

## 遗留问题

1. **character 页数 106（本轮无建）**：queue(character) 0→**3**（建序 142-144）。registry 全库 **1630**，unknown 0。
2. **下轮 R431 = NEW1（§3(7)）**：since_evv5=4<10；queue=3>0 且 since_discover=0<10 → NEW1，消费建序 142 **bell**（ACH Forward 木匠，183 mentions，首现 ACH-003，配对 [[Captain Hatteras]]/[[Johnson]]/[[Dr Clawbonny]]）。
3. **第二十二批 3 候选（建序 142-144）**：bell/harris/isaac-hakkabut。R431-R433 NEW1 消费 → queue 归 0 → R434 SCN28-zombie 补第二十三批。**EVV5 时点**：since_evv5 R431 起始=4，逐轮 +1 → R437 起始=10 → **R437 = §3(1b) EVV5**（除非期间 discover 令 since_discover≥10 触发 §3(1a) 合并轮）。
4. **回链回填债**（DEFERRED，非阻塞）：ACH 簇（bell→captain-hatteras/johnson/clawbonny 反向、altamont/johnson 互链反向、Simpson/Pen/Wilson 待建）、DSCF 簇（harris→dick-sand/negoro 反向）、OC 簇（isaac-hakkabut→ben-zoof 反向）、SC 簇（olbinett/lady-helena→glenarvan/mary-grant/mcnabbs 反向、john-mangles/robert-grant/thalcave/paganel 反向）、JCE 家宅簇（martha→professor-lidenbrock/axel/grauben 反向）、FC 簇（joliffe/rae→lieutenant-hobson/mac-nab/sabine/marbre 反向、Mrs Joliffe/Mrs Rae/Mrs Mac-Nab 待建）、grauben/saknussemm/fridrikssen 反向链、samuel-fergusson/dick-kennedy→joe 反向、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan / Robur the Conqueror）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs、Bell ACH vs SC/TTLU 一次性同名）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R426 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R437 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=366→367（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
