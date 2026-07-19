---
round: 377
date: 2026-07-19
type_round: 69
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R377 · SCN28-zombie · character — 第十批 discover：补 3 候选（caterna/popof/ephrinell），queue 0→3，since_discover 归零

## 执行摘要

Phase 2.1-B character discover 轮（type_round 69）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=4<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第九批（建序 103-105）R374-R376 全数消费（3 建：captain-spade/frycollin/kinko），queue 归 0，R376 NEW1 后本轮触发 zombie discover。

**第十批 3 候选**（=3 → discover_streak_low 保持 0）——ASC 单作品高频配角深挖，聚焦 Bombarnac 旅伴群像：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 106 | caterna | The Adventures of a Special Correspondent | ASC | ASC-004 | supporting | 140 | ABSENT | ASC 补 claudius-bombarnac/pan-chao |
| 107 | popof | The Adventures of a Special Correspondent | ASC | ASC-005 | supporting | 114 | ABSENT | ASC 补 claudius-bombarnac/faruskiar |
| 108 | ephrinell | The Adventures of a Special Correspondent | ASC | ASC-002 | supporting | 103 | ABSENT | ASC 补 claudius-bombarnac |

**候选说明**：
- **caterna**（ASC）——随妻同游之法国喜剧演员、Bombarnac 铁道旅途之欢乐旅伴；140 mentions（全库最高之一）。补 ASC 簇（claudius-bombarnac/pan-chao 旅伴群像）。首现 ASC-004-043。
- **popof**（ASC）——Grand Transasiatic 列车长、Bombarnac 之消息来源与旅途向导；114 mentions。补 ASC 簇（claudius-bombarnac 消息源，faruskiar 劫案时值守）。首现 ASC-005-020。
- **ephrinell**（ASC）——兜售义齿之美国行商、与 Miss Bluett 途中联姻的实利主义旅客；103 mentions。补 ASC 簇（claudius-bombarnac 观察之联姻副线）。首现 ASC-002-027。

**dup-check 汇总**：3 候选 exact-slug filesystem test -f 全 ABSENT；registry entity（caterna/popof/ephrinell）与 label（Caterna/Popof/Ephrinell）均 ABSENT，不在既有 3 parked 冲突（Hector Servadac/Robur the Conqueror/Claudius Bombarnac）内，无冲突。全 mentions ≥103 grounded。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=0、since_discover=3 | （被 §3(4) 先匹配）|
| **4** | **SCN28-zombie（queue(character)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 106-108）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：本轮为 discover 轮，无建页无编辑；仅更新 grow_state + queue.md（追加候选）+ 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 filesystem dup-check ABSENT、registry 无冲突。✔
- **grounding**：全 3 mentions ≥103（caterna 140、popof 114、ephrinell 103），逾 55 门。✔
- **既有页排除**：3 候选 test -f 全 ABSENT（negoro 误纳教训——filesystem dup-check）。✔
- **since_discover 归零**：3→0。✔

## 六步状态机（SCN28，grow_state 存 R378 起始计数）

| 字段 | R377 起始 | R378 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 377 | 378 |
| type_round | 69 | 70 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 3 | 0（SCN28 归零）|
| discover_streak_low | 0 | 0（new_candidates=3≥3）|
| rounds_since_last_corpus_discover | 313 | 314 |
| last_updated_round | 377 | 378 |

## 遗留问题

1. **character 页数 70（本轮无建）**：queue(character) 0→**3**（建序 106-108）。registry 全库 **1594**，unknown 0。
2. **下轮 R378 = NEW1（§3(7)）**：since_evv5=5<10；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 106（caterna，book The Adventures of a Special Correspondent，pn_anchor ASC-004，role supporting）。**下次 EVV5 于 R382 起始达 since_evv5=10（§3(1b)）。**
3. **第十批 3 候选（建序 106-108）**：caterna/popof/ephrinell。R378-R380 NEW1 续消费；建序 108 消费后（R380 末）queue 归 0 → R381 SCN28-zombie 补第十一批（但 R382 EVV5 逼近，注意 §3 优先级）。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + claudius-bombarnac/pan-chao→Caterna、claudius-bombarnac/faruskiar→Popof、claudius-bombarnac→Ephrinell（建对应页后回填 wikilink）、faruskiar/claudius-bombarnac→Kinko。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R372 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=313→314（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
