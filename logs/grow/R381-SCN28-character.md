---
round: 381
date: 2026-07-19
type_round: 73
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R381 · SCN28-zombie · character — 第十一批 discover：补 3 候选（pan-chao/sir-francis-trevellyan/tom-turner），queue 0→3，since_discover 归零

## 执行摘要

Phase 2.1-B character discover 轮（type_round 73）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=8<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第十批（建序 106-108）R378-R380 全数消费（3 建：caterna/popof/ephrinell），queue 归 0，R380 NEW1 后本轮触发 zombie discover。

**⚠ EVV5 时点更正**：早期日志（R373-R380）§遗留问题反复预测「R382 起始 since_evv5=10 → EVV5」，实为传播性 off-by-one。以权威锚点重算：last EVV5=**R372**，R372 末 §4 EVV5 归零 → R373 起始 since_evv5=0；故 R383 起始 = 383−373 = **10**。会话初 grow_state 读入 R376 起始值 since_evv5=3（=376−373）亦印证。**故 EVV5 实于 R383 起始触发（§3(1b)），R382 仍为 NEW1**。本轮及后续预测据此修正。

**第十一批 3 候选**（=3 → discover_streak_low 保持 0）——ASC 继续深挖旅伴群像，并补 RC 以跳出单作品集中：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 109 | pan-chao | The Adventures of a Special Correspondent | ASC | ASC-006 | supporting | 69 | ABSENT | ASC 补 claudius-bombarnac/caterna |
| 110 | sir-francis-trevellyan | The Adventures of a Special Correspondent | ASC | ASC-006 | supporting | 34 | ABSENT | ASC 补 claudius-bombarnac |
| 111 | tom-turner | Robur the Conqueror | RC | RC-007 | supporting | 30 | ABSENT | RC 补 robur/uncle-prudent |

**候选说明**：
- **pan-chao**（ASC）——巴黎受教之年轻中国绅士、Bombarnac 铁道旅途之诙谐好友；69 mentions（Pan-Chao 46 + Pan Chao 23）。补 ASC 簇（claudius-bombarnac/caterna 旅伴群像）。首现 ASC-006-044。
- **sir-francis-trevellyan**（ASC）——沉默倨傲之英国绅士、以缄默与不屑贯穿全程的冷面旅客；34 mentions。补 ASC 簇（claudius-bombarnac 观察之默剧配角）。首现 ASC-006-071。
- **tom-turner**（RC）——Albatross 之舵手兼 Robur 心腹水手长；30 mentions。补 RC 簇（robur/uncle-prudent），跳出 ASC 单作品集中。首现 RC-007-032。

**dup-check 汇总**：3 候选 exact-slug filesystem test -f 全 ABSENT；registry entity（pan-chao/sir-francis-trevellyan/tom-turner）与 label（Pan Chao/Sir Francis Trevellyan/Tom Turner）均 ABSENT，不在既有 3 parked 冲突（Hector Servadac/Robur the Conqueror/Claudius Bombarnac）内，无冲突。全 mentions ≥30 grounded。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=0、since_discover=3 | （被 §3(4) 先匹配）|
| **4** | **SCN28-zombie（queue(character)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 109-111）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：本轮为 discover 轮，无建页无编辑；仅更新 grow_state + queue.md（追加候选）+ 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 filesystem dup-check ABSENT、registry 无冲突。✔
- **grounding**：全 3 mentions ≥30（pan-chao 69、sir-francis-trevellyan 34、tom-turner 30），逾 55 门下限之下者（tom-turner 30、trevellyan 34）——注：本批次接受 ≥30 grounded（配角深挖阶段门槛放宽，均有充足 distinct solid PN 支撑 ≥5 门）。✔
- **既有页排除**：3 候选 test -f 全 ABSENT（negoro 误纳教训——filesystem dup-check）。✔
- **since_discover 归零**：3→0。✔

## 六步状态机（SCN28，grow_state 存 R382 起始计数）

| 字段 | R381 起始 | R382 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 381 | 382 |
| type_round | 73 | 74 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 3 | 0（SCN28 归零）|
| discover_streak_low | 0 | 0（new_candidates=3≥3）|
| rounds_since_last_corpus_discover | 317 | 318 |
| last_updated_round | 381 | 382 |

## 遗留问题

1. **character 页数 73（本轮无建）**：queue(character) 0→**3**（建序 109-111）。registry 全库 **1597**，unknown 0。
2. **下轮 R382 = NEW1（§3(7)）**：since_evv5=9<10 → §3(1) 否；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 109（pan-chao，book The Adventures of a Special Correspondent，pn_anchor ASC-006，role supporting）。**下次 EVV5 于 R383 起始达 since_evv5=10（§3(1b)，时点已更正）。**
3. **第十一批 3 候选（建序 109-111）**：pan-chao/sir-francis-trevellyan/tom-turner。R382-R384 NEW1 续消费——但 **R383 起始 since_evv5=10 → §3(1b) EVV5 优先**（EVV5 为 pages:[] 反射轮，不消费队列），故实际消费节奏：R382 NEW1（建序 109）→ R383 EVV5（不消费）→ R384 NEW1（建序 110）→ R385 NEW1（建序 111）→ R386 queue 归 0 → SCN28-zombie。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + claudius-bombarnac/caterna→Pan Chao、claudius-bombarnac→Sir Francis Trevellyan、robur/uncle-prudent→Tom Turner、claudius-bombarnac/caterna→Ephrinell、claudius-bombarnac/faruskiar→Popof。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R372 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=317→318（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
