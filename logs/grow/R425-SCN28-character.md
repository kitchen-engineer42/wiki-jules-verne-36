---
round: 425
date: 2026-07-19
type_round: 117
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R425 · SCN28-zombie · character — 第二十一批 discover：补 3 候选（johnson/altamont/olbinett），queue 0→3，since_discover 归零；续拓 ACH（Forward 远征簇）+ 补 SC（Duncan 搜救簇）

## 执行摘要

Phase 2.1-B character discover 轮（type_round 117）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=9<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第二十批（建序 136-138）R422-R424 全数消费（3 建：clawbonny/shandon/lady-helena），queue 归 0，本轮触发 zombie discover。

**第二十一批 3 候选**（=3 → discover_streak_low 保持 0）——跨作品避单作品集中，续拓 ACH 远征簇 + 补 SC 搜救簇：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 139 | johnson | The Adventures of Captain Hatteras | ACH | ACH-001 | supporting | 354 | ABSENT | ACH 补 clawbonny/shandon/captain-hatteras |
| 140 | altamont | The Adventures of Captain Hatteras | ACH | ACH-032 | supporting | 224 | ABSENT | ACH 补 clawbonny/shandon/johnson/captain-hatteras |
| 141 | olbinett | In Search of the Castaways | SC | SC-006 | supporting | 43 | ABSENT | SC 补 glenarvan/lady-helena/mary-grant/mcnabbs |

**候选说明**：
- **johnson**（ACH）——Forward 号之老水手长、历北极风霜之忠仆水手；354 mentions。ACH 远征簇（ACH-030-015 揉救 Clawbonny 冻鼻）。首现 ACH-001。
- **altamont**（ACH）——Porpoise 号之美国船长、冰原获救而与 Hatteras 争北极优先权的探险家；224 mentions。ACH 后半程核心。首现 ACH-032。
- **olbinett**（SC）——Duncan 号之司膳管事、随 Glenarvan 陆行搜救队之膳役；43 mentions。补 SC 既有簇。首现 SC-006。

**dup-check 汇总**：3 候选 exact-slug filesystem test -f 全 ABSENT（bucket jo/al/ol）；registry entity label + alias 均 ABSENT（Python 精确复验，非 grep 子串），无冲突。全 mentions ≥43 grounded。**排除（registry-catch）**：clawbonny/shandon（各既建 R422/R423，registry label EXISTS）；paganel/ayrton（各既建，registry label EXISTS）；bell/simpson（ACH 陆行队员，本批未取，留后批避单作品过度集中）。

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

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 139-141）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：本轮为 discover 轮，无建页无编辑；仅更新 grow_state + queue.md（追加候选）+ 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 filesystem dup-check ABSENT、registry entity+label+alias 精确复验无冲突。✔
- **grounding**：全 3 mentions ≥43（johnson 354、altamont 224、olbinett 43），均足支撑 ≥5 distinct solid PN。✔
- **registry-catch 排除**：clawbonny/shandon/paganel/ayrton 经 registry label EXISTS 命中既建，排除。✔
- **既有页排除**：3 候选 test -f + registry label/alias 全 ABSENT。✔
- **since_discover 归零**：3→0。✔

## 六步状态机（SCN28，grow_state 存 R426 起始计数）

| 字段 | R425 起始 | R426 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 425 | 426 |
| type_round | 117 | 118 |
| rounds_since_last_evv5 | 9 | 10 |
| rounds_since_last_discover | 3 | 0（SCN28 归零）|
| discover_streak_low | 0 | 0（new_candidates=3≥3）|
| rounds_since_last_corpus_discover | 361 | 362 |
| last_updated_round | 425 | 426 |

## 遗留问题

1. **character 页数 103（本轮无建）**：queue(character) 0→**3**（建序 139-141）。registry 全库 **1627**，unknown 0。
2. **下轮 R426 = EVV5（§3(1b)）**：since_evv5 R426 起始=**10**≥10 → §3(1b) EVV5 触发（since_discover R426 起始=0<10 → 非 §3(1a) 合并轮）。EVV5 为 character 全类型 schema-reflection 轮，pages:[]，仅 G4，不消费 queue，since_evv5 归 0。
3. **第二十一批 3 候选（建序 139-141）**：johnson/altamont/olbinett。R426 为 EVV5（不消费），R427 起 NEW1 消费 → 预计 R427-R429 消费 → queue 归 0 → R430 SCN28-zombie 补第二十二批。
4. **回链回填债**（DEFERRED，非阻塞）：**ACH 簇续拓**（johnson→clawbonny/captain-hatteras 反向、altamont→captain-hatteras/johnson 反向、shandon→captain-hatteras/clawbonny 反向、clawbonny→shandon 反向、Bell/Simpson/Wilson 待建）、**SC 簇**（olbinett→glenarvan/lady-helena/mary-grant/mcnabbs 反向、lady-helena→glenarvan/mary-grant/mcnabbs 反向、john-mangles/robert-grant/thalcave 反向）、JCE 家宅簇（martha→professor-lidenbrock/axel/grauben 反向）、FC 簇（joliffe/rae→lieutenant-hobson/mac-nab/sabine/marbre 反向、Mrs Joliffe/Mrs Rae/Mrs Mac-Nab 待建）、grauben/saknussemm/fridrikssen 反向链、samuel-fergusson/dick-kennedy→joe 反向、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R415 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R426 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=361→362（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
