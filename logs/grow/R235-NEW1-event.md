---
round: 235
date: 2026-07-18
type_round: 1
phase: "2.1"
current_type: event
gene: NEW1
pages: [ice-island-drift]
result: success
---

# GROW 2.1-B · R235 · NEW1 · event — 建 The Drifting Ice-Island（Victoria Island 断裂漂流，FC）

## 执行摘要

Phase 2.1-B event 类型第 2 建（type_round 1）。决策机 §3 首匹配 **NEW1**（since_evv5=1<10；streak=0<3；
since_discover=1<10、全局 queue≥10；queue(event)=3>0 → §3(4) 否；stub=0 → §3(7)）。

取 R233 event 队列**建序 2** **The Drifting Ice-Island**（FC 主）。事件锚定 pn_anchor=**FC-024**
（发现半岛已成浮岛之章）。gather 事件核心（"floating island" distinctPN=17，FC 独占 13；
"Victoria Island" distinctPN=73 全 FC）。逐句核**单指该事件**（1-8 地震将 Cape Bathurst 半岛
从大陆扯断 → 成浮冰岛 Victoria Island → 载 Fort Hope 殖民者漂流北冰洋），剔他作泛指浮岛（AM/TTLU/WC）。
exact-slug ice-island-drift ABSENT。

**恰达门 8 distinct solid PN**（FC×8，四节分配）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | FC-024-002 | 1-8 地震扯离锚泊，成任风浪摆布之浮岛 |
| What Happens | FC-024-032 | Hobson 释因（半岛变浮岛，困兽聚集）|
| What Happens | FC-024-029 | 断连后随潮涨落浮沉 |
| What Happens | FC-025-003 | 保留原名 Victoria Island |
| What Happens | FC-025-015 | 冬寒将 Victoria Island 焊入大冰原 |
| Significance | FC-025-011 | 若南漂太平洋则融解碎裂于居民足下 |
| Significance | FC-028-038 | 浮岛已下沉六英寸（逐寸厄运）|
| Significance | FC-032-002 | Kalumah 于浮岛距美洲岸 200 英里（漂流之远）|

**VVV 处置**：FC 2-char 码，PN 正常渲染，无需 RFC-0003 Note。pn_validator strict ✓。

event 计数 16→17，registry total 1491→1492，unknown 恒 0。add_page 一次成型（rev A3skN9，size 2575，
quality 自动 featured）。prose-gate awk 初 2 段超（What Happens 407 / Significance 406），拆分后 0 超段。
location=Victoria Island、pn_anchor=FC-024、book=The Fur Country、aliases=[The Voyage of Victoria Island]。
链 [[Victoria Island]]/[[Cape Bathurst]]/[[Fort Hope]]/[[The Fur Country]]（Hobson/Kalumah 未建 character，散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=1<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| ice-island-drift | A3skN9 | The Fur Country | Victoria Island | FC-024 | 8 | Cape Bathurst 半岛断裂成浮岛漂流；单事件核；FC 2-char 无需 RFC-0003 Note |

- **ice-island-drift**：8 distinct solid PN（FC 全用，四节分配）；aliases [The Voyage of Victoria Island]；event-schema 四 H2。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指该事件（Victoria Island 断裂漂流）；泛指浮岛已剔；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：初 2 段超（407/406），拆分后 0 超段。✔
- **G3 ≥5 distinct PN**：8 solid（FC），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；description 单引号（含撇号，'' 转义）。✔
- **registry 一致**：total 1492 event 17 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug ice-island-drift ABSENT；非既有 16 event。✔
- **单指核**：FC ch24-32 逐句确认指同一浮岛漂流事件。✔
- **排除检查**：提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R236 起始计数）

| 字段 | R235 起始 | R236 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 235 | 236 |
| type_round | 1 | 2 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 1 | 2 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 171 | 172 |
| last_updated_round | 235 | 236 |

## 遗留问题

1. **event 页数 17**：本轮 +1（The Drifting Ice-Island）。registry 全库 1492，unknown 0。
   event 队列余 2（建序 3-4）：comet-collision（OC/Gallia）/forward-mutiny（ACH）。
2. **下轮 R236 = NEW1（event）**：建 queue 建序 3 **The Comet's Collision**（OC，地球被彗星掠走一隅成 Gallia）。
   since_evv5=2<10、streak=0、queue(event)=2>0 → §3(7) NEW1。注：OC 2-char，无需 RFC-0003 Note。
3. **event 建页方法论续遵**：pn_anchor 锚定 + 单事件单指核 + 四节侧面分配。未建 character（Hobson/Kalumah）散文提及不强链。
4. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
5. **corpus-discover 顺延**：since_corpus=171→172（dead 变量）。
6. **EVV6 封存点**：Phase 2.1 关闭前须对每类型执行 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
7. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
