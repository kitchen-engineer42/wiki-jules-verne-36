---
round: 60
date: 2026-07-15
type_round: 32
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - bay-of-talcahuano
  - easter-island
  - cape-of-good-hope
  - smiths-straits
  - strait-of-gibraltar
result: accept
---

# GROW 2.1-B · R60 · NEW1 · place — 消费 R59 新候选首批 5 页（standard 档）

## 本轮公告

**R60 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选 / queue 21→16**

R59 后 since_evv5=9、since_discover=0、discover_streak_low=0、queue(place)=21。
决策矩阵：queue=21≥10 且 since_discover=0<10 → SCN28 不触发；since_evv5=9<10 → EVV5 不触发；落 NEW1。
消费 R59 广式重扫 19 新候选之首批 5 枚（择叙事最具体者，暂缓通用大洋）：
**Bay of Talcahuano**（SC 智利湾/Duncan 母港）+ **Easter Island**（DSCF 复活节岛）+
**Cape of Good Hope**（TTLU 好望角）+ **Smith's Straits**（ACH Kane 航路）+ **Strait of Gibraltar**（TTLU 直布罗陀）。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=9 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =9 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=21≥10, since_discover=0 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =27 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=21 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|------|-----------------|---------------------------|------|
| bay-of-talcahuano | In Search of the Castaways (SC) | k9olwz | 2321 | 7 | real / Chile (South America) | accept |
| easter-island | Dick Sand (DSCF) | zxBMmw | 2178 | 8 | real / Pacific Ocean | accept |
| cape-of-good-hope | Twenty Thousand Leagues (TTLU) | UPcJXH | 2055 | 6 | real / South Africa | accept |
| smiths-straits | The Adventures of Captain Hatteras (ACH) | T8Rfql | 1896 | 5 | real / Canadian Arctic Archipelago | accept |
| strait-of-gibraltar | Twenty Thousand Leagues (TTLU) | CT9YbA | 2147 | 6 | real / Mediterranean / Atlantic | accept |

> **续 R50 页内引注门**：五页页内 `(VVV-NNN-PPP)` 去重 ≥5——7/8/6/5（贴门）/6 全达门。
> **Easter Island 命名**：label Easter Island（现代通名）/ alias Isle of Pâques（Verne 用名 Isle of Paques）+ Vai-Hon（原住民名）。
> **Smith's Straits 变体**：alias Smith's Strait（单数），承 R59 修正——R57 主式漏计单数形。

## 命名与互链

- **命名**：bay-of-talcahuano（alias Talcahuano）/ easter-island（alias Isle of Pâques,Vai-Hon）/
  cape-of-good-hope / smiths-straits（alias Smith's Strait）/ strait-of-gibraltar（alias Straits of Gibraltar）。
- **互链**：Bay of Talcahuano ⇄ [[In Search of the Castaways]] / [[Cape Horn]] / [[Cape Bernouilli]]；
  Easter Island ⇄ [[Dick Sand: A Captain at Fifteen]]；
  Cape of Good Hope ⇄ [[Twenty Thousand Leagues Under the Sea]] / [[Nautilus]] / [[Cape Horn]]；
  Smith's Straits ⇄ [[The Adventures of Captain Hatteras]] / [[Melville Bay]] / [[Lancaster Strait]]；
  Strait of Gibraltar ⇄ [[Twenty Thousand Leagues Under the Sea]] / [[Nautilus]] / [[Vigo Bay]]。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{SC,DSCF,TTLU,ACH}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页全段分段核验通过（add_page.py 防缩减 + 散文门全 PASS）。Connections 节 wikilink 不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；页内引注 distinctPN 逐页核：7/8/6/5/6 |
| G2 散文门 ≤400 | PASS | add 前分段核验，五页全 PASS |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；含撇号/冒号 description 单引号转义 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选（21→16）；grow_state NEW1 six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 60→61`；`type_round 31→32`；`rounds_since_last_evv5 9→10`；
`rounds_since_last_discover 0→1`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 27→28`；`last_updated_round→61`。

## 遗留问题

1. **place 页数 120→124**：本轮 +5，registry 全库 1189→1194。
2. **queue(place) 16**：21 − R60 消费 5 = 16（14 真候选 + 2 holds）。余真候选含 Indian/Pacific/Atlantic Ocean、
   Antarctic Sea、Washburn Bay、Chatham Islands、Gulf of Mexico、Detroit River、Sandwich Islands、
   Coronation Gulf、Platte River、Caribbean Sea、Blue Ridge Mountains、Shannon Island。
3. **下轮 R61：since_evv5=10 ≥10 → 优先级 1b EVV5 触发**（自 R50 以来首次质量评估轮）。since_discover=1<10 故非 1a。
   EVV5 为质量抽检轮（非建页）：抽样近轮 place 页核 PN grounding/schema/页内引注门，产 EVV5 报告，since_evv5 归 0。
4. **两 hold 候选照旧**：Lake Ontario（主源 MW:4<5）、Black Sea（跨源过散）。
5. **SCN28-corpus 深扫倒计时**：since_corpus=28，距阈值 30 尚 2 轮（~R62/R63）。
6. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50 PARK。
7. **discover 双盲区债务**（R59 升格，记 HK-surface-discover-pattern-undercount）：build 后提 RFC。
8. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 七项债务照旧 PARK/记录。
