---
round: 236
date: 2026-07-18
type_round: 2
phase: "2.1"
current_type: event
gene: NEW1
pages: [comet-collision]
result: success
---

# GROW 2.1-B · R236 · NEW1 · event — 建 The Comet's Collision（彗星撞地球析出 Gallia，OC）

## 执行摘要

Phase 2.1-B event 类型第 3 建（type_round 2）。决策机 §3 首匹配 **NEW1**（since_evv5=2<10；streak=0<3；
since_discover=2<10、全局 queue≥10；queue(event)=2>0 → §3(4) 否；stub=0 → §3(7)）。

取 R233 event 队列**建序 3** **The Comet's Collision**（OC 主）。事件锚定 pn_anchor=**OC-027**
（Gallian Academy 定案彗星撞地之章）。gather 事件核心（"Gallia" distinctPN=156 全 OC；"collision" 124；
"comet" OC 独占 134）。逐句核**单指该事件**（12-31 夜彗星越黄道撞地球 → 析出一隅载幸存者入太空 → 名 Gallia），
剔泛指彗星（FEM/FWB/RM 等）。exact-slug comet-collision ABSENT。

**恰达门 8 distinct solid PN**（OC×8，四节分配）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | OC-027-037 | Gallian Academy 定案：12-31 夜彗星越黄道撞地，震裂析出一隅 |
| What Happens | OC-016-036 | Procope 早期假说：地球一隅被抛入太空 |
| What Happens | OC-027-030 | 地彗相撞、小世界被劈离飞入太空（确证）|
| What Happens | OC-027-032 | Timascheff 述彗星得名 Gallia |
| What Happens | OC-028-080 | Rosette 确认：1-1 凌晨 2:47 彗星掠地析出碎块 |
| What Happens | OC-028-083 | 「You are on my comet, on Gallia itself!」|
| Significance | OC-006-034 | 重力剧变：一跃三十英尺（新世界异象）|
| Significance | OC-007-038 | 1-6 行军见四村消失、岬角削平（灾后地貌）|

**VVV 处置**：OC 2-char 码，PN 正常渲染，无需 RFC-0003 Note。pn_validator strict ✓。

event 计数 17→18，registry total 1492→1493，unknown 恒 0。add_page 一次成型（rev SxkeJV，size 2564，
quality 自动 featured）。prose-gate awk 初 3 段超（Overview 406 / What Happens 425+439），拆分后 0 超段。
location=Gallia、pn_anchor=OC-027、book=Off on a Comet、aliases=[The Birth of Gallia]。
链 [[Gallia]]/[[Off on a Comet]]（Servadac/Timascheff/Procope/Rosette 未建 character，散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =2 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=2<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =2>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| comet-collision | SxkeJV | Off on a Comet | Gallia | OC-027 | 8 | 彗星撞地析出 Gallia；单事件核；OC 2-char 无需 RFC-0003 Note |

- **comet-collision**：8 distinct solid PN（OC 全用，四节分配）；aliases [The Birth of Gallia]；event-schema 四 H2。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指该事件（Gallia 诞生）；泛指彗星已剔；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：初 3 段超（406/425/439），拆分后 0 超段。✔
- **G3 ≥5 distinct PN**：8 solid（OC），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；description 单引号（含撇号 New Year''s，'' 转义）。✔
- **registry 一致**：total 1493 event 18 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug comet-collision ABSENT；非既有 17 event。✔
- **单指核**：OC ch16-28 逐句确认指同一撞击析出事件。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R237 起始计数）

| 字段 | R236 起始 | R237 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 236 | 237 |
| type_round | 2 | 3 |
| rounds_since_last_evv5 | 2 | 3 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 172 | 173 |
| last_updated_round | 236 | 237 |

## 遗留问题

1. **event 页数 18**：本轮 +1（The Comet's Collision）。registry 全库 1493，unknown 0。
   event 队列余 1（建序 4）：forward-mutiny（ACH）。
2. **下轮 R237 = NEW1（event）**：建 queue 建序 4 **The Forward Mutiny**（ACH，Forward 号船员哗变弃船焚船）。
   since_evv5=3<10、streak=0、queue(event)=1>0 → §3(7) NEW1。**注**：ACH 4-char VVV → 须加 RFC-0003 Note。
3. **R237 后 event 队列将罄**：建 forward-mutiny 后 queue(event)==0 → R238 = §3(4) SCN28-zombie（首轮 event discover 复评/续掘）。
   event 空间广阔（36 部作品仅 5+4 部有 event），SCN28 应能续掘 ≥3 净新事件锚点，保 streak=0 续 NEW1。
4. **event 建页方法论续遵**：pn_anchor 锚定 + 单事件单指核 + 四节侧面分配。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **corpus-discover 顺延**：since_corpus=172→173（dead 变量）。
7. **EVV6 封存点**：Phase 2.1 关闭前须对每类型执行 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
8. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
