---
round: 373
date: 2026-07-19
type_round: 65
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R373 · SCN28-zombie · character — 第九批 discover：补 3 候选（captain-spade/frycollin/kinko），queue 0→3，since_discover 归零

## 执行摘要

Phase 2.1-B character discover 轮（type_round 65）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=0<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第八批（建序 99-102）R368-R371 全数消费（4 建：engineer-serko/faruskiar/phil-evans/simon-hart），queue 归 0，R372 EVV5 后本轮触发 zombie discover。

**第九批 3 候选**（=3 → discover_streak_low 保持 0）——延续既有簇之配对补全，取 FF/RC/ASC 三作之打手/仆从/隐藏英雄：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 103 | captain-spade | Facing the Flag | FF | FF-001 | antagonist | 98 | ABSENT | FF 补 engineer-serko/simon-hart/ker-karraje |
| 104 | frycollin | Robur the Conqueror | RC | RC-002 | supporting | 79 | ABSENT | RC 补 uncle-prudent/phil-evans/robur |
| 105 | kinko | The Adventures of a Special Correspondent | ASC | ASC-013 | supporting | 106 | ABSENT | ASC 补 faruskiar/claudius-bombarnac |

**候选说明**：
- **captain-spade**（FF）——Ker Karraje 之打手、劫持 Thomas Roch 的纵帆船长；98 mentions。补 FF 簇（engineer-serko/simon-hart 页已纯文本提及 Spade，建后可回填 wikilink）。首现 FF-001-007。
- **frycollin**（RC）——Uncle Prudent 之胆怯黑人仆从、Albatross 上喜剧配角；79 mentions。补 RC 簇（phil-evans 页已纯文本提及 Frycollin，uncle-prudent 页亦涉，建后回填）。首现 RC-002-019。
- **kinko**（ASC）——藏身货箱偷渡之罗马尼亚青年、拯救列车却隐名的无名英雄；106 mentions。补 ASC 簇（faruskiar 情节中 Kinko 为真英雄，claudius-bombarnac 为其守秘）。首现 ASC-013-078。

**dup-check 汇总**：3 候选 exact-slug filesystem test -f 全 ABSENT；registry label（Captain Spade/Frycollin/Kinko）均不在既有 3 parked 冲突（Hector Servadac/Robur/Claudius Bombarnac）内，无冲突。全 mentions ≥79 grounded。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=0、since_discover=5 | （被 §3(4) 先匹配）|
| **4** | **SCN28-zombie（queue(character)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 103-105）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：本轮为 discover 轮，无建页无编辑；仅更新 grow_state + queue.md（追加候选）+ 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 filesystem dup-check ABSENT、registry 无冲突。✔
- **grounding**：全 3 mentions ≥79（captain-spade 98、frycollin 79、kinko 106），逾 55 门。✔
- **既有页排除**：3 候选 test -f 全 ABSENT（negoro 误纳教训——filesystem dup-check）。✔
- **since_discover 归零**：5→0。✔

## 六步状态机（SCN28，grow_state 存 R374 起始计数）

| 字段 | R373 起始 | R374 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 373 | 374 |
| type_round | 65 | 66 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 5 | 0（SCN28 归零）|
| discover_streak_low | 0 | 0（new_candidates=3≥3）|
| rounds_since_last_corpus_discover | 309 | 310 |
| last_updated_round | 373 | 374 |

## 遗留问题

1. **character 页数 67（本轮无建）**：queue(character) 0→**3**（建序 103-105）。registry 全库 **1591**，unknown 0。
2. **下轮 R374 = NEW1（§3(7)）**：since_evv5=1<10；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 103（captain-spade，book Facing the Flag，pn_anchor FF-001，role antagonist）。**下次 EVV5 于 R382 起始达 since_evv5=10（§3(1b)）。**
3. **第九批 3 候选（建序 103-105）**：captain-spade/frycollin/kinko。R374-R376 NEW1 续消费；建序 105 消费后（R376 末）queue 归 0 → R377 SCN28-zombie 补第十批。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + engineer-serko/simon-hart/ker-karraje→Captain Spade、uncle-prudent/phil-evans→Frycollin、faruskiar/claudius-bombarnac→Kinko（建对应页后回填 wikilink）。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R372 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=309→310（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
