---
round: 29
date: 2026-07-15
type_round: 1
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - the-chimneys
  - prospect-heights
  - tabor-island
  - cape-bathurst
  - victoria-island
result: accept
---

# GROW 2.1-B · R29 · NEW1 · place — 首批 place NEW1（+5 页，standard 档）

## 本轮公告

**R29 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档**

R28 CLOSE 后 current_type=place，P1 有 12 真新候选（修正后）。本轮 gate 3.9 以下无门触发，
落入 NEW1 默认门，建首批 5 页 place（≤5 standard 批）。选强度最高的两簇同源候选以便互链：
**MI 簇**（the Chimneys / Prospect Heights / Tabor Island）+ **FC 簇**（Cape Bathurst / Victoria Island）。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a/1b | EVV5（since_evv5 ≥ 10）| =0 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| P1 place=12, since_discover=0 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =27 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue(place)=12 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | citations | category/字段 | 判定 |
|------|------|-----|------|-----------|--------------|------|
| the-chimneys | MI(The Mysterious Island)| e1P5df | 2695 | 6 | fictional / Lincoln Island | accept |
| prospect-heights | MI | SxKQ05 | 2489 | 7 | fictional / Lincoln Island | accept |
| tabor-island | MI | stqg4C | 2563 | 6 | fictional / South Pacific | accept |
| cape-bathurst | FC(The Fur Country)| xKv5Vc | 2500 | 6 | real / Arctic North America | accept |
| victoria-island | FC | Id9H0K | 2658 | 7 | fictional / Arctic Ocean | accept |

> **place-schema 遵循**：4 H2（Overview / In the Narrative / Geography & Features / Connections），
> Connections 为纯 wikilink 无需 PN。均 ≥5 PN 引注达 standard 档。`real_or_fictional`：Tabor/Chimneys/
> Prospect Heights/Victoria = fictional（凡尔纳虚构）；Cape Bathurst = real（真实北美地名，凡尔纳借用）。
> **互链**：MI 簇三页互指 Lincoln Island / Granite House；FC 两页互指（Cape Bathurst ⇄ Victoria Island，
> 即「冰岬漂流」核心情节：Fort Hope 建于伪装成岬角的冰floe，1 月 8 日地震断裂漂为 Victoria Island）。

## PN 接地核验

所有正文句 PN 取自 `data/sentence_index/{MI,FC}-*.jsonl`，段级 PN 为 sid 前三段。示例：
Chimneys 命名 MI-004-020；Prospect Heights 命名 MI-011-074；Tabor 坐标 MI-034-116；
Fort Hope 建于冰上 FC-024-003；Victoria Island 漂流速率 FC-025-063。散文门 ≤400：victoria-island
Overview 初稿 423 超限，edit_page.py 拆分后过门（rev Id9H0K）；余 4 页 add 前均已 ≤400。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index，段级三段格式；keyword-overlap warn 非阻塞 |
| G2 散文门 ≤400 | PASS | victoria-island 拆分修正；余页 add 前核验 |
| G3 schema 合规 | PASS | 4 H2 齐备；专属字段 book/real_or_fictional/region 写入 frontmatter |
| G4 记录完整性 | PASS | 本日志；queue.md P1 消费 5 候选；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 29→30`；`type_round 0→1`；`rounds_since_last_evv5 0→1`（gene 无 EVV5）；
`rounds_since_last_discover 0→1`（gene 无 SCN28/CLOSE，非 discover 轮，streak 不变）；
`discover_streak_low` 保持 0；`rounds_since_last_corpus_discover 27→28`；`last_updated_round→30`。

## 遗留问题

1. **R30 = place（P1 余 7 候选）**：Prospect Heights / Cape Bathurst / Victoria Island 已建，P1 余
   Fort Reliance / Aberfoyle / Quiquendone / Fort Providence / New Aberfoyle / Back Cup / Crespo Island。
   下批建议 UC 簇（Aberfoyle / New Aberfoyle 互链地下城）+ FC 簇（Fort Reliance / Fort Providence）。
2. **place discover 未穷尽**：R31+ SCN28 深扫 36 部合集地名（真实地理门槛裁定：Iceland/Baltimore/Tampa
   均既有 Pilot，新真实地名候选待评估）。
3. **the tug / Ebba borderline**：Back Cup（含 Ebba lagoon）建页时回链复议 the tug 是否补建 technology。
4. **registry typefield 未透传**：real_or_fictional/region 未进 pages.json（仅 frontmatter 正确）；
   book 已透传。属既有 PARK 债务，不阻塞。
5. **EVV5 临近**：since_evv5 R30=1，下次 EVV5 在 R38（+10）；place 周期中段触。
6. featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区 六项债务照旧 PARK/记录。
