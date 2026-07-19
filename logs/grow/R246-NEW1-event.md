---
round: 246
date: 2026-07-18
type_round: 12
phase: "2.1"
current_type: event
gene: NEW1
pages: [whale-hunt-disaster]
result: success
---

# GROW 2.1-B · R246 · NEW1 · event — 建 The Whale Hunt Disaster（Hull 捕鲸覆没、少年 Dick Sand 掌舵，DSCF）

## 执行摘要

Phase 2.1-B event 类型第 10 建（type_round 12），消费 R243 discover 队列**建序 10**。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10；streak=0<3；since_discover=2<10、全局 queue≥10；queue(event)=2>0 → §3(4) 否；stub=0 → §3(7)）。

**The Whale Hunt Disaster**（DSCF 主，首个 DSCF event）。事件锚定 pn_anchor=**DSCF-008**（捕鲸艇覆没之章）。
gather("whale"/"jubarte"/"tail"/"perished" DSCF-007→009)。逐句核**单指该事件**：Hull 备艇捕 jubarte、
Dick Sand 留守 Pilgrim、母鲸尾击碎艇、全员葬身、少年独掌舵——单一捕鲸覆没事件。**排除**：DSCF whale 73 中捕鲸泛述剔除。
exact-slug whale-hunt-disaster ABSENT。**DSCF 4-char → page-top RFC-0003 Note**（同 TTLU/ACH/AWED 处理）。

**恰达门 8 distinct solid PN**（DSCF×8，四节分配）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | DSCF-007-007 | Hull 备艇捕 jubarte |
| Overview | DSCF-007-012 | Hull 迫留 Dick Sand 守 Pilgrim（宿命设置）|
| What Happens | DSCF-008-039 | 鲸中鱼叉翻身、露出哺乳幼鲸 |
| What Happens | DSCF-008-083 | 母鲸尾拍海面、掀巨浪 |
| What Happens | DSCF-008-108 | 尾下重击捕鲸艇 |
| What Happens | DSCF-008-112 | Dick Sand 赶到、活口全无 |
| Significance | DSCF-009-002 | Hull 与众人永逝 |
| Significance | DSCF-009-035 | 全员随之葬身 |

**VVV 处置**：DSCF 4-char，PN 渲染为 plain text，已加 page-top RFC-0003 Note。pn_validator strict ✓（重叠度门全过，无回炉）。

event 计数 24→25，registry total 1499→**1500（里程碑）**，unknown 恒 0。add_page 一次成型（rev VncGcd，size 2746，
quality 自动 featured）。prose-gate awk 首过 0 超段（awk 加 `!/^> /` 排除 Note 块引用）。
location=The Pilgrim、pn_anchor=DSCF-008、book='Dick Sand: A Captain at Fifteen'（含冒号 → 单引号）、aliases=[The Loss of Captain Hull]。
链 *[[dick-sand-a-captain-at-fifteen]]*（Hull/Dick Sand 未建 character，散文提及；Pilgrim 无 place 页，指向 work）。build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=2<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| whale-hunt-disaster | VncGcd | Dick Sand: A Captain at Fifteen | The Pilgrim | DSCF-008 | 8 | Hull 捕鲸覆没单指；剔捕鲸泛述；DSCF 4-char 加 RFC-0003 Note；book 含冒号用单引号 |

- **whale-hunt-disaster**：8 distinct solid PN（DSCF 全用，四节分配）；aliases [The Loss of Captain Hull]；event-schema 四 H2 + page-top Note。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指捕鲸覆没；泛述剔除；strict ✓。✔
- **G2 段落 ≤400 字**：首过 0 超段。✔
- **G3 ≥5 distinct PN**：8 solid（DSCF），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；book 含冒号用单引号；4-char Note 就位。✔
- **registry 一致**：total 1500 event 25 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug whale-hunt-disaster ABSENT；非既有 24 event；无 alias 冲突。✔
- **单指核**：DSCF-007→009 捕鲸覆没逐句确认指同一事件。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R247 起始计数）

| 字段 | R246 起始 | R247 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 246 | 247 |
| type_round | 12 | 13 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 182 | 183 |
| last_updated_round | 246 | 247 |

## 遗留问题

1. **event 页数 25**：本轮 +1（首个 DSCF event）。队列余 1（建序 11）。registry 全库 **1500**，unknown 0。
2. **下轮 R247 = NEW1（event）**：建 queue 建序 11 **The Abduction by the Albatross**（RC，RC-005）。
   since_evv5=2<10、streak=0、queue(event)=1>0 → §3(7) NEW1。RC 2-char，无需 RFC-0003 Note。
   建时核 Weldon Institute 二人（Uncle Prudent、Phil Evans）被 Robur 手下堵嘴蒙眼掳走单指。
3. **R247 后 queue(event) 将罄**：建序 11 消费后 queue(event)==0，R248 触发 §3(4) SCN28-zombie（event discover 第 3 轮）。
4. **event PN 回填债（R244 EVV5 记录）**：13/23 早期页 <5 PN，DEFERRED。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **corpus-discover 顺延**：since_corpus=182→183（dead 变量）。
7. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
8. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
