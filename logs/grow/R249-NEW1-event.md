---
round: 249
date: 2026-07-18
type_round: 15
phase: "2.1"
current_type: event
gene: NEW1
pages: [abduction-of-thomas-roch]
result: success
---

# GROW 2.1-B · R249 · NEW1 · event — 建 The Abduction of Thomas Roch（Roch 与看护 Gaydon 自 Healthful House 被 Ker Karraje 手下掳走，FF）

## 执行摘要

Phase 2.1-B event 类型第 12 建（type_round 15），消费 R248 discover 队列**建序 12**。决策机 §3 首匹配 **NEW1**
（since_evv5=4<10；streak=0<3；since_discover=0<10、全局 queue≥10；queue(event)=4>0 → §3(4) 否；stub=0 → §3(7)）。

**The Abduction of Thomas Roch**（FF 主，首个 FF event）。事件锚定 pn_anchor=**FF-003**（夜袭 Healthful House 掳人之章）。
gather("carried off"/"pavilion"/"gagged"/"Ebba"/"Gaydon" FF-002→004)。逐句核**单指该事件**：疯狂发明家 Thomas Roch 与
看护 Gaydon（Simon Hart）夜间自 Healthful House 17 号亭被 Count d'Artigas、Captain Spade 及 Ebba 水手掳上纵帆船——
单一掳人事件。**排除**：FF 中 fulgurator（Roch 的爆炸剂）献予各国之泛述剔除。
exact-slug abduction-of-thomas-roch ABSENT（变体 thomas-roch-abduction 亦 ABSENT）。FF 2-char，无需 RFC-0003 Note。

**恰达门 8 distinct solid PN**（FF×8，四节分配）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | FF-003-004 | 潜至后墙、17 号亭在其后（目标设置）|
| Overview | FF-003-043 | 布置使无人疑 Roch 与看护被掳上 Ebba（计划）|
| What Happens | FF-003-060 | 确认无人、Spade 率众入亭 |
| What Happens | FF-003-081 | 四水手扑倒 Gaydon、堵嘴捆缚蒙眼（核心）|
| What Happens | FF-003-085 | Gaydon 与 Roch 同法被掳 |
| What Happens | FF-003-088 | 众赴小艇、boatswain 已备接应 |
| Significance | FF-004-043 | 数时后 Roch 与看护已被掳走 |
| Significance | FF-004-071 | 当局录案：Healthful House 遭破入、二人被绑架 |

**VVV 处置**：FF 2-char，PN 正常渲染，无需 RFC-0003 Note。pn_validator --mode strict ✓（重叠度门全过，无回炉）。

event 计数 26→27，registry total 1501→**1502**，unknown 恒 0。add_page 一次成型（rev G4o4AT，size 2405，
quality 自动 featured）。prose-gate awk 首过 0 超段。
location=Healthful House、pn_anchor=FF-003、book=Facing the Flag、aliases=[The Kidnapping of Thomas Roch]。
链 [[Healthful House]]/*[[facing-the-flag]]*（Thomas Roch、Gaydon、Count d'Artigas、Ker Karraje、Ebba 未建 character/place，散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =4 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=0<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =4>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| abduction-of-thomas-roch | G4o4AT | Facing the Flag | Healthful House | FF-003 | 8 | Roch+Gaydon 被掳单指；剔 fulgurator 泛述；FF 2-char 无需 Note |

- **abduction-of-thomas-roch**：8 distinct solid PN（FF 全用，四节分配）；aliases [The Kidnapping of Thomas Roch]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指掳人事件；fulgurator 泛述剔除；strict ✓。✔
- **G2 段落 ≤400 字**：首过 0 超段。✔
- **G3 ≥5 distinct PN**：8 solid（FF），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；FF 2-char 无需 Note。✔
- **registry 一致**：total 1502 event 27 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug abduction-of-thomas-roch ABSENT；非既有 26 event；无 alias 冲突。✔
- **单指核**：FF-002→004 掳人经过逐句确认指同一事件。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R250 起始计数）

| 字段 | R249 起始 | R250 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 249 | 250 |
| type_round | 15 | 16 |
| rounds_since_last_evv5 | 4 | 5 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 185 | 186 |
| last_updated_round | 249 | 250 |

## 遗留问题

1. **event 页数 27**：本轮 +1（首个 FF event）。队列余 3（建序 13-15）。registry 全库 **1502**，unknown 0。
2. **下轮 R250 = NEW1（event）**：建 queue 建序 13 **terror-destruction**（MW，MW-017）。
   since_evv5=5<10、streak=0、queue(event)=3>0 → §3(7) NEW1。MW 2-char 无需 Note。
   建时核 "Terror" 风暴中遭雷击、电池起爆、坠海碎裂单指（MW-017-068/069），剔 Great Eyrie 泛述。
3. **建序 15 amazon-cryptogram 提醒**：EHLA 4-char，建时须加 page-top RFC-0003 Note。
4. **event PN 回填债（R244 EVV5 记录）**：13/23 早期页 <5 PN，DEFERRED。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **corpus-discover 顺延**：since_corpus=185→186（dead 变量）。
7. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
8. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
