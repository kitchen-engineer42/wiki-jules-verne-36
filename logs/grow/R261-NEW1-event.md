---
round: 261
date: 2026-07-18
type_round: 28
phase: "2.1"
current_type: event
gene: NEW1
pages: [charleston-blockade-run]
result: success
---

# GROW 2.1-B · R261 · NEW1 · event — 建 The Running of the Charleston Blockade（Dolphin 恃速强闯 Charleston 封锁线，BR）

## 执行摘要

Phase 2.1-B event 类型第 21 建（type_round 28），消费 R258 discover 队列**建序 21（末位）**。决策机 §3 首匹配 **NEW1**
（since_evv5=5<10；streak=0<3；since_discover=2<10、全局 queue≥10；queue(event)=1>0 → §3(4) 否；stub=0 → §3(7)）。

**The Running of the Charleston Blockade**（BR 首 event）。汽船 Dolphin 由 James Playfair 指挥，恃速与浅吃水强闯南北战争中的 Charleston 联邦封锁线（入港+出港）。
**锚精修**：R258 队列记 pn_anchor=**BR-003**，然逐句核 BR-003 系 Miss Halliburtt 陈情登船之由（欲赴被围之 Charleston 救父），非强闯本身。
真正的强闯：**入港**在 **BR-006**（定向、择 Sullivan 峡道、过 Fort Sumter、升英国旗高速穿窄道入湾）→ 抵港 BR-007-002；**出港突围**在 BR-009（Fort Sumter 逃逸信号、灯塔隐没、炮弹掠空、脱入大西洋）。锚改 **BR-006**（强闯之章）。slug 保持 charleston-blockade-run。

**单指核**：全 8 PN 单指 Dolphin 之封锁线强闯（立意→入港→抵港→出港突围），一连续事件。
**排除**：BR-003 Halliburtt 陈情、BR-004 父女谈判、BR-008 救援 Halliburtt 越狱筹划等属另线（人物/救援情节），剔除，仅取立意两句框定事件。
exact-slug charleston-blockade-run ABSENT（变体 running-the-blockade/dolphin-blockade-run/the-blockade-run 亦 ABSENT）。**BR 2-char → 无需 page-top Note**。

**恰达门 8 distinct solid PN**（BR-001×2 + BR-006×3 + BR-007×1 + BR-009×2，四节分配）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | BR-001-042 | Playfair 立誓指挥汽船、恃速蔑联邦海军、强闯某南方港（立意）|
| What Happens | BR-001-052 | 舍 New Orleans/Wilmington/Savannah、直取 Charleston、浅吃水可往联邦不可追处（择的）|
| What Happens | BR-006-012 | 定向毕、唯一悬念系择何峡道入 Charleston 湾（抉择）|
| What Happens | BR-006-030 | Fort Sumter 蔽其于联邦炮台、悄然掠过（闯关）|
| What Happens | BR-006-035 | 穿 Morris Island 灯塔浮标、升英国旗高速穿窄道、自由入湾中（入港实况）|
| Significance | BR-007-002 | 抵 Charleston 码头受万众欢呼、知其强闯 Sullivan 运私弹、欢声再倍（受迎）|
| Significance | BR-009-070 | 灯塔西南隐没、炮声渐弱、巡逻炮舰一弹掠空曳火线（出港险）|
| Significance | BR-009-076 | 汽船速脱大西洋、美岸没于夜、远火示 Morris Island 与 Charleston 诸炮台激战（脱险）|

**VVV 处置**：BR 2-char，PN 渲染正常，无需 RFC-0003 Note。
prose-gate awk 首过仅 Participants bullet 块合并误报（三 bullet 各 180/178/142 字，均 <400）。pn_validator --mode strict ✓。

event 计数 35→36，registry total 1510→**1511**，unknown 恒 0。add_page 一次成型（rev E2CxwS，size 3028，
quality 自动 featured）。
location=Charleston、pn_anchor=BR-006、book=The Blockade Runners、aliases=[The Dolphin's Blockade Run, The Forcing of the Charleston Blockade]。
链 *[[the-blockade-runners|The Blockade Runners]]*、[[Charleston]]（James Playfair、Miss Halliburtt、Crockston 未建 character，散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =5 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=2<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| charleston-blockade-run | E2CxwS | The Blockade Runners | Charleston | BR-006 | 8 distinct | Dolphin 强闯封锁线单指（入+出）；**锚由 queue 记 BR-003（Halliburtt 陈情）精修为 BR-006（强闯）**；剔救援/人物别线；BR 2-char 无 Note |

- **charleston-blockade-run**：8 distinct solid PN（BR-001×2 + BR-006×3 + BR-007×1 + BR-009×2，四节分配）；aliases [The Dolphin's Blockade Run, The Forcing of the Charleston Blockade]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Dolphin 强闯；Halliburtt 陈情/救援别线剔除；strict ✓。✔
- **G2 段落 ≤400 字**：散文段首过 0 超段；Participants bullet 各 <400（awk 块合并误报已核）。✔
- **G3 ≥5 distinct PN**：8 solid（BR-001/006/007/009），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；BR 2-char 无需 Note。✔
- **registry 一致**：total 1511 event 36 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug charleston-blockade-run ABSENT；变体 ABSENT；非既有 35 event；无 alias 冲突。✔
- **单指核**：BR-006 强闯逐句确认；BR-003 Halliburtt 陈情精修排除；救援别线排除。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R262 起始计数）

| 字段 | R261 起始 | R262 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 261 | 262 |
| type_round | 27 | 28 |
| rounds_since_last_evv5 | 5 | 6 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 197 | 198 |
| last_updated_round | 261 | 262 |

## 遗留问题

1. **event 页数 36**：本轮 +1（BR 首 event）。queue(event) 1→**0**（建序 19-21 全数消费）。registry 全库 **1511**，unknown 0。
2. **下轮 R262 = SCN28-zombie（event discover 第 6 轮）**：queue(event)==0 → §3(4) 触发。
   须从未覆盖作品播 ≥3 net-new event 候选。仍余零 event 作品：ASC（A Special Correspondent / Claudius Bombarnac）、WAI（Winter Amid the Ice）、
   DOSE（Doctor Ox）、PL（Pearl of Lima）、TN（Ticket No. 9672）、MZ（Master Zacharius）、SC/SC2、DA、DSCF、VB 等可续掘；UC-005 神秘炸柱悬疑亦可考（播种前须核 ≥5 distinct 可达）。
3. **消歧方法论沉淀（R256/R260/R261）**：event discover 队列锚点须视为线索非定论，建时逐句复核锚点章实指。
   已积三例：R256 UC-005→UC-018（firedamp 别章）、R260 TT-004→TT-018（月射回顾 vs 改地轴炮）、R261 BR-003→BR-006（陈情 vs 强闯）。
4. **event 覆盖**：24/36 部作品含 event；本会话 +WC +TT +BR。
5. **event PN 回填债（R244/R255 EVV5 记录）**：13/36 早期页 <5 PN，DEFERRED，下次 EVV5（约 R267）再审。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **corpus-discover 顺延**：since_corpus=197→198（dead 变量）。
8. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
9. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
