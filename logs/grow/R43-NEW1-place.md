---
round: 43
date: 2026-07-15
type_round: 15
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - flag-point
  - behring-sea
  - creek-glycerine
  - niagara-river
  - great-slave-lake
result: accept
---

# GROW 2.1-B · R43 · NEW1 · place — R41 补种第二批 5 页（standard 档）

## 本轮公告

**R43 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选**

R42 后 queue(place)=34，since_discover=1、since_evv5=3，轮首决策矩阵高优先门全否，落 NEW1。
建 R41 补种第二批高分 5 页（各源作 top distinctPN）：
**Flag Point**(GM:14 Godfrey 竖旗之岬，勘误恢复) / **Behring Sea**(FC:13 Victoria Island 漂入之海) /
**Creek Glycerine**(MI:13 Lincoln Island 人工溪) / **Niagara River**(MW:17 含变体 Erie 唯一出水口) /
**Great Slave Lake**(FC:13 Hobson 远征南起点大湖)。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=3 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =3 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=34, since_discover=1 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =10 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue(place)=34 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | 实测 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|------|-----------------|---------------------------|------|
| flag-point | Godfrey Morgan (GM)| Ua1a7j | 2038 | 14（严扫，勘误恢复）| fictional / Pacific (Spencer Island) | accept |
| behring-sea | The Fur Country (FC)| EnXo5X | 2197 | 13 | real / North Pacific (Bering Sea) | accept |
| creek-glycerine | The Mysterious Island (MI)| Xb3DpT | 2303 | 13 | fictional / Pacific (Lincoln Island) | accept |
| niagara-river | The Master of the World (MW)| ay5uGw | 2052 | 17（含 Niagara Falls/the Niagara 变体）| real / North America (NY–Canada) | accept |
| great-slave-lake | The Fur Country (FC)| P5rbdm | 2167 | 13 | real / North America (Canada, sub-Arctic) | accept |

> **建前二次校准（承铁律）**：五候选 distinctPN 逐页严扫复核——Flag Point（GM「Flag Point」14
> distinctPN，R34/R36/R38 曾误弃「GM 仅 4」，R41 勘误恢复，本轮实测确认 14）、Behring Sea（FC「Behring Sea」13，
> 与既有 behring-strait 异实体，前者海/后者峡）、Creek Glycerine（MI 13）、Niagara River（MW「Niagara River」严扫，
> 含「Niagara Falls/the Niagara」变体计 17）、Great Slave Lake（FC「(Great )Slave Lake」13）——全 ≥5 达 standard 门。
> 无同实体合并顾虑（五地各异；Behring Sea≠Behring Strait 已辨）。

> **互链**：Flag Point ⇄ [[Spencer Island]]（+纯文本 Godfrey Morgan/Dream Bay）；
> Behring Sea ⇄ [[Victoria Island]] / [[Behring Strait]]（FC 漂流簇；Aleutian/St Matthew 纯文本红链）；
> Creek Glycerine ⇄ [[Lincoln Island]] / [[Lake Grant]] / [[Falls River]] / [[Prospect Heights]]（MI 微地理簇）；
> Niagara River ⇄ [[Lake Erie]] / [[The Terror]] / [[Great Eyrie]]（MW 簇）；
> Great Slave Lake ⇄ [[Fort Reliance]] / [[Fort Confidence]]（FC 陆路前站；Fort Providence/Resolution 纯文本）。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{GM,FC,MI,MW}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页全段分段核验通过（add 前 `\n\n` 拆分实测 max 303–379，无超长段）。Connections 节 wikilink/纯文本不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；keyword-overlap warn 非阻塞 |
| G2 散文门 ≤400 | PASS | add 前分段核验，五页 max 379 |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；great-slave-lake 加 alias「Slave Lake」 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 43→44`；`type_round 14→15`；`rounds_since_last_evv5 3→4`；
`rounds_since_last_discover 1→2`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 10→11`；`last_updated_round→44`。

## 遗留问题

1. **queue(place) 余 29**：R42 后 34 − R43 消费 5 = 29。下批优选：
   Creek（已消费）外 Niagara（已消费）——余高分：Melville Bay(ACH:12) / Lake Baikal(MS:12) /
   Aleutian Islands(FC:12) / Slave Lake（已消费为 great-slave-lake）/ Niagara（已消费）/
   Wellington Channel(ACH:10) / Salt Lake(AWED:10) / Amsterdam Island(SC:9)。建前逐页复核 distinctPN、查同实体合并。
2. **since_corpus 本轮达 11**：距 SCN28-corpus 深扫门（≥30）尚远，暂不触发。
3. **since_evv5 达 4**：距 EVV5 门（≥10）尚 6 轮，约 R49 触发。
4. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39 EVV5 记录，PARK。
5. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 八项债务照旧 PARK/记录。
