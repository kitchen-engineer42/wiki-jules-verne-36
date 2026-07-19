---
round: 252
date: 2026-07-18
type_round: 18
phase: "2.1"
current_type: event
gene: NEW1
pages: [amazon-cryptogram]
result: success
---

# GROW 2.1-B · R252 · NEW1 · event — 建 The Amazon Cryptogram（证 Joam Dacosta 清白之密文被 Jarriquez 破译，EHLA）

## 执行摘要

Phase 2.1-B event 类型第 15 建（type_round 18），消费 R248 discover 队列**建序 15（末位）**。决策机 §3 首匹配 **NEW1**
（since_evv5=7<10；streak=0<3；since_discover=3<10、全局 queue≥10；queue(event)=1>0 → §3(4) 否；stub=0 → §3(7)）。

**The Amazon Cryptogram**（EHLA 主，首个 EHLA event）。事件锚定 pn_anchor=**EHLA-027**（密文证据浮现之章）。
gather("document"/"cryptogram"/"Jarriquez"/"innocence"/"cipher" EHLA-026→034)。逐句核**单指该事件**：Torres 所持、
由真凶亲笔所书、证 Joam Dacosta 清白的密文；Judge Jarriquez 辨其为 cryptogram、仿 Poe《Gold Bug》法主攻末段、
终破译致舆情逆转、Dacosta 昭雪——单一破译事件。**排除**：EHLA 中 Amazon 巨筏航行等泛述剔除。
**歧义规避**：EHLA-033-069「234」为 Jarriquez 以己名演示密码之**示例**，非文件真钥，故弃用，改取无歧义文件句。
exact-slug amazon-cryptogram ABSENT（变体 joam-garral-cryptogram 亦 ABSENT）。**EHLA 4-char → 已加 page-top RFC-0003 Note**。

**恰达门 8 distinct solid PN**（EHLA×8，四节分配）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | EHLA-027-002 | 密文由真凶亲笔书、证清白（文件本质）|
| Overview | EHLA-031-057 | Jarriquez 展纸验字："A document it really is!" |
| What Happens | EHLA-031-061 | 判定为 cryptogram |
| What Happens | EHLA-032-022 | 分析家本能被唤、眼前即密文 |
| What Happens | EHLA-032-027 | 集中资源主攻末段 |
| What Happens | EHLA-034-012 | 无空格巨块、试 'diamond'/'Tijuco'/'Dacosta' |
| Significance | EHLA-033-078 | 无辜者蒙冤、清白铁证却在手（利害）|
| Significance | EHLA-034-001 | 舆情逆转、由怒转怜、Dacosta 昭雪 |

**VVV 处置**：EHLA 4-char，PN 渲染为 plain text，已加 page-top RFC-0003 Note（同 TTLU/DSCF 处理）。
prose-gate awk 加 `!/^> /` 排除 Note 块引用。pn_validator --mode strict ✓（重叠度门全过，无回炉）。

event 计数 29→30，registry total 1504→**1505**，unknown 恒 0。add_page 一次成型（rev c19Rac，size 2896，
quality 自动 featured）。prose-gate awk 首过 0 超段。
location=Manaos、pn_anchor=EHLA-027、book=Eight Hundred Leagues on the Amazon、aliases=[The Decipherment of the Innocence Document]。
链 *[[eight-hundred-leagues-on-the-amazon]]*（Joam Dacosta、Jarriquez、Torres、Benito、Manoel 未建 character，散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=3<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| amazon-cryptogram | c19Rac | Eight Hundred Leagues on the Amazon | Manaos | EHLA-027 | 8 | 破译清白密文单指；剔 Amazon 巨筏泛述；避 234 示例歧义；EHLA 4-char 加 Note |

- **amazon-cryptogram**：8 distinct solid PN（EHLA，四节分配）；aliases [The Decipherment of the Innocence Document]；event-schema 四 H2 + page-top Note。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指清白密文破译；Amazon 巨筏及 234 示例句剔除；strict ✓。✔
- **G2 段落 ≤400 字**：首过 0 超段（awk 排除 Note）。✔
- **G3 ≥5 distinct PN**：8 solid（EHLA），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；EHLA 4-char page-top Note 就位。✔
- **registry 一致**：total 1505 event 30 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug amazon-cryptogram ABSENT；非既有 29 event；无 alias 冲突。✔
- **单指核**：EHLA-027→034 密文与破译逐句确认指同一事件。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R253 起始计数）

| 字段 | R252 起始 | R253 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 252 | 253 |
| type_round | 18 | 19 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 188 | 189 |
| last_updated_round | 252 | 253 |

## 遗留问题

1. **event 页数 30**：本轮 +1（首个 EHLA event）。队列 event **已罄**（R248 播的建序 12-15 全数消费）。registry 全库 **1505**，unknown 0。
2. **下轮 R253 = SCN28-zombie（event discover 第 4 轮）**：queue(event)==0 → §3(4) 触发。
   须从未覆盖作品播 ≥3 net-new event 候选（GM Godfrey Morgan、UC Underground City、Steam House、WC Cynthia、
   Kéraban、Green Ray、Tribulations of a Chinaman 等 20+ 部零 event 覆盖作品）。
3. **since_evv5=8→接近阈值**：R255 起 since_evv5 将达 10，触发 §3(1b) EVV5 反思轮（event 模板评审）。
4. **event PN 回填债（R244 EVV5 记录）**：13/23 早期页 <5 PN，DEFERRED。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **corpus-discover 顺延**：since_corpus=188→189（dead 变量）。
7. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
8. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
