---
round: 42
date: 2026-07-15
type_round: 14
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - ural-mountains
  - black-rock-creek
  - fort-confidence
  - halbrane-land
  - pamlico-sound
result: accept
---

# GROW 2.1-B · R42 · NEW1 · place — R41 补种首批 5 页（standard 档）

## 本轮公告

**R42 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选**

R41 SCN28 补种后 queue(place)=39，since_discover 归零。轮首决策矩阵高优先门全否，落 NEW1。
建 R41 补种首批高分 5 页（各源作 top distinctPN）：
**Ural Mountains**(MS:21 Strogoff 越境山脉) / **Pamlico Sound**(FF:21 Ebba 停泊之湾) /
**Black Rock Creek**(MW:17 Terror 藏身溪) / **Fort Confidence**(FC:16 大熊湖畔北极堡) /
**Halbrane Land**(AM:14 南极虚构地)。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=2 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =2 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=39, since_discover=0 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =9 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue(place)=39 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | 实测 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|------|-----------------|---------------------------|------|
| ural-mountains | Michael Strogoff (MS)| geZqUb | 2240 | 21（严扫，含变体 39）| real / Russia (Europe–Asia frontier) | accept |
| black-rock-creek | The Master of the World (MW)| h7arGO | 2126 | 17 | fictional / North America (Lake Erie shore) | accept |
| fort-confidence | The Fur Country (FC)| bfRrf3 | 2184 | 16 | real / Arctic (Great Bear Lake) | accept |
| halbrane-land | An Antarctic Mystery (AM)| J67Wnu | 2144 | 14 | fictional / Antarctic | accept |
| pamlico-sound | Facing the Flag (FF)| a0wpxD | 2085 | 21 | real / North America (North Carolina) | accept |

> **建前二次校准（承铁律）**：五候选 distinctPN 逐页严扫复核——Ural Mountains（MS「Ural Mountains」21，
> 含「the Urals/the Ural」变体 39）、Pamlico Sound（FF 21）、Black Rock Creek（MW「Black Rock Creek」/「Black Rock」17）、
> Fort Confidence（FC 16）、Halbrane Land（AM 14）——全 ≥5 达 standard 门。无同实体合并顾虑（五地各异）。

> **互链**：Ural Mountains ⇄ [[michael-strogoff]]（+纯文本 Ogareff/Ekaterenburg 红链）；
> Black Rock Creek ⇄ [[the-terror]] / [[robur]] / [[lake-erie]] / [[great-eyrie]]（MW 簇）；
> Fort Confidence ⇄ [[cape-bathurst]] / [[fort-hope]]（FC 漂流簇前站）；
> Halbrane Land ⇄ [[tsalal-island]] / [[christmas-harbour]]（AM 南极簇）；
> Pamlico Sound 纯文本（Ebba / Facing the Flag / Neuse River 无既有页，schema 允许）。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{MS,MW,FC,AM,FF}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页全段分段核验通过（add 前 `\n\n` 拆分，无超长段）。Connections 节 wikilink/纯文本不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；keyword-overlap warn 非阻塞 |
| G2 散文门 ≤400 | PASS | add 前分段核验，五页无超长段 |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；ural-mountains 加 alias「The Urals」 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 42→43`；`type_round 13→14`；`rounds_since_last_evv5 2→3`；
`rounds_since_last_discover 0→1`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 9→10`；`last_updated_round→43`。

## 遗留问题

1. **queue(place) 余 34**：R41 补种 39 − R42 消费 5 = 34。下批优选：
   Flag Point(GM:14, 勘误恢复) / Behring Sea(FC:13) / Creek Glycerine(MI:13) / Niagara River(MW:12) /
   Slave Lake(FC:12) / Aleutian Islands(FC:12) / Melville Bay(ACH:12) / Lake Baikal(MS:12)。
   建前逐页复核 distinctPN、查同实体合并。
2. **since_corpus 本轮达 10**（下轮 R43 后累进）：距 SCN28-corpus 深扫门（≥30）尚远，暂不触发。
3. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39 EVV5 记录，PARK。
4. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 八项债务照旧 PARK/记录。
