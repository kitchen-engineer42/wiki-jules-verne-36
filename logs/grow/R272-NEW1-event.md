---
round: 272
date: 2026-07-18
type_round: 39
phase: "2.1"
current_type: event
gene: NEW1
pages: [death-of-captain-nemo]
result: success
---

# GROW 2.1-B · R272 · NEW1 · event — 建 Death of Captain Nemo（Nemo 于 Nautilus 弥留、诵「God and my country!」溘逝、沉舟为墓，SI）

## 执行摘要

Phase 2.1-B event 类型第 28 建（type_round 39），消费 R271 discover 队列**建序 28（首位）**。决策机 §3 首匹配 **NEW1**
（since_evv5=5<10；streak=0<3；since_discover=0<10、全局 queue≥10；queue(event)=3>0 → §3(4) 否；stub%=0 → §3(7)）。

**Death of Captain Nemo**（SI 首 event）。Lincoln 岛神秘恩人 Nemo 于 Dakkar Grotto 泊定之 Nautilus 内弥留，
向殖民者自陈身世、请其代行遗愿；午夜叠臂、口诵「God and my country!」溘然长逝；殖民者依愿开阀，Nautilus 缓沉海底为其墓。

**锚核（本轮无精修）**：R271 队列记 pn_anchor=**SI-017**，逐句核该章确为弥留-长逝-沉舟全程所在
（愿殁 Nautilus 003 → 此地就死遗请 012 → 许诺遗愿 021 → 渐沉神态安详 076 → 叠臂待终 078 → 溘逝 079 → 阖 Prince Dakkar 之目 080 → 开阀渐沉 089），锚 **SI-017** 确认无误、保持。

**单指核**：全 9 PN 单指 Nemo 弥留-长逝-沉舟这一连续事件（愿殁→遗请→许诺→渐沉→叠臂→溘逝→揭身世→沉舟）。
**排除**：Nemo 身世自述长篇（SI-016）、殖民者后续重建、荒岛毁灭（建序 29）等别线剔除，仅取弥留-长逝-沉舟本身之句。
exact-slug death-of-captain-nemo ABSENT（变体 nemo-death/last-moments-of-captain-nemo 亦 ABSENT）。**SI 2-char → 无需 page-top Note**。

**工作页处置**：SI（The Secret of the Island，神秘岛第三部）无独立 work 页；改链既有 work 页 **[[The Mysterious Island]]**（Overview 段）+ character 页 **[[Captain Nemo]]**（Significance 段）。book 字段用 SI 章节页书名 **The Secret of the Island**。

**恰达门 9 distinct solid PN**（全 SI-017，一章内弥留全程）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | SI-017-003 | 愿留 Nautilus 至终、不欲移至 Granite House（愿殁）|
| What Happens | SI-017-012 | 「我将殁于此——此我所愿」、有一请相托（遗请）|
| What Happens | SI-017-021 | 「许我，代行遗愿，则我此生所为皆偿」（许诺）|
| What Happens | SI-017-076 | Nemo 无痛而显沉、面容为死气所白而全然平静（渐沉）|
| What Happens | SI-017-078 | 午夜后竭力叠臂于胸、若欲以此姿而终（叠臂）|
| Significance | SI-017-079 | 口诵「God and my country!」溘然长逝（溘逝）|
| Significance | SI-017-080 | Harding 俯身阖 Prince Dakkar 之目、其名今已不存（揭身世）|
| Significance | SI-017-089 | 开阀注水、Nautilus 缓沉没于水下为 Nemo 之墓（沉舟）|

**VVV 处置**：SI 2-char，PN 渲染正常，无需 RFC-0003 Note。
prose-gate awk 首过仅 Participants bullet 块合并误报（三 bullet 各 151/154/181 字，均 <400）。pn_validator --mode strict ✓。

event 计数 42→43，registry total 1517→**1518**，unknown 恒 0。add_page 一次成型（rev fL4Vjr，size 2470，
quality 自动 featured）。
location=Lincoln Island、pn_anchor=SI-017、book=The Secret of the Island、aliases=[The Last Moments of Captain Nemo, Death of Prince Dakkar]。
链 [[The Mysterious Island]] + [[Captain Nemo]]（Cyrus Harding、Ayrton 等未建/散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=0<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| death-of-captain-nemo | fL4Vjr | The Secret of the Island | Lincoln Island | SI-017 | 9 distinct | 弥留-长逝-沉舟单指（诵「God and my country」→ 揭身世 Prince Dakkar → 沉舟为墓）；锚 SI-017 核实无误保持；剔身世自述/荒岛毁灭别线；SI 2-char 无 Note；无 work 页改链 [[The Mysterious Island]] |

- **death-of-captain-nemo**：9 distinct solid PN（全 SI-017，一章内弥留全程）；aliases [The Last Moments of Captain Nemo, Death of Prince Dakkar]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指弥留-沉舟；身世自述/重建/荒岛毁灭别线剔除；strict ✓。✔
- **G2 段落 ≤400 字**：散文段首过 0 超段；Participants bullet 各 <400（151/154/181，awk 块合并误报已核）。✔
- **G3 ≥5 distinct PN**：9 solid（全 SI-017），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；SI 2-char 无需 Note。✔
- **registry 一致**：total 1518 event 43 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug death-of-captain-nemo ABSENT；变体 ABSENT；非既有 42 event；无 alias 冲突。✔
- **单指核**：SI-017 弥留全程逐句确认；锚核实无误无需精修。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R273 起始计数）

| 字段 | R272 起始 | R273 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 272 | 273 |
| type_round | 38 | 39 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 208 | 209 |
| last_updated_round | 272 | 273 |

## 遗留问题

1. **event 页数 43**：本轮 +1（SI 首 event）。queue(event) 3→**2**（建序 28 消费，余 29-30）。registry 全库 **1518**，unknown 0。
2. **下轮 R273 = NEW1（event）**：建 queue 建序 29 **destruction-of-lincoln-island**（SI，SI-019）。
   since_evv5=6<10、streak=0、queue(event)=2>0 → §3(7) NEW1。**SI 2-char 无需 Note**。
   建时核火山复苏-熔岩毁地-气爆没岛单指、剔 Duncan 救援(另一事件)/Nemo 之死(建序28)别线；无 work 页链 [[The Mysterious Island]]。
3. **消歧方法论四例沉淀（R256/R260/R261/R264）**：queue 锚点视为线索非定论，建时逐句复核。已积四例修正 + 五例核实无误（R265/R268/R269/R270/R272）。
4. **event 覆盖 31/36**：本会话 SI 入册；建序 30（DA）建毕后达 32/36。
5. **event PN 回填债（R244/R255/R266 EVV5）**：13/43 早期页 <5 PN，DEFERRED，下次 EVV5（约 R277）再审。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **corpus-discover 顺延**：since_corpus=208→209（dead 变量）。
8. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
9. **零 event 剩余**：VB（备选）、AMB/YEAR（判非事件）。建序 29-30 建毕后 queue(event) 归 0 → R275 = SCN28-zombie（掘 VB 或跨作品）。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
