---
round: 408
date: 2026-07-19
type_round: 100
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R408 · SCN28-zombie · character — 第十七批 discover：补 3 候选（joe/sabine/fridrikssen），queue 0→3，since_discover 归零；跨 FWB/FC/JCE 三作品收束核心配角，FWB 收束气球远征三人组

## 执行摘要

Phase 2.1-B character discover 轮（type_round 100）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=3<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第十六批（建序 124-126）R405-R407 全数消费（3 建：samuel-fergusson/mac-nab/hans-bjelke），queue 归 0，本轮触发 zombie discover。

**第十七批 3 候选**（=3 → discover_streak_low 保持 0）——跨 FWB/FC/JCE 三作品，收束三既有簇之核心配角：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 127 | joe | Five Weeks in a Balloon | FWB | FWB-006 | supporting | 531 | ABSENT | FWB 补 samuel-fergusson/dick-kennedy |
| 128 | sabine | The Fur Country | FC | FC-004 | supporting | 54 | ABSENT | FC 补 lieutenant-hobson/sergeant-long/mac-nab |
| 129 | fridrikssen | A Journey to the Center of the Earth | JCE | JCE-009 | supporting | 20 | ABSENT | JCE 补 professor-lidenbrock/axel/hans-bjelke |

**候选说明**：
- **joe**（FWB）——Ferguson 之忠仆兼远征「右手」、机敏乐天的随行侍从；FWB 531 mentions（全批最高）。收束气球远征三人组（fergusson/kennedy/joe，前二既建）。首现 FWB-006。**消歧警示**：mentions 极高，建页须严格取明指 Ferguson 侍从 Joe 之句，排除对话中泛称。
- **sabine**（FC）——探险队之加拿大猎人、Fort Hope 觅食队主力射手；54 mentions。补 FC 簇（既有 7 页）。首现 FC-004。
- **fridrikssen**（JCE）——Reykjavik 之博物学教授、荐 Hans 予 Lidenbrock 并助其考察的雷城学者；20 mentions。补 JCE 簇（professor-lidenbrock/axel/hans-bjelke 既建）。首现 JCE-009。

**dup-check 汇总**：3 候选 exact-slug filesystem test -f 全 ABSENT（bucket jo/sa/fr）；registry entity label + alias 均 ABSENT，无冲突。全 mentions ≥20 grounded。**排除**：nicholl（FEM/RM/TT 多值 book HK(d) 暂缓）；既建各主角（samuel-fergusson/dick-kennedy/mac-nab/hans-bjelke/professor-lidenbrock/axel 等）。

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

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 127-129）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：本轮为 discover 轮，无建页无编辑；仅更新 grow_state + queue.md（追加候选）+ 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 filesystem dup-check ABSENT、registry entity+label+alias 无冲突。✔
- **grounding**：全 3 mentions ≥20（joe 531、sabine 54、fridrikssen 20），均足支撑 ≥5 distinct solid PN。✔
- **alias 排除**：nicholl 多值 book 暂缓；本批无同一实体重建风险（joe/sabine/fridrikssen 均无既建 alias 命中）。✔
- **既有页排除**：3 候选 test -f + registry label/alias 全 ABSENT。✔
- **since_discover 归零**：4→0。✔

## 六步状态机（SCN28，grow_state 存 R409 起始计数）

| 字段 | R408 起始 | R409 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 408 | 409 |
| type_round | 100 | 101 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 4 | 0（SCN28 归零）|
| discover_streak_low | 0 | 0（new_candidates=3≥3）|
| rounds_since_last_corpus_discover | 344 | 345 |
| last_updated_round | 408 | 409 |

## 遗留问题

1. **character 页数 91（本轮无建）**：queue(character) 0→**3**（建序 127-129）。registry 全库 **1615**，unknown 0。
2. **下轮 R409 = NEW1（§3(7)）**：since_evv5=4<10；queue=3>0 且 since_discover=0<10 → NEW1，消费建序 127 **joe**（FWB Ferguson 侍从，531 mentions，可回链 [[Samuel Ferguson]]/[[Dick Kennedy]]，收束气球三人组）。**消歧警示**：joe mentions 极高，取明指侍从句。
3. **第十七批 3 候选（建序 127-129）**：joe/sabine/fridrikssen。R409-R411 NEW1 消费 → queue 归 0 → R412 SCN28-zombie 补第十八批。**EVV5 时点**：since_evv5 R409 起始=4，逐轮 +1 → R414 起始=9、R415 起始=10 → **R415 = §3(1b) EVV5**（除非期间 discover 令 since_discover≥10 触发 §3(1a) 合并轮）。
4. **回链回填债**（DEFERRED，非阻塞）：dick-kennedy→samuel-fergusson 反向、samuel-fergusson/dick-kennedy↔joe（待建）、Mrs Mac-Nab 待建、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R404 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R415 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=344→345（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
