---
round: 48
date: 2026-07-15
type_round: 20
phase: "2.1"
current_type: place
gene: SCN28
new_candidates: 18
result: accept
---

# GROW 2.1-B · R48 · SCN28 · place — 表层复扫补种 +18 候选（queue<10 触发）

## 本轮公告

**R48 — Phase 2.1 — SCN28（表层 discover）— place — 补种 18 候选 / 0 建页**

R47 后 queue(place)=9 < 10，决策矩阵优先级 3（SCN28：queue_size < 10）触发，落 discover 而非 NEW1。
全 36 部语料按 `(Cape|Lake|Mount|Fort|Port|Loch|Gulf|Point)+Name` 及
`Name+(Island|Bay|River|Sea|Strait|Sound|Channel|Peninsula|Harbour|Falls|Creek|Mountains|Land|Archipelago)`
双向标记全扫，过滤 86 既有 place + 9 在队候选 + 变体/人名/假匹配后，得 **~40 新候选（≫3 门）**——
证 place 表层未穷尽。curated 18 强候选入队，长尾 ~22 个 5–6 agg 候选 hold。

## 决策矩阵

| 优先级 | 门 | 判定 | 触发? |
|--------|-----|------|-------|
| 1a | EVV5+SCN28（since_evv5 ≥ 10 且 since_discover ≥ 10）| since_evv5=8 | 否 |
| 1b | EVV5（since_evv5 ≥ 10）| =8 | 否 |
| 2 | CLOSE+SCN28（discover_streak_low ≥ 3）| =0 | 否 |
| **3** | **SCN28（queue_size < 10 或 since_discover ≥ 10）** | **queue=9 < 10** | **触发** |
| 3.5 | SCN28-corpus（since_corpus ≥ 30）| =15 | （未及）|
| 3.9 | zombie-guard（queue(place)==0）| =9 | （未及）|
| NEW1（默认）| — | — | （未及）|

## 扫描与过滤记录

**入队 18 候选**（agg=跨源聚合估值，建前须主源逐页段级严扫）：

| 候选 | 主源/源作 | distinctPN | real/fictional | 备注 |
|------|-----------|-----------|----------------|------|
| Hudson's Bay | ACH/FC/OC/TT | 水体严扫 12 | real | 排除 Hudson's Bay Company（org 既有）|
| Baffin's Bay | ACH/FC/TN/WC | 含 Sea 变体 47 | real | alias Baffin's Sea |
| Walruses' Bay | FC | 22 | fictional | Cape Bathurst 簇 |
| Caspian Sea | ASC/FWB/MS/RC/TT/TTLU | agg 14 | real | 跨作 |
| Davis's Straits | ACH | 14 | real | alias Davis Strait |
| Sandwich Islands | AM/GM/MI/SC/SI | agg 10 | real | 夏威夷旧称 |
| Norfolk Island | MI/SC/SI | agg 10 | real | — |
| Cape Tchelynskin | WC | 10 | real | 欧亚极北 |
| Cape Verde | AM/FWB/SC/TTLU | agg 9 | real | alias Verde Islands |
| Faroe Islands | JCE/TN/TTLU/WC | agg 8 | real | — |
| Fort Sumter | BR/SC2 | 8 | real | 南北战争 |
| Morris Island | BR | 10 | real | Charleston 港，接 Fort Sumter |
| Lake Ontario | MW/PL/RC | agg 7 | real | 大湖链末湖 |
| Black Sea | ASC/MS/RC/RM/SC/TT | agg 7 | real | 跨作 |
| Dream Bay | GM | 7 | fictional | Godfrey 荒岛 |
| Altamont Harbour | ACH | 6 | fictional | New America，接 victoria-bay |
| Falkland Islands | AM/MI/TTLU | agg 6 | real | 接 port-egmont |
| Lake Ukereoue | FWB | 6 | real | 维多利亚湖旧称 |

**排除项**：
- **人名/假匹配**：Ned Land（TTLU 鱼叉手，POST「Land」误匹配，agg 265）/ Port Gr（JCE 截断）/ Lake City（generic）/ Greek Islands（generic）。
- **既有页变体**：Behring's Straits→behring-strait / Baffin's Sea→Baffin's Bay alias / Cape Mandible→mandible-cape / Lancaster Sound→lancaster-strait / Isle Tabor→tabor-island / Verde Islands→Cape Verde alias。
- **严扫归零**：Rock Creek（MW 排除 black rock 后 =0，恒为既有 black-rock-creek）。
- **已在队 9**：Polar Sea/Bear Lake/Melville Island/Gallian Sea/Cape Bernouilli/Cape Horn/Rocky Mountains/Loch Malcolm/Cape Washington。

**长尾 hold（~22，5–6 agg）**：Detroit River/Navy Island/Goat Island/Niagara Falls（MW 尼亚加拉簇）、Platte River/North Sea/
Chatham Islands/Sullivan Island/Washburn Bay/Lake Barnett/Lake Tinn/Fort Independence/Coronation Gulf/Balearic Isles/
Bahama Channel/Caribbean Sea/Cape Bon/Mount Mendif/Blueridge Mountains/Cape Saknussemm/Shannon Island/Mounts Doerfel/
Indian Peninsula/Long Island/Antarctic Sea。下轮 discover 或本批消费后再评估。

## EXIT-GATE 检查

| 门 | 结果 | 问题与处置 |
|----|------|---------|
| G1 PN 有效性 | N/A | 本轮 discover，不建页 |
| G2 散文门 ≤400 | N/A | 不建页 |
| G3 schema 合规 | N/A | 不建页 |
| G4 记录完整性 | PASS | 本日志；queue.md +18 候选（9→27）；grow_state discover six-step |
| I1 type_queue ∩ closed = ∅ | PASS | [event,character] ∩ [work,org,technology] = ∅ |
| I2 current_type ∉ closed | PASS | place ∉ closed |
| I3 counters ≥ 0 | PASS | 全部 ≥0 |
| I4 grow_phase 匹配 "2.N" | PASS | "2.1" |
| I5 phase2_closed==True ⟺ phase=="3" | PASS | False / "2.1" |

## state 更新（SCN28 表层 discover）

`current_round 48→49`；`type_round 19→20`；`rounds_since_last_evv5 8→9`；
`rounds_since_last_discover 6→0`（本轮为 discover，重置）；
`discover_streak_low` 保持 0（new_candidates=18 ≫ min=3，未低产）；
`rounds_since_last_corpus_discover 15→16`（本轮为表层 SCN28，非 SCN28-corpus 深扫，corpus 计数照增）；
`last_updated_round→49`。

## 遗留问题

1. **queue(place) 27**：R47 后 9 + R48 补种 18 = 27，远超阈值 10。下批回 NEW1 消费。
   下批优选（强候选优先，建前主源段级严扫）：Baffin's Bay(47)/Walruses' Bay(22)/Hudson's Bay(12)/
   Davis's Straits(14)/Caspian Sea(agg 14)/Sandwich Islands(agg 10)。
2. **聚合 vs 主源段级 distinctPN 铁律**：本轮多数 distinctPN 为跨源聚合估值，
   Caspian/Cape Verde/Black Sea/Lake Ontario 等跨作候选主源段级可能远低于 agg——建前必逐页主源严扫，
   跌破 5 则弃或留 list。承 R43–R47 同名混淆与聚合虚高教训。
3. **同名/org 辨析**：Hudson's Bay（水体）≠ Hudson's Bay Company（org 既有页）；建页须严扫排除 Company 语境（本轮已扫水体 12）。
4. **since_evv5 达 9**：距 EVV5 门（≥10）尚 1 轮，约 R50 触发（下轮 NEW1 后 since_evv5→10，R50 落 EVV5）。
5. **since_corpus 达 16**：距 SCN28-corpus 深扫门（≥30）尚 14 轮。
6. **discover 双盲区**：本轮再证表层 SCN28 与深扫聚合各有盲区（POST「Land」匹配 Ned Land 人名、
   跨源 agg 虚高）——照旧建前逐页语义拆分，PARK 记录。
7. **两 Pilot 页 PN=4（hong-kong/snaefellsjokull）**：承 R39 EVV5，PARK。
8. **featured 虚高、add_page.py 散文门旁路、RFC-0003 VVV 宽度、Robur alias、build_wanted 空格滤、
   registry typefield 未透传、深扫聚合 distinctPN 跨源误报** 七项债务照旧 PARK/记录。
