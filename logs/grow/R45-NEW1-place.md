---
round: 45
date: 2026-07-15
type_round: 17
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - fort-kearney
  - amsterdam-island
  - port-egmont
  - lake-taupo
  - cape-farewell
result: accept
---

# GROW 2.1-B · R45 · NEW1 · place — R41 补种第四批 5 页（standard 档）

## 本轮公告

**R45 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选**

R44 后 queue(place)=24，since_discover=3、since_evv5=5，轮首决策矩阵高优先门全否，落 NEW1。
建 R41 补种第四批 5 页：
**Fort Kearney**(AWED:11 Fogg 遭 Sioux 袭之驿站) / **Amsterdam Island**(SC:13 37 度线孤岛) /
**Port Egmont**(AM:9 Halbrane 福克兰补给港) / **Lake Taupo**(SC:11 Maori 囚地) /
**Cape Farewell**(ACH:严扫 6 格陵兰南岬)。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=5 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =5 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=24, since_discover=3 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =12 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue(place)=24 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | 实测 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|------|-----------------|---------------------------|------|
| fort-kearney | Around the World in Eighty Days (AWED)| 65u0la | 1908 | 11 | real / North America (Nebraska) | accept |
| amsterdam-island | In Search of the Castaways (SC)| HzFcAz | 1987 | 13 | real / Indian Ocean | accept |
| port-egmont | An Antarctic Mystery (AM)| MmS5Gb | 2184 | 9 | real / South Atlantic (Falklands) | accept |
| lake-taupo | In Search of the Castaways (SC)| KhAtUQ | 2118 | 11 | real / Oceania (New Zealand) | accept |
| cape-farewell | The Adventures of Captain Hatteras (ACH)| 6NbpIv | 1889 | 6（严扫，岬名，排除同名 schooner Farewell）| real / Arctic (Greenland) | accept |

> **建前二次校准（承铁律）+ 同名实体辨析**：Cape Farewell queue 估值 9 中混入了同名纵帆船「schooner Farewell」
> （ACH-012-058/023-018 指船非岬）；严扫「Cape Farewell」岬名仅 6 distinctPN（ACH-004-043/005-064/006-003/006-026/
> 010-009/047-030），仍 ≥5 达 standard 门，但页正文只引岬（5 净引 + 007-010 泛指 capes 作叙事色），船另论。
> 其余四候选（Fort Kearney 11 / Amsterdam Island 13 / Port Egmont 9 / Lake Taupo 11）逐页严扫达标，无合并顾虑。

> **互链**：Fort Kearney ⇄ [[Pacific Railroad]]（+纯文本 Aouda/Passepartout）；
> Amsterdam Island ⇄ 纯文本 [[Jacques Paganel]]/Duncan/Tristan d'Acunha（Paganel character 红链待 character 轮）；
> Port Egmont ⇄ [[Halbrane Land]] / [[Christmas Harbour]]（AM 簇；Hunt/Len Guy 纯文本）；
> Lake Taupo ⇄ 纯文本 Paganel/Bay of Plenty；
> Cape Farewell ⇄ [[The Forward]] / [[Melville Bay]]（ACH 极地簇）。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{AWED,SC,AM,ACH}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页全段分段核验通过（add 前 `\n\n` 拆分实测 max 290–352，无超长段）。Connections 节 wikilink/纯文本不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；keyword-overlap warn 非阻塞 |
| G2 散文门 ≤400 | PASS | add 前分段核验，五页 max 352 |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；amsterdam-island alias「Amsterdam Isles」 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 45→46`；`type_round 16→17`；`rounds_since_last_evv5 5→6`；
`rounds_since_last_discover 3→4`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 12→13`；`last_updated_round→46`。

## 遗留问题

1. **queue(place) 余 19**：R44 后 24 − R45 消费 5 = 19。下批优选：
   Lancaster Strait(ACH:7) / Bellot Strait(ACH:7) / Washington Bay(MI:7) / Cape Corrientes(SC:5) /
   Barrow Strait(ACH:6) / Victoria Bay(ACH:6) / Cape Washington(ACH:5) / Lake Superior(MW:6) /
   Lake Michigan(MW:6) / Mandible Cape(MI:9) / Lake Tanganyika(DSCF:6)。建前逐页复核 distinctPN、查同实体合并。
2. **since_corpus 本轮达 13**：距 SCN28-corpus 深扫门（≥30）尚远，暂不触发。
3. **since_evv5 达 6**：距 EVV5 门（≥10）尚 4 轮，约 R49 触发。
4. **同名实体辨析入账**：Cape Farewell（岬）≠ schooner Farewell（船）——承 Behring Sea≠Behring Strait（R43）、
   Great Salt Lake≠Salt Lake City（R44）之辨，queue 估值遇同名须按语义拆分，建前逐条 grep 上下文确认。
5. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39 EVV5 记录，PARK。
6. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 八项债务照旧 PARK/记录。
