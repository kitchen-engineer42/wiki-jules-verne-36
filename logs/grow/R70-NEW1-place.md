---
round: 70
date: 2026-07-15
type_round: 41
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - omsk
  - tomsk
  - pekin
  - london
  - san-francisco
result: accept
---

# GROW 2.1-B · R70 · NEW1 · place — 建 5 新页（standard 档）

## 本轮公告

**R70 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选 / queue 19→14**

R69 后 since_evv5=8、since_discover=1、discover_streak_low=0、queue(place)=19、since_corpus=6。
决策矩阵：since_evv5=8<10 → EVV5 系不触发；discover_streak_low=0<3 → CLOSE 不触发；
queue=19≥10 且 since_discover=1<10 → SCN28 不触发；since_corpus=6<30 → SCN28-corpus 不触发；落 NEW1。
建 5 新页（消费 R68 补种候选）：**Omsk**（MS Strogoff 家乡）+ **Tomsk**（MS 西西伯利亚大城）+
**Pekin**（ASC 清帝国京城）+ **London**（AWED Fogg 赌约起讫城）+ **San Francisco**（AWED 美洲登陆港）。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=8 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =8 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=19≥10, since_discover=1 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =6 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=19 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|-----------------|---------------------------|------|
| omsk | Michael Strogoff (MS) | zcgUM1 | 6 | real / Western Siberia (Russia) | accept |
| tomsk | Michael Strogoff (MS) | smNlPD | 7 | real / Western Siberia (Russia) | accept |
| pekin | The Adventures of a Special Correspondent (ASC) | I1W7pu | 8 | real / China | accept |
| london | Around the World in Eighty Days (AWED) | Yw89Sb | 7 | real / England | accept |
| san-francisco | Around the World in Eighty Days (AWED) | wOpuHo | 7 | real / California (United States) | accept |

> **续 R50 页内引注门**：五页页内 `(VVV-NNN-PPP)` 去重 ≥5——6/7/8/7/7 全达门。
> **Pekin alias**：Verne 原文用旧称「Pekin」，label 从原文，现代名「Peking」收 alias（Beijing 暂不收，未见原文）。
> **同书双页**：london 与 san-francisco 同出 AWED，distinctPN 各自独立核（互不复用引注）。
> **散文门复核**：五页首建段全 ≤400（max 398 london），无需裁剪。

## 命名与互链

- **命名**：omsk / tomsk / pekin（alias Peking）/ london / san-francisco（均 real）。
- **互链**：Omsk ⇄ [[Michael Strogoff]]；Tomsk ⇄ [[Michael Strogoff]]；
  Pekin ⇄ [[The Adventures of a Special Correspondent]]；London ⇄ [[Around the World in Eighty Days]]；
  San Francisco ⇄ [[Around the World in Eighty Days]]。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{MS,ASC,AWED}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页 add 前分段核验通过（max 398）。Connections 节 wikilink 不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；页内引注 distinctPN 逐页核：6/7/8/7/7 |
| G2 散文门 ≤400 | PASS | 五新页 add 前分段，全 PASS（max 398 london）|
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；pekin alias Peking |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选（19→14）；grow_state NEW1 six-step；无新 alias 冲突 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 70→71`；`type_round 41→42`；`rounds_since_last_evv5 8→9`；
`rounds_since_last_discover 1→2`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 6→7`；`last_updated_round→71`。

## 遗留问题

1. **place 页数 155→160**：本轮 +5，registry 全库 1223→1228，unknown 0。
2. **queue(place) 14≥10**：19 − R70 消费 5 = 14（含 2 holds Lake Ontario/Black Sea + Kara Sea 待精扫
   + 6 跨源候选 + R68 补种余 5：Manaos/Christiania/Bergen/Buffalo/Mounts Doerfel）。
3. **下轮 R71**：since_evv5=9<10、queue=14≥10、since_discover=2<10、since_corpus=7<30 → NEW1 建 5 页。
4. **EVV5 触发校正**：R71 后 since_evv5=10 → **R72 起**优先级 1b EVV5 抢占（质量抽检轮，非建页）。
   （校正 R69 log 中「R71 EVV5」表述：EVV5 实际在 since_evv5=10 时于 R72 触发。）
5. **alias 待核（建页时定）**：Manaos↔Manaus、Christiania↔Oslo。
6. **Kara Sea 建前须精扫**：承 R63–R68，「kara」子串过配。
7. **两 hold 照旧**：Lake Ontario（MW:4<5）、Black Sea（跨源过散）。
8. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50/R61 PARK。
9. **debt 照旧 PARK/记录**：HK-book-colon-yaml-break、HK-surface-discover-pattern-undercount、
   featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报。
