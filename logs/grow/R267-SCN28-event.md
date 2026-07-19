---
round: 267
date: 2026-07-18
type_round: 34
phase: "2.1"
current_type: event
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R267 · SCN28-zombie · event — 队列勘探（queue(event)==0 触发），播 3 net-new 候选

## 执行摘要

Phase 2.1-B event 第 7 次勘探（type_round 34）。R266 EVV5 反思后 since_evv5 reset=0，queue(event)==0（建序 22-24 R263-265 全数消费）→
决策机 §3 首匹配 **§3(4) SCN28-zombie**（since_evv5=0<10 → §3(1) 否；streak=0<3 → §3(2) 否；
since_discover=4<10、全局 queue≥10 → §3(3) 否；**queue(event)==0 → §3(4) 触发**）。

**勘探法**：全库 36 部作品，event 现覆盖 **27/36** 部。按 VVV 逐部核未覆盖作品，锁定素材充实者掘单指事件锚点，逐句核实 ≥5 distinct 可达。
仍余零/低 event 作品：ASC/PL/TN/DA/SC/SC2/VB/DSCF/AMB。

**播 3 net-new 候选**（≥ type_close_new_candidate_min=3 → productive；discover_streak_low 保持 0），取自 **3 部零 event 覆盖作品**：

| 建序 | slug | 作品(VVV) | pn_anchor | 单指事件 | ≥4-char? |
|------|------|-----------|-----------|---------|---------|
| 25 | death-of-martin-paz | The Pearl of Lima (PL) | PL-009 | Martin Paz 于马德拉大瀑布以套索救 Sarah、被箭穿心、二人同坠瀑涡殉情（PL-009-047/048/056/060/064/065/066/071）| 否（2-char）|
| 26 | christiania-lottery-drawing | Ticket No. 9672 (TN) | TN-019 | 克里斯蒂安尼亚大学礼堂抽奖、9672 号中十万马克、被认已随 Viking 沉没之 Ole Kamp 生还现身认领（TN-019-001/049/059/064/065/067/070/073）| 否（2-char）|
| 27 | ki-tsang-train-attack | Claudius Bombarnac (ASC) | ASC-020 | 蒙古大盗 Ki-Tsang 掀轨截停大中亚铁路、六十众伏兵袭帝室财车、Faruskiar 力战护宝终诛 Ki-Tsang（ASC-020-020/022/029/030/034/037 + ASC-021-001/004）| 否（3-char）|

三候选 exact-slug 全 ABSENT（含变体 martin-paz-death/cataract-of-the-madeira、the-lottery-drawing/ticket-9672-drawing/ole-kamp-return、gobi-train-attack/attack-on-the-transasiatic/ki-tsang-attack）。
锚点均逐章 sentence_index 实句核实、各 ≥8 distinct PN 可达、单指连续事件。三事件分属三部独立作品，无交叉歧义。
**VVV 宽度**：PL/TN 2-char、ASC 3-char，**三者皆 ≤3 char → 无需 page-top RFC-0003 Note**。
event 空间仍广：仍余 DA/SC（The Survivors of the Chancellor?）/SC2/VB/DSCF/AMB 等零/低 event 作品可续掘。

本轮**无建页**（纯勘探）。registry 恒 1514，event 39，unknown 0。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=4<10；全局 queue≥10 | 否 |
| **4** | **SCN28-zombie（queue(current_type)==0）** | **queue(event)==0** | **触发** |
| 5/6 | RCH2 系 | — | — |
| 7 | NEW1 | — | — |

## 页面处理记录

（本轮无建页；勘探播种 3 候选入 queue.md 建序 25-27，详见执行摘要表。）

## EXIT-GATE 检查

- **勘探产出 ≥3**：3 net-new ≥ 3 → productive。✔
- **候选查重**：3 slug（含变体共 11 例）exact-slug 全 ABSENT。✔
- **锚点核实**：PL-009/TN-019/ASC-020 均以 sentence_index 实句确认单指事件、各 ≥8 distinct PN 可达。✔
- **未覆盖作品优先**：3 候选取自 PL/TN/ASC 三部零 event 覆盖作品。✔
- **registry 一致**：total 1514 event 39 unknown 0；仅 Robur PARK。✔
- **无建页**：本轮纯 discover，未调 add_page/edit_page。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（SCN28，grow_state 存 R268 起始计数）

| 字段 | R267 起始 | R268 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 267 | 268 |
| type_round | 33 | 34 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 4 | **0（SCN28 reset）** |
| discover_streak_low | 0 | 0（productive，保持）|
| rounds_since_last_corpus_discover | 203 | 204 |
| last_updated_round | 267 | 268 |

## 遗留问题

1. **event 队列补充**：queue(event) 0→3（建序 25-27）。registry 全库 1514，unknown 0。
2. **下轮 R268 = NEW1（event）**：建 queue 建序 25 **death-of-martin-paz**（PL，PL-009）。
   since_evv5=1<10、streak=0、queue(event)=3>0 → §3(7) NEW1。**PL 2-char 无需 Note**。
   建时核瀑布救人殉情单指（套索缚舟→箭穿心→同坠瀑涡）、剔前章 Lima 族斗/起义泛述；工作页（若存 the-pearl-of-lima）链回。
3. **event 覆盖**：27/36 部作品含 event；R268-270 建成后将增至 30/36（+PL/TN/ASC）。
4. **消歧方法论四例沉淀（R256/R260/R261/R264）**：event discover 队列锚点须视为线索非定论，建时逐句复核锚点章实指。已积四例修正 + 一例核实无误（R265）。
5. **event PN 回填债（R244/R255/R266 EVV5 记录）**：13/39 早期页 <5 PN，DEFERRED，下次 EVV5（约 R277）或 EVV6 再审。
6. **散文门债**：37 页 >400（既有 DEFERRED）。
7. **corpus-discover 顺延**：since_corpus=203→204（dead 变量）。
8. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
9. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
