---
round: 399
date: 2026-07-19
type_round: 91
phase: "2.1"
current_type: character
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R399 · SCN28-zombie · character — 第十五批 discover：补 3 候选（thomas-black/taskinar/dick-kennedy），queue 0→3，since_discover 归零；跨 FC/GM/FWB 三作品，FWB 新起首个人物页，避单作品集中

## 执行摘要

Phase 2.1-B character discover 轮（type_round 91）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=5<10 → §3(1) 否；discover_streak_low=0<3 → §3(2) 否；**queue(character)=0 → §3(4) SCN28-zombie 触发**）。补候选队列，**pages:[]，仅 G4**，since_discover 归 0。

第十四批（建序 118-120）R396-R398 全数消费（3 建：kalumah/phina-hollaney/madge），queue 归 0，本轮触发 zombie discover。

**第十五批 3 候选**（=3 → discover_streak_low 保持 0）——跨 FC/GM/FWB 三作品，避单作品集中，FWB 新起：

| 建序 | slug | book | VVV | pn_anchor | role | mentions | dup-check | 簇 |
|------|------|------|-----|-----------|------|----------|-----------|-----|
| 121 | thomas-black | The Fur Country | FC | FC-003 | supporting | 67 | ABSENT | FC 补 paulina-barnett/lieutenant-hobson/sergeant-long/kalumah/madge |
| 122 | taskinar | Godfrey Morgan | GM | GM-002 | supporting | 22 | ABSENT | GM 补 william-kolderup |
| 123 | dick-kennedy | Five Weeks in a Balloon | FWB | FWB-003 | supporting | 382 | ABSENT | FWB 新起（首个人物页）|

**候选说明**：
- **thomas-black**（FC）——为观日全食而随队北极的偏执天文学家、心无旁骛之观测者；67 distinct PN。补 FC 簇（既有 5 页）。首现 FC-003-022。
- **taskinar**（GM）——Kolderup 之宿敌、于岛屿拍卖场上竞价落败的富豪对手；22 distinct PN。补 GM 簇（既有 4 页）。首现 GM-002-035。
- **dick-kennedy**（FWB）——Fergusson 之苏格兰猎手挚友、气球远征之忠实同伴；「Kennedy」FWB 382 mentions（「Dick Kennedy」全称 4，余以 Kennedy 指称）。**FWB 新簇开拓**——Five Weeks in a Balloon 首个人物页。首现 FWB-003-001。

**dup-check 汇总**：3 候选 exact-slug filesystem test -f 全 ABSENT（bucket th/ta/di）；registry entity + label（Thomas Black/Taskinar/Dick Kennedy/Kennedy）均 ABSENT，不在既有 3 parked 冲突（Hector Servadac/Robur the Conqueror/Claudius Bombarnac）内，无冲突。全 mentions ≥22 grounded。**排除**：（a）**pan-chao**——建序 109 已建 R382，但 registry label 存为「Pan Chao」（无连字符），故 alias_index 查「Pan-Chao」漏报 ABSENT；**filesystem test -f 捕获 EXISTS**，教训延续（R386 count-dartigas、R390 jasper-hobson 同理，filesystem 为可靠信号）。（b）**nicholl**——FEM/RM/TT 多作品 231/55/53 mentions，触 HK(d) 多值 book，暂缓。（c）van-mitten/pencroff——corpus 0 mentions（拼写异或不在集）；pencroft/nadia/harry-blount/alcide-jolivet/conseil/ned-land/barbicane/cyrus-harding 等既建。

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

SCN28-zombie 为 discover 轮，无建页、无编辑（仅 G4）。产出 3 候选追加 queue.md（建序 121-123）+ discover-note。

## EXIT-GATE 检查

- **G4 脚本操作**：本轮为 discover 轮，无建页无编辑；仅更新 grow_state + queue.md（追加候选）+ 写日志，未用 Write/Edit 于 pages/**。✔
- **候选充分性**：3 候选（=3）→ discover_streak_low 保持 0。全 filesystem dup-check ABSENT、registry entity+label 无冲突。✔
- **grounding**：全 3 mentions ≥22（dick-kennedy 382、thomas-black 67、taskinar 22），均足支撑 ≥5 distinct solid PN。✔
- **alias 排除**：pan-chao filesystem 捕获既建（label「Pan Chao」alias 查漏）；nicholl 多值 book 暂缓；本批无同一实体重建风险。✔
- **既有页排除**：3 候选 test -f 全 ABSENT。✔
- **since_discover 归零**：3→0。✔

## 六步状态机（SCN28，grow_state 存 R400 起始计数）

| 字段 | R399 起始 | R400 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | character | character |
| type_queue | [] | [] |
| current_round | 399 | 400 |
| type_round | 91 | 92 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 3 | 0（SCN28 归零）|
| discover_streak_low | 0 | 0（new_candidates=3≥3）|
| rounds_since_last_corpus_discover | 335 | 336 |
| last_updated_round | 399 | 400 |

## 遗留问题

1. **character 页数 85（本轮无建）**：queue(character) 0→**3**（建序 121-123）。registry 全库 **1609**，unknown 0。
2. **下轮 R400 = NEW1（§3(7)）**：since_evv5=6<10 → §3(1) 否；discover_streak_low=0<3；queue(character)=3>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 121（thomas-black，book The Fur Country，pn_anchor FC-003，role supporting）。**消费节奏：R400 NEW1（thomas-black）→ R401 NEW1（taskinar）→ R402 NEW1（dick-kennedy）→ queue 归 0 → R403 起始 since_evv5=10 → §3(1b) EVV5（不消费队列）→ R404 SCN28-zombie 补第十六批。**
3. **第十五批 3 候选（建序 121-123）**：thomas-black/taskinar/dick-kennedy。R400-R402 NEW1 消费 → queue 归 0 → R403 EVV5 → R404 SCN28-zombie 补第十六批。
4. **回链回填债**（DEFERRED，非阻塞）：既有 + paulina-barnett/lieutenant-hobson/sergeant-long/kalumah→Madge、william-kolderup→Phina Hollaney、paulina-barnett/lieutenant-hobson→Kalumah、carefinotu/tartlet→William W. Kolderup、lieutenant-hobson/paulina-barnett→Sergeant Long、tartlet→Carefinotu、kinko/claudius-bombarnac→Zinca Klork、ephrinell/claudius-bombarnac→Miss Horatia Bluett、robur/uncle-prudent→Tom Turner、claudius-bombarnac→Sir Francis Trevellyan。
5. **HK 待批**（parked）：（a）nemo-death 并 alias；（b）destruction-of-lincoln-island book SI→MI；（c）「Master of the World」book label；（d）跨作品多值 book RFC（nicholl FEM/RM/TT 即此类）；（e）character-vs-work 同名 label（Hector Servadac / Claudius Bombarnac / Godfrey Morgan——若后建 Godfrey 角色页则触发新同名冲突，暂缓）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债 + character 内容债**（R393 EVV5 复评恒定）：7 页 PN<5 + 12 页 over-400，均 Pilot 种子，DEFERRED backfill。
8. **entity quality none / featured re-grade**：Phase 2.1 EVV6 全库评审统一处理（DEFERRED）。
9. **corpus-discover 顺延**：since_corpus=335→336（dead 变量）。EVV6 封存点：Phase 2.1 关闭前回填 closed_types[].evv6_score。
