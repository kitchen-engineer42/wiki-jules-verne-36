---
round: 74
date: 2026-07-15
type_round: 45
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - semipolatinsk
  - tobolsk
  - kolyvan
  - ichim
  - baraba
result: accept
---

# GROW 2.1-B · R74 · NEW1 · place — 建 5 新页（standard 档）

## 本轮公告

**R74 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选 / queue 17→12**

R73（SCN28 discover）后 since_evv5=1、since_discover=0、discover_streak_low=0、queue(place)=17、since_corpus=10。
决策矩阵：since_evv5=1<10 → EVV5 系不触发；discover_streak_low=0<3 → CLOSE 不触发；
queue=17≥10 且 since_discover=0<10 → SCN28 不触发；since_corpus=10<30 → SCN28-corpus 不触发；落 NEW1。
建 5 新页（消费 R73 补种的 MS 西伯利亚城镇群）：**Semipolatinsk**（伊尔蒂什河畔军政镇）+
**Tobolsk**（西西伯利亚政府）+ **Kolyvan**（电报线镇/Michael 被俘地）+ **Ichim**（驿站镇）+
**Baraba**（Obi/Irtych 间沼泽 steppe）。五页均与既建 Irkutsk/Omsk/Tomsk 同源（MS 西伯利亚驿路），Connections 互链。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=1 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =1 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=17≥10, since_discover=0 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =10 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=17 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|-----------------|---------------------------|------|
| semipolatinsk | Michael Strogoff (MS) | KP2OU0 | 5 | real / Siberia (Irtish valley) | accept |
| tobolsk | Michael Strogoff (MS) | FU9QBq | 7 | real / Western Siberia | accept |
| kolyvan | Michael Strogoff (MS) | SsyuOj | 8 | real / Western Siberia | accept |
| ichim | Michael Strogoff (MS) | 8LYuvp | 7 | real / Western Siberia | accept |
| baraba | Michael Strogoff (MS) | CSm5sl | 7 | real / Western Siberia | accept |

> **续 R50 页内引注门**：五页页内 `(VVV-NNN-PPP)` 去重 ≥5——5/7/8/7/7 全达门。
> **Semipolatinsk 恰达门**：MS 全语料仅 5 段命名 Semipolatinsk（MS-002-021/003-061/003-065/009-030/012-075），
> 五段全引，distinctPN=5=门；今属哈萨克斯坦（Semey），label 从 Verne 原文旧称，region 记 Siberia (Irtish valley)。
> **alias**：baraba→Baraba Steppe（区域别名）；余四页 Verne 原文即用该名，无 modern alias。
> **Ichim=Ishim（伊希姆）**：label 从原文；页内采 MS-013 驿路段群（Ekaterenburg-Irkutsk 路四百二十英里处驿站镇），
> 未采「Ogareff 鞭击」情节（该情节非本页 5 引注所需）。
> **散文门五页全 ≤400**（add 前分段核验，无一超 400）。

## 命名与互链

- **命名**：semipolatinsk / tobolsk / kolyvan / ichim（alias 无）/ baraba（alias Baraba Steppe）——均 real。
- **互链**：五页 Connections 互引 + 链既建同源镇——
  Semipolatinsk ⇄ [[Michael Strogoff]]/[[Omsk]]/[[Tobolsk]]/[[Irkutsk]]；
  Tobolsk ⇄ [[Michael Strogoff]]/[[Omsk]]/[[Tomsk]]/[[Irkutsk]]；
  Kolyvan ⇄ [[Michael Strogoff]]/[[Tomsk]]/[[Omsk]]/[[Irkutsk]]；
  Ichim ⇄ [[Michael Strogoff]]/[[Omsk]]/[[Tomsk]]/[[Irkutsk]]；
  Baraba ⇄ [[Michael Strogoff]]/[[Kolyvan]]/[[Omsk]]/[[Tomsk]]。

## PN 接地核验

正文句 PN 自 `data/sentence_index/MS-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页 add 前分段核验通过。Connections 节 wikilink 不强制 PN。建后就地复核页面文件
`grep -oE '\([A-Za-z0-9]+-[0-9]+-[0-9]+\)' | sort -u | wc -l` = 5/7/8/7/7，全达门。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；页内引注 distinctPN 逐页核：5/7/8/7/7 |
| G2 散文门 ≤400 | PASS | 五新页 add 前分段，全 PASS |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；baraba 有 alias |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选（17→12）；grow_state NEW1 six-step；registry 1233→1238，unknown 0；无新 alias 冲突（Robur 旧账 PARK）|
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 74→75`；`type_round 45→46`；`rounds_since_last_evv5 1→2`；
`rounds_since_last_discover 0→1`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 10→11`；`last_updated_round→75`。

## 遗留问题

1. **place 页数 165→170**：本轮 +5，registry 全库 1233→1238，unknown 0。
2. **queue(place) 12≥10**：17 − R74 消费 5 = 12（含 3 R73 剩余 Belem/Tabatinga/Yokohama + 2 holds
   Lake Ontario/Black Sea + Kara Sea 待精扫 + 6 跨源候选 North Sea/Firth of Clyde/Long Island/
   Goat Island/Bay of Bengal/Cape Bon）。
3. **下轮 R75 = NEW1**：queue=12≥10、since_evv5=2<10、since_discover=1<10、since_corpus=11<30
   → 优先级 6 NEW1 建 5 页。优先消费 R73 剩余 Belem/Tabatinga/Yokohama + 跨源候选。
4. **单作强候选渐稀**：R73 已扫至 MS/EHLA/AWED 次级城镇；剩余单作强候选有限，后续或转向跨源精核。
5. **两 hold 照旧**：Lake Ontario（MW:4<5）、Black Sea（跨源过散）；Kara Sea 建前须精扫。
6. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50/R61 PARK。
7. **debt 照旧 PARK/记录**：HK-book-colon-yaml-break、HK-surface-discover-pattern-undercount、
   featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报。
