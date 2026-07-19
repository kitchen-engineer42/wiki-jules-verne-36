---
round: 258
date: 2026-07-18
type_round: 24
phase: "2.1"
current_type: event
gene: SCN28
pages: []
result: success
---

# GROW 2.1-B · R258 · SCN28-zombie · event — 队列勘探（queue(event)==0 触发），播 3 net-new 候选

## 执行摘要

Phase 2.1-B event 第 5 次勘探（type_round 24）。R257 消费末位队列（建序 18 new-aberfoyle-flood）后 **queue(event)==0**，
决策机 §3 首匹配 **§3(4) SCN28-zombie**（since_evv5=2<10 → §3(1) 否；streak=0<3 → §3(2) 否；
since_discover=4<10、全局 queue≥10 → §3(3) 否；**queue(event)==0 → §3(4) 触发**）。

**勘探法**：全库 36 部作品，event 现覆盖 21/36 部（本会话新增 RC/FF/MW/AM/EHLA/GM/UC 七部）。
按 sentence_index VVV 文件名核未覆盖作品，锁定素材充实者掘单指事件锚点，逐句核实。

**播 3 net-new 候选**（≥ type_close_new_candidate_min=3 → productive；discover_streak_low 保持 0），取自 **3 部零 event 覆盖作品**：

| 建序 | slug | 作品(VVV) | pn_anchor | 单指事件 | 4-char? |
|------|------|-----------|-----------|---------|---------|
| 19 | waif-cynthia-rescue | The Waif of the Cynthia (WC) | WC-002 | 婴儿卧柳条摇篮系于浮标、随波获渔夫救起，浮标刻船名 'Cynthia'（WC-002-068/087/091、WC-006-013）| 否 |
| 20 | kilimanjaro-cannon-shot | Topsy-Turvy (TT) | TT-004 | 900 尺巨炮以 40 万磅火棉发射小炮弹、欲改地轴（TT-004-003/004/005）| 否 |
| 21 | charleston-blockade-run | The Blockade Runners (BR) | BR-003 | 汽船 Dolphin 恃速强闯 Charleston 联邦封锁线（BR-001-042/052 立意 + BR-003 强闯）| 否 |

三候选 exact-slug 全 ABSENT（含变体 cynthia-waif-rescue/great-gun-firing/running-the-blockade 等）。
锚点均以 sentence_index 实句核实。三事件分属三部独立作品，无交叉歧义。
event 空间仍广：仍余 ASC（Special Correspondent）、WAI（Winter Amid the Ice）、DOSE（Doctor Ox）、PL（Pearl of Lima）、
TN（Ticket No. 9672）、MZ（Master Zacharius）等零 event 作品可续掘；UC-005 神秘炸柱悬疑亦可考（单指素材偏薄，播种前须核 ≥5 可达）。

本轮**无建页**（纯勘探）。registry 恒 1508，event 33，unknown 0。

## 决策矩阵（SCN28-zombie）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=4<10；全局 queue≥10 | 否 |
| **4** | **SCN28-zombie（queue(current_type)==0）** | **queue(event)==0** | **触发** |
| 5/6 | RCH2 系 | — | — |
| 7 | NEW1 | — | — |

## 页面处理记录

（本轮无建页；勘探播种 3 候选入 queue.md 建序 19-21，详见执行摘要表。）

## EXIT-GATE 检查

- **勘探产出 ≥3**：3 net-new ≥ 3 → productive。✔
- **候选查重**：3 slug（含变体）exact-slug 全 ABSENT。✔
- **锚点核实**：WC-002/TT-004/BR-003 均以 sentence_index 实句确认单指事件。✔
- **未覆盖作品优先**：3 候选取自 WC/TT/BR 三部零 event 覆盖作品。✔
- **registry 一致**：total 1508 event 33 unknown 0；仅 Robur PARK。✔
- **无建页**：本轮纯 discover，未调 add_page/edit_page。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（SCN28，grow_state 存 R259 起始计数）

| 字段 | R258 起始 | R259 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 258 | 259 |
| type_round | 24 | 25 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 4 | **0（SCN28 reset）** |
| discover_streak_low | 0 | 0（productive，保持）|
| rounds_since_last_corpus_discover | 194 | 195 |
| last_updated_round | 258 | 259 |

## 遗留问题

1. **event 队列补充**：queue(event) 0→3（建序 19-21）。registry 全库 1508，unknown 0。
2. **下轮 R259 = NEW1（event）**：建 queue 建序 19 **waif-cynthia-rescue**（WC，WC-002）。
   since_evv5=3<10、streak=0、queue(event)=3>0 → §3(7) NEW1。WC 2-char 无需 Note。
   建时核婴儿卧摇篮系浮标获救单指、浮标刻 'Cynthia'，剔后续身世追查泛述。
3. **event 覆盖**：21/36 部作品含 event；本会话由 15/36 增至 21/36（+RC/FF/MW/AM/EHLA/GM/UC）。
4. **event PN 回填债（R244/R255 EVV5 记录）**：13/33 早期页 <5 PN，DEFERRED，下次 EVV5（约 R267）再审。
5. **散文门债**：37 页 >400（既有 DEFERRED）。
6. **corpus-discover 顺延**：since_corpus=194→195（dead 变量）。
7. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
8. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
