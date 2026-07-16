---
round: 62
date: 2026-07-15
type_round: 34
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - antarctic-sea
  - washburn-bay
  - chatham-islands
  - detroit-river
  - sandwich-islands
result: accept
---

# GROW 2.1-B · R62 · NEW1 · place — 消费 R59 候选第二批 5 页（standard 档）

## 本轮公告

**R62 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选 / queue 16→11**

R61 后 since_evv5=0、since_discover=2、discover_streak_low=0、queue(place)=16、since_corpus=29。
决策矩阵：since_evv5=0<10 → EVV5 系不触发；queue=16≥10 且 since_discover=2<10 → SCN28 不触发；
since_corpus=29<30 → SCN28-corpus 不触发；落 NEW1。
消费 R59 广式重扫候选第二批 5 枚（择叙事最具体者，暂缓通用大洋 Indian/Pacific/Atlantic Ocean）：
**Antarctic Sea**（AM 南极之海）+ **Washburn Bay**（FC 北极湾）+ **Chatham Islands**（RC Albatross 抛锚）+
**Detroit River**（MW Terror 逃逸孔道）+ **Sandwich Islands**（AM 南桑威奇群岛）。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=0 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =0 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=16≥10, since_discover=2 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =29 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=16 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|------|-----------------|---------------------------|------|
| antarctic-sea | An Antarctic Mystery (AM) | e1kXwj | 1837 | 6 | real / Antarctic / Southern Ocean | accept |
| washburn-bay | The Fur Country (FC) | UY1iGg | 1776 | 5 | real / Canadian Arctic coast | accept |
| chatham-islands | Robur the Conqueror (RC) | 7muKE3 | 1608 | 5 | real / South Pacific (New Zealand) | accept |
| detroit-river | The Master of the World (MW) | 8PubXu | 1881 | 5 | real / United States (Great Lakes) | accept |
| sandwich-islands | An Antarctic Mystery (AM) | EHidZ8 | 1736 | 6 | real / South Atlantic / Southern Ocean | accept |

> **续 R50 页内引注门**：五页页内 `(VVV-NNN-PPP)` 去重 ≥5——6/5/5/5/6 全达门。
> **Sandwich Islands 语义更正**：queue 旧注记「桑威奇群岛（real；夏威夷旧称）」有误。
> AM 语境（Len Guy 南航出发点、Cook 命名、New Georgia/South Orkneys/South Georgia 邻列）确指 Cook 1775 年
> 所命名之**南大西洋南桑威奇群岛**，非夏威夷。本页按南桑威奇群岛建（region South Atlantic / Southern Ocean），
> 已在 queue.md 更正该注。
> **Detroit/Chatham/Washburn 承 R51 误 hold 平反**：三者 R51 曾误列 hold，R59 重扫复核为真候选，本轮建页确认。

## 命名与互链

- **命名**：antarctic-sea（alias Antarctic seas, Southern Seas）/ washburn-bay / chatham-islands（alias Pitt Island）/
  detroit-river / sandwich-islands（alias Sandwich Isles）。
- **互链**：Antarctic Sea ⇄ [[An Antarctic Mystery]] / [[Sandwich Islands]] / [[Halbrane Land]]；
  Washburn Bay ⇄ [[The Fur Country]] / [[Cape Bathurst]] / [[Victoria Island]]；
  Chatham Islands ⇄ [[Robur the Conqueror]] / [[Albatross]] / [[Robur]]；
  Detroit River ⇄ [[The Master of the World]] / [[The Terror]] / [[Lake Erie]]；
  Sandwich Islands ⇄ [[An Antarctic Mystery]] / [[Antarctic Sea]]。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{AM,FC,RC,MW}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页全段分段核验通过（add_page.py 防缩减 + 散文门全 PASS）。Connections 节 wikilink 不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；页内引注 distinctPN 逐页核：6/5/5/5/6 |
| G2 散文门 ≤400 | PASS | add 前分段核验，五页全 PASS |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；含撇号 description 单引号转义 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选（16→11）+ Sandwich 语义更正；grow_state NEW1 six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 62→63`；`type_round 33→34`；`rounds_since_last_evv5 0→1`；
`rounds_since_last_discover 2→3`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 29→30`；`last_updated_round→63`。

## 遗留问题

1. **place 页数 124→129**：本轮 +5，registry 全库 1194→1199。
2. **queue(place) 11**：16 − R62 消费 5 = 11（9 真候选 + 2 holds）。余真候选含 Indian/Pacific/Atlantic Ocean、
   Gulf of Mexico、Coronation Gulf、Platte River、Caribbean Sea、Blue Ridge Mountains、Shannon Island。
3. **下轮 R63：since_corpus=30 ≥30 → 优先级 3.5 SCN28-corpus 触发**（自建 wiki 以来首次深层语料扫描）。
   since_evv5=1<10、queue=11≥10 且 since_discover=3<10，故 1b/3 均不触发；3.5 抢占 NEW1。
   SCN28-corpus 为深扫轮（非建页）：跨全 36 部语料聚合扫描新 place 候选，产候选入 queue，since_corpus 归 0；
   若 new_candidates<3（corpus_new_candidate_min）则 corpus_discover_streak_low+=1。
4. **两 hold 候选照旧**：Lake Ontario（主源 MW:4<5）、Black Sea（跨源过散）。
5. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50/R61 PARK。
6. **discover 双盲区债务**（HK-surface-discover-pattern-undercount，R59 升格实质缺陷）：build 后提 RFC。
7. **featured 虚高、add_page.py 散文门旁路（R61 EVV5 暴露实例）、RFC-0003 VVV 宽度、Robur alias、
   build_wanted 空格滤、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 七项债务照旧 PARK/记录。
