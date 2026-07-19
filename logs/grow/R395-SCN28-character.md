---
round: 395
date: 2026-07-19
type_round: 87
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R395 · SCN28-zombie · character — 第十四批 discover：补 3 候选（kalumah/phina-hollaney/madge），queue 0→3，since_discover 归零；FC 补 kalumah/madge、GM 补 phina-hollaney，避单作品集中

## 执行摘要

Phase 2.1-B character discover 轮（type_round 87）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=1<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第十三批（建序 115-117）R391-R394 全数消费（3 建：carefinotu/sergeant-long/william-kolderup），R393 EVV5 间隔，queue 归 0，本轮触发 zombie discover。

**第十四批 3 候选**（=3 → discover_streak_low 保持 0）——深挖 FC + GM 两既有簇，避单作品集中：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 118 | kalumah | The Fur Country | FC | FC-019 | supporting | 93 | ABSENT | FC 补 paulina-barnett/lieutenant-hobson/sergeant-long |
| 119 | phina-hollaney | Godfrey Morgan | GM | GM-003 | supporting | 85 | ABSENT | GM 补 william-kolderup/tartlet/carefinotu |
| 120 | madge | The Fur Country | FC | FC-001 | supporting | 106 | ABSENT | FC 补 paulina-barnett/lieutenant-hobson/sergeant-long |

**候选说明**：
- **kalumah**（FC）——眷恋 Mrs Barnett 之因纽特少女、于浮冰绝境救助探险队的向导；93 distinct PN。补 FC 簇（既有 3 页）。首现 FC-019-043。
- **phina-hollaney**（GM）——Kolderup 之教女、Godfrey 之未婚妻、于旧金山守候环游归来的恋人；85 distinct PN。补 GM 簇（既有 3 页，收束婚姻主线）。首现 GM-003-011。
- **madge**（FC）——Mrs Paulina Barnett 之忠仆兼终身伴侣、探险全程相随的坚毅女性；106 distinct PN（全批最高）。补 FC 簇。首现 FC-001-028。

**dup-check 汇总**：3 候选 exact-slug filesystem test -f 全 ABSENT（bucket ka/ph/ma）；registry entity + label（Kalumah/Phina Hollaney/Phina/Madge/各 token）均 ABSENT，不在既有 3 parked 冲突（Hector Servadac/Robur the Conqueror/Claudius Bombarnac）内，无冲突。全 mentions ≥85 grounded。**HK(e) 规避**：phina 非 work 名，不触同名 label 风险（区别于暂缓的 Godfrey——若建 Godfrey 角色页则撞 work「Godfrey Morgan」）。**教训延续**：filesystem + registry alias 并查（R386 count-dartigas、R390 jasper-hobson 皆经 alias 检查捕获同一实体）。

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

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 118-120）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：本轮为 discover 轮，无建页无编辑；仅更新 grow_state + queue.md（追加候选）+ 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 filesystem dup-check ABSENT、registry entity+label 无冲突。✔
- **grounding**：全 3 mentions ≥85（madge 106、kalumah 93、phina-hollaney 85），均足支撑 ≥5 distinct solid PN。✔
- **alias 排除**：本批无同一实体重建风险；phina 非 work 名规避 HK(e)。✔
- **既有页排除**：3 候选 test -f 全 ABSENT。✔
- **since_discover 归零**：4→0。✔

## 六步状态机（SCN28，grow_state 存 R396 起始计数）

| 字段 | R395 起始 | R396 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 395 | 396 |
| type_round | 87 | 88 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 4 | 0（SCN28 归零）|
| discover_streak_low | 0 | 0（new_candidates=3≥3）|
| rounds_since_last_corpus_discover | 331 | 332 |
| last_updated_round | 395 | 396 |

## 遗留问题

1. **character 页数 82（本轮无建）**：queue(character) 0→**3**（建序 118-120）。registry 全库 **1606**，unknown 0。
2. **下轮 R396 = NEW1（§3(7)）**：since_evv5=2<10 → §3(1) 否；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 118（kalumah，book The Fur Country，pn_anchor FC-019，role supporting）。**下次 EVV5 于 R403 起始达 since_evv5=10（§3(1b)）——即 R396 NEW1（kalumah）→ R397 NEW1（phina-hollaney）→ R398 NEW1（madge）→ queue 归 0 → R399 SCN28-zombie 补第十五批 → …… → R403 EVV5。**
3. **第十四批 3 候选（建序 118-120）**：kalumah/phina-hollaney/madge。R396-R398 NEW1 消费 → queue 归 0 → R399 SCN28-zombie 补第十五批。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。FC 新建可回链 paulina-barnett/lieutenant-hobson/sergeant-long。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan——若后建 Godfrey 角色页则触发新同名冲突，暂缓）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R393 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=331→332（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
