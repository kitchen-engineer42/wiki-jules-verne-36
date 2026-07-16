---
round: 82
date: 2026-07-15
type_round: 53
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - auckland
  - shanghai
  - singapore
  - allahabad
  - benares
result: accept
---

# GROW 2.1-B · R82 · NEW1 · place — 建 5 新页（standard 档，SC/AWED 环球航线港群）

## 本轮公告

**R82 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选 / queue 14→9**

R81（NEW1 建 5 + 撤 1 重复页）后 since_evv5=9、since_discover=2、discover_streak_low=0、queue(place)=14、since_corpus=18。

> **⚠ 前轮 forecast 修正（off-by-one）**：R80、R81 日志均预告「R82 = EVV5」，实为**误算**。
> 六步在轮末施加、决策矩阵在轮首读上一轮末计数：R80 末 since_evv5=8 → R81 末=9 → **R82 首读=9<10**，
> EVV5 不触发。EVV5 实际在 **R83** 触发（R82 末 since_evv5→10，R83 首读=10≥10 → 优先级 1b）。
> 本轮按实际计数落 NEW1，不受错误 forecast 影响。

决策矩阵：since_evv5=9<10 → EVV5 系不触发；discover_streak_low=0<3 → CLOSE 不触发；
queue=14≥10 且 since_discover=2<10 → SCN28 不触发；since_corpus=18<30 → 非 corpus；落 NEW1。
建 5 新页，消费「环球航线港群」头部：**Auckland**（SC 新西兰港/37°线）+ **Shanghai**（AWED 太平洋邮轮始发港）+
**Singapore**（AWED 加煤港/电报站）+ **Allahabad**（AWED 铁路缺口/大象接驳）+ **Benares**（AWED 恒河圣城站）。
五页均单源、页内引注 5 全达门。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=9 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =9 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=14≥10, since_discover=2 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =18 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=14 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|-----------------|---------------------------|------|
| auckland | In Search of the Castaways (SC) | — | 5 | real / New Zealand | accept |
| shanghai | Around the World in Eighty Days (AWED) | — | 5 | real / China | accept |
| singapore | Around the World in Eighty Days (AWED) | — | 5 | real / Singapore | accept |
| allahabad | Around the World in Eighty Days (AWED) | — | 5 | real / India | accept |
| benares | Around the World in Eighty Days (AWED) | — | 5 | real / India | accept |

> **续 R50 页内引注门**：五新页页内 `(VVV-NNN-PPP)` 去重 =5/5/5/5/5 全达门。
> **AWED 印度铁路轴**：Allahabad（GIP 50 英里缺口）+ Benares（恒河圣城/Cromarty 离队），
> 与既建 Bombay/Calcutta 连成 Fogg 印度横穿链。
> **散文门五页全 ≤400**（add 前分段核验，无微调即通过）。
> **无 alias**：五页 Verne 原文即用现名，无 modern alias。
> **forward-link 门**：auckland 原引 [[Lord Glenarvan]]/[[Jacques Paganel]]（仅章节页无人物页），
> add 前改纯文本；benares [[Allahabad]] 为本轮同批建页，链接即时生效（续避红链惯例）。

## 命名与互链

- **命名**：auckland / shanghai / singapore / allahabad / benares——均 real。
- **互链**：
  Auckland ⇄ [[In Search of the Castaways]]（Macquarie/37°线，人物纯文本）；
  Shanghai ⇄ [[Around the World in Eighty Days]]/[[Yokohama]]/[[Phileas Fogg]]；
  Singapore ⇄ [[Around the World in Eighty Days]]/[[Hong Kong]]/[[Fix]]；
  Allahabad ⇄ [[Around the World in Eighty Days]]/[[Phileas Fogg]]（Kholby 大象接驳）；
  Benares ⇄ [[Around the World in Eighty Days]]/[[Allahabad]]/[[Phileas Fogg]]。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{SC,AWED}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页 add 前分段核验通过（无微调）。建后就地复核页面文件
`grep -oE '\([A-Za-z0-9]+-[0-9]+-[0-9]+\)' | sort -u | wc -l` = 5/5/5/5/5，全达门。Connections 节 wikilink 不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index（逐条 grep 核）；页内引注 distinctPN 逐页核 5/5/5/5/5 |
| G2 散文门 ≤400 | PASS | 五新页 add 前分段，全 PASS 无微调 |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；无新 alias；registry 仅 Robur 旧账 PARK（Tsalal 冲突 R81 已清）|
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选（14→9）；grow_state NEW1 six-step；registry 1262→1267，unknown 0 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 82→83`；`type_round 53→54`；`rounds_since_last_evv5 9→10`；
`rounds_since_last_discover 2→3`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 18→19`；`last_updated_round→83`。

## 遗留问题

1. **place 页数 194→199**：本轮 +5；registry 全库 1262→1267，unknown 0。
2. **queue(place) 9<10**：14 − R82 消费 5 = 9（Lake Ontario/Black Sea/North Sea/Long Island/Bay of Bengal/
   Cape Bon/Kara Sea 跨源或 hold + Ega/Zabediero 两单源）。**已跌破 discover 阈值 10**。
3. **下轮 R83 = EVV5（优先级 1b）**：R82 末 since_evv5→10，R83 首读=10≥10 → EVV5 触发；
   since_discover=3<10 → 1a 不触发，落单 EVV5（非建页质量审计轮：EVV5 six-step since_evv5 RESET 0、
   since_discover +=1；仅 G4 门；模板稳定则日志「无需更新」，仅 stage 日志+housekeeping+state）。
4. **R84 预判 = SCN28 discover**：R83 EVV5 后 queue 仍 9<10 → 优先级 3 SCN28 触发补种。
   届时须精核 hold 候选（North Sea/Cape Bon 跨源建页、Kara Sea 精扫、Bay of Bengal 核 RM 误配、
   Long Island 里海 Uzun Ada 异地同名剔除）+ 新裸词/河港轴补种。
5. **HK-R78-tsalal-dup 后续**：建议 R84 discover 轮附带补核 R77 建的 5 页（nijni-novgorod/bombay/
   melbourne/lima/gibraltar）是否另有既有重复页；本轮 R82 五港建前已交叉核 pages.json，均无既有页。
6. **两 hold + 跨源候选照旧**：Lake Ontario（agg 7 但单作 MW:4<5）、Black Sea（跨源过散）、
   North Sea/Cape Bon（跨源待建）、Long Island/Bay of Bengal（降级 hold）、Kara Sea（建前须精扫）。
7. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50/R61 PARK。
8. **debt 照旧 PARK/记录**：HK-book-colon-yaml-break、HK-surface-discover-pattern-undercount、
   featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报。
