---
round: 234
date: 2026-07-18
type_round: 0
phase: "2.1"
current_type: event
gene: NEW1
pages: [south-pole-attained]
result: success
---

# GROW 2.1-B · R234 · NEW1 · event — 建 South Pole Attained（Nemo 抵南极点植旗，TTLU；event 类型首建）

## 执行摘要

Phase 2.1-B **event 类型首轮建页**（type_round 0）。R233 CLOSE place→event 后 current_type=event、
type_queue=[character]、queue(event)=4（R233 播种 4 候选）。决策机 §3 首匹配 **NEW1**
（since_evv5=0<10；streak=0<3；since_discover=0<10、全局 queue≥10；queue(event)=4>0 → §3(4) 否；
stub=0 → §3(7) 默认 NEW1）。

取 R233 event 队列**建序 1** **South Pole Attained**（TTLU 主）。**event 建页新方法论**（非 toponym，
以 pn_anchor 锚定）首次落地：先 gather 事件核心（"South Pole" distinctPN=35，TTLU 独占 18），
定 pn_anchor=**TTLU-038**（第 38 章南极点抵达章）。逐句核**单指该事件**（Nemo 驾 Nautilus 抵地理南极点、
1868-03-21 植旗宣示），剔他作泛指南极（AM/RM/RC 等 17 PN 皆非本事件）。exact-slug south-pole-attained ABSENT。

**恰达门 9 distinct solid PN**（TTLU×9，四节分配，事件不同侧面）：

| 节 | PN | 侧面 |
|----|-----|------|
| Overview | TTLU-038-094 | Nemo 正式宣示（90°、1868-03-21、claim 1/6 globe）|
| What Happens | TTLU-037-013 | Nautilus 3-16 切入南极圈（起）|
| What Happens | TTLU-037-053 | Nemo 冷答目标为「Antarctic pole」|
| What Happens | TTLU-038-074 | 以 chronometer 定 3-21 正午测点法 |
| What Happens | TTLU-038-091 | 「The South Pole!」测毕惊呼 |
| What Happens | TTLU-038-097 | 展金 N 黑旗（植旗）|
| Significance | TTLU-037-054 | 较北极更不可及、「insane undertaking」（起因张力）|
| Significance | TTLU-042-008 | 后忆「grueling ordeal under the Ice Bank」（代价）|
| Significance | TTLU-045-044 | 后举旗「如南极所植」（呼应终章）|

**4-char VVV 处置**：TTLU 4 字符码，PN 渲染为纯文本（RFC-0003 未决）→ 页顶加 RFC-0003 Note
（同 giant-squid-attack 惯例）。PN data 有效，pn_validator strict ✓。

event 计数 15→16，registry total 1490→1491，unknown 恒 0。add_page 一次成型（rev N6Oncm，size 2923，
quality 自动 featured）。prose-gate awk 初 2 段超（Overview 432 / Significance 483），
拆分后 0 超段。location=South Pole、pn_anchor=TTLU-038、book=Twenty Thousand Leagues Under the Seas、aliases=[Nemo at the South Pole]。
链 [[Captain Nemo]]/[[Nautilus]]/[[Conseil]]/[[Ned Land]]/[[South Pole]]/[[Twenty Thousand Leagues Under the Sea]]。
build_registry 仅 Robur PARK。

## 决策矩阵（NEW1）

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|------|
| 1a/1b | EVV5（since_evv5≥10）| =0（§5.1 复位）| 否 |
| 2 | CLOSE+SCN28（streak≥3）| =0 | 否 |
| 3 | SCN28（queue<10 或 since_discover≥10）| since_discover=0<10；全局 queue≥10 | 否 |
| 4 | SCN28-zombie（queue(event)==0）| =4>0 | 否 |
| 5/6 | RCH2 系（stub%≥15）| =0 | 否 |
| **7** | **NEW1（默认）** | **—** | **触发** |

## 页面处理记录

| slug | rev | book | location | pn_anchor | 页内引注 | 消歧/要点 |
|------|-----|------|----------|-----------|---------|----------|
| south-pole-attained | N6Oncm | Twenty Thousand Leagues Under the Seas | South Pole | TTLU-038 | 9 | Nemo 抵地理南极点植旗；单事件核；4-char VVV → RFC-0003 Note |

- **south-pole-attained**：9 distinct solid PN（TTLU 全用，四节分配）；aliases [Nemo at the South Pole]；event-schema 四 H2（Overview/What Happens/Significance/Participants & Setting）。pn_validator strict ✓。

## EXIT-GATE 检查

- **G1 每句 PN grounding**：全句源自 sentence_index 且单指该事件（Nemo 抵南极点）；泛指南极（AM/RM/RC）已剔；pn_validator strict ✓。✔
- **G2 段落 ≤400 字**：初 2 段超（432/483），拆分后 0 超段。✔
- **G3 ≥5 distinct PN**：9 solid（TTLU），逾门。✔
- **G4 脚本建页**：add_page.py 建（quality 自动 featured），未用 Write/Edit 于 pages/**。✔
- **schema 一致**：event-schema 四 H2；frontmatter 含 book/location/pn_anchor；description 单引号（无冒号但含长句，稳妥）；4-char VVV 加 RFC-0003 Note。✔
- **registry 一致**：total 1491 event 16 unknown 0；仅 Robur PARK。✔
- **查重充分**：exact-slug south-pole-attained ABSENT；非既有 15 event（columbiad-launch/nemo-death/...）。✔
- **单指核**：TTLU ch37-38 逐句确认指同一南极抵达事件（非泛指南极航行）。✔
- **排除检查**：提交前 `git diff --cached --name-only | grep -iE 'butler.json|-schema.md|rfc-vernean'` 须 clean。✔

## 六步状态机（NEW1，grow_state 存 R235 起始计数）

| 字段 | R234 起始 | R235 起始（本轮末写入）|
|------|----------|---------------------|
| current_type | event | event |
| type_queue | [character] | [character] |
| current_round | 234 | 235 |
| type_round | 0 | 1 |
| rounds_since_last_evv5 | 0 | 1 |
| rounds_since_last_discover | 0 | 1 |
| discover_streak_low | 0 | 0 |
| rounds_since_last_corpus_discover | 170 | 171 |
| last_updated_round | 234 | 235 |

## 遗留问题

1. **event 页数 16**：本轮 +1（South Pole Attained）。registry 全库 1491，unknown 0。
   event 队列余 3（建序 2-4）：ice-island-drift（FC）/comet-collision（OC/Gallia）/forward-mutiny（ACH）。
2. **下轮 R235 = NEW1（event）**：建 queue 建序 2 **The Drifting Ice-Island**（FC，半岛断裂成浮冰岛漂流）。
   since_evv5=1<10、streak=0、queue(event)=3>0 → §3(7) NEW1。
3. **event 建页方法论已落地**：pn_anchor 锚定 + 单事件单指核 + 四节侧面分配（起因/经过/意义/参与者）。
   Significance 高重叠风险节：每 PN 系于 verbatim clause（本轮遵）。4-char VVV（TTLU/AWED/ACH）建页须加 RFC-0003 Note。
4. **HK-* 系列继承**：HK-dupcheck-bareterm-vs-slug、exact-slug 复核等 place 阶段教训于 event 继续适用（event slug 亦 kebab）。
5. **散文门债**：37 页 >400（既有 DEFERRED），跨类型延续；本轮页 over-400=0（拆分达标）。
6. **corpus-discover 顺延**：since_corpus=170→171（HK-corpus-discover-not-in-statemachine PARK，dead 变量）。
7. **EVV6 封存点**：Phase 2.1 关闭前须对每类型执行 EVV6 全库评审并回填 closed_types[].evv6_score（现四类型皆 null）。
8. **featured re-grade DEFERRED**：place/event 页 quality 若干 none，full-library re-grade 顺延至 RFC 批审。
9. **debt 照旧 PARK/记录**：HK-queue-size-scope、HK-premature-saturation-claim、HK-compute-quality-fullrun-regrade、
   HK-corpus-discover-not-in-statemachine、HK-addpage-prose-gate-bypass（37 页）、HK-close-override-productive-discover、
   HK-close-accelerated-on-exhaustive-zero、HK-legacy-h1-in-place-pages（150 页）、RFC-0003 VVV 宽度、Robur alias、featured 虚高。
