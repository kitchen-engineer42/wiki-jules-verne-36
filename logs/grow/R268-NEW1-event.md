---
round: 268
date: 2026-07-18
type_round: 35
phase: "2.1"
current_type: event
gene: NEW1
pages: [death-of-martin-paz]
result: success
---

# GROW 2.1-B · R268 · NEW1 · event — 建 The Death of Martin Paz（马德拉大瀑布救 Sarah 被箭穿心、二人同坠瀑涡殉情，PL）

## 执行摘要

Phase 2.1-B event 类型第 25 建（type_round 35），消费 R267 discover 队列**建序 25（首位）**。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10；streak=0<3；since_discover=0<10、全局 queue≥10；queue(event)=3>0 → §3(4) 否；stub%=0 → §3(7)）。

**The Death of Martin Paz**（PL 首 event）。年轻印第安人 Martin Paz 于马德拉大瀑布边，以套索缚住载着被判死刑的 Sarah 的独木舟、悬之于深渊之上，
终被一箭穿心，仰跌入舟、与 Sarah 同坠瀑涡殉情。

**锚核（本轮无精修）**：R267 队列记 pn_anchor=**PL-009**，逐句核该章确为殉情全程所在（瀑布 047 → Sarah 定死于此 048 → Martin Paz 现身 056 → 套索缚舟 060 → 舟悬深渊 064 → 箭穿心同坠 065 → 胜利呼声 066 → 永世结缡 071），锚 **PL-009** 确认无误、保持。

**单指核**：全 8 PN 单指 Martin Paz 瀑布救人-殉情这一连续事件（险境→现身→缚舟→力持→中箭→同坠→结局）。
**排除**：前章 Lima 印第安起义、族斗、Don Vegal/Samuel 恩怨别线剔除，仅取瀑布终局本身之句。
exact-slug death-of-martin-paz ABSENT（变体 martin-paz-death/cataract-of-the-madeira 亦 ABSENT）。**PL 2-char → 无需 page-top Note**。

**恰达门 8 distinct solid PN**（全 PL-009，一章内殉情全程）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | PL-009-047 | 村上马德拉自百尺高处倾泻、泡沫瀑布碎于利岩（险境）|
| What Happens | PL-009-048 | 不幸少女注定死于此泡沫风暴、日出时曝于独木舟（Sarah 定死）|
| What Happens | PL-009-056 | 忽一人现于对岸——乃 Martin Paz、Don Vegal 与印第安 Liberta 在侧（现身）|
| What Happens | PL-009-060 | 立岩上挥套索、长皮索自头顶展开、缚舟于将坠之际（缚舟）|
| What Happens | PL-009-064 | Martin Paz 倍力、舟悬深渊之上、水流不能胜其力（力持）|
| Significance | PL-009-065 | 忽一箭穿 Martin Paz 之心、仰跌入舟、随流与 Sarah 同坠瀑涡（同坠）|
| Significance | PL-009-066 | 胜利之呼声起于激流之上（呼声）|
| Significance | PL-009-071 | Martin Paz 与 Sarah 于短暂而终极之重逢中永世结缡（结局）|

**VVV 处置**：PL 2-char，PN 渲染正常，无需 RFC-0003 Note。
prose-gate awk 首过仅 Participants bullet 块合并误报（三 bullet 各 184/141/153 字，均 <400）。pn_validator --mode strict ✓。

event 计数 39→40，registry total 1514→**1515**，unknown 恒 0。add_page 一次成型（rev L2ELMJ，size 2567，
quality 自动 featured）。
location=Cataracts of the Madeira、pn_anchor=PL-009、book=The Pearl of Lima、aliases=[Martin Paz's Sacrifice, The Rescue at the Madeira Cataract]。
链 *[[the-pearl-of-lima|The Pearl of Lima]]*（Martin Paz、Sarah、Don Vegal、Liberta 未建 character，散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=0<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| death-of-martin-paz | L2ELMJ | The Pearl of Lima | Cataracts of the Madeira | PL-009 | 8 distinct | 瀑布救人-殉情单指（缚舟→中箭→同坠）；锚 PL-009 核实无误保持；剔前章起义/族斗别线；PL 2-char 无 Note |

- **death-of-martin-paz**：8 distinct solid PN（全 PL-009，一章内殉情全程）；aliases [Martin Paz's Sacrifice, The Rescue at the Madeira Cataract]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指瀑布殉情；前章起义/族斗别线剔除；strict ✓。✔
- **G2 段落 ≤400 字**：散文段首过 0 超段；Participants bullet 各 <400（184/141/153，awk 块合并误报已核）。✔
- **G3 ≥5 distinct PN**：8 solid（全 PL-009），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；PL 2-char 无需 Note。✔
- **registry 一致**：total 1515 event 40 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug death-of-martin-paz ABSENT；变体 ABSENT；非既有 39 event；无 alias 冲突。✔
- **单指核**：PL-009 殉情全程逐句确认；锚核实无误无需精修。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R269 起始计数）

| 字段 | R268 起始 | R269 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 268 | 269 |
| type_round | 34 | 35 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 204 | 205 |
| last_updated_round | 268 | 269 |

## 遗留问题

1. **event 页数 40**：本轮 +1（PL 首 event）。queue(event) 3→**2**（建序 25 消费，余 26-27）。registry 全库 **1515**，unknown 0。
2. **下轮 R269 = NEW1（event）**：建 queue 建序 26 **christiania-lottery-drawing**（TN，TN-019）。
   since_evv5=2<10、streak=0、queue(event)=2>0 → §3(7) NEW1。**TN 2-char 无需 Note**。
   建时核抽奖-认领单指（9672 中奖 → Ole Kamp 生还现身认领）、剔前章 Hulda/Sandgoist 让票别线；工作页（若存 ticket-no-9672）链回。
3. **消歧方法论四例沉淀（R256/R260/R261/R264）**：event discover 队列锚点须视为线索非定论，建时逐句复核锚点章实指。已积四例修正 + 两例核实无误（R265 MZ-005、R268 PL-009）。
4. **event 覆盖**：28/36 部作品含 event；本会话由 15/36 经 WC/TT/BR/DOSE/WAI/MZ/PL 增至 28/36。
5. **event PN 回填债（R244/R255/R266 EVV5 记录）**：13/40 早期页 <5 PN，DEFERRED，下次 EVV5（约 R277）或 EVV6 再审。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **corpus-discover 顺延**：since_corpus=204→205（dead 变量）。
8. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
9. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
