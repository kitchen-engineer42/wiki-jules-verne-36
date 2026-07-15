---
round: 46
date: 2026-07-15
type_round: 18
phase: "2.1"
current_type: place
gene: NEW1
new_candidates: 0
pages:
  - bellot-strait
  - lancaster-strait
  - barrow-strait
  - mandible-cape
  - washington-bay
result: accept
---

# GROW 2.1-B · R46 · NEW1 · place — R41 补种第五批 5 页（standard 档）

## 本轮公告

**R46 — Phase 2.1 — NEW1 — place — 5 建页 / standard 档 / 消费 5 候选**

R45 后 queue(place)=19，since_discover=4、since_evv5=6，轮首决策矩阵高优先门全否，落 NEW1。
建 R41 补种第五批 5 页（ACH 极地海峡簇 3 + MI Lincoln Island 簇 2）：
**Bellot Strait**(ACH:7 Boothia 南唯一出口) / **Lancaster Strait**(ACH:9 西北航道史门) /
**Barrow Strait**(ACH:9 Beechey 常道) / **Mandible Cape**(MI:13 Union Bay 北双岬) /
**Washington Bay**(MI:6 Lincoln 南湾)。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=6 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =6 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| 3 | SCN28（queue_size < 10 或 since_discover ≥ 10）| queue=19, since_discover=4 | 否 |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =13 | 否 |
| 3.9 | zombie-guard（queue(place)==0）| queue(place)=19 | 否 |
| RCH2（stub% ≥ 20%）| stub%=0 | 否 |
| **NEW1（默认）** | — | — | **触发** |

## 页面处理记录

| slug | 源作 | rev | size | 实测 distinctPN | real_or_fictional / region | 判定 |
|------|------|-----|------|-----------------|---------------------------|------|
| bellot-strait | The Adventures of Captain Hatteras (ACH)| y6DeUl | 1956 | 7 | real / Arctic (Boothia) | accept |
| lancaster-strait | The Adventures of Captain Hatteras (ACH)| ET7hlk | 2083 | 9 | real / Arctic (Baffin Bay) | accept |
| barrow-strait | The Adventures of Captain Hatteras (ACH)| UZuhWZ | 2098 | 9 | real / Arctic (Canadian archipelago) | accept |
| mandible-cape | The Mysterious Island (MI)| 2QN6vh | 2054 | 13 | fictional / Pacific (Lincoln Island) | accept |
| washington-bay | The Mysterious Island (MI)| 2N0bPg | 1952 | 6 | fictional / Pacific (Lincoln Island) | accept |

> **建前二次校准（承铁律）+ 同名实体辨析**：Bellot Strait queue 估值 7，但聚合初扫报 24——混入探险家「Bellot」
> 人名（ACH-020-025 记 Sir John Barrow 为 Bellot 立碑等）；严扫「Bellot Strait」海峡名 7 distinctPN，达标。
> Lancaster 亦「Strait 9 / Sound 3」两式，取主式 Strait 9。其余（Barrow 9 / Mandible Cape 13 / Washington Bay 6）
> 逐页严扫达 standard 门。Mandible Cape 为双岬（North/South Mandible Cape），一页统写。无跨实体合并顾虑。

> **互链**：Bellot Strait ⇄ [[The Forward]] / [[Beechey Island]]（ACH 极地簇）；
> Lancaster Strait ⇄ [[The Forward]] / [[Barrow Strait]] / [[Beechey Island]]（ACH 簇）；
> Barrow Strait ⇄ [[Lancaster Strait]] / [[Beechey Island]] / [[Wellington Channel]]（ACH 簇）；
> Mandible Cape ⇄ [[Lincoln Island]] / [[Union Bay]] / [[Claw Cape]] / [[Mount Franklin]]（MI 微地理簇）；
> Washington Bay ⇄ [[Lincoln Island]] / [[Union Bay]] / [[Claw Cape]] / [[Mount Franklin]]（MI 簇）。

## PN 接地核验

正文句 PN 自 `data/sentence_index/{ACH,MI}-*.jsonl`，段级 PN 为 sid 前三段。散文门 ≤400：
五页全段分段核验通过（add 前 `\n\n` 拆分实测 max 296–357，无超长段）。Connections 节 wikilink/纯文本不强制 PN。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | PASS | 全句 PN 自 sentence_index；keyword-overlap warn 非阻塞 |
| G2 散文门 ≤400 | PASS | add 前分段核验，五页 max 357 |
| G3 schema 合规 | PASS | 4 H2 齐备；book/real_or_fictional/region 写入；lancaster-strait alias「Lancaster Straits」、mandible-cape alias「Mandible Capes」 |
| G4 记录完整性 | PASS | 本日志；queue.md 消费 5 候选；grow_state six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（NEW1 six-step）

`current_round 46→47`；`type_round 17→18`；`rounds_since_last_evv5 6→7`；
`rounds_since_last_discover 4→5`（非 discover 轮，streak 不变）；`discover_streak_low` 保持 0；
`rounds_since_last_corpus_discover 13→14`；`last_updated_round→47`。

## 遗留问题

1. **queue(place) 余 14**：R45 后 19 − R46 消费 5 = 14。下批优选：
   Cape Corrientes(SC:5) / Victoria Bay(ACH:6) / Cape Washington(ACH:5) / Lake Superior(MW:6) /
   Lake Michigan(MW:6) / Lake Tanganyika(DSCF:6) / Niagara River（已建）/ Creek（已建）等。
   余多为 5–6 薄候选，建前逐页复核 distinctPN；若严扫跌破 5 则弃或留 list。
2. **since_corpus 本轮达 14**：距 SCN28-corpus 深扫门（≥30）尚远，暂不触发。
3. **since_evv5 达 7**：距 EVV5 门（≥10）尚 3 轮，约 R49 触发。
4. **同名实体辨析累计**：Bellot Strait（海峡）≠ 探险家 Bellot 人名——承 Cape Farewell≠schooner Farewell（R45）、
   Behring Sea≠Behring Strait（R43）、Great Salt Lake≠Salt Lake City（R44）之辨。同名 grep 聚合易虚高，
   建前必按语义拆分上下文。已四轮连续遇同名混淆，属 discover 双盲区之一表现，照旧 PARK 记录。
5. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39 EVV5 记录，PARK。
6. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   discover 双盲区、registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 八项债务照旧 PARK/记录。
