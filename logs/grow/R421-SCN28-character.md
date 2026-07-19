---
round: 421
date: 2026-07-19
type_round: 113
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R421 · SCN28-zombie · character — 第二十批 discover：补 3 候选（clawbonny/shandon/lady-helena），queue 0→3，since_discover 归零；开 ACH（Captain Hatteras）新簇 + 补 SC（Castaways）既有簇

## 执行摘要

Phase 2.1-B character discover 轮（type_round 113）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=5<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第十九批（建序 133-135）R418-R420 全数消费（3 建：joliffe/rae/martha），queue 归 0，本轮触发 zombie discover。

**第二十批 3 候选**（=3 → discover_streak_low 保持 0）——跨作品避单作品集中，开 ACH 新簇 + 补 SC 既有簇：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 136 | clawbonny | The Adventures of Captain Hatteras | ACH | ACH-002 | supporting | 199 | ABSENT | ACH 新簇 开 captain-hatteras |
| 137 | shandon | The Adventures of Captain Hatteras | ACH | ACH-001 | supporting | 261 | ABSENT | ACH 新簇 补 clawbonny/captain-hatteras |
| 138 | lady-helena | In Search of the Castaways | SC | SC-001 | supporting | 274 | ABSENT | SC 补 glenarvan/john-mangles/mary-grant/robert-grant/mcnabbs/thalcave |

**候选说明**：
- **clawbonny**（ACH）——Forward 号之博学好脾气随船医生、Hatteras 北极远征之百科全书式伙伴；199 mentions。开 ACH 新簇。首现 ACH-002。
- **shandon**（ACH）——Forward 号之大副兼受命指挥官、招募船员而不知船长身份的利物浦航海家；261 mentions。ACH 新簇。首现 ACH-001。
- **lady-helena**（SC）——Lord Glenarvan 之贤妻、力主搜救 Grant 船长遗孤的 Duncan 号女主人；274 mentions。补 SC 既有簇（六页 glenarvan/john-mangles/mary-grant/robert-grant/mcnabbs/thalcave）。首现 SC-001。

**dup-check 汇总**：3 候选 exact-slug filesystem test -f 全 ABSENT（bucket cl/sh/la）；registry entity label + alias 均 ABSENT，无冲突。全 mentions ≥199 grounded。**排除（registry-catch）**：glenarvan（filesystem gl/glenarvan EXISTS + registry label「Lord Glenarvan」→ 既有 slug glenarvan，同一实体已建）；mangles（filesystem 假 ABSENT 但 registry label「John Mangles」→ 既有 slug john-mangles，教训延续 R417 servadac/R412 impey-barbicane/R403 pierre-aronnax）；mcnabbs（registry label「Major McNabbs」→ 既有 slug mcnabbs，另触 HK(f) 同名异实体 Mac-Nab vs Major McNabbs）；mary-grant/robert-grant/thalcave/captain-hatteras（各既建，registry label EXISTS）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=0、since_discover=3 | （被 §3(4) 先匹配）|
| **4** | **SCN28-zombie（queue(character)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 136-138）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：本轮为 discover 轮，无建页无编辑；仅更新 grow_state + queue.md（追加候选）+ 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 filesystem dup-check ABSENT、registry entity+label+alias 无冲突。✔
- **grounding**：全 3 mentions ≥199（lady-helena 274、shandon 261、clawbonny 199），均足支撑 ≥5 distinct solid PN。✔
- **registry-catch 排除**：glenarvan（filesystem EXISTS + label）、mangles（label John Mangles → john-mangles）、mcnabbs（label Major McNabbs，另 HK(f)）经 registry 复验命中既建，排除。✔
- **既有页排除**：3 候选 test -f + registry label/alias 全 ABSENT；mary-grant/robert-grant/thalcave/captain-hatteras registry label EXISTS 已排除。✔
- **since_discover 归零**：3→0。✔

## 六步状态机（SCN28，grow_state 存 R422 起始计数）

| 字段 | R421 起始 | R422 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 421 | 422 |
| type_round | 113 | 114 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 3 | 0（SCN28 归零）|
| discover_streak_low | 0 | 0（new_candidates=3≥3）|
| rounds_since_last_corpus_discover | 357 | 358 |
| last_updated_round | 421 | 422 |

## 遗留问题

1. **character 页数 100（本轮无建）**：queue(character) 0→**3**（建序 136-138）。registry 全库 **1624**，unknown 0。
2. **下轮 R422 = NEW1（§3(7)）**：since_evv5=6<10；queue=3>0 且 since_discover=0<10 → NEW1，消费建序 136 **clawbonny**（ACH 随船医生，199 mentions，开 ACH 新簇，配对 [[Captain Hatteras]]）。
3. **第二十批 3 候选（建序 136-138）**：clawbonny/shandon/lady-helena。R422-R424 NEW1 消费 → queue 归 0 → R425 SCN28-zombie 补第二十一批。**EVV5 时点**：since_evv5 R422 起始=6，逐轮 +1 → R426 起始=10 → **R426 = §3(1b) EVV5**（除非期间 discover 令 since_discover≥10 触发 §3(1a) 合并轮）。
4. **回链回填债**（DEFERRED，非阻塞）：ACH 新簇（clawbonny/shandon→captain-hatteras 反向、clawbonny↔shandon 反向）、SC 簇（lady-helena→glenarvan/john-mangles/mary-grant/robert-grant/mcnabbs/thalcave 反向）、JCE 家宅簇（martha→professor-lidenbrock/axel/grauben 反向）、FC 簇（joliffe/rae→lieutenant-hobson/mac-nab/sabine/marbre 反向、Mrs Joliffe/Mrs Rae/Mrs Mac-Nab 待建）、grauben/saknussemm/fridrikssen 反向链、samuel-fergusson/dick-kennedy→joe 反向、hans-bjelke↔professor-lidenbrock/axel 反向、william-kolderup→J. R. Taskinar、kalumah/madge/paulina-barnett/sergeant-long→Thomas Black、paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan）；（f）同名异实体人物 label（Mac-Nab vs Major McNabbs）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R415 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。下次 EVV5 R426 复评。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=357→358（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
