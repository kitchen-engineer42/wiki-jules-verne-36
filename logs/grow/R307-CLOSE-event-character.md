---
round: 307
date: 2026-07-19
type_round: 73
phase: "2.1"
current_type: event
gene: CLOSE+SCN28
pages: []
result: success
---

# GROW 2.1-B · R307 · CLOSE+SCN28 · event→character — event 收官（final_count 64），切末类型 character，切后立即 SCN28 首批 discover 掘 6 候选建序 51-56

## 执行摘要

Phase 2.1-B event 类型 discover 轮（type_round 73）。决策机 §3 首匹配 **§3(2) CLOSE+SCN28**
（since_evv5=7<10 → §3(1) 否；**discover_streak_low=3≥type_close_streak(3) → §3(2) CLOSE+SCN28 触发**）。

R305/R306 连两轮 exhaustive re-scan 零候选（单事件作品第二事件矿竭），discover_streak_low 达 3，本轮收官 event。

**§5.1 类型切换（ACTIVE→CLOSED）**：
- closed_types 追加 `{type:'event', closed_at_round:307, final_count:64, evv6_score:null}`（final_count 逐 pages.json 计 event=64 核实）。
- current_type **event→character**（type_queue[0] 弹出为新 current；type_queue [character]→[]，character 为末类型）。
- 类型级计数复位：type_round→0、discover_streak_low→0、rounds_since_last_evv5→0。

**切换后立即执行 discover**（本轮 gene = CLOSE+SCN28，为新类型 character 补候选队列）：
character 为 SCN23 权重最高实体类型（type-survey 估 ~180-240，现仅 15 页覆盖头部主角），候选池充沛。首批掘 **6 候选**（建序 51-56）：

| 建序 | slug | book | pn_anchor | 简述 | 复现 |
|------|------|------|-----------|------|------|
| 51 | aronnax | Twenty Thousand Leagues Under the Seas | TTLU-002 | 博物学者叙述者，登 Abraham Lincoln 追海怪随 Nautilus | 34 章 |
| 52 | ayrton | The Mysterious Island | MI-039 | Tabor 岛遗弃叛徒水手，后 Lincoln 岛救赎 | MI24/SI20/SC17 |
| 53 | dick-sand | Dick Sand, A Captain at Fifteen | DSCF-002 | 十五岁见习水手，Pilgrim 号临危掌舵 | 36 章 |
| 54 | pencroft | The Mysterious Island | MI-002 | 直率水手，Lincoln 岛殖民造船主力 | MI61/SI20 |
| 55 | herbert | The Mysterious Island | MI-002 | 少年博物学徒，中弹濒死获救 | MI61/SI20 |
| 56 | paganel | In Search of the Castaways | SC-006 | 心不在焉之地理学会秘书，误登 Duncan | 61 章 |

**dup-check（filesystem + registry，遵 memory 规则）**：全 6 slug + 变体 + alias 双查 **ABSENT**——`ls */slug.md` 无匹配；registry alias 命中仅 work（dick-sand-a-captain-at-fifteen）/chapter（DSCF/SC-chNN）/event（tabor-island-castaway、wreck-of-the-pilgrim）页，**无 character 实体页**。6 候选均干净。

**低产判定**：new_candidates=6≥type_close_new_candidate_min(3) → **productive discover，discover_streak_low 保持 0**（且 §5.1 已复位 0）。

本轮 discover 轮，不建页（pages: []）。registry 不变（event 64、total 1539、character 15、unknown 0）。

## 决策矩阵（CLOSE+SCN28）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| **2** | **CLOSE+SCN28（streak≥3）** | **discover_streak_low=3≥3** | **触发** |
| 3 | SCN28（queue<10 或 since_discover≥10）| — | — |
| 4 | SCN28-zombie（queue(event)==0）| — | — |
| 5/6 | RCH2 系（stub%≥15）| — | — |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

本轮为 CLOSE+discover 轮，无建页/编辑。动作：§5.1 类型切换（event→character）+ SCN28 首批 character discover（6 候选建序 51-56）+ 更新 grow_state + 写日志。

## EXIT-GATE 检查

- **G1–G3、schema**：discover 轮不建页，N/A。✔
- **G4 脚本建页**：本轮不建页，无 Write/Edit 于 pages/**。✔
- **registry 一致**：不变（total 1539、event 64、character 15、unknown 0）；build_registry 未跑（无页变动）。✔
- **§5.1 切换正确性**：closed_types 追加 event(64,307)；type_queue [character]→[]；current_type event→character；type_round/streak/since_evv5 复位 0——对齐 R233 place→event 先例。✔
- **discover 充分性**：6 候选均 filesystem + registry dup-check ABSENT，pn_anchor 逐一 corpus 核实存在（TTLU-002/MI-039/DSCF-002/MI-002/SC-006）。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（CLOSE+SCN28，grow_state 存 R308 起始计数）

| 字段 | R307 起始 | R308 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | **character**（§5.1 切换）|
| type_queue | [character] | **[]**（character 弹出为 current）|
| current_round | 307 | 308 |
| type_round | 73 | **0**（§5.1 复位）|
| rounds_since_last_evv5 | 7 | **0**（§5.1 复位）|
| rounds_since_last_discover | 0 | 0（SCN28 reset）|
| discover_streak_low | 3 | **0**（§5.1 复位 + productive discover）|
| rounds_since_last_corpus_discover | 243 | 244 |
| last_updated_round | 307 | 308 |
| closed_types | [work,org,tech,place] | **+event(64,307)** |

## 遗留问题

1. **event 类型收官**：final_count 64（work 33 / org 15 / tech 20 / place 422 / event 64）；closed_types 五类型皆 evv6_score:null（EVV6 封存点待 Phase 2.1 关闭前回填）。event 为 Phase 2.1-B 广度扩张之末一实体高潮类型（掘零事件作品 + 单事件作品第二事件二策略，二矿均竭）。
2. **character 类型启幕（末类型）**：type_queue 切后空 → character 建成即 Phase 2.1 迭代末。首批 6 候选建序 51-56 已入队。**下轮 R308 = NEW1（§3(7)）**：since_evv5=0<10；discover_streak_low=0<3；since_discover=0<10 且全局 queue≥10 → §3(3) 否；queue(character)=6>0 → §3(4) 否；stub%=0 → §3(7) NEW1，消费建序 51（aronnax）。建时须逐句 corpus 核 pn_anchor（遵 anchor-as-clue 教训）、≥5 distinct solid PN、pn_validator --mode strict、段 ≤400。
3. **character 候选池充沛**：type-survey 估 ~180-240，现仅 15 页（头部主角 captain-nemo/phileas-fogg/passepartout/axel/barbicane 等）。首批 6 后仍有大量二线角色（Nab、Herbert 之外的 MI 殖民者、SC 群像、Michel Strogoff 群像等）可续掘；后续 discover 轮（SCN28/zombie）补充。
4. **HK 待批**（parked，勿自主编辑）：（a）nemo-death 并 alias「Death of Prince Dakkar」（+补 PN ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一；（c）「Master of the World」book label 归一（terror-destruction/great-eyrie-investigation 归并）。
5. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
6. **散文门债**：37 页 >400（既有 DEFERRED）。
7. **corpus-discover 顺延**：since_corpus=243→244（dead 变量）。
8. **EVV6 封存点·迫近**：character 类型建成后 type_queue 空 → Phase 2.1 迭代末，触发 §5.2 EVV6 全库评审 + 回填 closed_types[].evv6_score（现五类型皆 null），并处理 event 13 页 PN 回填债 + 散文门债。
9. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
