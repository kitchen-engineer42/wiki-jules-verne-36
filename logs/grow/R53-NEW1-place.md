---
round: 53
date: 2026-07-15
type_round: 25
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - loch-malcolm
  - gallian-sea
  - cape-bernouilli
  - great-bear-lake
  - cape-horn
result: accept
---

# GROW 2.1-B · R53 · NEW1 · place — R36/R41 长尾强候选批量消费 5 页（standard 档，续 R50 页内引注门）

## 本轮公告

**R53 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选**

R52 后 since_evv5=2、since_discover=4、queue(place)=12，决策矩阵高优先门全否，落 NEW1。
建 5 页，全取 R36/R41 长尾块中主源 distinctPN≫5 之强候选：
**Loch Malcolm**（UC 地下湖，New Aberfoyle 簇）+ **Gallian Sea**（OC 彗星海）+
**Cape Bernouilli**（SC 澳洲 37 度线西端）+ **Great Bear Lake**（FC 极北大湖）+ **Cape Horn**（TTLU/SC 跨源极南岬）。
前轮曾误判「强候选渐尽」，本轮重扫 R36/R41 老块，证长尾仍存多枚 UC:13/OC:12/FC:11/SC:10/TTLU:18 级强候选。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=2 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =2 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=12, since_discover=4 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =20 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue=12 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | 段级 / 页内 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|------|----------------------|---------------------------|------|
| loch-malcolm | The Underground City (UC)| jN9IR0 | 2016 | 段级 13 / 页内 6 | fictional / Scotland (New Aberfoyle) | accept |
| gallian-sea | Off on a Comet (OC)| PVRXrN | 1865 | 段级 12 / 页内 5 | fictional / Gallia (comet) | accept |
| cape-bernouilli | In Search of the Castaways (SC)| 2OkoaN | 2056 | 段级 10 / 页内 6 | real / Australia (South Australia) | accept |
| great-bear-lake | The Fur Country (FC)| fWO4Yz | 2001 | 段级 11 / 页内 7 | real / Canada (NWT) | accept |
| cape-horn | TTLU + SC（跨源）| OyXgWE | 1971 | 跨源段级 18 / 页内 6 | real / Chile (Tierra del Fuego) | accept |

> **续 R50 页内引注门**：五页成页后核页内 `(VVV-NNN-PPP)` 去重 ≥5——
> loch-malcolm 6、gallian-sea 5（贴门）、cape-bernouilli 6、great-bear-lake 7、cape-horn 6，全达门。
> Cape Horn 承 cape-verde/caspian-sea 先例，单一真实地跨源引注（SC 3 + TTLU 3）合法计和。

## 命名与互链

- **命名**：loch-malcolm / gallian-sea / cape-bernouilli / **great-bear-lake**（label Great Bear Lake / alias Bear Lake，从语料实名「Great Bear Lake」）/ cape-horn。
- **互链**：Loch Malcolm ⇄ [[The Underground City]] / [[New Aberfoyle]] / [[Loch Katrine]]（地下/地上双湖对照）；
  Gallian Sea ⇄ [[Off on a Comet]] / [[Gourbi Island]]（彗星世界）；
  Cape Bernouilli ⇄ [[In Search of the Castaways]] / [[Twofold Bay]]（37 度线两端）；
  Great Bear Lake ⇄ [[The Fur Country]] / [[Fort Confidence]] / [[Cape Bathurst]]（极北漂流簇）；
  Cape Horn ⇄ [[Twenty Thousand Leagues Under the Sea]] / [[In Search of the Castaways]]（Nautilus/Duncan 皆绕行）。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{UC,OC,SC,FC,TTLU}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页全段分段核验通过（add_page.py 防缩减 + 散文门全 PASS）。Connections 节 wikilink 不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；页内引注 distinctPN ≥5 逐页核：6/5/6/7/6 |
| G2 散文门 ≤400 | PASS | add 前分段核验，五页全 PASS |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；含撇号/冒号值单引号转义 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选（12→7）；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 53→54`；`type_round 24→25`；`rounds_since_last_evv5 2→3`；
`rounds_since_last_discover 4→5`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 20→21`；`last_updated_round→54`。

## 遗留问题

1. **place 页数 102→107**：本轮 +5，registry 全库 1170→1175。
2. **queue(place) 7**：12 − R53 消费 5 = 7，首次跌破 SCN28 阈值（<10）。余 5 真候选
   （Polar Sea FC:14 / Melville Island ACH:9 borderline / Rocky Mountains RM:9 跨作 / Cape Washington ACH:5 贴门 / Hudson's Bay 12 需排除 Company org 义）
   + 2 hold（Lake Ontario 主源 MW:4<5、Black Sea 跨源过散）。
   **下轮 R54：queue=7<10 触发优先级 3 SCN28**——表层复扫补种 place 候选池（自 R48 以来首次 discover）。
3. **两 hold 候选照旧**：Lake Ontario（待净分升格）、Black Sea（跨源过散）。
4. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39/R50 PARK。
5. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 八项债务照旧 PARK/记录。
