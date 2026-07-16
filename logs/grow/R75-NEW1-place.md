---
round: 75
date: 2026-07-15
type_round: 46
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - belem
  - tabatinga
  - yokohama
  - firth-of-clyde
  - goat-island
result: accept
---

# GROW 2.1-B · R75 · NEW1 · place — 建 5 新页（standard 档，首度批量消费跨源候选）

## 本轮公告

**R75 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选 / queue 12→7**

R74 后 since_evv5=2、since_discover=1、discover_streak_low=0、queue(place)=12、since_corpus=11。
决策矩阵：since_evv5=2<10 → EVV5 系不触发；discover_streak_low=0<3 → CLOSE 不触发；
queue=12≥10 且 since_discover=1<10 → SCN28 不触发；since_corpus=11<30 → 非 corpus；落 NEW1。
建 5 新页：3 单作强候选 **Belem**（EHLA 亚马逊河口城/jangada 终点）+ **Tabatinga**（EHLA 巴西边境首镇）+
**Yokohama**（AWED 日本港/Fogg 太平洋登船地）；首度批量建 2 跨源候选 **Firth of Clyde**（SC+UC=6）+
**Goat Island**（MW+RC=6）——页内引注跨作聚合达门。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=2 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =2 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=12≥10, since_discover=1 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =11 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=12 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|-----------------|---------------------------|------|
| belem | Eight Hundred Leagues on the Amazon (EHLA) | 4RMi1h | 8 | real / Pará (Brazil) | accept |
| tabatinga | Eight Hundred Leagues on the Amazon (EHLA) | uDOWJs | 8 | real / Amazonas (Brazil) | accept |
| yokohama | Around the World in Eighty Days (AWED) | 8xOdsa | 7 | real / Japan | accept |
| firth-of-clyde | In Search of the Castaways (SC) +UC | SO3uY4 | 6 | real / Scotland | accept |
| goat-island | The Master of the World (MW) +RC | Dv9GUK | 6 | real / New York (United States) | accept |

> **续 R50 页内引注门**：五页页内 `(VVV-NNN-PPP)` 去重 ≥5——8/8/7/6/6 全达门。
> **跨源建页首度批量**：Firth of Clyde 页内引注跨 SC（4）+ UC（2）=6；Goat Island 跨 MW（4）+ RC（2）=6。
> 二者单作 max=4<5，但跨作聚合达门，且各作命中均确为同一 real 地物（词边界逐句核）——依 R59 起「跨源建页」惯例建。
> **book 字段取主源**：Firth of Clyde=In Search of the Castaways（SC 主，Duncan 试航）；
> Goat Island=The Master of the World（MW 主，narrator 被卷向瀑布）。
> **alias**：belem→Para（帕拉州名/旧称）；余四页无 modern alias。
> **散文门五页全 ≤400**（add 前分段核验，无一超 400）。

## 命名与互链

- **命名**：belem（alias Para）/ tabatinga / yokohama / firth-of-clyde / goat-island——均 real。
- **互链**：
  Belem ⇄ [[Eight Hundred Leagues on the Amazon]]/[[Manaos]]/[[Iquitos]]/[[Tabatinga]]；
  Tabatinga ⇄ [[Eight Hundred Leagues on the Amazon]]/[[Iquitos]]/[[Manaos]]/[[Belem]]；
  Yokohama ⇄ [[Around the World in Eighty Days]]/[[San Francisco]]/[[London]]；
  Firth of Clyde ⇄ [[In Search of the Castaways]]/[[The Underground City]]；
  Goat Island ⇄ [[The Master of the World]]/[[Robur the Conqueror]]/[[Buffalo]]。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{EHLA,AWED,SC,UC,MW,RC}-*.jsonl`，段级 PN 为 sid 前三段。
散文门 ≤400：五页 add 前分段核验通过。建后就地复核页面文件
`grep -oE '\([A-Za-z0-9]+-[0-9]+-[0-9]+\)' | sort -u | wc -l` = 8/8/7/6/6，全达门。Connections 节 wikilink 不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；页内引注 distinctPN 逐页核：8/8/7/6/6 |
| G2 散文门 ≤400 | PASS | 五新页 add 前分段，全 PASS |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；belem 有 alias（Para）|
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选（12→7）+ Long Island/Bay of Bengal 降级 hold；grow_state NEW1 six-step；registry 1238→1243，unknown 0；无新 alias 冲突 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 75→76`；`type_round 46→47`；`rounds_since_last_evv5 2→3`；
`rounds_since_last_discover 1→2`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 11→12`；`last_updated_round→76`。

## 遗留问题

1. **place 页数 170→175**：本轮 +5，registry 全库 1238→1243，unknown 0。
2. **queue(place) 7<10**：12 − R75 消费 5 = 7（含 2 holds Lake Ontario/Black Sea + North Sea/Cape Bon
   跨源 + Kara Sea 待精扫 + 新降级 Long Island/Bay of Bengal 二 hold）。R73 补种 8 已消费 5，余
   Belem/Tabatinga/Yokohama 亦本轮消费——R73 批已全清。
3. **下轮 R76 = SCN28（优先级 3）**：since_evv5=3<10、queue=7<10、since_discover=2<10、since_corpus=12<30
   → 优先级 3 SCN28 触发（表层复扫补种）。单作强候选渐稀，R76 或重点转向跨源精核（North Sea/Cape Bon 已在队，
   另核 Bay of Bengal/Long Island 真 distinctPN）+ 剩余零散镇名（MS Nijni-Udinsk 复核、EHLA/ASC 河港）。
4. **Long Island / Bay of Bengal 降级 hold（本轮复核）**：ASC「Long Island」实为里海 Uzun Ada 译名（异地同名），
   纽约长岛真 distinctPN=TTLU:3+AWED:1=4<门；Bay of Bengal RM:1 疑子串误配，确 distinctPN 或仅 4。均 hold 待精核。
5. **两 hold 照旧**：Lake Ontario（MW:4<5）、Black Sea（跨源过散）；Kara Sea 建前须精扫。
6. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50/R61 PARK。
7. **debt 照旧 PARK/记录**：HK-book-colon-yaml-break、HK-surface-discover-pattern-undercount、
   featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报。
