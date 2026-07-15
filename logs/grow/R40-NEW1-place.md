---
round: 40
date: 2026-07-15
type_round: 12
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - lake-erie
  - fort-providence
  - beechey-island
  - gulf-stream
  - torres-strait
result: accept
---

# GROW 2.1-B · R40 · NEW1 · place — R36 复扫第三批 5 页（standard 档）

## 本轮公告

**R40 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选**

R39 EVV5 反思后 since_evv5 归零。轮首决策矩阵高优先门全否，落 NEW1 默认门。
建 R36 复扫第三批 5 页：
**大湖/北极堡**（Lake Erie MW:27 Terror 现身之湖 / Fort Providence ACH:22 Hatteras 越冬堡）+
**北极岛**（Beechey Island ACH:23 极地探险总汇合点）+
**Nautilus 航线**（Gulf Stream TTLU:18 大西洋暖流 / Torres Strait TTLU:16 搁浅海峡）。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=0 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =0 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=15, since_discover=3 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =7 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue(place)=15 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | 实测 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|------|-----------------|---------------------------|------|
| lake-erie | The Master of the World (MW)| XonrDi | 2224 | 27 | real / North America (Great Lakes) | accept |
| fort-providence | Adv. of Captain Hatteras (ACH)| P7ngFy | 2295 | 22 | fictional / Arctic (New America) | accept |
| beechey-island | Adv. of Captain Hatteras (ACH)| 5uyZIE | 2206 | 23 | real / Arctic (Barrow Strait) | accept |
| gulf-stream | Twenty Thousand Leagues (TTLU)| MglZSp | 2380 | 18 | real / Atlantic Ocean | accept |
| torres-strait | Twenty Thousand Leagues (TTLU)| qxYQqX | 2327 | 16 | real / Pacific (Australia–N. Guinea) | accept |

> **建前二次校准（承 R38 铁律）**：五候选 distinctPN 为 R36 grep 值，本轮建页前逐页复核：
> Lake Erie=27（MW 严扫）、Fort Providence=22（ACH「Fort Providence」严扫，非宽「Providence」）、
> Beechey Island=23（ACH）、Gulf Stream=18（TTLU）、Torres Strait=16（TTLU）——全 ≥5 达 standard 门。
> 无同实体合并顾虑（五地各异）。

> **互链**：Lake Erie ⇄ [[the-terror]] / [[robur]] / [[great-eyrie]]（MW 簇）；
> Fort Providence ⇄ [[captain-hatteras]] / [[the-forward]] / [[north-pole]]（Hatteras 北极簇）；
> Beechey Island ⇄ [[captain-hatteras]] / [[the-forward]] / [[fort-providence]]（同书互引）；
> Gulf Stream ⇄ [[nautilus]] / [[captain-nemo]] / [[sargasso-sea]]（TTLU 航线）；
> Torres Strait ⇄ [[nautilus]] / [[captain-nemo]] / [[ned-land]]（TTLU 搁浅段）。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{MW,ACH,TTLU}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页全段分段核验通过（add 前 `\n\n` 拆分，无超长段）。Connections 节 wikilink/纯文本不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；keyword-overlap warn 非阻塞 |
| G2 散文门 ≤400 | PASS | add 前分段核验，五页无超长段 |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 40→41`；`type_round 11→12`；`rounds_since_last_evv5 0→1`；
`rounds_since_last_discover 3→4`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 7→8`；`last_updated_round→41`。

## 遗留问题

1. **queue(place) 余 9**（实测 grep 开放候选，非估算）：R37 消费 5 − R38 消费 6 − R40 消费 5 后余 9。
   下批优选：Polar Sea(FC:14) / Loch Malcolm(UC:13) / Lake Baikal(MS:12) / Gallian Sea(OC:12) /
   Bear Lake(FC:11) / Cape Bernouilli(SC:10) / Cape Horn(TTLU:9) / Rocky Mountains(RM:9) /
   Melville Island(ACH:9)。建前逐页复核 distinctPN、查同实体合并。
2. **queue(place)=9 < 10 → R41 触 SCN28**：轮首决策矩阵优先级 3（queue_size < 10）先于 NEW1。
   **R41 应为 SCN28 表层复扫**（discover 轮，0 建页；since_discover=4→0，扫 place 补种候选池）。
   since_evv5 本轮 0→1，距 EVV5 尚 9 轮。R41 轮首以 state 值重判确认。
3. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39 EVV5 记录，非本轮扩张产物，PARK。
4. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 八项债务照旧 PARK/记录。
