---
round: 417
date: 2026-07-19
type_round: 109
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R417 · SCN28-zombie · character — 第十九批 discover：补 3 候选（joliffe/rae/martha），queue 0→3，since_discover 归零；收束 FC 军民匠役 + JCE 家仆补全

## 执行摘要

Phase 2.1-B character discover 轮（type_round 109）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=1<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第十八批（建序 130-132）R413-R416 全数消费（3 建：marbre/saknussemm/grauben，中隔 R415 EVV5），queue 归 0，本轮触发 zombie discover。

**第十九批 3 候选**（=3 → discover_streak_low 保持 0）——收束 FC 与 JCE 两簇余下具名配角：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 133 | joliffe | The Fur Country | FC | FC-001 | supporting | 96 | ABSENT | FC 补 lieutenant-hobson/mac-nab/sabine/marbre |
| 134 | rae | The Fur Country | FC | FC-001 | supporting | 30 | ABSENT | FC 补 mac-nab/marbre |
| 135 | martha | A Journey to the Center of the Earth | JCE | JCE-001 | supporting | 24 | ABSENT | JCE 补 professor-lidenbrock/axel/grauben |

**候选说明**：
- **joliffe**（FC）——Fort Hope 之下士司务、精于分派物资又爱管闲事的忙碌军曹；96 mentions。补 FC 簇。首现 FC-001。
- **rae**（FC）——探险队之铁匠、Fort Hope 营建之匠人；30 mentions。补 FC 簇（Rae 于 FC-035-005 与 mac-nab 并列受 marbre 告知浮岛之危）。首现 FC-001。
- **martha**（JCE）——Lidenbrock 教授之忠仆女佣、Königstrasse 宅邸之持家人；24 mentions。补 JCE 簇（完足 Lidenbrock 家宅：教授/Axel/Gräuben/Martha）。首现 JCE-001。

**dup-check 汇总**：3 候选 exact-slug filesystem test -f 全 ABSENT（bucket jo/ra/ma）；registry entity label + alias 均 ABSENT，无冲突。全 mentions ≥24 grounded。**排除**：servadac（filesystem test -f 假 ABSENT 但 registry label「Hector Servadac」既有 slug hector-servadac，同一实体已建，另触 HK(e) character-vs-work 同名——registry 查捕获，教训延续 R412 impey-barbicane/R403 pierre-aronnax）；herbert/neb/pencroft/ayrton/uncle-prudent/phil-evans/dick-sand/hercules（各主角既建，filesystem EXISTS）；nicholl（FEM/RM/TT 多值 book HK(d) 暂缓）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=0、since_discover=4 | （被 §3(4) 先匹配）|
| **4** | **SCN28-zombie（queue(character)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 133-135）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：本轮为 discover 轮，无建页无编辑；仅更新 grow_state + queue.md（追加候选）+ 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 filesystem dup-check ABSENT、registry entity+label+alias 无冲突。✔
- **grounding**：全 3 mentions ≥24（joliffe 96、rae 30、martha 24），均足支撑 ≥5 distinct solid PN。✔
- **alias 排除**：servadac 经 registry label 复验命中既有 slug hector-servadac（另 HK(e)），排除；nicholl 多值 book 暂缓。✔
- **既有页排除**：3 候选 test -f + registry label/alias 全 ABSENT；各主角 filesystem EXISTS 已排除。✔
- **since_discover 归零**：4→0。✔

## 六步状态机（SCN28，grow_state 存 R418 起始计数）

| 字段 | R417 起始 | R418 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 417 | 418 |
| type_round | 109 | 110 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 4 | 0（SCN28 归零）|
| discover_streak_low | 0 | 0（new_candidates=3≥3）|
| rounds_since_last_corpus_discover | 353 | 354 |
| last_updated_round | 417 | 418 |

## 遗留问题

1. **character 页数 97（本轮无建）**：queue(character) 0→**3**（建序 133-135）。registry 全库 **1621**，unknown 0。
2. **下轮 R418 = NEW1（§3(7)）**：since_evv5=2<10；queue=3>0 且 since_discover=0<10 → NEW1，消费建序 133 **joliffe**（FC 下士司务，96 mentions，配对 [[Jaspar Hobson]]/[[Mac-Nab]]/[[Sabine]]/[[Marbre]]）。
3. **第十九批 3 候选（建序 133-135）**：joliffe/rae/martha。R418-R420 NEW1 消费 → queue 归 0 → R421 SCN28-zombie 补第二十批。**EVV5 时点**：since_evv5 R418 起始=2，逐轮 +1 → R426 起始=10 → **R426 = §3(1b) EVV5**（除非期间 discover 令 since_discover≥10 触发 §3(1a) 合并轮）。
4. **回链回填债**（DEFERRED，非阻塞）：FC 簇（joliffe/rae→lieutenant-hobson/mac-nab/sabine/marbre 反向、sabine↔marbre 反向）、JCE 簇（martha→professor-lidenbrock/axel/grauben 反向、grauben/saknussemm/fridrikssen 反向链）、FWB（samuel-fergusson/dick-kennedy→joe 反向）、Mrs Mac-Nab 待建、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R415 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R426 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=353→354（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
