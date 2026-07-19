---
round: 274
date: 2026-07-18
type_round: 41
phase: "2.1"
current_type: event
gene: NEW1
pages: [the-madman-in-the-balloon]
result: success
---

# GROW 2.1-B · R274 · NEW1 · event — 建 The Madman in the Balloon（气球升空遇疯客、割吊篮索、攀网自救、锚索钩地得生，DA）

## 执行摘要

Phase 2.1-B event 类型第 30 建（type_round 41），消费 R271 discover 队列**建序 30（末位）**。决策机 §3 首匹配 **NEW1**
（since_evv5=7<10；streak=0<3；since_discover=2<10、全局 queue≥10；queue(event)=1>0 → §3(4) 否；stub%=0 → §3(7)）。

**The Madman in the Balloon**（DA 首 event）。叙事者气球升空，一陌生人藏身篮中，渐露疯癫本相、狂列历代飞行家之死、
执意同赴死；宣「时辰已到，我等必死」、欲割吊篮索弃篮于空；叙事者绝望搏斗被制、疯客割断吊篮索，
篮坠而叙事者攀入网眼；暴风驱球向海、锚索钩地令其松手坠落，得生于荷兰田野，醒于 Harderwick 农舍。

**锚核（本轮无精修）**：R271 队列记 pn_anchor=**DA-001**，逐句核该单章确为升空-疯客掀祸-脱险全程所在
（识破疯客 159 → 疯客起立 200 → 「必死」宣言 201 → 「割断这些索」203 → 缠斗-割吊篮索 204 → 篮坠攀网 210 → 锚索钩地生还 215 → 醒于农舍 217），锚 **DA-001** 确认无误、保持。

**单指核**：全 8 PN 单指气球升空-疯客掀祸-脱险这一连续事件（识破→起立→宣言→图弃篮→搏斗割索→篮坠攀网→锚索得生→醒转）。
**排除**：球升技术描写、疯客所列历代飞行家掌故（背景铺陈）、升空初程别线剔除，仅取疯客掀祸-脱险本身之句。
exact-slug the-madman-in-the-balloon ABSENT（变体 balloon-drama-over-holland/the-balloon-drama 亦 ABSENT）。**DA 2-char → 无需 page-top Note**。

**工作页处置**：DA 有 work 页 **[[A Drama in the Air]]**，Overview + Participants 段链回。book=A Drama in the Air、location=Holland。

**恰达门 8 distinct solid PN**（全 DA-001，一章内掀祸-脱险全程）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | DA-001-159 | 再无幻想余地、识破可怖真相——身处疯客之侧（识破）|
| What Happens | DA-001-200 | 高稀空气中见同伴起立于前、意在毁灭（起立）|
| What Happens | DA-001-201 | 「时辰已到！我等必死。为世所弃、所鄙。共毁之！」（宣言）|
| What Happens | DA-001-203 | 「割断这些索！弃篮于空」、妄想球将升向太阳（图弃篮）|
| What Happens | DA-001-204 | 绝望搏斗、被压制、疯客割断吊篮索（搏斗割索）|
| Significance | DA-001-210 | 篮坠入空、本能攀住绳索、拔身入网眼（攀网）|
| Significance | DA-001-215 | 距海二里、暴风驱之、骤震松手、绳滑指间、落于坚土得生（锚索得生）|
| Significance | DA-001-217 | 醒时卧 Harderwick 农舍病榻、距 Amsterdam 十五里（醒转）|

**VVV 处置**：DA 2-char，PN 渲染正常，无需 RFC-0003 Note。
prose-gate awk 首过仅 Participants bullet 块合并误报（三 bullet 各 132/156/160 字，均 <400）。pn_validator --mode strict ✓。

event 计数 44→45，registry total 1519→**1520**，unknown 恒 0。add_page 一次成型（rev ViimPs，size 2487，
quality 自动 featured）。
location=Holland、pn_anchor=DA-001、book=A Drama in the Air、aliases=[The Balloon Drama, The Drama in the Air]。
链 [[A Drama in the Air]]（疯客、叙事者未建 character，散文提及）。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =7 | 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=2<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =1>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| the-madman-in-the-balloon | ViimPs | A Drama in the Air | Holland | DA-001 | 8 distinct | 升空-疯客掀祸-脱险单指（割吊篮索 → 攀网 → 锚索得生）；锚 DA-001 核实无误保持；剔球升技术/历代飞行家掌故别线；DA 2-char 无 Note；链 [[A Drama in the Air]] |

- **the-madman-in-the-balloon**：8 distinct solid PN（全 DA-001，一章内掀祸-脱险全程）；aliases [The Balloon Drama, The Drama in the Air]；event-schema 四 H2。pn_validator --mode strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指疯客掀祸-脱险；球升技术/飞行家掌故/升空初程别线剔除；strict ✓。✔
- **G2 段落 ≤400 字**：散文段首过 0 超段；Participants bullet 各 <400（132/156/160，awk 块合并误报已核）。✔
- **G3 ≥5 distinct PN**：8 solid（全 DA-001），逾门。✔
- **G4 脚本建页**：add_page.py 建，未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；DA 2-char 无需 Note。✔
- **registry 一致**：total 1520 event 45 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug the-madman-in-the-balloon ABSENT；变体 ABSENT；非既有 44 event；无 alias 冲突。✔
- **单指核**：DA-001 掀祸-脱险全程逐句确认；锚核实无误无需精修。✔
- **排除检查**：提交前 grep `butler.json|-schema.md|rfc-vernean` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R275 起始计数）

| 字段 | R274 起始 | R275 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 274 | 275 |
| type_round | 40 | 41 |
| rounds_since_last_evv5 | 7 | 8 |
| rounds_since_last_discover | 2 | 3 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 210 | 211 |
| last_updated_round | 274 | 275 |

## 遗留问题

1. **event 页数 45**：本轮 +1（DA 首 event）。queue(event) 1→**0**（建序 30 消费，R271 三候选全建毕）。registry 全库 **1520**，unknown 0。
2. **下轮 R275 = SCN28-zombie discover（§3(4)）**：queue(event)==0 触发僵尸勘探。
   since_evv5=8<10、streak=0、queue(event)=0 → §3(4) SCN28-zombie。
   零 event 作品仅余 VB（气球题材，备选），AMB/YEAR 判非离散叙事事件；VB 单部或不足 3 候选 → 或需转向**低覆盖作品**（仅 1 event 之作）掘第二事件，或 discover_streak_low 或将 +1（若 new_candidates<3）。
   **注**：next EVV5 约 R277（since_evv5 至 R277 达 10）；若 R275/276 为建页轮则 R277 触发 §3(1b) EVV5。
3. **消歧方法论四例沉淀（R256/R260/R261/R264）**：queue 锚点视为线索非定论，建时逐句复核。已积四例修正 + 七例核实无误（R265/R268/R269/R270/R272/R273/R274）。
4. **event 覆盖 32/36**：本会话 SI+DA 入册（+ 前述 WC/TT/BR/DOSE/WAI/MZ/PL/TN/ASC）。仅余 VB/AMB/YEAR/（及另一部）无 event。
5. **event PN 回填债（R244/R255/R266 EVV5）**：13/45 早期页 <5 PN，DEFERRED，下次 EVV5（约 R277）再审。
6. **散文门债**：37 页 >400（既有 DEFERRED）；本轮页 over-400=0。
7. **corpus-discover 顺延**：since_corpus=210→211（dead 变量）。
8. **EVV6 封存点**：Phase 2.1 关闭前每类型 EVV6 全库评审并回填 closed_types[].evv6_score（四类型皆 null）。
9. **零/低 event 掘矿策略**：R275 zombie 若零 event 作品候选不足 3，转向低覆盖作品（各作品第二 event）以维持 productive；否则接受 streak+1。
10. **featured re-grade DEFERRED**；HK-* 系列债照旧 PARK/记录。
