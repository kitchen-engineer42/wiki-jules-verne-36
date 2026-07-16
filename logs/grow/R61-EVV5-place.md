---
round: 61
date: 2026-07-15
type_round: 33
phase: "2.1"
current_type: place
gene: EVV5
new_candidates: 0
pages: []
result: schema-stable-with-backfill
---

# GROW 2.1-B · R61 · EVV5 · place — 质量抽检轮（自 R50 以来首次）

## 本轮公告

**R61 — Phase 2.1 — EVV5 — place — 质量评估轮 / 0 建页 / 1 反哺（hudsons-bay 4→5）/ since_evv5 归 0**

R60 后 since_evv5=10、since_discover=1、discover_streak_low=0、queue(place)=16。
决策矩阵：since_evv5=10≥10 → **优先级 1b EVV5 触发**（since_discover=1<10 故非 1a EVV5+SCN28）。
EVV5 为质量抽检轮（非建页）：全库 place 页五维反射扫描 + 反哺缺陷页 + 产报告，since_evv5 归 0。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=10, since_discover=1 | 否 |
| **1b** | **EVV5（since_evv5 ≥ 10）** | **=10** | **触发** |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=16≥10, since_discover=1 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =28 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=16 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| NEW1（默认）| — | 被 1b 抢占 | 否 |

## 五维反射扫描（全库 place）

扫描全部 `type: place` 页（126 文件命中；pages.json place 计 124，差 2 见遗留②），五维核验：

| 维度 | 结果 | 判定 |
|------|------|------|
| D1 H2 结构（Overview / In the Narrative / Geography & Features / Connections）| 4 H2 齐备，不合规 0 | PASS |
| D2 页内 distinctPN（standard 档 ≥5）| min 4 / max 14 / median 7 | 3 页 <5，见下 |
| D3 散文段 ≤400 | 全库 PASS（本轮反哺触发 add_page.py 旁路遗产：见下）| PASS |
| D4 wikilink 数 | 8 页零 wikilink（均 schema 允许，Connections 可为空）| PASS |
| D5 类型专属字段（book / real_or_fictional / region）| 缺失 0，100% 齐备 | PASS |

### D2 页内引注门 <5 的三页

| slug | distinctPN | 来源 | 处置 |
|------|-----------|------|------|
| hudsons-bay | 4→**5** | GROW R56 建页缺陷 | **本轮反哺**（见下）|
| snaefellsjokull | 4 | Pilot 页（BIRTH 期）| PARK（承 R39/R50）|
| hong-kong | 4 | Pilot 页（BIRTH 期）| PARK（承 R39/R50）|

## hudsons-bay 反哺记录（GROW 建页缺陷修正）

**缺陷根因**：R56 建页日志声称 hudsons-bay 页内引注「5（贴门）」，实为 **4 distinct**——
`FC-004-002` 在 Overview 与 Geography 两处重复引用，去重后仅 FC-004-002 / ACH-017-015 / ACH-017-014 / ACH-004-016 四枚。
R56 日志误将「引注次数 5」记为「distinctPN 5」。

**反哺动作**：Geography & Features 新增一段，引 `FC-010-019`（The Fur Country 第 10 章，
Samuel Hearne「On November 6, 1769, this agent left Fort Prince of Wales, on the river Churchill,
near the western shores of Hudson's Bay.」——Hudson's Bay 水体义西岸，与既有 4 枚不重复）。

**连带修正（add_page.py 散文门旁路遗产）**：edit_page.py 强制散文门，暴露 R56 经 add_page.py 建页时
未受 ≤400 门约束的 Overview 段（431 字）。本轮同步将 Overview 缩至 <400（删冗余同位语，保 FC-004-002 引与 Chesterfield inlet 引文），
Geography 新引注独立成段。反哺后 rev=VuZZQz，size 2047→2197（+150），**distinctPN 4→5**（防缩减 PASS）。

## PN 接地核验

反哺句 PN 自 `data/sentence_index/FC-*.jsonl`，sid 前三段去重得 distinctPN。
edit_page.py 防缩减 + 散文门全 PASS；registry / backlinks 重建（1194 页 / 1103 被引 2606 条）。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G4 记录完整性 | PASS | 本日志；grow_state EVV5 six-step；hudsons-bay 反哺 rev VuZZQz；queue.md 不动（EVV5 不消费）|

> EVV5 为质量评估轮，仅 G4 出口门（不建页，故 G1–G3 与 I1–I5 不适用于新页）。
> 反哺页 hudsons-bay 经 edit_page.py 全检（PN 有效 / 散文 ≤400 / 防缩减）通过。

## 结论

**place-schema 稳定，无需变更**。五维全 PASS，唯一 GROW 建页缺陷（hudsons-bay 页内引注虚报）已反哺修正。
两 Pilot 页（snaefellsjokull / hong-kong）PN=4 照旧 PARK。承 R50 判定：schema 无结构性问题，广度扩张继续。

## state 更新（EVV5 six-step）

`current_round 61→62`；`type_round 32→33`；`rounds_since_last_evv5 10→0`（本轮归零）；
`rounds_since_last_discover 1→2`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 28→29`；`last_updated_round→62`。

## 遗留问题

1. **R56 建页日志 distinctPN 虚报**（本轮修正）：记 add_page.py 散文门旁路 + 引注次数/distinctPN 混淆双重隐患。
   已反哺 hudsons-bay；根因（add_page.py 不强制散文门 & 建页时未去重核 distinctPN）入债务照旧 PARK。
2. **place 页数 file-glob 126 vs pages.json 124 差 2**：疑 substring 命中非 place 变体（如 `type: place-*` 或注释）。
   非阻塞，记录待 build 后核。
3. **queue(place) 16 不变**：EVV5 不消费候选。余 14 真候选 + 2 holds（Indian/Pacific/Atlantic Ocean、
   Antarctic Sea、Washburn Bay、Chatham Islands、Gulf of Mexico、Detroit River、Sandwich Islands、
   Coronation Gulf、Platte River、Caribbean Sea、Blue Ridge Mountains、Shannon Island）。
4. **下轮 R62：since_evv5=0、since_discover=2、queue=16≥10 → 优先级落 NEW1**（建 5 页，消费 queue 16→11）。
   择叙事最具体者，暂缓通用大洋（Indian/Pacific/Atlantic Ocean 留后批）。
5. **SCN28-corpus 深扫倒计时**：since_corpus=29（R61 后），距阈值 30 尚 1 轮 → **R62 后 since_corpus=30，R63 触发**深扫。
6. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50 PARK，非 GROW 建页，不反哺。
7. **discover 双盲区债务**（HK-surface-discover-pattern-undercount，R59 升格实质缺陷）：build 后提 RFC。
8. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 七项债务照旧 PARK/记录。
