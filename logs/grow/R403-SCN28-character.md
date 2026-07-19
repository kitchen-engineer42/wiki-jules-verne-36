---
round: 403
date: 2026-07-19
type_round: 95
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R403 · SCN28-zombie · character — 第十六批 discover：补 3 候选（samuel-fergusson/mac-nab/hans-bjelke），queue 0→3，since_discover 归零；跨 FWB/FC/JCE 三作品，role 破全 supporting 单调，R404 起 EVV5

## 执行摘要

Phase 2.1-B character discover 轮（type_round 95）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=9<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第十五批（建序 121-123）R400-R402 全数消费（3 建：thomas-black/taskinar/dick-kennedy），queue 归 0，本轮触发 zombie discover。

**EVV5 时点**：本轮末 since_evv5 +1 → 10（R404 起始），**R404 = §3(1b) EVV5**（pages:[] 反射轮，不消费队列）。故第十六批实际消费自 R405 起。

**第十六批 3 候选**（=3 → discover_streak_low 保持 0）——跨 FWB/FC/JCE 三作品，避单作品集中，role 多样：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 124 | samuel-fergusson | Five Weeks in a Balloon | FWB | FWB-001 | protagonist | 177 | ABSENT | FWB 补 dick-kennedy |
| 125 | mac-nab | The Fur Country | FC | FC-001 | supporting | 93 | ABSENT | FC 补 paulina-barnett/lieutenant-hobson/sergeant-long/kalumah/madge/thomas-black |
| 126 | hans-bjelke | Journey to the Center of the Earth | JCE | JCE-011 | supporting | 153 | ABSENT | JCE 补 professor-lidenbrock/axel |

**候选说明**：
- **samuel-fergusson**（FWB）——气球横越非洲之博学探险家、Victoria 号之主帅；「Ferguson」FWB 177 mentions。**role=protagonist**——FWB 主角。补 FWB 簇（dick-kennedy 既建）。首现 FWB-001。
- **mac-nab**（FC）——探险队之苏格兰木匠工头、Fort Hope 营建之主力；93 distinct PN。补 FC 簇（既有 6 页）。首现 FC-001-011。
- **hans-bjelke**（JCE）——冰岛绒鸭猎人、Lidenbrock 地心探险之沉默忠仆向导；「Hans」JCE 153 mentions。补 JCE 簇（professor-lidenbrock/axel 既建）。首现 JCE-011。

**dup-check 汇总**：3 候选 exact-slug filesystem test -f 全 ABSENT（bucket sa/ma/ha）；registry entity + label（Samuel Ferguson/Ferguson/Mac-Nab/Hans Bjelke/各 token）均 ABSENT，不在既有 3 parked 冲突（Hector Servadac/Robur the Conqueror/Claudius Bombarnac）内，无冲突。全 mentions ≥93 grounded。**排除**：（a）**pierre-aronnax**——filesystem test -f 假 ABSENT（slug 若为 pierre-aronnax），但 registry label「Pierre Aronnax」→ 既有 slug **aronnax**，同一实体已建；**registry label 复验捕获**，教训延续（R399 pan-chao label「Pan Chao」、R386 count-dartigas=ker-karraje、R390 jasper-hobson=lieutenant-hobson——slug 变体/别名须 registry 并查，filesystem 单验不足）。（b）**nicholl**——FEM/RM/TT 多作品，触 HK(d) 多值 book，暂缓。（c）otto-lidenbrock（→professor-lidenbrock）/axel/michael-strogoff/phileas-fogg/passepartout/conseil/ned-land/captain-nemo 等既建。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =9 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=0、since_discover=3 | （被 §3(4) 先匹配）|
| **4** | **SCN28-zombie（queue(character)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 124-126）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：本轮为 discover 轮，无建页无编辑；仅更新 grow_state + queue.md（追加候选）+ 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 filesystem dup-check ABSENT、registry entity+label 无冲突。✔
- **grounding**：全 3 mentions ≥93（samuel-fergusson 177、hans-bjelke 153、mac-nab 93），均足支撑 ≥5 distinct solid PN。✔
- **alias 排除**：pierre-aronnax 经 registry label 捕获既有 slug aronnax（同一实体）而排除；nicholl 多值 book 暂缓；本批无同一实体重建风险。✔
- **既有页排除**：3 候选 test -f + registry label 全 ABSENT。✔
- **since_discover 归零**：3→0。✔

## 六步状态机（SCN28，grow_state 存 R404 起始计数）

| 字段 | R403 起始 | R404 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 403 | 404 |
| type_round | 95 | 96 |
| rounds_since_last_evv5 | 9 | 10（R404 起 §3(1b) EVV5）|
| rounds_since_last_discover | 3 | 0（SCN28 归零）|
| discover_streak_low | 0 | 0（new_candidates=3≥3）|
| rounds_since_last_corpus_discover | 339 | 340 |
| last_updated_round | 403 | 404 |

## 遗留问题

1. **character 页数 88（本轮无建）**：queue(character) 0→**3**（建序 124-126）。registry 全库 **1612**，unknown 0。
2. **下轮 R404 = EVV5（§3(1b)）**：since_evv5=10≥10 → §3(1b) EVV5 触发（since_discover=0<10 → 非 §3(1a) 合并轮）。**EVV5 为 pages:[] schema 反射轮**——扫全 character（88 页）3 结构指标（5 H2 精确匹配、role∈enum、book 非空）+ 2 内容债（≥5 distinct PN、prose ≤400），不消费队列，since_evv5 归 0。**第十六批消费自 R405 起**：R405 NEW1（建序 124 samuel-fergusson）→ R406 NEW1（125 mac-nab）→ R407 NEW1（126 hans-bjelke）→ queue 归 0 → R408 SCN28-zombie 补第十七批。
3. **第十六批 3 候选（建序 124-126）**：samuel-fergusson/mac-nab/hans-bjelke。R404 EVV5（不消费）→ R405-R407 NEW1 消费 → R408 SCN28-zombie。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + dick-kennedy↔samuel-fergusson（待建，双向）、（Joe 待建）、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。JCE 新建 hans-bjelke 可回链 professor-lidenbrock/axel。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT 即此类）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan——若后建 Godfrey 角色页则触发新同名冲突，暂缓）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R393 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。R404 EVV5 将复评此二债。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=339→340（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
