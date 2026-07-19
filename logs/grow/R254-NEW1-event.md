---
round: 254
date: 2026-07-18
type_round: 20
phase: "2.1"
current_type: event
gene: NEW1
pages: [wreck-of-the-dream]
result: success
---

# GROW 2.1-B · R254 · NEW1 · event — 建 The Wreck of the Dream（汽船 Dream 触礁沉没、Godfrey 沦落荒岛，GM）

## 执行摘要

Phase 2.1-B event 类型第 16 建（type_round 20），消费 R253 discover 队列**建序 16**。决策机 §3 首匹配 **NEW1**
（since_evv5=9<10；streak=0<3；since_discover=0<10、全局 queue≥10；queue(event)=3>0 → §3(4) 否；stub=0 → §3(7)）。

**The Wreck of the Dream**（GM 主，首个 GM event）。事件锚定 pn_anchor=**GM-007**（汽船触礁沉没之章）。
gather("wreck"/"struck"/"sinking"/"cable"/"route"/"catastrophe"/"whirlpool" GM-007→008、GM-022）。逐句核**单指该沉船事件**：
迷雾中 Dream 触暗礁、进水沉没，Turcott 令弃船，Godfrey 与 Tartlet 泅上荒礁——单一海难事件。
**排除**：岛上后续（火/野人/洪水等）属别事件，剔除；岛上生活泛述剔除。
**staged 反转纳入 Significance**：GM-022-022 揭 Kolderup 密令水压沉船、待二人登陆后打捞驶离——同一沉船事件之真相，非别事件。
exact-slug wreck-of-the-dream ABSENT（变体 dream-shipwreck/dream-wreck 亦 ABSENT）。**GM 2-char → 无需 page-top Note**。

**恰达门 8 distinct solid PN**（GM×8，四节分配；跨 GM-007/008/022 三章）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | GM-008-004 | Godfrey 荒礁过夜、推知沉船发生于新月高潮（时空定位）|
| What Happens | GM-007-095 | "We are sinking!" 甲板惊呼、Godfrey 冲出舱（灾变起）|
| What Happens | GM-007-101 | Dream 触礁、水漫甲板、明显下沉（触礁核心）|
| What Happens | GM-007-104 | Turcott 令弃船、距岸仅半链（弃船）|
| What Happens | GM-008-005 | Dream 前数日风暴中偏离航线（成因）|
| Significance | GM-008-006 | Turcott 侦察若彻底本可免难（人祸归因）|
| Significance | GM-008-012 | 疑全员被沉船漩涡卷没（人命代价）|
| Significance | GM-022-022 | Kolderup 揭沉船系水压密令、待登陆后打捞（staged 反转）|

**VVV 处置**：GM 2-char，PN 渲染正常，无需 RFC-0003 Note。
prose-gate awk 首过 0 超段。pn_validator --mode strict ✓（重叠度门全过，无回炉）。

event 计数 30→31，registry total 1505→**1506**，unknown 恒 0。add_page 一次成型（rev kFZQQ2，size 2383，
quality 自动 featured）。
location=Pacific Ocean、pn_anchor=GM-007、book=Godfrey Morgan、aliases=[The Foundering of the Dream]。
链 *[[godfrey-morgan]]*（Godfrey、Tartlet、Turcott、Kolderup 未建 character，散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =9 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=0<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =3>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| wreck-of-the-dream | kFZQQ2 | Godfrey Morgan | Pacific Ocean | GM-007 | 8 | Dream 触礁沉没单指；剔岛上后续别事件；staged 反转纳 Significance；GM 2-char 无 Note |

- **wreck-of-the-dream**：8 distinct solid PN（GM，跨三章 007/008/022，四节分配）；aliases [The Foundering of the Dream]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指 Dream 触礁沉没；岛上后续及泛述剔除；strict ✓。✔
- **G2 段落 ≤400 字**：首过 0 超段。✔
- **G3 ≥5 distinct PN**：8 solid（GM，跨 007/008/022 三 distinct 章、8 distinct 段），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；GM 2-char 无需 Note。✔
- **registry 一致**：total 1506 event 31 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug wreck-of-the-dream ABSENT；变体 dream-shipwreck/dream-wreck ABSENT；非既有 30 event；无 alias 冲突。✔
- **单指核**：GM-007→008、GM-022 逐句确认指同一沉船事件。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R255 起始计数）

| 字段 | R254 起始 | R255 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 254 | 255 |
| type_round | 20 | 21 |
| rounds_since_last_evv5 | 9 | **10（临界）** |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 190 | 191 |
| last_updated_round | 254 | 255 |

## 遗留问题

1. **event 页数 31**：本轮 +1（首个 GM event）。queue(event) 3→2（建序 17-18 待建）。registry 全库 **1506**，unknown 0。
2. **下轮 R255 = EVV5 反思轮（§3(1b)）**：since_evv5=10≥阈值 10 → §3(1b) 触发。
   since_discover=1<10 → 非 §3(1a) EVV5+SCN28，纯 EVV5。event 模板评审 + PN 回填债审视（13/23 早期页 <5 PN）。
   **注**：EVV5 为反思轮，不建页；轮末 since_evv5 reset=0。建序 17-18 顺延至 R256 起。
3. **建序 17-18 待建**：new-aberfoyle-explosion（UC-005 瓦斯爆炸）、new-aberfoyle-flood（UC-016 矿井淹没），R256 起 NEW1 消费。
4. **event PN 回填债（R244 EVV5 记录）**：13/23 早期页 <5 PN，DEFERRED，R255 EVV5 可再审。
5. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
6. **corpus-discover 顺延**：since_corpus=190→191（dead 变量）。
7. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
8. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
