---
round: 345
date: 2026-07-19
type_round: 37
phase: "2.1"
current_type: character
gene: SCN28-zombie
pages: []
result: success
---

# GROW 2.1-B · R345 · SCN28-zombie · character — 第六批 discover：补充 8 候选（建序 81–88），queue(character) 0→8

## 执行摘要

Phase 2.1-B character discover 轮（type_round 37）。R344 消费建序 80（len-guy，第五批末位）后 **queue(character)=0**，决策机 §3 首匹配 **SCN28-zombie**
（since_evv5=4<10 → 1a/1b 否；discover_streak_low=0<3 → 2 否；§3(3) queue<10 成立且 §3(4) queue==0 成立 → **SCN28 discover 触发**）。本轮 pages:[]，仅补候选队列，不建页。

**补充 8 候选（建序 81–88）**，全 filesystem + registry dup-check **ABSENT**，全 grounded（sentence_index mentions ≥51 且有 first_pn）：

| 建序 | slug | Label | book | pn_anchor | role | mentions | 簇 |
|------|------|-------|------|-----------|------|----------|----|
| 81 | paulina-barnett | Paulina Barnett | The Fur Country | FC-001 | supporting | 465 | 配对 lieutenant-hobson（FC） |
| 82 | palmyrin-rosette | Palmyrin Rosette | Off on a Comet | OC-027 | supporting | 96 | 扩 hector-servadac/ben-zoof（OC） |
| 83 | dirk-peters | Dirk Peters | An Antarctic Mystery | AM-004 | supporting | 180 | 配对 len-guy（AM） |
| 84 | william-guy | William Guy | An Antarctic Mystery | AM-005 | supporting | 63 | 配对 len-guy（AM） |
| 85 | james-starr | James Starr | The Underground City | UC-001 | protagonist | 276 | 新簇种子（UC） |
| 86 | nell | Nell | The Underground City | UC-012 | supporting | 170 | 配对 james-starr（UC） |
| 87 | claudius-bombarnac | Claudius Bombarnac | The Special Correspondent | ASC-001 | narrator | 51 | 新簇种子（ASC） |
| 88 | erik | Erik | The Waif of the Cynthia | WC-001 | protagonist | 415 | 新簇种子（WC） |

8≥3 → **discover_streak_low 保持 0**。since_discover 归 0。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a | EVV5+SCN28（since_evv5≥10 且 since_discover≥10）| evv5=4、disc=7 | 否 |
| 1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue(character)=0<10 | **成立** |
| **4** | **SCN28-zombie（queue(character)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | — |
| 7 | NEW1（默认）| — | — |

> queue==0 → §3(3)/§3(4) 同真，走 SCN28-zombie 补池。

## 候选 grounding + dup-check 记录

- **grounding**：逐候选 grep sentence_index（data/sentence_index/{VVV}-*.jsonl），取 mentions 总数 + 首现 pn。全 ≥51 mentions（最高 paulina-barnett 465、erik 415），均有 first_pn，corpus 存在性确认。
- **dup-check**：8 slug 全 `ls docs/wiki/pages/*/<slug>.md` 无匹配 + pages.json registry 无 key → 全 ABSENT。
- **簇策**：FC 补 paulina-barnett 配对 lieutenant-hobson；OC 扩 palmyrin-rosette；AM 双补 dirk-peters/william-guy 配对 len-guy；UC 新起 james-starr/nell 配对；ASC/WC 各单主角起新簇。

## EXIT-GATE 检查（discover 轮仅 G4 适用）

- **G4 脚本操作**：本轮不建页，仅 Edit 追加 logs/butler/queue.md（非 pages/**）。✔
- **无 pages 变更**：pages:[]，registry 不变（1569 character 45 unknown 0）。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（SCN28，grow_state 存 R346 起始计数）

| 字段 | R345 起始 | R346 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 345 | 346 |
| type_round | 37 | 38 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 7 | 0 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 281 | 282 |
| last_updated_round | 345 | 346 |

## 遗留问题

1. **queue(character) 0→8**（建序 81–88）。character 页数仍 45，registry 1569，unknown 0（discover 不建页）。
2. **下轮 R346 = NEW1（§3(7)）**：since_evv5=5<10；discover_streak_low=0<3；queue(character)=8>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 81（paulina-barnett）。FC 簇配对 lieutenant-hobson，建后回填互链。
3. **下次 EVV5 预判**：since_evv5 上次归零 R340，R350 起始达 10 → EVV5 约 R350 触发（届时 queue 尚余候选，1b 优先于 NEW1）。
4. **深池渐罄提示**：36 部合集主要角色多已建/在队；本批后深池主角候选趋少，后续批次将转次要角色补全或单作品配对。Mathias Sandorf/Kaw-djer/Wilhelm Storitz/Kéraban 确认不在本 36 部合集（勿再列）。
5. **回链回填债**（DEFERRED，非阻塞）：hector-servadac→Ben Zoof、lieutenant-hobson→Barnett/Long、thomas-roch→Simon Hart/Ker Karraje、len-guy→William Guy/Jeorling、captain-grant→Robert。建对应页后 edit_page 回填。
6. **HK(e) character-vs-work 同名 label 张力**：hector-servadac vs off-on-a-comet alias，parked。EVV6/HK 批处理裁决。
7. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label。
8. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
9. **散文门债 + character 内容债**（R340 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
10. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
11. **corpus-discover 顺延**：since_corpus=281→282（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
