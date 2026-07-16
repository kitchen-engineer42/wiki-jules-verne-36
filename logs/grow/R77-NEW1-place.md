---
round: 77
date: 2026-07-15
type_round: 48
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - nijni-novgorod
  - bombay
  - melbourne
  - lima
  - gibraltar
result: accept
---

# GROW 2.1-B · R77 · NEW1 · place — 建 5 新页（standard 档，消费 R76 城市候选）

## 本轮公告

**R77 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选 / queue 19→14**

R76（SCN28 discover 补种 12）后 since_evv5=4、since_discover=0、discover_streak_low=0、queue(place)=19、since_corpus=13。
决策矩阵：since_evv5=4<10 → EVV5 系不触发；discover_streak_low=0<3 → CLOSE 不触发；
queue=19≥10 且 since_discover=0<10 → SCN28 不触发；since_corpus=13<30 → 非 corpus；落 NEW1。
建 5 新页，消费 R76 补种城市候选头部 5 强候选：**Nijni-Novgorod**（MS Volga 集市城/Michael 启程地）+
**Bombay**（AWED 印度登陆港）+ **Melbourne**（SC 澳洲段主港）+ **Lima**（PL 舞台城）+
**Gibraltar**（OC 彗星残片）。五页均单作 distinctPN ≥36，页内引注 5–7 全达门。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=4 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =4 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=19≥10, since_discover=0 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =13 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=19 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|-----------------|---------------------------|------|
| nijni-novgorod | Michael Strogoff (MS) | wbkzp8 | 7 | real / Russia (Volga) | accept |
| bombay | Around the World in Eighty Days (AWED) | X4VjfN | 6 | real / India | accept |
| melbourne | In Search of the Castaways (SC) | BlNOir | 6 | real / Australia (Victoria) | accept |
| lima | The Pearl of Lima (PL) | kEohlq | 6 | real / Peru | accept |
| gibraltar | Off on a Comet (OC) | wU2WSt | 5 | real / Strait of Gibraltar | accept |

> **续 R50 页内引注门**：五页页内 `(VVV-NNN-PPP)` 去重 ≥5——7/6/6/6/5 全达门。
> **首度大城市批量**：五页均单作强候选（MS:47/AWED:50/SC:51/PL:36/OC:38），非跨源——R76 裸词扫描
> 揭示的主要城市 runway。
> **Gibraltar real 判定**：直布罗陀为 real 地物；OC（Off on a Comet）情节中被彗星 Gallia 掠为残片，
> 但地物本身 real → real_or_fictional=real，region Strait of Gibraltar。
> **散文门五页全 ≤400**（add 前分段核验，Gibraltar 一段 425 拆分后通过）。
> **alias**：五页均无 modern alias（Verne 原文即用现名）。

## 命名与互链

- **命名**：nijni-novgorod / bombay / melbourne / lima / gibraltar——均 real。
- **互链**：
  Nijni-Novgorod ⇄ [[Michael Strogoff]]/[[Ichim]]/[[Omsk]]/[[Tomsk]]/[[Irkutsk]]；
  Bombay ⇄ [[Around the World in Eighty Days]]/[[Allahabad]]/[[Calcutta]]/[[Yokohama]]/[[Hong Kong]]；
  Melbourne ⇄ [[In Search of the Castaways]]/[[Firth of Clyde]]；
  Lima ⇄ [[The Pearl of Lima]]；
  Gibraltar ⇄ [[Off on a Comet]]/[[Cape Bon]]。

> **前向链**：Bombay 链 [[Allahabad]]/[[Calcutta]]（R76 候选，待 R78+ 建）；Gibraltar 链 [[Cape Bon]]（queue 跨源候选）。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{MS,AWED,SC,PL,OC}-*.jsonl`，段级 PN 为 sid 前三段。
散文门 ≤400：五页 add 前分段核验通过（Gibraltar 拆一段）。建后就地复核页面文件
`grep -oE '\([A-Za-z0-9]+-[0-9]+-[0-9]+\)' | sort -u | wc -l` = 7/6/6/6/5，全达门。Connections 节 wikilink 不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；页内引注 distinctPN 逐页核：7/6/6/6/5 |
| G2 散文门 ≤400 | PASS | 五新页 add 前分段，Gibraltar 425 段拆分后全 PASS |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；无 alias 冲突（新增） |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选（19→14）；grow_state NEW1 six-step；registry 1243→1248，unknown 0（仅 Robur alias 旧账 PARK）|
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 77→78`；`type_round 48→49`；`rounds_since_last_evv5 4→5`；
`rounds_since_last_discover 0→1`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 13→14`；`last_updated_round→78`。

## 遗留问题

1. **place 页数 175→180**：本轮 +5，registry 全库 1243→1248，unknown 0。
2. **queue(place) 14≥10**：19 − R77 消费 5 = 14（含 R76 剩余 7：Morganton/Tijuco/Kilimanjaro/Tsalal/
   Calcutta/Allahabad/Benares + 既有 7：Lake Ontario/Black Sea/North Sea/Cape Bon/Kara Sea +
   Long Island/Bay of Bengal 两 hold）。
3. **下轮 R78 = NEW1**：queue=14≥10、since_evv5=5<10、since_discover=1<10、since_corpus=14<30
   → 优先级 6 NEW1 建 5 页。优先消费 R76 剩余城市候选（Morganton/Tijuco/Kilimanjaro/Tsalal/Calcutta）。
4. **EVV5 将于 R82 触发**（since_evv5 R77 后=5，R82 达 10）。
5. **place runway 充足**：R76 已证枯竭错觉证伪；剩余 7 R76 候选 + 印度次城（Allahabad/Benares）
   + 后续裸词扫描仍有余量。
6. **两 hold + 跨源候选照旧**：Lake Ontario（MW:4<5）、Black Sea（跨源过散）、North Sea/Cape Bon
   （跨源待建）、Long Island/Bay of Bengal（降级 hold）、Kara Sea（建前须精扫）。
7. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50/R61 PARK。
8. **debt 照旧 PARK/记录**：HK-book-colon-yaml-break、HK-surface-discover-pattern-undercount、
   featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报。
