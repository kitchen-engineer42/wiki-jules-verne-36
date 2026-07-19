---
round: 251
date: 2026-07-18
type_round: 17
phase: "2.1"
current_type: event
gene: NEW1
pages: [halbrane-wreck]
result: success
---

# GROW 2.1-B · R251 · NEW1 · event — 建 The Wreck of the Halbrane（Halbrane 遭翻滚冰山撞毁坠海、南极搁浅覆没，AM）

## 执行摘要

Phase 2.1-B event 类型第 14 建（type_round 17），消费 R248 discover 队列**建序 14**。决策机 §3 首匹配 **NEW1**
（since_evv5=6<10；streak=0<3；since_discover=2<10、全局 queue≥10；queue(event)=2>0 → §3(4) 否；stub=0 → §3(7)）。

**The Wreck of the Halbrane**（AM 主，首个 AM event）。事件锚定 pn_anchor=**AM-019**（冰山撞毁之章）。
gather("iceberg"/"stranded"/"hundred feet"/"abyss"/"avalanche" AM-018→020)。逐句核**单指该事件**：双桅捕海豹船 Halbrane
雾中撞翻滚冰山、被掀上百尺搁浅冰壁、停搁数周、终坠五百尺深渊、片甲无存——单一覆没事件。
**排除**：AM 中 Grampus 沉船（Arthur Pym 背景）等泛述剔除。
exact-slug halbrane-wreck ABSENT（变体 the-halbrane/halbrane 亦 ABSENT）。AM 2-char，无需 RFC-0003 Note。

**恰达门 8 distinct solid PN**（AM×8，四节分配；均异段落号，无去重问题）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | AM-019-111 | 雾中撞冰山、无法避开（起因）|
| Overview | AM-018-143 | 剧震将叙者掀出铺位（撞击时刻）|
| What Happens | AM-019-113 | 冰山翻滚、撞 Halbrane 如羽毛板击毽、掀上百尺搁浅（核心）|
| What Happens | AM-019-115 | 唯一交通工具被掀离水面、举至百尺高 |
| What Happens | AM-020-007 | 冰山如搁浅浅滩般静止（数周搁浅）|
| What Happens | AM-020-127 | 前一刻百尺高空、此刻五百尺深海（终坠）|
| Significance | AM-020-126 | 如雪崩般坠深渊、片甲无存 |
| Significance | AM-020-129 | 船覆没时铁汉 West 落泪 |

**VVV 处置**：AM 2-char，PN 正常渲染，无需 RFC-0003 Note。pn_validator --mode strict ✓（重叠度门全过，无回炉）。

event 计数 28→29，registry total 1503→**1504**，unknown 恒 0。add_page 一次成型（rev AuGBjK，size 2487，
quality 自动 featured）。prose-gate awk 首过 0 超段。
location=Antarctic Sea、pn_anchor=AM-019、book=An Antarctic Mystery、aliases=[The Loss of the Halbrane]。
链 [[antarctic-sea]]/*[[an-antarctic-mystery]]*（Halbrane 船、Len Guy、West、Jeorling 未建，散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =6 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=2<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| halbrane-wreck | AuGBjK | An Antarctic Mystery | Antarctic Sea | AM-019 | 8 | 冰山撞毁单指；剔 Grampus 背景沉船泛述；AM 2-char 无需 Note |

- **halbrane-wreck**：8 distinct solid PN（AM，四节分配，异段落号）；aliases [The Loss of the Halbrane]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指冰山撞毁；Grampus 背景剔除；strict ✓。✔
- **G2 段落 ≤400 字**：首过 0 超段。✔
- **G3 ≥5 distinct PN**：8 solid（AM），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；AM 2-char 无需 Note。✔
- **registry 一致**：total 1504 event 29 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug halbrane-wreck ABSENT；非既有 28 event；无 alias 冲突。✔
- **单指核**：AM-018→020 撞毁与覆没逐句确认指同一事件。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R252 起始计数）

| 字段 | R251 起始 | R252 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 251 | 252 |
| type_round | 17 | 18 |
| rounds_since_last_evv5 | 6 | 7 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 187 | 188 |
| last_updated_round | 251 | 252 |

## 遗留问题

1. **event 页数 29**：本轮 +1（首个 AM event）。队列余 1（建序 15）。registry 全库 **1504**，unknown 0。
2. **下轮 R252 = NEW1（event）**：建 queue 建序 15（末位）**amazon-cryptogram**（EHLA，EHLA-027）。
   since_evv5=7<10、streak=0、queue(event)=1>0 → §3(7) NEW1。**EHLA 4-char → 须 page-top RFC-0003 Note**。
   建时核证 Joam Dacosta 清白之密文被破译单指（EHLA-026-086/027-002），剔 Amazon 木筏航行泛述。
3. **R252 后 queue(event) 将罄**：建序 15 消费后 queue(event)==0，R253 触发 §3(4) SCN28-zombie（event discover 第 4 轮）。
4. **event PN 回填债（R244 EVV5 记录）**：13/23 早期页 <5 PN，DEFERRED。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **corpus-discover 顺延**：since_corpus=187→188（dead 变量）。
7. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
8. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
