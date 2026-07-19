---
round: 355
date: 2026-07-19
type_round: 47
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R355 · SCN28 · character — 第七批 discover（queue 归 0 触 §3(4) zombie；补建序 89-98 十候选，since_discover 归 0）

## 执行摘要

Phase 2.1-B character discover 轮（type_round 47），决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=4<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；queue(character)=0 → §3(3) SCN28 命中，且 §3(4) zombie 亦命中——本轮以 discover 补池）。R354 消费第六批末位建序 88（erik）后 queue(character)==0，触发第七批 discover。

**本轮补 10 候选（建序 89-98），全 filesystem+registry dup-check ABSENT，mentions ≥55 grounded**。new_candidates=10≥type_close_new_candidate_min(3) → **discover_streak_low 保持 0**（未触 CLOSE 迹象）。since_discover 归 0。pages:[]，仅 G4。

**簇策**（多为既有簇配对补全 + 单作品新簇）：
- **FEM 补**：j-t-maston（Gun Club 秘书）+ captain-nicholl（Barbicane 宿敌），配对既有 barbicane。
- **DSCF 新簇**：cousin-benedict（昆虫学表亲）+ mrs-weldon（船主之妻）+ captain-hull（Pilgrim 号船长）三页起步。
- **ACH 补**：doctor-clawbonny（博学随船医生），配对既有 captain-hatteras。
- **WC 补**：tudor-brown（阻挠 Erik 之反派），配对既有 erik。
- **RC 补**：uncle-prudent（Weldon Institute 会长），配对既有 robur。
- **FF 补**：ker-karraje（海盗首领），配对既有 thomas-roch。
- **ASC 补**：major-noltitz（俄国军医挚友），配对既有 claudius-bombarnac。

**深池策略转向**：36 部合集之主要主角多已建，第七批起转次要角色/单作品补全——既有簇之配对补全（FEM/ACH/WC/RC/FF/ASC）+ DSCF 单作品三页新簇。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=0、since_discover=9 | 命中 |
| **4** | **SCN28-zombie（queue(character)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | — |
| 7 | NEW1（默认）| — | — |

> queue(character)==0 → §3(4) zombie discover。补 10 grounded+dup-checked 候选入 queue.md，pages:[]，仅 G4，since_discover 归零。

## 页面处理记录

本轮为 discover 轮，无建页。补 10 候选入 `logs/butler/queue.md`（建序 89-98）：

| 建序 | slug | Label | book | VVV | pn_anchor | role | mentions | dup-check |
|------|------|-------|------|-----|-----------|------|----------|-----------|
| 89 | j-t-maston | J. T. Maston | From the Earth to the Moon | FEM | FEM-001 | supporting | 131 | ABSENT |
| 90 | captain-nicholl | Captain Nicholl | From the Earth to the Moon | FEM | FEM-010 | antagonist | 55 | ABSENT |
| 91 | cousin-benedict | Cousin Benedict | Dick Sand A Captain at Fifteen | DSCF | DSCF-001 | supporting | 252 | ABSENT |
| 92 | mrs-weldon | Mrs. Weldon | Dick Sand A Captain at Fifteen | DSCF | DSCF-001 | supporting | 586 | ABSENT |
| 93 | captain-hull | Captain Hull | Dick Sand A Captain at Fifteen | DSCF | DSCF-001 | supporting | 194 | ABSENT |
| 94 | doctor-clawbonny | Doctor Clawbonny | The Adventures of Captain Hatteras | ACH | ACH-002 | supporting | 199 | ABSENT |
| 95 | tudor-brown | Tudor Brown | The Waif of the Cynthia | WC | WC-010 | antagonist | 91 | ABSENT |
| 96 | uncle-prudent | Uncle Prudent | Robur the Conqueror | RC | RC-002 | supporting | 203 | ABSENT |
| 97 | ker-karraje | Ker Karraje | Facing the Flag | FF | FF-010 | antagonist | 114 | ABSENT |
| 98 | major-noltitz | Major Noltitz | The Adventures of a Special Correspondent | ASC | ASC-004 | supporting | 97 | ABSENT |

## EXIT-GATE 检查

- **G4 脚本操作**：本轮为 discover 轮，无建页；仅追加 queue.md + 更新 grow_state + 写日志，未用 Write/Edit 于 pages/**。✔
- **查重充分**：10 候选 exact-slug filesystem（遍历 pages/*/）+ pages.json entity 双检 ABSENT。✔
- **grounding 充分**：10 候选 mentions 55-586，均 ≥type_close_new_candidate_min 门以上，各有 first_appearance 章。✔
- **new_candidates≥3**：=10 → discover_streak_low 保持 0，未触 CLOSE。✔
- **since_discover 归零**：9→0。✔

## 六步状态机（SCN28，grow_state 存 R356 起始计数）

| 字段 | R355 起始 | R356 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 355 | 356 |
| type_round | 47 | 48 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 9 | 0（discover 归零）|
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 291 | 292 |
| last_updated_round | 355 | 356 |

## 遗留问题

1. **第七批 10 候选入队（建序 89-98）**：queue(character) 0→**10**。全 filesystem+registry dup-check ABSENT，mentions ≥55 grounded。registry 全库仍 **1577**，character 53，unknown 0（本轮无建页）。
2. **下轮 R356 = NEW1（§3(7)）**：since_evv5=5<10；discover_streak_low=0<3；queue(character)=10>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 89（j-t-maston，book From the Earth to the Moon，pn_anchor FEM-001，role supporting）。**下次 EVV5 于 R360 起始达 since_evv5=10。**
3. **簇成型预期**：本批消费后——FEM 三主角+（barbicane/j-t-maston/captain-nicholl）；DSCF 开簇三页；ACH 补 doctor-clawbonny；WC 配对 tudor-brown；RC 配对 uncle-prudent；FF 配对 ker-karraje；ASC 配对 major-noltitz。
4. **深池策略转向**：主要主角罄，第七批起转次要角色/单作品补全。后续批次候选 mention 门槛可能续降，需持续 exhaustive re-scan 防过早 CLOSE。
5. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、dirk-peters→Arthur Pym、william-guy→Arthur Pym、james-starr→Nell/Simon Ford、claudius-bombarnac→Major Noltitz、erik→Schwaryencrona/Durrien、captain-grant→Robert。
6. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label。
7. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
8. **散文门债 + character 内容债**（R350 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
9. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
10. **corpus-discover 顺延**：since_corpus=291→292（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
