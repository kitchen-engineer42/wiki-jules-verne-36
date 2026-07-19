---
round: 253
date: 2026-07-18
type_round: 19
phase: "2.1"
current_type: event
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R253 · SCN28-zombie · event — 队列勘探（queue(event)==0 触发），播 3 net-new 候选

## 执行摘要

Phase 2.1-B event 第 4 次勘探（type_round 19）。R252 消费末位队列（建序 15 amazon-cryptogram）后 **queue(event)==0**，
决策机 §3 首匹配 **§3(4) SCN28-zombie**（since_evv5=8<10 → §3(1) 否；streak=0<3 → §3(2) 否；
since_discover=4<10、全局 queue≥10 → §3(3) 否；**queue(event)==0 → §3(4) 触发**）。

**勘探法**：event 现覆盖 16/36 部作品（含 R248 播的 FF/MW/AM/EHLA）。锁定未覆盖作品掘单指 event 锚点，
gather 事件描述词（wreck/explosion/flood/attack/rescue）scoped 未覆盖 VVV（GM/UC/WC 等）。

**播 3 net-new 候选**（≥ type_close_new_candidate_min=3 → productive；discover_streak_low 保持 0），取自 **2 部未覆盖作品**：

| 建序 | slug | 作品(VVV) | pn_anchor | 单指事件 | 4-char? |
|------|------|-----------|-----------|---------|---------|
| 16 | wreck-of-the-dream | Godfrey Morgan (GM) | GM-008 | 汽船 Dream 触礁沉没、Godfrey 与 Tartlet 沦落荒岛（GM-008-012/013）| 否 |
| 17 | new-aberfoyle-explosion | The Underground City (UC) | UC-005 | New Aberfoyle 煤矿 firedamp 瓦斯爆炸（UC-005-011）| 否 |
| 18 | new-aberfoyle-flood | The Underground City (UC) | UC-016 | Coal Town 突遭地下水淹没（UC-016-006/011/012）| 否 |

三候选 exact-slug 全 ABSENT（含变体 dream-shipwreck/firedamp-explosion/new-aberfoyle-flood）。
锚点均以 sentence_index 实句核实。UC 二事件（爆炸 UC-005 vs 淹没 UC-016）分属不同章、不同灾种，建时须严格区分。
event 空间仍广（WC Waif of the Cynthia、Steam House、Green Ray、Kéraban、Tribulations of a Chinaman 等 18+ 部零 event 覆盖）。

本轮**无建页**（纯勘探）。registry 恒 1505，event 30，unknown 0。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =8 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=4<10；全局 queue≥10 | 否 |
| **4** | **SCN28-zombie（queue(current_type)==0）** | **queue(event)==0** | **触发** |
| 5/6 | RCH2 系 | — | — |
| 7 | NEW1 | — | — |

## 页面处理记录

（本轮无建页；勘探播种 3 候选入 queue.md 建序 16-18，详见执行摘要表。）

## EXIT-GATE 检查

- **勘探产出 ≥3**：3 net-new ≥ 3 → productive。✔
- **候选查重**：3 slug（含变体）exact-slug 全 ABSENT。✔
- **锚点核实**：GM-008/UC-005/UC-016 均以 sentence_index 实句确认单指事件。✔
- **未覆盖作品优先**：3 候选取自 GM/UC 二部零 event 覆盖作品。✔
- **registry 一致**：total 1505 event 30 unknown 0；仅 Robur PARK。✔
- **无建页**：本轮纯 discover，未调 add_page/edit_page。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（SCN28，grow_state 存 R254 起始计数）

| 字段 | R253 起始 | R254 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 253 | 254 |
| type_round | 19 | 20 |
| rounds_since_last_evv5 | 8 | 9 |
| rounds_since_last_discover | 4 | **0（SCN28 reset）** |
| discover_streak_low | 0 | 0（productive，保持）|
| rounds_since_last_corpus_discover | 189 | 190 |
| last_updated_round | 253 | 254 |

## 遗留问题

1. **event 队列补充**：queue(event) 0→3（建序 16-18）。registry 全库 1505，unknown 0。
2. **下轮 R254 = NEW1（event）**：建 queue 建序 16 **wreck-of-the-dream**（GM，GM-008）。
   since_evv5=9<10、streak=0、queue(event)=3>0 → §3(7) NEW1。GM 2-char 无需 Note。
   建时核汽船 Dream 触礁沉没、Godfrey 沦落荒岛单指，剔岛上后续（火/野人/洪水等属别事件）。
3. **EVV5 临近**：since_evv5=9，**R255 将达 10 → §3(1b) EVV5 反思轮**（event 模板评审 + 回填债审视）。
4. **event PN 回填债（R244 EVV5 记录）**：13/23 早期页 <5 PN，DEFERRED，R255 EVV5 可再审。
5. **散文门债**：37 页 >400（既有 DEFERRED）。
6. **corpus-discover 顺延**：since_corpus=189→190（dead 变量）。
7. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
8. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
