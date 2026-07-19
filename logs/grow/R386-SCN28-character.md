---
round: 386
date: 2026-07-19
type_round: 78
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R386 · SCN28-zombie · character — 第十二批 discover：补 3 候选（tartlet/horatia-bluett/zinca-klork），queue 0→3，since_discover 归零；排除 count-dartigas（ker-karraje 别名冲突）

## 执行摘要

Phase 2.1-B character discover 轮（type_round 78）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=2<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第十一批（建序 109-111）R382/R384/R385 全数消费（3 建：pan-chao/sir-francis-trevellyan/tom-turner），queue 归 0，R385 NEW1 后本轮触发 zombie discover。

**第十二批 3 候选**（=3 → discover_streak_low 保持 0）——跳出 ASC 单作品集中，GM 新起 + ASC 既有簇配对补全：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 112 | tartlet | Godfrey Morgan | GM | GM-004 | supporting | 245 | ABSENT | GM 新起（godfrey-morgan work 页存）|
| 113 | horatia-bluett | The Adventures of a Special Correspondent | ASC | ASC-004 | supporting | 52 | ABSENT | ASC 补 ephrinell/claudius-bombarnac |
| 114 | zinca-klork | The Adventures of a Special Correspondent | ASC | ASC-004 | supporting | 51 | ABSENT | ASC 补 kinko/claudius-bombarnac |

**候选说明**：
- **tartlet**（GM）——Godfrey Morgan 之滑稽舞蹈兼体操教师、荒岛遇难的怯懦搭档；245 mentions（全库最高之一）。GM 新簇首页（godfrey-morgan work 页已存，label Godfrey Morgan）。首现 GM-004-002。
- **horatia-bluett**（ASC）——兜售束身衣之英国女行商、途中与 Ephrinell 联姻的实利主义旅客；52 mentions。补 ASC 簇（ephrinell 义齿商联姻副线之女方）。首现 ASC-004-021，label Miss Horatia Bluett。
- **zinca-klork**（ASC）——Kinko 藏身货箱所寄之罗马尼亚未婚妻、于北京翘首以待；51 mentions。补 ASC 簇（kinko 偷渡英雄之寄托）。首现 ASC-004-016，label Zinca Klork。

**排除 count-dartigas**：FF 145 mentions（全批最高），但 registry alias 检查显示「Count d'Artigas」→ **ker-karraje**（已建）。d'Artigas 即 Ker Karraje 之伪装化名，同一实体，重建将致 label/alias 冲突。故剔除，改取 zinca-klork 补位。（dup-check 纪律教训：filesystem test -f ABSENT 不足，须并查 registry alias。）

**dup-check 汇总**：3 候选 exact-slug filesystem test -f 全 ABSENT（bucket ta/ho/zi）；registry entity + label（Tartlet/Miss Horatia Bluett/Zinca Klork/各 token）均 ABSENT，不在既有 3 parked 冲突（Hector Servadac/Robur the Conqueror/Claudius Bombarnac）内，无冲突。全 mentions ≥51 grounded。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=0、since_discover=4 | （被 §3(4) 先匹配）|
| **4** | **SCN28-zombie（queue(character)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 112-114）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：本轮为 discover 轮，无建页无编辑；仅更新 grow_state + queue.md（追加候选）+ 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 filesystem dup-check ABSENT、registry entity+label 无冲突。✔
- **grounding**：全 3 mentions ≥51（tartlet 245、horatia-bluett 52、zinca-klork 51），均足支撑 ≥5 distinct solid PN。✔
- **alias 排除**：count-dartigas 经 registry alias 检查系 ker-karraje 化名，剔除（filesystem+registry 并查纪律）。✔
- **既有页排除**：3 候选 test -f 全 ABSENT。✔
- **since_discover 归零**：4→0。✔

## 六步状态机（SCN28，grow_state 存 R387 起始计数）

| 字段 | R386 起始 | R387 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 386 | 387 |
| type_round | 78 | 79 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 4 | 0（SCN28 归零）|
| discover_streak_low | 0 | 0（new_candidates=3≥3）|
| rounds_since_last_corpus_discover | 322 | 323 |
| last_updated_round | 386 | 387 |

## 遗留问题

1. **character 页数 76（本轮无建）**：queue(character) 0→**3**（建序 112-114）。registry 全库 **1600**，unknown 0。
2. **下轮 R387 = NEW1（§3(7)）**：since_evv5=3<10 → §3(1) 否；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 112（tartlet，book Godfrey Morgan，pn_anchor GM-004，role supporting）。**下次 EVV5 于 R393 起始达 since_evv5=10（§3(1b)）。**
3. **第十二批 3 候选（建序 112-114）**：tartlet/horatia-bluett/zinca-klork。R387-R389 NEW1 消费；建序 114 消费后（R389 末）queue 归 0 → R390 SCN28-zombie 补第十三批。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan、claudius-bombarnac/major-noltitz→Pan Chao、ephrinell/kinko→（待建 horatia-bluett/zinca-klork 回链）。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R383 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=322→323（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
