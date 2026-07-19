---
round: 306
date: 2026-07-19
type_round: 72
phase: "2.1"
current_type: event
gene: SCN28-zombie
pages: []
result: success
---

# GROW 2.1-B · R306 · SCN28-zombie · event — re-scan 续零候选，discover_streak_low 2→3 达 type_close_streak，R307 将 CLOSE event 切 character

## 执行摘要

Phase 2.1-B event 类型 discover 轮（type_round 72）。决策机 §3 首匹配 **§3(4) SCN28-zombie**
（since_evv5=6<10 → §3(1) 否；discover_streak_low=2<3 → §3(2) 否；since_discover=0<10、全局 queue≥10 → §3(3) 否；**queue(event)==0 → §3(4) SCN28-zombie 触发**）。

**re-scan 结论：new_candidates=0**（续 R305）。

event→work map 自 R305 exhaustive re-scan 后**无变**：R305/R306 间零 event 页新增，registry 恒 64 event / 33 book。R305 已逐 book 判定 6 单事件作品无干净离散第二事件（DA 单章 / DOSE 饱和 / BR 饱和 / MW 实为双事件 label 债 / SI 属 MI），单事件作品第二事件矿竭之结论不变。

**低产判定**：new_candidates=0 < type_close_new_candidate_min(3) → **discover_streak_low 2→3 = type_close_streak(3)**。

**R307 = CLOSE+SCN28**：下轮 discover_streak_low=3≥3 → §3(2) 触发 CLOSE+SCN28，收 event（final_count 64、closed_at_round 307）、type_queue 出队 → current_type 切 **character**（type_queue 末类型）。

本轮 discover 轮，不建页（pages: []）。registry 不变（event 64、total 1539、unknown 0）。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =2（本轮末 →3）| 否（本轮起始 2）|
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=0<10；全局 queue≥10 | 否 |
| **4** | **SCN28-zombie（queue(event)==0）** | **=0** | **触发** |
| 5/6 | RCH2 系（stub%≥15）| — | — |
| 7 | NEW1（默认）| — | — |

## 页面处理记录

本轮为 discover 轮，无建页/编辑。仅记 re-scan 负结果 + 更新 grow_state + 写日志。

## EXIT-GATE 检查

- **G1–G3、schema**：discover 轮不建页，N/A。✔
- **G4 脚本建页**：本轮不建页，无 Write/Edit 于 pages/**。✔
- **registry 一致**：不变（total 1539 event 64 unknown 0）。✔
- **re-scan 充分性**：map 自 R305 无变（零 event 页新增），矿竭结论延续；R305 已全覆盖逐 book 判定。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（SCN28-zombie，grow_state 存 R307 起始计数）

| 字段 | R306 起始 | R307 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 306 | 307 |
| type_round | 72 | 73 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 0 | 0 |
| discover_streak_low | 2 | **3**（= type_close_streak）|
| rounds_since_last_corpus_discover | 242 | 243 |
| last_updated_round | 306 | 307 |

## 遗留问题

1. **queue(event) 恒 0**：续零候选。registry 不变（event 64、total 1539、unknown 0）。
2. **下轮 R307 = CLOSE+SCN28（§3(2)）**：discover_streak_low=3≥type_close_streak(3) → §3(2) 触发。动作：closed_types 追加 {type:'event', closed_at_round:307, final_count:64, evv6_score:null}；type_queue 出队 [character]→[]；current_type event→**character**；SCN28 探勘 character 首批候选（characters 为 SCN23 权重最高实体类型，候选池充沛，预期 new_candidates≥3）。**注意**：CLOSE 轮同时重置 discover_streak_low→0（新类型起算）、since_discover→0。
3. **event 类型收官**：final_count 64（work 33 / org 15 / tech 20 / place 422 / event 64）。event 为 Phase 2.1-B 广度扩张之末一实体高潮类型（掘零事件作品 + 单事件作品第二事件二策略）；character 为末类型，其后 type_queue 空 → Phase 2.1 迭代收尾。
4. **EVV6 封存点·迫近**：Phase 2.1 关闭前须每类型 EVV6 全库评审并回填 closed_types[].evv6_score（现五类型将皆 null）；event EVV6 时并处理 13 页 PN 回填债 + 散文门债。character 类型建设完成后即 Phase 2.1 迭代末，触发 EVV6 全库评审。
5. **HK 待批**：（a）nemo-death 并 alias「Death of Prince Dakkar」（+补 PN ≥5）；（b）destruction-of-lincoln-island book SI→MI 归一；（c）「Master of the World」book label 归一（terror-destruction/great-eyrie-investigation 归并）。
6. **event PN 回填债**：13/64 早期页 <5 PN，DEFERRED。
7. **散文门债**：37 页 >400（既有 DEFERRED）。
8. **corpus-discover 顺延**：since_corpus=242→243（dead 变量）。
9. **EVV6 封存点**：见 §4。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
