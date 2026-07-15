---
round: 51
date: 2026-07-15
type_round: 22
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - morris-island
  - fort-sumter
  - faroe-islands
  - cape-verde
  - lake-ukereoue
result: accept
---

# GROW 2.1-B · R51 · NEW1 · place — R48 补种第二批 5 页（standard 档，首用 R50 页内引注门）

## 本轮公告

**R51 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选 + 2 hold**

R50 EVV5 后 since_evv5=0、since_discover=2、queue(place)=22，决策矩阵高优先门全否，落 NEW1。
建 R48 SCN28 补种第二批 5 强候选：**Charleston 内战簇 2**（Morris Island / Fort Sumter，BR）+
**北大西洋 1**（Faroe Islands，WC）+ **大西洋群岛 1**（Cape Verde，SC/TTLU）+ **非洲大湖 1**（Lake Ukereoue，FWB）。
本轮首次执行 **R50 新门（GROW-JUDGMENT-R50）**：五页建前逐页核**页内实际引注 distinctPN ≥5**（非仅语料段级）。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=0 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =0 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=22, since_discover=2 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =18 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=22 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | 段级 / 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|------|----------------------|---------------------------|------|
| morris-island | The Blockade Runners (BR)| OaJV6i | 2303 | 段级 10 / 页内 8 | real / United States (Charleston Harbor) | accept |
| fort-sumter | The Blockade Runners (BR)| D0jeAV | 1896 | 段级 8 / 页内 8 | real / United States (Charleston Harbor) | accept |
| faroe-islands | The Waif of the Cynthia (WC)| EToiZ3 | 1642 | 段级 5 / 页内 5 | real / North Atlantic | accept |
| cape-verde | In Search of the Castaways (SC)| jlHiPh | 1892 | 主源 SC:4 + TTLU:3 / 页内 6 | real / Atlantic (off West Africa) | accept |
| lake-ukereoue | Five Weeks in a Balloon (FWB)| MJxCPm | 2114 | 段级 7 / 页内 6 | real / Africa (equatorial lakes) | accept |

> **首用 R50 页内引注门**：五页建前逐页 grep sentence_index 校主源段级，成页后逐页核页内 `(VVV-NNN-PPP)` 引注去重 ≥5——
> morris-island 8、fort-sumter 8、faroe-islands 5（贴门）、cape-verde 6、lake-ukereoue 6，全达门。cape-verde 主源 SC:4 单源 <5，
> 但系真实唯一地物（西非佛得角群岛），跨 TTLU（Atlantis 峰）合法互链，页内引注 6 达门（承 caspian-sea 纳 RC / cape-horn TTLU+SC 跨作先例）。

## 建前主源段级严扫 + 消歧（承聚合校准铁律）

R48 入队多跨源 agg 估值，本轮建前逐页主源段级严扫，两候选净分后 **hold**：

| 候选 | agg | 严扫实况 | 处置 |
|------|-----|---------|------|
| **Sandwich Islands** | 10 | 主源 AM:6 实为「**南三明治群岛**」（Halbrane 南极航路，近 New Georgia/福克兰），**非**队列所标「夏威夷旧称」；夏威夷义散见 SC/GM/MI/SI 各 1（<5）| **hold**：同名双实体，两义净分后均不达门，待清晰消歧 |
| **Norfolk Island** | 10 | MI:4 与 SI:4 系《神秘岛》**同文异版**（Bob Harvey/Speedy 逐句重复，非增量），真实主源段级 4；SC:2 | **hold**：不达 standard ≥5 |

## 命名与互链

- **命名**：morris-island / fort-sumter / faroe-islands（alias Faroe and Shetland Islands）/ lake-ukereoue（Verne 拼写，alias Ukereoue，即维多利亚湖旧称）；
  cape-verde（label Cape Verde / alias Cape Verde Islands·Verde Islands）。均现代规范 label + 语料变体 alias。
- **互链**：Morris Island ⇄ [[The Blockade Runners]] / [[Fort Sumter]]；Fort Sumter ⇄ [[The Blockade Runners]] / [[Morris Island]]（Charleston 内战簇）；
  Faroe Islands ⇄ [[The Waif of the Cynthia]] / [[Canadian General Transportation Company]]（既有 org 页，Cynthia 船东）；
  Cape Verde ⇄ [[In Search of the Castaways]] / [[Twenty Thousand Leagues Under the Seas]]（Atlantis 峰）；
  Lake Ukereoue ⇄ [[Five Weeks in a Balloon]] / [[Lake Tanganyika]] / [[Lake Tchad]]（FWB 非洲大湖簇）。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{BR,WC,SC,TTLU,FWB}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页全段分段核验通过（add_page.py 防缩减 + 散文门全 PASS）。Connections 节 wikilink/纯文本不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；**页内引注 distinctPN ≥5 逐页核**（新门）：8/8/5/6/6 |
| G2 散文门 ≤400 | PASS | add 前分段核验，五页全 PASS |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；含撇号/冒号值单引号转义 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选 + 2 hold（22→15）；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 51→52`；`type_round 22→23`；`rounds_since_last_evv5 0→1`；
`rounds_since_last_discover 2→3`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 18→19`；`last_updated_round→52`。

## 遗留问题

1. **place 页数 92→97**：本轮 +5，registry 全库 1160→1165。
2. **queue(place) 15**：22 − R51 消费 5 − 2 hold = 15。下批优选：
   Cape Verde 已建；余强候选 Lake Ontario(agg 7)/Black Sea(agg 7)/Dream Bay(GM 7)/Altamont Harbour(ACH 6)/Falkland Islands(agg 6)。
   建前逐页主源段级严扫 + 核页内引注 ≥5（R50 门）。
3. **两 hold 候选**：Sandwich Islands（南极/夏威夷同名消歧）、Norfolk Island（MI/SI 同文异版 4<5）。
   若后续深扫可净分某义 ≥5 再评估，否则留 list 提及。
4. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50 PARK，Phase 3 深度轮触及可补引。
5. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 八项债务照旧 PARK/记录。
