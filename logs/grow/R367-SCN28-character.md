---
round: 367
date: 2026-07-19
type_round: 59
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R367 · SCN28-zombie · character — 第八批 discover：补 4 候选（engineer-serko/faruskiar/phil-evans/simon-hart），queue 0→4，since_discover 归零

## 执行摘要

Phase 2.1-B character discover 轮（type_round 59）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=5<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第七批（建序 89-98）R356-R366 全数消费（10 建：j-t-maston/captain-nicholl/cousin-benedict/mrs-weldon/captain-hull/doctor-clawbonny/tudor-brown/uncle-prudent/ker-karraje/major-noltitz），queue 归 0，触发本轮 zombie discover。

**第八批 4 候选**（≥3 → discover_streak_low 保持 0）——聚焦既有簇之配对补全，取 FF/ASC/RC 三作之反派与配角：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 99 | engineer-serko | Facing the Flag | FF | FF-003 | antagonist | 153 | ABSENT | FF 补 ker-karraje/thomas-roch |
| 100 | faruskiar | The Adventures of a Special Correspondent | ASC | ASC-008 | antagonist | 95 | ABSENT | ASC 补 major-noltitz/claudius-bombarnac |
| 101 | phil-evans | Robur the Conqueror | RC | RC-002 | supporting | 146 | ABSENT | RC 补 uncle-prudent/robur |
| 102 | simon-hart | Facing the Flag | FF | FF-001 | narrator | 103（含 Gaydon）| ABSENT | FF 补 ker-karraje/thomas-roch |

**候选说明**：
- **engineer-serko**（FF）——Ker Karraje 首席帮凶、潜艇设计者、狡黠工程师；153 mentions 跨 14 章，强 grounded。补 R365 ker-karraje 之 FF 簇。
- **faruskiar**（ASC）——伪装尊贵旅客之铁道劫匪首领、Bombarnac 一行之叛徒；95 mentions 跨 18 章。补 R366 major-noltitz 之 ASC 簇（major-noltitz/claudius-bombarnac 页均已链其名为纯文本，建后回填 wikilink）。
- **phil-evans**（RC）——Weldon Institute 秘书、Uncle Prudent 冷静对手兼同囚；146 mentions 跨 22 章。补 R364 uncle-prudent 之 RC 簇（uncle-prudent 页已纯文本提及，建后回填）。
- **simon-hart**（FF）——伪装看守 Warder Gaydon 之工程师、第一人称叙事者；直呼 Simon Hart 31 + Warder Gaydon 72 = 103 name-anchored，grounded 充分。role=narrator。补 FF 簇。**dup-check**：exact-slug simon-hart + 变体 warder-gaydon 均 filesystem+registry ABSENT。

**dup-check 汇总**：4 候选 exact-slug filesystem 全 ABSENT；registry label（Engineer Serko/Serko/Faruskiar/Phil Evans/Simon Hart/Warder Gaydon）全 ABSENT。全 mentions ≥95 grounded。

**注**：negoro（DSCF 反派厨子，275 mentions）本轮勘探复核发现 **已建**（docs/wiki/pages/ne/negoro.md 存），故不入候选——去除既有页误纳（feedback：filesystem dup-check）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=0、since_discover=11 | （被 §3(4) 先匹配）|
| **4** | **SCN28-zombie（queue(character)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 4 候选追加 queue.md（建序 99-102）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：本轮为 discover 轮，无建页无编辑；仅更新 grow_state + queue.md（追加候选）+ 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：4 候选（≥3）→ discover_streak_low 保持 0。全 filesystem+registry dup-check ABSENT。✔
- **grounding**：全 4 mentions ≥95（simon-hart 含 Warder Gaydon 别名 103），逾 55 门。✔
- **既有页排除**：negoro 复核已建，剔除（filesystem dup-check 教训）。✔
- **since_discover 归零**：11→0。✔

## 六步状态机（SCN28，grow_state 存 R368 起始计数）

| 字段 | R367 起始 | R368 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 367 | 368 |
| type_round | 59 | 60 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 11 | 0（SCN28 归零）|
| discover_streak_low | 0 | 0（new_candidates=4≥3）|
| rounds_since_last_corpus_discover | 303 | 304 |
| last_updated_round | 367 | 368 |

## 遗留问题

1. **character 页数 63（本轮无建）**：queue(character) 0→**4**（建序 99-102）。registry 全库 **1587**，unknown 0。
2. **下轮 R368 = NEW1（§3(7)）**：since_evv5=6<10；discover_streak_low=0<3；queue(character)=4>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 99（engineer-serko，book Facing the Flag，pn_anchor FF-003，role antagonist）。**下次 EVV5 于 R371 起始达 since_evv5=10。**
3. **第八批 4 候选（建序 99-102）**：engineer-serko/faruskiar/phil-evans/simon-hart。R368 起 NEW1 续消费；建序 102 消费后（R371 前）queue 归 0——但 R371 起始 since_evv5=10，§3(1b) EVV5 先于 NEW1，故 EVV5 轮先行，discover 顺延。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + 新增 major-noltitz→Faruskiar、uncle-prudent→Phil Evans、ker-karraje→Engineer Serko/Simon Hart、thomas-roch→Simon Hart/Ker Karraje（建对应页后回填 wikilink）。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R361 EVV5 复评）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=303→304（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
