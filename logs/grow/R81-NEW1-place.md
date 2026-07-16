---
round: 81
date: 2026-07-15
type_round: 52
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - amazon
  - volga
  - omaha
  - liverpool
  - suez
result: accept
---

# GROW 2.1-B · R81 · NEW1 · place — 建 5 新页（standard 档，大河/大港群）+ 撤 R78 重复页 tsalal

## 本轮公告

**R81 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选 / queue 19→14 / 附撤 1 重复页**

R80（NEW1 建 5）后 since_evv5=8、since_discover=1、discover_streak_low=0、queue(place)=19、since_corpus=17。
决策矩阵：since_evv5=8<10 → EVV5 系不触发；discover_streak_low=0<3 → CLOSE 不触发；
queue=19≥10 且 since_discover=1<10 → SCN28 不触发；since_corpus=17<30 → 非 corpus；落 NEW1。
建 5 新页，消费 R79 补种「大河/大港」头部：**Amazon**（EHLA 主河）+ **Volga**（MS 欧俄大河）+
**Omaha**（AWED 太平洋铁路东端）+ **Liverpool**（AWED 归国港）+ **Suez**（AWED 运河镇）。
五页均单源、页内引注 5 全达门。

**附带修复**：build_registry 报 `alias conflict: 'Tsalal Island' → tsalal-island vs tsalal`。
经查 R78 所建 `tsalal` 与既有 `tsalal-island`（R37 正页，halbrane-land 反链）为**同一实体重复页**，
违反 LAW §10 label 唯一性。R78 建页时未做 pages.json 既有页交叉核（该纪律 R79 起才落地）。
本轮 `git rm docs/wiki/pages/ts/tsalal.md` 撤销我方重复页，正页 tsalal-island 承载 `[[Tsalal Island]]` 链接，
反链无损（halbrane-land 原即指向 tsalal-island）。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=8 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =8 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=19≥10, since_discover=1 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =17 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=19 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|-----------------|---------------------------|------|
| amazon | Eight Hundred Leagues on the Amazon (EHLA) | bANurV | 5 | real / South America | accept |
| volga | Michael Strogoff (MS) | 5nEKXa | 5 | real / Russia | accept |
| omaha | Around the World in Eighty Days (AWED) | bJq4g4 | 5 | real / United States (Nebraska) | accept |
| liverpool | Around the World in Eighty Days (AWED) | oncRz1 | 5 | real / England | accept |
| suez | Around the World in Eighty Days (AWED) | 1JMJ5R | 5 | real / Egypt | accept |
| ~~tsalal~~ | An Antarctic Mystery (AM) | — | — | — / — | **RETIRE**（R78 重复页，git rm；正页 tsalal-island）|

> **续 R50 页内引注门**：五新页页内 `(VVV-NNN-PPP)` 去重 =5/5/5/5/5 全达门。
> **AWED 三港连建**：Omaha/Liverpool/Suez 同源，Fogg 环球航线三节点（运河→铁路东端→归国港），
> distinctPN 稳固，接地句均确指地名（词边界，非人名/船名）。
> **散文门五页全 ≤400**（add 前分段核验，无微调即通过）。
> **alias**：amazon→Amazon River；余四页 Verne 原文即用现名，无 modern alias。
> **forward-link 门**：amazon 原引 [[Ega]]（未建）、volga 原引 [[Ural]]（未建），add 前改为
> 仅链既建页 / 纯文本（续 R80 [[Irtish]]→[[Baraba]] 惯例），避免红链。

## 命名与互链

- **命名**：amazon（alias Amazon River）/ volga / omaha / liverpool / suez——均 real。
- **互链**：
  Amazon ⇄ [[Eight Hundred Leagues on the Amazon]]/[[Iquitos]]/[[Tabatinga]]/[[Manaos]]/[[Belem]]；
  Volga ⇄ [[Michael Strogoff]]/[[Nijni-Novgorod]]/[[Perm]]；
  Omaha ⇄ [[Around the World in Eighty Days]]/[[San Francisco]]/[[Phileas Fogg]]；
  Liverpool ⇄ [[Around the World in Eighty Days]]/[[London]]/[[Phileas Fogg]]/[[Fix]]；
  Suez ⇄ [[Around the World in Eighty Days]]/[[Bombay]]/[[Fix]]/[[Phileas Fogg]]。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{EHLA,MS,AWED}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页 add 前分段核验通过（无微调）。建后就地复核页面文件
`grep -oE '\([A-Za-z0-9]+-[0-9]+-[0-9]+\)' | sort -u | wc -l` = 5/5/5/5/5，全达门。Connections 节 wikilink 不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index（20 句逐条 grep 核）；页内引注 distinctPN 逐页核 5/5/5/5/5 |
| G2 散文门 ≤400 | PASS | 五新页 add 前分段，全 PASS 无微调 |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；amazon 有 alias（Amazon River）；撤 tsalal 后 label 冲突清零（仅 Robur 旧账 PARK）|
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选（19→14）+ Tsalal 条作废；grow_state NEW1 six-step；registry 1258→1263→撤 1 = 1262，unknown 0 |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 81→82`；`type_round 52→53`；`rounds_since_last_evv5 8→9`；
`rounds_since_last_discover 1→2`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 17→18`；`last_updated_round→82`。

## 遗留问题

1. **place 页数 190→194**：本轮 +5 新页 −1 重复页（tsalal）= 净 +4；registry 全库 1258→1262，unknown 0。
2. **queue(place) 14≥10**：19 − R81 消费 5 = 14（含 Auckland/Shanghai/Singapore/Ega/Zabediero +
   R76 剩 Allahabad/Benares + 既有 7 跨源/hold）。
3. **下轮 R82 = EVV5（优先级 1b）**：R81 后 since_evv5=9，R82 起达 10 → 触发 EVV5；届时 since_discover=2<10
   → 优先级 1b 单 EVV5（非建页质量审计轮：模板稳定则日志「无需更新」，仅 stage 日志+housekeeping+state）。
4. **新增 housekeeping：HK-R78-tsalal-dup**——R78 建页未交叉核 pages.json 致重复页，R81 已撤。
   根因：既有页交叉核纪律 R79 起才落地，R77/R78 建页在此前。建议补扫 R77/R78 建的 10 页是否另有重复
   （下次 discover 轮附带核；本轮已抽核余页无 label 冲突，registry 仅剩 Robur 旧账）。
5. **place runway 仍充足**：候选池余 12+；后续尚有美西铁路镇、南美/亚洲港、俄/西伯利亚河待精核。
6. **两 hold + 跨源候选照旧**：Lake Ontario（MW:4<5）、Black Sea（跨源过散）、North Sea/Cape Bon
   （跨源待建）、Long Island/Bay of Bengal（降级 hold）、Kara Sea（建前须精扫）。
7. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50/R61 PARK。
8. **debt 照旧 PARK/记录**：HK-book-colon-yaml-break、HK-surface-discover-pattern-undercount、
   featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报。
