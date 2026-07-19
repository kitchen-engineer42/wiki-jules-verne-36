---
round: 259
date: 2026-07-18
type_round: 26
phase: "2.1"
current_type: event
gene: NEW1
pages: [waif-cynthia-rescue]
result: success
---

# GROW 2.1-B · R259 · NEW1 · event — 建 The Rescue of the Waif of the Cynthia（弃婴卧浮标摇篮获渔夫救起，WC）

## 执行摘要

Phase 2.1-B event 类型第 19 建（type_round 26），消费 R258 discover 队列**建序 19（首位）**。决策机 §3 首匹配 **NEW1**
（since_evv5=3<10；streak=0<3；since_discover=0<10、全局 queue≥10；queue(event)=3>0 → §3(4) 否；stub=0 → §3(7)）。

**The Rescue of the Waif of the Cynthia**（WC 首 event）。事件锚定 pn_anchor=**WC-002**（渔夫 Hersebom 向医生 Malarius 陈述弃婴身世之章）。
逐句核**单指该弃婴获救事件**：医生自 Malarius 处知婴儿非渔夫亲子系海难漂来（WC-002-063）、Hersebom 郑重承认非亲生（WC-002-064）、
峡湾岛口垂钓时划向白物见柳条摇篮裹毛毯系浮标卧睡婴（WC-002-068）、唯海难可解且浮标习刻船名（WC-002-087）、
终忆浮标刻 'Cynthia'（WC-002-091）、Katrina 视如己出与 Otto/Vanda 并列（WC-002-065）、抚养无别（WC-002-069）、
多年后 Erik 由父述摇篮漂流获救而恍悟身世（WC-006-013）——单一弃婴获救事件及其身世线索。
**排除**：WC-002-068 系单一巨段（约 30 句叙述摇篮/浮标/婴儿，计 1 distinct PN）；后续身世追查（Erik 寻亲远航）泛述剔除。
exact-slug waif-cynthia-rescue ABSENT（变体 cynthia-waif-rescue/finding-of-erik 亦 ABSENT）。**WC 2-char → 无需 page-top Note**。

**恰达门 8 distinct solid PN**（WC-002×7 + WC-006×1，四节分配）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | WC-002-063 | 医生知婴非亲子、系海难漂来获收养（缘起）|
| What Happens | WC-002-064 | Hersebom 郑重承认男孩非亲生（证实）|
| What Happens | WC-002-068 | 峡湾岛口划向白物、见柳条摇篮系浮标卧睡婴（获救实况）|
| What Happens | WC-002-087 | 唯海难可解、浮标习刻所属船名（线索）|
| Significance | WC-002-091 | 终忆浮标刻名 'Cynthia'、失船得名（船名揭晓）|
| Significance | WC-002-065 | Katrina 视如己出、与 Otto/Vanda 并列为子（家庭）|
| Significance | WC-002-069 | 可怜小儿今为己子、抚养无别（收养定情）|
| Significance | WC-006-013 | 多年后 Erik 由父述摇篮漂流获救而恍悟己史（身世落定）|

**VVV 处置**：WC 2-char，PN 渲染正常，无需 RFC-0003 Note。
prose-gate awk 首过 0 超段。pn_validator --mode strict ✓（重叠度门全过，无回炉）。

event 计数 33→34，registry total 1508→**1509**，unknown 恒 0。add_page 一次成型（rev 4KDNOS，size 2469，
quality 自动 featured）。
location=Noroe、pn_anchor=WC-002、book=The Waif of the Cynthia、aliases=[The Finding of Erik]。
链 *[[the-waif-of-the-cynthia|The Waif of the Cynthia]]*（Hersebom、Katrina、Erik、Malarius 未建 character，散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =3 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=0<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| waif-cynthia-rescue | 4KDNOS | The Waif of the Cynthia | Noroe | WC-002 | 8 | 弃婴卧浮标摇篮获救单指；WC-002-068 单一巨段计 1 PN；剔后续身世追查泛述；WC 2-char 无 Note |

- **waif-cynthia-rescue**：8 distinct solid PN（WC-002×7 + WC-006×1，四节分配）；aliases [The Finding of Erik]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指弃婴获救；后续 Erik 寻亲泛述剔除；strict ✓。✔
- **G2 段落 ≤400 字**：首过 0 超段。✔
- **G3 ≥5 distinct PN**：8 solid（WC-002×7 + WC-006×1），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；WC 2-char 无需 Note。✔
- **registry 一致**：total 1509 event 34 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug waif-cynthia-rescue ABSENT；变体 ABSENT；非既有 33 event；无 alias 冲突。✔
- **单指核**：WC-002 弃婴获救逐句确认指同一事件；WC-002-068 巨段计 1 PN；身世追查泛述排除。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R260 起始计数）

| 字段 | R259 起始 | R260 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 259 | 260 |
| type_round | 25 | 26 |
| rounds_since_last_evv5 | 3 | 4 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 195 | 196 |
| last_updated_round | 259 | 260 |

## 遗留问题

1. **event 页数 34**：本轮 +1（WC 首 event）。queue(event) 3→**2**（建序 19 消费，余建序 20-21）。registry 全库 **1509**，unknown 0。
2. **下轮 R260 = NEW1（event）**：建 queue 建序 20 **kilimanjaro-cannon-shot**（TT，TT-004）。
   since_evv5=4<10、streak=0、queue(event)=2>0 → §3(7) NEW1。TT 2-char 无需 Note。
   建时核 900 尺巨炮单次发射单指、剔 Gun Club 筹谋泛述。
3. **event 覆盖**：22/36 部作品含 event；本会话 +WC。
4. **event PN 回填债（R244/R255 EVV5 记录）**：13/34 早期页 <5 PN，DEFERRED，下次 EVV5（约 R267）再审。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **corpus-discover 顺延**：since_corpus=195→196（dead 变量）。
7. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
8. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
