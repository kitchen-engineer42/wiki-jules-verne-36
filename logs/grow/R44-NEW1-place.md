---
round: 44
date: 2026-07-15
type_round: 16
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - melville-bay
  - lake-baikal
  - aleutian-islands
  - wellington-channel
  - great-salt-lake
result: accept
---

# GROW 2.1-B · R44 · NEW1 · place — R41 补种第三批 5 页（standard 档）

## 本轮公告

**R44 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选**

R43 后 queue(place)=29，since_discover=2、since_evv5=4，轮首决策矩阵高优先门全否，落 NEW1。
建 R41 补种第三批高分 5 页：
**Melville Bay**(ACH:12 Forward 首程目标湾) / **Lake Baikal**(MS:18 含变体 Strogoff 越境大湖) /
**Aleutian Islands**(FC:17 漂流末程盼达岛链) / **Wellington Channel**(ACH:10 极海通道) /
**Great Salt Lake**(AWED:10 Fogg 横美盐湖)。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=4 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =4 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=29, since_discover=2 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =11 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue(place)=29 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | 实测 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|------|-----------------|---------------------------|------|
| melville-bay | The Adventures of Captain Hatteras (ACH)| DgSjCF | 2197 | 12 | real / Arctic (Baffin Bay) | accept |
| lake-baikal | Michael Strogoff (MS)| 1ZLYip | 2047 | 18（含「the Baikal」变体）| real / Asia (Siberia) | accept |
| aleutian-islands | The Fur Country (FC)| Dm9iGl | 2084 | 17 | real / North Pacific (Bering Sea) | accept |
| wellington-channel | The Adventures of Captain Hatteras (ACH)| 9pMXcs | 2186 | 10 | real / Arctic (Canadian archipelago) | accept |
| great-salt-lake | Around the World in Eighty Days (AWED)| 5hL12o | 1986 | 10 | real / North America (Utah) | accept |

> **建前二次校准（承铁律）**：五候选 distinctPN 逐页严扫复核——Melville Bay（ACH 12）、
> Lake Baikal（MS「Lake Baikal」+「the Baikal」变体严扫 18，高于 queue 估值 12）、
> Aleutian Islands（FC「Aleutian Islands/Isles」17，高于 queue 估值 12）、Wellington Channel（ACH 10）、
> Great Salt Lake（AWED「(Great )Salt Lake」10；页写「Great Salt Lake」湖，alias「Salt Lake」，
> 与 Salt Lake City 城镇辨明——本页写湖，城作纯文本提及）——全 ≥5 达 standard 门。无同实体合并顾虑。

> **互链**：Melville Bay ⇄ [[Beechey Island]] / [[The Forward]]（ACH 极地簇；Franklin/Smith's Straits 纯文本）；
> Lake Baikal ⇄ [[Michael Strogoff]]（+纯文本 Angara/Irkutsk）；
> Aleutian Islands ⇄ [[Behring Sea]] / [[Victoria Island]]（FC 漂流簇末程）；
> Wellington Channel ⇄ [[Beechey Island]] / [[The Forward]]（ACH 极地簇；Lancaster/Barrow 纯文本）；
> Great Salt Lake ⇄ [[Pacific Railroad]]（+纯文本 Salt Lake City/Ogden/Weber River）。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{ACH,MS,FC,AWED}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页全段分段核验通过（add 前 `\n\n` 拆分实测 max 295–382，无超长段）。Connections 节 wikilink/纯文本不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；keyword-overlap warn 非阻塞 |
| G2 散文门 ≤400 | PASS | add 前分段核验，五页 max 382 |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；lake-baikal alias「The Baikal」、aleutian-islands alias「Aleutian Isles」、great-salt-lake alias「Salt Lake」 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 44→45`；`type_round 15→16`；`rounds_since_last_evv5 4→5`；
`rounds_since_last_discover 2→3`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 11→12`；`last_updated_round→45`。

## 遗留问题

1. **queue(place) 余 24**：R43 后 29 − R44 消费 5 = 24。下批优选：
   Fort Kearney(AWED:9) / Amsterdam Island(SC:9) / Port Egmont(AM:9) / Lake Taupo(SC:8) /
   Cape Farewell(ACH:8) / Lancaster Strait(ACH:7) / Bellot Strait(ACH:7) / Washington Bay(MI:7)。
   建前逐页复核 distinctPN、查同实体合并。
2. **since_corpus 本轮达 12**：距 SCN28-corpus 深扫门（≥30）尚远，暂不触发。
3. **since_evv5 达 5**：距 EVV5 门（≥10）尚 5 轮，约 R49 触发。
4. **queue 估值偏低勘误**：本轮 Lake Baikal（估 12 实 18）、Aleutian Islands（估 12 实 17）严扫均高于 R41 queue 估值——
   承铁律「两界都要验」，估值可偏高亦可偏低，建前必逐页实测。
5. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39 EVV5 记录，PARK。
6. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 八项债务照旧 PARK/记录。
