---
round: 390
date: 2026-07-19
type_round: 82
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R390 · SCN28-zombie · character — 第十三批 discover：补 3 候选（carefinotu/sergeant-long/william-kolderup），queue 0→3，since_discover 归零；排除 jasper-hobson（lieutenant-hobson 同一实体）、paulina-barnett（已建）

## 执行摘要

Phase 2.1-B character discover 轮（type_round 82）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=6<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第十二批（建序 112-114）R387-R389 全数消费（3 建：tartlet/horatia-bluett/zinca-klork），queue 归 0，R389 NEW1 后本轮触发 zombie discover。

**第十三批 3 候选**（=3 → discover_streak_low 保持 0）——深挖 GM + FC 两既有簇，避单作品集中：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 115 | carefinotu | Godfrey Morgan | GM | GM-018 | supporting | 90 | ABSENT | GM 补 tartlet |
| 116 | sergeant-long | The Fur Country | FC | FC-001 | supporting | 233 | ABSENT | FC 补 lieutenant-hobson/paulina-barnett |
| 117 | william-kolderup | Godfrey Morgan | GM | GM-001 | supporting | 88 | ABSENT | GM 补 tartlet/carefinotu |

**候选说明**：
- **carefinotu**（GM）——Godfrey 荒岛所救之忠仆、火中脱险的黑人「星期五」；90 mentions。补 GM 簇（tartlet/godfrey-morgan work）。首现 GM-018-007。
- **sergeant-long**（FC）——Jasper Hobson 之坚毅副手、探险队军士；233 mentions。补 FC 簇（既有 lieutenant-hobson/paulina-barnett 2 页）。首现 FC-001-011。
- **william-kolderup**（GM）——Godfrey 之富豪叔父兼监护人、旧金山巨贾、安排环游之纳博布；88 mentions。补 GM 簇（tartlet/carefinotu）。首现 GM-001-053。

**排除**：
- **jasper-hobson**（FC 591 mentions，全批最高）——registry alias 检查显示「Lieutenant Hobson」→ **lieutenant-hobson**（已建）。Jasper Hobson 即 Lieutenant Hobson 同一实体（The Fur Country 主角），重建将致 label/alias 冲突。剔除。
- **paulina-barnett**（FC 49 mentions）——filesystem test -f + entity 均 EXISTS（已建）。剔除。

**dup-check 汇总**：3 候选 exact-slug filesystem test -f 全 ABSENT（bucket ca/se/wi）；registry entity + label（Carefinotu/Sergeant Long/William W. Kolderup/各 token）均 ABSENT，不在既有 3 parked 冲突（Hector Servadac/Robur the Conqueror/Claudius Bombarnac）内，无冲突。全 mentions ≥88 grounded。**教训延续**：filesystem + registry alias 并查（R386 count-dartigas、本轮 jasper-hobson 皆经 alias 检查捕获同一实体）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| queue=0、since_discover=3 | （被 §3(4) 先匹配）|
| **4** | **SCN28-zombie（queue(character)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 115-117）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：本轮为 discover 轮，无建页无编辑；仅更新 grow_state + queue.md（追加候选）+ 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 filesystem dup-check ABSENT、registry entity+label 无冲突。✔
- **grounding**：全 3 mentions ≥88（sergeant-long 233、carefinotu 90、william-kolderup 88），均足支撑 ≥5 distinct solid PN。✔
- **alias 排除**：jasper-hobson 系 lieutenant-hobson 同一实体（registry alias），paulina-barnett 已建（filesystem），均剔除。✔
- **既有页排除**：3 候选 test -f 全 ABSENT。✔
- **since_discover 归零**：3→0。✔

## 六步状态机（SCN28，grow_state 存 R391 起始计数）

| 字段 | R390 起始 | R391 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 390 | 391 |
| type_round | 82 | 83 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 3 | 0（SCN28 归零）|
| discover_streak_low | 0 | 0（new_candidates=3≥3）|
| rounds_since_last_corpus_discover | 326 | 327 |
| last_updated_round | 390 | 391 |

## 遗留问题

1. **character 页数 79（本轮无建）**：queue(character) 0→**3**（建序 115-117）。registry 全库 **1603**，unknown 0。
2. **下轮 R391 = NEW1（§3(7)）**：since_evv5=7<10 → §3(1) 否；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 115（carefinotu，book Godfrey Morgan，pn_anchor GM-018，role supporting）。**下次 EVV5 于 R393 起始达 since_evv5=10（§3(1b)）——即 R391 NEW1（carefinotu）→ R392 NEW1（sergeant-long）→ R393 EVV5（不消费）→ R394 NEW1（william-kolderup）。**
3. **第十三批 3 候选（建序 115-117）**：carefinotu/sergeant-long/william-kolderup。R391-R392 NEW1 消费；R393 EVV5 间隔；R394 NEW1 消费建序 117 → queue 归 0 → R395 SCN28-zombie 补第十四批。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。GM/FC 新建可回链 tartlet/lieutenant-hobson/paulina-barnett。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan——若后建 Godfrey 角色页则触发新同名冲突，暂缓）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R383 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=326→327（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
