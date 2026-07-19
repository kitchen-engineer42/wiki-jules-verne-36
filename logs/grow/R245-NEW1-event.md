---
round: 245
date: 2026-07-18
type_round: 11
phase: "2.1"
current_type: event
gene: NEW1
pages: [chancellor-fire]
result: success
---

# GROW 2.1-B · R245 · NEW1 · event — 建 The Burning of the Chancellor（棉货舱自燃、无法扑救的海上火灾，SC2）

## 执行摘要

Phase 2.1-B event 类型第 9 建（type_round 11），消费 R243 discover 队列**建序 9**。R244 EVV5 reset since_evv5=0，
决策机 §3 首匹配 **NEW1**（since_evv5=0<10；streak=0<3；since_discover=1<10、全局 queue≥10；queue(event)=3>0 → §3(4) 否；stub=0 → §3(7)）。

**The Burning of the Chancellor**（SC2 主，首个 SC2 event）。事件锚定 pn_anchor=**SC2-009**（察觉船货起火之章）。
gather("fire"/"combustion"/"cotton"/"smoke"/"flames" SC2)。逐句核**单指该事件**：SC2 棉货舱自燃、
Curtis 封舱隔绝空气未果、甲板拱起黑烟、终弃救船——单一持续火灾事件。**排除**：SC2 中枪火/炉火泛指句剔除。
exact-slug chancellor-fire ABSENT（burning-of-the-chancellor/chancellor-shipwreck 变体亦 ABSENT）。SC2 3-char，无需 RFC-0003 Note。

**恰达门 8 distinct solid PN**（SC2×8，四节分配）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | SC2-009-002 | Kazallon 惊悉最可怖之灾 |
| Overview | SC2-009-005 | 货舱着火、无法触及燃烧源 |
| What Happens | SC2-009-008 | 棉花 spontaneous combustion 起因 |
| What Happens | SC2-010-005 | Curtis 封舱隔气图扼火 |
| What Happens | SC2-013-012 | 甲板拱起、黑烟如安全阀喷出 |
| What Happens | SC2-012-003 | Curtis 认败：flames will find a vent |
| Significance | SC2-010-010 | 任何震动或引爆炸——浮动火药库 |
| Significance | SC2-012-012 | Curtis 眼睁睁船付烈焰的痛楚 |

**VVV 处置**：SC2 3-char，PN 正常渲染，无需 RFC-0003 Note。pn_validator strict ✓（重叠度门全过，无回炉）。

event 计数 23→24，registry total 1498→1499，unknown 恒 0。add_page 一次成型（rev gYF2mt，size 2711，
quality 自动 featured）。prose-gate awk 首过 0 超段。
location=The Chancellor、pn_anchor=SC2-009、book=The Survivors of the Chancellor、aliases=[The Chancellor Cargo Fire]。
链 [[atlantic-ocean]]/*[[survivors-of-the-chancellor]]*（Kazallon/Curtis 未建 character，散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0（R244 reset）| 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=1<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| chancellor-fire | gYF2mt | The Survivors of the Chancellor | The Chancellor | SC2-009 | 8 | 棉货舱自燃单指；剔 SC2 枪火/炉火泛指；work slug 为 survivors-of-the-chancellor（无 the-）；SC2 3-char 无需 Note |

- **chancellor-fire**：8 distinct solid PN（SC2 全用，四节分配）；aliases [The Chancellor Cargo Fire]；event-schema 四 H2。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指棉货舱火灾；泛指剔除；strict ✓。✔
- **G2 段落 ≤400 字**：首过 0 超段。✔
- **G3 ≥5 distinct PN**：8 solid（SC2），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；description 单引号。✔
- **registry 一致**：total 1499 event 24 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug chancellor-fire ABSENT；非既有 23 event；无 alias 冲突。✔
- **单指核**：SC2-009→013 火灾发展逐句确认指同一事件。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R246 起始计数）

| 字段 | R245 起始 | R246 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 245 | 246 |
| type_round | 11 | 12 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 181 | 182 |
| last_updated_round | 245 | 246 |

## 遗留问题

1. **event 页数 24**：本轮 +1（首个 SC2 event）。队列余 2（建序 10-11）。registry 全库 1499，unknown 0。
2. **下轮 R246 = NEW1（event）**：建 queue 建序 10 **The Whale Hunt Disaster**（DSCF，DSCF-008）。
   since_evv5=1<10、streak=0、queue(event)=2>0 → §3(7) NEW1。DSCF 4-char → **须 RFC-0003 Note**（page-top）。
   建时核 Hull 捕鲸覆没单指（DSCF whale 73 有捕鲸泛述，剔除）。
3. **DSCF 4-char VVV 提醒**：DSCF 为 4 字符 VVV，PN 渲染须加 page-top RFC-0003 Note（同 TTLU/ACH/AWED 处理）。
4. **event PN 回填债（R244 EVV5 记录）**：13/23 早期页 <5 PN，DEFERRED，留 EVV6/RCH2 统一补。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **corpus-discover 顺延**：since_corpus=181→182（dead 变量）。
7. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
8. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
