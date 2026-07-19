---
round: 257
date: 2026-07-18
type_round: 23
phase: "2.1"
current_type: event
gene: NEW1
pages: [new-aberfoyle-flood]
result: success
---

# GROW 2.1-B · R257 · NEW1 · event — 建 The Flooding of New Aberfoyle（Coal Town 突遭预谋淹没，UC）

## 执行摘要

Phase 2.1-B event 类型第 18 建（type_round 23），消费 R253 discover 队列**建序 18（末位）**。决策机 §3 首匹配 **NEW1**
（since_evv5=1<10；streak=0<3；since_discover=3<10、全局 queue≥10；queue(event)=1>0 → §3(4) 否；stub=0 → §3(7)）。

**The Flooding of New Aberfoyle**（UC 第二 event）。事件锚定 pn_anchor=**UC-016**（Coal Town 突遭淹没之章）。
gather 已于 R256 摸清 UC-016 淹没段落。逐句核**单指该淹没事件**：Coal Town 居民惊逃、疑海水灌入全矿、Simon Ford 止乱判危已解、
急流仅抬升 Loch Malcolm 数尺、Loch Katrine 泄水之谜、Starr 三人返灾场查、发现矿柱遭暗爆预谋掏空——单一（人为）淹没事件及其查因。
**排除**：UC-016-046 系另一次「水箱 stanchion 被锯」小型淹没（婚礼前连环破坏之一），别事件，剔除；UC-016-044/045/047（火灾/矿车）亦剔。
exact-slug new-aberfoyle-flood ABSENT（变体 coal-town-inundation/new-aberfoyle-inundation 亦 ABSENT）。**UC 2-char → 无需 page-top Note**。

**恰达门 8 distinct solid PN**（UC-016×8，四节分配）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | UC-016-006 | Coal Town 惊呼、突遭淹没、居民逃上 schist 岩顶（灾起）|
| What Happens | UC-016-007 | 疑海水灌入全矿、New Aberfoyle 无人得生（最坏设想）|
| What Happens | UC-016-008 | Simon Ford 止乱、判水不再涨、危已解（止乱）|
| What Happens | UC-016-011 | 急流灌入最低层、仅抬 Loch Malcolm 数尺、Coal Town 无损（实况）|
| What Happens | UC-016-012 | Simon 初不辨因、当晚报载 Loch Katrine 泄水奇象（成因谜）|
| Significance | UC-016-025 | Starr 偕 Simon、Harry 决返灾场自证（查因）|
| Significance | UC-016-026 | 查见矿柱遭爆破掏空、焦痕证坍塌系人为预谋（真相：破坏）|
| Significance | UC-016-027 | Starr：若灌入者为海而非小湖后果不堪（利害）|

**VVV 处置**：UC 2-char，PN 渲染正常，无需 RFC-0003 Note。
prose-gate awk 首过 0 超段。pn_validator --mode strict ✓（重叠度门全过，无回炉）。

event 计数 32→33，registry total 1507→**1508**，unknown 恒 0。add_page 一次成型（rev u5LuoG，size 2714，
quality 自动 featured）。
location=New Aberfoyle、pn_anchor=UC-016、book=The Underground City、aliases=[The Inundation of Coal Town]。
链 *[[the-underground-city]]*、[[New Aberfoyle]]（Simon Ford、Harry、James Starr、Nell 未建 character，散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =1 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=3<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| new-aberfoyle-flood | u5LuoG | The Underground City | New Aberfoyle | UC-016 | 8 | Coal Town 预谋淹没单指；剔 UC-016-046 水箱淹没别事件、UC-018 firedamp、UC-005 炸柱；UC 2-char 无 Note |

- **new-aberfoyle-flood**：8 distinct solid PN（UC-016，四节分配）；aliases [The Inundation of Coal Town]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Coal Town 淹没；UC-016-046 水箱淹没及火灾/矿车剔除；strict ✓。✔
- **G2 段落 ≤400 字**：首过 0 超段。✔
- **G3 ≥5 distinct PN**：8 solid（UC-016，8 distinct 段），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；UC 2-char 无需 Note。✔
- **registry 一致**：total 1508 event 33 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug new-aberfoyle-flood ABSENT；变体 ABSENT；非既有 32 event；无 alias 冲突。✔
- **单指核**：UC-016 主淹没逐句确认指同一事件；UC-016-046 别淹没排除。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R258 起始计数）

| 字段 | R257 起始 | R258 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 257 | 258 |
| type_round | 23 | 24 |
| rounds_since_last_evv5 | 1 | 2 |
| rounds_since_last_discover | 3 | 4 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 193 | 194 |
| last_updated_round | 257 | 258 |

## 遗留问题

1. **event 页数 33**：本轮 +1（UC 第二 event，UC 三事件已建 firedamp/flood 二）。queue(event) 1→**0**（建序 16-18 全数消费）。registry 全库 **1508**，unknown 0。
2. **下轮 R258 = SCN28-zombie（event discover 第 5 轮）**：queue(event)==0 → §3(4) 触发。
   须从未覆盖作品播 ≥3 net-new event 候选（Steam House、WC Waif of the Cynthia、Green Ray、Kéraban、Tribulations of a Chinaman、
   Mathias Sandorf、Clipper of the Clouds 之外未建作品等 18+ 部零/低 event 覆盖作品）。
   **note**：UC 仍余 UC-005「神秘炸柱破坏悬疑」可考（但单指素材偏薄，播种前须核 ≥5 distinct 可达性）。
3. **消歧方法论沉淀（R256 起）**：event discover 播种「同名灾种」须核锚点章实指；UC 一书三事件（UC-005 炸柱 / UC-016 淹没 / UC-018 firedamp）勿混。
4. **event PN 回填债（R244/R255 EVV5 记录）**：13/33 早期页 <5 PN，DEFERRED。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **corpus-discover 顺延**：since_corpus=193→194（dead 变量）。
7. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
8. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
